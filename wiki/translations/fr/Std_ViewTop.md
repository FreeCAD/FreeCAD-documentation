---
- GuiCommand:/fr
   Name:Std ViewTop
   Name/fr:Std Vue de dessus
   MenuLocation:Affichage → Vues standards → Dessus
   Workbenches:Tous
   Shortcut:**2**
   SeeAlso:[Std Vue de face](Std_ViewFront/fr.md), [Std Vue droite](Std_ViewRight/fr.md)
---

# Std ViewTop/fr

## Description

La **Std Vue de dessus** place la caméra dans la [vue 3D](3D_view/fr.md) dans la direction de l\'axe des Z négatifs.

![](images/FreeCAD_views_front.svg ) 
*La flèche 1 pointe dans le sens de la vue de dessus*



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande :
    -   Appuyez sur le bouton **<img src="images/Std_ViewTop.svg" width=16px> [Dessus](Std_ViewTop/fr.md)**.
    -   Sélectionnez l\'option **Affichage → Vues standards → <img src="images/Std_ViewTop.svg" width=16px> Dessus** dans le menu.
    -   Sélectionnez l\'option **Vues standard → <img src="images/Std_ViewTop.svg" width=16px> Dessus** dans le menu contextuel de la [Vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier: **2**.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \'vue de dessus\', utilisez la méthode `viewTop` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewTop()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewTop/fr
