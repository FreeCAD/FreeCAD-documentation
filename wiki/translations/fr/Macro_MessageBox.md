# Macro MessageBox/fr
{{Macro/fr
|Name=MessageBox
|Icon=Macro MessageBox.png
|Description=Montre comment donner des informations à l'utilisateur dans les macros
|Author=Gaël Ecorchard
|Version=1.0
|Date=2011-09-19
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/7/7f/Macro_MessageBox.png Icone]
}}

## Description

Cette macro permet d\'afficher un signal, ou un texte dans une boîte de dialogue, avec un icône distinctif.

<img alt="MessageBox" src=images/Macro_MessageBox_00.png  style="width:480px;"> 
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

Pour pouvoir utiliser les caractères accentués dans le champ texte de **Qt**, grâce à la balise **\# -\*- coding: utf-8 -\*-** il faut ajouter un \" **u** \" devant le message à afficher.

Exemple :


{{MacroCode|code=
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Warning, u'Trop d'éléments désignés', msg)
    ...
    ...
msg = u'Élément sélectionnés affichés'
}}

Pour afficher plusieurs lignes dans une boîte de dialogue **Qt**, il faut ajouter **\"\\n\"** (entre guillemets, valable aussi, entre apostrophes) entre chaque lignes.

Valable aussi **\"\\r\\n\"** qui correspondent à **CR** retour chariot, et **LF** fin de ligne, valable aussi **\"\\t\"** qui est une tabulation, les caractères doivent se trouver entre guillemets (ou apostrophes) comme une chaîne de caractère, les balises peuvent se trouver à côté du texte à afficher **\"\\nRayon\\t : \"**, la balise **\" \\ \"** (slash inversé) délimite la commande.

Exemple :


{{MacroCode|code=
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Information,u"Coordonnées",u"Coordonnée X : "+str(x)+"\r\n"+u"Coordonnée Y : "+str(y)+"\n"+u"Coordonnée Z :<br>
 "+str(z)+"\nRayon\t     : "+str(r))
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro MessageBox/fr
