# App Link/fr
{{TOCright}}

## Introduction

<img alt="" src=images/Link.svg  style="width:32px;">

Un [App Link](App_Link/fr.md), ou formellement un `App::Link`, est un type d\'objet qui fait référence ou lie à un autre objet dans le même document ou dans un autre document. Il est spécialement conçu pour dupliquer efficacement un seul objet plusieurs fois, ce qui permet de créer des [assemblages](assembly/fr.md) complexes à partir de sous-assemblages plus petits et de plusieurs composants réutilisables tels que des vis, des écrous et des éléments de fixation similaires.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux du programme. L'objet `App::Link* est un composant central du système : il ne dépend d'aucun atelier mais peut être utilisé avec la plupart des objets créés dans tous les ateliers.`

## Utilisation

1.  Sélectionnez un objet dans la [Vue en arborescence](Tree_view/fr.md) ou la [Vue 3D](3D_view/fr.md) pour lequel vous souhaitez créer un lien.
2.  Appuyez sur le bouton **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake/fr.md)**. L\'objet généré a la même icône que l\'objet d\'origine mais a une superposition de flèche indiquant qu\'il s\'agit d\'un lien.

Voir la page [Std LinkMake](Std_LinkMake/fr.md) pour les informations complètes, y compris son utilisation dans un [Script](Std_LinkMake/fr#Script.md).

## Propriétés

[App Link](App_Link/fr.md) (classe `App::Link`) est dérivée de la classe de base [App DocumentObject](App_DocumentObject/fr.md) (classe `App::DocumentObject`). Elle partage toutes les propriétés de cette dernière.

Voir la liste complète des propriétés à la page [Std Créer un lien](Std_LinkMake/fr.md).


{{Std Base navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > App Link/fr
