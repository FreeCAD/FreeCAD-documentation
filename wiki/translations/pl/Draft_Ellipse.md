---
- GuiCommand:
   Name:Draft Ellipse
   Name/pl:Draft: Elipsa
   MenuLocation:Kreślenie - Elipsa
   Workbenches:[Rysunek Roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Shortcut:**E** **L**
   Version:0.7
---

# Draft Ellipse/pl

## Opis

Polecenie <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> **Elipsa** tworzy elipsę w bieżącej [płaszczyźnie roboczej](Draft_SelectPlane/pl.md) z dwóch punktów definiujących prostokąt, w którym zmieści się elipsa.

Rysunek elipsy można przekształcić w łuk eliptyczny, ustawiając jego właściwości {{PropertyData/pl|Kąt Pierwszy}} i {{PropertyData/pl|Kąt Ostatni}} na odmienne wartości.

<img alt="" src=images/Draft_ellipse_example.jpg  style="width:400px;"> 
*Elipsa zdefiniowana przez narożniki prostokąta*

## Użycie

Zobacz również [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Ellipse.svg" width=16px> [Elipsa](Draft_Ellipse/pl.md)**.
    -   Wybierz z menu opcję **Kreślenie → <img src="images/Draft_Ellipse.svg" width=16px> Elipsa**.
    -   Użyj skrótu klawiaturowego: **E**, a następnie **L**.
2.  Otworzy się panel zadań **Elipsa**. Zobacz [Opcje](#Opcje.md), aby uzyskać więcej informacji.
3.  Wybierz pierwszy punkt w oknie [widoku 3D](3D_view/pl.md), lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px>. Wprowadź punkt**.
4.  Wybierz drugi punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**. Ten punkt nie może być związany z osią X, Y lub Z.

## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi.

-   Aby ręcznie wprowadzić współrzędne, wprowadź składowe X, Y i Z, i naciśnij **Enter** po każdej z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy masz już żądane wartości. Wskazane jest, aby przed wprowadzeniem współrzędnych wysunąć kursor z okna [widoku 3D](3D_view/pl.md).
-   Naciśnij klawisz **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne drugiego punktu są odniesione do pierwszego punktu, w przeciwnym razie są one odniesione do początku układu współrzędnych.
-   Naciśnij klawisz **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne są zależne od globalnego układu współrzędnych, w przeciwnym razie są one odniesione do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md). {{Version/pl|0.20}}
-   Naciśnij klawisz **L** lub kliknij pole wyboru **Wypełnienie**, aby przełączyć tryb wypełnienia. Jeśli tryb wypełnienia jest włączony, utworzona elipsa będzie miała właściwość {{PropertyData/pl|Utwórz ścianę}} ustawioną na wartość `True` i będzie miała wypełnioną powierzchnię.
-   Naciśnij klawisz **T** lub kliknij pole wyboru **Kontynuuj**, aby przełączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie zostanie uruchomione ponownie po zakończeniu, umożliwiając dalsze tworzenie elips.
-   Naciśnij klawisz **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij przycisk **Esc** lub przycisk **Zamknij**, aby przerwać wykonywanie polecenia.

## Uwagi

-   Elipsę szkicu można edytować za pomocą polecenia [Edycja](Draft_Edit/pl.md).

## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Preferencje](Draft_Preferences/pl.md).

-   Aby zmienić liczbę miejsc po przecinku używanych do wprowadzania współrzędnych: **Edycja → Preferencje → Ogólne → Jednostki → Ustawienia jednostek → Liczba cyfr po przecinku**.
-   Aby zmienić wartość początkową trybu wypełnienia: **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Wypełniaj obiekty powierzchniami, gdy tylko jest to możliwe**. Zmiana trybu wypełnienia w panelu zadań spowoduje nadpisanie tych preferencji dla bieżącej sesji programu FreeCAD.
-   Jeśli opcja **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Używaj elementów pierwotnych, gdy jest to możliwe** jest zaznaczona, polecenie utworzy [Elipsę](Part_Ellipse/pl.md) środowiska Część, zamiast środowiska Rysunek Roboczy.

## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Elipsa wywodzi się z obiektu [Część: Part2DObject](Part_Part2DObject/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:

### Dane


{{TitleProperty|Rysunek Roboczy}}

-    {{PropertyData/pl|Obszar|Area}}: (tylko do odczytu) określa pole powierzchni lica elipsy. Wartość będzie równa {{value|0.0}}, jeśli {{PropertyData/pl|Utwórz ścianę}} ma wartość `False` lub powierzchnia nie może zostać utworzona.

-    {{PropertyData/pl|Kąt pierwszy|Angle}}: określa kąt pierwszego punktu elipsy, zwykle {{value|0&#176;}}.

-    {{PropertyData/pl|Kąt ostatni|Angle}}: określa kąt ostatniego punktu elipsy, zwykle {{value|0&#176;}}.

-    {{PropertyData/pl|Promień główny|Length}}: określa promień główny elipsy.

-    {{PropertyData/pl|Utwórz ścianę|Bool}}: określa, czy elipsa ma tworzyć ścianę, czy nie. Jeśli ma wartość `True` tworzona jest powierzchnia, w przeciwnym razie tylko obwód jest traktowany jako część obiektu. Ta właściwość działa tylko jeśli kształt jest pełną elipsą.

-    {{PropertyData/pl|Promień mniejszy|Length}}: określa promień mniejszy elipsy.

### Widok


{{TitleProperty|Rysunek Roboczy}}

-    {{PropertyView/pl|Wzór|Enumeration}}: określa [wzór](Draft_Pattern/pl.md), którym ma być wypełniona powierzchnia elipsy. Ta właściwość działa tylko wtedy, gdy {{PropertyData/pl|Utwórz ścianę}} ma wartość `True` i gdy {{PropertyView/pl|Tryb wyświetlania}} ma wartość {{value|Linie płaskie}}.

-    {{PropertyView/pl|Rozmiar wzoru|Float}}: określa rozmiar [wzoru](Draft_Pattern/pl.md).

## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć Elipsę użyj metody `make_ellipse` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeEllipse`.


```python
ellipse = make_ellipse(majradius, minradius, placement=None, face=True, support=None)
```

-   Tworzy obiekt `ellipse` o podanym promieniu głównym *(`majradius`)* i małym *(`minradius`)* w milimetrach.
    -   Większa wartość zostanie użyta dla promienia głównego *(oś X)*, jeśli nie zostanie podane inne umiejscowienie.
-   Jeśli `placement` ma wartość `None`, elipsa zostanie utworzona w punkcie początkowym.
-   Jeśli `face` ma wartość `True`, elipsa zostanie utworzona jako powierzchnia, czyli będzie wyglądać na wypełnioną.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

ellipse1 = Draft.make_ellipse(3000, 200)
ellipse2 = Draft.make_ellipse(700, 1000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

ellipse3 = Draft.make_ellipse(700, 1000, placement=place3)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Ellipse/pl
