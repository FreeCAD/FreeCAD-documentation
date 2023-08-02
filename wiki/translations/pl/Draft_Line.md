---
- GuiCommand:
   Name: Draft Line
   Name/pl: Rysunek roboczy: Linia
   MenuLocation: Kreślenie -> Linia
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **L** **I**
   Version: 0.7
   SeeAlso: Draft_Wire/pl
---

# Draft Line/pl

## Opis

Polecenie <img alt="" src=images/Draft_Line.svg  style="width:24px;"> **Linia** środowiska Rysunek Roboczy, tworzy linię prostą.

Linia środowiska Rysunek Roboczy jest w rzeczywistości [polilinią](Draft_Wire/pl.md) z tylko dwoma punktami.

<img alt="" src=images/Draft_Line_example.jpg  style="width:400px;"> 
*Linia utworzona przez dwa punkty*

## Użycie

Zobacz również [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Line.svg" width=16px> [Utwórz linię ...](Draft_Line.md)**.
    -   Wybierz z menu opcję **Kreślenie → <img src="images/Draft_Line.svg" width=16px> Linia** opcję z menu.
    -   Użyj skrótu klawiaturowego: **L**, a następnie **I**.
2.  Otworzy się panel zadań **Linia**. Aby uzyskać więcej informacji, zobacz [Opcje](#Opcje.md).
3.  Wybierz pierwszy punkt w oknie [widoku 3D](3D_view/pl.md), lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px>. Wprowadź punkt**.
4.  Wybierz drugi punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px>. Wprowadź punkt**.

## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi.

-   Aby ręcznie wprowadzić współrzędne, wprowadź składowe X, Y i Z, i naciśnij klawisz **Enter** po każdej z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy masz już żądane wartości. Wskazane jest, aby przed wprowadzeniem współrzędnych wysunąć kursor poza okno [widoku 3D](3D_view/pl.md).
-   Aby użyć współrzędnych biegunowych, wprowadź wartość dla **Długości** i wartość dla **Kąta**, a następnie naciśnij klawisz **Enter** po każdej z nich.
-   Zaznacz pole wyboru **kąt**, aby związać kursor do określonego kąta. Aby funkcja działała, pole wejściowe **Długość** musi przyjmować wartość niezerową.
-   Naciśnij klawisz **H**, aby zmienić aktywność z pola wprowadzania **X** na pole wprowadzania **Długość** i z powrotem. W zależności od pola wejściowego, które otrzymuje aktywność, pole wyboru **Kąt** jest zaznaczane lub odznaczane.
-   Naciśnij klawisz **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne drugiego punktu odnoszą się do pierwszego punktu, w przeciwnym razie odnoszą się do początku układu współrzędnych.
-   Naciśnij klawisz **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne odnoszą się do głównego układu współrzędnych, w przeciwnym razie do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md). {{Version/pl|0.20}}
-   Naciśnij klawisz **T** lub kliknij pole wyboru **Kontynuuj**, aby przełączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie uruchomi się ponownie po zakończeniu, pozwalając Ci kontynuować tworzenie linii.
-   Naciśnij klawisz **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij klawisz **Esc** lub przycisk **Zamknij**, aby przerwać polecenie.

## Uwagi

-   Linia może być edytowana za pomocą polecenia [Edytuj aktywny obiekt](Draft_Edit.md).
-   Linie środowiska Rysunek Roboczy oraz [polilinie](Draft_Wire/pl.md) można łączyć za pomocą polecenia [Utwórz wielopunktowa linię \...](Draft_Wire/pl.md), polecenia [Połącz zaznaczone linie](Draft_Join/pl.md) lub polecenia [Ulepsz kształt](Draft_Upgrade/pl.md).

## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Preferencje](Draft_Preferences/pl.md).

-   Aby zmienić liczbę miejsc po przecinku używanych do wprowadzania wartości współrzędnych długości i kątów: **Edycja → Preferencje → Ogólne → Jednostki → Ustawienia jednostek → Liczba cyfr po przecinku**.
-   Aby zmienić wartość początkową trybu wypełnienia: **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Wypełniaj obiekty powierzchniami, gdy tylko jest to możliwe**. Zmiana trybu wypełnienia w panelu zadań spowoduje nadpisanie tych preferencji dla bieżącej sesji programu FreeCAD.
-   Jeśli opcja **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Używaj elementów pierwotnych, gdy jest to możliwe** jest zaznaczona, polecenie utworzy [Linia](Part_Line/pl.md) środowiska Część, zamiast środowiska Rysunek Roboczy.

## Właściwości

Zobacz stronę [polilinia](Draft_Wire/pl#W.C5.82a.C5.9Bciwo.C5.9Bci.md).

## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć linię użyj metody `make_line` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeLine`.


```python
line = make_line(p1, p2)
line = make_line(LineSegment)
line = make_line(Shape)
```

-   Tworzy obiekt `Line` pomiędzy punktami `p1` oraz `p2`, każdy zdefiniowany przez jego `FreeCAD.Vector`, z jednostkami w milimetrach.
-   Tworzy obiekt `Line` z `Part.LineSegment`.
-   Tworzy obiekt `Line` od pierwszego do ostatniego wierzchołka danego `Shape`.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 500, 0)
p3 = App.Vector(-250, -500, 0)
p4 = App.Vector(500, 1000, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p3, p4)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Line/pl
