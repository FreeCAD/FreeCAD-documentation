# Part Feature/fr
## Introduction


{{TOCright}}

<img alt="" src=images/Part_3D_object.svg  style="width:32px;">

Un objet [Part Feature](Part_Feature/fr.md), ou formellement un `Part::Feature`, est un élément simple associé à une [forme topologique](Part_TopoShape/fr.md) qui peut être affiché dans la [Vue 3D](3D_view/fr.md).

Part Feature est la classe parente de la plupart des objets 2D (Draft, Sketcher) et 3D (Part, PartDesign), à l\'exception des maillages, qui sont normalement basés sur [Mesh Feature](Mesh_Feature/fr.md) ou [FEM FemMeshObject](FEM_Mesh/fr.md) pour les objets FEM.

Chaque objet créé avec l\'[Atelier Part](Part_Workbench/fr.md) est essentiellement un [Part Feature](Part_Feature/fr.md).

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Schéma simplifié des relations entre les objets principaux dans le programme. La classe `Part::Feature* est l’origine de la plupart des objets 2D (Draft, Sketcher) et 3D (Part, PartDesign) qui ont des [Part formes topologiques](Part_TopoShape/fr.md).`

## Utilisation

La [Part Feature](Part_Feature/fr.md) est un objet interne. Par conséquent, il ne peut pas être créé à partir de l\'interface graphique, uniquement à partir de la [Console Python](Python_console/fr.md), comme décrit dans la section [Scrip](Part_Feature#Script.md). section.

L\'objet `Part::Feature` est défini dans [Part Workbench](Part_Workbench/fr.md), mais peut être utilisé comme classe de base pour [objets scripté](scripted_objects/fr.md) dans tous les [ateliers](Workbenches/fr.md) générant des formes géométriques 2D et 3D. En fait, tous les objets produits dans [Atelier Part](Part_Workbench/fr.md) sont des instances d\'un `Part::Feature`. Les objets solides importés à partir de fichiers STEP ou BREP seront importés à l\'aide de [Atelier Part](Part_Workbench/fr.md). Ils seront donc également importés en tant qu\'éléments `Part::Feature` bien que sans historique paramétrique.


`Part::Feature`

est également la classe parente de [PartDesign Corps](PartDesign_Body/fr.md), de [PartDesign Features](PartDesign_Feature/fr.md) et de [Part Part2DObject](Part_Part2DObject/fr.md), qui est spécialisée pour les formes 2D (planes).

Un objet `Part::Feature` possède de simples propriétés, telles qu\'un [emplacement](Placement/fr.md), et des couleurs permettant de définir l\'apparence de ses sommets, arêtes et faces. Les ateliers peuvent ajouter plus de propriétés à cet élément de base pour produire un objet avec un comportement complexe.

## Propriétés

[Part Feature](Part_Feature/fr.md) (`Part::Feature` class) est dérivé de la classe de base [App GeoFeature](App_GeoFeature/fr.md) (`App::GeoFeature` class) de ce fait partage toutes les propriétés de cette dernière.

Outre les propriétés décrites dans [App GeoFeature](App_GeoFeature/fr.md), Part Feature possède la propriété {{PropertyData/fr|Shape}} qui contrôle le type de géométrie affiché dans la [vue 3D](3D_view/fr.md). Elle stocke [Part TopoShape](Part_TopoShape/fr.md) de cet objet. Il s\'agit de la géométrie affichée dans la [Vue 3D](3D_view/fr.md).

Les autres propriétés de cet objet sont celles liées à l\'apparence de sa [TopoShape](Part_TopoShape/fr.md), incluant **Angular Deflection**, **Deviation**, **Draw Style**, **Lighting**, **Line Color**, **Line Width**, **Point Color**, **Point Size** ainsi que les propriétés cachées **Diffuse Color**, **Line Color Array**, **Line Material**, **Point Color Array** et **Point Material**.

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets scriptés peuvent avoir.

Ce sont les propriétés disponibles dans l\'[éditeur de propriétés](property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Show all** dans le menu contextuel de l\'[éditeur de propriétés](property_editor/fr.md).

### Données


{{TitleProperty|Base}}

-    {{PropertyData/fr|Placement|Placement}}: la position de l\'objet dans la [ Vue 3D](3D_view/fr.md). Le placement est défini par une `Base` un point (vecteur) et une `Rotation` (axe et angle). Voir [Placement](Placement/fr.md).

    -   
        {{PropertyData/fr|Angle}}
        
        : l\'angle de rotation autour des {{PropertyData/fr|Axis}}. Par défaut, il s\'agit de {{value|0°}} (zéro en degré).

    -   
        {{PropertyData/fr|Axis}}
        
        : vecteur unitaire qui définit l\'axe de rotation pour le placement. Chaque composant est une valeur à virgule flottante entre {{value|0}} et {{value|1}}. Si une valeur est supérieure à {{value|1}}, le vecteur est normalisé de sorte que la magnitude du vecteur est {{value|1}}. Par défaut, il s\'agit de l\'axe Z positif, {{value|(0, 0, 1)}}.

    -   
        {{PropertyData/fr|Position}}
        
        : un vecteur avec les coordonnées 3D du point de base. Par défaut, c\'est l\'origine {{value|(0, 0, 0)}}.

-    {{PropertyData/fr|Label|String}}: le nom modifiable par l\'utilisateur de cet objet. Il s\'agit d\'une chaîne UTF8 arbitraire.

##### Propriétés cachées de Données 

-    {{PropertyData/fr|Proxy|PythonObject|hidden}}: une classe personnalisée associée à cet objet. Cela n\'existe que pour la version [Python](Python/fr.md). Voir [Script](Part_Feature/fr#Script.md).

-    {{PropertyData/fr|Shape|PartShape|hidden}}: classe [Part TopoShape](Part_TopoShape/fr.md) associée à cet objet.

-    {{PropertyData/fr|Label2|String|hidden}}: description plus longue et modifiable par l\'utilisateur de cet objet, il s\'agit d\'une chaîne UTF8 arbitraire qui peut inclure des retours à la ligne. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    {{PropertyData/fr|Expression Engine|ExpressionEngine|hidden}}: une liste d\'expressions. Par défaut, elle est vide {{value|[]}}.

-    {{PropertyData/fr|Visibility|Bool|hidden}}: affiche ou non l\'objet.

### Vue

La plupart des objets dans FreeCAD ont ce qu\'on appelle un \"[viewprovider](viewprovider/fr.md)\", c\'est-à-dire une classe qui définit l\'apparence visuelle de l\'objet dans la [vue 3D](3D_view/fr.md) et dans la [vue en arborescence](Tree_view/fr.md). Le viewprovider par défaut des objets Part Feature définit les propriétés suivantes. Les objets scriptés dérivés de Part Feature auront également accès à ces propriétés.


{{TitleProperty|Base}}

-    {{PropertyView/fr|Proxy|PythonObject|hidden}}: une classe [viewprovider](viewprovider/fr.md) personnalisée associée à cet objet. Cela n\'existe que pour la version [Python](Python/fr.md). Voir [Script](Part_Feature/fr#Script.md).


{{TitleProperty|Options d'affichage}}

-    {{PropertyView/fr|Bounding Box|Bool}}: si `True`, l\'objet affichera le cadre de délimitation dans la [Vue 3D](3D_view/fr.md).

-    {{PropertyView/fr|Display Mode|Enumeration}}: {{value|Flat Lines}} (visualisation régulière), {{value|Shaded}} (pas d\'arêtes), {{value|Wireframe}} (pas de faces), {{value|Points}} (uniquement les sommets).

-    {{PropertyView/fr|Show In Tree|Bool}}: la valeur par défaut est `True`, auquel cas l\'objet apparaîtra dans la [Vue en arborescence](Tree_view/fr.md) sinon, l\'objet sera masqué dans l\'arborescence. Une fois qu\'un objet de l\'arborescence est invisible, vous pouvez le revoir en ouvrant le menu contextuel sur le nom du document (clic droit) et en sélectionnant {{CheckBox|TRUE|Show hidden items}}. Ensuite, l\'élément masqué peut être choisi et {{PropertyView/fr|Show In Tree}} peut être rétabli à `True`.

-    {{PropertyView/fr|Visibility|Bool}}: si `True`, l\'objet apparaît dans la [Vue 3D](3D_view/fr.md) sinon, il est invisible. Par défaut, cette propriété peut être activée et désactivée en appuyant sur la barre **Espace** du clavier.


{{TitleProperty|Style de l'objet}}

-    {{PropertyView/fr|Angular Deflection|Angle}}: il accompagne {{PropertyView/fr|Déviation}}. C\'est un autre moyen de spécifier la précision avec laquelle générer le maillage pour le rendu à l\'écran ou lors de l\'exportation. La valeur par défaut est {{value|28.5 degrees}} ou {{value|0.5 radians}}. Il s\'agit de la valeur maximale, plus la valeur est petite, plus l\'apparence sera lisse dans la [vue 3D](3D_view/fr.md) et plus le maillage exporté sera fin.

-    {{PropertyView/fr|Deviation|FloatConstraint}}: il accompagne {{PropertyView/fr|Déviation angulaire}}. C\'est un autre moyen de spécifier la précision avec laquelle générer le maillage pour le rendu à l\'écran ou lors de l\'exportation. La valeur par défaut est {{value|0.5%}}. Il s\'agit de la valeur maximale, plus la valeur est petite, plus l\'apparence sera lisse dans la [vue 3D](3D_view/fr.md) et plus le maillage exporté sera fin.

-    {{PropertyView/fr|Diffuse Color|ColorList|hidden}}: c\'est une liste de tuples RVB définissant les couleurs, similaire à {{PropertyView/fr|Shape Color}}. La valeur par défaut est la liste {{value|[(0.8, 0.8, 0.8)]}}.

L\'écart est une valeur en pourcentage qui est liée aux dimensions en millimètres de la boîte englobante de l\'objet. L\'écart en millimètres peut être calculé comme suit: 
```python
deviation_in_mm = (w + h + d)/3 * deviation/100
``` où {{value|w}}, {{value|h}}, {{value|d}} sont les dimensions de la boîte englobante.

-    {{PropertyView/fr|Draw Style|Enumeration}}: {{value|Solid}} (par défaut), {{value|Dashed}}, {{value|Dotted}}, {{value|Dashdot}}; définit le style des bords dans la [Vue 3D](3D_view/fr.md).

-    {{PropertyView/fr|Lighting|Enumeration}}: {{value|Two side}} (par défaut), {{value|One side}}; l\'éclairage provient de deux côtés ou d\'un côté dans la [Vue 3D](3D_view/fr.md).

-    {{PropertyView/fr|Line Color|Color}}: un tuple de trois valeurs RVB à virgule flottante  presque noir .

-    {{PropertyView/fr|Line Color Array|ColorList|hidden}}: c\'est une liste de tuples RVB définissant les couleurs, similaire à {{PropertyView/fr|Line Color}}. la valeur par défaut est la liste {{value|[(0.09, 0.09, 0.09)]}}.

-    {{PropertyView/fr|Line Material|Material|hidden}}: un [App Material](App_Material/fr.md) associé aux arêtes de cet objet. Par defaut c\'est vide.

-    {{PropertyView/fr|Line Width|FloatConstraint}}: valeur flottante qui détermine la largeur en pixels des bords dans la [Vue 3D](3D_view/fr.md). Par défaut {{value|2.0}}.

-    {{PropertyView/fr|Point Color|Color}}: similair à **Line Color**, définit la couleur des sommets.

-    {{PropertyView/fr|Point Color Array|ColorList|hidden}}: c\'est une liste de tuples RVB définissant les couleurs, similaire à {{PropertyView/fr|Point Color}}. la valeur par défaut est la liste {{value|[(0.09, 0.09, 0.09)]}}.

-    {{PropertyView/fr|Point Material|Material|hidden}}: un [App Material](App_Material/fr.md) associé aux arêtes de cet objet. Par defaut c\'est vide.

-    {{PropertyView/fr|Point Size|FloatConstraint}}: similaire à **Line Width**, définit la taille des sommets.

-    {{PropertyView/fr|Shape Color|Color}}: similaire à gris clair .

-    {{PropertyView/fr|Shape Material|Material|hidden}}: un [App Material](App_Material/fr.md) associé aux arêtes de cet objet. Par defaut c\'est vide.

-    {{PropertyView/fr|Transparency|Percent}}: un entier de {{value|0}} à {{value|100}} (un pourcentage) qui détermine le niveau de transparence des faces dans la [Vue 3D](3D_view/fr.md). Une valeur de {{value|100}} indique des faces complètement invisibles; les visages sont invisibles, mais ils peuvent toujours être sélectionnés tant que **Selectable** est `True`.


{{TitleProperty|Selection}}

-    {{PropertyView/fr|On Top When Selected|Enumeration}}: contrôle la manière dont la sélection s\'effectue dans la [Vue 3D](3D_view/fr.md), si l\'objet a une [Shape](Part_TopoShape/fr.md) et s\'il y a beaucoup d\'objets partiellement couverts par d\'autres. La valeur par défaut est {{value|Disabled}}, ce qui signifie qu\'aucune mise en évidence spéciale ne se produira; {{value|Enabled}} signifie que l\'objet apparaîtra au-dessus de tout autre objet lorsqu\'il est sélectionné; {{value|Object}} signifie que l\'objet n\'apparaîtra en haut que si l\'objet entier est sélectionné dans la [Vue en arborescence](Tree_view/fr.md); {{value|Element}} signifie que l\'objet n\'apparaîtra en haut que si un sous-élément (sommet, arête, face) est sélectionné dans la [Vue 3D](3D_view/fr.md).

-    {{PropertyView/fr|Selectable|Bool}}: s\'il est `True`, l\'objet peut être sélectionné avec le pointeur dans la [Vue 3D](3D_view/fr.md). Sinon, l\'objet ne peut pas être sélectionné tant que cette option n\'est pas définie sur `True`.

-    {{PropertyView/fr|Selection Style|Enumeration}}: il contrôle la façon dont l\'objet est mis en évidence. Si c\'est {{value|Shape}}, la forme entière (sommets, arêtes et faces) sera mise en surbrillance dans la [Vue 3D](3D_view/fr.md); s\'il s\'agit de {{value|BoundBox}}, un cadre de délimitation apparaîtra autour de l\'objet et sera mis en surbrillance.

### Valeur d\'écart 

<img alt="" src=images/View_property_Deviation.svg  style="width:500px;"> 
*Paramètres de déflexion de l'algorithme `BRepMesh_IncrementalMesh*; d < déviation linéaire, α < déviation angulaire.`

Consultez le fil du forum, [Déviation et déviation angulaire](https://forum.freecadweb.org/viewtopic.php?f=3&t=45512).

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

Ce `Part::Feature` de base n\'a pas d\'objet Proxy, il ne peut donc pas être entièrement utilisé pour la sous-classification.

Par conséquent, pour la sous-classe [Python](Python/fr.md), vous devez créer l\'objet `Part::FeaturePython`. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::FeaturePython", "Name")
obj.Label = "Custom label"
```

### Name (Nom) 


**Voir aussi: [Objet name](Object_name/fr.md), pour plus d'informations sur les propriétés du nom.**

La fonction `addObject` a deux arguments de chaîne de base.

-   Le premier argument indique le type d\'objet, dans ce cas, `"Part::FeaturePython"`.
-   Le deuxième argument est une chaîne qui définit l\'attribut `Name`. S\'il n\'est pas fourni, il utilise par défaut le même nom que la classe, c\'est-à-dire `"Part__FeaturePython"`. `Name` ne peut contenir que des caractères alphanumériques simples et le trait de soulignement, `[_0-9a-zA-Z]`. Si d\'autres symboles sont donnés, ils seront convertis en traits de soulignement; par exemple, `"A+B:C*"` est converti en `"A_B_C_"`.

### Label (Etiquette) 

Si vous le souhaitez, l\'attribut `Label` peut être remplacé par un texte plus significatif.

-    `Label`peut accepter n\'importe quelle chaîne UTF8, y compris les accents et les espaces. Puisque la [Vue en arborescence](Tree_view/fr.md) affiche le `Label`, il est recommandé de changer le `Label` en une chaîne plus descriptive.

-   Par défaut, `Label` est unique, tout comme `Name`. Ce comportement peut être modifié dans [Réglage des préférences](Preferences_Editor/fr.md), **Edition → Préférences → Général → Document → Autoriser la duplication des étiquettes dans un document**. Cela signifie qu\'en général, `Label` peut être répété dans le même document. Lors du test d\'un élément spécifique, l\'utilisateur doit s\'appuyer sur `Name` plutôt que sur `Label`.


 {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Feature/fr
