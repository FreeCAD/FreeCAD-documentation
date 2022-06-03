# Macro MessageBox/cs
<div class="mw-translate-fuzzy">


{{Macro/cs
|Name=MessageBox
|Icon=Macro MessageBox.png
|Translate=MessageBox
|Description=Ukazuje jak uživateli dávat informace v makrech.
|Author=Gaël Ecorchard
|Version=1.0
|Date=2011-09-19
}}


</div>

## Popis

Ukazuje jak uživateli dávat informace v makrech.

<img alt="" src=images/Macro_MessageBox_00.png  style="width   *480px;"> 
*MessageBox*

## Skript

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

Aby bylo možné používat znaky s diakritickými znaménky v textových polích z **Qt**, musí se při použítí značky \'\'\' \#-\*-coding   * utf-8-\*- \'\'\' přidávat **u** před zobrazovanou zprávou
Příklad    *


{{MacroCode|code=
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Warning, u'Trop d'éléments désignés', msg)
    ...
    ...
msg = u'Élément sélectionnés affichés'
}}

Pro zobrazení víceřádkového textu v dialogovém okně **Qt**, musí být přidáno **\"\\n\"** (uvozovky, platné jsou i apostrofy) za každým řádkem.
Platné je i *\' \"\\r\\n\"*\' což koresponduje s **CR** carriage return (návrat vozíku), a **LF** end of line(posun řádku). Lze použít i **\" \\t\"** což je tabulátor. Znaky by měly být mezi uvozovkami (a apostrofy) jako znakový řetězec. Značky mohou být hned vedle zobrazovaného textu **\" \\nRayon\\t   * \"**, značka **\" \\ \"** (obrácené lomítko) znamená, že jde o příkaz.
Příklad    *


{{MacroCode|code=
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Information,u"Coordonnées",u"Coordonnée X    * "+str(x)+"\r\n"+u"Coordonnée Y    * "+str(y)+"\n"+u"Coordonnée Z    *<br>
 "+str(z)+"\nRayon\t        * "+str(r))
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro MessageBox/cs
