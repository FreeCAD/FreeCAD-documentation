---
 TutorialInfo:r
   Topic: Assembly3, un squelette cinématique
   Level: Une connaissance de base d'Assembly3 et des outils Sketcher est utile.
   FCVersion: 0.20 et ultérieure
   Time: 40 minutes
   Author: User:FBXL5
   SeeAlso: Tutorial_KinematicAssembly/fr, Tutorial_KinematicController/fr
---

# Tutorial KinematicSkeleton/fr





## Introduction

Ce tutoriel explique comment mettre en place un mécanisme simple en 2D et attacher des objets en 3D, principalement à l\'aide de les outils de l\' <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [atelier Assembly3](Assembly3_Workbench/fr.md) externe.

Ce tutoriel n\'utilise pas le principe du schéma squelette (voir Assembly3 [Create-Skeleton-Sketch](https://github.com/realthunder/FreeCAD_assembly3/wiki/Create-Skeleton-Sketch) sur GitHub).

Nous utiliserons plutôt des <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [PartDesign Corps](PartDesign_Body/fr.md) ne contenant qu\'une seule <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [esquisse](Sketcher_Workbench/fr.md), pour construire un mécanisme en 2D, un **squelette multi esquisse**.

Les dimensions, ainsi que les couleurs, sont tirées du [tutoriel SolveSpace](http://solvespace.com/linkage.pl) auquel il est fait référence sur la page GitHub de Assembly3 (voir ci-dessus).

## Squelette à plusieurs esquisses 

Ce squelette dit \"multi esquisses\" se compose de plusieurs <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Corps](PartDesign_Body/fr.md) individuels et un conteneur <img alt="" src=images/Assembly_New_Assembly.svg  style="width:16px;"> [Assemblage](Assembly3_CreateAssembly/fr.md). Pour pouvoir attacher d\'autres objets, chaque corps est placé dans un conteneur d\'assemblage distinct.

### Objets du corps 2D 

Les corps, et leurs esquisses, qui sont utilisés dans ce montage :

-   Une plaque de base (vert)
-   Une manivelle (bleue)
-   Deux plaques mobiles (rouge et gris)
-   Quatre bielles (blanche, jaune, violette et marron)

<img alt="" src=images/Assembly3_SketchSkeleton-01.png  style="width:400px;"> 
*Les huit esquisses sont colorées individuellement et positionnées manuellement en déplaçant leurs corps parents*

La forme peut s\'écarter de celle de la pièce réelle, mais la position de l\'articulation définissant la géométrie doit être précise.

### Conteneurs d\'assemblage 

#### Assemblage parent 

Pour fixer ou contrôler la position de tous les corps, il faut un <img alt="" src=images/Assembly_New_Assembly.svg  style="width:16px;"> objet Assembly. Il ajoute une branche Assembly à la [Vue en arborescence](Tree_view/fr.md).

-   Appuyez sur le bouton **<img src="images/Assembly_New_Assembly.svg" width=16px> [Create assembly](Assembly3_CreateAssembly/fr.md)** pour créer une branche Assembly dans la [Vue en arborescence](Tree_view/fr.md).

#### Sous-assemblages 

Répétez l\'action ci-dessus pour créer un objet Assembly pour chaque corps et faites glisser le corps dans son conteneur Parts. Fixez ensuite le corps à son assemblage :

1.  Activez l\'objet Assembly (double-cliquez).
2.  Sélectionnez un cercle/arc appartenant à l\'objet Body.
3.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintLock.svg" width=16px> [Create "Locked" constraint](Assembly3_ConstraintLock/fr.md)** pour fixer le corps dans son sous-assemblage.

L\'assemblage de la manivelle, par exemple, doit ressembler à ceci :

<img alt="" src=images/Assembly3_SketchSkeleton-25.png  style="width:500px;"> 
*La branche du sous-assemblage de la manivelle dans l'arborescence et la manivelle avec son élément verrouillé dans la vue 3D*

#### Arborescence Assembly 

Dans la vue en arborescence, faites glisser toutes les branches du sous-assemblage dans le conteneur Parts de l\'objet Assembly parent.

<img alt="" src=images/Assembly3_SketchSkeleton-26.png  style="width:300px;"> 
*Branche Assembly dans la vue en arborescence*

Ils sont maintenant prêts à être arrangés.

### Plaque de base fixe 

Tout d\'abord, nous avons besoin d\'une partie fixe. Pour fixer complètement la base, nous sélectionnons habituellement une face, mais dans ce cas, un cercle fera aussi bien l\'affaire.

1.  Sélectionnez un cercle de la base.
2.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Create "Locked" constraint](Assembly3_ConstraintLock/fr.md)** pour fixer la base.

<img alt="" src=images/Assembly3_SketchSkeleton-02.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-03.png  style="width:300px;"> 
*Cercle sélectionné → Base fixée avec l'objet Element créé et le système de coordonnées de l'élément (ECS) affiché (vert)*

### Liaisons

Pour les articulations de type charnière, nous sélectionnons un cercle de chaque esquisse et utilisons la contrainte <img alt="" src=images/Assembly_ConstraintCoincidence.svg  style="width:16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence/fr.md). Non seulement elle rend les plans XY des deux éléments coplanaires, mais elle rend également leurs axes Z colinéaires.

1.  Sélectionnez un cercle de chaque objet à connecter.
2.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintCoincidence.svg‎‎" width=16px> [Create "Plane Coincidence" constraint](Assembly3_ConstraintCoincidence/fr.md)**.

#### Base - Manivelle 

<img alt="" src=images/Assembly3_SketchSkeleton-04.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-05.png  style="width:300px;"> 
*Cercles sur la base et la manivelle sélectionnés → Manivelle relocalisée avec les objets Élément et ECS créés affichés (vert)*

#### Base - Plateau supérieur 

<img alt="" src=images/Assembly3_SketchSkeleton-06.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-07.png  style="width:300px;"> 
*Cercles sur la plaque de base et la plaque supérieure sélectionnés → Plaque supérieure relocalisée*

Les liaisons déjà créées peuvent être identifiées par leurs représentations de contraintes (rouge).

#### Manivelle - tige 1 

<img alt="" src=images/Assembly3_SketchSkeleton-08.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-09.png  style="width:300px;"> 
*Cercles sur la manivelle et la tige 1 sélectionnés → Tige 1 déplacée et manivelle inclinée*

#### Plaque supérieure - tige 1 

La dernière liaison de cette chaîne cinématique relie deux éléments dont les directions Z sont déjà définies et une contrainte <img alt="" src=images/Assembly_ConstraintPointOnLine.svg  style="width:16px;"> [Point on line](Assembly3_ConstraintPointOnLine/fr.md) est tout ce dont nous avons besoin.

1.  Sélectionnez un cercle de chaque objet à connecter.
2.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintPointOnLine.svg‎‎" width=16px> [Create "PointOnLine" constraint](Assembly3_ConstraintPointOnLine/fr.md)**.

<img alt="" src=images/Assembly3_SketchSkeleton-10.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-11.png  style="width:300px;"> 
*Cercles sur la plaque supérieure et la tige 1 sélectionnés → Tige 1 déplacée, manivelle et plaque supérieure inclinées*

Si les axes Z de trois éléments ou articulations sont parallèles et se trouvent sur le même plan virtuel, le solveur peut échouer à les réarranger dans une étape suivante parce qu\'il est incapable de décider dans quelle direction l\'articulation centrale doit être tournée. Cela peut se produire pour l\'élément tige 1, l\'articulation manivelle - tige 1 et l\'articulation base - manivelle que nous avons ici. Dans ce cas, nous devons aider le solveur et faire tourner un objet (par exemple la manivelle) manuellement en utilisant l\'outil <img alt="" src=images/Assembly_AxialMove.svg  style="width:16px;"> [Axial move](Assembly3_AxialMove/fr.md).

#### Plaque supérieure - tige 2 

Une autre (sous-)chaîne cinématique commence avec des contraintes <img alt="" src=images/Assembly_ConstraintCoincidence.svg  style="width:16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence/fr.md).

<img alt="" src=images/Assembly3_SketchSkeleton-12.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-13.png  style="width:300px;"> 
*Cercles sur la plaque supérieure (ou la base) et tige 2 sélectionnés → Tige 2 relocalisée*

#### Tige 2 - Plaque inférieure 

<img alt="" src=images/Assembly3_SketchSkeleton-14.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-15.png  style="width:300px;"> 
*Cercles sur la tige 2 et plaque inférieure sélectionné → Plaque inférieure déplacée et tige 2 inclinée*

#### Plaque supérieure - tige 3 

<img alt="" src=images/Assembly3_SketchSkeleton-16.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-17.png  style="width:300px;"> 
*Cercles sur la plaque supérieure et tige 3 sélectionnés → Déplacement de la tige 3 et réorganisation de la sous-chaîne cinématique supérieure*

#### Plaque inférieure - tige 3 

Et cette (sous-)chaîne cinématique se termine par une contrainte <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:16px;"> [Point on line](Assembly3_ConstraintPointOnLine/fr.md) aussi.

<img alt="" src=images/Assembly3_SketchSkeleton-18.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-19.png  style="width:300px;"> 
*Cercles sur la plaque inférieure et tige 3 sélectionnés → Relocalisation de la tige 3 et réarrangement des sous-chaînes ukinématiques*

Pour relier les deux sous-chaînes cinématiques, nous utilisons la tige 4 avec une contrainte <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence/fr.md) à une extrémité et une contrainte <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:16px;"> [Point on line](Assembly3_ConstraintPointOnLine/fr.md) à l\'autre extrémité.

#### Manivelle - tige 4 

<img alt="" src=images/Assembly3_SketchSkeleton-20.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-21.png  style="width:300px;"> 
*Cercles sur la manivelle et la tige 4 sélectionnés → Tige 4 relocalisée*

#### Plaque inférieure - tige 4 

<img alt="" src=images/Assembly3_SketchSkeleton-22.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-23.png  style="width:300px;"> 
*Cercles sur la plaque inférieure et tige 4 sélectionnés → Tige 4 déplacée et disposition finale de l'assemblage cinématique*

### Actionneur

Puisque Assembly3 ne fournit aucun moyen de contrôler les assemblages cinématiques, nous avons besoin d\'une aide externe telle que ce [contrôleur cinématique](Tutorial_KinematicController/fr.md). Pour utiliser ce contrôleur, nous devons marquer l\'étiquette d\'une contrainte avec le suffixe {{Incode|"Driver"}} pour en faire une contrainte de mouvement. Il peut être séparé par un {{Incode|"."}} ou {{Incode|"-"}} pour plus de clarté, car le contrôleur ne vérifiera que si le label se termine par {{Incode|"Driver"}}.

Nous changeons donc le label de la liaison Base-Manivelle en {{Incode|Base-Crank.Driver}}.

### Squelette terminé 

L\'assemblage cinématique terminé avec la représentation désactivée des éléments et des contraintes doit ressembler à ceci :

<img alt="" src=images/Assembly3_SketchSkeleton-24.png  style="width:500px;"> 
*Assemblage terminé dans la [Vue en arborescence](Tree_view/fr.md) et la [Vue 3D](3D_view/fr.md)*

<img alt="" src=images/Assembly3_SketchSkeleton-27.gif  style="width:500px;"> 
*Animation GIF réalisée à partir d'une séquence d'images de ce [contrôleur cinématique](Tutorial_KinematicController/fr.md)*

## Attachement de la géométrie 3D 

Mes attentes concernant l\'attachement d\'un nouvel objet à un objet de base appartenant à un assemblage cinématique étaient quelque chose comme :

-   Placer le nouvel objet dans le conteneur Parts de l\'objet de base.
-   Positionner le nouvel objet par rapport à l\'objet de base.
-   Fixer le décalage et l\'orientation relatifs à l\'aide de la contrainte Attachment.

Mais cela aurait été trop facile.

L\'outil <img alt="" src=images/Assembly_ConstraintAttachment.svg  style="width:16px;"> [Assembly3 ConstraintAttachment](Assembly3_ConstraintAttachment/fr.md), comme tout outil de contrainte d\'Assembly3, repose sur l\'utilisation d\'objets Element et de leurs systèmes de coordonnées d\'éléments (ECSs) pour les tâches de positionnement.

Ainsi, attacher des objets n\'est qu\'une autre façon d\'ajouter des objets à un (sous-)ensemble.

Attachons la tige 4-3D à la tige 4 par exemple :

Les objets ont une orientation différente et l\'objet 3D doit avoir un décalage par rapport à l\'objet 2D.

1.  Placez le nouvel objet dans le conteneur Parts de l\'objet de base.
2.  Sélectionnez deux cercles ou arcs correspondants.
3.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintAttachment.svg‎‎" width=16px> [Create "Attachment" constraint](Assembly3_ConstraintAttachment/fr.md)**.

:   <img alt="" src=images/Assembly3_SketchSkeleton-28.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-29.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-30.png  style="width:200px;">



*Tige 4 (verrouillée) et Tige 4-3D → Arcs sélectionnés → Tige 4-3D relocalisée (les deux ECSs sont au même endroit avec une orientation identique)*

Il est maintenant évident que l\'outil <img alt="" src=images/Assembly_ConstraintAttachment.svg  style="width:16px;"> [Assembly3 ConstraintAttachment](Assembly3_ConstraintAttachment/fr.md) ignore le décalage et l\'orientation entre les deux objets.

Cependant, la position est déjà définie comme nous le voulions et il nous suffit donc d\'adapter l\'angle manuellement et de définir le décalage souhaité :

-   Définissez la **Offset, Angle** du premier élément du conteneur Attachment pour qu\'il corresponde à l\'orientation.
-   Définissez la **Offset, Position, z** du même élément pour appliquer un décalage.

Si nous définissons les propriétés du deuxième élément, le mouvement de l\'angle et du décalage ira dans la direction opposée.

:   <img alt="" src=images/Assembly3_SketchSkeleton-30.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-31.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-32.png  style="width:200px;">



*Comme attaché → Angle adapté → Décalage défini*

S\'il y a un objet 3D attaché à chaque objet 2D, cela pourrait ressembler à ceci :

<img alt="" src=images/Assembly3_SketchSkeleton-33.gif  style="width:500px;">

## Remarques

La section [Attachement de la géométrie 3D](#Attachement_de_la_g.C3.A9om.C3.A9trie_3D.md) ne fait qu\'effleurer l\'extension d\'un sous-ensemble, et d\'autres contraintes ou combinaisons de contraintes peuvent être plus appropriées que la contrainte d\'attachement.

Il est important de déplacer un tel assemblage cinématique par petits pas, sinon le solveur abandonnera et échouera. Il est presque impossible d\'utiliser <img alt="" src=images/Assembly_Move.svg  style="width:16px;"> [Move part](Assembly3_MovePart/fr.md) ou <img alt="" src=images/Assembly_AxialMove.svg  style="width:16px;"> [Axial move](Assembly3_AxialMove/fr.md) pour cette tâche.

La contrainte <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:16px;"> [Assembly3_ConstraintCoincidence](Assembly3_ConstraintCoincidence/fr.md) est utilisée pour piloter l\'assemblage cinématique, sa propriété **Angle** (activée par la propriété **Lock Angle**) accepte des nombres positifs ou négatifs en virgule flottante supérieurs à 360 et peut donc faire plusieurs tours complets.



---
⏵ [documentation index](../README.md) > Tutorial KinematicSkeleton/fr
