---
 GuiCommand:
   Name: TechDraw 2PointCosmeticLine
   Name/pl: Dodaj linię kosmetyczną wytyczoną przez dwa punkty
   MenuLocation: Rysunek Techniczny , Dodaj Linię , Dodaj linię środkową pomiędzy dwoma punktami
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_FaceCenterLine/pl, TechDraw_2LineCenterLine/pl, TechDraw_2PointCenterLine/pl
---

# TechDraw 2PointCosmeticLine/pl



## Opis

Narzędzie **Dodaj linię kosmetyczną wytyczoną przez dwa punkty** dodaje linię kosmetyczną pomiędzy dwoma punktami. Punkty mogą być rozmieszczone zarówno w przestrzeni 2D jak i 3D. Wynikowa linia może być użyta do wymiarowania.

<img alt="" src=images/CosLine2PointsSample.png  style="width:200px;">



*Linia kosmetyczna pomiędzy dwoma punktami*



## Użycie

1.  Wybierz 2 wierzchołki w widoku lub 2 wierzchołki w oknie [widoku 3D](3D_view/pl.md).
2.  Jeśli zaznaczyłeś punkty w oknie widoku 3D: dodaj właściwy widok Rysunku Technicznego do zaznaczenia, wybierając go w oknie [Widoku drzewa](Tree_view/pl.md).
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw-line2points.svg" width=16px> Dodaj linię kosmetyczną wytyczoną przez dwa punkty**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Dodaj linie → <img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> Dodaj linię kosmetyczną wytyczoną przez dwa punkty**.
4.  Otworzy się panel zadań.
5.  Opcjonalnie dostosuj współrzędne punktów.
6.  Naciśnij przycisk **OK**.
7.  Zostanie dodana geometria pomocnicza w postaci linii łączącej dwa punkty. W przypadku punktów 3D linia łączy rzuty punktów.



## Edycja

Aby zmienić punkty końcowe linii kosmetycznej:

1.  Wybierz linię kosmetyczną.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw-line2points.svg" width=16px> Dodaj linię kosmetyczną wytyczoną przez dwa punkty**.
    -   Wybierz opcję **Rysunek Techniczny → Dodaj linie → <img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> Dodaj linię kosmetyczną wytyczoną przez dwa punkty**.
3.  Otworzy się panel zadań.
4.  Dostosuj współrzędne punktów.
5.  Naciśnij przycisk **OK**.



## Uwagi

Aby usunąć linię kosmetyczną użyj narzędzia <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [Usuń geometrie pomocnicze](TechDraw_CosmeticEraser/pl.md).

-   Aby zmienić wygląd linii kosmetycznej użyj narzędzia <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [Zmień wygląd linii](TechDraw_DecorateLine/pl.md).



## Właściwości

Linie kosmetyczne nie mają własnych właściwości, ponieważ nie są obiektami dokumentu.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Linie kosmetyczne można tworzyć za pomocą metod {{Incode|makeCosmeticLine(v1, v2)}} lub {{Incode|makeCosmeticLine3d(v1, v2)}} w DrawViewPart.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCosmeticLine/pl
