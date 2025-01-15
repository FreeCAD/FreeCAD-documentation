# Part Part2DObject/fr
## Introduction

<img alt="" src=images/Tree_Part2D.svg  style="width:32px;">

[Part Part2DObject](Part_Part2DObject/fr.md), ou formellement un `Part::Part2DObject`, est un élément simple associé à une [une forme topologique](Part_TopoShape/fr.md) qui peut être affiché dans la [Vue 3D](3D_view/fr.md).

Le `Part::Part2DObject` est dérivé de [Part Feature](Part_Feature/fr.md) mais est spécialisé pour la géométrie 2D, étant donné que sa forme reposera sur un plan. Ce plan est défini par sa propriété **Placement** (position, normale et rotation). Cependant, le plan peut également être défini en prenant en charge des éléments géométriques, tel que le plan créé par trois sommets arbitraires ou une face d\'un corps solide.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux dans Freecad*

## Utilisation

[Part Part2DObject](Part_Part2DObject/fr.md) est un objet interne. Par conséquent, il ne peut pas être créé à partir de l\'interface graphique, uniquement à partir de la [Console Python](Python_console/fr.md), comme décrit dans la section [Script](#Script.md).


`Part::Part2DObject`

est défini dans l\'[atelier Part](Part_Workbench/fr.md) mais peut être utilisé comme classe de base pour les [Objets créés par script](Scripted_objects/fr.md) dans tous les [Ateliers](Workbenches/fr.md) qui produisent des formes géométriques 2D. Par exemple, c\'est l\'objet de base pour les esquisses ([Sketcher SketchObject](Sketcher_SketchObject/fr.md)), et pour la plupart des objets créés avec l\'[atelier Draft](Draft_Workbench.md).

Des ateliers peuvent ajouter plus de propriétés à cet élément de base pour produire un objet au comportement complexe.

## Propriétés

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets scriptés peuvent avoir.

[Part Part2DObject](Part_Part2DObject/fr.md) (de classe `Part::Part2DObject`) est dérivé de [Part Feature](Part_Feature/fr.md) (de classe `Part::Feature`) et hérite de toutes ses propriétés.

Le Part2DObject possède également les propriétés supplémentaires suivantes dans l\'[éditeur de propriétés](Property_editor/fr.md). Les propriétés cachées peuvent être affichées à l\'aide de la commande **Show all** du menu contextuel de l\'[éditeur de propriétés](Property_editor/fr.md).

### Données


{{TitleProperty|Attachment}}

-    <div id="Property_Attacher_Type">
    </div>
    **Attacher Type|String|Hidden**: nom de la classe de l\'objet moteur de l\'attachement. La valeur par défaut est `Attacher::AttachEnginePlane`.

-    <div id="Property_Support">
    </div>
    **Support|LinkSubList**: il s\'agit du plan ou de la face supportant la géométrie 2D. Par défaut, il s\'agit d\'une liste vide `[]`.

-    <div id="Property_Map_Mode">
    </div>
    **Map Mode|Enumeration**: {{value|Deactivated}} par défaut. Cette propriété détermine un plan que l\'objet utilisera comme référence pour la géométrie 2D. En cliquant sur l\'ellipse **...** (trois points), à droite du champ de saisie, lance la commande [Part Ancrage](Part_EditAttachment/fr.md) qui permet de sélectionner le plan de référence en choisissant différents éléments dans la [Vue 3D](3D_view/fr.md). Les différents modes sont : {{value|Deactivated}}, {{value|Translate origin}}, {{value|Object's XY}}, {{value|Object's XZ}}, {{value|Object's YZ}}, {{value|Plane face}}, {{value|Tangent to surface}}, {{value|Normal to edge}}, {{value|Frenet NB}}, {{value|Frenet TN}}, {{value|Frenet TB}}, {{value|Concentric}}, {{value|Revolution section}}, {{value|Plane by 3 points}}, {{value|Normal to 3 points}}, {{value|Folding}}, {{value|Inertia 2-3}}, {{value|Align O-N-X}}, {{value|Align O-N-Y}}, {{value|Align O-X-Y}}, {{value|Align O-X-N}}, {{value|Align O-Y-N}}, {{value|Align O-Y-X}}.

-    <div id="Property_Map_Reversed">
    </div>
    **Map Reversed|Bool**: sa valeur par défaut est `False` ; si elle est `True`, la direction Z sera inversée. Par exemple, une [esquisse](sketch/fr.md) sera retournée à l\'envers. Caché si **Map Mode** est {{value|Deactivated}}.

-    <div id="Property_Map_Path">
    </div>
    **Map Path Parameter|Float|Hidden**: définit le point de la courbe vers lequel mapper une [esquisse](sketch/fr.md). Il va de {{value|0}} à {{value|1}}, qui correspondent aux {{value|start}} et {{value|end}}. La valeur par défaut est {{value|0}}.

-    <div id="Property_Attachment_Offset">
    </div>
    **Attachment Offset|Placement**: la position de l\'objet dans la [Vue 3D](3D_view/fr.md), par rapport au placement de l\'objet d\'attachement. L\'emplacement est défini par un point `Base` (vecteur) et un `Rotation` (axe et angle). Voir [Placement](Placement/fr.md). Masqué si **Map Mode** est {{value|Deactivated}}.

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](Scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au document.

Un Part2DObject est créé avec la méthode `addObject()` du document.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObject", "Name")
obj.Label = "Custom label"
```

Pour la sous-classification de [Python](Python/fr.md), vous devez créer l\'objet `Part::Part2DObjectPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObjectPython", "Name")
obj.Label = "Custom label"
```



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Part2DObject/fr
