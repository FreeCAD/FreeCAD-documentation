# <img alt="Icône de l\'atelier Image" src=images/Workbench_Image.svg  style="width:64px;"> Image Workbench/fr


{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_Image.svg  style="width:24px;"> [Atelier Image](Image_Workbench/fr.md) gère différents formats de [bitmap](bitmap/fr.md) et vous permet de les ouvrir dans FreeCAD.

## Outils

-   <img alt="" src=images/Image_Open.svg  style="width:32px;"> [Ouvrir\...](Image_Open/fr.md): ouvrir une image dans une nouvelle fenêtre.
-   <img alt="" src=images/Image_CreateImagePlane.svg  style="width:32px;"> [Créer un plan d\'image](Image_CreateImagePlane/fr.md): importer une image sur un plan dans la vue 3D.
-   <img alt="" src=images/Image_Scaling.svg  style="width:32px;"> [Redimensionner une image](Image_Scaling/fr.md): redimensionner une image importée dans un plan.

## Fonctionnalités

-   Comme une [esquisse](Sketcher_Workbench/fr.md), une image importée peut être attachée à l\'un des plans principaux XY, XZ ou YZ et recevoir un décalage positif ou négatif.
-   L\'image est importée avec une relation de 1 pixel égal 1 millimètre.
-   Nous vous recommandons d\'importer une image dans une résolution raisonnable.

## Processus de travail 

L\'utilisation la plus courante de cet atelier est le traçage sur l\'image, avec les outils de [Draft](Draft_Workbench/fr.md) ou de [Sketcher](Sketcher_Workbench/fr.md), afin de générer un corps solide basé sur les contours de l\'image.

Le traçage sur une image donne de meilleurs résultats si l'image présente un petit décalage négatif, par exemple -0,1 mm par rapport au plan de travail. Cela signifie que l\'image sera légèrement derrière le plan où vous dessinez votre géométrie 2D, de sorte que vous ne dessinez pas sur l\'image elle-même.

Le décalage de l\'image peut être défini lors de l\'importation ou modifié ultérieurement via ses propriétés.





{{Image Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Image Workbench/fr
