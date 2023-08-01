# Macro findConfigFiles/de
{{Macro
|Name=findConfigFiles
|Icon=Macro_findConfigFiles.png
|Description=Use this macro to find your user setting configuration files, that is,<br/>'''system.cfg'''<br/>'''user.cfg'''<br/>These files can be renamed in order to reset FreeCAD's settings back to their original defaults. This can sometimes fix problems you are having with FreeCAD.<br/>You should exit FreeCAD before renaming the files, and then open FreeCAD again afterwards. If renaming the files did not solve the issue you were having you can delete the new files FreeCAD created and rename the original files back to their original names in order to restore your previous settings. You can also safely delete the renamed files once you are certain you no longer need or want them, but it is recommended to rename them instead of deleting until you are certain they are no longer needed.<br/>Note: The macro does not rename the files or make any changes to your settings. It merely finds the location of these files, copies that location to the clipboard, and (attempts to) open the folder containing these files on your computer using the default file browser. 
|Author=TheMarkster
|Version=2022.03.15
|Date=2022-03-15
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/b5/Macro_findConfigFiles.png ToolBar Icon]
}}

## Beschreibung

Verwende dieses Makro, um deine Benutzereinstellungs-Konfigurationsdateien zu finden, d.h,

-    `system.cfg`
    

-    `user.cfg`
    

Diese Dateien können umbenannt werden, um die Einstellungen von FreeCAD wieder auf die ursprünglichen Standardwerte zurückzusetzen. Dies kann manchmal Probleme beheben, die du mit FreeCAD hast.

You should exit FreeCAD before renaming the files, and then open FreeCAD again afterwards. If renaming the files did not solve the issue you were having you can delete the new files FreeCAD created and rename the original files back to their original names in order to restore your previous settings. You can also safely delete the renamed files once you are certain you no longer need or want them, but it is recommended to rename them instead of deleting until you are certain they are no longer needed.

Note: The macro does not rename the files or make any changes to your settings. It merely finds the location of these files, copies that location to the clipboard, and (attempts to) open the folder containing these files on your computer using the default file browser.

## Script

ToolBar icon ![](images/Macro_findConfigFiles.png )

**Macro_findConfigFiles.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
import FreeCAD
import subprocess, os 
from PySide import QtCore,QtGui
import platform 
__title__ = "findConfigFiles"
__author__ = "TheMarkster"
__url__ = "https://www.freecadweb.org/wiki/Macro_findConfigFiles"
__Wiki__ = "http://www.freecadweb.org/wiki/index.php?title=Macro_findConfigFiles"
__date__ = "2022.03.15" 
__version__ = __date__


"""A macro to help with user configuration files --<TheMarkster>"""

clipboard = QtGui.QApplication.clipboard()
sys = platform.system()
userFolder = App.getUserConfigDir() if hasattr(App,"getUserConfigDir") else App.getUserAppDataDir()

msgBox = QtGui.QMessageBox()
msgBox.setWindowTitle('findConfigFiles macro')
msgBox.setTextFormat(QtCore.Qt.RichText)
#msgBox.setStandardButtons(QtGui.QMessageBox.Ok.__or__(QtGui.QMessageBox.Cancel))
#__or__() is deprecated in python 3.8 and the pipe symbol interferes with addon manager, so add buttons separately
msgBox.addButton(QtGui.QMessageBox.Ok)
msgBox.addButton(QtGui.QMessageBox.Cancel)
msgBox.addButton("Copy to Clipboard and Open",QtGui.QMessageBox.ApplyRole)

#HTML tags are part of the source -- do not edit
#thanks to user C4e for help with the paragraph formatting
msg = """
 These files are located here on your system:
 <p>
    <b><font color = 'blue'>""" + userFolder + """</font></b>
 </p>
 <p>
 This macro was created to support you in renaming the configuration files of your user application. 
 This can <i>sometimes</i> correct some issues you are having using FreeCAD.
 If it doesn't work you can always go back and rename them back to their original names.
 </p>
 <p>
 To reset your configuration settings, exit FreeCAD and rename these 2 files:
 <ul>
    <li><b><font color='blue'>system.cfg</font></b>
    <li><b><font color = 'blue'>user.cfg</font></b>
 </ul>
 Rename them e.g. to user/system.cfg.backup or something similar.
 </p>
 <p>
 When you press OK the macro will attempt to open the folder location for you, but 
 you might need to open it manually if this doesn't work.
 </p>
 <p>
 Renaming these files will reset <i>all</i> of your FreeCAD settings back to default.
 </p>
 <p>
 (This macro does <i>not</i> make any changes to these files or to your user settings.)</p>
 """


msgBox.setText(msg)
ok = msgBox.exec_()
if ok==0:
    clipboard.setText(userFolder)
if ok == QtGui.QMessageBox.Ok or ok==0:
    if 'Windows' in sys:
        subprocess.Popen('start explorer.exe '+userFolder, shell=True)
    elif 'Linux' in sys:
        os.system("xdg-open '%s'" % userFolder)
    elif 'Darwin' in sys:
        subprocess.Popen(["open", userFolder])
    else:
        msgBox = QtGui.QMessageBox()
        msg = "We were unable to determine your platform, and thus cannot open your '+userFolder+' for you, but you can still do it manually.\n"
        msgBox.exec_()}}

## Link

[findConfigFiles macro](https://forum.freecadweb.org/viewtopic.php?f=22&t=29888)



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro findConfigFiles/de
