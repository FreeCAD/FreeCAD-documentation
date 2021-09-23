# Macro MessageBox/de
 {{Macro/de
|Name=MessageBox
|Translate=MessageBox
|Icon=Macro MessageBox.png
|Description=Zeigen Sie, wie Sie dem Benutzer Informationen in Makros geben.
|Author=Gaël Ecorchard
|Version=1.0
|Date=2011-09-19
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/7/7f/Macro_MessageBox.png ToolBar Icon]
}}

## Beschreibung

Zeigen Sie, wie Sie dem Benutzer Informationen in Makros geben.

<img alt="" src=images/Macro_MessageBox_00.png  style="width:480px;"> 
*MessageBox*

## Skript

ToolBar Icon ![](images/Macro_MessageBox.png )

**Macro\_MessageBox.FCMacro**


{{MacroCode|code=
#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
"""Show how to give information to the user in macros
"""
from PySide import QtCore, QtGui
 
def errorDialog(msg):
    # Create a simple dialog QMessageBox
    # The first argument indicates the icon used: one of QtGui.QMessageBox.{NoIcon, Information, Warning, Critical, Question} 
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Warning, 'Error in macro MessageBox', msg)
    diag.setWindowModality(QtCore.Qt.ApplicationModal)
    diag.exec_()
 
msg = 'Example of warning message'
errorDialog(msg)
raise(Exception(msg))
}}

Um die akzentuierten Zeichen im Textfeld von **Qt** zu verwenden, muss der Tag **\# - \* - Codierung verwendet werden: utf-8 - \* -** muss ein **u** hinzugefügt werden or der anzuzeigenden Nachricht
Beispiel:


{{MacroCode|code=
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Warning, u'Trop d'éléments désignés', msg)
    ...
    ...
msg = u'Élément sélectionnés affichés'
}}

Um mehrere Zeilen in einem Dialogfeld anzuzeigen, muss **Qt** zwischen jeder Zeile **\"\\ n\"** (Zitat, auch zwischen Apostrophen gültig) eingefügt werden.
Gültig auch **\"\\r\\n\"**, das **CR** Wagenrücklauf und **LF** Zeilenende entspricht, ebenfalls gültig **\\t** ist ein Tabulator, Zeichen sollten zwischen Anführungszeichen (und Apostrophe) als Zeichenfolge stehen. Die Tags befinden sich neben dem Text, um **\"anzuzeigen. \\nRayon\\t:\"**, der Tag *\' \"\\\"*\' (umgekehrter Schrägstrich) definiert den Befehl.
Beispiel:


{{MacroCode|code=
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Information,u"Coordonnées",u"Coordonnée X : "+str(x)+"\r\n"+u"Coordonnée Y : "+str(y)+"\n"+u"Coordonnée Z :<br>
 "+str(z)+"\nRayon\t     : "+str(r))
}}




