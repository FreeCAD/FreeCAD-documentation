---
- GuiCommand:/fr
   Name:Std Group
   Name/fr:Std Group
   MenuLocation:[Vue arborescente](Tree_view/fr.md) → Clic droit sur le nom du document
   Workbenches:Tous
   Shortcut:
   Version:
   SeeAlso:[Std Part](Std_Part/fr.md), [Draft Sélectionner un groupe](Draft_SelectGroup/fr.md), [Draft Ajouter au groupe](Draft_AddToGroup/fr.md)
---

# Std Group/fr

## Description

[Std Group](Std_Group/fr.md) (appelé en interne [App DocumentObjectGroup](App_DocumentObjectGroup/fr.md)) est un conteneur à usage général qui vous permet de regrouper différents types d\'objets dans la [vue par aborescence](tree_view/fr.md), quel que soit leur type de données. Il est utilisé comme un simple dossier pour classer et organiser les objets dans votre modèle afin de conserver une structure logique. Les Std Groupes peuvent être imbriqués dans d\'autres Std Groupes.

L\'outil Std Group n\'est pas défini par un atelier particulier mais par le système de base ; il se trouve donc dans la **barre d'outils de structure** qui est disponible dans tous les [Ateliers](Workbenches/fr.md).

Pour regrouper des objets 3D en une seule unité, avec l\'intention de créer des assemblages, utilisez plutôt [Std Part](Std_Part/fr.md).

![](images/Std_Group_example.png )



*Divers éléments à l'intérieur des Std Group dans la vue en arborescence.*

## Utilisation

1.  Cliquez sur le nom du document dans la [vue en arborescence](tree_view.md), ouvrez le menu contextuel (clic droit) et choisissez **Créer un groupe**.
2.  Vous pouvez également appuyer sur le bouton **<img src="images/Std_Group.svg" width=16px> [Group](Std_Group/fr.md)** dans la barre d\'outils de structure. Un groupe vide est créé.
3.  Pour ajouter des objets à un groupe, sélectionnez-les dans la [vue en arborescence](tree_view/fr.md) puis faites-les glisser et déposez-les sur le groupe.
4.  Pour supprimer des objets d\'un groupe, faites-les glisser hors du groupe et sur l\'étiquette du document en haut de la [vue en arborescence](tree_view/fr.md).

### Remarques

-   L\'objet Group n\'affecte pas les positions dans la [vue 3D](3D_view/fr.md) des éléments qu\'il contient ; il s\'agit essentiellement d\'un dossier qui permet d\'organiser la [vue en arborescence](tree_view.md).
-   Le groupe peut également être créé à partir de la [console Python](Python_console/fr.md), et sous-classé pour créer des \"groupes\" spéciaux, comme indiqué dans la section [Script](Std_Group/fr#Script.md).

## Propriétés

Un _ (classe `App::DocumentObject`). Il partage donc toutes les propriétés de ce dernier.

En plus des propriétés décrites dans [App FeaturePython](App_FeaturePython/fr.md), qui est l\'instance la plus élémentaire d\'un [App DocumentObject](App_DocumentObject/fr.md), App DocumentObjectGroup a la propriété **Group**.

Ce sont les propriétés disponibles dans l\'[éditeur de propriétés](property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Show all** dans le menu contextuel de l\'[éditeur de propriétés](property_editor/fr.md).

### Données


{{TitleProperty|Base}}

-    {{PropertyData/fr|Label|String}}: nom modifiable par l\'utilisateur de cet objet, c\'est une chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Group|LinkList}}: liste d\'objets référencés. Par défaut vide {{value|[]}}.

#### Propriétés cachées de Données 

-    {{PropertyData/fr|Proxy|PythonObject}}: classe personnalisée associée à cet objet. Cela n\'existe que pour la version [Python](Python/fr.md). Voir [Script](Std_Group/fr#Script.md).

### Vue


{{TitleProperty|Base}}

Voir [App FeaturePython](App_FeaturePython/fr.md) pour les propriétés d\'affichage de base.

#### Propriétés cachées de Vue 

-    {{PropertyView/fr|Proxy|PythonObject}}: classe personnalisée associée à cet objet. Cela n\'existe que pour la version [Python](Python/fr.md). Voir [Script](Std_Group/fr#Script.md).

## Héritage

Un _ (`App::DocumentObject` class) et est complété par une extension de groupe.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux du programme. La classe `App::DocumentObjectGroup* est un groupe simple qui utilise l'extension Groupe pour pouvoir contenir tout type d'objet.`

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au document.

Un Std Group ([App DocumentObjectGroup](App_DocumentObjectGroup/fr.md)) est créé avec la méthode `addObject()` du document. Une fois qu\'un groupe existe, d\'autres objets peuvent y être ajoutés avec les méthodes `addObject()` ou `addObjects()` de ce groupe. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroup", "Group")

bod1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
bod2 = App.ActiveDocument.addObject("Part::Box", "Box")

obj.addObjects([bod1, bod2])
App.ActiveDocument.recompute()
```


`App::DocumentObjectGroup`

de base n\'a pas d\'objet Proxy, il ne peut donc pas être entièrement utilisé pour la sous-classification.

Par conséquent, pour la sous-classe [Python](Python/fr.md), vous devez créer l\'objet `App::DocumentObjectGroupPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "Name")
obj.Label = "Custom label"
```

Par exemple, [Analyse FEM](FEM_Analysis/fr.md) est un objet `App::DocumentObjectGroupPython` avec une icône personnalisée et des propriétés supplémentaires.

## Liens

-   [Cas d\'utilisation dans Arch Tutorial](Arch_tutorial/fr#Organiser_votre_mod.C3.A8le.md)
-   [Structure du document](Document_structure/fr.md)
-   [Organisation de votre modèle](Arch_tutorial/fr#Organiser_votre_mod.C3.A8le.md)





{{Std Base navi

}}

---
[documentation index](../README.md) > Std Group/fr
