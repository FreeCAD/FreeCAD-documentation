# Body/fr
## Introduction

Dans FreeCAD, le mot \"[Body](Body/fr.md)\" est normalement utilisé pour faire référence à un objet [PartDesign Corps (Body)](PartDesign_Body/fr.md) (classe `PartDesign::Body`) défini par l\'[atelier PartDesign](PartDesign_Workbench/fr.md). Il s\'agit d\'un objet conteneur qui peut contenir des [esquisses 2D](Sketch/fr.md) et des [fonctions géométriques 3D](PartDesign_Feature/fr.md) pour créer une forme solide.

Voir [PartDesign Corps](PartDesign_Body/fr.md) pour plus d\'informations sur ce type d\'objet.



## Utilisation

1.  Basculer vers l\'[atelier PartDesign](PartDesign_Workbench/fr.md).
2.  Presser **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Corps](PartDesign_Body/fr.md)**.
3.  Presser **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Nouvelle esquisse](PartDesign_NewSketch/fr.md)** pour créer une nouvelle [esquisse](Sketch/fr.md).
4.  Créer un dessin fermé, puis utilisez **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Protrusion](PartDesign_Pad/fr.md)** pour extruder l\'esquisse et créer un solide initial.
5.  Ajouter d\'autres esquisses et protrusions et utiliser d\'autres outils de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) pour modifier et transformer le solide initial.

Au lieu d\'utiliser des [esquisses](Sketch/fr.md), vous pouvez ajouter des [PartDesign fonctions](PartDesign_Feature/fr.md) primitives, par exemple un **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [PartDesign Cube additif](PartDesign_AdditiveBox/fr.md)**. Un nombre illimité de fonctions additives et soustractives peuvent être utilisées pour créer un volume final.



## Remarques

Un corps est requis lors de l\'utilisation de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) dans une procédure de [modification d\'élément](feature_editing/fr.md).

Un corps n\'est pas requis lors de l\'utilisation de l\'[atelier Part](Part_Workbench/fr.md), car cet atelier utilise un flux de [géométrie constructive de solide](Constructive_solid_geometry/fr.md), basé sur des [formes primitives](Part_Primitives/fr.md) et des opérations booléennes.


{{PartDesign Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > Body/fr
