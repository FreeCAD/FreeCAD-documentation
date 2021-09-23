---
- GuiCommand:/pl
   Name:Draft Wire
   Name/pl:Rysunek Roboczy: Linia łamana
   MenuLocation:Kreślenie → Linia łamana
   Workbenches:[Rysunek Roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Shortcut:**P** **L**
---

# Draft Wire/pl

## Opis

Polecenie <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> **Rysunek Roboczy: Linia łamana** [tworzy](#Utwórz.md) polilinię, czyli sekwencję kilku połączonych segmentów linii. Polecenie to może być również użyte do [łączenia](#Przyłącz.md) [linii](Draft_Line/pl.md) i polilinii.

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;"> 
*Linia zdefiniowana przez wiele punktów*

## Utwórz

## Użycie

Zobacz również [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Wire.svg" width=16px> [Utwórz wielopunktową linię ...](Draft_Wire/pl.md)**.
    -   Wybierz opcję z menu **Kreślenie → <img src="images/Draft_Wire.svg" width=16px> Polilinia**.
    -   Użyj skrótu klawiaturowego: **P**, a następnie **L**.
2.  Otworzy się panel zadań **Polilinia**. Zobacz [opcje](#Opcje.md) aby uzyskać więcej informacji.
3.  Wybierz pierwszy punkt w oknie [widoku 3D](3D_view/pl.md), lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px>. Wprowadź punkt**.
4.  Wybierz dodatkowe punkty w oknie [widoku 3D](3D_view/pl.md), lub wpisz współrzędne i wciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px>. Wprowadź punkt**.
5.  Naciśnij przycisk **Esc** lub przycisk **Zamknij**, aby zakończyć działanie polecenia.

### Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi.

-   Aby ręcznie wprowadzić współrzędne, wprowadź składowe X, Y i Z, i naciśnij klawisz **Enter** za każdym razem. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy ustawisz żądane wartości. Wskazane jest, aby przed wprowadzeniem współrzędnych przesunąć kursor myszki poza okno [widoku 3D](3D_view/pl.md).
-   Naciśnij klawisz **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne są odnoszone do ostatniego punktu, jeśli jest dostępny, w przeciwnym razie są odnoszone do początku układu współrzędnych.
-   Naciśnij klawisz **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne odnoszone są do globalnego układu współrzędnych, w przeciwnym razie są odnoszone do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane.md). {{Version/pl|0.20}}
-   Naciśnij klawisz **L** lub kliknij pole wyboru **Wypełniony**, aby przełączyć tryb wypełnienia. Jeśli tryb wypełniania jest włączony, utworzona polilinia będzie miała wartość {{PropertyData/pl|Utwórz powierzchnię}} ustawioną na {{True}} i będzie miała wypełnioną powierzchnię, pod warunkiem, że jest zamknięta i nie przecina się sama. Zauważ, że polilinia z powierzchnią nie będzie wyświetlana poprawnie, dla takiej konstrukcji wartość {{PropertyData/pl|Utwórz powierzchnię}} musi być ustawiona na {{False}}.
-   Naciśnij klawisz **T** lub kliknij w pole wyboru **Kontynuuj**, aby przełączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie uruchomi się ponownie po użyciu przycisku **<img src="images/Draft_FinishLine.svg" width=16px> Zakończ** lub **<img src="images/Draft_CloseLine.svg" width=16px> Zamknij**, lub po utworzeniu zamkniętej polilinii przez przyciągnięcie do pierwszego punktu polilinii, co pozwala na kontynuowanie tworzenia polilinii.
-   Naciśnij przycisk {{button|<img src="images/Draft_UndoLine.svg" width=16px> Cofnij}}, aby cofnąć ostatni punkt. Skrót klawiaturowy **Ctrl** + **Z** obecnie nie działa zgodnie z oczekiwaniami.
-   Naciśnij przycisk **A** lub przycisk **<img src="images/Draft_FinishLine.svg" width=16px> Zakończ**, aby zakończyć polecenie i pozostawić polilinię otwartą.
-   Naciśnij klawisz **O** lub przycisk **<img src="images/Draft_CloseLine.svg" width=16px> Zamknij**, by zakończyć polecenie i zamknąć polilinię. Zamknięta polilinia może być także utworzona przez przyciągnięcie do pierwszego punktu polilinii.
-   Wciśnij klawisz **W** lub przycisk **<img src="images/Draft_Wipe.svg" width=16px> Wyczyść**, aby usunąć już umieszczone segmenty, ale kontynuować pracę od ostatniego punktu.
-   Wciśnij klawisz **U** lub przycisk **<img src="images/Draft_SelectPlane.svg" width=16px> [Ustaw płaszczyznę roboczą](Draft_SelectPlane/pl.md)** aby ustawić aktualną płaszczyznę roboczą w orientacji ostatniego odcinka.
-   Naciśnij klawisz **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij klawisz **Esc** lub przycisk {{button|Zamknij}}, aby zakończyć polecenie.

## Przyłącz

## Użycie 

1.  Punkty końcowe [linii](Draft_Line/pl.md) i/lub polilinii, które mają być połączone muszą się dokładnie pokrywać. Jeśli jest to wymagane, najpierw dopasuj punkty, aby to zapewnić.
2.  Wybierz dwie lub więcej [linii](Draft_Line/pl.md) i/lub polilinii.
3.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Wire.svg" width=16px> [Utwórz wielopunktową linię](Draft_Wire/pl.md)**.
    -   Wybierz opcję w menu **Kreślenie → <img src="images/Draft_Wire.svg" width=16px> Polilinia**.
    -   Użyj skrótu klawiaturowego: **P**, a następnie **L**.

## Uwagi

-   Polilinia środowiska Rysunek Roboczy może być edytowana za pomocą polecenia [Edytuj](Draft_Edit/pl.md).
-   Polilinia środowiska Rysunek Roboczy może być przekształcona w [Krzywą złożoną](Draft_BSpline/pl.md) za pomocą polecenia [Poililinia na krzywą złożoną](Draft_WireToBSpline/pl.md).
-   [Linie](Draft_Line/pl.md) i polilinia środowiska Rysunek Roboczy, mogą być również połączone za pomocą polecenia [Połącz](Draft_Join/pl.md) lub [Ulepsz kształt](Draft_Upgrade/pl.md).

## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Preferencje](Draft_Preferences/pl.md).

-   Aby zmienić liczbę miejsc po przecinku używanych do wprowadzania wartości współrzędnych długości i kątów: **Edycja → Preferencje → Ogólne → Jednostki → Ustawienia jednostek → Liczba cyfr po przecinku**.
-   Aby zmienić wartość początkową trybu wypełnienia: **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Wypełniaj obiekty powierzchniami, gdy tylko jest to możliwe**. Zmiana trybu wypełnienia w panelu zadań spowoduje nadpisanie tych preferencji dla bieżącej sesji programu FreeCAD.

## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt polilinia wywodzi się z obiektu [Część: Part2DObject](Part_Part2DObject/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:

### Dane


{{TitleProperty|Rysunek Roboczy}}

-    {{PropertyData/pl|Obszar|Area}}: *(tylko do odczytu)* Określa powierzchnię polilinii. Wartość będzie wynosić {{value|0.0}} jeśli {{PropertyData/pl|Utwórz powierzchnię}} przyjmuje wartość {{False}} lub powierzchnia nie może zostać utworzona.

-    {{PropertyData/pl|Podstawowa|Link}}
    

-    {{PropertyData/pl|Wielkość fazki|Length}}: określa długość fazek na rogach polilinii.

-    {{PropertyData/pl|Zamknięta|Bool}}: określa czy polilinia jest zamknięta czy nie. Jeśli polilinia jest początkowo otwarta, wartość ta wynosi `False`, ustawienie jej na `True` spowoduje narysowanie segmentu linii zamykającego polilinię. Jeśli polilinia jest początkowo zamknięta, wartość ta wynosi `True`, a ustawienie jej na `False` spowoduje usunięcie ostatniego segmentu i otwarcie polilinii.

-    {{PropertyData/pl|Koniec|VectorDistance}}: określa punkt końcowy polilinii.

-    {{PropertyData/pl|Promień zaokrąglenia|Length}}: określa promień zaokrągleń na rogach polilinii.

-    {{PropertyData/pl|Długość|Length}}: *(tylko do odczytu)* określa całkowitą długość przewodu.

-    {{PropertyData/pl|Utwórz powierzchnię|Bool}}: określa czy polilinia tworzy ścianę, czy też nie. Jeśli posiada wartość `True`, to tworzona jest powierzchnia, w przeciwnym razie tylko krawędzie są uważane za część obiektu. Właściwość ta działa tylko wtedy, gdy {{PropertyData/pl|Closed}} ma wartość `True` i gdy polilinia nie przecina się samoistnie.

-    {{PropertyData/pl|Punkty|VectorList}}: określa punkty polilinii w jej lokalnym układzie współrzędnych.

-    {{PropertyData/pl|Start|VectorDistance}}: określa punkt początkowy polilinii.

-    {{PropertyData/pl|Pododdziały|Integer}}: określa liczbę podziałów dla każdej krawędzi polilinii. Jeśli jest to wartość {{value|1}} każda krawędź zostanie podzielona na równe segmenty o wartości {{value|2}}. Podziały są stosowane przed fazowaniem i zaokrąglaniem.

-    {{PropertyData/pl|Narzędzia|Link}}
    

### Widok


{{TitleProperty|Rysunek Roboczy}}

-    **Rozmiar strzałki|Length**: określa wielkość symbolu wyświetlanego na końcu polilinii.

-    **Typ strzałki|Enumeration**: określa typ symbolu wyświetlanego na końcu przewodu, którym może być {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} lub {{value|Tick-2}}.

-    **Zakończenie strzałki.|Bool**: określa, czy pokazywać symbol na końcu przewodu, aby można go było użyć jak linii adnotacji.

-    **Wzór|Enumeration**: określa rodzaj [wypełnienia](Draft_Pattern/pl.md), którym ma być pokryta powierzchnia zamkniętej linii. Ta właściwość działa tylko wtedy, gdy właściwość {{PropertyData/pl|Utwórz powierzchnię}} ma wartość `True` i gdy {{PropertyView/pl|Display Mode}} ma wartość {{value|Flat Lines}}.

-    **Rozmiar wzoru|Float**: określa rozmiar [wypełnienia](Draft_Pattern/pl.md).

## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć polilinię użyj metody `make_wire` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeWire`.


```python
wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
wire = make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Tworzy obiekt `Wire` z podaną listą punktów, `pointslist`.
    -   Każdy punkt na liście jest zdefiniowany przez jego `FreeCAD.Vector`, z jednostkami w milimetrach.
    -   Alternatywnie, dane wejściowe mogą być typu `Part.Wire`, z których wyodrębniane są punkty.
-   Jeśli `closed` ma wartość `True`, lub jeśli pierwszy i ostatni punkt mają identyczne wartości, polilinia jest zamknięta.
-   Jeśli `placement` ma wartość `None`, kształt jest tworzony w punkcie początkowym.
-   Jeśli parametr `face` ma wartość `True`, a polilinia jest zamknięta, to polilinia będzie ścianą, czyli będzie wyglądała na wypełnioną.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Wire/pl
