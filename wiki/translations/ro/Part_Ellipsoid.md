# Part Ellipsoid/ro
---
- GuiCommand:   Name:Part Ellipsoid   MenuLocation:Part → [Workbenches:[[Part Workbench   Part](Part_CreatePrimitives___Create_Primitives]]_→_Ellipsoid.md),  [OpenSCAD](OpenSCAD_Workbench.md)|SeeAlso:..---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Un solid parametric este Elipsoidul care este disponibil din dialogul Create Primitives în Atelierul de lucru Part.


</div>

The <img alt="" src=images/Part_Ellipsoid.svg  style="width:24px;"> [Part Ellipsoid](Part_Ellipsoid.md) command creates a parametric Ellipsoid solid.


<div class="mw-translate-fuzzy">

Forma produsă este limitată în FreeCAD ca fiind un sferoid solid (opțional trunchiat), forma pe care ați crea-o prin rotirea unei elipse în jurul axei sale. Implicit este a [oblate\_spheroid](http://en.wikipedia.org/wiki/Oblate_spheroid), forma pe care ați crea-o prin rotirea unei elipse în jurul axei sale minore. Parametrii pot fi modificați pentru a forma a[prolate\_spheroid](http://en.wikipedia.org/wiki/Prolate_spheroid).


</div>


<div class="mw-translate-fuzzy">

Sferoidul implicit din FreeCAD va avea un cerc pentru orice secțiune transversală paralelă cu planul xy. Secțiunea transversală paralelă cu celelalte două planuri va fi o elipsă.


</div>

În mathematică, un [Ellipsoid](http://en.wikipedia.org/wiki/Ellipsoid) ar avea o secțiune eliptică în toate cele trei planuri.

## Usage

A parametric Ellipsoid solid is available from the Create Primitives dialogue in the Part workbench.

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md)
2.  Access the Ellipsoid command several ways:
    -   Through the Create Primitives dialogue, pressing the <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Primitives](Part_Primitives.md) button located in the Part toolbar
    -   Using the **Part → [Create primitives](Part_Primitives.md) → Ellipsoid** entry in the Part menu

## Proprietăți

-   Radius 1, implicit semiaxa minoră paralelă la axa Z,
-   Radius 2, implicită semiaxa majoră paralelă la planul XY,

este, de asemenea, raza maximă a secțiunii circulare

-   Angle 1, trunchierea inferioară a elipsoidului, paralelă cu secțiunea transversală circulară (-90 grade într-un sferic complet)
-   Angle 2, trunchierea superioară a elipsoidului, paralelă cu secțiunea transversală circulară (90 de grade într-un sferic complet)
-   Angle 3, unghiul de rotație a secțiunii transversale eliptice (360 degrees in a full spheroid)

![](images/Part_Ellipsoid_screenshot.jpg )



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Ellipsoid/ro
