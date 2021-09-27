---
- GuiCommand:/fr
   Name:Std ViewIsometric
   Name/fr:Std Vue isométrique
   MenuLocation:Affichage → Vues standards → Axonometric → Isométrique
   Workbenches:Tous
   Shortcut:**0**
   SeeAlso:[Std Vue orthographique](Std_OrthographicCamera/fr.md), [Std Vue dimétrique](Std_ViewDimetric/fr.md), [Std Vue trimétrique](Std_ViewTrimetric/fr.md)
---

# Std ViewIsometric/fr

## Description

La commande **Std Vue isométrique** réaligne la caméra dans la _ mais la commande fonctionne également si la vue est en [mode perspective](Std_PerspectiveCamera/fr.md).

![](images/Std_ViewIsometric_example.svg ) *L'[Axes du repère](Std_AxisCross/fr.md) et un cube en vue isométrique*

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Std_ViewIsometric.svg" width=16px> [Choisir la vue isométrique (0)](Std_ViewIsometric/fr.md)**.
    -   Sélectionnez l\'option **Affichage → Vues standard → Axonometric → <img src="images/Std_ViewIsometric.svg" width=16px> Isométrique** dans le menu.
    -   Sélectionnez l\'option **Vues standard → <img src="images/Std_ViewIsometric.svg" width=16px> Isométrique** dans le menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Utilisez le raccourci clavier: **0**.

## Remarques

-   Il est également possible de passer en mode d\'affichage isométrique via le menu Mini-cube du [Cube de navigation](Navigation_Cube/fr.md).

## Script


**Voir aussi:**

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
[documentation index](../README.md) > Std ViewIsometric/fr
