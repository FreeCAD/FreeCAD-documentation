---
- GuiCommand:/fr
   Name:Std Part
   Name/fr:Std Part
   Workbenches:Tous
   MenuLocation:Aucun
   Version:0.17
   SeeAlso:[Std Groupe](Std_Group/fr.md), [PartDesign Corps](PartDesign_Body/fr.md)
---

# Std Part/fr

## Description


**[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)**

(appelé en interne [App Part](App_Part/fr.md)) est un conteneur à usage général qui conserve ensemble un groupe d\'objets afin qu\'ils puissent être déplacés ensemble en tant qu\'unité dans la [vue 3D](3D_view/fr.md).

L\'élément Std Part a été développé pour être le bloc de construction de base pour créer des [assemblages](assembly/fr.md) mécaniques. En particulier, il est conçu pour organiser les objets qui ont une [Part TopoShape](Part_TopoShape/fr.md), comme [Part Primitives](Part_CreatePrimitives/fr.md), [PartDesign Corps](PartDesign_Body/fr.md), et d\'autres [Part Features](Part_Feature/fr.md). Std Part fournit un [objet Origin](#Origine.md) avec des axes X, Y et Z locaux et des plans standard, qui peuvent être utilisés comme référence pour positionner les objets contenus. De plus, des Std Parts peuvent être imbriquées dans d\'autres Std Parts pour créer un grand assemblage à partir de sous-assemblages plus petits.

Bien qu\'elle soit principalement destinée aux corps solides, Std Part peut être utilisée pour gérer tout objet possédant une propriété [Positionnement](Placement/fr.md), elle peut donc également contenir [Mesh Features](Mesh_Feature/fr.md), [Esquisses](Sketch/fr.md) et d\'autres objets dérivés de la classe [App GeoFeature](App_GeoFeature/fr.md).

Ne pas confondre **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Corps](PartDesign_Body/fr.md)** avec **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)**. Le premier est un objet spécifique utilisé dans l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Atelier PartDesign](PartDesign_Workbench/fr.md), destiné à modéliser un [solide contigu unique](PartDesign_Body/fr#Solide_contigu_unique.md) au moyen de [PartDesign Features](PartDesign_Feature/fr.md). En revanche, [Std Part](Std_Part.md) n\'est pas utilisée pour la modélisation, juste pour arranger différents objets dans l\'espace, avec l\'intention de créer des [assemblages](assembly/fr.md).

L\'outil **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)** n\'est pas défini par un atelier particulier mais par le système de base. Il se trouve donc dans la **structure toolbar** qui est disponible dans tous les [ateliers](Workbenches/fr.md). Pour grouper des objets arbitrairement sans tenir compte de leur position, utilisez **[<img src=images/Std_Group.svg style="width:16px"> [Std Groupe](Std_Group/fr.md)**. Cet objet n\'affecte pas les placements des éléments qu\'il contient, c\'est essentiellement juste un dossier qui sert à garder la [Vue en arborescence](Tree_view/fr.md) organisée.

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )



*À gauche : éléments à l'intérieur d'une Std Part dans la [Vue en arborescence](Tree_view/fr.md). À droite : les objets positionnés dans l'espace, référés à l'origine de Std Part.*

## Utilisation

1.  Appuyez sur le bouton **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)**. Un Part vide est créée et devient automatiquement *[actif](Std_Part/fr#Statut_actif.md)*.
2.  Pour ajouter des objets à un Part, sélectionnez-les dans la [vue en arborescence](tree_view/fr.md), puis faites-les glisser et déposez-les sur le Part.
3.  Pour supprimer des objets d\'un Part, faites-les glisser hors du Part et sur l\'étiquette du document en haut de la [vue en arborescence](tree_view/fr.md).

### Remarques

-   Depuis la v0.19, un objet donné ne peut appartenir qu\'à un seul Part.
-   Double-cliquez sur Part dans la [vue en arborescence](tree_view/fr.md) ou ouvrez le menu contextuel (clic droit) et sélectionnez **Toggle active part** pour activer ou désactiver Part. Si un autre Part est actif, il sera désactivé. Voir [status actif](Std_Part/fr#Statut_actif.md) pour plus d\'informations.

### Limitations

-   À l\'heure actuelle, les méthodes [Draft accrochage](Draft_Snap/fr.md) ne fonctionnent pas sur les conteneurs de Part sélectionnés ni sur les objets à l\'intérieur de ceux-ci.
-   Part n\'a pas de [forme topologique](Part_TopoShape/fr.md) donc les opérations 3D comme les [Part Opérations booléennes](Part_Boolean/fr.md) ne peuvent pas être utilisées sur un Part lui-même. Par exemple, vous ne pouvez pas sélectionner deux Parts et effectuer une [Part Union](Part_Union/fr.md) ou une [Part Soustraction](Part_Cut/fr.md).
    -   Ces opérations booléennes ne fonctionnent que sur les objets contenus tant que ceux-ci sont dérivés de [Part Feature](Part_Feature/fr.md) et ont une [forme topologique](Part_TopoShape/fr.md).

## Propriétés

[Std Part](Std_Part/fr.md) est appelée en interne [App Part](App_Part/fr.md) (classe `App::Part`) et est dérivé d\'une [App GeoFeature](App_GeoFeature/fr.md) (classe `App::GeoFeature`). Il partage donc la plupart des propriétés de ce dernier.

En plus des propriétés décrites dans [App GeoFeature](App_GeoFeature/fr.md), la classe App Part possède des propriétés qui l\'aident à gérer les informations dans le contexte d\'un assemblage, par exemple, **Type**, **Id**, **License**, **LicenseURL**, **Color** et **Group**.

Ce sont les propriétés disponibles dans l\'[éditeur de propriétés](property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Show all** dans le menu contextuel de l\'[éditeur de propriétés](property_editor/fr.md).

### Données


{{TitleProperty|Base}}

-    {{PropertyData/fr|Type|String}}: une description de cet objet. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    {{PropertyData/fr|Id|String}}: une identification ou un numéro de pièce pour cet objet. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    {{PropertyData/fr|License|String}}: un champ pour spécifier la licence pour cet objet. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    {{PropertyData/fr|LicenseURL|String}}: un champ pour spécifier l\'adresse Web de la licence ou du contrat pour cet objet. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    {{PropertyData/fr|Color|Color}}: un tuple de quatre valeurs RGBA à virgule flottante white color.

-    {{PropertyData/fr|Placement|Placement}}: la position de l\'objet dans la [Vue 3D](3D_view/fr.md). Le placement est défini par un point `Base` (vecteur) et une `Rotation` (axe et angle). Voir [Positionnement](Placement/fr.md).

    -   
        {{PropertyData/fr|Angle}}
        
        : l\'angle de rotation autour de {{PropertyData/fr|Axis}}. Par défaut, il s\'agit de {{value|0°}} (zéro degré).

    -   
        {{PropertyData/fr|Axis}}
        
        : le vecteur unitaire qui définit l\'axe de rotation pour le placement. Chaque composant est une valeur à virgule flottante entre {{value|0}} et {{value|1}}. Si une valeur est supérieure à {{value|1}}, le vecteur est normalisé de sorte que l\'amplitude du vecteur est {{value|1}}. Par défaut, il s\'agit de l\'axe Z positif, {{value|(0, 0, 1)}}.

    -   
        {{PropertyData/fr|Position}}
        
        : un vecteur avec les coordonnées 3D du point de base. Par défaut, c\'est l\'origine {{value|(0, 0, 0)}}.

-    {{PropertyData/fr|Label|String}}: le nom modifiable par l\'utilisateur de cet objet, c\'est une chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Group|LinkList}}: une liste d\'objets référencés. Par défaut, il est vide {{value|[]}}.

##### Propriétés cachées de Données 

-    {{PropertyData/fr|Material|Map}}: carte avec les propriétés du matériau. Par défaut, il est {}.

-    {{PropertyData/fr|Meta|Map}}: carte avec des méta-informations supplémentaires. Par défaut, il est {}.

-    {{PropertyData/fr|Uid|UUID}}: l\'identifiant universellement unique [universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) (UUID) (numéro 128 bits) de l\'objet. Ceci est attribué au moment de la création.

-    {{PropertyData/fr|Label2|String}}: une description plus longue et modifiable par l\'utilisateur de cet objet, c\'est une chaîne UTF8 arbitraire qui peut inclure des retours à la ligne. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    {{PropertyData/fr|Expression Engine|ExpressionEngine}}: une liste d\'expressions. Par défaut, il est vide {{value|[]}}.

-    {{PropertyData/fr|Visibility|Bool}}: afficher ou non l\'objet.

-    {{PropertyData/fr|Origin|Link}}: l\'objet [App Origin](App_Origin/fr.md) qui est la référence de position pour tous les éléments répertoriés dans **Group**.

-    {{PropertyData/fr|_ Group Touched|Bool}}: si le groupe est touché ou non.

### Vue

App Part n\'a que les cinq propriétés de la base [App FeaturePython](App_FeaturePython/fr.md) et n\'a pas de propriétés masquées.


{{TitleProperty|Base}}

-    {{PropertyView/fr|Display Mode|Enumeration}}: {{value|Group}}.

-    {{PropertyView/fr|On Top When Selected|Enumeration}}: {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    {{PropertyView/fr|Selection Style|Enumeration}}: {{value|Shape}} (défaut), {{value|BoundBox}}. Si l\'option est {{value|Shape}}, la forme entière (sommets, arêtes et faces) sera mise en surbrillance dans la [vue 3D](3D_view/fr.md) ; s\'il s\'agit de {{value|BoundBox}}, seul le cadre de sélection sera mis en surbrillance.

-    {{PropertyView/fr|Show In Tree|Bool}}: s\'il s\'agit de `True`, l\'objet apparaît dans la [vue en arborescence](Tree_view/fr.md). Sinon, il est défini comme invisible.

-    {{PropertyView/fr|Visibility|Bool}}: s\'il s\'agit de `True`, l\'objet apparaît dans la [vue 3D](3D_view/fr.md) ; sinon il est invisible. Par défaut, cette propriété peut être activée et désactivée en appuyant sur la barre **Espace** du clavier.

## Concept d\'assemblage 

Std Part est destiné à être le bloc de construction de base pour créer des assemblages. Contrairement à un [PartDesign Corps](PartDesign_Body/fr.md), un assemblage est censé être une collection d\'éléments distincts et distinctifs qui sont connectés d\'une manière ou d\'une autre dans le monde physique, par exemple par pression, vis ou colle.

Exemples qui pourraient être des Parts :

-   Une table en bois composée de pièces individuelles en bois (pieds, plateau) assemblées par de la colle ou des vis métalliques.
-   Un roulement à billes composé de plusieurs billes en acier, d\'une bague intérieure, d\'un dispositif de retenue, d\'un joint et d\'une bague extérieure.
-   Un assemblage d\'une vis avec une rondelle et un écrou assorti.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*A gauche : trois solides contigus individuels, chacun modélisé par un [PartDesign Corps](PartDesign_Body/fr.md). À droite : les corps individuels réunis à l'intérieur d'un Std Part pour créer un assemblage.*

De manière générale, lors de l\'importation d\'un fichier STEP dans le programme, l\'assemblage principal et ses sous-assemblages seront importés en tant que conteneurs de Parts, chacun d\'eux contenant une simple [Part Feature](Part_Feature/fr.md).

## Explications détaillées 

### Statut actif 

Un document ouvert peut contenir plusieurs Part. Un Part actif sera affiché dans la [vue en arborescence](Tree_view/fr.md) avec la couleur d\'arrière-plan spécifiée par la valeur **Conteneur actif** dans [éditeur de préférences](Preferences_Editor/fr#Couleurs.md) (par défaut, clair bleu). Une partie active sera également affichée en gras.

Pour activer ou désactiver un Part :

-   Double-cliquez dessus dans l\'[arborescence](Tree_view/fr.md) ou
-   Ouvrez le menu contextuel (clic droit) et sélectionnez **Toggle active part**.


**Remarques :**

-    {{emphasis|active status}}de Parts a été développé en v0.17 en parallèle avec le {{emphasis|active status}} de [PartDesign Corps](PartDesign_Body/fr.md). Cependant, à partir de la v0.19, ce statut ne sert plus à rien pour les Parts.

-   Même lorsqu\'un Part est actif, les objets nouvellement créés ne sont pas placés automatiquement à l\'intérieur. Dans ce cas, faites simplement glisser ces nouveaux objets et déposez-les sur le Part souhaité.

-   Un seul Part peut être actif à la fois.

![](images/Std_Part_active.png )



*Document avec deux Std Parts, dont le second est actif.*

### Origine

L\'Origine se compose des trois axes standard (X, Y, Z) et de trois plans standard (XY, XZ et YZ). Les [Esquisses](Sketch/fr.md) et d\'autres objets peuvent être attachés à ces éléments lors de leur création.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )



*À gauche : Part Origin dans la [vue en arborescence](tree_view/fr.md) et telle qu'elle apparaît affichée dans la [vue 3D](3D_view/fr.md). À droite : représentation des éléments Origin dans la [Vue 3D](3D_view/fr.md).*


**Remarque :**

L\'origine est un [App Origin](App_Origin/fr.md) objet (de classe `App::Origin`) tandis que les axes et les plans sont respectivement des objets de type `App::Line` et `App::Plane`. Chacun de ces éléments peut être masqué et non masqué individuellement avec la barre **Espace**. Cela est utile pour choisir la référence correcte lors de la création d\'autres objets.


**Remarque 2 :**

tous les éléments à l\'intérieur du Part sont référencés à l\'origine du Part, ce qui signifie que le Part peut être déplacé et tourné en référence au système de coordonnées global sans affecter le placement des éléments à l\'intérieur.

### Gestion de la visibilité 

La visibilité d\'un Part remplace la visibilité de tout objet qu\'elle contient. Si Part est masqué, les objets qu\'il contient seront également masqués, même si leur propriété individuelle **Visibility** est définie sur `True`. Si Part est visible, la **Visibility** de chaque objet détermine si l\'objet est affiché ou non.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*La visibilité de Std Part détermine si les objets regroupés sous lui sont affichés dans la [vue 3D](3D_view/fr.md) ou non. À gauche : Part est masqué, donc aucun des objets ne sera affiché dans la [vue 3D](3D_view/fr.md). À droite : Part est visible, donc chaque objet contrôle sa propre visibilité.*

### Héritage

Un [Std Part](Std_Part/fr.md) est formellement une instance de la classe `App::Part` dont le parent est la base de [App GeoFeature](App_GeoFeature/fr.md) (`App::GeoFeature` class) et est complété par une extension Origin.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux du programme. La classe `App::Part* est un simple conteneur qui a une position dans l'espace 3D et a une origine pour contrôler le placement des objets regroupés sous celui-ci`

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au document.

Std Part ([App Part](App_Part/fr.md)) est créé avec la méthode `addObject()` du document. Une fois que Part existe, d\'autres objets peuvent y être ajoutés avec les méthodes `addObject()` ou `addObjects()` de Part.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::Part", "Part")

bod1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
bod2 = App.ActiveDocument.addObject("Part::Box", "Box")

obj.addObjects([bod1, bod2])
App.ActiveDocument.recompute()
```

Vous ne pouvez pas créer un `App::Part` scripté. Cependant, vous pouvez ajouter un comportement `App::Part` à un objet `Part::FeaturePython` scripté en utilisant le code suivant :


```python
class MyGroup(object):
    def __init__(self, obj=None):
        self.Object = obj
        if obj:
            self.attach(obj)

    def __getstate__(self):
        return

    def __setstate__(self, _state):
        return

    def attach(self, obj):
        obj.addExtension('App::OriginGroupExtensionPython')
        obj.Origin = FreeCAD.ActiveDocument.addObject('App::Origin', 'Origin')

    def onDocumentRestored(self, obj):
        self.Object = obj

class ViewProviderMyGroup(object):
    def __init__(self, vobj=None):
        if vobj:
            vobj.Proxy = self
            self.attach(vobj)
        else:
            self.ViewObject = None

    def attach(self, vobj):
        vobj.addExtension('Gui::ViewProviderOriginGroupExtensionPython')
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject('Part::FeaturePython', 'Group', group.MyGroup(), group.ViewProviderMyGroup(), True)
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std Part/fr
