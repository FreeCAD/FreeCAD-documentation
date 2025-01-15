---
 GuiCommand:
   Name: Std Group
   Name/fr: Std Groupe
   MenuLocation: Tree_view/fr , Clic droit sur le nom du document , Créer un groupe
   Workbenches: Tous
   Shortcut: 
   Version: 
   SeeAlso: Std_Part/fr, Draft_SelectGroup/fr, Draft_AddToGroup/fr
---

# Std Group/fr

## Description

[Std Groupe](Std_Group/fr.md) (appelé en interne [App DocumentObjectGroup](App_DocumentObjectGroup/fr.md)) est un conteneur à usage général qui vous permet de regrouper différents types d\'objets dans la [vue en arborescence](Tree_view/fr.md), quel que soit leur type de données. Il est utilisé comme un simple dossier pour classer et organiser les objets dans votre modèle afin de conserver une structure logique. Les Std Groupes peuvent être imbriqués dans d\'autres Std Groupes.

L\'outil Std Groupe n\'est pas défini par un atelier particulier mais par le système de base. Il se trouve donc dans la **barre d'outils de structure** qui est disponible dans tous les [ateliers](Workbenches/fr.md).

Pour regrouper des objets 3D en une seule unité, avec l\'intention de créer des assemblages, utilisez plutôt [Std Part](Std_Part/fr.md).

![](images/Std_Group_example.png )



*Divers éléments à l'intérieur de Std Groupes dans la vue en arborescence.*



## Utilisation

1.  Effectuez l\'une des opérations suivantes :
    -   Cliquez avec le bouton droit de la souris sur le nom du document dans la [vue en arborescence](Tree_view/fr.md) et dans le menu contextuel, choisissez **Créer un groupe**.
    -   Appuyez sur le **<img src="images/Std_Group.svg" width=16px> [Créer un groupe](Std_Group/fr.md)**.
2.  Un groupe vide est créé.
3.  Pour ajouter des objets au groupe, sélectionnez-les dans la [vue en arborescence](Tree_view/fr.md) et faites un glisser/déposer dans le groupe.
4.  Pour supprimer des objets du groupe, faites-les glisser hors du groupe et déposez-les sur l\'étiquette du document en haut de [vue en arborescence](Tree_view/fr.md).
5.  Vous pouvez également ajouter et supprimer des objets en modifiant la propriété **Group** du groupe.



## Propriétés

[Std Groupe](Std_Group/fr.md), appelé en interne [App DocumentObjectGroup](App_DocumentObjectGroup/fr.md) (classe `App::DocumentObjectGroup`), est dérivé de l\'objet de base [App DocumentObject](App_DocumentObject/fr.md) (classe `App::DocumentObject`) et hérite de toutes ses propriétés.

Std Groupe a les mêmes propriétés que [App FeaturePython](App_FeaturePython/fr#Propri.C3.A9t.C3.A9s.md), qui est l\'instance la plus basique d\'un [App DocumentObject](App_DocumentObject/fr.md). Il possède également les propriétés supplémentaires suivantes dans l\'éditeur de propriétés de l\'[éditeur de propriétés](Property_editor/fr.md). Les propriétés cachées peuvent être affichées à l\'aide de la commande **Tout afficher** du menu contextuel de l\'[éditeur de propriétés](Property_editor/fr.md).



### Données


{{TitleProperty|Base}}

-    **Group|LinkList**: liste d\'objets référencés. Par défaut vide {{value|[]}}.

-    **_ Group Touched|Bool|Hidden**: indique si le groupe est touché ou non.



## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](Scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au document.

Std Groupe ([App DocumentObjectGroup](App_DocumentObjectGroup/fr.md)) est créé avec la méthode `addObject()` du document. Une fois qu\'un groupe existe, d\'autres objets peuvent y être ajoutés avec les méthodes `addObject()` ou `addObjects()`.


```python
import FreeCAD as App

doc = App.newDocument()
group = App.ActiveDocument.addObject("App::DocumentObjectGroup", "Group")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

group.addObjects([obj1, obj2])
App.ActiveDocument.recompute()
```


`App::DocumentObjectGroup`

de base n\'a pas d\'objet Proxy, il ne peut donc pas être entièrement utilisé pour la sous-classification.

Pour la sous-classification en [Python](Python/fr.md), vous devez créer l\'objet `App::DocumentObjectGroupPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "Name")
obj.Label = "Custom label"
```

Par exemple, une [analyse FEM](FEM_Analysis/fr.md) est un objet `App::DocumentObjectGroupPython` avec une icône personnalisée et des propriétés supplémentaires.



## Liens

-   [Cas d\'utilisation dans le tutoriel Arch](Arch_tutorial/fr#Organiser_votre_mod.C3.A8le.md)
-   [Structure du document](Document_structure/fr.md)
-   [Organisation de votre modèle](Arch_tutorial/fr#Organiser_votre_mod.C3.A8le.md)



---
⏵ [documentation index](../README.md) > Std Group/fr
