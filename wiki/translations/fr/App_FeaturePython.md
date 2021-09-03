

## Introduction

Un objet <img alt="" src=images/Feature.svg  style="width:32px;"> [App FeaturePython](App_FeaturePython/fr.md), ou officiellement `App::FeaturePython`, est une simple instance de [App DocumentObject](App_DocumentObject/fr.md) dans [Python](Python/fr.md).

Il s\'agit d\'un objet simple qui, par défaut, n\'a pas beaucoup de propriétés, par exemple, pas de [Positionnement](Placement/fr.md) ni [forme topologique](Part_TopoShape/fr.md). Cet objet est destiné à un usage général, et en lui donnant des propriétés. Il peut être utilisé pour gérer différents types de données.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Diagramme simplifié des relations entre les objets centraux du programme. La classe `App::FeaturePython* est une implémentation simple de {{incode|App::DocumentObject` qui peut être utilisée à n'importe quelle fin, car elle n'a pas de [TopoShape](Part_TopoShape/fr.md) par défaut.}}

## Utilisation

[App FeaturePython](App_FeaturePython/fr.md) est un objet interne. Il ne peut donc pas être créé à partir de l\'interface graphique. Il est censé être sous-classé par des classes qui géreront différents types de données.

Voir [Script](App_FeaturePython/fr#Script.md) pour plus d\'informations.

## Propriétés

Une classe [App FeaturePython](App_FeaturePython/fr.md) (`App::FeaturePython` classe) est dérivée de la classe de base [App DocumentObject](App_DocumentObject/fr.md) (`App::DocumentObject` classe).Elle partage toutes les propriétés de cette dernière.

En plus des propriétés décrites dans [App DocumentObject](App_DocumentObject/fr.md), FeaturePython possède un fournisseur de vues de base, il apparaît donc dans la [vue arborescente](tree_view/fr.md).

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets scriptés peuvent avoir.

Ce sont les propriétés disponibles dans l\'[éditeur de propriétés](property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Show all** dans le menu contextuel de l\'[éditeur de propriétés](property_editor/fr.md).

### Données


{{TitleProperty|Base}}

-    {{PropertyData/fr|Proxy|PythonObject|Hidden}}: une classe personnalisée associée à cet objet.

-    {{PropertyData/fr|Label|String}}: le nom modifiable par l\'utilisateur de cet objet, c\'est une chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Label2|String|Hidden}}: une description plus longue et modifiable par l\'utilisateur de cet objet, c\'est une chaîne UTF8 arbitraire qui peut inclure des retours à la ligne. Par défaut, c\'est une chaîne vide {{value|""}}.

-    {{PropertyData/fr|Expression Engine|ExpressionEngine|Hidden}}: une liste d\'expressions. Par défaut vide {{value|[]}}.

-    {{PropertyData/fr|Visibility|Bool|Hidden}}: affiche ou non l\'objet.

### Vue

Ces propriétés correspondent aux propriétés basique de la base [viewprovider](viewprovider/fr.md), `Gui::ViewProviderDocumentObject`, qui est héritée par tous les viewprovider du logiciel.


{{TitleProperty|Base}}

-    {{PropertyView/fr|Proxy|PythonObject}}: une classe de fournisseur de vue personnalisée associée à cet objet. Cette propriété n\'existe que pour les classes capables d\'attribuer une classe personnalisée.


{{TitleProperty|Display Options}}

-    {{PropertyView/fr|Display Mode|Enumeration}}: il est vide par défaut.

-    {{PropertyView/fr|Show In Tree|Bool}}: la valeur par défaut est `True`, auquel cas l\'objet apparaîtra dans la [Vue en arborescence](Tree_view/fr.md) sinon l\'objet sera masqué dans l\'arborescence. Une fois qu\'un objet de l\'arborescence est invisible, vous pouvez le revoir en ouvrant le menu contextuel sur le nom du document (clic droit) et en sélectionnant {{CheckBox|TRUE|Show hidden items}}. Ensuite, l\'élément masqué peut être choisi et **Show In Tree** peut être rétabli à `True`.

-    {{PropertyView/fr|Visibility|Bool}}: par défaut `True`, dans ce cas l\'objet sera visible dans la [Vue 3D](3D_view/fr.md) s\'il a une [Shape](Part_TopoShape/fr.md) sinon il sera invisible. Par défaut, cette propriété peut être activée et désactivée en sélectionnant l\'objet et en appuyant sur la barre **Espace** du clavier.


{{TitleProperty|Selection}}

-    {{PropertyView/fr|On Top When Selected|Enumeration}}: il contrôle la manière dont la sélection s\'effectue dans la [Vue 3D](3D_view/fr.md) si l\'objet a une [Shapeet](Part_TopoShape/fr.md) s\'il y a de nombreux objets partiellement couverts par d\'autres. La valeur par défaut est {{value|Disabled}}, ce qui signifie qu\'aucune mise en évidence spéciale ne se produira; {{value|Enabled}} signifie que l\'objet apparaîtra au-dessus de tout autre objet lorsqu\'il est sélectionné; {{value|Object}} signifie que l\'objet n\'apparaîtra en haut que si l\'objet entier est sélectionné dans la [Vue en arborescence](Tree_view/fr.md); {{value|Element}} signifie que l\'objet n\'apparaîtra en haut que si un sous-élément (sommet, arête, face) est sélectionné dans la [Vue 3D](3D_view/fr.md).

-    {{PropertyView/fr|Selection Style|Enumeration}}: il contrôle la façon dont l\'objet est mis en évidence s\'il a une [Shape](Part_TopoShape/fr.md). Si c\'est {{value|Shape}}, la forme entière (sommets, arêtes et faces) sera mise en surbrillance dans la [Vue 3D](3D_view/fr.md); s\'il s\'agit de {{value|BoundBox}}, un cadre de délimitation apparaîtra autour de l\'objet et sera mis en surbrillance.

## Script


**Voir aussi:**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au programme.

Un App FeaturePython est créé avec la méthode `addObject()` du document.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::FeaturePython", "Name")
obj.Label = "Custom label"
```

Par exemple, les éléments [Draft Text](Draft_Text/fr.md), [Draft Dimension](Draft_Dimension/fr.md) et [Proxy pour plan de travail](Draft_WorkingPlaneProxy/fr.md) de l\'[Atelier Draft](Draft_Workbench/fr.md) sont des objets `App::FeaturePython` avec une icône personnalisée et des propriétés additionnelles. Ils contiennent des données mais pas une [Part TopoShape](Part_TopoShape/fr.md) réelle.

Si l\'objet souhaité doit avoir un placement, une forme, une pièce jointe ou d\'autres propriétés complexes, il est préférable de créer l\'une des classes les plus complexes, par exemple, [App GeoFeature](App_GeoFeature/fr.md), [Part Feature ](Part_Feature/fr.md) ou [Part Part2DObject](Part_Part2DObject/fr.md).


{{Document objects navi

}} 
