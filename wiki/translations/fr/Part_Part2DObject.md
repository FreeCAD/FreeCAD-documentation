# Part Part2DObject/fr



## Introduction

<img alt="" src=images/Tree_Part2D.svg  style="width:32px;">

Un objet [Part Part2DObject](Part_Part2DObject/fr.md) ou formellement un `Part::Part2DObject`, est un élément simple associé à une [une forme topologique](Part_TopoShape/fr.md) qui peut être affiché dans la [Vue 3D](3D_view/fr.md).

Le `Part::Part2DObject` est dérivé d\'un [Part Feature](Part_Feature/fr.md) mais est spécialisé pour la géométrie 2D, étant donné que sa forme reposera sur un plan. Ce plan est défini par sa propriété **Placement** (position, normale et rotation). Cependant, le plan peut également être défini en prenant en charge des éléments géométriques, tel que le plan créé par trois sommets arbitraires ou une face d\'un corps solide.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Diagramme simplifié des relations entre les objets centraux du programme. La classe `Part::Part2DObject* est spécialisée pour les formes 2D, c'est donc la classe de base pour les objets plans créés avec les ateliers Draft et Sketcher. Il comprend une extension qui lui permet d'être attaché aux faces et aux plans.`

## Utilisation

[Part Part2DObject](Part_Part2DObject/fr.md) est un objet interne. Par conséquent, il ne peut pas être créé à partir de l\'interface graphique, uniquement à partir de la [Console Python](Python_console/fr.md), comme décrit dans la section [Script](Part_Feature#Script.md).


`Part::Part2DObject`

est défini dans l\'[atelier Part](Part_Workbench/fr.md) mais peut être utilisé comme classe de base pour les [Objets créés par script](scripted_objects/fr.md) dans tous les [Ateliers](Workbenches/fr.md) qui produisent des formes géométriques 2D. Par exemple, c\'est l\'objet de base pour les esquisses ([Sketcher SketchObject](Sketcher_SketchObject/fr.md)), et pour la plupart des objets créés avec l\'[atelier Draft](Draft_Workbench.md).

Des ateliers peuvent ajouter plus de propriétés à cet élément de base pour produire un objet au comportement complexe.

## Propriétés

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets scriptés peuvent avoir.

Un [Part Part2DObject](Part_Part2DObject/fr.md) (de classe `Part::Part2DObject`) est dérivé d\'un [Part Feature](Part_Feature/fr.md) (de classe `Part::Feature`) de fait, il partage toutes les propriétés de cette dernière.

Outre les propriétés décrites dans [Part Feature](Part_Feature/fr.md), le corps de PartDesign a les propriétés suivantes dans l\'[éditeur de propriétés](property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Show all** dans le menu contextuel de l\'[éditeur de propriétés](property_editor/fr.md).

### Données


{{TitleProperty|Attachment}}

-    {{PropertyData/fr|Map Mode|Enumeration}}: {{value|Deactivated}} \"Désactivé\" par défaut. Cette propriété détermine un plan que l\'objet utilisera comme référence pour la géométrie 2D. En cliquant sur l\'ellipse **...**, à droite du champ de saisie, s\'ouvre le [Panneau des tâches](Task_panel/fr.md) de [Part Ancrage](Part_EditAttachment/fr.md) qui permet de sélectionner le plan de support en sélectionnant différents éléments dans le panneau de tâches [Vue 3D](3D_view/fr.md). Les différents modes sont: {{value|Deactivated}}, {{value|Translate origin}}, {{value|Object's XY}}, {{value|Object's XZ}}, {{value|Object's YZ}}, {{value|Plane face}}, {{value|Tangent to surface}}, {{value|Normal to edge}}, {{value|Frenet NB}}, {{value|Frenet TN}}, {{value|Frenet TB}}, {{value|Concentric}}, {{value|Revolution section}}, {{value|Plane by 3 points}}, {{value|Normal to 3 points}}, {{value|Folding}}, {{value|Inertia 2-3}}, {{value|Align O-N-X}}, {{value|Align O-N-Y}}, {{value|Align O-X-Y}}, {{value|Align O-X-N}}, {{value|Align O-Y-N}}, {{value|Align O-Y-X}}.

Voir [Part Ancrage](Part_EditAttachment/fr.md) pour plus d\'informations sur tous les modes de mappage.

Les deux propriétés suivantes sont normalement masquées. Ils deviennent visibles une fois que {{PropertyData/fr|Map Mode}} est autre chose que {{value|Deactivated}}.

-    {{PropertyData/fr|Map Reversed|Bool}}: par défaut à `False`, s\'il est à `True`, la direction Z sera inversée. Par exemple, un [sketch](sketch/fr.md) sera mis à l\'envers.

-    {{PropertyData/fr|Attachment Offset|Placement}}: la position de l\'objet dans la [vue 3D](3D_view/fr.md) par rapport au placement de l\'objet attaché. Le placement est défini par un point `Base` (vecteur) et `Rotation` (axe et angle). Voir [Positionnement](Placement/fr.md).

##### Propriétés cachées de Données 


{{TitleProperty|Base}}

-    {{PropertyData/fr|Proxy|PythonObject}}: classe personnalisée associée à cet objet. Cela n\'existe que pour la version [Python](Python/fr.md). Voir [Script](Part_Part2DObject/fr#Script.md).


{{TitleProperty|Attachment}}

-    {{PropertyData/fr|Attacher Type|String}}: nom de classe de l\'objet moteur d\'attachement qui pilote l\'ancrage. Par défaut `Attacher::AttachEnginePlane`.

-    {{PropertyData/fr|Support|LinkSubList}}: c\'est le plan ou la face supportant la géométrie 2D. Par défaut, une liste vide `[]`.

-    {{PropertyData/fr|Map Path Parameter|Float}}: définit le point de la courbe sur laquelle mapper une [Esquisse](sketch/fr.md). Il va de {{value|0}} à {{value|1}}, ce qui correspond aux {{value|start}} et {{value|end}}. Par défaut {{value|0}}.

### Vue


{{TitleProperty|Grid}}

-    {{PropertyView/fr|Grid Size|Length}}: une valeur flottante qui détermine la taille de l\'espacement des lignes de grille locales dans la [Vue 3D](3D_view/fr.md). Par défaut {{value|10 mm}}.

-    {{PropertyView/fr|Grid Snap|Bool}}: par défaut `False`. Si mis à `True`, la grille peut être utilisée pour capturer des points.

-    {{PropertyView/fr|Grid Style|Enumeration}}: le style des lignes de la grille :{{value|Dashed}} (default) ou {{value|Light}}.

-    {{PropertyView/fr|Show Grid|Bool}}: par défaut `False`. Si mis à `True`, une grille locale à l\'objet sera affichée dans la [Vue 3D](3D_view/fr.md). Cette grille est indépendante de la [Bascule de l\'affichage de la grille](Draft_ToggleGrid/fr.md).

-    {{PropertyView/fr|Tight Grid|Bool}}: si mis à `True`, valeur par defaut, la grille locale sera localisée autour de l\'origine de la forme, sinon elle se prolongera davantage.

##### Propriétés cachées de Données 


{{TitleProperty/fr|Base}}

-    {{PropertyView/fr|Proxy|PythonObject}}: classe personnalisée associée à cet objet. Cela n\'existe que pour la version [Python](Python/fr.md). Voir [Script](Part_Part2DObject/fr#Script.md).

Toutes les autres propriétés de vue, y compris les propriétés masquées, sont celles de l\'objet de base [Part Feature](Part_Feature/fr.md)

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md), et [objet scripté](scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au document.

Un Part2DObject est créé avec la méthode `addObject()` du document. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObject", "Name")
obj.Label = "Custom label"
```

Ce `Part::Feature` de base n\'a pas d\'objet Proxy, il ne peut donc pas être entièrement utilisé pour la sous-classification.

Par conséquent, pour la sous-classe [Python](Python/fr.md), vous devez créer l\'objet `Part::Part2DObjectPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObjectPython", "Name")
obj.Label = "Custom label"
```

Par exemple, la plupart des outils de [Atelier Draft](Draft_Workbench/fr.md), comme [Draft Ligne](Draft_Line/fr.md), [Draft Rectangle](Draft_Rectangle/fr.md), [Draft Polygone](Draft_Polygon/fr.md) etc\... sont des objets `Part::Part2DObjectPython` avec une icône personnalisée et des propriétés supplémentaires.


  
