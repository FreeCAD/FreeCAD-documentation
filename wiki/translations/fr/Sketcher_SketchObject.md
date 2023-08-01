# Sketcher SketchObject/fr
## Introduction

<img alt="" src=images/Sketcher_Sketch.svg  style="width:32px;">

Un [Sketcher SketchObject](Sketcher_SketchObject/fr.md), ou formellement un `Sketcher::SketchObject`, est l\'élément de base pour créer des objets 2D avec l\'[Atelier Sketcher](Sketcher_Workbench/fr.md).


`Sketcher::SketchObject`

est dérivé de [Part Part2DObject](Part_Part2DObject/fr.md). Cela signifie qu\'il s\'agit d\'un objet [Part Feature](Part_Feature/fr.md) spécialisé dans la géométrie 2D. Comme Part2DObject, l\'objet SketchObject peut être attaché à des plans et à des faces. En plus de cela, SketchObject peut gérer les contraintes géométriques des lignes et des courbes qui y sont dessinées.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux dans Freecad*



## Utilisation

1.  Basculez vers l\'[Atelier Sketcher](Sketcher_Workbench/fr.md).
2.  Appuyez sur **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)**.
3.  Sélectionnez une **Orientation de l'esquisse**: plan XY, plan XZ ou plan YZ. Vous pouvez également choisir d\'**Inverser la direction** et donner une valeur de **Décalage**.
4.  Appuyez sur **OK**.

Bien que SketchObject puisse être utilisé seul pour dessiner sur un plan, il est le plus souvent utilisé conjointement avec l\'[Atelier PartDesign](PartDesign_Workbench/fr.md) pour créer des solides extrudés.

1.  Basculer vers l\'[Atelier PartDesign](PartDesign_Workbench/fr.md).

2.  Appuyez sur **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Corps](PartDesign_Body/fr.md)**.

3.  Appuyez sur **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Nouvelle esquisse](PartDesign_NewSketch/fr.md)**.

4.  
    **Fonction sélectionnée**: XY_Plane (Plan de base), XZ_Plane (Plan de base) ou YZ_Plane (Plan de base).

5.  Appuyez sur **OK**.



## Propriétés

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets scriptés peuvent avoir.

[Sketcher SketchObject](Sketcher_SketchObject/fr.md) (classe `Sketcher::SketchObject`) est dérivé de [Part Part2DObject](Part_Part2DObject/fr.md) (classe `Part::Part2DObject`) et hérite de toutes ses propriétés.

Le SketchObject possède également les propriétés supplémentaires suivantes dans l\'[éditeur de propriétés](Property_editor/fr.md). Les propriétés cachées peuvent être affichées à l\'aide de la commande **Show all** du menu contextuel de l\'[éditeur de propriétés](Property_editor/fr.md).



### Données


{{TitleProperty|Sketch}}

-    **Geometry|GeometryList|Hidden**: une liste des géométries de Part qui existent dans l\'esquisse.

-    **Constraints|**: contraintes nommées, si elles existent ; sinon, il s\'agit d\'une liste vide `[]`.

-    **External Geometry|LinkSubList**: une liste de géométries de pièces extérieures à cette esquisse qui sont utilisées comme référence.

-    **Fully Constrained|Bool|Hidden**: (en lecture seule) si `True` l\'esquisse est entièrement contrainte.



### Vue


{{TitleProperty|Auto Constraints}}

-    **Autoconstraints|Bool**: si `True` les contraintes sont automatiquement ajoutées lorsque la géométrie est dessinée.

-    **Avoid Redundant|Bool**: si `True` les contraintes automatiques redondantes sont évitées.


{{TitleProperty|Grid}}

-    **Grid Auto Size|Bool|Hidden**: si `True`, la grille est redimensionnée en fonction de la boîte de délimitation de la géométrie de l\'esquisse.

-    **Grid Size|Length**: la taille de l\'espacement des lignes de la grille locale dans la [Vue 3D](3D_view/fr.md) ; la valeur par défaut est {{value|10 mm}}.

-    **Grid Snap|Bool**: si `True`, la grille peut être utilisée pour fixer des points.

-    **Grid Style|Enumeration**: le style des lignes de la grille ; {{value|Dashed}} (par défaut) ou {{value|Light}}.

-    **Show Grid|Bool**: si `True`, une grille locale à l\'objet sera affichée dans la [Vue 3D](3D_view/fr.md). Cette grille est indépendante de la [Draft Grille](Draft_ToggleGrid/fr.md).

-    **Show Only In Edit Mode|Bool**: si `True`, la grille n\'est affichée que lorsque l\'esquisse est en cours d\'édition.

-    **Tight Grid|Bool**: si `True` la grille locale sera localisée autour de l\'origine de la forme, sinon elle s\'étendra davantage.

-    **max Number Of Lines|Integer**: le nombre maximum de lignes dans la grille.


{{TitleProperty|Visibility automation}}

-    **Editing Workbench|String**: nom de l\'atelier à activer lors de l\'édition de l\'esquisse ; la valeur par défaut est {{value|SketcherWorkbench}}.

-    **Force Ortho|Bool**: si `True`, la caméra sera forcée à [mode de vue orthographique](Std_OrthographicCamera/fr.md) lorsque l\'esquisse est ouverte.

-    **Hide Dependent|Bool**: si `True`, tous les objets qui dépendent de l\'esquisse sont masqués lorsque l\'esquisse est ouverte.

-    **Restore Camera|Bool**: si `True`, la position de la caméra est enregistrée avant l\'ouverture de l\'esquisse et est restaurée après sa fermeture.

-    **Section View|Bool**: si `True`, seuls les (parties des) objets situés derrière le plan de l\'esquisse sont visibles pendant l\'édition de l\'esquisse.

-    **Show Links|Bool**: si `True`, tous les objets utilisés dans les liens vers la géométrie externe sont affichés à l\'ouverture de l\'esquisse.

-    **Show Support|Bool**: si `True`, tous les objets auxquels cette esquisse est attachée sont affichés lorsque l\'esquisse est ouverte.

-    **Tempo Vis|PythonObject|Hidden**: une classe personnalisée associée à cet objet, qui gère le masquage et l\'affichage d\'autres objets lors de l\'ouverture et de la fermeture de l\'esquisse.



## Création de scripts 


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](Scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au document.

Un SketchObject est créé avec la méthode `addObject()` du document.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher::SketchObject", "Sketch")
obj.Label = "Custom label"
```

Pour la sous-classification de [Python](Python/fr.md), vous devez créer l\'objet `Sketcher::SketchObjectPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher::SketchObjectPython", "CustomSketch")
obj.Label = "Custom label"
```


{{Sketcher_Tools_navi

}} {{Document_objects_navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SketchObject/fr
