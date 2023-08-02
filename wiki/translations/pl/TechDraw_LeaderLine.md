---
- GuiCommand:
   Name: TechDraw LeaderLine
   Name/pl: Rysunek Techniczny: Dodaj linię odniesienia do widoku
   MenuLocation: Rysunek Techniczny -> Dodaj linie -> Dodaj linię odniesienia do widoku
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_RichTextAnnotation/pl, TechDraw_WeldSymbol/pl, TechDraw_LineGroup/pl
---

# TechDraw LeaderLine/pl


</div>



## Opis

Narzędzie **Dodaj linię odniesienia do widoku** dodaje linię do widoku. Inne obiekty adnotacji *(takie jak [Wstaw adnotację w postaci tekstu sformatowanego](TechDraw_RichTextAnnotation/pl.md))* mogą być połączone z linią prowadzącą w celu utworzenia złożonych adnotacji.

![](images/TechDraw_LeaderLine_sample.png )


<div class="mw-translate-fuzzy">



*Linia pomocnicza dodana do View001.*


</div>




<div class="mw-translate-fuzzy">

## Użycie


</div>


<div class="mw-translate-fuzzy">

1.  Wybierz widok.
2.  Naciśnij przycisk **<img src="images/TechDraw_LeaderLine.svg" width=16px> Dodaj linię odniesienia do widoku**. Otworzy się okno dialogowe umożliwiające narysowanie linii pomocniczej i przypisanie do niej symboli końcowych.
3.  Kliknij **Wybierz punkty**, a następnie kliknij na stronie, aby zdefiniować punkt początkowy linii.
4.  Przesuń kursor myszki i kliknij inny punkt, aby utworzyć linię. Przytrzymaj klawisz **Ctrl**, aby przyciągnąć do wielokrotności kąta 22,5°.
5.  Teraz możesz
    1.  zakończyć rysowanie linii poprzez dwukrotne kliknięcie lub naciśnięcie przycisku **Zapisz punkty**.
    2.  dodać kolejne punkty, aby zdefiniować więcej segmentów linii.
6.  Aby zakończyć tworzenie, naciśnij **OK**, aby zamknąć okno dialogowe.


</div>

## Usage edit 


<div class="mw-translate-fuzzy">

1.  Wybierz linię odniesienia w oknie drzewa dokumentu i kliknij ją dwukrotnie.
2.  Otworzy się okno dialogowe, w którym można zmienić wygląd.
3.  Aby edytować punkty, kliknij **Edytuj punkty**, a punkty linii staną się widoczne na rysunku.
4.  Przeciągnij punkty w wybrane miejsce i zakończ zmianę klikając na **Zapisz zmiany**.


</div>



## Uwagi


<div class="mw-translate-fuzzy">

-   Linię odniesienia można edytować, klikając ją dwukrotnie w oknie widoku Drzewa. Dwukrotne kliknięcie w obszarze graficznym nie jest jeszcze obsługiwane. Segmenty linii można edytować, naciskając **Edytuj punkty**. Aby zakończyć edycję punktów, naciśnij **Zapisz zmiany** lub **Odrzuć zmiany**.
-   Jeśli podczas tworzenia linii odniesienia nie zdefiniowano żadnych punktów, na środku widoku zostanie umieszczona krótka linia. Później nie będzie można dodawać kolejnych punktów.
-   Domyślnie włączona jest opcja [Ustawienia](TechDraw_Preferences/pl.md) **Linia odniesienia automatycznie poziomo**. Dlatego ostatni segment linii będzie poziomy. Więc jeśli masz tylko jeden segment, otrzymasz poziomą linię, bez względu na to, gdzie wybrałeś drugi punkt.
-   Można wyłączyć funkcję automatycznego poziomowania dla istniejących linii prowadzących, zmieniając właściwość **Auto Poziom**.


</div>



## Właściwości

### Data


{{Properties_Title|Base}}

-    **Start Symbol|Enumeration**: The symbol at the start of the leaderline. Options: <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Filled Arrow, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Open Arrow, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Tick, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Dot, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Open Circle, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Fork, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Filled Triangle, None.

-    **End Symbol|Enumeration**: The symbol at the end of the leaderline. Idem.

-    **X|Distance**: The X coordinate of the leaderline relative to the View.

-    **Y|Distance**: The Y coordinate of the leaderline relative to the View.


{{Properties_Title|Leader}}

-    **Leader Parent|Link**: The View the leaderline is attached to.

-    **Way Points|VectorList**: The points of the leaderline.

-    **Scalable|Bool**: Specifies if the leaderline scales with **Leader Parent**.

-    **Auto Horizontal|Bool**: Specifies if the last leaderline segment is forced to be horizontal.

### View


{{TitleProperty|Base}}

-    **Keep Label|Bool**: Not used.

-    **Stack Order|Integer**: Over or underlap relative to other drawing objects. <small>(v0.21)</small> 


{{TitleProperty|Line Format}}

-    **Color|Color**: The color of the leaderline.

-    **Line Style|Enumeration**: The style of the leaderline. Options: NoLine, <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continuous, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Dash, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Dot, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> DashDot, <img alt="Length" src=images/DashDotDot-line.svg  style="width:20px;"> DashDotDot.

-    **Line Width|Length**: The width of the leaderline.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Dodaj linię odniesienia do widoku** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
myPage = FreeCAD.ActiveDocument().Page
myBase = FreeCAD.ActiveDocument().View
leaderObj = FreeCAD.ActiveDocument.addObject('TechDraw::DrawLeaderLine','DrawLeaderLine')
FreeCAD.activeDocument().myPage.addView(leaderObj)
FreeCAD.activeDocument().leaderObj.LeaderParent = myBase
#first waypoint is always (0,0,0)  
#rest of waypoints are positions relative to (0,0,0)
leaderObj.WayPoints = [p0,p1,p2]
leaderObj.X = 5
leaderObj.Y = 5
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LeaderLine/pl
