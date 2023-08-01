# Part Feature/fr
## Introduction

<img alt="" src=images/Part_3D_object.svg  style="width:32px;">

Un objet [Part Feature](Part_Feature/fr.md), ou formellement un `Part::Feature`, est une [forme topologique](Part_TopoShape/fr.md) qui peut être affiché dans la [Vue 3D](3D_view/fr.md).

Part Feature est la classe parente de la plupart des objets 2D (Draft, Sketcher) et 3D (Part, PartDesign), à l\'exception des maillages, qui sont normalement basés sur [Mesh Feature](Mesh_Feature/fr.md) ou [FEM FemMeshObject](FEM_Mesh/fr.md) pour les objets FEM.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux dans Freecad*

## Utilisation

[Part Feature](Part_Feature/fr.md) est un objet interne. Par conséquent, il ne peut pas être créé à partir de l\'interface graphique, uniquement à partir de la [Console Python](Python_console/fr.md), comme décrit dans la section [Script](#Script.md).

L\'objet `Part::Feature` est défini dans l\'[atelier Part](Part_Workbench/fr.md) mais peut être utilisé comme classe de base pour les [objets scriptés](Scripted_objects/fr.md) dans tous les [ateliers](Workbenches/fr.md) générant des formes géométriques 2D et 3D. En fait, tous les objets produits dans l\'[atelier Part](Part_Workbench/fr.md) sont des instances d\'un `Part::Feature`.


`Part::Feature`

est également la classe parente de [PartDesign Corps](PartDesign_Body/fr.md), de [PartDesign Features](PartDesign_Feature/fr.md) et de [Part Part2DObject](Part_Part2DObject/fr.md), qui est spécialisée pour les formes 2D (planes).

Des ateliers peuvent ajouter plus de propriétés à cet élément de base pour produire un objet au comportement complexe.

## Propriétés

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets scriptés peuvent avoir.

[Part Feature](Part_Feature/fr.md) (classe `Part::Feature`) est dérivée de [App GeoFeature](App_GeoFeature/fr.md) (classe `App::GeoFeature`) et hérite de toutes ses propriétés. Elle possède également plusieurs propriétés supplémentaires. Notamment une propriété **Shape**, qui stocke la [Part TopoShape](Part_TopoShape/fr.md) de l\'objet. Il s\'agit de la géométrie qui est affichée dans la [vue 3D](3D_view/fr.md). Les autres propriétés de cet objet sont celles liées à l\'apparence de sa [TopoShape](Part_TopoShape/fr.md).

Ce sont les propriétés disponibles dans l\'[éditeur de propriétés](Property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Show all** dans le menu contextuel de l\'[éditeur de propriétés](Property_editor/fr.md).

### Données


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: une classe personnalisée associée à cet objet. Ceci n\'existe que pour la version en [Python](Python/fr.md). Voir [Script](#Script.md).

-    **Shape|PartShape|Hidden**: une classe [Part TopoShape](Part_TopoShape/fr.md) associée à cet objet.

-    **Placement|Placement**: la position de l\'objet dans la [vue 3D](3D_view/fr.md). Le placement est défini par un point `Base` (vecteur), et `Rotation` (axe et angle). Voir [Placement](Placement/fr.md).

    -   
        **Angle**
        
        : l\'angle de rotation autour de **Axis**. Par défaut, il est {{value|0°}}. (zéro degré).

    -   
        **Axis**
        
        : le vecteur unitaire qui définit l\'axe de rotation du placement. Chaque composante est une valeur à virgule flottante comprise entre {{value|0}} et {{value|1}}. Si une valeur est supérieure à {{value|1}}, le vecteur est normalisé de manière à ce que sa magnitude soit {{value|1}}. Par défaut, il s\'agit de l\'axe Z positif, {{value|(0, 0, 1)}}.

    -   
        **Position**
        
        : un vecteur contenant les coordonnées 3D du point de base. Par défaut, il s\'agit de l\'origine {{value|(0, 0, 0)}}.

-    **Label|String**: le nom modifiable par l\'utilisateur de cet objet, il s\'agit d\'une chaîne UTF8 arbitraire.

-    **Label2|String|Hidden**: une description plus longue, modifiable par l\'utilisateur, de cet objet. Il s\'agit d\'une chaîne UTF8 arbitraire qui peut inclure des nouvelles lignes. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: une liste d\'expressions. Par défaut, elle est vide {{value|[]}}.

-    **Visibility|Bool|Hidden**: affichage ou non de l\'objet.

### Vue

La plupart des objets dans FreeCAD ont ce qu\'on appelle un \"[viewprovider](viewprovider/fr.md)\", c\'est-à-dire une classe qui définit l\'apparence visuelle de l\'objet dans la [vue 3D](3D_view/fr.md) et dans la [vue en arborescence](Tree_view/fr.md). Le viewprovider par défaut des objets Part Feature définit les propriétés suivantes. Les objets scriptés dérivés de Part Feature auront également accès à ces propriétés.


{{TitleProperty|Base}}

-    {{PropertyView/fr|Proxy|PythonObject|hidden}}: une classe [viewprovider](Viewprovider/fr.md) personnalisée associée à cet objet. Cela n\'existe que pour la version [Python](Python/fr.md). Voir [Script](#Script.md).


{{TitleProperty|Options d'affichage}}

-    **Bounding Box|Bool**: si `True`, l\'objet affichera le cadre de délimitation dans la [Vue 3D](3D_view/fr.md).

-    **Display Mode|Enumeration**: {{value|Flat Lines}} (visualisation régulière), {{value|Shaded}} (pas d\'arêtes), {{value|Wireframe}} (pas de faces), {{value|Points}} (uniquement les sommets).

-    **Show In Tree|Bool**: la valeur par défaut est `True`, auquel cas l\'objet apparaîtra dans la [Vue en arborescence](Tree_view/fr.md) sinon, l\'objet sera masqué dans l\'arborescence. Une fois qu\'un objet de l\'arborescence est invisible, vous pouvez le revoir en ouvrant le menu contextuel sur le nom du document (clic droit) et en sélectionnant {{CheckBox|TRUE|Show hidden items}}. Ensuite, l\'élément masqué peut être choisi et **Show In Tree** peut être rétabli à `True`.

-    **Visibility|Bool**: si `True`, l\'objet apparaît dans la [Vue 3D](3D_view/fr.md) sinon, il est invisible. Par défaut, cette propriété peut être activée et désactivée en appuyant sur la barre **Espace**.


{{TitleProperty|Style de l'objet}}

-    **Angular Deflection|Angle**: il accompagne **Déviation**. C\'est un autre moyen de spécifier la précision avec laquelle générer le maillage pour le rendu à l\'écran ou lors de l\'exportation. La valeur par défaut est {{value|28.5 degrees}} ou {{value|0.5 radians}}. Il s\'agit de la valeur maximale, plus la valeur est petite, plus l\'apparence sera lisse dans la [vue 3D](3D_view/fr.md) et plus le maillage exporté sera fin.

-    **Deviation|FloatConstraint**: il accompagne **Déviation angulaire**. C\'est un autre moyen de spécifier la précision avec laquelle générer le maillage pour le rendu à l\'écran ou lors de l\'exportation. La valeur par défaut est {{value|0.5%}}. Il s\'agit de la valeur maximale, plus la valeur est petite, plus l\'apparence sera lisse dans la [vue 3D](3D_view/fr.md) et plus le maillage exporté sera fin.

-    **Diffuse Color|ColorList|hidden**: c\'est une liste de tuples RVB définissant les couleurs, similaire à **Shape Color**. La valeur par défaut est la liste {{value|[(0.8, 0.8, 0.8)]}}.

-    **Draw Style|Enumeration**: {{value|Solid}} (default), {{value|Dashed}}, {{value|Dotted}}, {{value|Dashdot}} ; définit le style des bords dans la [vue 3D](3D_view/fr.md).

-    **Lighting|Enumeration**: {{value|Two side}} (par défaut), {{value|One side}} ; l\'éclairage provient de deux côtés ou d\'un seul côté dans la [vue 3D](3D_view/fr.md).

-    **Line Color|Color**: un tuple de trois valeurs RVB à virgule flottante  presque noir .

-    **Line Color Array|ColorList|hidden**: il s\'agit d\'une liste de tuples RVB définissant les couleurs, similaire à **Line Color**. Par défaut, il s\'agit d\'une liste de {{value|[(0.09, 0.09, 0.09)]}}.

-    **Line Material|Material|hidden**: un [App Material](App_Material/fr.md) associé aux bords de cet objet. Par défaut, il est vide.

-    **Line Width|FloatConstraint**: un flottant qui détermine la largeur en pixels des bords dans la [vue 3D](3D_view/fr.md). La valeur par défaut est {{value|2.0}}.

-    {{PropertyView/fr|Point Color|Color}}: similair à **Line Color**, définit la couleur des sommets.

-    {{PropertyView/fr|Point Color Array|ColorList|hidden}}: c\'est une liste de tuples RVB définissant les couleurs, similaire à {{PropertyView/fr|Point Color}}. la valeur par défaut est la liste {{value|[(0.09, 0.09, 0.09)]}}.

-    {{PropertyView/fr|Point Material|Material|hidden}}: un [App Material](App_Material/fr.md) associé aux arêtes de cet objet. Par defaut c\'est vide.

-    {{PropertyView/fr|Point Size|FloatConstraint}}: similaire à **Line Width**, définit la taille des sommets.

-    **Shape Color|Color**: similaire à gris clair .

-    **Shape Material|Material|hidden**: un [App Material](App_Material/fr.md) associé aux arêtes de cet objet. Par defaut c\'est vide.

-    **Transparency|Percent**: un entier de {{value|0}} à {{value|100}} (un pourcentage) qui détermine le niveau de transparence des faces dans la [Vue 3D](3D_view/fr.md). Une valeur de {{value|100}} indique des faces complètement invisibles; les visages sont invisibles, mais ils peuvent toujours être sélectionnés tant que **Selectable** est `True`.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: contrôle la manière dont la sélection s\'effectue dans la [Vue 3D](3D_view/fr.md), si l\'objet a une [Shape](Part_TopoShape/fr.md) et s\'il y a beaucoup d\'objets partiellement couverts par d\'autres. La valeur par défaut est {{value|Disabled}}, ce qui signifie qu\'aucune mise en évidence spéciale ne se produira; {{value|Enabled}} signifie que l\'objet apparaîtra au-dessus de tout autre objet lorsqu\'il est sélectionné; {{value|Object}} signifie que l\'objet n\'apparaîtra en haut que si l\'objet entier est sélectionné dans la [Vue en arborescence](Tree_view/fr.md); {{value|Element}} signifie que l\'objet n\'apparaîtra en haut que si un sous-élément (sommet, arête, face) est sélectionné dans la [Vue 3D](3D_view/fr.md).

-    **Selectable|Bool**: s\'il est `True`, l\'objet peut être sélectionné avec le pointeur dans la [Vue 3D](3D_view/fr.md). Sinon, l\'objet ne peut pas être sélectionné tant que cette option n\'est pas définie sur `True`.

-    **Selection Style|Enumeration**: il contrôle la façon dont l\'objet est mis en évidence. Si c\'est {{value|Shape}}, la forme entière (sommets, arêtes et faces) sera mise en surbrillance dans la [Vue 3D](3D_view/fr.md); s\'il s\'agit de {{value|BoundBox}}, un cadre de délimitation apparaîtra autour de l\'objet et sera mis en surbrillance.

### Déflexion angulaire et déviation 

<img alt="" src=images/View_property_Deviation.svg  style="width:500px;"> 
*Déflexion angulaire et paramètres de déviation ; d < déflexion linéaire, α < déflexion angulaire.*

L\'écart est une valeur en pourcentage qui est liée aux dimensions en millimètres de la boîte englobante de l\'objet. L\'écart en millimètres peut être calculé comme suit:


```python
deviation_in_mm = (w + h + d)/3 * deviation/100
```

où {{value|w}}, {{value|h}}, {{value|d}} sont les dimensions de la boîte englobante.

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](Scripted_objects/fr.md).

Une entité de pièce, Part Feature, est créée avec la méthode `addObject()` du document.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Feature", "Name")
obj.Label = "Custom label"
```

Pour la sous-classification de [Python](Python/fr.md), vous devez créer l\'objet `Part::FeaturePython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::FeaturePython", "Name")
obj.Label = "Custom label"
```

### Name (Nom) 

Voir aussi : [Object name](Object_name/fr.md) pour plus d\'informations sur les propriétés de `Name`.

La méthode `addObject` possède deux arguments de base de type chaîne.

-   Le premier argument indique le type d\'objet, dans ce cas, `"Part::FeaturePython"`.
-   Le deuxième argument est une chaîne qui définit l\'attribut `Name`. S\'il n\'est pas fourni, il utilise par défaut le même nom que la classe, c\'est-à-dire `"Part__FeaturePython"`. `Name` ne peut contenir que des caractères alphanumériques simples et le trait de soulignement, `[_0-9a-zA-Z]`. Si d\'autres symboles sont donnés, ils seront convertis en traits de soulignement; par exemple, `"A+B:C*"` est converti en `"A_B_C_"`.

### Label (Etiquette) 

Si vous le souhaitez, l\'attribut `Label` peut être remplacé par un texte plus significatif.

-    `Label`peut accepter n\'importe quelle chaîne UTF8, y compris les accents et les espaces. Puisque la [Vue en arborescence](Tree_view/fr.md) affiche `Label`, il est recommandé de changer `Label` en une chaîne plus descriptive.

-   Par défaut, `Label` est unique, tout comme `Name`. Ce comportement peut être modifié dans [Réglage des préférences](Preferences_Editor/fr.md), **Édition → Préférences → Général → Document → Autoriser la duplication des étiquettes dans un document**. Cela signifie qu\'en général, `Label` peut être répété dans le même document. Lors du test d\'un élément spécifique, l\'utilisateur doit s\'appuyer sur `Name` plutôt que sur `Label`.


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Feature/fr
