# Land Survey Workbench Blueprint/fr




{{VeryImportantMessage|
Ce plan de développement est probablement obsolète. Pour plus d'informations, voir [Plan de développement](Development_roadmap/fr.md).<br>
Si vous n'êtes pas impliqué dans le développement discuté ici :<br>
!!! S'IL VOUS PLAÎT, NE MODIFIEZ PAS ET NE TRADUISEZ PAS !!!
}}


{{VeryImportantMessage|Remarque importante : L'atelier Land Survey a été abandonné. Si des développeurs intéressés veulent en être le fer de lance, faites-le nous savoir sur le forum.}}


{{TOCright}}

Cette page répertorie les exigences et la mise en œuvre d\'un nouvel établi utilisable dans le domaine de [Land Survey (Arpentage)](http://en.wikipedia.org/wiki/Land_survey). La page est un peu dépassée. Vous trouverez les dernières informations sur le fil de discussion: <http://forum.freecadweb.org/viewtopic.php?f=8&t=6973>

## Selection rectangle 

> Un nouveau mode souris peut être requis:
>
> -   clic gauche sur un objet sélectionne l\'objet
> -   clic gauche dans un espace vide - commencer l\'action de sélection; cliquez à nouveau - terminer l\'action de sélection, ajouter au jeu de sélection
>     -   CTRL - exclure de l\'ensemble déjà sélectionné
> -   appuyez et maintenez le bouton du milieu pour faire un panoramique
> -   menu contextuel sur clic droit
> -   roue haut / bas - zoom

## Calques

-   Les propriétés des objets telles que la couleur, l\'épaisseur des lignes, la visibilité, la capacité d\'impression peuvent être définies par objet ou peuvent être héritées de la couche parente.
-   Chaque objet a un calque parent / un objet peut faire partie d\'un calque ou non.

## Blocs

Les blocs sont des objets qui se comportent dans la plupart des cas comme un seul objet. Les objets ne perdent pas leur individualité à l\'intérieur du bloc.

> S\'il y a un Upgrade/Downgrade, cette fonctionnalité peut déjà être présente.

### Attributs dynamiques 

Variables. Composants du bloc qui peuvent être modifiés sans changer la définition du bloc. La position à l\'intérieur du bloc est l\'un de ces attributs.

> Cette fonctionnalité s\'intégrera bien si elle est exprimée en tant que propriétés.

## Points

Dans l\'arpentage, les points sont généralement associés à des nombres, à une description et à d\'autres caractéristiques.

> Les blocs avec des propriétés dynamiques devraient le faire.

## Querry tools for 2 and a half system 

La position plane est généralement découplée (en particulier dans les applications de cadastre) de la hauteur. Lorsque vous voulez connaître la distance entre deux points, vous voulez en fait connaître la distance en projection horizontale. Le plan horizontal est XY, Y pointant vers le nord. Z pointe vers le haut (altitude positive).

## Format de texte enrichi ; Tableaux 

Support général pour le [format de texte enrichi](https://fr.wikipedia.org/wiki/Rich_Text_Format).

Remarque: les informations de cette page sont basées sur une compréhension superficielle des composants internes de FreeCAD. Cela demande à être approfondi. Les contributions sont les bienvenues! \--[Xtnickx](User:Xtnickx.md) 11:00, 26 January 2013 (UTC).



[Category:Roadmap](Category:Roadmap.md) [Category:Developer](Category:Developer.md)
