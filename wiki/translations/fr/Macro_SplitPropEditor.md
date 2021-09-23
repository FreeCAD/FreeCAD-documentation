# Macro SplitPropEditor/fr
{{Macro
|Name=SplitPropEditor
|Icon=
|Description=Cette macro permet de séparer temporairement l'éditeur de propriétés de la vue combo vers un widget docké séparé.
|Author=OpenBrain
|Date=2019-12-27
|Version=0.63
|FCVersion= 0.17+
|Download=
|SeeAlso=
}}

## Description

### Contexte

Cette macro a été écrite car certaines opérations dans FreeCAD demandent un accès fréquent à l\'éditeur de propriétés. Sa hauteur limitée dans la vue combinée peut être un problème, en particulier lorsque l\'accès à la vue arborescente est également nécessaire en même temps. La macro résout ce problème en permettant à l\'utilisateur de diviser temporairement le widget de l\'éditeur de propriétés en un widget de dock séparé. Le widget nouvellement créé est défini à droite de la fenêtre lors de la création mais peut être déplacé (ancré ou flottant) comme tout autre widget de dock. Lorsque l\'éditeur de propriétés séparées n\'est plus nécessaire, l\'utilisateur peut fermer le widget supplémentaire et l\'éditeur de propriétés est automatiquement replacé dans la vue combinée. Notez que lorsque l\'éditeur de propriétés est détaché de la vue combinée, sa hauteur est stockée et est ensuite restaurée lorsqu\'il revient à la vue combinée. De plus, lorsque l\'éditeur de propriétés est divisé, il fournit un mécanisme de dimensionnement des polices afin que davantage de propriétés puissent être affichées.

### Utilisation

Pour diviser l\'éditeur de propriétés, exécutez simplement la macro. Lorsque la macro a été exécutée une fois dans la session, il existe différentes manières de diviser/réinitialiser l\'éditeur de propriétés:

-   Lorsque l\'éditeur de propriétés est divisé, la fermeture du widget de dock supplémentaire le réinitialisera dans la vue combinée.
-   Exécutez à nouveau la macro: à chaque exécution, la division de l\'éditeur de propriétés sera basculée. C\'est un moyen utile si vous attachez la macro à une icône personnalisée dans une barre d\'outils.
-   Double-cliquez sur le libellé de l\'onglet \'Model\' dans la vue combinée: chaque double-clic bascule la division de l\'éditeur de propriétés.
-   Allez dans Affichage-\> Panneaux et basculez le panneau \'Editeur de propriétés\'.

Lorsque l\'éditeur de propriétés est divisé dans son widget séparé, effectuez un clic du milieu de la souris sur la barre de titre du widget pour avoir accès au calibreur de polices.

### Installation

La macro est disponible via le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md). Le code est fourni sur cette page pour plus de commodité au cas où votre système n\'ait pas git-python. Bien qu\'elle devrait être à jour, la dernière version de la macro est toujours disponible sur [FreeCAD-macro repository](https://github.com/FreeCAD/FreeCAD-macros/blob/master/PureGui/SplitPropEditor.FCMacro)

Pour des explications plus détaillées, consultez la page [Comment installer une Macro](How_to_install_macros/fr.md). Notez que la macro est prête à être définie comme [une macro au démarrage](Macro_at_Startup/fr.md).

## Script

### Discussion du forum 

Pour tout commentaire (bug, demande de fonctionnalité, commentaires, \...), merci d\'utiliser ce fil de discussion: <https://forum.freecadweb.org/viewtopic.php?f=22&t=39345>

### Code

**Macro\_SplitPropEditor.FCMacro**


{{MacroCode|code=
#!/usr/bin/python
#####################################
# Copyright (c) openBrain 2019
# Licensed under LGPL v2
#
# This FreeCAD macro will split the property editor from the combo view to a new dockable widget (panel)
# * The default widget is docked to the right of the window but can be freely moved
# * When the new widget is closed, the property editor is set back to its location in the combo view
# * When the macro has been run once, the new widget is registered in FC UI and can (shall) be hidden/shown as original panels are
# * Mouse middle click on the panel title displays a temporary slider to change font size
#
# Version history :
# *0.63 : add comments in the code
# *0.62 : property edit subpanel height is recorded and restored
# *0.61 : property editor split is toggles when 'Model' tab label is double clicked in Combo View
# *0.6 : improve behavior of macro so it toggles property editor split at each run
# *0.52 : stop timer when no more needed
# *0.51 : fix issue when separate Property View is enabled
# *0.5 : beta release
#
#####################################

__Name__ = 'SplitPropEditor'
__Comment__ = 'Splits the property editor from the combo view to a new dock widget (panel)'
__Author__ = 'openBrain'
__Version__ = '0.63'
__Date__ = '2019-12-27'
__License__ = 'LGPL v2'
__Web__ = 'https://www.freecadweb.org/wiki/Macro_SplitPropEditor'
__Wiki__ = 'https://www.freecadweb.org/wiki/Macro_SplitPropEditor'
__Icon__ = ''
__Help__ = 'Run macro once to create the new property editor panel'
__Status__ = 'Beta'
__Requires__ = 'FreeCAD >= 0.17'
__Communication__ = 'https://forum.freecadweb.org/viewtopic.php?f=22&t=39345'

### Perform needed imports
from PySide import QtCore, QtGui
import FreeCAD as App
import FreeCADGui as Gui

### Define a custom QDockWidget class
class PropEditor(QtGui.QDockWidget):

    def __init__(self):
        mw = Gui.getMainWindow() 
        pt = mw.findChild(QtGui.QWidget,'Combo View').findChild(QtGui.QWidget, 'propertyTab') # look for the property editor
        if not pt:
            raise Exception("Can't find property editor widget, exiting") 
        self.ptWid = pt.parent() # find property editor widget
        self.oldParent = pt.parent().parent() # find property editor parent (is a QSplitter)
        self.oldIndex = self.oldParent.indexOf(self.ptWid) # store index of property editor in the QSplitter
        self.font = QtGui.QFont(pt.font()) # store current font
        super(PropEditor, self).__init__() # run inherited class constructor
        self.setParent(mw)
        self.setObjectName("PropEdit")
        self.setWindowTitle("Property Editor")
        ### create a custom title bar widget so font can be sized when property editor is split
        self.titleWid = QtGui.QWidget()
        lay = QtGui.QHBoxLayout()
        self.fs = QtGui.QSlider(QtCore.Qt.Horizontal) # slider to size font
        oldPs = self.font.pointSize()
        self.fs.setSliderPosition(oldPs) # set default slider position
        self.fs.setMaximum(oldPs) # maximum font size is default one
        self.fs.setMinimum(int(oldPs/2+1)) # minimum font size is almost half the default one
        self.fs.setPageStep(1) # needed so mouse wheel step is 1
        self.fs.valueChanged.connect(self.changeFs)
        self.fs.sliderReleased.connect(self.changeFs) # needed to manage font sizer hiding when slider is held by user
        lay.addWidget(QtGui.QLabel("Size : "))
        lay.addWidget(self.fs)
        self.titleWid.setLayout(lay)
        self.timer = QtCore.QTimer(self) # set a timer so font sizer is hidden after some time
        self.timer.setInterval(2500)
        self.timer.timeout.connect(self.titleBarTo)
        ### connect to 'Model' tab label double-clicking to toggle split
        self.tb = mw.findChild(QtGui.QWidget,'Combo View').findChild(QtGui.QWidget, 'combiTab')
        self.tb.tabBarDoubleClicked.connect(self.toggleVisibility)

    def changeFs(self, fs=0): # called when font sizer slider is moved
        self.timer.start() # restart timeout timer
        if fs != 0:
            self.font.setPointSize(fs) # compute new font ...
            self.ptWid.setFont(self.font) # ... then apply

    def showEvent(self, event): # called when custom dock widget is shown
        self.ptHeight=self.oldParent.sizes() # record property editor height (handled at QSplitter to prevent opaque resizing)
        self.setWidget(self.ptWid) # transfer property editor widget to custom dock widget
        self.ptWid.setFont(self.font) # apply custom font size

    def hideEvent(self, event): # called when custom dock widget is hidden
        self.oldParent.insertWidget(self.oldIndex, self.ptWid) # reset property editor widget to combo view
        self.oldParent.setSizes(self.ptHeight) # restore property editor height
        self.ptWid.setFont(QtGui.QFont()) # restore default font of combo view

    def mousePressEvent(self, event): # called when mouse is pressed on the custom dock widget
        if event.button() == QtCore.Qt.MouseButton.MidButton: # if button is middle one
            self.setTitleBarWidget(self.titleWid) # show the font sizer in the title bar
            self.timer.start() # start timeout timer

    def titleBarTo(self): # called when timeout timer expires
        if not self.fs.isSliderDown(): # if slider is no more held by user
            self.resetTitleBar() # reset title bar

    def resetTitleBar(self):
        self.setTitleBarWidget(None) # set title bar to 'None' so it get back its default aspect
        self.timer.stop() # stop timeout timer

    def toggleVisibility(self, index = -2): # called to toggle property editor split ...
    # ... 'index' is needed when used as slot for 'Model' tab double-click ...
    # ... '-2' value can't be sent by signal so we know its a 'manual' call
        if index == -2 or self.tb.tabText(index).replace('&','') == 'Model': # if manual call or double-click on 'Model' tab label
            self.setVisible(self.isHidden()) # toggle custom dock widget visibility (behavior handled by show/hide events)

def run() : # define main function
    pe = Gui.getMainWindow().findChild(QtGui.QWidget, 'PropEdit') # check if a custom property editor dock widget already exist
    if not pe: # if doesn't exist yet
        Gui.getMainWindow().addDockWidget(QtCore.Qt.RightDockWidgetArea, PropEditor()) # create it
    else: # if already exists
        pe.toggleVisibility() # toggle property editor split

if __name__ == '__main__': # if macro called to run
    run()
}}

---
[documentation index](../README.md) > Macro SplitPropEditor/fr
