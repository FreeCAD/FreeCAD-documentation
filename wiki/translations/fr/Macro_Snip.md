# Macro Snip/fr
{{Macro/fr
|Name=Macro Snip
|Icon=Snip.png
|Description=Utilisez cette macro pour poster facilement des captures d’écran sur le forum FreeCAD.<br/>Il est préférable d’ajouter cette macro à votre barre d’outils de macros personnalisées globales pour un accès rapide et facile.<br/>Lors de la publication sur le forum FreeCAD, il est souvent utile d'être en mesure d'inclure des captures d'écran. Le problème est que c'est une tâche un peu fastidieuse. Cette macro facilite un peu la tâche.<br/>La macro peut prendre des captures d’écran ou utiliser des captures d’écran existantes déjà copiées dans le Presse-papiers du système. Pour ignorer l'image déjà dans le presse-papiers, appuyez sur la touche Maj tout en appelant la macro. Pour utiliser la macro afin de prendre la capture d'écran, ajustez la taille et l'emplacement de la boîte de dialogue qui apparaît, puis cliquez sur OK. En cliquant sur OK, la macro tentera de prendre une capture d'écran de la zone de l'écran couverte par la boîte de dialogue. La boîte de dialogue elle-même est semi-transparente, vous pouvez donc voir le contenu ci-dessous.
|Author=TheMarkster
|Version=1.22
|Date=2022.02.23
|FCVersion=Tous
|Download=[https://wiki.freecadweb.org/images/a/a0/Snip.png Icône de la barre d'outils]
|SeeAlso=[Macro Copy3DViewToClipboard](Macro_Copy3DViewToClipboard/fr.md), [Macro Screen Wiki](Macro_Screen_Wiki/fr.md)
|Shortcut=Sur Windows: Windows Key + Shift + S<br/>
Sur Mac: Command + Shift + 4<br/>
Sur Linux: gnone-screenshot utility<br/>
}}

## Description

Utilisez cette macro pour poster facilement des captures d'écran sur le [forum FreeCAD](https://forum.freecadweb.org).

Il est préférable d'ajouter cette macro à votre barre d'outils de macros personnalisées globales pour un accès rapide et facile.

Lors de la publication sur le forum FreeCAD, il est souvent utile de: être en mesure d\'inclure des captures d\'écran. Le problème est que c\'est une tâche un peu fastidieuse. Cette macro vise donc à faciliter un peu cette tâche.

## Utilisation

La macro peut prendre des captures d'écran ou utiliser des captures d'écran existantes déjà copiées dans le Presse-papiers du système. Pour ignorer l\'image déjà dans le presse-papiers, appuyez sur la touche **Maj** tout en appelant la macro. Pour utiliser la macro afin de prendre la capture d\'écran, ajustez la taille et l\'emplacement de la boîte de dialogue qui apparaît, puis cliquez sur **OK**. En cliquant sur **OK**, la macro tentera de prendre une capture d\'écran de la zone de l\'écran couverte par la boîte de dialogue. La boîte de dialogue elle-même est semi-transparente, vous pouvez donc voir le contenu ci-dessous.

<img alt="" src=images/Snip-Screenshot1.png  style="width:600px;"> 
*Snip screenshot1,  Remarquez comment le dialogue est semi-transparent. Seul le contenu de l'écran situé sous la boîte de dialogue sera capturé..*

Après avoir cliqué sur **OK**, la macro prend ensuite la capture d\'écran et l\'enregistre dans un fichier temporaire. Une boîte de dialogue d'ouverture de fichier s'ouvre alors à l'emplacement du fichier. Vous pouvez glisser-déposer le fichier de là vers le forum dans la zone de texte où vous tapez le texte de votre message. Lors de l\'annulation de la boîte de dialogue, le fichier de capture d\'écran temporaire est automatiquement supprimé. Vous pouvez également ouvrir le fichier de capture d\'écran dans votre application par défaut installée pour ouvrir les fichiers {{FileName|.png}} (sous Windows, il s'agit généralement de Paint). Cela peut être utile si vous souhaitez ajouter des annotations à la capture d\'écran ou éventuellement des modifications supplémentaires, telles que le rognage.

<img alt="" src=images/Snip-Screenshot2.png  style="width:600px;"> 
*Snip screenshot2, Ceci est la boîte de dialogue d'ouverture de fichier qui apparaît automatiquement après la capture d'écran. L'image peut être glissée et déposée sur le forum ou elle peut être ouverte pour un traitement ultérieur dans votre application système par défaut pour l'ouverture de fichiers png. Vous pouvez également cliquer sur l'image avec le bouton droit de la souris et l'ouvrir **Open with..* avec une autre application de votre choix.**

Si la macro ne fonctionne pas sur votre système pour capturer des captures d\'écran, elle peut toujours être utile pour les captures que vous avez capturées à l\'aide d\'autres outils. Copiez simplement la capture d\'écran dans le presse-papiers, puis exécutez la macro. Il créera le fichier temporaire et ouvrira le répertoire du fichier dans une boîte de dialogue d\'ouverture de fichier pour vous. Quelques autres outils pour prendre des screenshots:

:   Sur Windows: Touche Windows + **Shift** + **S**
:   Sur Mac: **Command** + **Shift** + **4**
:   Sur Linux: utilitaire gnome-screenshot

## Paramètres

La macro prend en charge les paramètres utilisateur qui peuvent être définis à l\'aide de **Outils → Editer paramètres... → Plugins → Snip_Macro**

:   
    `LastX`, `LastY`, `LastWidth`, `LastHeight`: emplacement et taille de la dernière utilisation de la zone de capture

:   
    `WindowOpacity`(0.85): une valeur entre 0,0 (moins opaque) et 1,0 (plus opaque)

:   
    `SnipDelay`(0.5): délai (en secondes) entre la fermeture de la zone de capture et la capture

:   
    `DesiredWidth`(0): largeur souhaitée (en pixels), ignorée si 0 \-- redimensionne l\'image à votre convenance en conservant le rapport hauteur/largeur actuel

:   
    `ScaleFactor`(1.0): facteur d\'échelle souhaité, (remplace DesiredWidth si ScaleFactor n\'est pas 1.0) \-- met l\'image à l\'échelle au facteur d\'échelle

Les paramètres `Last` sont réinitialisés par la macro à chaque exécution. Ainsi la macro garde une trace de l\'endroit où placer la boîte de sélection, à la dernière position qu\'elle avait quand l\'utilisateur a pris une capture d\'écran.

Le paramètre `WindowOpacity` est l\'opacité de la zone de capture.

Le paramètre `SnipDelay` peut être ajusté pour accélérer un peu les choses mais si la valeur est trop petite, la capture d\'écran prise peut inclure la boîte snip elle-même. Il faut un certain temps pour fermer la boîte de dialogue avant de prendre le capture d\'écran.

Le paramètre `DesiredWidth` met l\'image à l\'échelle à la largeur souhaitée, sauf s\'il est égal à 0 (valeur par défaut), auquel cas aucune mise à l\'échelle n\'est effectuée. Par exemple, si vous définissez la largeur souhaitée sur 800, vous obtiendrez des images d\'une largeur de 800 pixels. La hauteur sera automatiquement mise à l\'échelle pour conserver le rapport hauteur/largeur actuel. Si l\'image d\'origine était de 1600x1200 et que la largeur désirée est de 800, l\'image résultante sera de 800x600.

Le paramètre `ScaleFactor` met l\'image à l\'échelle selon le rapport souhaité, par ex. 0.5. La valeur par défaut est 1.0, auquel cas aucune mise à l\'échelle n\'est effectuée. Cela remplace le paramètre DesiredWidth si ScaleFactor n\'est pas 1.0.

Vous pouvez contourner toute mise à l\'échelle en maintenant la touche Ctrl enfoncée tout en cliquant sur le bouton OK pour prendre la capture d\'écran.

## Script

Icône de la barre d\'outils ![](images/Snip.png )

**Macro\_Snip.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
"""
***************************************************************************
*   Copyright (c) 2019 <TheMarkster>                                 *
*                                                                         *
*   This file is a supplement to the FreeCAD CAx development system.      *
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU Lesser General Public License (LGPL)    *
*   as published by the Free Software Foundation; either version 2 of     *
*   the License, or (at your option) any later version.                   *
*                                                                         *
*   This software is distributed in the hope that it will be useful,      *
*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
*   GNU Library General Public License at http://www.gnu.org/licenses     *
*   for more details.                                                     *
*                                                                         *
*   For more information about the GNU Library General Public License     *
*   write to the Free Software Foundation, Inc., 59 Temple Place,         *
*   Suite 330, Boston, MA  02111-1307 USA                                 *
*                                                                         *
***************************************************************************
"""



"""
Snip Macro

This is a macro to make it easier to post screenshots to the FreeCAD forum.

The forum supports a drag and drop interface -- just drag and drop an image to the
textarea where you type in your post.  But it still requires many
tedious steps.  This macro is to reduce some of those steps.

You should add the macro to your custom macro toolbar to save as many clicks as possible.

The first thing the macro does is to check if there is an image already saved to the 
system clipboard, and if so, it uses that one.  To bypass the clipboard, press Shift
while invoking the macro.

"""

__title__ = "Snip"
__author__ = "TheMarkster"
__url__ = ""
__Wiki__ = ""
__date__ = "2022.02.23"
__version__ = 1.22
import FreeCAD
from PySide import QtGui,QtCore
import uuid
import time
import tempfile, os, shutil

class SnipBox(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.detailsTextEdit = QtGui.QTextEdit("Details")
        self.Details = QtGui.QPushButton("Details")
        self.Details.clicked.connect(self.onDetailsClicked)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.detailsTextEdit)
        layout.addStretch()
        buttons = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok,
            QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        buttons.addButton(self.Details, QtGui.QDialogButtonBox.ActionRole)
        buttons.setCenterButtons(True)
        layout.addWidget(buttons)
        self.setLayout(layout)
        self.detailsTextEdit.setVisible(False)

    def setDetailedText(self, txt):
        self.detailsTextEdit.setText(txt)

    def onDetailsClicked(self):
        self.detailsTextEdit.setVisible(not self.detailsTextEdit.isVisible())

    def event(self, e): #credit serge_gubenko of stackoverflow for this
        result = QtGui.QDialog.event(self, e)
        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setMinimumWidth(0)
        self.setMaximumWidth(16777215)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        textEdit = self.findChild(QtGui.QTextEdit)
        if textEdit != None :
            textEdit.setMinimumHeight(0)
            textEdit.setMaximumHeight(16777215)
            textEdit.setMinimumWidth(0)
            textEdit.setMaximumWidth(16777215)
            textEdit.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
#thanks to mario52 for this
        if result == True:
            try:
                rect = mb.frameGeometry()
                rectwidth  = rect.width()
                rectheight = rect.height()
                mb.setWindowTitle("Snip macro v"+str(__version__)+"  "+str(rectwidth)+" x "+str(rectheight))
            except Exception:
                None
##############
        return result
pg = FreeCAD.ParamGet("User parameter:Plugins/Snip_Macro")
#parameters were originally in BaseApp, but should be in Plugins, so relocate if necessary
if FreeCAD.ParamGet("User parameter:BaseApp/Preferences").HasGroup("Snip_Macro"):
    deprecated = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Snip_Macro")
    pg.SetInt("LastX",deprecated.GetInt("LastX",0))
    pg.SetInt("LastY",deprecated.GetInt("LastY",0))
    pg.SetInt("LastWidth",deprecated.GetInt("LastWidth",0))
    pg.SetInt("LastHeight",deprecated.GetInt("LastHeight",0))
    pg.SetFloat("WindowOpacity",deprecated.GetFloat("WindowOpacity",0.85))
    pg.SetFloat("SnipDelay",deprecated.GetFloat("SnipDelay",0.5))
    FreeCAD.ParamGet("User parameter:BaseApp/Preferences").RemGroup("Snip_Macro")

desired_width = pg.GetInt("DesiredWidth",0) #used for scaling to desired width, maintaining aspect ratio
pg.SetInt("DesiredWidth", desired_width)
scale_factor = pg.GetFloat("ScaleFactor", 1.0) #scale by scale factor instead of desired width
pg.SetFloat("ScaleFactor", scale_factor)

skipClipboard = False
modifiers = QtGui.QApplication.keyboardModifiers()
if modifiers == QtCore.Qt.ShiftModifier:
    skipClipboard = True

userCanceled = False
fname = "Snip macro screenshot-"+str(uuid.uuid4())[:6]+".png"
image = None
if not skipClipboard:
    clip = QtGui.QClipboard()
    image = clip.image(QtGui.QClipboard.Clipboard)
if not image:

    #use our own screen grabber
    mb = SnipBox()     
    details = """
Move and resize this box to cover the part of the screen you wish to grab.
If it succeeds an open file dialog will appear.  Drag and drop the file
from the open file dialog to the forum.  The file will be deleted after
you close the dialog.

If this fails you can still use this macro to handle screenshots you
copied to the clipboard using other tools:

Windows snip tool: Window Key + Shift + S
Mac snip tool: Command + Shift + 4
Linux: gnome-screenshot utility

If the macro finds there is already an image copied to the clipboard 
it uses that image instead of bringing up this dialog.  Press Shift
while invoking this macro to bypass the clipboard.  Alternatively,
you can clear the image from the clipboard by copying some text to it.

The Open button will open the file in the system
default application for handling png files, e.g. Paint in windows.  This
can be useful if you wish to annotate the screenshot.  But most of the
time you will simply want to drag and drop the file to the forum, then
Cancel to close the open file dialog afterwards.

If you wish to open the screenshot file with another application, right-click
the file and select open with... option or drag/drop to that other application.

User Parameters: These can be accessed via Tools menu -> Edit Parameters in 
Plugins -> Snip_Macro:

LastX, LastY, LastWidth, LastHeight -- location and size of snip box last use
WindowOpacity (0.85) -- value between 0.0 (less opaque) and 1.0 (more opaque)
SnipDelay (0.5) -- time (in seconds) delay between snip box close and snip
DesiredWidth -- image will be scaled to this width (unless it is 0) maintaining
current aspect ratio.
ScaleFactor -- float value, e.g. 0.5 -- image will be scaled to that scale factor.
Note: ScaleFactor (if not 1.0) will take precedence over DesiredWidth
Hold down Ctrl key to ignore scaling.

The SnipDelay parameter can be adjusted to speed things up a bit, but if it 
is too small the screenshot taken might include the snip box itself because
we need to wait for it to close before taking the screenshot.

"""
    mb.setWindowTitle("Snip macro v"+str(__version__))
    mb.setDetailedText(details)
    if pg.GetFloat("WindowOpacity",0.85) == 0.85:
        pg.SetFloat("WindowOpacity",0.85)
    mb.setWindowOpacity(pg.GetFloat("WindowOpacity",0.85))
    lastX = pg.GetInt("LastX",0)
    lastY = pg.GetInt("LastY",0)
    lastWidth = pg.GetInt("LastWidth",100)
    lastHeight = pg.GetInt("LastHeight",100)
    mb.setGeometry(lastX, lastY, lastWidth, lastHeight)
    mb.resize(lastWidth, lastHeight)
    mb.setWindowFlags(QtCore.Qt.Tool)
    result = mb.exec_()
    if not result:
        userCanceled = True
    if not userCanceled:
        clientRect = mb.geometry()
        rect = mb.frameGeometry()
        diff = rect.height()-clientRect.height()
        pg.SetInt("LastX", rect.x())
        pg.SetInt("LastY", rect.y())
        pg.SetInt("LastWidth", rect.width())
        pg.SetInt("LastHeight", rect.height()-diff)
        QtGui.QApplication.processEvents()
        snipDelay = pg.GetFloat("SnipDelay", 0.5)
        if snipDelay == 0.5:
            pg.SetFloat("SnipDelay", 0.5)
        time.sleep(snipDelay) #give time for dialog to close before taking screenshot
        QtGui.QApplication.processEvents()
        if hasattr(QtGui.QApplication,"primaryScreen"):
            screen = QtGui.QApplication.primaryScreen()
            image = screen.grabWindow(0,rect.x(),rect.y(),rect.width(),rect.height()).toImage()
        else:
            long_qdesktop_id = QtGui.QApplication.desktop().winId()
            image = QtGui.QPixmap.grabWindow(long_qdesktop_id, rect.x(), rect.y(), rect.width(), rect.height()).toImage()
        if not image:
            raise Exception("Snip Macro Error: Unable to grab screen image\n")
        modifiers = QtGui.QApplication.keyboardModifiers()
        skipScaling = False
        if modifiers == QtCore.Qt.ControlModifier:
            skipScaling = True
        if not skipScaling:
            if scale_factor != 1.0:
                #image = image.scaledToWidth(rect.width()*scale_factor)
                image = image.smoothScaled(rect.width()*scale_factor, rect.height()*scale_factor)
            elif desired_width != 0:
                #image = image.scaledToWidth(desired_width)
                image = image.smoothScaled(desired_width, rect.height()*float(desired_width)/float(rect.width()))

if not userCanceled:
    dirPath = tempfile.mkdtemp()
    filePath = dirPath + os.path.sep + fname
    image.save(filePath)
    fileName = QtGui.QFileDialog.getOpenFileName(QtGui.QApplication.activeWindow(),
    "Drag the image to the forum, then Cancel will delete the temporary file", dirPath, "PNG (*.png)")
    if fileName[0]:  #user selected Open or double-clicked file
        import subprocess, os, platform
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', fileName[0]))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(fileName[0])
        else:                                   # linux variants
            subprocess.call(('xdg-open', fileName[0]))
        QtGui.QApplication.processEvents() #allow some time for file to open before deleting temp folder and contents
        time.sleep(1)
        QtGui.QApplication.processEvents()
    shutil.rmtree(dirPath)
}}

## Lien

La discussion sur le forum [Snip macro](https://forum.freecadweb.org/viewtopic.php?f=9&t=38328&sid=385bf3174dcae7fb8bdf529f4e76dfed)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Snip/fr
