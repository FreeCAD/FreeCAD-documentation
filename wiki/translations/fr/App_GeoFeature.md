# App GeoFeature/fr
## Introduction

<img alt="" src=images/Feature.svg  style="width:32px;">

Un objet [App GeoFeature](App_GeoFeature/fr.md), ou officiellement `App::GeoFeature`, est la classe de base de la plupart des objets qui afficheront des éléments géométriques dans la [Vue 3D](3D_view/fr.md) car il inclut une propriété **Placement**.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux dans Freecad*

## Utilisation

[App GeoFeature](App_GeoFeature/fr.md) est un objet interne, il ne peut donc pas être créé à partir de l\'interface graphique. Il n\'est généralement pas destiné à être utilisé directement, mais il peut plutôt être sous-classé pour obtenir un objet nu qui n\'a qu\'une propriété **Placement** de base pour définir sa position dans la [vue 3D](3D_view/fr.md).

Certains des objets dérivés les plus importants sont les suivants:

-   La classe [Part Feature](Part_Feature/fr.md), le parent de la plupart des objets 2D et 3D [formes topologiques](Part_TopoShape/fr.md).
-   La classe [Mesh Feature](Mesh_Feature/fr.md), le parent de la plupart des objets fabriqués à partir de [maillages](Mesh_MeshObject/fr.md), pas des solides.
-   La classe [Fem FemMeshObject](FEM_Mesh/fr.md), le parent des maillages d\'éléments finis créés avec l\'[atelier FEM](FEM_Workbench/fr.md).
-   La classe [Path Feature](Path_Feature/fr.md), le parent des chemins créés avec l\'[atelier Path](Path_Workbench/fr.md) pour une utilisation dans l\'usinage CNC.
-   La classe [App Part](App_Part/fr.md), qui définit [Std Parts](Std_Part/fr.md) qui peut être utilisée comme conteneurs de corps pour effectuer des assemblages.

Lorsque vous créez cet objet dans [Python](Python/fr.md), au lieu de sous-classer `App::GeoFeature`, vous devez sous-classer `App::GeometryPython` car ce dernier inclut une valeur par défaut fournisseur de vues et attributs `Proxy` pour l\'objet lui-même et son fournisseur de vues. Voir [Script](App_GeoFeature/fr#Script.md).

## Propriétés App GeoFeature 

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets crées par script peuvent avoir.

[App GeoFeature](App_GeoFeature/fr.md) (classe `App::GeoFeature`) est dérivée de la classe de base [App DocumentObject](App_DocumentObject/fr.md). (classe `App::DocumentObject`) et hérite de toutes ses propriétés. En outre, il possède une propriété **Placement**, qui contrôle sa position dans la [vue 3D](3D_view.md).

## Propriétés App GeometryPython 

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets scriptés peuvent avoir.

La classe [App GeometryPython](App_GeoFeature/fr.md) (classe `App::GeometryPython`) est dérivée de la classe de base [App GeoFeature](App_GeoFeature/fr.md) (classe `App::GeoFeature`) et hérite de toutes ses propriétés. Elle possède également plusieurs propriétés supplémentaires.

Ce sont les propriétés disponibles dans l\'[éditeur de propriétés](Property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Show all** dans le menu contextuel de l\'[éditeur de propriétés](Property_editor/fr.md).

### Données


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: une classe personnalisée associée à cet objet.

-    **Placement|Placement**: la position de l\'objet dans la [Vue 3D](3D_view/fr.md). Le placement est défini par un point `Base` (vecteur) et un `Rotation` (axe et angle). Voir [Positionnement](Placement/fr.md).

    -   
        **Angle**
        
        : l\'angle de rotation autour de **Axis**. Par défaut {{value|0°}} (zéro degré).

    -   
        **Axis**
        
        : le vecteur unitaire qui définit l\'axe de rotation pour le placement. Chaque composant est une valeur à virgule flottante entre {{value|0}} et {{value|1}}. Si une valeur est supérieure à {{value|1}}, le vecteur est normalisé de sorte que l\'amplitude du vecteur est {{value|1}}. Par défaut, il s\'agit de l\'axe Z positif, {{value|(0, 0, 1)}}.

    -   
        **Position**
        
        : un vecteur avec les coordonnées 3D du point de base. Par défaut, c\'est l\'origine {{value|(0, 0, 0)}}.

-    **Label|String**: le nom modifiable par l\'utilisateur de cet objet, il s\'agit d\'une chaîne UTF8 arbitraire.

-    **Label2|String|Hidden**: une description plus longue, modifiable par l\'utilisateur, de cet objet. Il s\'agit d\'une chaîne UTF8 arbitraire qui peut inclure des nouvelles lignes. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: une liste d\'expressions. Par défaut, elle est vide {{value|[]}}.

-    **Visibility|Bool|Hidden**: affichage ou non de l\'objet.

### Vue


{{TitleProperty|Base}}

-    **Proxy|PythonObject|hidden**: une classe personnalisée de [viewprovider](Viewprovider/fr.md) associée à cet objet.


{{TitleProperty|Display Options}}

-    **Bounding Box|Bool**: mis à `True`, l\'objet affichera le cadre de délimitation dans la [Vue 3D](3D_view/fr.md).

-    **Display Mode|Enumeration**: voir les informations dans [App FeaturePython](App_FeaturePython/fr.md).

-    **Show In Tree|Bool**: voir les informations dans [App FeaturePython](App_FeaturePython/fr.md).

-    **Visibility|Bool**: voir les informations dans [App FeaturePython](App_FeaturePython/fr.md).


{{TitleProperty|Object Style}}

-    **Shape Color|Color**: un tuple de trois valeurs RVB à virgule flottante  light gray .

-    **Shape Material|Material|Hidden**: un [App Material](App_Material/fr.md) associé à cet objet. Par defaut, vide.

-    **Transparency|Percent**: un entier de {{value|0}} à {{value|100}} qui détermine le niveau de transparence des faces dans la [Vue 3D](3D_view/fr.md). Une valeur de {{value|100}} indique des faces complètement invisibles. Les faces sont invisibles mais elles peuvent toujours être sélectionnées tant que **Selectable** est `True`.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: voir les informations dans [App FeaturePython](App_FeaturePython/fr.md).

-    **Selectable|Bool**: s\'il est `True`, l\'objet peut être sélectionné avec le pointeur dans la [Vue 3D](3D_view/fr.md). Sinon, l\'objet ne peut pas être sélectionné tant que cette option n\'est pas définie sur `True`.

-    **Selection Style|Enumeration**: voir les informations dans [App FeaturePython](App_FeaturePython/fr.md).

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](Scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au document.

Un GeoFeature est créé avec la méthode `addObject()` du document. Si vous souhaitez créer un objet avec une 2D ou 3D [forme topologique](Part_TopoShape/fr.md), il peut être préférable de créer l\'une des sous-classes spécialisées pour la manipulation des formes, par exemple, [Part Feature](Part_Feature/fr.md) ou [Part Part2DObject](Part_Part2DObject/fr.md).


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeoFeature", "Name")
obj.Label = "Custom label"
```

Pour la sous-classification de [Python](Python/fr.md), vous devez créer l\'objet `App::GeometryPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeometryPython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > App GeoFeature/fr
