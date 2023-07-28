---
- GuiCommand:/fr
   Name:Std ViewRotateRight
   Name/fr:Std Rotation à droite
   MenuLocation:Affichage → Vues standards → Rotation à droite
   Workbenches:Tous
   Shortcut:**Maj**+**droite**
   SeeAlso:[Std Rotation à gauche](Std_ViewRotateLeft/fr.md)
---

# Std ViewRotateRight/fr

## Description

La commande **Std Rotation à droite** fait pivoter la caméra dans la [vue 3D](3D_view/fr.md) active dans la direction de la vue par incréments de 90 degrés vers la droite (dans le sens horaire).



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Sélectionnez l\'option **Affichage → Vues standards → <img src="images/Std_ViewRotateRight.svg" width=16px> Rotation à droite** dans le menu.
    -   Sélectionnez l\'option **Vues standards → <img src="images/Std_ViewRotateRight.svg" width=16px> Rotation à droite** dans le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier : **Maj**+**Droite**.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour faire tourner la vue à droite, utilisez la méthode `viewRotateRight` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateRight()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewRotateRight/fr
