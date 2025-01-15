# Mesh Feature/fr
## Introduction

<img alt="" src=images/Mesh_Tree.svg  style="width:32px;">

Un objet [Mesh Feature](Mesh_Feature/fr.md), ou formellement un `Mesh::Feature`, est un élément simple avec un [objet de maillage](Mesh_MeshObject/fr.md) associé qui peut être affiché dans la [vue 3D](3D_view/fr.md).

Une fonction de maillage (Mesh Feature) est conceptuellement similaire à une [Part Feature](Part_Feature/fr.md). Le premier est l\'objet de base pour les éléments avec des informations de \"maillage\", tandis que le second est l\'objet de base pour les éléments avec des informations de \"forme géométrique\".

Notez que l\'**<img src="images/Workbench_FEM.svg" width=16px> [atelier FEM](FEM_Workbench/fr.md)** utilise également des maillages, mais dans ce cas, il utilise un objet différent, appelé [FEM FemMeshObject](FEM_Mesh/fr.md) (classe `Fem::FemMeshObject`). Cet objet n\'est pas dérivé de la fonction de maillage et possède des propriétés différentes.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux dans Freecad*



## Utilisation

Presque tous les objets maillés créés par les commandes disponibles dans l\'interface graphique de l\'[atelier Mesh](Mesh_Workbench/fr.md) sont des [Mesh Features](Mesh_Feature/fr.md). Les objets maillés paramétriques créés par la commande [Mesh Solide régulier](Mesh_BuildRegularSolid/fr.md) sont les seules exceptions. Un [Mesh Feature](Mesh_Feature/fr.md) peut également être créé à partir de la [console Python](Python_console/fr.md) comme décrit dans la section [Script](Mesh_Feature/fr#Script.md).

L\'objet `Mesh::Feature` est défini dans l\'[atelier Mesh](Mesh_Workbench/fr.md) mais peut être utilisé comme classe de base pour les [objets scriptés](Scripted_objects/fr.md) dans tous les [ateliers](Workbenches/fr.md) générant des formes géométriques 2D et 3D.

Un `Mesh::Feature` a des propriétés simples comme un [placement](Placement/fr.md) et des propriétés visuelles pour définir l\'apparence de ses arêtes et faces.



## Propriétés

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets crées par script peuvent avoir.

La classe [Mesh Feature](Mesh_Feature/fr.md) (classe `Mesh::Feature`) est dérivée de [App GeoFeature](App_GeoFeature/fr.md) de base. (classe `App::GeoFeature`) et hérite de toutes ses propriétés. Elle possède également plusieurs propriétés supplémentaires, notamment une propriété **Mesh**, qui stocke son [Mesh MeshObject](Mesh_MeshObject/fr.md). Il s\'agit de la géométrie qui est affichée dans la [vue 3D](3D_view/fr.md).

Ce sont les propriétés disponibles dans l\'[éditeur de propriétés](Property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Tout afficher** dans le menu contextuel de l\'[éditeur de propriétés](Property_editor/fr.md).



### Données


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: une classe personnalisée associée à cet objet. Ceci n\'existe que pour la version en [Python](Python/fr.md). Voir [Script](#Script.md).

-    **Mesh|MeshKernel**: une classe [Mesh MeshObject](Mesh_MeshObject/fr.md) associée à cet objet. Elle répertorie le nombre de {{Value|Points}}, {{Value|Edges}} et {{Value|Faces}} du maillage.

-    **Placement|Placement**: la position de l\'objet dans la [vue 3D](3D_view/fr.md). Le placement est défini par un `Base` point (vecteur) et un `Rotation` (axe et angle). Voir [Placement](Placement/fr.md).

    -   
        **Angle**
        
        : l\'angle de rotation autour de {{PropertyData/fr|Axis}}. Par défaut, {{value|0°}} (zéro degré).

    -   
        **Axis**
        
        : le vecteur unitaire qui définit l\'axe de rotation du placement. Chaque composant est une valeur à virgule flottante entre {{value|0}} et {{value|1}}. Si une valeur est supérieure à {{value|1}}, le vecteur est normalisé de sorte que la norme du vecteur soit {{value|1}}. Par défaut, il s\'agit de l\'axe Z positif, {{value|(0, 0, 1)}}.

    -   
        **Position**
        
        : un vecteur avec les coordonnées 3D du point de base. Par défaut, il s\'agit de l\'origine {{value|(0, 0, 0)}}.

-    **Label|String**: le nom modifiable par l\'utilisateur de cet objet, c\'est une chaîne UTF8 arbitraire.

-    **Label2|String|Hidden**: une description plus longue, modifiable par l\'utilisateur, de cet objet. Il s\'agit d\'une chaîne UTF8 arbitraire qui peut inclure des nouvelles lignes. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: une liste d\'expressions. Par défaut, elle est vide {{value|[]}}.

-    **Visibility|Bool|Hidden**: affichage ou non de l\'objet.



### Vue


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: une classe personnalisée de [viewprovider](Viewprovider/fr.md) associée à cet objet. Ceci n\'existe que pour la version en [Python](Python/fr.md). Voir [Script](#Script.md).


{{TitleProperty|Display Options}}

-    **Bounding Box|Bool**: si la valeur est `True`, l\'objet affichera la boîte englobante dans la [vue 3D](3D_view/fr.md).

-    **Display Mode|Enumeration**: {{value|Shaded}} (pas d\'arêtes), {{value|Wireframe}} (pas de faces), {{value|Flat Lines}} (affichage classique), {{value|Points}} (uniquement les sommets).

-    **Show In Tree|Bool**: si la valeur est `True`, l\'objet apparaît dans la [Tree view](Tree_view.md). Sinon, il est défini comme invisible.

-    **Visibility|Bool**: si elle est `True`, l\'objet apparaît dans la [vue 3D](3D_view/fr.md) ; sinon, il est invisible. Par défaut, cette propriété peut être activée ou désactivée en appuyant sur la barre **Espace**.


{{TitleProperty|Object Style}}

-    **Coloring|Bool|Hidden**: la valeur par défaut est `False`.

-    **Crease Angle|FloatConstraint**:

-    **Lighting|Enumeration**: {{value|Un côté}}. (par défaut), {{value|Two side}} ; l\'éclairage provient de deux côtés ou d\'un seul côté dans la [vue 3D](3D_view/fr.md).

-    **Line Color|Color**: un tuple de trois valeurs RVB à virgule flottante complètement noir.

-    **Line Transparency|Percent**: un nombre entier de {{value|0}} à {{value|100}} (un pourcentage) qui détermine le niveau de transparence des bords dans la [vue 3D](3D_view/fr.md). Une valeur de {{value|100}} indique des bords complètement invisibles ; les bords sont invisibles mais peuvent toujours être sélectionnés tant que **Selectable** est `True`.

-    **Line Width|FloatConstraint**: un flottant qui détermine la largeur en pixels des bords dans la [vue 3D](3D_view/fr.md). La valeur par défaut est {{value|1.0}}.

-    **Open Edges|Bool**: la valeur par défaut est `False`.

-    **Point Size|FloatConstraint**: similaire à **Line Width**, définit la taille des sommets.

-    **Shape Color|Color**: similaire à gris clair.

-    **Shape Material|Material|Hidden**: un [App Material](App_Material/fr.md) associé à cet objet. Par défaut, il est vide.

-    **Transparency|Percent**: un nombre entier compris entre {{value|0}} et {{value|100}} (un pourcentage) qui détermine le niveau de transparence des faces dans la [vue 3D](3D_view/fr.md). Une valeur de {{value|100}} indique des faces complètement invisibles ; les faces sont invisibles mais peuvent toujours être sélectionnées tant que **Selectable** est `True`.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (par défaut), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selectable|Bool**: si elle vaut `True`, l\'objet peut être sélectionné avec le pointeur dans la [vue 3D](3D_view/fr.md). Sinon, l\'objet ne peut pas être sélectionné tant que cette option n\'est pas définie sur `True`.

-    **Selection Style|Enumeration**: {{value|Shape}} (par défaut), {{value|BoundBox}}. Si l\'option est {{value|Shape}}, la forme entière (sommets, arêtes et faces) sera mise en évidence dans la [vue 3D](3D_view/fr.md) ; si elle est {{value|BoundBox}}, seule la boîte de délimitation sera mise en évidence.



## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](Scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au document.

Un Mesh Feature est créée avec la méthode `addObject()` du document.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::Feature", "Name")
obj.Label = "Custom label"
```

Pour la sous-classification de [Python](Python/fr.md), vous devez créer l\'objet `Mesh::FeaturePython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::FeaturePython", "Name")
obj.Label = "Custom label"
```



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Mesh](Mesh_Workbench.md) > Mesh Feature/fr
