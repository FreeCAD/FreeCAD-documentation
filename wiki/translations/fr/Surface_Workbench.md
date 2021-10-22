# <img alt="Icône de l\'atelier Surface" src=images/Workbench_Surface.svg  style="width:64px;"> Surface Workbench/fr


{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_Surface.svg  style="width:24px;"> <img src=images/Part_Builder.svg style="width:atelier Surface](Surface_Workbench/fr.md) fournit des outils pour créer et modifier de simples surfaces _** lorsque l\'option **Face from edges** est utilisée. Cependant, contrairement à cet outil, les outils de l\'atelier Surface sont paramétriques et offrent des options supplémentaires. À cet égard, les outils de cet atelier sont similaires à des fonctionnalités telles que **[16px"> <img src=images/PartDesign_AdditivePipe.svg style="width:PartDesign Lissage additif](PartDesign_AdditiveLoft/fr.md)** et **[16px"> [PartDesign Balayage additif](PartDesign_AdditivePipe/fr.md)**.

Les fonctionnalités fournies sont :

-   Création de surfaces à partir d\'arêtes.
-   Alignement de la courbure des faces voisines.
-   Contrainte des surfaces sur des courbes et des sommets supplémentaires.
-   Extension de faces.
-   Un maillage peut être utilisé comme modèle pour créer des courbes splines sur sa surface.

<img alt="" src=images/Surface_example.png  style="width:350px;">

## Utilisation

L\'objectif de l\'atelier Surface est de créer des faces avec des formes qui ne sont pas disponibles avec les outils standard des autres ateliers.

<img alt="" src=images/Toy_Duck.png  style="width:350px;">



*Surface créée avec des esquisses placées dans des plans de référence avec les outils de l'[atelier PartDesign](PartDesign_Workbench/fr.md)*

L\'atelier Surface s\'intègre à d\'autres ateliers de FreeCAD. L\'exemple ci-dessus a été créé à partir d\'**<img src=images/Sketcher_NewSketch.svg style="width:16px"> <img src=images/PartDesign_Plane.svg style="width:esquisses](Sketch/fr.md)** placé sur des **_. La conception peut être entièrement paramétrique si tous les plans et esquisses de référence sont définis en conséquence. Dans la plupart des cas, il suffit de dessiner une esquisse fermée pour définir la limite d\'une face, puis d\'utiliser différentes options pour modifier davantage sa forme.

La surface générée ne peut pas être placée dans un **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/Std_Part.svg style="width:PartDesign Corps](PartDesign_Body/fr.md)**. Cependant, la surface générée peut être contenue dans un **_** associé qui contient les plans de référence et les esquisses. L\'outil non paramétrique **[16px"> [Part Générateur de formes](Part_Builder/fr.md)** peut ensuite être utilisé pour créer une [coque](Glossary/fr#Shell.md) et enfin un [solide](Glossary/fr#Solid.md).

## Outils

-   <img alt="" src=images/Surface_Filling.svg  style="width:32px;"> [Remplissage](Surface_Filling/fr.md) : remplit une série de courbes limites avec une surface.

-   <img alt="" src=images/Surface_GeomFillSurface.svg  style="width:32px;"> [Remplir entre les courbes limites](Surface_GeomFillSurface/fr.md) : crée une surface à partir de deux, trois ou quatre arêtes limites.

-   <img alt="" src=images/Surface_Sections.svg  style="width:32px;"> [Sections](Surface_Sections/fr.md) : crée une surface à partir d\'arêtes qui représentent des sections transversales de surface. {{Version/fr|0.19}}

-   <img alt="" src=images/Surface_ExtendFace.svg  style="width:32px;"> [Extension de surface](Surface_ExtendFace/fr.md) : extrapole la surface aux limites avec ses paramètres U et V locaux.

-   <img alt="" src=images/Surface_CurveOnMesh.svg  style="width:32px;"> _ sélectionné.





{{Surface Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Surface Workbench/fr
