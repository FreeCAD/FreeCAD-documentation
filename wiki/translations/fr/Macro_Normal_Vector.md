# Macro Normal Vector/fr
{{Macro/fr
|Name=Normal Vector Macro
|Icon=Macro_Normal_Vector.png
|Description=Donne la Normale du vecteur de la face sélectionnée.
|Author=ulrich1a
|Version=1.0
|Date=2016-09-26
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/8/8b/Macro_Normal_Vector.png ToolBar Icon]
}}

## Description

Cette simple macro extrait le vecteur normal de la face précédemment choisie dans la vue 3D et l\'affiche dans la console python

## Utilisation

-   Choisissez une face dans la vue 3D.
-   Collez la macro dans la console python.
-   FreeCAD affiche les informations du vecteur de la normal dans la console Python.
-   Utilisez ces valeurs pour la mise en place de la direction lors de la création d\'une vue de dessin.

## Script

Icône de la barre d\'outils ![](images/Macro_Normal_Vector.png )

**Macro\_Normal\_Vector.FCMacro**


{{MacroCode|code=
Gui.Selection.getSelectionEx()[0].SubObjects[0].Faces[0].normalAt(0,0)
}}

## Lien

[Link to dicussion thread (german)](http://forum.freecadweb.org/viewtopic.php?f=13&t=10959)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Normal Vector/fr
