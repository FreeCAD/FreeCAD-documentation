---
- GuiCommand:/fr
   Name:Std ViewBottom
   Name/fr:Std Vue de dessous
   MenuLocation:Affichage → Vues standards → Dessous
   Workbenches:Tous
   Shortcut:**5**
   SeeAlso:[Std Vue de l'arrière](Std_ViewRear/fr.md), [Std Vue gauche](Std_ViewLeft/fr.md)
---

# Std ViewBottom/fr

## Description

La **Std Vue de dessous** place la caméra dans la [vue 3D](3D_view/fr.md) dans la direction de l\'axe des Z positifs.

![](images/FreeCAD_views_rear.svg ) 
*La flèche 5 pointe dans le sens de la vue de dessous*

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Std_ViewBottom.svg" width=16px> [Std Afficher la vue de dessous](Std_ViewBottom/fr.md)**.
    -   Sélectionnez l\'option **Affichage → Vues standard → <img src="images/Std_ViewBottom.svg" width=16px> Dessous** dans le menu.
    -   Sélectionnez l\'option **Vues standard → <img src="images/_Std_ViewBottom.svg_" width= 16px> Dessous** dans le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier: **5**.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \'vue de dessous\', utilisez la méthode `viewBottom` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewBottom()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewBottom/fr
