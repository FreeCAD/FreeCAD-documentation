# Feature/fr
## Introduction

Dans FreeCAD, le mot \"[Feature](Feature/fr.md)\" est normalement utilisé pour faire référence à un objet [PartDesign Feature](PartDesign_Feature/fr.md) (classe `PartDesign::Feature`) défini par la classe [PartDesign Workbench](PartDesign_Workbench/fr.md). Il s\'agit d\'une opération ou d\'une étape de modélisation effectuée pour créer ou modifier un solide [Shape](Shape/fr.md) en suivant le paradigme [feature publishing](feature_editing/fr.md).

Voir [PartDesign Feature](PartDesign_Feature/fr.md) pour plus d\'informations sur ce type d\'objet.

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Atelier PartDesign](PartDesign_Workbench/fr.md).
2.  Appuyez sur **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Corps](PartDesign_Body/fr.md)**.
3.  Appuyez sur le bouton **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Nouvelle esquisse](PartDesign_NewSketch/fr.md)** pour créer une nouvelle [Esquisse](Sketch/fr.md).
4.  Créez un fil fermé, puis utilisez le bouron **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Protrusion](PartDesign_Pad/fr.md)** pour extruder l\'esquisse et créer un solide initial. Ce solide initial est la fonction initiale.
5.  Ajoutez plus d\'esquisses et de tampons et utilisez d\'autres outils de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) pour modifier et transformer le solide initial. Chacune de ces étapes correspond aux Caractéristiques du [Corps](Body/fr.md).
6.  Alternativement, ajoutez des objets primitifs, comme **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [PartDesign Cube additif](PartDesign_AdditiveBox/fr.md)** et **[<img src=images/PartDesign_SubtractiveCylinder.svg style="width:16px"> [PartDesign Cylindre soustractif](PartDesign_SubtractiveCylinder/fr.md)**. Un nombre quelconque d\'étapes additives et soustractives sont des fonctionnalités utilisées pour créer un volume final.

## Remarques

Dans le sens général, \"Feature\" peut être n\'importe quelle étape de modélisation utilisée pour créer une [Forme](Shape/fr.md) finale avec n\'importe quel outil de n\'importe quel [Atelier](Workbenches/fr.md).

-   Par exemple, dans l\'[Atelier Part](Part_Workbench/fr.md), dans le flux de travail de [géométrie solide constructive](constructive_solid_geometry/fr.md), \"Feature\" peut être n\'importe quelle opération booléenne comme **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Union](Part_Fuse/fr.md)**, **[<img src=images/Part_Cut.svg style="width:16px"> [Part Soustraction](Part_Cut/fr.md)** ou **[<img src=images/Part_Common.svg style="width:16px"> [Part Intersection](Part_Common/fr.md)**.

Dans un sens plus spécifique, une \"entité\" est une étape de modélisation utilisée à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md).

-   Par exemple, **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [PartDesign Cylindre additif](PartDesign_AdditiveCylinder/fr.md)**, **[<img src=images/PartDesign_AdditiveLoft.svg style="width:16px"> [PartDesign Lissage additif](PartDesign_AdditiveLoft/fr.md)**, **[<img src=images/_PartDesign_Pocket.svg style="width:16px"> [PartDesign Cavité](PartDesign_Pocket/fr.md)**, **[<img src=images/_PartDesign_SubtractiveCone.svg style="width:16px"> [PartDesign Cône soustractif](PartDesign_SubtractiveCone/fr.md)** etc\... sont toutes des \"Fonctionnalités\" (Features).


{{PartDesign Tools navi

}}  {{Document objects navi}} 

[<img src="images/Property.png" style="width:16px"> Glossary](Category_Glossary.md)

---
[documentation index](../README.md) > [Glossary](Category_Glossary.md) > Feature/fr
