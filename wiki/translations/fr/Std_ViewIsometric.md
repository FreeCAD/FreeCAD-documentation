---
 GuiCommand:
   Name: Std ViewIsometric
   Name/fr: Std Vue isométrique
   MenuLocation: Affichage , Vues standards , Axonométrique , Isométrique
   Workbenches: Tous
   Shortcut: **0**
   SeeAlso: Std_OrthographicCamera/fr, Std_ViewDimetric/fr, Std_ViewTrimetric/fr
---

# Std ViewIsometric/fr

## Description

La commande **Std Vue isométrique** réaligne la caméra dans la [vue 3D](3D_view/fr.md) active pour obtenir une vue [isométrique](https://fr.wikipedia.org/wiki/Perspective_isom%C3%A9trique). Pour une vue vraiment isométrique, la vue 3D doit être en [mode orthographique](Std_OrthographicCamera/fr.md) mais la commande fonctionne également si la vue est en [mode perspective](Std_PerspectiveCamera/fr.md).

![](images/Std_ViewIsometric_example.svg ) 
*Les [axes du repère](Std_AxisCross/fr.md) et un cube en vue isométrique*



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Std_ViewIsometric.svg" width=16px> [Choisir la vue isométrique (0)](Std_ViewIsometric/fr.md)**.
    -   Sélectionnez l\'option **Affichage → Vues standard → Axonométrique → <img src="images/Std_ViewIsometric.svg" width=16px> Isométrique** du menu.
    -   Sélectionnez l\'option **Vues standard → <img src="images/Std_ViewIsometric.svg" width=16px> Isométrique** du menu contextuel de la [vue 3D](3D_view/fr.md).
    -   Sélectionnez l\'option **<img src="images/Std_ViewIsometric.svg" width=16px> Vue isométrique** du menu mini-cube du [cube de navigation](Navigation_Cube/fr.md).
    -   Utilisez le raccourci clavier : **0**.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Utilisez la méthode `viewIsometric` de l\'objet View pour passer en vue isométrique. Les méthodes `viewDimetric` et `viewTrimetric` sont également disponibles.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.viewIsometric()
```



---
⏵ [documentation index](../README.md) > Std ViewIsometric/fr
