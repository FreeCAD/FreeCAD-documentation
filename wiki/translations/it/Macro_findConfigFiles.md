# Macro findConfigFiles/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=findConfigFiles
|Icon=Macro_findConfigFiles.png
|Translate=Trova la cartella di configurazione
|Description=Trova la cartella contenente i file di configurazione
|Author=TheMarkster
|Version=2018.09.10
|Date=2018-09-10
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/b5/Macro_findConfigFiles.png ToolBar Icon]
}}


</div>

## Descrizione

Usare questa macro per trovare i file di configurazione delle impostazioni utente.

-    `system.cfg`
    

-    `user.cfg`
    

Questi fili possono essere rinominati per ripristinare le impostazioni di FreeCAD ai loro valori originali. Questo a volte può risolvere i problemi che si incontrano con FreeCAD.

Prima di rinominare i file si dovrebbe uscire da FreeCAD , quindi riavviare FreeCAD in seguito. Se la ridenominazione dei file non ha risolto il problema riscontrato, è possibile eliminare i nuovi file creati da FreeCAD e rinominare i file originali con i loro nomi originali per ripristinare le impostazioni precedenti. È inoltre possibile eliminare in modo sicuro i file rinominati quando si è certi di non averne più bisogno o di volerli conservare, ma si consiglia di rinominarli anziché eliminarli finché non si è certi che non sono più necessari.

Nota: la macro non rinomina i file e non apporta modifiche alle impostazioni. Trova semplicemente la posizione di questi file, copia quella posizione negli Appunti e (tenta di) aprire la cartella contenente questi file utilizzando il browser di file predefinito.

## Script

ToolBar icon ![](images/Macro_findConfigFiles.png )

**Macro\_findConfigFiles.FCMacro**


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

## Vincolo

Il foro [findConfigFiles macro](https://forum.freecadweb.org/viewtopic.php?f=22&t=29888)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro findConfigFiles/it
