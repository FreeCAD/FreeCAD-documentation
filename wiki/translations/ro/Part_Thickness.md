---
- GuiCommand:
   Name:Part Thickness
   MenuLocation:Part → Thickness
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Offset](Part_Offset.md)
---

# Part Thickness/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul **Thickness** funcționează pe forme solide și le trasnformă în obiecte goale tip cochilie, dând fiecărei fațete o grosime definită. Pe unele solide vă permite să accelerați în mod semnificativ lucrarea și evitați extrudările și buzunarele.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Utilizare

1.  Creați un solid
2.  Selectați una sau mai multe fațete
3.  Click pe instrumentul **<img src="images/Part_Thickness.png" width=16px> '''Part Thickness'''
**
4.  Definiți parametrii (vedeți [Options](#Options.md))
5.  Click pe OK pentru a confirma, creați operațiunea și eșiți din funcție
6.  In tabelul Properties ajustați parametri dacă este necesar.


</div>

## Options


<div class="mw-translate-fuzzy">

## Opțiuni

-   Thickness: Grosimea peretelui obiectului rezultat, este setat la valoarea dorită
    -   A positive value will offset the faces outward
    -   A negative value will offset the faces inward
-   Mode
    -   Skin: Select this option if you want to get an item like a vase, headless but with the bottom
    -   Pipe: Select this option if you want to get an object like a pipe, headless and bottomless. In this case it may be convenient to select the faces to be deleted before you start the tool. Helping with predefined views buttons or use the numeric keys.
    -   RectoVerso:
-   Join Type
    -   Arc: removes the outer edges and create a fillet with a radius equal to the thickness defined
    -   Tangent:
    -   Intersection:
-   Intersection:
-   Self-intersection: Enables self-intersection
-   Face / Done: Select the faces to be removed, then click Done
-   Update view: Actualizează automat vizualizarea în timp real


</div>

## Notes


<div class="mw-translate-fuzzy">

## Limitări

Uneori, pe o anumită formă produc rezultate bizare. Salvați munca înainte de a aplica grosimea pe obiecte complexe


</div>

## Links


<div class="mw-translate-fuzzy">

## Legături

Un bun exemplu de cum se utilizează acest instrument găsiți pe forum: [Re: Help designing a simple enclosure](http://forum.freecadweb.org/viewtopic.php?f=3&t=3766&p=29741&hilit=enclosure#p29547)


</div>



## Exemple

**Hollow cylinder**

1.  Create **<img src="images/Part_Cylinder.svg" width=16px> [Cylinder](Part_Cylinder.md)** with radius 10mm and height 20mm
2.  Select the top and bottom surface of the cylinder
3.  Click on the **<img src="images/Part_Thickness.svg" width=16px> Thickness
** button (no need to change default settings) and press **OK**

Notes:

-   For this shape, consider using **<img src="images/Part_Tube.svg" width=16px> [Tube](Part_Tube.md)** instead.
-   Select the cylinder\'s top surface only to create a receptacle.

![](images/ThicknessEsempio1.png )

![](images/ThicknessEsempio2.png )

**Box-Enclosure**

![](images/ThicknessEsempio3.png )

![](images/ThicknessEsempio4.png )



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Thickness/ro
