---
- GuiCommand:/fr
   Name:Std ViewRight
   Name/fr:Std Vue de droite
   MenuLocation:Affichage → Vues standards → Droite
   Workbenches:Tous
   Shortcut:**3**
   SeeAlso:[Std Vue de face](Std_ViewFront/fr.md), [Std Vue de dessus](Std_ViewTop/fr.md)
---

# Std ViewRight/fr

## Description

La **Std Vue de droite** place la caméra dans la [vue 3D](3D_view/fr.md) dans la direction de l\'axe des X négatifs.

![](images/FreeCAD_views_front.svg ) 
*La flèche 3 pointe dans le sens de la vue de droite*



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande :
    -   Appuyez sur le bouton **<img src="images/Std_ViewRight.svg" width=16px> [Droite](Std_ViewRight/fr.md)**.
    -   Sélectionnez l\'option **Affichage → Vues standards → <img src="images/Std_ViewRight.svg" width=16px> Droite** dans le menu.
    -   Sélectionnez l\'option **Vues standard → <img src="images/Std_ViewRight.svg" width=16px> Droite** dans le menu contextuel de la [Vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier : **3**.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \'vue de droite\', utilisez la méthode `viewRight` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRight()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewRight/fr
