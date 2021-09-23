# Part/fr


## Introduction


{{TOCright}}

Dans FreeCAD, le mot \"[Part](Part/fr.md)\" est normalement utilisé pour faire référence à une classe <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std Part](Std_Part/fr.md) (`App::Part`), un type d\'objet conteneur défini par le système de base. Cette pièce permet de gérer la position des formes 3D afin de créer des assemblages mécaniques.

Voir <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std Part](Std_Part/fr.md) pour plus d\'informations sur ce type d\'objet.

## Comment l\'utiliser 

L\'outil Std Part n\'est pas défini par un atelier particulier, mais par le système de base, il se trouve donc dans la **structure toolbar**, qui est disponible dans tous les [ateliers](Workbenches/fr.md).

1.  Appuyez sur le bouton **<img src=images/_Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)**. Une pièce vide est créée et devient automatiquement *[active](Std_Part/fr#Active_status.md)*.

## Notes

Dans un usage informel, une \"pièce\" peut être n\'importe quelle figure géométrique visible dans la [vue 3D](3D_view/fr.md), et son concept peut donc être confondu avec celui de \"[Body](Body/fr.md)\" ou \"[Assembly](Assembly/fr.md)\".

Cependant, lorsque plus de précision est requise, la distinction doit être faite.

-   Un \"[Body](Body/fr.md)\" est utilisé pour des éléments contigus uniques, généralement créés avec les ateliers [Part](Part_Workbench/fr.md) ou [PartDesign](PartDesign_Workbench/fr.md).
    -   Un \"corps\" a une \"[Forme](Shape/fr.md)\".
-   Une \"pièce\" est utilisée pour regrouper un seul \"Body\", ou plusieurs d\'entre eux pour former un assemblage.
    -   Une \"pièce\" a une collection de \"[Shapes](Shape/fr.md)\", mais n\'a pas de \"Shape\" qui lui soit propre.
-   Un \"assemblage\" est une collection de \"pièces\" disposées d\'une manière ou d\'une autre, manuellement ou à l\'aide d\'un atelier d\'assemblage.


{{Std Base navi

}} {{Document objects navi}} 

[Category:Glossary](Category:Glossary.md)
