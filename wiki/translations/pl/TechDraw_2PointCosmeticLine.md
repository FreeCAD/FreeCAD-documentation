---
- GuiCommand:
   Name: TechDraw 2PointCosmeticLine
   Name/pl: Dodaj linię kosmetyczną wytyczoną przez dwa punkty
   MenuLocation: Rysunek Techniczny -> Dodaj Linię -> Dodaj linię środkową pomiędzy dwoma punktami
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_FaceCenterLine/pl, TechDraw_2LineCenterLine/pl
---

# TechDraw 2PointCosmeticLine/pl


</div>



## Opis


<div class="mw-translate-fuzzy">

Narzędzie **Dodaj linię kosmetyczną wytyczoną przez dwa punkty** dodaje linię kosmetyczną pomiędzy dwoma wierzchołkami *(punktami)*. Wierzchołki mogą być rozmieszczone zarówno w przestrzeni 2D jak i 3D. Wynikowa linia może być użyta do wymiarowania. Obecność linii może być modyfikowana za pomocą narzędzia [Zmień wygląd linii](TechDraw_DecorateLine/pl.md).


</div>

<img alt="" src=images/CosLine2PointsSample.png  style="width:200px;">


<div class="mw-translate-fuzzy">



*Linia kosmetyczna pomiędzy dwoma punktami*


</div>




<div class="mw-translate-fuzzy">

## Użycie


</div>


<div class="mw-translate-fuzzy">

1.  Wybierz 2 wierzchołki w widoku lub 2 wierzchołki w widoku 3D.
2.  Naciśnij przycisk **<img src="images/TechDraw-line2points.svg" width=16px> Dodaj linię kosmetyczną wytyczoną przez dwa punkty**.
3.  Otworzy się okno dialogowe, w którym możesz ustawić współrzędne 2 punktów.
4.  Zostanie dodana linia łącząca 2 wybrane wierzchołki. W przypadku punktów 3d, linia połączy rzuty wybranych punktów.


</div>




<div class="mw-translate-fuzzy">

## Edycja linii kosmetycznej 


</div>

Aby zmienić punkty końcowe linii kosmetycznej:


<div class="mw-translate-fuzzy">

1.  Wybierz linię kosmetyczną.
2.  Naciśnij przycisk **<img src="images/TechDraw-line2points.svg" width=16px> Dodaj linię kosmetyczną wytyczoną przez dwa punkty**.
3.  Otworzy się okno dialogowe, w którym możesz zmienić współrzędne punktów końcowych.
4.  Naciśnij przycisk **OK**, aby zobaczyć swoje zmiany.


</div>

## Notes

-   To delete a cosmetic line use <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw CosmeticEraser](TechDraw_CosmeticEraser.md).
-   To change the appearance of a cosmetic line use <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [TechDraw DecorateLine](TechDraw_DecorateLine.md).



## Właściwości

Linie kosmetyczne nie mają własnych właściwości, ponieważ nie są obiektami dokumentu.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).


<div class="mw-translate-fuzzy">

Linie kosmetyczne można tworzyć za pomocą metod makeCosmeticLine(v1, v2) lub makeCosmeticLine3d(v1, v2) w DrawViewPart.


</div>





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCosmeticLine/pl
