# Mesh Feature/fr
## Introduction


{{TOCright}}

Un objet <img alt="" src=images/Mesh_Tree.svg  style="width:32px;"> _ qui lui est associé et qui peut être affiché dans la [vue 3D](3D_view/fr.md).

Une fonction de maillage (Mesh Feature) est conceptuellement similaire à une [Part Feature](Part_Feature/fr.md). Le premier est l\'objet de base pour les éléments avec des informations de \"maillage\", tandis que le second est l\'objet de base pour les éléments avec des informations de \"forme géométrique\".

Notez que l\'**<img src="images/Workbench_FEM.svg" width=16px> [atelier FEM](FEM_Workbench/fr.md)** utilise également des maillages, mais dans ce cas, il utilise un objet différent, appelé [FEM FemMeshObject](FEM_Mesh/fr.md) (classe `Fem::FemMeshObject`). Cet objet n\'est pas dérivé de la fonction de maillage, il a donc des propriétés différentes.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux du programme. La classe `Mesh::Feature* est à l'origine de la plupart des objets possédant un [maillage triangulaire](Mesh_MeshObject/fr.md). Ces objets sont créés à partir de l'[atelier Mesh](Mesh_Workbench/fr.md) ou en important des fichiers STL, OBJ et des formats de maillage similaires.`

## Utilisation

Presque tous les objets maillés créés par les commandes disponibles dans l\'interface graphique de l\'[atelier Mesh](Mesh_Workbench/fr.md) sont des [Mesh Features](Mesh_Feature/fr.md). Les objets maillés paramétriques créés par la commande [Mesh Solide régulier](Mesh_BuildRegularSolid/fr.md) sont les seules exceptions. Un [Mesh Feature](Mesh_Feature/fr.md) peut également être créé à partir de la [console Python](Python_console/fr.md) comme décrit dans la section [Script](Mesh_Feature/fr#Script.md).

L\'objet `Mesh::Feature` est défini dans l\'[atelier Mesh](Mesh_Workbench/fr.md) mais peut être utilisé comme classe de base pour les [objets scriptés](Scripted_objects/fr.md) dans tous les [ateliers](Workbenches/fr.md) générant des formes géométriques 2D et 3D.

Un `Mesh::Feature` a des propriétés simples comme un [placement](Placement/fr.md) et des propriétés visuelles pour définir l\'apparence de ses arêtes et faces.

## Propriétés

_ (classe `App::GeoFeature`), de ce fait partage toutes les propriétés de cette dernière.

Outre les propriétés décrites dans [App GeoFeature](App_GeoFeature/fr.md), Mesh Feature possède la propriété {{PropertyData/fr|Mesh}} qui contrôle le type de géométrie affiché dans la [vue 3D](3D_view/fr.md). Elle stocke [Mesh MeshObject](Mesh_MeshObject/fr.md) de cet objet. Il s\'agit de la géométrie affichée dans la [Vue 3D](3D_view/fr.md).

Les autres propriétés de cet objet sont celles liées à l\'apparence de son [Mesh MeshObject](Mesh_MeshObject/fr.md), y compris {{PropertyView/fr|Crease Angle}}, {{PropertyView/fr|Lighting}}, {{PropertyView/fr|Line Color}}, {{PropertyView/fr|Line Transparency}}, {{PropertyView/fr|Line Width}}, {{PropertyView/fr|Open Edges}}, {{PropertyView/fr|Point Size}} ainsi que la propriété masquée {{PropertyView/fr|Coloring}}.

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets crées par script peuvent avoir.

Ce sont les propriétés disponibles dans l\'[éditeur de propriétés](Property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Show all** dans le menu contextuel de l\'[éditeur de propriétés](Property_editor/fr.md).

### Données


{{TitleProperty|Base}}

-    {{PropertyData/fr|Mesh|MeshKernel}}: une classe [Mesh MeshObject](Mesh_MeshObject/fr.md) associée à cet objet. Elle répertorie le nombre de {{Value|Points}}, {{Value|Edges}} et {{Value|Faces}} du maillage.

-    {{PropertyData/fr|Placement|Placement}}: la position de l\'objet dans la [vue 3D](3D_view/fr.md). Le placement est défini par un `Base` point (vecteur) et un `Rotation` (axe et angle). Voir [Placement](Placement/fr.md).

    -   
        {{PropertyData/fr|Angle}}
        
        : l\'angle de rotation autour de {{PropertyData/fr|Axis}}. Par défaut, {{value|0°}} (zéro degré).

    -   
        {{PropertyData/fr|Axis}}
        
        : le vecteur unitaire qui définit l\'axe de rotation du placement. Chaque composant est une valeur à virgule flottante entre {{value|0}} et {{value|1}}. Si une valeur est supérieure à {{value|1}}, le vecteur est normalisé de sorte que la norme du vecteur soit {{value|1}}. Par défaut, il s\'agit de l\'axe Z positif, {{value|(0, 0, 1)}}.

    -   
        {{PropertyData/fr|Position}}
        
        : un vecteur avec les coordonnées 3D du point de base. Par défaut, il s\'agit de l\'origine {{value|(0, 0, 0)}}.

-    {{PropertyData/fr|Label|String}}: le nom modifiable par l\'utilisateur de cet objet, c\'est une chaîne UTF8 arbitraire.

##### Propriétés cachées de Données 


{{TitleProperty|Base}}

-    {{PropertyData/fr|Expression Engine|ExpressionEngine}}: une liste d\'expressions. Par défaut, vide {{value|[]}}.

-    {{PropertyData/fr|Label2|String}}: description plus longue et modifiable par l\'utilisateur de cet objet, il s\'agit d\'une chaîne UTF8 arbitraire. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    {{PropertyData/fr|Proxy|PythonObject}}: une classe personnalisée associée à cet objet. Cela n\'existe que pour la version [Python](Python/fr.md). Voir [Script](Mesh_Feature/fr#Script.md).

-    {{PropertyData/fr|Visibility|Bool}}: affiche ou non l\'objet.

### Vue

La plupart des objets dans FreeCAD ont ce qu\'on appelle un \"fournisseur de vues\", c\'est-à-dire une classe qui définit l\'apparence visuelle de l\'objet dans la [vue 3D](3D_view/fr.md) et dans la [vue en arborescence](Tree_view/fr.md). Le fournisseur de vue par défaut des objets Mesh Feature définit les propriétés suivantes. Les objets scriptés dérivés de Mesh Feature auront également accès à ces propriétés.


{{TitleProperty|Base}}

-    {{PropertyView/fr|Bounding Box|Bool}}: s\'il est `True`, l\'objet affichera le cadre de délimitation dans la [vue 3D](3D_view/fr.md).

-    {{PropertyView/fr|Crease Angle|FloatConstraint}}:

-    {{PropertyView/fr|Display Mode|Enumeration}}: {{value|Shaded}} (sans arêtes), {{value|Wireframe}} (sans faces), {{value|Flat Lines}} (visualisation régulière), {{value|Points}} (uniquement les sommets).

-    {{PropertyView/fr|Lighting|Enumeration}}: {{value|One side}} (par défaut), {{value|Two side}}. L\'éclairage provient de deux côtés ou d\'un côté dans la [vue 3D](3D_view/fr.md).

-    {{PropertyView/fr|Line Color|Color}}: un tuple de trois valeurs RVB à virgule flottante complètement noir.

-    {{PropertyView/fr|Line Transparency|Percent}}: un entier de {{value|0}} à {{value|100}} (un pourcentage) qui détermine le niveau de transparence des arêtes dans la [Vue 3D](3D_view/fr.md). Une valeur de {{value|100}} indique des arêtes complètement invisibles; les bords sont invisibles mais ils peuvent toujours être choisis tant que {{PropertyView/fr|Selectable}} est `True`.

-    {{PropertyView/fr|Line Width|FloatConstraint}}: valeur en flottant qui détermine la largeur en pixels des bords dans la [vue 3D](3D_view/fr.md). La valeur par défaut est {{value|1.0}}.

-    {{PropertyView/fr|On Top When Selected|Enumeration}}: {{value|Disabled}} (par défaut), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    {{PropertyView/fr|Open Edges|Bool}}: la valeur par défaut est `False`.

-    {{PropertyView/fr|Point Size|FloatConstraint}}: similaire à {{PropertyView/fr|Line Width}}, définit la taille des sommets.

-    {{PropertyView/fr|Selectable|Bool}}: s\'il est `True`, l\'objet peut être sélectionné avec le pointeur dans la [vue 3D](3D_view/fr.md). Sinon, l\'objet ne peut pas être sélectionné tant que cette option n\'est pas définie sur `True`.

-    {{PropertyView/fr|Selection Style|Enumeration}}: {{value|Shape}} (par défaut), {{value|BoundBox}}. Si l\'option est {{value|Shape}}, la forme entière (sommets, arêtes et faces) sera mise en évidence dans [vue 3D](3D_view/fr.md); s\'il s\'agit de {{value|BoundBox}}, seul le cadre englobant sera mis en surbrillance.

-    {{PropertyView/fr|Shape Color|Color}}: similaire à gris clair.

-    {{PropertyView/fr|Show In Tree|Bool}}: s\'il vaut `True`, l\'objet apparaît dans la [vue en arborescence](tree_view/fr.md). Sinon, il est défini comme invisible.

-    {{PropertyView/fr|Transparency|Percent}}: un entier de {{value|0}} à {{value|100}} (un pourcentage) qui détermine le niveau de transparence des faces dans la [3D vue](3D_view/fr.md). Une valeur de {{value|100}} indique des faces complètement invisibles; les faces sont invisibles mais elles peuvent toujours être sélectionnées tant que {{PropertyView/fr|Selectable}} est `True`.

-    {{PropertyView/fr|Visibility|Bool}}: s\'il est `True`, l\'objet apparaît dans la [vue 3D](3D_view/fr.md); sinon, il est invisible. Par défaut, cette propriété peut être activée et désactivée en appuyant sur la barre **Espace** du clavier.

##### Propriétés cachées de Données 


{{TitleProperty|Base}}

-    {{PropertyView/fr|Coloration|Bool}}: par défaut `False`.

-    {{PropertyView/fr|Proxy|PythonObject}}: une classe de fournisseur de vue personnalisée associée à cet objet. N\'existe que pour la version [Python](Python/fr.md). Voir [Script](Mesh_Feature/fr#Script.md).

-    {{PropertyView/fr|Shape Material|Material}}: un [App Material](App_Material/fr.md) associé à cet objet. Par defaut, vide.

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](Scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au programme.

Un Mesh Feature est créée avec la méthode `addObject()` du document. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::Feature", "Name")
obj.Label = "Custom label"
```

Ce `Mesh::Feature` de base n\'a pas d\'objet Proxy, il ne peut donc pas être entièrement utilisé pour la sous-classification.

Par conséquent, pour la sous-classe [Python](Python/fr.md), vous devez créer l\'objet `Mesh::FeaturePython`. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::FeaturePython", "Name")
obj.Label = "Custom label"
```


{{Mesh Tools navi

}} {{Document objects navi}} 

_

---
[documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Mesh](Mesh_Workbench.md) > Mesh Feature/fr
