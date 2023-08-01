# Macro Toggle Drawstyle/fr
{{Macro/fr
|Name=Macro Toggle Drawstyle
|Description=Cette macro permet de basculer style d'affichage de l'objet sélectionné.
|Author=Piffpoof
|Version=2.0
|Date=2020-02-02
|FCVersion= >=0.17
|Download=[https://www.freecadweb.org/wiki/images/0/0b/Macro_Toggle_Drawstyle.png ToolBar Icon]
|SeeAlso=[Macro Toggle Drawstyle Optimized](Macro_Toggle_Drawstyle_Optimized/fr.md) <img src="images/Macro_Toggle_Drawstyle_Optimized.png" width=24px> pour tous les langages
}}

## Description

Lorsque vous travaillez avec FreeCAD il y a des moments où vous voulez changer rapidement le style d\'affichage (DrawStyle) de l\'objet courant. Le bouton est disponible dans le menu déroulant DrawStyle où tous les modes peuvent être sélectionnés. Cette macro active 2 des modes disponibles comme un bouton cliquable sur une barre d\'outils que l\'utilisateur peut cliquer pour basculer entre les deux modes d\'affichages. L\'utilisateur peut modifier le code de macro pour sélectionner le mode d\'affichage qu\'ils souhaitent faire basculer. Cette macro n\'ajoute pas de fonctionnalités dans le menu déroulant DrawStyles, mais donne une facilité d\'exécution qui change de mode avec un clic de souris.

## Installation

L\'installation copiez le code dans le répertoire Macro approprié. Il est préférable de l\'ajouter sur votre barre d\'outils de manière à être facilement accessible.

-   voir [Comment installer une macro](How_to_install_macros/fr.md)
-   voir [Comment créer une barre d\'outils personnalisée](Customize_Toolbars/fr.md)

## Utilisation

Sélectionnez un objet, puis cliquez sur le bouton associé sur votre barre d\'outils , ou appeler la à partir du menu Macro. Le Style d\'affichage de l\'objet sélectionné basculera entre les deux modes d\'affichage des deux Styles d\'affichage spécifiés dans le code de macro (voir liste de code ci-dessous). **Remarque**: Le cahier des charges pour chaque DrawStyle est listé dans le code, en modifiant le code (qui est documenté dans le code de macro), l\'utilisateur peut sélectionner 2 Style d\'affichage et basculer entre eux.

## Interface utilisateur 

L\'objet sélectionné sera redessiné dans le deuxième Style spécifié dans la macro.

Script optimisé pour toutes les langues, sur un objet sélectionné ou pour tous les objets [Keyboard shortcut, View toolbar - Wireframe](https://forum.freecadweb.org/viewtopic.php?f=3&t=14336&start=40#p146239) (Sun Nov 27, 2016 6:49 pm)

## Script

ToolBar icon ![](images/Macro_Toggle_Drawstyle.png )

**Macro Toggle Drawstyle.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
#
#
#           Macro: Toggle Draw Style
#
# This macros allows the user to switch between different Drawstyles by clicking on
# the button of a Macro in a toolbar.
#
# initial code:     triplus
# macro-isation:    piffpoof
#
# This macro switches (or toggles) between 2 selected styles from the Drawstyle menu.
# As written the macro toggles between "WireFrame" and "As is".
# Immediately below this text is a list of the legal values for the Drawstyle menu.
# The first 2 lines of executable code are of the form "DrawstyleA = " followed by
# the 2nd line which is of the form "DrawstyleB = ".
# These 2 lines specify which of the Drawstyle values the macro will toggle between.
# Drawstyle "As is" is the system default and so is specified as the first drawstyle.
# The second line specifies which drawstyle will be toggled to and from.
# Any of the legal values may be used, so if, for example, it is desired to toggle between
# the Shaded and Points drawstyles, then the 2 lines of code would be modified to be:
#
# drawstyleA = "Shaded"
# drawstyleB = "Points"
#
# but remember that the hash signs ('#') are not to be present on the executable lines.
#
###Legal Values for Drawstyle###
#
# 0 = "As is"
# 1 = "Flat lines"
# 2 = "Shaded
# 3 = "Wireframe"
# 4 = "Points"
# 5 = "Hidden line"
# 6 = "No shading"
#
################################

# triplus @ 2016, 2020
# Toggle global display mode
# ==============================

# 0 = "As is"
# 1 = "Flat lines"
# 2 = "Shaded
# 3 = "Wireframe"
# 4 = "Points"
# 5 = "Hidden line"
# 6 = "No shading"

styleA = 0
styleB = 3

# ==============================

from PySide import QtGui
import FreeCADGui as Gui

mw = Gui.getMainWindow()


act = {
    0: mw.findChild(QtGui.QAction, "Std_DrawStyleAsIs"),
    1: mw.findChild(QtGui.QAction, "Std_DrawStyleFlatLines"),
    2: mw.findChild(QtGui.QAction, "Std_DrawStyleShaded"),
    3: mw.findChild(QtGui.QAction, "Std_DrawStyleWireframe"),
    4: mw.findChild(QtGui.QAction, "Std_DrawStylePoints"),
    5: mw.findChild(QtGui.QAction, "Std_DrawStyleHiddenLine"),
    6: mw.findChild(QtGui.QAction, "Std_DrawStyleNoShading"),
}


actionA = act[styleA]
actionB = act[styleB]


if actionA.isChecked():
    actionB.trigger()
else:
    actionA.trigger()

}}

## Lien

The forum discussion [Keyboard shortcut, View toolbar - Wireframe](https://forum.freecadweb.org/viewtopic.php?f=3&t=14336)



---
⏵ [documentation index](../README.md) > Macro Toggle Drawstyle/fr
