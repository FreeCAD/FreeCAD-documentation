# Macro Snip/en
{{Macro
|Name=Macro Snip
|Icon=Snip.png
|Description=Use this macro to easily post screenshots to the FreeCAD forum.<br/>It is best to add this macro to your global custom macros toolbar for quick and easy access.<br/>When posting to the FreeCAD forum it is often useful to be able to include screenshots. The problem is this is a somewhat tedious task. This macro is to make that task a bit easier.<br/>The macro can take screenshots or it can use existing screenshots that have already been copied to the system clipboard. To bypass the image already in clipboard press the Shift key while invoking the macro. To use the macro to take the screenshot adjust the size and placement of the dialog that pops up, then click OK. Upon clicking OK the macro will attempt to take a screenshot of the area of the screen covered by the dialog. The dialog itself is semi-transparent, so you can see the contents beneath.
|Author=TheMarkster
|Version=1.3
|Date=2024.07.23
|FCVersion=All
|Download=[https://wiki.freecadweb.org/images/a/a0/Snip.png ToolBar Icon]
|SeeAlso=[Macro Copy3DViewToClipboard](Macro_Copy3DViewToClipboard.md), [Macro Screen Wiki](Macro_Screen_Wiki.md)
|Shortcut=On Windows: Windows Key + Shift + S<br/>
On Mac: Command + Shift + 4<br/>
On Linux: gnome-screenshot utility<br/>
}}

## Description

Use this macro to easily post screenshots to the [FreeCAD forum](https://forum.freecadweb.org).

It is best to add this macro to your global custom macros toolbar for quick and easy access.

When posting to the FreeCAD forum it is often useful to be able to include screenshots. The problem is this is a somewhat tedious task. This macro therefore aims to make that task a bit easier.

## Usage

The macro can take screenshots or it can use existing screenshots that have already been copied to the system clipboard. To bypass the image already in clipboard press the **Shift** key while invoking the macro. To use the macro to take the screenshot adjust the size and placement of the dialog that pops up, then click **OK**. Upon clicking **OK** the macro will attempt to take a screenshot of the area of the screen covered by the dialog. The dialog itself is semi-transparent, so you can see the contents beneath.

<img alt="" src=images/Snip-Screenshot1.png  style="width:600px;"> 
*Notice how the dialog is semi-transparent. Only the screen contents below the dialog will be captured.*

After clicking **OK**, the macro then takes the screenshot and saves it to a temporary file. A file open dialog is then opened at the file\'s location. You can drag and drop the file from there to the forum into the textarea where you type in your text for your forum post. Upon canceling the dialog the temporary screenshot file is deleted automatically. You may also open the screenshot file in your default application installed for opening **.png** files (on Windows this is typically Paint). This can be useful if you wish to add some annotations to the screenshot or perhaps additional editing, such as cropping.

<img alt="" src=images/Snip-Screenshot2.png  style="width:600px;"> 
*This is the open file dialog that pops up automatically after taking the screenshot. The image can be dragged and dropped to the forum or it can be opened for further processing in your system default application for opening png files. Alternatively, you can right-click on the image and **Open with..* another application of your choice.**

If the macro doesn\'t work on your system to capture screenshots it can still be useful for screenshots you have captured using other tools. Simply copy the screenshot to the clipboard, then run the macro. It will create the temporary file and open the file\'s directory in an open file dialog for you. Some other tools for taking screenshots:

:   Windows: Windows Key + **Shift** + **S**
:   MacOS: **Command** + **Shift** + **4**
:   Linux: gnome-screenshot utility

## Parameters

The Macro supports user parameters, which can be set using **Tools → Edit Parameters... → Plugins → Snip_Macro**

:   
    `LastX`, `LastY`, `LastWidth`, `LastHeight`: location and size of snip box last use

:   
    `WindowOpacity`(0.85): a value between 0.0 (less opaque) and 1.0 (more opaque)

:   
    `SnipDelay`(0.5): time (in seconds) delay between snip box close and snip

:   
    `DesiredWidth`(0): desired width (in pixels), ignored if 0 \-- scales image to desired with keeping current aspect ratio

:   
    `ScaleFactor`(1.0): desired scale factor, (overrides DesiredWidth if ScaleFactor is not 1.0) \-- scales image to scale factor

The `Last` parameters are reset by the macro each time it is run. This is how it keeps track of where to place the snip box, which is the last place it was when the user took a screenshot.

The `WindowOpacity` parameter is the opacity of the snip box.

The `SnipDelay` parameter can be adjusted to speed things up a bit, but if the value is too small the screenshot taken might include the snip box itself because there needs to be duration of time to close the dialog before taking the screenshot.

The `DesiredWidth` parameter scales the image to the desired width unless it is 0 (the default) in which case no scaling is done. For example, if you set the desired width to 800 then you will get images that are 800 pixels wide. The height will be automatically scaled to maintain the current aspect ratio. If the original image was 1600x1200 and the DesiredWidth is 800, then the resulting image will be 800x600.

The `ScaleFactor` parameter scales the image to the desired ratio, e.g. 0.5. The default is 1.0, in which case no scaling is done. This overrides the DesiredWidth parameter if ScaleFactor is not 1.0.

You can bypass all scaling by holding down the Ctrl key while clicking the Ok button to take the screen shot.

## Script

ToolBar icon ![](images/Snip.png )

**Macro_Snip.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
"""
***************************************************************************
*   Copyright (c) 2019 <TheMarkster>                                      *
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
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          *
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
textarea where you type in your post. But it still requires many
tedious steps. This macro is to reduce some of those steps.

You should add the macro to your custom macro toolbar to save as many clicks as possible.

The first thing the macro does is to check if there is an image already saved to the
system clipboard, and if so, it uses that one. To bypass the clipboard, press Shift
while invoking the macro.

"""

__title__ = "Snip"
__author__ = "TheMarkster"
__url__ = ""
__Wiki__ = ""
__date__ = "2024.07.23"
__version__ = 1.3
import FreeCAD
from PySide import QtGui,QtCore
import uuid
import time
import tempfile, os, shutil

# class SnipBox(QtGui.QDialog):
#     def __init__(self, scale, desired_width):
#         QtGui.QDialog.__init__(self)
#         self.scale = scale
#         self.desired_width = desired_width
#
#         self.detailsTextEdit = QtGui.QTextEdit("Details")
#         self.Details = QtGui.QPushButton("Details")
#         self.Scaling = QtGui.QPushButton("Scaling")
#         self.Details.clicked.connect(self.onDetailsClicked)
#         self.Scaling.clicked.connect(self.onScalingClicked)
#         layout = QtGui.QVBoxLayout()
#         layout.addWidget(self.detailsTextEdit)
#         layout.addStretch()
#         buttons = QtGui.QDialogButtonBox(
#             QtGui.QDialogButtonBox.Ok,
#             QtCore.Qt.Horizontal, self)
#         buttons.accepted.connect(self.accept)
#         buttons.rejected.connect(self.reject)
#         buttons.addButton(self.Details, QtGui.QDialogButtonBox.ActionRole)
#         buttons.addButton(self.Scaling, QtGui.QDialogButtonBox.ActionRole)
#         buttons.setCenterButtons(True)
#         layout.addWidget(buttons)
#         self.setLayout(layout)
#         self.detailsTextEdit.setVisible(False)
#
#     def setDetailedText(self, txt):
#         self.detailsTextEdit.setText(txt)
#
#     def setTitle(self, rectwidth, rectheight):
#         if self.scale != 1.0:
#            out_width = rect.width()*scale_factor
#         elif self.desired_width != 0:
#             out_width = desired_width
#         self.setWindowTitle(f"Snip macro v{__version__} {rectwidth} x {rectheight} output width {out_width}")
#
#
#     def onDetailsClicked(self):
#         self.detailsTextEdit.setVisible(not self.detailsTextEdit.isVisible())
#
#     def onScalingClicked(self):
#         pass
#
#     def event(self, e): #credit serge_gubenko of stackoverflow for this
#         result = QtGui.QDialog.event(self, e)
#         self.setMinimumHeight(0)
#         self.setMaximumHeight(16777215)
#         self.setMinimumWidth(0)
#         self.setMaximumWidth(16777215)
#         self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
#         textEdit = self.findChild(QtGui.QTextEdit)
#         if textEdit != None :
#             textEdit.setMinimumHeight(0)
#             textEdit.setMaximumHeight(16777215)
#             textEdit.setMinimumWidth(0)
#             textEdit.setMaximumWidth(16777215)
#             textEdit.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# #thanks to mario52 for this
#         if result == True:
#             try:
#                 rect = mb.frameGeometry()
#                 rectwidth  = rect.width()
#                 rectheight = rect.height()
#                 mb.setTitle(rectwidth,rectheight)
#
#             except Exception:
#                 None
# ##############
#         return result
class SnipBox(QtGui.QDialog):
    def __init__(self, scale, desired_width):
        QtGui.QDialog.__init__(self)
        self.pg = FreeCAD.ParamGet("User parameter:Plugins/Snip_Macro")
        self.scale = scale
        self.desired_width = desired_width

        self.detailsTextEdit = QtGui.QTextEdit("Details")
        self.Details = QtGui.QPushButton("Details")
        self.Scaling = QtGui.QPushButton("Scaling")
        self.Details.clicked.connect(self.onDetailsClicked)
        self.Scaling.clicked.connect(self.onScalingClicked)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.detailsTextEdit)
        layout.addStretch()

        # Scaling widgets
        self.scaleLabel = QtGui.QLabel("Scale:")
        self.scaleSpinBox = QtGui.QDoubleSpinBox()
        self.scaleSpinBox.setDecimals(2)
        self.scaleSpinBox.setSingleStep(0.1)
        self.scaleSpinBox.setValue(self.scale)
        self.scaleSpinBox.valueChanged.connect(self.updateScale)

        self.fixedWidthLabel = QtGui.QLabel("Fixed Width:")
        self.fixedWidthSpinBox = QtGui.QSpinBox()
        self.fixedWidthSpinBox.setRange(0, 10000)
        self.fixedWidthSpinBox.setValue(self.desired_width)
        self.fixedWidthSpinBox.valueChanged.connect(self.updateDesiredWidth)

        self.scaleLayout = QtGui.QVBoxLayout()
        self.scaleText = QtGui.QLabel("Scale values other than 1.0 will override fixed width setting")
        self.scaleLayout.addWidget(self.scaleText)
        scaleHBox1 = QtGui.QHBoxLayout()
        scaleHBox1.addWidget(self.scaleLabel)
        scaleHBox1.addWidget(self.scaleSpinBox)

        scaleHBox2 = QtGui.QHBoxLayout()
        scaleHBox2.addWidget(self.fixedWidthLabel)
        scaleHBox2.addWidget(self.fixedWidthSpinBox)

        self.scaleLayout.addLayout(scaleHBox1)
        self.scaleLayout.addLayout(scaleHBox2)

        self.scaleWidget = QtGui.QWidget()
        self.scaleWidget.setLayout(self.scaleLayout)
        self.scaleWidget.setVisible(False)

        layout.addWidget(self.scaleWidget)

        buttons = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok,
            QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        buttons.addButton(self.Details, QtGui.QDialogButtonBox.ActionRole)
        buttons.addButton(self.Scaling, QtGui.QDialogButtonBox.ActionRole)
        buttons.setCenterButtons(True)
        layout.addWidget(buttons)
        self.setLayout(layout)
        self.detailsTextEdit.setVisible(False)

    def setDetailedText(self, txt):
        self.detailsTextEdit.setText(txt)

    def setTitle(self, rectwidth, rectheight):
        if self.scale != 1.0:
            out_width = rectwidth * self.scale
        elif self.desired_width != 0:
            out_width = self.desired_width
        self.setWindowTitle(f"Snip macro v{__version__} {rectwidth} x {rectheight} output width {out_width}")

    def onDetailsClicked(self):
        if self.scaleWidget.isVisible():
            self.scaleWidget.setVisible(False)
        self.detailsTextEdit.setVisible(not self.detailsTextEdit.isVisible())

    def onScalingClicked(self):
        if self.detailsTextEdit.isVisible():
            self.detailsTextEdit.setVisible(False)
        self.scaleWidget.setVisible(not self.scaleWidget.isVisible())

    def updateScale(self, value):
        self.scale = value
        self.pg.SetFloat("ScaleFactor", self.scale)

    def updateDesiredWidth(self, value):
        self.desired_width = value
        self.pg.SetInt("DesiredWidth", self.desired_width)

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
                mb.setTitle(rectwidth,rectheight)
            except Exception:
                None
##############
        return result

def get_screen_for_widget(widget):
    screen_geometry = widget.geometry()
    for screen in QtGui.QApplication.screens():
        if screen.geometry().contains(screen_geometry.center()):
            return screen
def get_widget_screen_coordinates(widget):
    screen = get_screen_for_widget(widget)
    widget_geometry = widget.geometry()
    screen_geometry = screen.geometry()
    return QtCore.QRect(widget_geometry.x() - screen_geometry.x(),
                        widget_geometry.y() - screen_geometry.y(),
                        widget_geometry.width(),
                        widget_geometry.height())


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
    mb = SnipBox(scale_factor, desired_width)
    details = """
Move and resize this box to cover the part of the screen you wish to grab.
If it succeeds an open file dialog will appear. Drag and drop the file
from the open file dialog to the forum. The file will be deleted after
you close the dialog.

If this fails you can still use this macro to handle screenshots you
copied to the clipboard using other tools:

Windows snip tool: Window Key + Shift + S
Mac snip tool: Command + Shift + 4
Linux: gnome-screenshot utility

If the macro finds there is already an image copied to the clipboard
it uses that image instead of bringing up this dialog. Press Shift
while invoking this macro to bypass the clipboard. Alternatively,
you can clear the image from the clipboard by copying some text to it.

The Open button will open the file in the system
default application for handling png files, e.g. Paint in windows. This
can be useful if you wish to annotate the screenshot. But most of the
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
   # mb.setWindowTitle("Snip macro v"+str(__version__))
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
        scale_factor = mb.scale
        desired_width = mb.desired_width
        rect = get_widget_screen_coordinates(mb)
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
            #screen = QtGui.QApplication.primaryScreen()
            screen = get_screen_for_widget(mb)
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
                image = image.smoothScaled(rect.width()*scale_factor, rect.height()*scale_factor)
            elif desired_width != 0:
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

## Link

The forum discussion [Snip macro](https://forum.freecadweb.org/viewtopic.php?f=9&t=38328&sid=385bf3174dcae7fb8bdf529f4e76dfed)



---
⏵ [documentation index](../README.md) > Macro Snip/en
