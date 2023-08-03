---
 GuiCommand:
   Name: Std ViewDimetric
   Name/fr: Std Vue dimétrique
   MenuLocation: Affichage , Vues standards , Axonometric , Dimétrique
   Workbenches: Tous
   SeeAlso: Std_ViewIsometric/fr, Std_ViewTrimetric/fr
---

# Std ViewDimetric/fr

## Description

La commande **Std Vue dimétrique** réaligne la caméra dans la [vue 3D](3D_view/fr.md) active pour obtenir une vue [dimetrique](https://en.wikipedia.org/wiki/Axonometric_projection#Three_types). Pour une vue vraiment dimétrique, la vue 3D doit être en [mode orthographique](Std_OrthographicCamera/fr.md) mais la commande fonctionne également si la vue est en [mode perspective](Std_PerspectiveCamera/fr.md).

![](images/Std_ViewDimetric_example.svg ) 
*Les [Axes du repère](Std_AxisCross/fr.md) et un cube en vue dimétrique*



## Utilisation

1.  Sélectionnez l\'option **Affichage → Vues standards → Axonométrique → <img src="images/Std_ViewDimetric.svg" width=16px> Dimétrique** dans le menu.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour changer la vue en \'vue dimétrique\', utilisez la méthode `viewDimetric` de l\'objet ActiveView. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewDimetric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewDimetric/fr
