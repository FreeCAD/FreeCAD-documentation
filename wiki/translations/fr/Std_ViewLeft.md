---
- GuiCommand:/fr
   Name:Std ViewLeft
   Name/fr:Std Vue de gauche
   MenuLocation:Affichage → Vues standards → Gauche
   Workbenches:Tous
   Shortcut:**6**
   SeeAlso:[Std Vue arrière](Std_ViewRear/fr.md), [Std Vue de dessous](Std_ViewBottom/fr.md)
---

# Std ViewLeft/fr

## Description

La **Std Vue de gauche** place la caméra dans la [vue 3D](3D_view/fr.md) dans la direction de l\'axe des X positifs.

![](images/FreeCAD_views_rear.svg ) 
*La flèche 6 pointe dans le sens de la vue de gauche*



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande :
    -   Appuyez sur le bouton **<img src="images/Std_ViewLeft.svg" width=16px> [Gauche](Std_ViewLeft/fr.md)**.
    -   Sélectionnez l\'option **Affichage → Vues standards → <img src="images/Std_ViewLeft.svg" width=16px> Gauche** dans le menu.
    -   Sélectionnez l\'option **Vues standard → <img src="images/Std_ViewLeft.svg" width=16px> Gauche** dans le menu contextuel de la [Vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier : **6**.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \'vue de gauche\', utilisez la méthode `viewLeft` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewLeft()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewLeft/fr
