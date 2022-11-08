---
- GuiCommand   */pl
   Name   *TechDraw 2PointCosmeticLine
   Name/pl   *Dodaj linię kosmetyczną wytyczoną przez dwa punkty
   MenuLocation   *Rysunek Techniczny → Dodaj Linię → Dodaj linię środkową pomiędzy dwoma punktami
   Workbenches   *[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version   *0.19
   SeeAlso   *[Dodaj linię środkową do ściany](TechDraw_FaceCenterLine/pl.md), [Dodaj linię środkową pomiędzy dwoma liniami](TechDraw_2LineCenterLine/pl.md)
---

# TechDraw 2PointCosmeticLine/pl

## Opis


<div class="mw-translate-fuzzy">

Narzędzie **Dodaj linię kosmetyczną wytyczoną przez dwa punkty** dodaje linię kosmetyczną pomiędzy dwoma wierzchołkami *(punktami)*. Wierzchołki mogą być rozmieszczone zarówno w przestrzeni 2D jak i 3D. Wynikowa linia może być użyta do wymiarowania. Obecność linii może być modyfikowana za pomocą narzędzia [Zmień wygląd linii](TechDraw_DecorateLine/pl.md).


</div>

<img alt="" src=images/CosLine2PointsSample.png  style="width   *200px;">



*Linia kosmetyczna pomiędzy dwoma punktami*

## Użycie


<div class="mw-translate-fuzzy">

1.  Wybierz 2 wierzchołki w widoku lub 2 wierzchołki w widoku 3D.
2.  Naciśnij przycisk **<img src="images/TechDraw-line2points.svg" width=16px> Dodaj linię kosmetyczną wytyczoną przez dwa punkty**.
3.  Otworzy się okno dialogowe, w którym możesz ustawić współrzędne 2 punktów.
4.  Zostanie dodana linia łącząca 2 wybrane wierzchołki. W przypadku punktów 3d, linia połączy rzuty wybranych punktów.


</div>

## Edycja linii kosmetycznej 


<div class="mw-translate-fuzzy">

Aby zmienić punkty końcowe linii kosmetycznej, użyj narzędzia **<img src="images/TechDraw-line2points.svg" width=16px> Dodaj linię kosmetyczną wytyczoną przez dwa punkty
**


</div>

1.  Wybierz linię kosmetyczną.
2.  Naciśnij przycisk **<img src="images/TechDraw-line2points.svg" width=16px> Dodaj linię kosmetyczną wytyczoną przez dwa punkty**.
3.  Otworzy się okno dialogowe, w którym możesz zmienić współrzędne punktów końcowych.
4.  Naciśnij przycisk **OK**, aby zobaczyć swoje zmiany.


<div class="mw-translate-fuzzy">

Aby usunąć linię kosmetyczną należy wybrać linię do usunięcia i użyć przycisku z paska narzędzi **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Usuń obiekt kosmetyczny](TechDraw_CosmeticEraser/pl.md)**.


</div>


<div class="mw-translate-fuzzy">

Aby pozbyć się linii kosmetycznej, użyj narzędzia [Usuń obiekt kosmetyczny](TechDraw_CosmeticEraser/pl.md).


</div>

## Właściwości

Linie kosmetyczne nie mają własnych właściwości, ponieważ nie są obiektami dokumentu.

## Tworzenie skryptów 


**Zobacz również   ***

[TechDraw API](TechDraw_API.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Linie kosmetyczne można tworzyć za pomocą metod makeCosmeticLine(v1, v2) lub makeCosmeticLine3d(v1, v2) w DrawViewPart.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCosmeticLine/pl
