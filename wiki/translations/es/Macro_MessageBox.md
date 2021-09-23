# Macro MessageBox/es
{{Macro/es
|Name=MessageBox
|Translate=MessageBox
|Icon=Macro MessageBox.png
|Description=Muestra como dar información al usuario en las  macros
|Author=Gaël Ecorchard
|Version=1.0
|Date=2011-09-19
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/7/7f/Macro_MessageBox.png ToolBar Icon]
}}

## Descripción

Muestra como dar información al usuario en las macros

<img alt="" src=images/Macro_MessageBox_00.png  style="width:480px;"> 
*MessageBox*

## Script

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

Para usar los caracteres acentuados en el campo de texto de **Qt**, usando la etiqueta **\# - \* - codificación: utf-8 - \* -** debe agregarse una **u** antes del mensaje a mostrar
Ejemplo:


{{MacroCode|code=
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Warning, u'Trop d'éléments désignés', msg)
    ...
    ...
msg = u'Élément sélectionnés affichés'
}}

Para mostrar varias líneas en un cuadro de diálogo **Qt**, debe agregarse **\"\\ n\"** (cita, válida también entre apóstrofes) entre cada línea.
Válido también **\"\\ r \\ n\"** que corresponde a **CR** retorno de carro, y **LF** fin de línea, válido también **\"\\ t\"** es una pestaña, los caracteres deben estar entre comillas (y apóstrofes) como una cadena de caracteres, las etiquetas se pueden encontrar al lado del texto para mostrar \'\'\'\"\\ nRayon \\ t:\" \'\'\', la etiqueta **\"\\\"** (barra invertida) define el comando.
Ejemplo:


{{MacroCode|code=
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Information,u"Coordonnées",u"Coordonnée X : "+str(x)+"\r\n"+u"Coordonnée Y : "+str(y)+"\n"+u"Coordonnée Z :<br>
 "+str(z)+"\nRayon\t     : "+str(r))
}}

---
[documentation index](../README.md) > Macro MessageBox/es
