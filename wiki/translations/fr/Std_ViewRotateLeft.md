---
- GuiCommand:/fr
   Name:Std_RotateLeft
   Name/fr:Std Rotation à gauche
   MenuLocation:Affichage → Vues standards‏‎ → Rotation à gauche
   Workbenches:Tous
   Shortcut: **Maj**+**Gauche**
   SeeAlso:[Std Rotation à droite](Std_ViewRotateRight/fr.md)
---

## Description

La commande **Std Rotation à gauche** fait pivoter la caméra dans la [vue 3D](3D_view/fr.md) active dans la direction de la vue par incréments de 90 degrés vers la gauche (dans le sens antihoraire).

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Sélectionnez l\'option **Affichage → Vues standards → <img src="images/Std_ViewRotateLeft.svg" width=16px> Rotation à gauche** dans le menu.
    -   Sélectionnez l\'option **Vues standards → <img src="images/Std_ViewRotateLeft.svg" width=16px> Rotation à gauche** dans le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier: **Maj**+**Gauche**.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour faire tourner la vue à gauche, utilisez la méthode `viewRotateLeft` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateLeft()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}  
