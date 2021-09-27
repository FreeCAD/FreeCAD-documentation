# SheetMetal Examples/fr
{{TOCright}}

## Introduction

L\'atelier SheetMetal est devenu très puissant et exige une documentation appropriée.

Pour éviter de surcharger les pages d\'outils avec des exemples, cette page a été ajoutée pour rassembler les pièces montrant et expliquant les caractéristiques spéciales de SheetMetal.

Phases planifiées pour générer du contenu :

1.  Collecte d\'images
2.  Ajout de descriptions de flux de travail
3.  Ajout de tutoriels plus détaillés

## Charnière

<img alt="" src=images/SheetMetal_Example-01.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-01a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01d.png  style="width:200px;"> *Processus de travail pour une charnière:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Cavité](PartDesign_Pocket/fr.md)**,
**<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Perçage](PartDesign_Hole/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

## Clip papier 

<img alt="" src=images/SheetMetal_Example-02.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-02a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02d.png  style="width:200px;"> *Processus de travail pour un clip papier:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> [Sketch on Sheet](SheetMetal_SketchOnSheet/fr.md)**,
cloner, retourner et fusionner,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

Dommage qu\'il manque un outil pour mettre en miroir l\'objet entier. Un objet de liaison pourrait être mis en miroir, mais lorsqu\'il est fusionné (booléen), le dépliage échoue. Pour obtenir une pièce dépliable avec les deux moitiés fusionnées, un clone ou l\'un d\'une paire d\'objets de liaison doit être retourné (tourné de 180°) au lieu d\'être mis en miroir.

## Collier oméga 

<img alt="" src=images/SheetMetal_Example-03.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-03a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03c.png  style="width:200px;"> *Processus de travail pour un collier oméga:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Perçage](PartDesign_Hole/fr.md)**,
**<img src="images/PartDesign_Fillet.svg" width=16px> [PartDesign Congé](PartDesign_Fillet/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

## Bol hexagonal 

<img alt="" src=images/SheetMetal_Example-04.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-04a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04c.png  style="width:200px;"> *Processus de travail pour un bol hexagonal:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall/fr.md)**,
6x **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Add Corner Relief](SheetMetal_AddCornerRelief/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

<img alt="" src=images/SheetMetal_Example-04d.png  style="width:200px;">

Lorsqu\'un grugeage d\'angle est ajouté (côté droit), il peut être nécessaire d\'ajuster la valeur de la propriété *Taille*.

## Pince à crayon 

<img alt="" src=images/SheetMetal_Example-05.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-05a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05d.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05e.png  style="width:200px;"> *Processus de travail pour une pince à crayon:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Cavité](PartDesign_Pocket/fr.md)**,
3x **<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

## Exemple de dépliage 

<img alt="" src=images/SheetMetal_Example-06.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-06a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06d.png  style="width:200px;"> *Processus de travail pour déplier:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall/fr.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude/fr.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

Pour la deuxième utilisation de **Extend Face**, une Esquisse avec deux contours est utilisée pour la forme de l\'extension(s) et avec la valeur de \"use subtraction\" réglée à true, elle fournit la forme pour les découpes aussi.

## Blindage d\'USB 

<img alt="" src=images/SheetMetal_Example-07.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-07a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07d.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07e.png  style="width:200px;"> *Processus de travail pour un blindage d'USB:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude/fr.md)**,
**<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Cavité](PartDesign_Pocket/fr.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude/fr.md)**,
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

(La forme de la languette n\'est qu\'une vision artistique de ce qui pourrait être caché à l\'intérieur d\'une vraie prise).

_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal Examples/fr
