# Assembly/fr
## Introduction




Dans FreeCAD, le mot \"[Assembly](Assembly/fr.md)\" est normalement utilisé pour désigner un [modèle 3D](model/fr.md) composé de plusieurs parties distinctes, assemblées d\'une manière ou d\'une autre pour créer un objet fonctionnel, juste comme les produits de la vie réelle sont fabriqués.

Par exemple, un boulon, une rondelle et un écrou sont trois corps distincts qui, lorsqu\'ils sont assemblés, constituent un ensemble.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;">



*À gauche : trois solides distincts, chacun modélisé par un [PartDesign Corps](PartDesign_Body/fr.md).<br>À droite : les corps réunis dans un [Std Part](Std_Part.md) pour créer un assemblage.*



## Utilisation



### Assemblage manuel 

De manière générale, vous n\'avez pas besoin d\'outils spéciaux pour créer des assemblages, vous avez juste besoin de disposer de nombreux [corps](Body/fr.md) différents d\'une manière ou d\'une autre.

Pour positionner les corps où vous le souhaitez, vous pouvez

-   utiliser l\'outil [Std Transformer](Std_TransformManip/fr.md),
-   utiliser la fenêtre de dialogue <img alt="" src=images/Std_Placement.svg  style="width:16px;"> [Std Positionner](Std_Placement/fr.md), ou
-   modifier la propriété de [placement](Placement/fr.md) directement dans l\'[éditeur de propriétés](Property_editor/fr.md).

Vous pouvez utiliser l\'un des pseudo-assemblages faits par un des [ateliers externes](external_workbenches/fr.md) comme Lattice2, Manipulator, Part-o-magic ou WorkFeature, pour vous aider à trouver des intersections, mesurer des distances et distribuer vos objets de la manière souhaitée.

En général, l\'objet **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/fr.md)** a été conçu pour servir de bloc de construction de base pour créer des assemblages. Cet objet est utilisé pour regrouper plusieurs [corps](body/fr.md) et les déplacer ensemble en tant qu\'unité, c\'est-à-dire en tant que sous-ensemble. Ensuite, ce sous-assemblage peut être placé à côté ou utilisé à l\'intérieur d\'autres sous-assemblages afin de créer l\'assemblage final.



### Assemblage contraint 

Vous pouvez également utiliser l\'[atelier Assembly](Assembly_Workbench/fr.md) intégré ou des extensions, comme <img alt="" src=images/A2p_workbench.svg  style="width:24px;"> [A2plus](A2plus_Workbench/fr.md), <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Assembly3](Assembly3_Workbench/fr.md) ou <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Assembly4](Assembly4_Workbench/fr.md). Noter que [Assembly2](Assembly2_Workbench/fr.md) n\'est pas maintenu, il n\'est donc pas recommandé pour les nouveaux modèles.

Les ateliers d\'assemblage utilisent des contraintes et des expressions pour créer des relations entre les objets de votre modèle, afin de lier mathématiquement les objets en place, par exemple, \"cette face doit coller à cette autre face\", \"ce cylindre doit être concentrique à ce cercle \",\" ce point doit suivre ce bord \" etc\...

Il s\'agit d\'une utilisation avancée du logiciel qui est normalement utilisé dans les systèmes mécaniques complexes. Si votre [modèle](model/fr.md) n\'est pas très complexe, l\'utilisation d\'un atelier d\'assemblage peut ne pas être nécessaire.



## Remarques

-   Depuis FreeCAD 1.0, un [atelier Assembly](Assembly_Workbench/fr.md) officiel est inclus par défaut dans le système.

-   Noter que les ateliers d\'assemblage sont généralement incompatibles entre eux. Si vous créez un assemblage avec l\'un de ces ateliers, vous devez vous y tenir et ne pas utiliser un autre atelier d\'assemblage pour travailler avec le même document.


{{Std Base navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > Assembly/fr
