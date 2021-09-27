---
- GuiCommand:/fr
   Name:Std ViewTrimetric
   Name/fr:Std Vue trimétrique
   MenuLocation:Affichage → Vues standards → Axonometric → Trimétrique
   Workbenches:Tous
   SeeAlso:[Std Vue isométrique](Std_ViewIsometric/fr.md), [Std Vue dimétrique](Std_ViewDimetric/fr.md)
---

# Std ViewTrimetric/fr

## Description

La commande **Std Vue trimétrique** réaligne la caméra dans la _ mais la commande fonctionne également si la vue est en [mode perspective](Std_PerspectiveCamera/fr.md).

![](images/Std_ViewTrimetric_example.svg ) *L'[Axes du repère](Std_AxisCross/fr.md) et un cube en vue trimétrique*

## Utilisation

1.  Sélectionnez l\'option **Affichage → Vues standards → Axonometric → <img src="images/Std_ViewTrimetric.svg" width=16px> Trimétrique** dans le menu.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \'vue trimétrique\', utilisez la méthode `viewTrimetric` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewTrimetric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewTrimetric/fr
