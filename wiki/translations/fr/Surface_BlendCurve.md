---
- GuiCommand:
   Name: Surface BlendCurve
   Name/fr: Surface Fusion de courbes
   MenuLocation: Surface -> Fusionner des courbes
   Workbenches: Surface_Workbench/fr
   Version: 0.21
---

# Surface BlendCurve/fr

## Description


**[<img src=images/Surface_BlendCurve.svg style="width:16px"> [Surface Fusion de courbes](Surface_BlendCurve/fr.md)**

crée une courbe de Bézier entre deux arêtes, avec la continuité souhaitée.

La géométrie de base peut appartenir à des courbes créées avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md), mais aussi à des objets solides tels que ceux créés avec l\'[atelier Part](Part_Workbench/fr.md).

<img alt="" src=images/Surface_BlendCurve_G3_example.png  style="width:400px;"> <img alt="" src=images/Surface_BlendCurve_Comb.png  style="width:400px;"> 
*Surface Fusion de courbes reliant 2 arêtes avec une continuité G3. Les polygones orange représentent les points de contrôle. Le peigne de courbure (de l'[extension Curves](Curves_Workbench/fr.md)) est lisse aux points de contact.*



## Utilisation

1.  Sélectionnez deux arêtes dans la [vue 3D](3D_view/fr.md).
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Surface_BlendCurve.svg" width=16px> [Fusionner des courbes](Surface_BlendCurve/fr.md)**.
    -   Sélectionnez l\'option **Surface → <img src="images/Surface_BlendCurve.svg" width=16px> Fusionner des courbes** du menu.
3.  Ajustez la forme de la courbe dans les propriétés Data de l\'objet.



## Propriétés

[Surface Fusion de courbes](Surface_BlendCurve/fr.md) (classe `Surface::Filling`) est dérivée de la classe de base [Part Feature](Part_Feature/fr.md) (classe `Part::Feature` via la sous-classe `Part::Spline`), elle partage donc toutes les propriétés de cette dernière.

Outre les propriétés décrites dans [Part Feature](Part_Feature/fr.md), Surface Fusion de courbes a les propriétés suivantes dans l\'[éditeur de propriétés](property_editor/fr.md).



### Données


{{TitleProperty|Blend Curve}}

-    **Start Edge|LinkSub**: premier bord d\'entrée.

-    **Start Continuity|Integer**: valeur de continuité géométrique

-    **Start Parameter|Float**: paramètre normalisé le long de l\'arête, de {{Value|0.0}} (début de l\'arête) à {{Value|1.0}} (fin de l\'arête).

-    **Start Size|Float**: taille de la tangente.

-    **End Edge|LinkSub**: deuxième arête d\'entrée.

-    **End Continuity|Integer**: valeur de continuité géométrique

-    **End Parameter|Float**: paramètre normalisé le long de l\'arête, de {{Value|0.0}} (début de l\'arête) à {{Value|1.0}} (fin de l\'arête).

-    **End Size|Float**: taille de la tangente.



### Vue


{{TitleProperty|Base}}

-    **Control Points|Bool**: par défaut `False`. Mis à `True`, elle affichera une superposition avec les points de contrôle de la surface.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Fusion de courbes peut être utilisé dans les [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) en ajoutant l\'objet `Surface::FeatureBlendCurve`.

-   Les arêtes à utiliser pour définir la courbe doivent être assignées en tant que [LinkSub](LinkSub/fr.md) aux propriétés `StartEdge` et `EndEdge` de l\'objet.
-   Tous les objets dotés d\'arêtes doivent être calculés avant de pouvoir être utilisés comme entrée pour les propriétés de l\'objet Fusion de courbes.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

points1 = [App.Vector(-20, -20, 0), App.Vector(-20, -8, 0), App.Vector(-17, 7, 0), App.Vector(-18, 25, 0)]
obj1 = Draft.make_bspline(points1)

points2 = [App.Vector(60, 26, 0), App.Vector(37, 4, 0), App.Vector(33, -20, 0)]
obj2 = Draft.make_bspline(points2)

doc.recompute()

bcurve = doc.addObject("Surface::FeatureBlendCurve","BlendCurve")
bcurve.StartEdge = (obj1, 'Edge1')
bcurve.EndEdge = (obj2, 'Edge1')
bcurve.EndParameter = 1.00
bcurve.StartSize = -5.00
bcurve.EndSize = -5.00

doc.recompute()
```





{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface BlendCurve/fr
