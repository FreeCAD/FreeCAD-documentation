---
- GuiCommand:/fr
   Name:Part Ellipsoid
   Name/fr:Part Ellipsoide
   MenuLocation:Pièce → [Créer des primitives...](Part_Primitives/fr.md) → Ellipsoïde
   Workbenches:[Part](Part_Workbench/fr.md), [OpenSCAD](OpenSCAD_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---

## Description

La commande <img alt="" src=images/Part_Ellipsoid.svg  style="width:24px;"> [Part Ellipsoïde](Part_Ellipsoid/fr.md) crée un solide ellipsoïde paramétrique.

La forme produite est solide un sphéroïde (éventuellement tronquée) est limitée dans FreeCAD, la forme est créée par rotation d\'une ellipse autour de son axe. Par défaut, il s\'agit d\'un [Oblate Spheroid](http://en.wikipedia.org/wiki/Oblate_spheroid), la forme est créée, par la rotation d\'une ellipse autour de son petit axe. Les paramètres peuvent être modifiés pour former un [Prolate Spheroid](http://en.wikipedia.org/wiki/Prolate_spheroid).

Le sphéroïde par défaut dans FreeCAD aura un cercle pour toute section transversale parallèle au plan XY. La section transversale parallèle aux deux autres plans sera une ellipse.

En mathématique, un [Ellipsoïde](https://fr.wikipedia.org/wiki/Ellipso%C3%AFde) aurait une section transversale elliptique dans les trois plans.

## Utilisation

Un solide ellipsoïde paramétrique est disponible à partir de la boîte de dialogue Créer des primitives dans l\'atelier Part.

1.  Basculez vers l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md)
2.  Accédez à la commande Ellipsoïde de plusieurs manières:
    -   Dans la boîte de dialogue Créer des primitives, en appuyant sur le bouton <img alt="" src=images/Part_CreatePrimitives.svg  style="width:32px;"> [Création de primitives géométriques\...](Part_Primitives/fr.md) situé dans la barre d\'outils Part.
    -   Using the {{MenuCommand|Pièce → [Créer des primitives...](Part_Primitives/fr.md) → Ellipsoïde}} dans le menu Pièce.

## Propriétés

-   Radius 1, Par défaut le petit rayon est parallèle à l\'axe Z,
-   Radius 2, Par défaut le grand rayon est parallèle au plan XY, il est également le grand rayon au croisement de la section circulaire
-   Angle 1, la troncature inférieure de l\'ellipsoïde, est parallèle à la section transversale circulaire (-90 degrés dans un sphéroïde complet)
-   Angle 2, la troncature supérieure de l\'ellipsoïde, est parallèle à la section transversale circulaire (90 degrés dans un sphéroïde complet)
-   Angle 3, est l\'angle de rotation de la section transversale elliptique (360 degrés dans un ellipsoïde complet)

![](images/Part_Ellipsoid_screenshot.jpg )





 
