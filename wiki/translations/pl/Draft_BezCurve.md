---
 GuiCommand:
   Name: Draft BezCurve
   Name/pl: Rysunek Roboczy: Krzywa Béziera
   MenuLocation: Kreślenie , Narzędzia krzywych Béziera , Krzywa Béziera<br>Kreślenie 2D , Krzywa Béziera
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Shortcut: **B** **Z**
   Version: 0.14
   SeeAlso: Draft_CubicBezCurve/pl, Draft_BSpline/pl
---

# Draft BezCurve/pl



## Opis

Polecenie <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> **Krzywa Béziera** tworzy krzywą [Béziera](http://en.wikipedia.org/wiki/Bezier_curve) na podstawie kilku punktów.

Polecenie tworzy pojedynczą krzywą Béziera o **Stopniu** równym `number_of_points - 1`. Można ją przekształcić w fragmentaryczną krzywą Béziera, zmniejszając tę właściwość.

Polecenia Krzywa Béziera i [Sześcienna krzywa Béziera](Draft_CubicBezCurve/pl.md) używają **punktów kontrolnych** do zdefiniowania położenia i krzywizny odcinka krzywej. Z kolei polecenie [Krzywa złożona](Draft_BSpline/pl.md) określa **dokładne punkty**, przez które będzie przechodzić krzywa.

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;"> 
*Krzywa Beziera zdefiniowana przez wiele punktów*



## Użycie

Zapoznaj się również z informacjami na stronie: [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Istnieje kilka sposobów wywołania polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_BezCurve.svg" width=16px> '''Krzywa Beziera'''**.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz z menu opcję **Kreślenie → Narzędzia krzywych Béziera → <img src="images/Draft_BezCurve.svg" width=16px> Krzywa Béziera**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Kreślenie 2D → <img src="images/Draft_BezCurve.svg" width=16px> Krzywa Béziera** z menu.
    -   Użyj skrótu klawiaturowego: **B**, a następnie **Z**.
2.  Zostanie otwarty panel zadań **Krzywa Béziera**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
3.  Wybierz pierwszy punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
4.  Wybierz dodatkowe punkty w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
5.  Naciśnij **Esc** lub przycisk **Zamknij**, aby zakończyć polecenie.



## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi *(w wersji 1.0)*.

-   Aby ręcznie wprowadzić współrzędne, wprowadź składowe X, Y i Z, a następnie naciśnij klawisz **Enter** po każdej z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy masz już żądane wartości. Wskazane jest, aby przed wprowadzeniem współrzędnych wysunąć kursor poza obszar okna [widoku 3D](3D_view/pl.md).
-   Wciśnij **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne są względne do ostatniego punktu, jeśli jest dostępny, w przeciwnym razie są one względne do początku układu współrzędnych.
-   Naciśnij **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne odnoszą się do globalnego układu współrzędnych, w przeciwnym razie odnoszą się do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md).
-   Naciśnij **F** lub kliknij pole wyboru **Wypełniony**, aby przełączyć tryb wypełnienia. Jeśli tryb wypełnienia jest włączony, utworzona krzywa będzie miała właściwość **Utwórz ścianę** ustawione na {{TRUE/pl}} i będzie miała wypełnioną ścianę, pod warunkiem, że jest zamknięta i nie przecina się samoczynnie. Należy pamiętać, że krzywa przecinająca się z powierzchnią nie będzie wyświetlana poprawnie, dla takiej krzywej **Utwórz ścianę** musi być ustawiona na {{FALSE/pl}}.
-   Naciśnij **N** lub kliknij pole wyboru **Kontynuuj**, aby włączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie uruchomi się ponownie po użyciu **<img src="images/Draft_FinishLine.svg" width=16px> Zakończ** lub **<img src="images/Draft_CloseLine.svg" width=16px> Zamknij**, lub po utworzeniu zamkniętej krzywej poprzez przyciągnięcie do pierwszego punktu krzywej, umożliwiając dalsze tworzenie krzywych.
-   Naciśnij **/** lub przycisk **<img src="images/Draft_UndoLine.svg" width=16px> Cofnij**, aby anulować ostatni punkt.
-   Naciśnij **A** lub przycisk **<img src="images/Draft_FinishLine.svg" width=16px> Zakończ**, aby zakończyć polecenie i pozostawić krzywą otwartą.
-   Naciśnij **O** lub przycisk **<img src="images/Draft_CloseLine.svg" width=16px> Zamknij**, aby zakończyć polecenie i zamknąć krzywą. Zamkniętą krzywą można również utworzyć, przyciągając ją do pierwszego punktu krzywej.
-   Naciśnij **W** lub przycisk **<img src="images/Draft_Wipe.svg" width=16px> Wyczyść**, aby usunąć już umieszczone segmenty, ale kontynuować pracę od ostatniego punktu.
-   Naciśnij **U** lub przycisk **<img src="images/Draft_SelectPlane.svg" width=16px> [Ustaw płaszczyznę roboczą](Draft_SelectPlane/pl.md)**, aby ustawić bieżącą płaszczyznę roboczą w orientacji określonej przez ostatni i poprzedni punkt.
-   Naciśnij **S**, aby włączyć lub wyłączyć [Przyciąganie](Draft_Snap.md).
-   Naciśnij **Esc** lub przycisk **Zamknij**, aby zakończyć polecenie.



## Uwagi

-   Krzywa Beziera środowiska Rysunek Roboczy może być edytowana za pomocą polecenia [Edytuj](Draft_Edit/pl.md).
-   OpenCascade, a tym samym FreeCAD, nie obsługuje krzywych Béziera o stopniach większych niż 25. W praktyce nie powinno to stanowić problemu, ponieważ większość użytkowników zazwyczaj używa krzywych Béziera o stopniach od 3 do 5.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Krzywa Beziera środowiska Rysunek Roboczy wywodzi się z obiektu [Część: Part2DObject](Part_Part2DObject/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Rysunek Roboczy}}

-    **Obszar|Area**: *(tylko do odczytu)* określa obszar powierzchni krzywej. Wartość będzie {{value|0.0}} jeśli właściwość **Utwórz ścianę** ma wartość {{FALSE/pl}} lub ściana nie może zostać utworzona.

-    **Zamknięta|Bool**: określa czy krzywa jest zamknięta czy nie. Jeśli krzywa jest początkowo otwarta, wartość ta wynosi {{FALSE/pl}}, ustawienie jej na {{TRUE/pl}} spowoduje narysowanie segmentu w celu zamknięcia krzywej. Jeśli krzywa jest początkowo zamknięta, wartość ta wynosi {{TRUE/pl}}, ustawienie jej na {{FALSE/pl}} spowoduje usunięcie ostatniego segmentu i otwarcie krzywej.

-    **Ciągła|IntegerList**: *(tylko do odczytu)* określa ciągłość krzywej.

-    **Stopień|Integer**: określa stopień krzywej.

-    **Długość|Length**: *(tylko do odczytu)* określa całkowitą długość krzywej.

-    **Utwórz ścianę|Bool**: określa czy krzywa tworzy powierzchnię czy nie. Jeśli jest {{TRUE/pl}}, tworzona jest ściana, w przeciwnym razie tylko obwód jest uważany za część obiektu. Ta właściwość działa tylko wtedy, gdy właściwość **Zamknięta** ma wartość {{TRUE/pl}} i jeśli krzywa nie przecina się samoczynnie.

-    **Punkty|VectorList**: określa punkty kontrolne krzywej w jej lokalnym układzie współrzędnych.



### Widok


{{TitleProperty|Rysunek Roboczy}}

-    **Rozmiar strzałki|Length**: określa rozmiar symbolu wyświetlanego na końcu krzywej.

-    **Typ strzałki|Enumeration**: określa typ symbolu wyświetlanego na końcu krzywej, którym może być {{value|Punkt}}, {{value|Okrąg}}, {{value|Strzałka}}, {{value|Grot}} lub {{value|Grot-2}}.

-    **Zakończenie strzałki|Bool**: określa, czy na końcu krzywej ma być wyświetlany symbol, aby można go było użyć jako linii adnotacji.

-    **Wzór|Enumeration**: określa [Wzór](Draft_Pattern/pl.md), którym ma być wypełniona powierzchnia zamkniętej krzywej. Ta właściwość działa tylko jeśli właściiwość **Utwórz ścianę** ma wartość {{TRUE/pl}} i jeśli właściwość **Tryb wyświetlania** ma wartość {{value|Cieniowany z krawędziami}}.

-    **Rozmiar wzoru|Float**: określa rozmiar [Wzoru](Draft_Pattern/pl.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć Krzywa Beziera środowiska Rysunek Roboczy użyj metody `make_bezcurve` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeBezCurve`.


```python
bezcurve = make_bezcurve(pointslist, closed=False, placement=None, face=None, support=None, degree=None)
bezcurve = make_bezcurve(Part.Wire, closed=False, placement=None, face=None, support=None, degree=None)
```

-   Tworzy obiekt `bezcurve` z podaną listą punktów, `pointslist`.
    -   Każdy punkt na liście jest zdefiniowany przez jego `FreeCAD.Vector`, z jednostkami w milimetrach.
    -   Alternatywnie, dane wejściowe mogą być typu `Part.Wire`, z których wyodrębniane są punkty.
-   Jeśli `closed` ma wartość {{True/pl}}, lub jeśli pierwszy i ostatni punkt mają identyczne wartości, krzywa jest zamknięta.
-   Jeśli `placement` ma wartość `Brak`, kształt jest tworzony w punkcie początkowym.
-   Jeśli parametr `ściana` ma wartość {{True/pl}}, a krzywa jest zamknięta, to krzywa będzie ścianą, czyli będzie wyglądała na wypełnioną.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)
p4 = App.Vector(1500, -2000, 0)

bezcurve1 = Draft.make_bezcurve([p1, p2, p3, p4], closed=True)
bezcurve2 = Draft.make_bezcurve([p4, 1.3*p2, p1, 4.1*p3], closed=True)
bezcurve3 = Draft.make_bezcurve([1.7*p3, 1.5*p4, 2.1*p2, p1], closed=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BezCurve/pl
