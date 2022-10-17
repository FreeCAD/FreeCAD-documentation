---
- GuiCommand   */pl
   Name   *Draft Trimex
   Name/pl   *Rysunek Roboczy   * Przytnij
   MenuLocation   *Modyfkacja → Przytnij
   Workbenches   *[Rysunek Roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Shortcut   ***T** **R**
   SeeAlso   *[Part   * Wyciągnij](Part_Extrude.md)
---

# Draft Trimex/pl

## Opis

Narzędzie <img alt="" src=images/Draft_Trimex.svg  style="width   *24px;"> **Przytnij** przycina lub wydłuża [Linie](Draft_Line/pl.md) i [Polilinie](Draft_Wire/pl.md) tak, że ich koniec znajduje się na przecięciu z inną linią lub krawędzią.

Polecenie <img alt="" src=images/Draft_Trimex.svg  style="width   *24px;"> **Przytnij** [przycina lub rozszerza](#Przytnij_lub_rozszerz.md) wybrany obiekt. Przecięcia z krawędzią innego obiektu mogą być użyte do określenia nowych punktów końcowych. Polecenie może być również użyte do [wyciągnięcia](#Wyciągnij.md) ściany, w którym to przypadku tworzy obiekt [wyciągnięcia](Part_Extrude/pl.md).

<img alt="" src=images/Draft_trimex_example.jpg  style="width   *400px;"> 
*Wyżej   * Przedłużony odcinek linii, następnie przycięty odcinek linii. Niżej   * Powierzchnia wyciągnięta w bryłę*

## Przytnij lub rozszerz 

## Użycie

1.  Opcjonalnie wybierz jeden obiekt. Musi to być obiekt środowiska Rysunek Roboczy [Linia](Draft_Line/pl.md), [Linia łamana](Draft_Wire/pl.md), [Łuk](Draft_Arc/pl.md) lub [Okrąg](Draft_Line/pl.md) *(tylko te mogą być tylko przycinane)*. Jeśli wybrany obiekt jest zamknięty, musi mieć ustawioną właściwość **Make Face** na wartość `False`.
2.  Istnieje kilka sposobów na wywołanie polecenia   *
    -   Naciśnij przycisk **<img src="images/Draft_Trimex.svg" width=16px> [Przytnij](Draft_Trimex/pl.md)**.
    -   Wybierz z menu opcję **Modyfikacja → <img src="images/Draft_Trimex.svg" width=16px> Przytnij / Wydłuż**.
    -   Użyj skrótu klawiaturowego   * **T**, a następnie **R**.
3.  Jeśli nie wybrałeś jeszcze obiektu   * wybierz obiekt w oknie [widoku 3D](3D_view/pl.md).
4.  Otworzy się panel zadań **Przytnij / wydłuż**. Zobacz akapit [Opcje](#Opcje.md), aby uzyskać więcej informacji.
5.  Przesuń kursor w oknie [widoku 3D](3D_view/pl.md) tak, aby podgląd odpowiadał żądanemu rezultatowi. W razie potrzeby użyj klawiszy modyfikatorów, jak wyjaśniono w punkcie [Opcje](#Opcje.md).
6.  Wykonaj jedną z następujących czynności   *
    -   Wybierz punkt w oknie [widoku 3D](3D_view/pl.md)
    -   Wprowadź **Odległość** lub **Kąt**. Odległość jest odległością delta. Ta opcja nie działa, jeśli używane są klawisze modyfikatorów.
    -   Przesuń kursor nad krawędź należącą do innego obiektu i kliknij, gdy ta krawędź zostanie podświetlona, aby przyciąć lub wydłużyć wybrany obiekt, używając przecięcia z podświetloną krawędzią jako nowego punktu końcowego. Podczas ucinania rzut punktu, w którym krawędź tnąca jest zaznaczona, na obiekt, który ma zostać ucięty, określa wynik domyślny. Zauważ, że [przyciąganie](Draft_Snap/pl.md) może mieć tutaj niepożądany wpływ. W niektórych przypadkach może być konieczne tymczasowe wyłączenie tej funkcjonalności.

### Opcje

Wspomniane tutaj skróty klawiaturowe mogą być zmienione. Zobacz stronę [Rysunek Roboczy   * Preferencje](Draft_Preferences/pl.md).

-   Przytrzymaj **Alt** aby odwrócić domyślny kierunek polecenia.
-   Przytrzymaj **Shift** by ograniczyć operację do bieżącego segmentu [linii łamanej](Draft_Wire/pl.md).
-   Naciśnij klawisz **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).

Poniżej znajduje się przykład wyjaśniający działanie klawiszy modyfikatorów. Lewa lub dolna krawędź kształtu-U linii łamanej została wysunięta. Wszystkie rodzaje [przyciągania](Draft_Snap/pl.md) zostały wyłączone.

![](images/Draft_Trimex_example2.png )

1.  Łuk został kliknięty w pobliżu lewego dolnego rogu linii. Jest to zachowanie domyślne.
2.  Klawisz **Alt** został przytrzymany, gdy łuk został kliknięty w pobliżu lewego dolnego rogu linii.
3.  Wciśnięto klawisz **Y**, a po najechaniu na lewą krawędź wciśnięto klawisz **Shift** i kliknięto na łuk. Naciśnięcie przycisku **Y** jest wymagane tylko w przypadku krawędzi, które są mniej więcej równoległe do osi Y.

## Wyciągnij

## Użycie 

Zobacz także strony   * [Rysunek Roboczy   * Przyciąganie](Draft_Snap/pl.md) i [Rysunek Roboczy   * Wiązania](Draft_Constrain/pl.md).

1.  Pomocna może być najpierw zmiana [Płaszczyzny roboczej rysunku](Draft_SelectPlane/pl.md) tak, by nie była współliniowa z powierzchnią, którą chcesz wyciągnąć.
2.  Opcjonalnie wybierz pojedynczą ścianę lub obiekt z pojedynczą ścianą.
3.  Istnieje kilka sposobów na wywołanie tego polecenia   *
    -   Naciśnij przycisk **<img src="images/Draft_Trimex.svg" width=16px> [Przytnij / wydłuż](Draft_Trimex/pl.md)**.
    -   Wybierz z menu opcję **Modifikacja → <img src="images/Draft_Trimex.svg" width=16px> Przytnij / wydłuż**.
    -   Użyj skrótu klawiaturowego   * **T**, a następnie **R**.
4.  Jeśli nie wybrałeś jeszcze obiektu lub ściany   * wybierz obiekt z pojedynczą ścianą w oknie [widoku 3D](3D_view/pl.md).
5.  Otworzy się panel zadań **Przytnij / wydłuż**. Zobacz [Opcje](#Opcje_2.md), aby uzyskać więcej informacji.
6.  Aby zdefiniować kierunek i odległość wyciągania, wykonaj jedną z poniższych czynności   *
    -   Wybierz punkt w oknie [widoku 3D](3D_view/pl.md), który nie leży na tej samej płaszczyźnie co ściana.
    -   Upewnij się, że kursor znajduje się po właściwej stronie ściany w [widoku 3D](3D_view.md) i wprowadź **Odległość**.

### Opcje 

Wspomniane tutaj klawisze modyfikatorów mogą zostać zmienione. Zobacz stronę [Rysunek Roboczy   * Preferencje](Draft_Preferences/pl.md).

-   Przytrzymaj klawisz **Shift**, by uzyskać wyciągnięcie w kierunku, który nie jest równoległy do wektora normalnego ściany.

## Ustawienia

Zobacz także strony   * [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy   * Preferencje](Draft_Preferences/pl.md).

-   Aby zmienić liczbę miejsc po przecinku używanych do wprowadzania odległości   * **Edycja → Preferencje... → Ogólne → Jednostki → Ustawienia jednostek → Liczba cyfr po przecinku**.

## Tworzenie skryptów 

Zobacz również stronę   * [Dokumentacja API generowana automatycznie](https   *//freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Dla narzędzia Przytnij nie ma dostępnego interfejsu programistycznego. Do wyciągania obiektów służy metoda `extrude` modułu Rysunek Roboczy.


```python
extrusion = extrude(obj, vector, solid=False)
```

-    `obj`to obiekt, który ma zostać wyciągnięty.

-    `vector`to kierunek i odległość wyciskania.

-   Jeśli `solid` ma wartość `True`, to zamiast powłoki zostanie utworzona bryła.

-    `extrusion`jest zwracana wraz z utworzonym obiektem.

Przykład   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(1500, 500)
doc.recompute()

vector = App.Vector(0, 0, 300)
solid = Draft.extrude(rectangle, vector, solid=True)
doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Trimex/pl
