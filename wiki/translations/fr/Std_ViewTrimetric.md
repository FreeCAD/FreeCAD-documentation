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

La commande **Std Vue trimétrique** réaligne la caméra dans la [vue 3D](3D_view/fr.md) active pour obtenir une vue [trimétrique](https://en.wikipedia.org/wiki/Axonometric_projection#Three_types). Pour une vue vraiment dimétrique, la vue 3D doit être en [mode orthographique](Std_OrthographicCamera/fr.md) mais la commande fonctionne également si la vue est en [mode perspective](Std_PerspectiveCamera/fr.md).

![](images/Std_ViewTrimetric_example.svg ) 
*Les [Axes du repère](Std_AxisCross/fr.md) et un cube en vue trimétrique*



## Utilisation

1.  Sélectionnez l\'option **Affichage → Vues standards → Axonométrique → <img src="images/Std_ViewTrimetric.svg" width=16px> Trimétrique** dans le menu.



## Script


**Voir aussi :**

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
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewTrimetric/fr
