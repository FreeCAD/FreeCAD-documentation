# OpenSCAD RefineShapeFeature/ro
---
- GuiCommand:   Name:OpenSCAD RefineShapeFeature   MenuLocation:OpenSCAD - Refine Shape Feature   Workbenches:[[OpenSCAD Workbench   OpenSCAD]]|SeeAlso:


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Curata liniile inutile. După o operație booleană, unele linii care definesc forma anterioară rămân vizibile, această unealtă creează o copie total curățată a originalului.


</div>

![](images/PartRefineShape_it.png )

## Usage


<div class="mw-translate-fuzzy">

## Utilizare

1.  Selectați forma de curățat.
2.  Click pe meniul **OpenSCAD → Refine shape**.

-   Se creează un obiect copil total curățat și obiectul părinte este ascuns.


</div>

## Limitations


<div class="mw-translate-fuzzy">

## Limitări

-   Algoritmul de rafinare funcționează numai pe cochilii. Prin urmare, acesta iterează peste cochilia formei de intrare și apoi pentru fiecare coajă creează o coajă nouă cu fațete fizionate ori de câte ori este posibil. Aceasta înseamnă că, dacă forma dvs. de intrare este doar o fațetă, un filament/polilinie sârmă, o margine sau un vârf, atunci algoritmul nu face nimic.
-   Spre deosebire de [Part refine shape](Part_RefineShape.md) în Atelierul Part, această funcți(e)onalitae se va "ACTUALIZA" când se schimbă formele precedente.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Notă

-   funcția nu modifică forma existentă, dar returnează o nouă formă
-   funcția este folosită în mod normal ca ultim pas în istoricul de modelare
-   funcția poate ajuta la obținerea racordărilor dificile de lucrat
-   funcția este destinată să împiedice imprimantele 3D să imprime marginile/muchiile nedorite


</div>





{{OpenSCAD_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD RefineShapeFeature/ro
