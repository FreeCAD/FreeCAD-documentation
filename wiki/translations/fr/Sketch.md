# Sketch/fr
## Introduction


{{TOCright}}

Dans FreeCAD, le mot \"[Sketch](Sketch/fr.md)\" est normalement utilisé pour désigner un [Objet esquisse](Sketcher_SketchObject/fr.md) (`Sketcher::Sketcher::SketchObject` class) définie par l\'[atelier Sketcher](Sketcher_Workbench/fr.md). Il s\'agit d\'un dessin 2D qui utilise des contraintes mathématiques pour décrire avec précision la géométrie 2D.

Voir [Sketcher SketchObject](Sketcher_SketchObject/fr.md) pour plus d\'informations sur le type d\'objet.

## Utilisation

Il existe deux manières courantes de créer une esquisse: directement dans l\'[atelier Sketcher](Sketcher_Workbench/fr.md), ou à partir de l\'[atelier PartDesign](PartDesign_Workbench/fr.md).

### Atelier Sketcher 

1.  Passez dans l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;">[atelier Sketcher](Sketcher_Workbench/fr.md).
2.  Cliquez sur le bouton **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Créer une esquisse](Sketcher_NewSketch/fr.md)**.

### Atelier PartDesign 

1.  Passez dans l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Atelier PartDesign](PartDesign_Workbench.md).
2.  Cliquez sur le bouton **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Corps](PartDesign_Body/fr.md)**.
3.  Cliquez sur le bouton **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Créer une esquisse](PartDesign_NewSketch/fr.md)**.

Une fois l\'édition de l\'esquisse terminée, fermez-la pour quitter le mode d\'édition. Double-cliquez dessus pour entrer à nouveau en mode édition.

## Remarques

Une esquisse est très couramment utilisée en conjonction avec l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Atelier PartDesign](PartDesign_Workbench/fr.md) pour créer des solides par extrusion, en utilisant le bouton **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Protrusion](PartDesign_Pad/fr.md)**.

Néanmoins, une esquisse peut toujours être créée à toute autre fin. Elle ne doit pas être liée à un [PartDesign Corps](PartDesign_Body/fr.md). Par exemple, l\'outil **[<img src=images/Arch_Window.svg style="width:16px"> [Arch Fenêtre](Arch_Window/fr.md)** de l\'<img alt="" src=images/Workbench_Arch.svg  style="width:16px;"> [Atelier Arch](Arch_Workbench/fr.md) utilise des esquisses pour définir les formes des fenêtres et des portes. De la même manière, elles peuvent être utilisées pour définir la forme de **[<img src=images/Arch_Wall.svg style="width:16px"> [Arch Murs](Arch_Wall/fr.md)**.


{{Sketcher Tools navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Sketcher](Category_Sketcher.md) > Sketch/fr
