# Sketcher SketchObject/fr
## Introduction

<img alt="" src=images/Sketcher_Sketch.svg  style="width:32px;">

Un [Sketcher SketchObject](Sketcher_SketchObject/fr.md), ou formellement un `Sketcher::SketchObject`, est l\'élément de base pour créer des objets 2D avec l\'[atelier Sketcher](Sketcher_Workbench/fr.md).


`Sketcher::SketchObject`

est dérivé de [Part Part2DObject](Part_Part2DObject/fr.md). Cela signifie qu\'il s\'agit d\'un objet [Part Feature](Part_Feature/fr.md) spécialisé dans la géométrie 2D. Comme Part2DObject, l\'objet SketchObject peut être attaché à des plans et à des faces. En plus de cela, SketchObject peut gérer les contraintes géométriques des lignes et des courbes qui y sont dessinées.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux dans Freecad*



## Utilisation

Voir [Sketcher Créer une esquisse](Sketcher_NewSketch/fr.md).



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

-    **Grid Auto|Bool**: si `True`, la grille est redimensionnée en fonction de la boîte de délimitation de la géométrie de l\'esquisse.

-    **Grid Size|Length**: la taille de l\'espacement des lignes de la grille locale dans la [vue 3D](3D_view/fr.md) ; la valeur par défaut est {{value|10 mm}}.

-    **Show Grid|Bool**: si `True`, une grille locale à l\'objet sera affichée dans la [vue 3D](3D_view/fr.md). Cette grille est indépendante de la [Draft Grille](Draft_ToggleGrid/fr.md).


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



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SketchObject/fr
