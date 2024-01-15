---
 GuiCommand:
   Name: Draft Polygon
   Name/pl: Rysunek Roboczy: Wielokąt foremny
   MenuLocation: Kreślenie , Wielokąt foremny
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **P** **G**
   Version: 0.7
---

# Draft Polygon/pl



## Opis

Polecenie <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> **Wielokąt foremny** tworzy okrąg w bieżącej [płaszczyźnie roboczej](Draft_SelectPlane/pl.md) na bazie punktu środkowego i promienia. Promień może być zdefiniowany przez wybranie punktu.

Szkic wielokąta może zostać przełączony z wpisanego na opisany poprzez zmianę jego właściwości **Tryb kreślenia**. Narożniki szkicu wielokąta można zaokrąglić lub sfazować, zmieniając odpowiednio właściwości **Promień zaokrąglenia** lub **Promień sfazowania**.

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;"> 
*Wielokąt foremny zdefiniowany przez dwa punkty, środek i promień.*



## Użycie

Zapoznaj się również z informacjami na stronie: [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_Polygon.svg" width=16px> '''Wielokąt foremny'''**.
    -   Wybierz opcję z menu **Kreślenie → <img src="images/Draft_Polygon.svg" width=16px> Wielokąt foremny**.
    -   Użyj skrótu klawiaturowego: **P**, a następnie **G**.
2.  Otworzy się panel zadań **Wielokąt**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
3.  Ustaw żądaną liczbę **Boków**.
4.  Wybierz pierwszy punkt, środek wielokąta, w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
5.  Wybierz drugi punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz **Promień**.



## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi *(w wersji 0.22)*.

-   Aby samodzielnie wprowadzić współrzędne środka, wprowadź komponent X, Y i Z i naciśnij **Enter** po każdym z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy uzyskasz żądane wartości. Zaleca się przesunięcie wskaźnika poza obszar okna [widoku 3D](3D_view/pl.md) przed wprowadzeniem współrzędnych.
-   Naciśnij **G** lub kliknij pole wyboru **Globalne**, aby włączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne są odnoszone do globalnego układu współrzędnych, w przeciwnym razie są odnoszone do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md). {{Version/pl|0.20}}
-   Naciśnij **F** lub kliknij pole wyboru **Wypełniony**, aby przełączyć tryb wypełnienia. Jeśli tryb wypełnienia jest włączony, utworzony wielokąt będzie miał właściwość **Utwórz ścianę** ustawioną na wartość `True` i będzie miał wypełnioną ścianę.
-   Naciśnij **N** lub kliknij pole wyboru **Kontynuuj**, aby przełączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie uruchomi się ponownie po zakończeniu, umożliwiając dalsze tworzenie wielokątów.
-   Naciśnij **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij **Esc** lub przycisk **Zamknij**, aby przerwać wykonywanie polecenia.



## Uwagi

-   Wielokąt foremny środowiska Rysunek Roboczy można edytować za pomocą polecenia [Edycja](Draft_Edit/pl.md).



## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Ustawienia](Draft_Preferences/pl.md).

-   Jeśli **Edycja → Preferencje ... → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Użyj prymitywów części, gdy są dostępne**, polecenie utworzy [Wielokąt foremny](Part_RegularPolygon/pl.md) środowiska Część zamiast wielokąta środowiska Rysunek Roboczy.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Wielokąt foremny środowiska Rysunek Roboczy wywodzi się z obiektu [Część: Part2DObject](Part_Part2DObject/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Rysunek Roboczy}}

-    **Obszar|Area**: *(tylko do odczytu)* określa obszar ściany wielokąta. Wartość będzie wynosić {{value|0.0}} jeśli włsściwość **Utwórz ścianę** ma wartość {{FALSE/pl}}.

-    **Promień sfazowania|Length**: określa długość faz w narożnikach wielokąta.

-    **Tryb kreślenia|Enumeration**: określa, czy wielokąt jest {{value|wpisany}} w okrąg lub {{value|opisany}} okręgiem.

-    **Liczba ścian|Integer**: określa liczbę boków wielokąta.

-    **Promień zaokrąglenia|Length**: określa promień zaokrąglenia w rogach wielokąta.

-    **Utwórz ścianę|Bool**: określa, czy wielokąt tworzy ścianę, czy nie. Jeśli ma wartość {{TRUE/pl}}, tworzona jest ściana, w przeciwnym razie tylko kontur jest uważany za część obiektu.

-    **Promień|Length**: określa promień okręgu definiującego wielokąt.



### Widok


{{TitleProperty|Rysunek Roboczy}}

-    **Wzór|Enumeration**: określa [Wzór](Draft_Pattern/pl.md), którym ma zostać wypełniona ściana wielokąta. Ta właściwość działa tylko jeśli właściwość **Utwórz ścianę** ma wartość `True` i jeśli właściwość **Tryb wyświetlania** ma wartość {{value|Cieniowany z krawędziami}}.

-    **Rozmiar wzoru|Float**: określa rozmiar [Wzoru](Draft_Pattern/pl.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć **Wielokąt foremny** środowiska Rysunek Roboczy użyj metody `make_polygon` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makePolygon`.


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```

-   Tworzy obiekt `wielokąt` z podaną liczbą ścian (`nfaces`) i oparty na `promieniu` okręgu w milimetrach.
-   Jeśli włściwość `wpisany` ma wartość {{True/pl}}, wielokąt zostanie wpisany w okrąg, w przeciwnym razie zostanie opisany.
-   Jeśli włściwość `umiejscowienie` ma wartość `Brak`, wielokąt zostanie utworzony w punkcie początkowym, a jeden z jego wierzchołków będzie leżał na osi X.
-   Jeśli włściwość `ściana` ma wartość {{True/pl}}, wielokąt utworzy ścianę, czyli będzie wyglądał na wypełniony.

Przykład: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(4, radius=500)
polygon2 = Draft.make_polygon(5, radius=750)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

Polygon3 = Draft.make_polygon(6, radius=1450, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Polygon/pl
