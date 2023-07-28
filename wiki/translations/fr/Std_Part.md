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

1.  Appuyez sur le bouton **[<img src=images/Std_Part.svg style="width:16px"> [Créer une pièce](Std_Part/fr.md)**.
2.  Une pièce vide est créée et devient automatiquement *[active](#Statut_actif.md)*.
3.  Pour ajouter des objets à la pièce, sélectionnez-les dans la [Vue en arborescence](Tree_view/fr.md), puis faites-les glisser et déposez-les sur la pièce.
4.  Pour retirer des objets de la pièce, faites-les glisser hors de la pièce et déposez-les sur l\'étiquette du document en haut de la [Vue en arborescence](Tree_view/fr.md).
5.  Vous pouvez également ajouter et supprimer des objets en modifiant la propriété **Group** de la pièce.



## Remarques

-   Un objet ne peut appartenir qu\'à une seule pièce.
-   Les opérations 3D comme les [Part Opération booléenne](Part_Boolean/fr.md) ne peuvent pas être appliquées aux pièces. Par exemple, vous ne pouvez pas sélectionner deux pièces et effectuer un [Part Union](Part_Fuse/fr.md) ou un [Part Soustraction](Part_Cut/fr.md).



## Propriétés

[Std Part](Std_Part/fr.md), appelée en interne [App Part](App_Part/fr.md) (classe `App::Part`), est dérivé de [App GeoFeature](App_GeoFeature/fr.md) (classe `App::GeoFeature`) et hérite de toutes ses propriétés. Il possède également plusieurs propriétés supplémentaires. Notamment des propriétés qui l\'aident à gérer les informations dans le contexte d\'un assemblage, par exemple, **Type**, **Id**, **License**, **LicenseURL** and **Group**.

Ce sont les propriétés disponibles dans l\'[éditeur de propriétés](Property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Show all** dans le menu contextuel de l\'[éditeur de propriétés](Property_editor/fr.md).



### Données


{{TitleProperty|Base}}

-    **Type|String**: une description pour cet objet. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    **Material|Link**: le matériau de cet objet.

-    **Meta|Map|Hidden**: avec des méta-informations supplémentaires. Par défaut, il est vide {}.

-    **Id|String**: une identification ou un numéro de pièce pour cet objet. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    **Uid|UUID|Hidden**: l\'[identificateur unique et universel](https://fr.wikipedia.org/wiki/Universally_unique_identifier) (UUID) (numéro de 128 bits) de l\'objet. Il est attribué au moment de la création.

-    **License|String**: champ permettant de spécifier la licence de cet objet. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    **LicenseURL|String**: champ permettant de spécifier l\'adresse web de la licence ou du contrat pour cet objet. Par défaut, il s\'agit d\'une chaîne vide {{value|""}}.

-    **Color|Color**: un tuple de quatre valeurs RGBA à virgule flottante couleur blanche.

-    **Placement|Placement**: la position de l\'objet dans la [Vue 3D](3D_view/fr.md). L\'emplacement est défini par un point `Base` (vecteur) et un `Rotation` (axe et angle). Voir [Placement](Placement/fr.md).

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

-    **Visibility|Bool|Hidden**: affichage ou non l\'objet.

-    **Origin|Link|Hidden**: l\'objet [App Origin](App_OriginGroupExtension.md) qui sert de référence positionnelle pour tous les éléments énumérés dans **Group**.

-    **Group|LinkList**: une liste d\'objets référencés. Par défaut, elle est vide {{value|[]}}.

-    **_Group Touched|Bool|Hidden**: indique si le groupe est touché ou non.



### Vue


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: {{value|Group}}.

-    **Show In Tree|Bool**: si la valeur est `True`, l\'objet apparaît dans la [Vue en arborescence](Tree_view/fr.md). Sinon, il est défini comme invisible.

-    **Visibility|Bool**: si elle est `True`, l\'objet apparaît dans la [Vue 3D](3D_view/fr.md) ; sinon, il est invisible. Par défaut, cette propriété peut être activée ou désactivée en appuyant sur la barre **Espace** du clavier.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (par défaut) (par défaut), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selection Style|Enumeration**: {{value|Shape}}. (par défaut), {{value|BoundBox}}. Si l\'option est {{value|Shape}}, la forme entière (sommets, arêtes et faces) sera mise en évidence dans la [Vue 3D](3D_view/fr.md) ; si elle est {{value|BoundBox}}, seule la boîte de délimitation sera mise en évidence.



## Explications détaillées 



### Statut actif 

Un document ouvert peut contenir plusieurs parties. Mais une seule pièce peut être active. La partie active est affichée dans la [vue en arborescence](Tree_view/fr.md) avec la couleur de fond spécifiée par la valeur **Contenant actif** dans l\'[éditeur de préférences](Preferences_Editor/fr#Couleurs.md) (par défaut, bleu clair). Il sera également affiché avec du texte en gras.

Pour activer ou désactiver un Part :

-   Double-cliquez dessus dans l\'[arborescence](Tree_view/fr.md) ou
-   Ouvrez le menu contextuel (clic droit) et sélectionnez **Toggle active part**.

![](images/Std_Part_active.png )



*Document avec deux Std Parts, dont le second est actif.*



### Origine

L\'Origine se compose des trois axes standard (X, Y, Z) et de trois plans standard (XY, XZ et YZ). Les [esquisses](Sketch/fr.md) et d\'autres objets peuvent être attachés à ces éléments lors de leur création.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )



*À gauche : Part Origin dans la [vue en arborescence](Tree_view/fr.md). À droite : représentation des éléments Origin dans la [Vue 3D](3D_view/fr.md).*


**Remarque**

: L\'origine est un [App Origin](App_OriginGroupExtension/fr.md) objet (de classe `App::Origin`) tandis que les axes et les plans sont respectivement des objets de type `App::Line` et `App::Plane`. Chacun de ces éléments peut être masqué et non masqué individuellement avec la barre **Espace**. Cela est utile pour choisir la référence correcte lors de la création d\'autres objets.


**Remarque 2 :**

tous les éléments à l\'intérieur du Part sont référencés à l\'origine du Part, ce qui signifie que le Part peut être déplacé et tourné en référence au système de coordonnées global sans affecter le placement des éléments à l\'intérieur.



### Gestion de la visibilité 

La visibilité d\'un Part remplace la visibilité de tout objet qu\'elle contient. Si Part est masqué, les objets qu\'il contient seront également masqués, même si leur propriété individuelle **Visibility** est définie sur `True`. Si Part est visible, la **Visibility** de chaque objet détermine si l\'objet est affiché ou non.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*La visibilité de Std Part détermine si les objets regroupés sous lui sont affichés dans la [vue 3D](3D_view/fr.md) ou non. À gauche : Part est masqué, donc aucun des objets ne sera affiché dans la [vue 3D](3D_view/fr.md). À droite : Part est visible, donc chaque objet contrôle sa propre visibilité.*



## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](Scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au document.

Std Part ([App Part](App_Part/fr.md)) est créé avec la méthode `addObject()` du document. Une fois que Part existe, d\'autres objets peuvent y être ajoutés avec les méthodes `addObject()` ou `addObjects()`.


```python
import FreeCAD as App

doc = App.newDocument()
part = App.ActiveDocument.addObject("App::Part", "Part")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

part.addObjects([obj1, obj2])
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
        obj.addExtension("App::OriginGroupExtensionPython")
        obj.Origin = FreeCAD.ActiveDocument.addObject("App::Origin", "Origin")

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
        vobj.addExtension("Gui::ViewProviderOriginGroupExtensionPython")
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject("Part::FeaturePython",
                             "Group",
                             group.MyGroup(),
                             group.ViewProviderMyGroup(),
                             True)
```





{{Std_Base_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Part/fr
