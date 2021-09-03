---
- GuiCommand:/fr
   Name:Std ViewRear
   Name/fr:Std Vue de l'arrière
   MenuLocation:Affichage → Vues standards → Arrière
   Workbenches:Tous
   Shortcut:**4**
   SeeAlso:[Std Vue de dessous](Std_ViewBottom/fr.md), [Std Vue de gauche](Std_ViewLeft/fr.md)
---

## Description

La **Std Vue de l\'arrière** place la caméra dans la [vue 3D](3D_view/fr.md) dans la direction de l\'axe des Y négatifs.

![](images/FreeCAD_views_rear.svg ) *La flèche 4 pointe dans le sens de la vue arrière*

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Std_ViewRear.svg" width=16px> [Std Afficher la vue arrière (4)](Std_ViewRear.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Affichage → Vues standards → <img src="images/Std_ViewRear.svg" width=16px> Arrière}} dans le menu.
    -   Sélectionnez l\'option {{MenuCommand|Vues standard → <img src="images/Std_ViewRear.svg" width=16px> Arrière}} dans le menu contextuel de la [Vue 3](3D_view/fr.md).
    -   Utilisez le raccourci clavier: **4**.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \'vue arrière\', utilisez la méthode `viewRear` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRear()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}  
