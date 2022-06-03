# Macro SketchUnmap/fr
{{Macro/fr
|Name=SketchUnmap
|Description=Cette macro réinitialise un emplacement absolu de l’esquisse et crée éventuellement un plan de référence.<br/>Cette macro a été écrite principalement pour contourner le problème de dénomination topologique susceptible de casser un modèle lorsqu'une esquisse a été attachée directement ou indirectement à une face ou à un objet. tout autre élément topologique.<br/>
Pour éviter les ruptures, une macro doit être appliquée lorsque le modèle est toujours correct. Il ne peut pas "réparer" un modèle cassé. Si vous venez de casser votre modèle, annulez les dernières modifications dans une bonne situation, appliquez la macro aux esquisses instables, puis recommencez l'opération précédente.
|Icon=SketchUnmap.svg
|Author=OpenBrain
|Date=2019-06-14
|Version=0.6.2
|FCVersion= 0.17+
|Download= [https   *//www.freecadweb.org/wiki/images/3/34/SketchUnmap.svg ToolBar Icon]
}}

## Description

### Contexte

Cette macro a été écrite principalement pour contourner le problème de dénomination topologique susceptible de casser un modèle lorsqu\'une esquisse a été directement ou indirectement attachée à une face ou à tout autre élément topologique. Pour éviter les ruptures, une macro doit être appliquée lorsque le modèle est toujours correct. Il ne peut pas \"réparer\" un modèle cassé. Si vous venez de casser votre modèle, annulez les dernières modifications dans une bonne situation, appliquez la macro aux esquisses instables, puis recommencez l\'opération précédente.

### Utilisation

Sur le plan fonctionnel, la macro supprimera le mappage actuel de l\'esquisse sur laquelle elle est appliquée, puis lui appliquera un placement absolu afin de l\'immuniser contre les modifications de support de mappage.

Pour ce faire, la macro proposera essentiellement 3 options (si votre esquisse n\'est pas dans un corps PartDesign, seule la première option est disponible et sera appliquée automatiquement)   *

-   Mode \"Raw\" =\> le placement de l\'esquisse est rendu absolu dans le référentiel de corps, rien de plus
-   \"Mode DP\@Face\" =\> un plan de référence est créé à l\'emplacement de la face de mappage, puis l\'esquisse y est attachée en respectant son décalage d\'attache
-   Mode \"DP\@Sketch\" =\> un lieu de référence est créé à l\'emplacement de l\'esquisse (y compris le décalage de la pièce jointe), puis l\'esquisse est attachée à son origine

Pour utiliser la macro, sélectionnez simplement l\'esquisse cible (par exemple, dans l\'arborescence), puis exécutez la macro. C\'est tout !

### Installation

La macro est disponible via le [gestionnaire d\'extensions](Std_AddonMgr/fr.md). Le code est fourni sur cette page pour plus de commodité au cas où votre système n\'ait pas git-python. Bien qu\'elle devrait être à jour, la dernière version de la macro est toujours disponible sur [FreeCAD-macro repository](https   *//github.com/FreeCAD/FreeCAD-macros/blob/master/Information/SimpleProperties.FCMacro)

Pour des explications plus détaillées, voir la page [ Comment installer des macros](How_to_install_macros/fr.md).

### Détails

Pour une meilleure compréhension, voici un exemple   * Supposons un simple cube dont la face supérieure (jaune) a été dessinée. Un cylindre est créé avec un cercle matelassé dont l\'esquisse a été mappée (face plate) à la face préparée et décalée pour répondre aux besoins (offset de pièce jointe)   *

![](images/Unmap_ex1.png )

Maintenant, pour une raison quelconque, vous devez inverser la direction de tirage du tirage (bien sûr, sans que le cylindre se déplace). Voici ce qui se passe fondamentalement   *

![](images/Unmap_ex2.png )

L\'arborescence indique une erreur, la vue 3D n\'est pas mise à jour et l\'esquisse du cercle flotte au milieu de nulle part \...

Vient maintenant le travail de la macro (que vous devez exécuter avant de changer la face de référence, lorsque l\'esquisse est toujours à la bonne place). Sélectionnez l\'esquisse et exécutez-le. Si votre esquisse est dans un corps, une boîte de message vous demandera de choisir parmi les 3 options différentes (si votre esquisse sort d'un corps, elle appliquera automatiquement la première)   *

-   \"Raw\" mode
-   \"DP\@Face mode\"
-   \"DP\@Sketch\" mode

Ce qui en terme d\'image donne ce qui suit   *

![](images/Unmap_macro.png )

## Script

ToolBar Icon ![](images/SketchUnmap.svg )

**Macro\_SketchUnmap.FCMacro**


{{MacroCode|code=
#!/usr/bin/python
#####################################
# Copyright (c) openBrain 2019
# Licensed under LGPL v2
#
# This FreeCAD macro will unmap a sketch from eg. a face and make its placement absolute in the body. It proposes 3 options (forcely the first if sketch not in a body)    *
# * "Raw" mode => the sketch placement is made absolute in the body referential, nothing more
# * "DP@Face mode" => a datum plane is created where the mapping face is, then the sketch is attached to it respecting its attachment offset
# * "DP@Sketch" mode => a datum place is created where the sketch is (including attachment offset), then the sketch is attached to its origin
#
# Main use of the macro is to make design more robust to topological naming issue
#
# Version history    *
# *0.6.2    * add icon (metadata)
# *0.6.1    * minor changes after PR review
# *0.6    * some typo improvement + commenting for official PR
# *0.5    * beta release
#
#####################################

__Name__ = 'SketchUnmap'
__Comment__ = 'Unmap a sketch & makes its placement absolute"'
__Author__ = 'openBrain'
__Version__ = '0.6.2'
__Date__ = '2019-06-14'
__License__ = 'LGPL v2'
__Web__ = 'https   *//www.freecadweb.org/wiki/Macro_SketchUnmap'
__Wiki__ = 'https   *//www.freecadweb.org/wiki/Macro_SketchUnmap'
__Icon__ = 'SketchUnmap.svg'
__Help__ = 'Select the sketch to unmap (eg. in the tree view) then run the macro'
__Status__ = 'Beta'
__Requires__ = 'FreeCAD >= 0.17'
__Communication__ = 'https   *//forum.freecadweb.org/viewtopic.php?f=22&t=36078'
#    __Files__ = ''

__dbg__ = False  #True for debugging

from PySide import QtGui

def cslM(msg)   * #Print message in console
    FreeCAD.Console.PrintMessage('\n')
    FreeCAD.Console.PrintMessage(msg)

def cslW(msg)   * #Print warning in console
    FreeCAD.Console.PrintMessage('\n')
    FreeCAD.Console.PrintWarning(msg)

def cslE(msg)   * #Print error in console
    FreeCAD.Console.PrintMessage('\n')
    FreeCAD.Console.PrintError(msg)

def cslD(msg)   * #Print debug message in console
    if __dbg__   *
        FreeCAD.Console.PrintMessage('\n')
        FreeCAD.Console.PrintMessage("Debug    * " + str(msg))

_0Vec_ = FreeCAD.Vector(0, 0, 0) #Shortener for null vector
_ZVec_ = FreeCAD.Vector(0, 0, 1) #Shortener for Z axis

if __dbg__   *  ##Clear report view in debug mode
    FreeCADGui.getMainWindow().findChild(QtGui.QTextEdit, "Report view").clear()

cslM("Starting SketchUnmap macro")
cslD("Checking selection")

##If selection is wrong, print error message and exit
if (len(Gui.Selection.getSelection()) != 1 or str(Gui.Selection.getSelection()[0]) != '<Sketcher   *   *SketchObject>')   *
    cslE("You must select a sketch that you want to unmap (and only one) ... Exiting")
else   *
    cslD("Selection OK")
    App.ActiveDocument.openTransaction("SketchUnmap") #Open transaction for undo management
    sk = Gui.Selection.getSelection()[0] #Get target sketch
    skNatPl = sk.Placement #Store placement
    skNatAO = sk.AttachmentOffset #Store attachment offset
    skInBody = False
    for obj in sk.InList   * ##Check if sketch is inside a Body
        if obj.TypeId == 'PartDesign   *   *Body'   *
            skInBody = True
            skBody = obj
    cslD("Sketch in a body    * " + str(skInBody))
    msgb = QtGui.QMessageBox() ##Prepare the message box to choose option
    msgb.setWindowTitle("Unmap Sketch    * Mode selection")
    msgb.setText("""Choose which unmapping mode you want to apply    *
    Raw => the sketch placement is made absolute in the body referential, nothing more
    DP@Face => a datum plane is created where the mapping face is, then the sketch is attached to it respecting its attachment offset
    DP@Sketch => a datum place is created where the sketch is (including attachment offset), then the sketch is attached to its origin
        Click 'Cancel' to cancel operation""")
    msgb.setIcon(QtGui.QMessageBox.Question)
    rbut = msgb.addButton("Raw", QtGui.QMessageBox.AcceptRole)
    fbut = msgb.addButton("DP@Face", QtGui.QMessageBox.AcceptRole)
    sbut = msgb.addButton("DP@Sketch", QtGui.QMessageBox.AcceptRole)
    cbut = msgb.addButton("Cancel", QtGui.QMessageBox.RejectRole)
    if skInBody   * #If sketch in a Body
        msgb.exec_() ##Show message box and get user choice
        msgbRep = msgb.clickedButton()
    else   *
        msgbRep = rbut #Else apply raw mode automatically
    if msgbRep == rbut   * #If raw mode
        sk.Support = None ##Just unmap the sketch so its placement is absolute
        sk.MapMode = 'Deactivated'
    elif msgbRep == fbut   * #If DP@Face mode
        newDP = skBody.newObject('PartDesign   *   *Plane','DP' + sk.Name) #Create a datum plane
        if sk.Label != sk.Name   * ##Eventually clarify its label
            newDP.Label = 'DP' + sk.Label
        newDP.Support = None ##Plane is placed absolute
        newDP.MapMode = 'Deactivated'
        newDP.Placement = skNatPl.multiply(skNatAO.inverse()) #Plane placement is set to former face one
        sk.Support = [(newDP,'')] #Sketch is mapped to plane keeping its attachment offset
    elif  msgbRep == sbut   * #If DP@Sketch mode
        newDP = skBody.newObject('PartDesign   *   *Plane','DP' + sk.Name) #Create a datum plane
        if sk.Label != sk.Name   * ##Eventually clarify its label
            newDP.Label = 'DP' + sk.Label
        newDP.Support = None ##Plane is placed absolute
        newDP.MapMode = 'Deactivated'
        newDP.Placement = skNatPl #Plane placement is set to former sketch one
        sk.Support = [(newDP,'')] ##Sketch is mapped to plane resetting its attachment offset
        sk.AttachmentOffset = App.Placement(_0Vec_, App.Rotation(_ZVec_, 0))
    App.ActiveDocument.commitTransaction() #Commit transaction for undo management
    cslM("SketchUnmap Macro ended correctly")
}}

### Limitations

-   Ne traitez qu\'un croquis à la fois
-   Travaillez uniquement sur des objets d\'esquisse

### Discussion sur le forum 

Pour tout commentaire (bug, demande de fonctionnalité, commentaires, \...), veuillez utiliser ce fil de discussion    * [(FR) macro to remap sketch to different reference](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=36078)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro SketchUnmap/fr
