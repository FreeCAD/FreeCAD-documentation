# Property editor/fr
{{TOCright}}

## Description

L\'[éditeur de propriétés](Property_editor/fr.md) apparaît lorsque l\'onglet **Model** de la [vue combinée](combo_view/fr.md) est actif dans l\'[interface](interface/fr.md); il permet de gérer les propriétés exposées publiquement des objets du document.

Généralement, l\'éditeur de propriétés est conçu pour traiter un seul objet à la fois. Les valeurs affichées dans l\'éditeur de propriétés appartiennent à l\'objet sélectionné du document actif. Malgré cela, certaines propriétés, telles que les couleurs, peuvent être définies pour plusieurs objets sélectionnés. Si aucun élément n\'est sélectionné, l\'éditeur de propriétés sera vide.

Toutes les propriétés ne peuvent pas toujours être modifiées. en fonction du statut spécifique de la propriété, certains d\'entre eux seront invisibles (non répertoriés) ou en lecture seule (non modifiables). {{TOCright}}

![](images/FreeCAD_Property_editor_empty.png )



*Éditeur de propriétés vide, quand aucun objet n'est sélectionné.*

## Définition d\'une propriété 

Une propriété est une information comme un numéro ou une chaîne de texte qui est rattachée à un document Freecad ou à un objet dans le document.

Les [objets scriptés](scripted_objects/fr.md) personnalisés peuvent utiliser n\'importe quel type de propriété défini dans le système de base. Voir la liste complète dans [Propriétés](Property/fr.md).

Certains des types de propriétés les plus couramment utilisés sont : 
```python
App::PropertyBool
App::PropertyFloat
App::PropertyAngle
App::PropertyDistance
App::PropertyInteger
App::PropertyString
App::PropertyMatrix
App::PropertyVector
App::PropertyPlacement
```

Différents objets peuvent avoir différents types de propriétés. Cependant, de nombreux objets ont les mêmes types car ils sont dérivés de la même classe interne. Par exemple, la plupart des objets décrivant des formes géométriques (lignes, cercles, rectangles, corps solides, pièces importées, etc.) ont la propriété \"Placement\" qui définit leur position dans la [Vue 3D](3D_view/fr.md).

## Vue et Propriétés des données 

Il existe deux classes de propriétés d\'entités accessibles via des onglets dans l\'éditeur de propriétés :

-    **View**propriétés liées à l\'aspect \"visuel\" de l\'objet. Les propriétés **View** sont liées à l\'attribut **ViewProvider** (`ViewObject`) de l\'objet et ne sont accessibles que lorsque l\'interface graphique est chargée. Ils ne sont pas accessibles lorsque vous utilisez FreeCAD en mode console ou en tant que bibliothèque sans tête.

-    **Data**propriétés, liées aux paramètres \"physiques\" de l\'objet. Les propriétés **Data** définissent les caractéristiques essentielles de l\'objet. Elles existent à tout moment, même lorsque FreeCAD est utilisé en mode console ou en tant que bibliothèque. Cela signifie que si vous chargez un document en mode console, vous pouvez modifier le rayon d\'un cercle ou la longueur d\'une ligne, même si vous ne pouvez pas voir le résultat à l\'écran.

Pour cette raison, les propriétés **Data** sont considérées comme plus \"importantes\", car elles définissent réellement la géométrie d\'une forme. D\'autre part, les propriétés **View** sont moins importantes car elles affectent uniquement l\'apparence superficielle de la géométrie. Par exemple, un cercle de 10 mm de rayon est différent d\'un cercle de 5 mm de rayon ; la couleur des cercles (propriété View) n\'affecte pas leurs formes, mais le rayon (propriété Data). Dans de nombreux cas dans cette documentation, le mot \"Property\" désigne une \"propriété de données\" et non \"View property\".

### Propriétés de base 


**Voir aussi: [Objet name](Object_name/fr.md)**

L\'objet [scripté](scripted_objects/fr.md) le plus élémentaire n\'affiche aucune propriété **Data** dans l\'éditeur de propriétés, à l\'exception de son attribut `Label`. Le `Label` est une chaîne éditable par l\'utilisateur qui identifie l\'objet dans la [vue en arborescence](tree_view/fr.md). D\'autre part, le `Name` d\'un objet est un attribut interne qui est affecté à l\'objet au moment de sa création. cet attribut est en lecture seule, il ne peut donc pas être modifié et il n\'est pas non plus affiché dans l\'éditeur de propriétés.

Un objet paramétrique de base est créé comme suit


```python
obj = App.ActiveDocument.addObject("App::FeaturePython", "App__FeaturePython")
obj.Label = "Plain_object"
print(obj.Name)
print(obj.Label)
```

<img alt="" src=images/FreeCAD_Property_editor_View_basic.png  style="width:" height="264px;"> <img alt="" src=images/FreeCAD_Property_editor_Data_basic.png  style="width:" height="264px;">



*Onglets Vue et Données de l’éditeur de propriétés, pour une basique "App::FeaturePython" d'un objet scripté.*

La plupart des objets géométriques pouvant être créés et affichés dans la [Vue 3D](3D_view/fr.md) sont dérivés d\'un `Part::Feature`. Voir [Part Feature](Part_Feature/fr.md) pour les propriétés les plus élémentaires de ces objets.

Pour la géométrie 2D, la plupart des objets sont dérivés de [`Part::Part2DObject`](Part_Part2DObject/fr.md) (itself derived from [`Part::Feature`](Part_Feature/fr.md)) qui est la base du [Sketchers](Sketch/fr.md), et de [Draft éléments](Draft_Workbench/fr.md). Voir [Part Part2DObject](Part_Part2DObject/fr.md) pour les propriétés les plus élémentaires de ces objets.

## Actions


{{Version/fr|0.19}}

Un clic droit dans un espace vide de la vue ou avec une propriété sélectionnée ne montre qu\'une seule commande:

-    **Show all**: s\'il est actif, en plus des propriétés standard qui apparaissent déjà, il affiche toutes les propriétés masquées des données et de vues dans leurs onglets respectifs.

    -   Données: \"Proxy\", \"Label2\", \"Expression Engine\", and \"Visibility\".
    -   Voir: \"Proxy\".

Lorsque l\'option **Show all** est active et qu\'une propriété est sélectionnée, d\'autres actions sont disponibles avec un deuxième clic droit:

-    **Show all**: désactive la commande **Show all**, masquant ainsi les propriétés supplémentaires de données et d\'affichage.

-    **Add Property**: ajoute une propriété dynamique à l\'objet. cela fonctionne à la fois avec C++ defined objects, et Python [objets scriptés](scripted_objects/fr.md).

-    **Expression...**: appelle l\'éditeur de formule, qui permet d\'utiliser [expressions](Expressions/fr.md) dans la valeur de la propriété.

-    **Hidden**: si actif, définit la propriété comme masquée, ce qui signifie qu\'elle ne sera affichée dans l\'éditeur de propriétés que si **Show all** est actif.

-    **Output**: s\'il est actif, définit la propriété comme sortie.

-    **NoRecompute**: si actif, définit la propriété comme non recalculée lorsque le document est recalculé; Ceci est utile lorsqu\'une propriété ne doit pas être affectée par d\'autres mises à jour.

-    **ReadOnly**: si actif, définit la propriété en lecture seule. Elle ne sera plus modifiable dans l\'éditeur de propriétés jusqu\'à ce que ce paramètre soit désactivé. L\'entrée de menu **Expression...** n\'est plus disponible. **Remarque:** Il peut encore être possible de modifier la propriété via un dialogue qui met à jour la propriété.

-    **Transient**: si actif, définit la propriété sur transitoire. La valeur d\'une propriété transitoire n\'est pas enregistrée dans un fichier. Lors de l\'ouverture d\'un fichier, elle est instanciée avec sa valeur par défaut.

-    **Touched**: s\'il est actif, il est touché et prêt à être recalculé.

-    **EvalOnRestore**: s\'il est actif, il est évalué lors de la restauration du document.

## Exemple de propriétés d\'un objet PartDesign 

Dans cette section, nous montrons quelques propriétés communes qui sont visibles pour un [PartDesign Corps](PartDesign_Body/fr.md) et une [PartDesign Fonction](PartDesign_Feature/fr.md). Les propriétés spécifiques d\'un objet peuvent être trouvées dans la page de documentation spécifique de cet objet.

### Vue

La plupart de ces propriétés sont héritées de l\'objet de base [Part Feature](Part_Feature/fr.md).

<img alt="" src=images/FreeCAD_Property_editor_View.png  style="width:490px;"> {{TitleProperty|Base}}

-    {{PropertyView/fr|Angular Deflection}}: c\'est une autre façon de spécifier la finesse de génération du maillage pour le rendu à l\'écran ou lors de l\'exportation. La valeur par défaut est 28,5 degrés, soit 0,5 radians. Plus la valeur est petite, plus l\'apparence sera lisse dans la [Vue 3D](3D_view/fr.md), et plus le maillage sera exporté sera fin.

-    {{PropertyView/fr|Bounding Box}}: indique si une boîte montrant l\'étendue globale de l\'objet est affichée.

-    {{PropertyView/fr|Deviation}}: définit la précision de la représentation polygonale du modèle dans la [vue 3D](3D_view/fr.md) (pavage). Des valeurs plus faibles indiquent une meilleure qualité. La valeur est en pourcentage de la taille de l\'objet.

-    {{PropertyView/fr|Display Mode}}: mode d\'affichage de l\'ensemble du corps, {{Value|Flat lines}} (défaut), {{Value|Shaded}}, {{Value|Wireframe}}, {{Value|Points}}.

-    {{PropertyView/fr|Display Mode Body}}: mode d\'affichage du Tip du corps, {{Value|Through}} (default), {{Value|Tip}}.

-    {{PropertyView/fr|Draw Style}}: {{Value|Solid}}, {{Value|Dashed}}, {{Value|Dotted}}, {{Value|Dashdot}}; définit le style des bords dans la [vue 3D](3D_view.md).

-    {{PropertyView/fr|Lighting}}: {{Value|One side}}, {{Value|Two side}} (default).

-    {{PropertyView/fr|Line Color}}: la couleur RVB des bords, elle est par défaut {{value|(25, 25, 25)}}.

-    {{PropertyView/fr|Line Width}}: l\'épaisseur des bords, elle est par défaut {{value|2}} pixels.

-    {{PropertyView/fr|On Top When Selected}}: {{value|Disabled}}, {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    {{PropertyView/fr|Point Color}}: the RGB color of the vertices, it defaults to {{value|(25, 25, 25)}}.

-    {{PropertyView/fr|Point Size}}: la taille des sommets, il est par défaut {{value|2}} pixels.

-    {{PropertyView/fr|Selectable}}: si l\'objet est sélectionnable ou non.

-    {{PropertyView/fr|Selection Style}}: {{value|Shape}}, {{value|BoundBox}}.

-    {{PropertyView/fr|Shape Color}}: la couleur RVB de la forme, elle est par défaut {{value|(204, 204, 204)}}.

-    {{PropertyView/fr|Show In Tree}}: s\'il est réglé sur `True`, l\'objet apparaît dans l\'arborescence. Sinon, il est défini comme invisible.

-    {{PropertyView/fr|Transparency}}: le degré de transparence de {{value|0}} (défaut) à {{value|100}}.

-    {{PropertyView/fr|Visibility}}: si l\'objet est visible dans la [Vue 3D](3D_view/fr.md) ou non. Basculez avec la barre **Espace** du clavier.




### Données

Dans ce cas, nous observons les propriétés de la fonction [PartDesign Révolution](PartDesign_Revolution/fr.md).

<img alt="" src=images/FreeCAD_Property_editor_Data.png  style="width:490px;"> {{TitleProperty|Base}}

-    {{PropertyData/fr|Label}}: L\'étiquette est le nom donné à l\'objet (fonctionnalité) par l\'utilisateur. Ce nom peut être modifié à volonté.


{{TitleProperty|Part Design}}

-    {{PropertyData/fr|Refine}}: s\'il faut affiner la fusion effectuée avec d\'autres objets.


{{TitleProperty|Revolution}}

-    {{PropertyData/fr|Base}}: le point dans l\'espace qui spécifie le centre de la révolution. Il ne peut pas être modifié directement, uniquement lors de la modification de la fonction.

-    {{PropertyData/fr|Axis}}: l\'axe autour duquel la révolution sera effectuée. Il ne peut pas être modifié directement, uniquement lors de la modification de la fonction.

-    {{PropertyData/fr|Angle}}: l\'angle qui spécifie la proportion de rotation de l\'élément de base. Par défaut, c\'est {{value|360 deg}}, mais cela peut être n\'importe quelle fraction de cela.


{{TitleProperty|Sketch Based}}

-    {{PropertyData/fr|Midplane}}: si l\'objet de base est une [Esquisse](Sketch/fr.md), lorsque cette propriété est `True`, il effectuera la révolution avec l\'esquisse servant de plan de symétrie. Cela est visible si l\'{{PropertyData/fr|Angle}} est différent de {{value|360 deg}}.

-    {{PropertyData/fr|Reversed}}: Par défaut, mis à `True`. Permet d\'effectuer la révolution dans une direction ou l\'autre.




## Script


**See also:**

[FreeCAD Script de Base](FreeCAD_Scripting_Basics/fr.md).

Voir la page [objets scriptés ](scripted_objects/fr.md) pour obtenir des informations complètes sur l\'ajout de propriétés aux objets définis via un script [Python](Python/fr.md).

La plupart des propriétés visibles dans l\'éditeur de propriétés sont accessibles depuis la [console Python](Python_console/fr.md). Dans la plupart des cas, ces propriétés ne sont que des attributs de la classe qui définit l\'objet sélectionné. Par exemple, si l\'éditeur de propriétés affiche la propriété {{PropertyData/fr|Group}}, cela signifie que l\'objet a l\'attribut `Group`. 
```python
print(obj.Group)
```

Ces attributs (properties) sont ajoutés avec la méthode `addProperty` de l\'objet de base. Au minimum, il est nécessaire de spécifier le type de [propriété](property/fr.md) et son nom. 
```python
obj.addProperty("App::PropertyFloat", "Custom")
print(obj.Custom)
```

Les propriétés suivent la convention `CapitalCamelCase` ou `PascalCase`, ce qui signifie que chaque mot commence par une majuscule et qu\'il n\'y a pas de soulignement. Lorsque l\'éditeur de propriétés affiche ces noms, il laisse un espace entre chaque lettre majuscule, ce qui facilite la lecture.


```python
obj.addProperty("App::PropertyDistance", "CustomCamelProperty")
obj.CustomCamelProperty = 1000
print(obj.CustomCamelProperty)
```

![](images/FreeCAD_Property_editor_Custom.png ) 
*Éditeur de propriétés affichant les propriétés de données d'un [PartDesign Corps](PartDesign_Body/fr.md), avec deux propriétés supplémentaires, "Personnalisées" et "Propriété Camel personnalisée".*

De la même manière, les propriétés **View** sont ajoutées, non pas à l\'objet de base, mais à son `ViewObject`. Ensuite, il s\'ensuit que des propriétés comme {{PropertyView/fr|Angular Deflection}}, {{PropertyView/fr|Bounding Box}}, {{PropertyView/fr|Display Mode}}, {{PropertyView/fr|Display Mode Body}}, {{PropertyView/fr|Line Color}}, et d\'autres, peuvent être examinés et modifiés à partir de la [console Python](Python_console/fr.md).


```python
print(obj.ViewObject.AngularDeflection)
print(obj.ViewObject.BoundingBox)
print(obj.ViewObject.DisplayMode)
print(obj.ViewObject.DisplayModeBody)
print(obj.ViewObject.LineColor)
```

Toutes les propriétés publiques de l\'objet et de son provider de vues sont contenues dans l\'attribut `PropertiesList` correspondant. 
```python
print(obj.PropertiesList)
print(obj.ViewObject.PropertiesList)
```





{{Interface navi

}} {{Std Base navi}}

---
[documentation index](../README.md) > Property editor/fr
