 {{Macro/fr
|Icon=Macro_Toggle_Views_Visibility.png
|Name=Macro Toggle Panels Visibility
|Name/fr=Macro Toggle Panels Visibility
|Description=Cette macro permet de basculer la visibilité des différentes vues de FreeCAD, la fenêtre active (3D ou Python) utilise tout l'espace disponible de l'écran.
|Author=Piffpoof
|Version=1.0
|Date=2015-01-17
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/d/d0/Macro_Toggle_Views_Visibility.png Toolbar icon]
|SeeAlso=[https://forum.freecadweb.org/viewtopic.php?f=22&t=30450&hilit=Toggle_Panels Toggle_Panels]
}}

## Description

Pendant votre usage de FreeCAD, il arrive souvent que vous avez besoin de plusieurs fenêtres complémentaire (Combo View, Console Python, etc.) . Inversement, vous avez souvent besoin de concentrer sur le contenu principale (votre dessin). Ce macro permets de cacher ou révéler les fenêtres complémentaire avec un clique.

## Installation

Pour installer ce Macro, mettez le code dans votre dossier a Macro et lancez le a partir de votre barre à outils ou de votre liste des Macros. Il est préférable de créer une bouton pour le lancer dans votre barre à outils pour le rendre plus accessible.

-   [Comment installer une Macro](How_to_install_macros/fr.md)
-   [Personnaliser la barre d\'outils ](Customize_Toolbars/fr.md)

## Usage

Cliquez le bouton associé dans votre barre à outils ou exécuter le a partir de votre liste des Macros. Les fenêtres complémentaire de Python console, Report view et Combo view vont changer leur état de visible a caché ou inversement.

## Interface Utilisateur 

Sur lancement du macro (par bouton ou a partir du liste des macros) les fenêtres complémentaire vont apparaître ou disparaître.

## Script

Toolbar icon ![](images/Macro_Toggle_Views_Visibility.png )

**Macro\_Toggle\_Panels\_Visibility.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
# macro to toggle visibility of Report view, Python console, Combo view
from PySide import QtCore, QtGui
mainWindow = FreeCADGui.getMainWindow()
dockWidgets = mainWindow.findChildren(QtGui.QDockWidget)
for dw in dockWidgets:
    if dw.objectName() == "Python console":
        pcWidget = dw
    if dw.objectName() == "Combo View":
        cvWidget = dw
    if dw.objectName() == "Report view":
        rvWidget = dw
     
if pcWidget.isVisible():
    pcWidget.hide()
    cvWidget.hide()
    rvWidget.hide()
else:
    pcWidget.show()
    cvWidget.show()
    rvWidget.show()

}}




