---
- GuiCommand:/fr
   Name:Std ViewIsometric
   Name/fr:Std Vue isométrique
   MenuLocation:Affichage → Vues standards → Axonométrique → Isométrique
   Workbenches:Tous
   Shortcut:**0**
   SeeAlso:[Std Vue orthographique](Std_OrthographicCamera/fr.md), [Std Vue dimétrique](Std_ViewDimetric/fr.md), [Std Vue trimétrique](Std_ViewTrimetric/fr.md)
---

# Std ViewIsometric/fr

## Description

La commande **Std Vue isométrique** réaligne la caméra dans la [vue 3D](3D_view/fr.md) active pour obtenir une vue [isométrique](https://fr.wikipedia.org/wiki/Perspective_isom%C3%A9trique). Pour une vue vraiment isométrique, la vue 3D doit être en [mode orthographique](Std_OrthographicCamera/fr.md) mais la commande fonctionne également si la vue est en [mode perspective](Std_PerspectiveCamera/fr.md).

![](images/Std_ViewIsometric_example.svg ) 
*Les [Axes du repère](Std_AxisCross/fr.md) et un cube en vue isométrique*



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande :
    -   Appuyez sur le bouton **<img src="images/Std_ViewIsometric.svg" width=16px> [Choisir la vue isométrique (0)](Std_ViewIsometric/fr.md)**.
    -   Sélectionnez l\'option **Affichage → Vues standard → Axonométrique → <img src="images/Std_ViewIsometric.svg" width=16px> Isométrique** dans le menu.
    -   Sélectionnez l\'option **Vues standard → <img src="images/Std_ViewIsometric.svg" width=16px> Isométrique** dans le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Sélectionnez l\'option **<img src="images/Std_ViewIsometric.svg" width=16px> Isométrique** dans le menu Mini-cube du [Cube de navigation](Navigation_Cube/fr.md).
    -   Utilisez le raccourci clavier : **0**.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \'vue isométrique\', utilisez la méthode `viewIsometric` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewIsometric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIsometric/fr
