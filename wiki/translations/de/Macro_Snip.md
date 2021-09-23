# Macro Snip/de
{{Macro/de
|Name=Schnitt
|Icon=Snip.png
|Description=Verwende dieses Makro, um Bildschirmfotos im FreeCAD-Forum zu veröffentlichen.<br/> Am besten füge dieses Makro zu deiner globalen benutzerdefinierten Makro-Werkzeugleiste hinzu, damit du schnell und einfach darauf zugreifen kannst.<br/> Wenn du im FreeCAD-Forum veröffentlichst, ist es oft nützlich, Bildschirmfotos einbinden zu können. Das Problem ist, dass dies eine etwas mühsame Aufgabe ist. Dieses Makro soll diese Aufgabe etwas erleichtern.<br/>Das Makro kann Bildschirmfotos machen oder es kann vorhandene Bildschirmfotos verwenden, die bereits in die Zwischenablage des Systems kopiert wurden. Um das bereits in der Zwischenablage befindliche Bild zu umgehen, drücke die Umschalttaste, während du das Makro aufrufst. Um das Makro zur Aufnahme des Bildschirmfotos zu verwenden, passe die Größe und Platzierung des eingeblendeten Dialogfelds an, und klicke dann auf OK. Wenn du auf OK klickst, versucht das Makro, ein Bildschirmfoto des vom Dialogfeld abgedeckten Bildschirmbereichs zu erstellen. Das Dialogfeld selbst ist halbtransparent, so dass du den Inhalt darunter sehen kannst. 
|Author=TheMarkster
|Version=1.21
|Date=19.10.2020
|FCVersion=Alle
|Download=[https://wiki.freecadweb.org/images/a/a0/Snip.png ToolBar Icon]
|SeeAlso=[Macro Copy3DViewToClipboard](Macro_Copy3DViewToClipboard.md) <img src="images/Macro_Copy3DViewToClipboard.png" width=24px><br/>[Macro Screen Wiki](Macro_Screen_Wiki.md) <img src="images/Macro_Screen_Wiki.png" width=24px>
|Shortcut=Unter Windows: Windows Key + Shift + S<br/>
Unter Mac: Command + Shift + 4<br/>
Unter Linux: gnone-screenshot utility<br/>
}}

## Beschreibung

Verwende dieses Makro, um Bildschirmfotos auf einfache Weise im [FreeCAD Forum](https://forum.freecadweb.org) zu veröffentlichen.

Am besten füge dieses Makro zu deiner globalen benutzerdefinierten Makro Werkzeugleiste hinzu, damit du schnell und einfach darauf zugreifen kannst.

Beim Veröffentlichen im FreeCAD Forum ist es oft nützlich, Bildschirmfotos beifügen zu können. Das Problem ist, dass dies eine etwas mühsame Aufgabe ist. Dieses Makro soll diese Aufgabe daher etwas erleichtern.

## Anwendung

Das Makro kann Bildschirmfotos erstellen oder vorhandene Bildschirmfotos verwenden, die bereits in die Zwischenablage des Systems kopiert wurden. Um das bereits in der Zwischenablage befindliche Bild zu umgehen, drücke die Taste **Umschalten**, während du das Makro aufrufst. Um das Makro zur Aufnahme des Bildschirmfotos zu verwenden, passe die Größe und Platzierung des eingeblendeten Dialogfelds an und klicke dann auf **OK**. Wenn du auf **OK** klickst, versucht das Makro, ein Bildschirmfoto des vom Dialogfeld abgedeckten Bildschirmbereichs zu erstellen. Das Dialogfeld selbst ist halbtransparent, so dass du den Inhalt darunter sehen kannst.

<img alt="" src=images/Snip-Screenshot1.png  style="width:600px;"> 
*Schnitt screenshot1, Beachte, wie der Dialog halbtransparent ist.  Es wird nur der Bildschirminhalt unterhalb des Dialogs erfasst.*

Nach dem Klicken auf **OK** erstellt das Makro dann das Bildschirmfoto und speichert es in einer temporären Datei. Am Speicherort der Datei wird dann ein Datei Öffnen Dialogfeld geöffnet. Du kannst die Datei von dort in das Forum ziehen und loslassen im Textbereich, wo du deinen Text für deinen Forumsbeitrag eingibst. Bei Abbruch des Dialogs wird die temporäre Bildschirmfoto Datei automatisch gelöscht. Du könntest die Bildschirmfoto Datei auch in deiner Standardanwendung öffnen, die zum Öffnen von {{FileName|.png}} Dateien installiert ist (unter Windows ist dies typischerweise Paint). Dies kann nützlich sein, wenn du dem Bildschirmfoto einige Anmerkungen hinzufügen oder vielleicht zusätzliche Bearbeitungen, wie z.B. Zuschneiden, vornehmen möchtest.

<img alt="" src=images/Snip-Screenshot2.png  style="width:600px;"> *Snip screenshot2, Dies ist der Dateiöffnungsdialog, der nach der Aufnahme des Bildschirmfotos automatisch aufklappt. Das Bild kann in das Forum gezogen und losgelassen werden oder es kann zur weiteren Bearbeitung in deiner System Standardanwendung zum Öffnen von png Dateien geöffnet werden. 
Alternativ dazu kannst du auf das Bild rechtsklicken und **Öffnen mit..* mit einer anderen Anwendung deiner Wahl öffnen.**

Wenn das Makro auf deinem System nicht funktioniert, um Bildschirmfotos zu erstellen, kann es trotzdem nützlich sein für Bildschirmfotos, die du mit anderen Werkzeugen erstellt hast. Kopiere das Bildschirmfoto einfach in die Zwischenablage und führe dann das Makro aus. Das Makro erstellt die temporäre Datei und öffnet das Verzeichnis der Datei in einem Datei Öffnen Dialog für dich. Einige andere Werkzeuge zum Erstellen von Bildschirmfotos:

:   Windows: Windows Taste + **Umschalten** + **S**
:   MacOS: **Command** + **Umschalten** + **4**
:   Linux: gnome-Bildschirmfoto Hilfsprogramm

## Parameter

Das Makro unterstützt Benutzerparameter, die mit **Werkzeuge → Parameter bearbeiten... → Zusatzmodule → Schnitt_Makro**


<div class="mw-translate-fuzzy">


:   
    `LetzteX`, `LetzteY`, `LetzteBreite`, `LetzteHöhe`: Lage und Größe des zuletzt verwendeten Schnittkastens

:   
    `FensterDurchsichtigkeit`(0.85): ein Wert zwischen 0.0 (weniger durchsichtig) und 1.0 (mehr durchsichtig)

:   
    `SchnittVerzögerung`(0.5): Zeit (in Sekunden) Verzögerung zwischen schliessen des Schnittkastens und Schnitt


</div>

Die `Letzten` Parameter werden von dem Makro bei jeder Ausführung zurückgesetzt. So wird er verfolgt, wo der Schnittkasten zu platzieren ist, d.h. an der Stelle, an der er sich zuletzt befand, als der Benutzer ein Bildschirmfoto gemacht hat.

Der `FensterDurchsichtigkeit` Parameter ist die Durchsichtigkeit des Schnittkastens.

Der `SchnittVerzögerung` Parameter kann angepasst werden, um die Dinge etwas zu beschleunigen, aber wenn der Wert zu klein ist, könnte das aufgenommene Bildschirmfoto den Schnittkasten selbst enthalten, weil vor der Aufnahme des Bildschirmfotos eine gewisse Zeitspanne zum Schließen des Dialogs benötigt wird.

The `DesiredWidth` parameter scales the image to the desired width unless it is 0 (the default) in which case no scaling is done. For example, if you set the desired width to 800 then you will get images that are 800 pixels wide. The height will be automatically scaled to maintain the current aspect ratio. If the original image was 1600x1200 and the DesiredWidth is 800, then the resulting image will be 800x600.

The `ScaleFactor` parameter scales the image to the desired ratio, e.g. 0.5. The default is 1.0, in which case no scaling is done. This overrides the DesiredWidth parameter if ScaleFactor is not 1.0.

You can bypass all scaling by holding down the Ctrl key while clicking the Ok button to take the screen shot.

## Skript

ToolBar icon ![](images/Snip.png )

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
__date__ = "2020.10.19"
__version__ = 1.21
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

## Verweis

Die Forumsdiskussion [Schnitt Makro](https://forum.freecadweb.org/viewtopic.php?f=9&t=38328&sid=385bf3174dcae7fb8bdf529f4e76dfed)

---
[documentation index](../README.md) > Macro Snip/de
