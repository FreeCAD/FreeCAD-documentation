# App DocumentObjectGroup/fr


## Introduction

<img alt="" src=images/Folder.svg  style="width:32px;">

Un objet [App DocumentObjectGroup](App_DocumentObjectGroup/fr.md), ou formellement un `App::DocumentObjectGroup`, est un élément simple qui permet de regrouper tout type de [App DocumentObject](App_DocumentObject/fr.md) dans la [vue en arborescence](tree_view/fr.md) quel que soit son type de données.

Il a été développé pour organiser les objets dans la [vue en arborescence](tree_view/fr.md) d\'une manière logique pour l\'utilisateur.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Diagramme simplifié des relations entre les objets principaux du programme. La classe `App::DocumentObjectGroup* a une extension qui lui permet de regrouper tout type d'objet. Le Group lui-même n'a pas beaucoup de propriétés.`

## Utilisation

1.  Appuyez sur le bouton **<img src=images/Std_Group.svg style="width:16px"> [Std Group](Std_Group/fr.md)** dans la barre d\'outils de structure. Un Group vide est créé.
2.  Pour ajouter des objets à un Group, sélectionnez-les dans la [vue en arborescence](tree_view/fr.md) puis faites-les glisser et déposez-les sur le Group.
3.  Pour supprimer des objets d\'un Group, faites-les glisser hors du Group et sur l\'étiquette du document en haut de la [vue en arborescence](tree_view/fr.md).

Voir la page [Std Group](Std_Part/fr.md) pour les informations complètes, y compris son utilisation dans un [Script](Std_Part/fr#Script.md).

## Propriétés

Un [App DocumentObjectGroup](App_DocumentObjectGroup/fr.md) (classe `App::DocumentObjectGroup`) est dérivé de la base [App DocumentObject](App_DocumentObject/fr.md) (`App::DocumentObject` class), par conséquent, il partage toutes les propriétés de ce dernier.

Voir les propriétés dans la page [Std Group](Std_Part/fr.md).


{{Std Base navi

}} {{Document objects navi}} 
