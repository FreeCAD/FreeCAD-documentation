---
 GuiCommand:
   Name: Draft Circle
   Name/pl: Draft: Okrąg
   MenuLocation: Drafting , Okrąg
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **C** **I**
   Version: 0.7
   SeeAlso: Draft_Arc/pl, Draft_Arc_3Points/pl

---

# Draft Circle/pl

## Opis

Polecenie <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> **Okrąg** tworzy okrąg w bieżącej [płaszczyźnie roboczej](Draft_SelectPlane/pl.md) na bazie punktu środkowego i promienia. Promień może być zdefiniowany przez wybranie punktu.

Rysunek okręgu można przekształcić w łuk eliptyczny, ustawiając jego właściwości {{PropertyData/pl|Kąt Pierwszy}} i {{PropertyData/pl|Kąt Ostatni}} na odmienne wartości.

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;"> 
*Okrąg wyznaczony przez dwa punkty, środek i promień*

## Użycie

Zobacz również [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Circle.svg" width=16px> [Okrąg](Draft_Circle/pl.md)**.
    -   Wybierz z menu opcję **Kreślenie → <img src="images/Draft_Circle.svg" width=16px> Okrąg**.
    -   Użyj skrótu klawiaturowego: **C**, a następnie **I**.
2.  Otworzy się panel zadań **Okrąg**. Zobacz [Opcje](#Opcje.md), aby uzyskać więcej informacji.
3.  Wybierz pierwszy punkt, środek okręgu, w oknie [widoku 3D](3D_view/pl.md), lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
4.  Wybierz drugi punkt w oknie [widoku 3D](3D_view/pl.md), lub wpisz wartość **Promienia**.

## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi.

-   Aby ręcznie wprowadzić współrzędne środka, wprowadź składowe X, Y i Z, a następnie naciśnij klawisz **Enter** po każdej z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy masz już żądane wartości. Wskazane jest, aby przed wprowadzeniem współrzędnych wysunąć kursor poza obszar okna [widoku 3D](3D_view/pl.md).
-   Naciśnij **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne są odniesione do globalnego układu współrzędnych, w przeciwnym razie są one odniesione do układu współrzędnych [płaszczyzny robocza](Draft_SelectPlane/pl.md). {{Version/pl|0.20}}
-   Naciśnij klawisz **L** lub kliknij pole wyboru **Wypełniony**, aby przełączyć tryb wypełnienia. Jeśli tryb wypełnienia jest włączony, utworzony okrąg będzie miał ustawioną właściwość {{PropertyData/pl|Make Face}} na `True` i będzie miał wypełnioną ścianę.
-   Naciśnij klawisz **T** lub kliknij pole wyboru **Kontynuuj**, aby przełączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie zostanie uruchomione ponownie po zakończeniu, umożliwiając dalsze tworzenie okręgów.
-   Naciśnij klawisz **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij klawisz **Esc** lub przycisk **Zamknij**, aby przerwać działanie polecenia.

## Uwagi

-   Szkic okręgu można edytować za pomocą polecenia [Edycja](Draft_Edit/pl.md).

## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Preferencje](Draft_Preferences/pl.md).

-   Aby zmienić liczbę miejsc po przecinku używanych do wprowadzania współrzędnych i promieni: **Edycja → Preferencje → Ogólne → Jednostki → Ustawienia jednostek → Liczba cyfr po przecinku**.
-   Aby zmienić wartość początkową trybu wypełnienia: **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Wypełniaj obiekty powierzchniami, gdy tylko jest to możliwe**. Zmiana trybu wypełnienia w panelu zadań spowoduje nadpisanie tych preferencji dla bieżącej sesji programu FreeCAD.
-   Jeśli opcja **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Używaj elementów pierwotnych, gdy jest to możliwe** jest zaznaczona, polecenie utworzy [Okrąg](Part_Circle/pl.md) środowiska Część, zamiast środowiska Rysunek Roboczy.

## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt okrąg wywodzi się z obiektu [Część: Part2DObject](Part_Part2DObject/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:

### Dane


{{TitleProperty|Rysunek Roboczy}}

-    {{PropertyData/pl|Powierzchnia|Area}}: *(tylko do odczytu)* określa pole powierzchni koła. Wartość będzie równa {{value|0.0}}, jeśli właściwość {{PropertyData/pl|Utwórz ścianę}} ma wartość `False` lub powierzchnia nie może zostać utworzona.

-    {{PropertyData/pl|Kąt pierwszy|Angle}}: określa kąt początkowy okręgu, zwykle {{value|0&#176;}}.

-    {{PropertyData/pl|Kąt ostatni|Angle}}: określa kąt końcowy okręgu, zwykle {{value|0&#176;}}.

-    {{PropertyData/pl|Utwórz ścianę|Bool}}: określa, czy okrąg tworzy ścianę, czy nie. Jeśli ma wartość `True`, tworzona jest ściana, w przeciwnym razie tylko obwód jest uważany za część obiektu. Właściwość ta działa tylko wtedy, gdy {{PropertyData/pl|Kąt pierwszy}} i {{PropertyData/pl|Kąt ostatni}} mają tę samą wartość. Zauważ, że {{value|0&#176;}} i {{value|360&#176;}} nie są uważane za takie same.

-    {{PropertyData/pl|Promień|Length}}: określa długość promienia okręgu.

### Widok


{{TitleProperty|Rysunek Roboczy}}

-    {{PropertyView/pl|Wzór|Enumeration}}: określa [wzór](Draft_Pattern/pl.md), którym ma być wypełniona powierzchnia koła. Ta właściwość działa tylko wtedy, gdy {{PropertyData/pl|Utwórz ścianę}} ma wartość `True` i gdy {{PropertyView/pl|Tryb wyświetlania}} ma wartość {{value|Linie płaskie}}.

-    {{PropertyView/pl|Rozmiar wzoru|Float}}: określa rozmiar [wzoru](Draft_Pattern/pl.md).

## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć okrąg użyj metody `make_circle` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeCircle`.


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```

-   Tworzy obiekt `Okrąg` o podanej wartości `Promienia` w milimetrach.
    -   
        `Promień`
        
        może być również obiektem `Część.krawędź`, którego atrybut `Krzywa` musi być obiektem `Część.okrąg`.
-   Jeśli `Umiejscowienie` ma wartość `Brak`, okrąg jest tworzony w punkcie początkowym.
-   Jeśli `Ściana` ma wartość `Prawda`, okrąg zostanie utworzony jako powierzchnia, czyli będzie wyglądał na wypełniony.
-   Jeśli `Kąt pierwszy` i `Kąt ostatni` są podane w stopniach i mają różne wartości, zostaną one użyte, a obiekt pojawi się jako [Łuk](Draft_Arc/pl.md).

Przykład: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Circle/pl
