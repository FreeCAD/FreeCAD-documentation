---
- TutorialInfo:/fr
   Topic:TechDraw
   Level:Débutant
   Time:10 minutes
   Author:Andergrin
   FCVersion:0.19
---

# TechDraw Pitch Circle Tutorial/fr





## Introduction

Ce tutoriel explique comment ajouter un cercle imaginaire à une vue <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/fr.md). Il suppose que le modèle est un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Corps](PartDesign_Body/fr.md) avec au moins trois trous dans un motif circulaire. Pour le cercle, une esquisse distincte sera créée. Une procédure similaire peut être utilisée dans d\'autres situations et pour ajouter d\'autres éléments de type annotation aux vues [TechDraw](TechDraw_Workbench/fr.md).

<img alt="" src=images/Circle.png  style="width:250px;"> <img alt="" src=images/Pitch_Circle.png  style="width:300px;">

## Créer l\'esquisse du cercle 

1.  Activez le <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Corps](PartDesign_Body/fr.md).
2.  Si nécessaire : basculez vers l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md).
3.  Dans la [vue 3D](3D_view.md), sélectionnez la bonne face appartenant au corps.
4.  Créez une nouvelle esquisse avec l\'icône <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [PartDesign Nouvelle esquisse](PartDesign_NewSketch/fr.md).
5.  L\'esquisse sera attachée à la face sélectionnée.
6.  Lancez la commande <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [Sketcher Géométrie externe](Sketcher_External/fr.md).
7.  Sélectionnez trois arêtes circulaires (trous) dans le corps.
8.  Utilisez la commande <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:24px;"> [Sketcher Géométrie externe](Sketcher_External/fr.md). Utilisez la commande [Sketcher Création d\'un cercle par 3 points](Sketcher_Create3PointCircle/fr.md) pour créer un cercle contraint aux points centraux de la géométrie externe.
9.  L\'esquisse doit maintenant être entièrement contrainte.
10. Fermez l\'esquisse.

## Créer la vue TechDraw 

1.  Passez à l\' <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [atelier TechDraw](TechDraw_Workbench/fr.md).
2.  Si vous n\'en avez pas déjà un : créez une <img alt="" src=images/TechDraw_PageDefault.svg  style="width:24px;"> [TechDraw page](TechDraw_PageDefault/fr.md).
3.  Assurez-vous que la [vue 3D](3D_view/fr.md) est correctement alignée.
4.  Maintenez la touche **Ctrl** enfoncée et dans la [Vue par arborescence](Tree_view/fr.md), sélectionnez le corps et l\'esquisse qui vient d\'être créée.
5.  Insérez une nouvelle vue en appelant la fonction <img alt="" src=images/TechDraw_View.svg  style="width:24px;"> [TechDraw Vue](TechDraw_View/fr.md).
6.  Passez à la page [TechDraw](TechDraw_Workbench/fr.md).
7.  Sélectionnez le cercle.
8.  Lancez la commande <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:24px;"> [TechDraw Apparence des lignes](TechDraw_DecorateLine/fr.md).
9.  Modifiez les **Style** et **Weight** du cercle.


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Pitch Circle Tutorial/fr
