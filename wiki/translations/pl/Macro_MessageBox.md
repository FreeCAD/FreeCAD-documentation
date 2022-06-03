# Macro MessageBox/pl
{{Macro
|Name=MessageBox
|Icon=Macro MessageBox.png
|Description=Show how to give information to the user in macros.
|Author=Gaël Ecorchard
|Version=1.0
|Date=2011-09-19
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/7/7f/Macro_MessageBox.png ToolBar Icon]
}}

## Description

Show how to give information to the user in macros

<img alt="" src=images/Macro_MessageBox_00.png  style="width   *480px;"> 
*MessageBox*

## Script

ToolBar Icon ![](images/Macro_MessageBox.png )

**Macro\_MessageBox.FCMacro**


{{MacroCode|code=
#! /usr/bin/env python
# -*- coding   * utf-8 -*-
 
"""Show how to give information to the user in macros
"""
from PySide import QtCore, QtGui
 
def errorDialog(msg)   *
    # Create a simple dialog QMessageBox
    # The first argument indicates the icon used   * one of QtGui.QMessageBox.{NoIcon, Information, Warning, Critical, Question} 
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Warning, 'Error in macro MessageBox', msg)
    diag.setWindowModality(QtCore.Qt.ApplicationModal)
    diag.exec_()
 
msg = 'Example of warning message'
errorDialog(msg)
raise(Exception(msg))
}}

In order to use the accented characters in the text field from **Qt**, using the tag \'\'\' \#-\*-coding   * utf-8-\*- \'\'\' must be added a **u** before the message to display
Example    *


{{MacroCode|code=
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Warning, u'Trop d'éléments désignés', msg)
    ...
    ...
msg = u'Élément sélectionnés affichés'
}}

To display multiple lines in a dialog box **Qt**, must be added **\"\\n\"** (quotation, valid also between apostrophes) between each line.
Valid also *\' \"\\r\\n\"*\' which correspond to **CR** carriage return, and **LF** end of line, valid also **\" \\t\"** is a tab, characters should be between quotation marks (and apostrophes) as a character string, the tags can be found next to the text to display **\" \\nRayon\\t   * \"**, the tag **\" \\ \"** (reversed slash) defines the command.
Example    *


{{MacroCode|code=
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Information,u"Coordonnées",u"Coordonnée X    * "+str(x)+"\r\n"+u"Coordonnée Y    * "+str(y)+"\n"+u"Coordonnée Z    *<br>
 "+str(z)+"\nRayon\t        * "+str(r))
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro MessageBox/pl
