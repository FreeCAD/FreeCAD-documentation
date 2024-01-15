---
 GuiCommand:
   Name: TechDraw LeaderLine
   Name/pl: Rysunek Techniczny: Dodaj linię odniesienia do widoku
   MenuLocation: Rysunek Techniczny , Dodaj linie , Dodaj linię odniesienia do widoku
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_RichTextAnnotation/pl, TechDraw_WeldSymbol/pl
---

# TechDraw LeaderLine/pl



## Opis

Narzędzie **Dodaj linię odniesienia do widoku** dodaje linię do widoku. Inne obiekty adnotacji *(takie jak [Wstaw adnotację w postaci tekstu sformatowanego](TechDraw_RichTextAnnotation/pl.md))* mogą być połączone z linią prowadzącą w celu utworzenia złożonych adnotacji.

![](images/TechDraw_LeaderLine_sample.png ) 
*Linia pomocnicza dodana do Widoku.*



## Użycie

1.  Wybierz widok.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_LeaderLine.svg" width=16px> Dodaj linię odniesienia do widoku**.

Otworzy się okno dialogowe umożliwiające narysowanie linii pomocniczej i przypisanie do niej symboli końcowych.

-   Wybierz opcję z menu **Rysunek Techniczny → Dodaj linie → <img src="images/TechDraw_LeaderLine.svg" width=16px>. Dodaj linię prowadzącą do widoku**.

1.  Otworzy się panel zadań.
2.  Naciśnij przycisk **Wybierz punkty**.
3.  Wybierz pierwszy punkt na stronie, aby zdefiniować punkt początkowy linii.
4.  Wybierz następny punkt na stronie. Przytrzymaj **Ctrl**, aby przyciągnąć do wielokrotności kąta 22,5°. Opcjonalnie użyj podwójnego kliknięcia zamiast pojedynczego, aby zakończyć wprowadzanie punktów.
5.  Opcjonalnie dodaj więcej punktów.
6.  Jeśli punkt nie został kliknięty dwukrotnie: naciśnij przycisk **Zapisz punkty**.
7.  Opcjonalnie zmień **Symbol początku**, **Symbol końca**, **Kolor**, **Szerokość** i **Styl** linii odniesienia. Więcej informacji można znaleźć w sekcji [Właściwości](#Właściwości.md).
8.  Naciśnij przycisk **OK**.



## Edycja

1.  Kliknij dwukrotnie linię prowadzącą w oknie [Widoku drzewa](Tree_view.md).
2.  Otworzy się panel zadań.
3.  Aby edytować punkty:
4.  Naciśnij przycisk **Edytuj punkty**.
    1.  Linia prowadząca jest oznaczona tymczasowymi węzłami.
    2.  Przeciągnij jeden lub więcej węzłów do nowej pozycji.
    3.  Naciśnij przycisk **Zapisz zmiany**.
5.  Opcjonalnie zmień **Symbol początku**, **Symbol końca**, **Kolor**, **Szerokość** i **Styl** linii odniesienia. Więcej informacji można znaleźć w sekcji [Właściwości](#Właściwości.md).
6.  Naciśnij przycisk **OK**.



## Uwagi

-   Nie można dodawać ani usuwać punktów z istniejącej linii odniesienia.
-   Jeśli podczas tworzenia nie określono żadnych punktów, na środku widoku umieszczana jest krótka linia. Nie ma sposobu na naprawienie takiej linii, należy ją usunąć.
-   Domyślnie zaznaczona jest [opcja](TechDraw_Preferences/pl#Adnotacje.md) **Linia odniesienia automatycznie poziomo**. Oznacza to, że ostatni segment nowej linii odniesienia jest rysowany poziomo. Jeśli jest tylko jeden segment, wynikiem jest pojedyncza pozioma linia.
-   Można wyłączyć tę funkcję automatycznego poziomego rysowania dla istniejących linii prowadzących, zmieniając ich właściwość **Auto Poziom**.



## Właściwości



### Dane


{{Properties_Title|Podstawowe}}

-    **Symbol początku|Enumeration**: Symbol na początku linii prowadzącej. Opcje: <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Otwarta strzałka, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Grot, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Kropka, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Otwarte koło, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Widełki, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Wypełniony trójkąt, Brak.

-    **Symbol końca|Enumeration**: Symbol na końcu linii prowadzącej. Idem.

-    **X|Odległość**: Współrzędna X linii prowadzącej względem widoku.

-    **Y|Odległość**: Współrzędna Y linii prowadzącej względem widoku.


{{Properties_Title|Linia odniesienia}}

-    **Leader Parent|Link**: Widok, do którego dołączona jest linia prowadząca.

-    **Punkty trasy|VectorList**: Punkty linii prowadzącej.

-    **Skalowalny|Bool**: Określa, czy linia odniesienia skaluje się wraz z **Leader Parent**.

-    **Auto poziom|Bool**: Określa, czy ostatni segment linii prowadzącej ma być ustawiony poziomo.



### Widok


{{TitleProperty|Podstawa}}

-    **Zachowaj etykietę|Bool**: Nieużywane.

-    **Kolejność na stosie|Integer**: Nakładanie się lub niedopasowanie względem innych obiektów rysunku. {{Version/pl|0.21}}


{{TitleProperty|Format linii}}

-    **Kolor|Color**: Kolor linii prowadzącej.

-    **Style linii|Enumeration**: Styl linii prowadzącej. Opcje: Brak, <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Ciągła, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Kreska, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Kropka, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> Kreska kropka, <img alt="Length" src=images/DashDotDot-line.svg  style="width:20px;"> Kreska kropka kropka.

-    **Szerokość linii|Length**: Szerokość linii prowadzącej.



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
