# Macro findConfigFiles/fr
{{Macro/fr
|Name=findConfigFiles
|Icon=Macro_findConfigFiles.png
|Description=Utilisez cette macro pour rechercher les fichiers de configuration de vos paramètres utilisateur, c'est-à-dire <br/>'''system.cfg'''<br/>'''user.cfg'''<br/> Ces fichiers peuvent être renommés dans afin de réinitialiser les paramètres de FreeCAD à leurs valeurs par défaut d'origine. Cela peut parfois résoudre les problèmes que vous rencontrez avec FreeCAD. <br/> Vous devez quitter FreeCAD avant de renommer les fichiers, puis rouvrir FreeCAD par la suite. Si renommer les fichiers n'a pas résolu le problème que vous rencontriez, vous pouvez supprimer les nouveaux fichiers créés par FreeCAD et renommer les fichiers d'origine à leurs noms d'origine afin de restaurer vos paramètres précédents. Vous pouvez également supprimer en toute sécurité les fichiers renommés une fois que vous êtes certain que vous n'en avez plus besoin ou que vous ne les souhaitez plus, mais il est recommandé de les renommer au lieu de les supprimer jusqu'à ce que vous soyez certain qu'ils ne sont plus nécessaires. <br/> Remarque   * la macro ne renommer les fichiers ou apporter des modifications à vos paramètres. Elle trouve simplement l'emplacement de ces fichiers, copie cet emplacement dans le presse-papiers et (tente d'ouvrir) le dossier contenant ces fichiers sur votre ordinateur à l'aide du navigateur de fichiers par défaut.
|Author=TheMarkster
|Version=2022.03.15
|Date=2022-03-15
|FCVersion=Tous
|Download=[https   *//www.freecadweb.org/wiki/images/b/b5/Macro_findConfigFiles.png Icône de la barre d'outils]
}}

## Description

Utilisez cette macro pour trouver les fichiers de configuration utilisateur.

-    `system.cfg`
    

-    `user.cfg`
    

Ces fichiers peuvent être renommés afin de réinitialiser les paramètres de FreeCAD à leurs valeurs par défaut d\'origine. Cela peut parfois résoudre les problèmes que vous rencontrez avec FreeCAD.

Vous devez quitter FreeCAD avant de renommer les fichiers, puis ré-ouvrir FreeCAD par la suite. Si le fait de renommer les fichiers n\'a pas résolu le problème que vous aviez, vous pouvez supprimer les nouveaux fichiers créés par FreeCAD et renommer les fichiers d\'origine en leurs noms d\'origine afin de restaurer vos paramètres précédents. Vous pouvez également supprimer les fichiers renommés en toute sécurité une fois que vous êtes certain de ne plus en avoir besoin ou de les vouloir, mais il est recommandé de les renommer au lieu de les supprimer jusqu\'à ce que vous soyez certain qu\'ils ne sont plus nécessaires.

Remarque   * La macro ne renomme pas les fichiers ou n\'apporte aucune modification à vos paramètres. Il trouve simplement l\'emplacement de ces fichiers, copie cet emplacement dans le presse-papiers et (tente d\'ouvrir) le dossier contenant ces fichiers sur votre ordinateur en utilisant le navigateur de fichiers par défaut.

## Script

Icône de la barre d\'outils ![](images/Macro_findConfigFiles.png )

**Macro_findConfigFiles.FCMacro**


{{MacroCode|code=
# -*- coding   * utf-8 -*-
import FreeCAD
import subprocess, os 
from PySide import QtCore,QtGui
import platform 
__title__ = "findConfigFiles"
__author__ = "TheMarkster"
__url__ = "https   *//www.freecadweb.org/wiki/Macro_findConfigFiles"
__Wiki__ = "http   *//www.freecadweb.org/wiki/index.php?title=Macro_findConfigFiles"
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
 These files are located here on your system   *
 <p>
    <b><font color = 'blue'>""" + userFolder + """</font></b>
 </p>
 <p>
 This macro was created to support you in renaming the configuration files of your user application. 
 This can <i>sometimes</i> correct some issues you are having using FreeCAD.
 If it doesn't work you can always go back and rename them back to their original names.
 </p>
 <p>
 To reset your configuration settings, exit FreeCAD and rename these 2 files   *
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
if ok==0   *
    clipboard.setText(userFolder)
if ok == QtGui.QMessageBox.Ok or ok==0   *
    if 'Windows' in sys   *
        subprocess.Popen('start explorer.exe '+userFolder, shell=True)
    elif 'Linux' in sys   *
        os.system("xdg-open '%s'" % userFolder)
    elif 'Darwin' in sys   *
        subprocess.Popen(["open", userFolder])
    else   *
        msgBox = QtGui.QMessageBox()
        msg = "We were unable to determine your platform, and thus cannot open your '+userFolder+' for you, but you can still do it manually.\n"
        msgBox.exec_()}}

## Lien

[findConfigFiles macro](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=29888)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro findConfigFiles/fr
