---
- GuiCommand:/pl
   Name:Draft Rectangle
   Name/pl:Draft: Prostokąt
   MenuLocation:Drafting → Prostokąt
   Workbenches:[Rysunek roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Shortcut:**R** **E**
   Version:0.7
---

# Draft Rectangle/pl

## Opis

Polecenie <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> **Prostokąt** tworzy prostokąt w bieżącej [płaszczyźnie roboczej](Draft_SelectPlane/pl.md) przy uzyciu dwóch punktów.

Rogi prostokąta mogą być zaokrąglone lub sfazowane poprzez zmianę właściwości {{PropertyData/pl|Promień zaokrąglenia}} lub {{PropertyData/pl|Rozmiar fazki}}. Możliwe jest również podzielenie prostokąta przez zmianę jego właściwości {{PropertyData/pl|Kolumny}} i/lub {{PropertyData/pl|Rzędy}}.

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;"> 
*Prostokąt zdefiniowany przez dwa punkty*

## Użycie

Zobacz również [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Rectangle.svg" width=16px> [Tworzy prostokąt ...](Draft_Rectangle/pl.md)**.
    -   Wybierz z menu opcję **Kreślenie → <img src="images/Draft_Rectangle.svg" width=16px> Prostokąt**.
    -   Użyj skrótu klawiaturowego: **R**, a następnie **E**.
2.  Otworzy się panel zadań **Prostokąt**. Zobacz akapit [Opcje](#Opcje.md), aby uzyskać więcej informacji.
3.  Wybierz pierwszy punkt w oknie [widoku 3D](3D_view.md), lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
4.  Wybierz drugi punkt w oknie [widoku 3D](3D_view.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**. Ten punkt nie może być związany z osią X, Y lub Z.

## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi.

-   Aby ręcznie wprowadzić współrzędne, wprowadź składowe X, Y i Z, i naciśnij klawisz **Enter** po każdej z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy masz już żądane wartości. Wskazane jest, aby przed wprowadzeniem współrzędnych wysunąć kursor myszki poza okno [widoku 3D](3D_view/pl.md).
-   Naciśnij klawisz **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne drugiego punktu są odniesione do pierwszego punktu, w przeciwnym razie są one odniesione do początku układu współrzędnych.
-   Naciśnij klawisz **G** lub kliknij w pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne są odniesione do globalnego układu współrzędnych, w przeciwnym razie są one odniesione do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md). {{Version/pl|0.20}}
-   Naciśnij klawisz **L** lub kliknij pole wyboru **Wypełnienie**, aby przełączyć tryb wypełnienia. Jeśli tryb wypełnienia jest włączony, utworzony prostokąt będzie miał ustawioną właściwość {{PropertyData/pl|Utwórz ścianę}} na wartość `True` i będzie miał wypełnioną powierzchnię.
-   Naciśnij klawisz **T** lub kliknij pole wyboru **Kontynuuj**, aby przełączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie zostanie uruchomione ponownie po zakończeniu operacji, umożliwiając dalsze tworzenie prostokątów.
-   Naciśnij klawisz **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij klawisz **Esc** lub przycisk **Zamknij**, aby przerwać działanie polecenia.

## Uwagi

-   Szkic prostokąta można edytować za pomocą polecenia [Edycja](Draft_Edit/pl.md).

## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Preferencje](Draft_Preferences/pl.md).

-   Aby zmienić ilość miejsc po przecinku używanych przy wprowadzaniu współrzędnych: **Edycja → Preferencje → Ogólne → Jednostki → Ustawienia jednostek → Liczba cyfr po przecinku**.
-   Aby zmienić wartość początkową trybu wypełnienia: **Edycja → Preferencje → Kreślenie → Ustawienia ogólne → Opcje narzędzi do kreślenia → Wypełniaj obiekty powierzchniami, gdy tylko jest to możliwe**. Zmiana trybu wypełnienia w panelu zadań spowoduje nadpisanie tych preferencji dla bieżącej sesji FreeCAD.
-   Jeśli opcja **Edycja → Preferencje → Kreślenie → Ustawienia ogólne → Opcje narzędzi szkicu → Używaj elementów pierwotnych, gdy jest to możliwe** jest zaznaczona, polecenie utworzy [płaszczyznę części](Part_Plane/pl.md) zamiast szkicu prostokąta.

## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Prostokąt wywodzi się z obiektu [Część: Part2DObject](Part_Part2DObject/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:

### Dane


{{TitleProperty|Rysunek Roboczy}}

-    {{PropertyData/pl|Powierzchnia|Area}}: *(tylko do odczytu)* określa powierzchnię prostokąta. Wartość ta będzie równa {{value|0.0}}, jeśli właściwość {{PropertyData/pl|Utwórz ścianę}} ma wartość `False`.

-    {{PropertyData/pl|Rozmiar fazki|Length}}: określa długość faz na rogach prostokąta.

-    {{PropertyData/pl|Kolumny|Integer}}: określa liczbę kolumn o równej wielkości, na które podzielony jest prostokąt.

-    {{PropertyData/pl|Promień zaokrąglenia|Length}}: określa promień zaokrągleń na rogach prostokąta.

-    {{PropertyData/pl|Wysokość|Distance}}: określa wysokość prostokąta.

-    {{PropertyData/pl|Długość|Distance}}: określa długość prostokąta.

-    {{PropertyData/pl|Utwórz ścianę|Bool}}: określa, czy prostokąt tworzy powierzchnię, czy nie. Jeśli wartość jest równa `True`, tworzona jest ściana, w przeciwnym razie tylko obwód jest uważany za część obiektu.

-    {{PropertyData/pl|Rzędy|Integer}}: określa liczbę równej wielkości rzędów, na które podzielony jest prostokąt.

### Widok


{{TitleProperty|Rysunek Roboczy}}

-    {{PropertyView/pl|Wzór|Enumeration}}: określa [wzór](Draft_Pattern/pl.md), którym ma być wypełniona powierzchnia prostokąta. Ta właściwość działa tylko wtedy, gdy właściwość {{PropertyData/pl|Utwórz ścianę}} ma wartość `True` i gdy właściwość {{PropertyView/pl|Tryb wyświatlania}} ma wartość {{value|Płaskie linie}}.

-    {{PropertyView/pl|Rozmiar wzoru|Float}}: określa rozmiar [wzoru](Draft_Pattern/pl.md).

-    {{PropertyView/pl|Obraz tekstury|File}}: określa ścieżkę pliku obrazu, który ma zostać odwzorowany na powierzchni prostokąta. Wyczyszczenie tej właściwości spowoduje usunięcie obrazu. Prostokąt powinien mieć takie same proporcje jak obraz, aby uniknąć zniekształceń.

## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć prostokąt użyj metody `mmake_rectangle` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeRectangle`.


```python
rectangle = make_rectangle(length, height, placement=None, face=None, support=None)
```

-   Tworzy obiekt `Prostokąt` o `Długości` w kierunku X i `Wysokości` w kierunku Y, z jednostkami w milimetrach.
-   Jeśli parametr `Umiejscownienie` ma wartość `Brak`, prostokąt zostanie utworzony w punkcie początkowym, a jego długość będzie równoległa do osi X.
-   Jeśli parametr `Ściana` ma wartość `Prawda`, prostokąt zostanie utworzony jako powierzchnia, czyli będzie wyglądał na wypełniony.

Przykład: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle1 = Draft.make_rectangle(4000, 1000)
rectangle2 = Draft.make_rectangle(1000, 4000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 45))

rectangle3 = Draft.make_rectangle(3500, 250, placement=place3)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rectangle/pl
