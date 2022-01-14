---
- GuiCommand:/pl
   Name:Draft Offset
   Name/pl:Rysunek Roboczy: Odsunięcie
   MenuLocation:Modyfikacja → Odsunięcie
   Workbenches:[Rysunek Roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Shortcut:**O** **S**
   SeeAlso:[Odsunięcie 2D](Part_Offset2D/pl.md)
---

# Draft Offset/pl

## Opis

Narzędzie <img alt="" src=images/Draft_Offset.svg  style="width:24px;"> **Odsunięcie** przesuwa każdy segment wybranego obiektu o zadaną odległość lub tworzy przesuniętą kopię wybranego obiektu.

<img alt="" src=images/Draft_Offset_example.jpg  style="width:400px;"> 
*Odsunięcie linii łamanej*

## Użycie

Zobacz także strony: [Rysunek Roboczy: Przyciąganie](Draft_Snap/pl.md) i [Rysunek Roboczy: Wiązania](Draft_Constrain/pl.md).

1.  Opcjonalnie wybierz jeden obiekt. Obiekt musi leżeć na aktualnej [płaszczyźnie roboczej](Draft_SelectPlane/pl.md).
2.  Istnieje kilka sposobów, aby wywołać to polecenie:
    -   Naciśnij przycisk **<img src="images/Draft_Offset.svg" width=16px> [Odsuń](Draft_Offset/pl.md)**.
    -   Wybierz z menu opcję **Modifikacja → <img src="images/Draft_Offset.svg" width=16px> Odsunięcie**.
    -   Użyj skrótu klawiaturowego: **O**, a następnie **S**.
3.  Jeśli nie wybrałeś jeszcze obiektu: wybierz obiekt w oknie [widoku 3D](3D_view/pl.md).
4.  Otwiera się panel zadań **Odsunięcie**. Zobacz [Opcje](#Opcje.md), aby uzyskać więcej informacji.
5.  Aby zdefiniować odległość przesunięcia, wykonaj jedną z poniższych czynności:
    -   Wybierz punkt w oknie [widoku 3D](3D_view/pl.md)
    -   Wprowadź wartość:
        1.  Upewnij się, że kursor znajduje się po właściwej stronie obiektu w oknie [widoku 3D](3D_view/pl.md).
        2.  Nie wysuwaj kursora poza okno [widoku 3D](3D_view/pl.md).
        3.  Wprowadź **Dystans**.
        4.  Naciśnij klawisz **Enter** aby zakończyć polecenie.

## Opcje

Wspomniane tutaj skróty klawiaturowe mogą być zmienione. Zobacz stronę [Rysunek Roboczy: Preferencje](Draft_Preferences/pl.md).

-   Jeśli pole wyboru **Odsunięcie w stylu OpenCascade** jest zaznaczone, używany jest specjalny styl odsunięcia: otwarte [polilinie](Draft_Wire/pl.md) są odsunięte po obu stronach, a nowe krawędzie są łączone z zaokrąglonymi rogami. Działa to tylko dla planarnych obiektów Rysunku roboczego z co najmniej dwoma prostymi krawędziami. Zauważ, że przy tym stylu tworzony jest nowy obiekt nieparametryczny, a jeśli tryb kopiowania jest wyłączony, oryginalny obiekt jest usuwany.
-   Naciśnij **P** lub kliknij pole wyboru **Copy**, aby przełączyć tryb kopiowania. Jeśli tryb kopiowania jest włączony, polecenie utworzy kopię z przesunięciem zamiast przesunięcia oryginalnego obiektu.
-   Przytrzymanie klawisza **Alt** przed wybraniem punktów w oknie [widoku 3D](3D_view/pl.md) również przełączy tryb kopiowania. Gdy klawisz **Alt** jest przytrzymany, można wybrać wiele punktów przesunięcia. Aby zakończyć polecenie i zobaczyć utworzone kopie, należy puścić klawisz **Alt**.
-   Przytrzymaj klawisz **Shift**, aby zachować odległość przesunięcia związaną z bieżącym segmentem.
-   Naciśnij klawisz **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij klawisz **Esc** lub przycisk **Zamknij**, aby zakończyć polecenie.

## Uwagi

-   Aby utworzyć przesuniętą wersję [krzywą złożoną](Draft_BSpline/pl.md), jej punkty są przesuwane indywidualnie, a z nowych punktów obliczana jest nowa krzywa złożona. Ta nowa krzywa nie jest równoległa do krzywej oryginalnej. Aby uzyskać dokładne przesunięcie równoległe [krzywej złożonej](Draft_BSpline/pl.md) należy użyć polecenia [Part: Odsunięcie 2D](Part_Offset2D/pl.md).
-   Polecenie nie radzi sobie z [krzywą Beziera](Draft_BezCurve/pl.md). Zamiast niego użyj polecenia [Part: Odsunięcie 2D](Part_Offset2D/pl.md).

## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Preferencje](Draft_Preferences/pl.md).

-   Aby zmienić liczbę miejsc po przecinku używanych do wprowadzania odległości: **Edycja → Preferencje → Ogólne → Jednostki → Ustawienia jednostek → Liczba cyfr po przecinku**.

## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby odsunąć obiekty należy użyć metody `offset` modułu Rysunek Roboczy. Metoda ta może obsługiwać tylko obiekty typu[polilinia](Draft_Wire/pl.md), [okrąg](Draft_Circle/pl.md), [prostokąt](Draft_Rectangle/pl.md), [wielokąt](Draft_Polygon/pl.md) i [linia złożona](Draft_BSpline/pl.md).


```python
offset_obj = offset(obj, delta, copy=False, bind=False, sym=False, occ=False)
```

-    `obj`to obiekt, który ma zostać odsunięty.

-    `delta`zawiera informacje o odsunięciu:

    -   Dla [polilinii](Draft_Wire/pl.md), [prostokątów](Draft_Rectangle/pl.md) i [wielokątów](Draft_Polygon/pl.md) jest to wektor przesunięcia, który musi być prostopadły do pierwszego segmentu obiektu.
    -   Dla [okręgu](Draft_Circle/pl.md) jest to nowy promień.
    -   Dla [linii złożonej](Draft_BSpline/pl.md) jest to lista nowych punktów.

-   Jeśli wartość opcji `copy` wynosi `True`, oryginalny obiekt jest zachowywany i tworzony jest nowy obiekt.

-   Jeśli wartość opcji `bind` wynosi `True`, tworzona jest ściana poprzez połączenie kształtu oryginalnego obiektu z kształtem jego odsunięcia. Działa to tylko dla otwartych [polilinii](Draft_Wire/pl.md).

-   Jeśli wartość parametru `sym` wynosi `True`, a wartość parametru `bind` również wynosi `True`, to odsunięcie jest wykonywane po obu stronach oryginalnego obiektu, a całkowita szerokość jest równa długości podanego wektora. Działa to tylko dla otwartych [polilinii](Draft_Wire/pl.md).

-   Jeśli wartość parametru `occ` wynosi `True` używane jest odsunięcie w stylu OCC. Zobacz [Opcje](#Opcje.md). Jeśli wartość parametru `occ` wynosi `True`, argumenty `bind` i `sym` są ignorowane.

-    `offset_obj`jest zwracany z oryginalnym obiektem odsunięcia, lub z nowym obiektem. Jeśli wartość parametru `bind` wynosi `True` lub wartość parametru `occ` wynosi `True`, to nowy obiekt jest obiektem `[Część: Cecha](Part_Feature/pl.md)`.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1500, 2000, 0)
p3 = App.Vector(4000, 0, 0)

wire = Draft.make_wire([p1, p2, p3])
doc.recompute()

vector = App.Vector(-200, 150, 0)
offset1 = Draft.offset(wire, vector, copy=True, bind=True, sym=True)
offset2 = Draft.offset(wire, 3*vector, copy=True)
offset3 = Draft.offset(wire, 6*vector, copy=True)
offset4 = Draft.offset(wire, 9*vector, copy=True)
offset5 = Draft.offset(wire, 1.5*vector, copy=True, occ=True)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Offset/pl
