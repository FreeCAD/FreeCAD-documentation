# App DocumentObject/fr
{{TOCright}}

## Introduction

<img alt="" src=images/Px.svg  style="width:32px;">

Un objet [App DocumentObject](App_DocumentObject/fr.md), ou officiellement `App::DocumentObject`, est la classe de base de toutes les classes d\'objets gérées dans le document.

De manière générale, un \"DocumentObject\" est toute \"chose\" qui peut apparaître dans la [vue en arborescence](tree_view/fr.md) et qui est enregistrée et restaurée lors de l\'ouverture d\'un document.

![](images/App_DocumentObject_example.png )



*Vue arborescente montrant différents objets dans le document. Chacun d'eux est un "document object", finalement dérivé de la classe `App::DocumentObject* base.`

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux du programme. La classe `App::DocumentObject* est la classe de base de pratiquement tous les objets du logiciel.`

## Utilisation

[App DocumentObject](App_DocumentObject/fr.md) est une classe interne, elle ne peut donc pas être créée à partir de l\'interface graphique, ni destinée à être utilisée seule. Il définit simplement le comportement de base et les propriétés des objets dans le logiciel.

Certains des DocumentObjects les plus importants sont les suivants:

-   La classe [App FeaturePython](App_FeaturePython/fr.md), un objet vide qui peut être utilisé à différentes fins, en fonction des propriétés ajoutées.
-   La classe [App GeoFeature](App_GeoFeature/fr.md) , l\'objet de base de tous les objets géométriques, c\'est-à-dire des objets qui ont une propriété [Placement](Placement/fr.md) qui définit leur position dans la \[\[3D view/fr\|vue 3D\] \].
-   La classe [Part Feature](Part_Feature/fr.md), dérivée d\'App GeoFeature, et la classe parent d\'objets avec 2D et 3D [topological shapes](Part_TopoShape/fr.md).
-   La classe [Mesh Feature](Mesh_Feature/fr.md), dérivée d\'App GeoFeature, et la classe parent d\'objets avec 2D et 3D [meshes](Mesh_MeshObject/fr.md).

## Propriétés

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets crées par script peuvent avoir.

Ce sont les propriétés de base que possèdent essentiellement tous les objets. Ces propriétés sont accessibles depuis la [console Python](Python_console/fr.md).

-    {{PropertyData/fr|Expression Engine|ExpressionEngine}}: une liste d\'expressions.

-    {{PropertyData/fr|Label|String}}: le nom modifiable par l\'utilisateur de cet objet, il s\'agit d\'une chaîne UTF8 arbitraire. Par défaut, c\'est la même chose que `Name`.

-    {{PropertyData/fr|Label2|String}}: description plus longue et modifiable par l\'utilisateur de cet objet, il s\'agit d\'une chaîne UTF8 arbitraire qui peut inclure des retours à la ligne. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    {{PropertyData/fr|Visibility|Bool}}: afficher ou non l\'objet.

Pour les objets dérivés, seul {{PropertyData/fr|Label}} sera répertoriée par défaut dans l\'[ éditeur de propriété](property_editor/fr.md). Les autres propriétés seront masquées.

## Script


**Voir aussi:**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au programme.

Un DocumentObject est créé avec la méthode `addObject()` du document. Cependant, en général, il n\'est pas nécessaire de créer cet objet manuellement. Il est généralement préférable de sous-classer l\'une des sous-classes les plus complexes, par exemple, [App FeaturePython](App_FeaturePython/fr.md), [App GeoFeature](App_GeoFeature/fr.md), [\|Part Feature](Part_Feature/fr.md), [Part Part2DObject](Part_Part2DObject/fr.md), etc.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObject", "Name")
obj.Label = "Custom label"
```


{{Document objects navi

}}

---
[documentation index](../README.md) > App DocumentObject/fr
