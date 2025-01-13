---
 GuiCommand:
   Name: Draft BSpline
   Name/pl: Draft: Krzywa złożona
   MenuLocation: Kreślenie , Krzywa złożona<br>Kreślenie 2D , Krzywa złożona
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Shortcut: **B** **S**
   SeeAlso: Draft_Wire/pl, Draft_CubicBezCurve/pl, Draft_BezCurve/pl
   Version: 0.7
---

# Draft BSpline/pl



## Opis

Polecenie <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> **Krzywa złożona** tworzy krzywą [B-spline](http://en.wikipedia.org/wiki/B-spline) na podstawie kilku punktów.

Polecenie Krzywa złożona określa punkty **exact points**, przez które będzie przechodzić krzywa. Polecenia [Krzywa złożona](Draft_BezCurve/pl.md) i [Sześcienna krzywa Beziera](Draft_CubicBezCurve/pl.md) używają z kolei **punktów kontrolnych** do określenia położenia i krzywizny odcinka krzywej.

<img alt="" src=images/Draft_bspline_example.jpg  style="width:400px;"> 
*Odcinek krzywej zdefiniowany przez wiele punktów.*



## Użycie

Zapoznaj się również z informacjami na stronie: [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_BSpline.svg" width=16px> '''Krzywa złożona'''**.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz opcję **Kreślenie → <img src="images/Draft_BSpline.svg" width=16px> Krzywa złożona** z menu.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Kreślenie 2D → <img src="images/Draft_BSpline.svg" width=16px> Krzywa złożona** z menu.
    -   Użyj skrótu klawiaturowego: **B**, a następnie **S**.
2.  Otworzy się panel zadań **Krzywa złożona**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
3.  Wybierz pierwszy punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt
**
4.  Wybierz dodatkowe punkty w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
5.  Naciśnij **Esc** lub przycisk **Zamknij**, aby zakończyć polecenie.



## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi *(w wersji 1.0)*.

-   Aby ręcznie wprowadzić współrzędne, wprowadź element X, Y i Z i naciśnij **Enter** po każdym z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy uzyskasz żądane wartości. Zaleca się przesunięcie wskaźnika poza obszar okna [widoku 3D](3D_view/pl.md) przed wprowadzeniem współrzędnych.
-   Wciśnij **R** lub kliknij pole wyboru **Relatywnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne są względne do ostatniego punktu, jeśli jest dostępny, w przeciwnym razie są one względne do początku układu współrzędnych.
-   Naciśnij **G** lub kliknij pole wyboru **Globalne**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne są odniesione do globalnego układu współrzędnych, w przeciwnym razie odnoszą się do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md).
-   Naciśnij **F** lub kliknij pole wyboru **Wypełnij**, aby przełączyć tryb wypełnienia. Jeśli tryb wypełnienia jest włączony, utworzony splajn będzie miał właściwość **Utwórz ścianę** ustawione na wartość {{TRUE/pl}} i będzie miał wypełnioną ścianę, pod warunkiem, że jest zamknięty i nie następuje samo-przecinanie. Należy pamiętać, że przecinający się splajn ze ścianą nie będzie wyświetlany poprawnie, dla takiego splajnu właściwość **Make Face** musi być ustawione na wartość {{FALSE/pl}}.
-   Naciśnij **N** lub kliknij pole wyboru **Kontynuuj**, aby włączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie uruchomi się ponownie po użyciu przycisku **<img src="images/Draft_FinishLine.svg" width=16px> Zakończ** lub **<img src="images/Draft_CloseLine.svg" width=16px> Zamknij**, lub po utworzeniu zamkniętego splajnu poprzez przyciągnięcie do pierwszego punktu splajnu, umożliwiając dalsze tworzenie splajnów.
-   Naciśnij **/** lub przycisk **<img src="images/Draft_UndoLine.svg" width=16px> Cofnij**, aby cofnąć ostatni punkt.
-   Naciśnij **A** lub przycisk **<img src="images/Draft_FinishLine.svg" width=16px> Zakończ**, aby zakończyć polecenie i pozostawić otwartą krzywą.
-   Naciśnij **O** lub przycisk **<img src="images/Draft_CloseLine.svg" width=16px> Zamknij**, aby zakończyć polecenie i zamknąć linię krzywą. Zamkniętą krzywą można również utworzyć poprzez przyciągnięcie do pierwszego punktu splajnu.
-   Naciśnij **W** lub przycisk **<img src="images/Draft_Wipe.svg" width=16px> Wyczyść**, aby usunąć już umieszczone segmenty krzywej, ale kontynuować pracę od ostatniego punktu.
-   Naciśnij **U** lub przycisk **<img src="images/Draft_SelectPlane.svg" width=16px> [ustaw płaszczyzne roboczą](Draft_SelectPlane/pl.md)**, aby ustawić bieżącą płaszczyznę roboczą w orientacji określonej przez ostatni i poprzedni punkt.
-   Naciśnij **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap.md).
-   Naciśnij **Esc** lub przycisk **Zamknij**, aby zakończyć polecenie.



## Uwagi

-   Krzywa złożona środowiska Rysunek Roboczy może być edytowana za pomocą polecenia [Edytuj](Draft_Edit.md).
-   Krzywa złożona środowiska Rysunek Roboczy może zostać przekonwertowany na [polilinię](Draft_Wire/pl.md) za pomocą narzędzia [Polilinia na krzywą złożoną](Draft_WireToBSpline/pl.md).



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Krzywa złożona środowiska Rysunek Roboczy wywodzi się z obiektu [Część: Part2DObject](Part_Part2DObject/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Rysunek Roboczy}}

-    **Obszar|Area**: *(tylko do odczytu)* określa obszar powierzchni krzywej. Wartość będzie wynosiła {{value|0.0}} jeśli właściwość **Utwórz ścianę** ma wartość {{FALSE/pl}} lub ściana nie może zostać utworzona.

-    **Zamknięty|Bool**: określa czy krzywa jest zamknięta czy nie. Jeśli odcinek jest początkowo otwarty, wartość ta wynosi {{FALSE/pl}}, ustawienie jej na {{TRUE/pl}} spowoduje narysowanie segmentu krzywej w celu zamknięcia krzywej. Jeśli krzywa jest początkowo zamknięta, ta wartość to {{TRUE/pl}}, ustawienie jej na {{FALSE/pl}} spowoduje usunięcie ostatniego segmentu krzywej i otwarcie krzywej.

-    **Utwórz ścianę|Bool**: określa, czy krzywa tworzy ścianę, czy nie. Jeśli ma wartość {{TRUE/pl}}, tworzona jest ściana, w przeciwnym razie tylko krawędź jest uważana za część obiektu. Ta właściwość działa tylko wtedy, gdy włąściwość **Zamknięty** ma wartość {{TRUE/pl}} i jeśli krzywa nie przecina się sama.

-    **Parametryzacja|Float**: wpływa na kształt krzywej.

-    **Punkty|VectorList**: określa punkty krzywej w jego lokalnym układzie współrzędnych.



### Widok


{{TitleProperty|Rysunek Roboczy}}

-    **Rozmiar strzałki|Length**: określa rozmiar symbolu wyświetlanego na końcu krzywej.

-    **Typ strzałki|Enumeration**: określa typ symbolu wyświetlanego na końcu krzywej, którym może być {{value|Punkt}}, {{value|Okrąg}}, {{value|Strzałka}}, {{value|Grot}} lub {{value|Grot-2}}.

-    **Zakończenie strzałki|Bool**: określa, czy na końcu krzywej ma być wyświetlany symbol, aby można go było użyć jako linii adnotacji.

-    **Wzór|Enumeration**: określa [Wzór](Draft_Pattern/pl.md), którym ma być wypełniona powierzchnia zamkniętej krzywej. Ta właściwość działa tylko jeśli właściiwość **Utwórz ścianę** ma wartość {{TRUE/pl}} i jeśli właściwość **Tryb wyświetlania** ma wartość {{value|Cieniowany z krawędziami}}.

-    **Rozmiar wzoru|Float**: określa rozmiar [Wzoru](Draft_Pattern/pl.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć linię Krzywa złożona użyj metody `make_line` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeLine`.


```python
bspline = make_bspline(pointslist, closed=False, placement=None, face=None, support=None)
bspline = make_bspline(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Tworzy obiekt `Krzywej złóżonej` z podaną listą punktów, `pointslist`.
    -   Każdy punkt na liście jest zdefiniowany przez jego `FreeCAD.Vector`, z jednostkami w milimetrach.
    -   Alternatywnie, dane wejściowe mogą być typu `Part.Wire`, z których wyodrębniane są punkty.
-   Jeśli właściwość `Zamknięty` ma wartość {{True/pl}}, lub jeśli pierwszy i ostatni punkt mają identyczne wartości, krzywa jest zamknięta.
-   Jeśli `umiejscowienie` ma wartość `Brak`, kształt jest tworzony w punkcie początkowym.
-   Jeśli właściwość `ściana` ma wartość {{True/pl}}, a krzywą jest zamknięta, to krzywa będzie ścianą, czyli będzie wyglądała na wypełnioną.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

spline1 = Draft.make_bspline([p1, p2, p3], closed=False)
spline2 = Draft.make_bspline([p1, 2*p3, 1.3*p2], closed=False)
spline3 = Draft.make_bspline([1.3*p3, p1, -1.7*p2], closed=False)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BSpline/pl
