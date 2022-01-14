# App Part/fr
## Introduction

<img alt="" src=images/Geofeaturegroup.svg  style="width:32px;">

Un objet [App Part](App_Part/fr.md), ou officiellement un `App::Part`, est un élément qui permet de regrouper des objets dans l\'espace 3D.

Il a été développé pour être utilisé dans les assemblages. Son **Origin** sert de référence de position pour les objets groupés.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux du programme. La classe `App::Part* est un simple conteneur qui a une position dans l'espace 3D et a une origine pour contrôler le placement des objets regroupés sous celui-ci`

## Utilisation

1.  Appuyez sur le bouton **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)**. Un Part vide est créée et devient automatiquement *[active](Std_Part/fr#Statut_actif.md)*.
2.  Pour ajouter des objets à un Part, faites-les glisser et déposez-les sur Part dans la [vue en arborescence](tree_view/fr.md).
3.  Pour supprimer des objets d\'un Part, faites-les glisser hors de Part et sur l\'étiquette du document en haut de la [vue en arborescence](tree_view/fr.md).

Voir la page [Std Part](Std_Part/fr.md) pour les informations complètes, y compris son utilisation dans un [Script](Std_Part/fr#Script.md).

## Propriétés

Une classe [App Part](App_Part/fr.md) (classe `App::Part`) est dérivée de la classe de base [App GeoFeature](App_GeoFeature/fr.md) (classe `App::GeoFeature`) donc partage la plupart des propriétés de ce dernier.

Voir la liste complète des propriétés dans la page [Std Part](Std_Part/fr.md).


{{Std Base navi

}} {{Document objects navi}}

---
[documentation index](../README.md) > App Part/fr
