---
 GuiCommand:
   Name: Draft Arc 3Points
   Name/pl: Rysunek Roboczy: Łuk przez trzy punkty
   MenuLocation: Kreślenie , Narzędzia łuku , Łuk przez trzy punkty
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **A** **R**
   Version: 0.7
   SeeAlso: Draft_Arc/pl, Draft_Circle/pl
---

# Draft Arc 3Points/pl



## Opis

Polecenie <img alt="" src=images/Draft_Arc_3Points.svg  style="width:24px;"> **Łuk przez trzy punkty** tworzy łuk kołowy w bieżącej [płaszczyźnie roboczej](Draft_SelectPlane/pl.md) z trzech punktów, które definiują jego obwód. Środek i promień są obliczane na podstawie tych punktów.

Łuk jest w rzeczywistości obiektem typu [okrąg](Draft_Circle/pl.md) z {{PropertyData/pl|kątem pierwszym}}, który nie jest taki sam jak jego {{PropertyData/pl|kąt drugi}}.

<img alt="" src=images/Draft_Arc_3Points_example.png  style="width:400px;"> 
*Łuk zdefiniowany przez trzy punkty na jego obwodzie.*



## Użycie

Zapoznaj się również z informacjami na stronie: [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_Arc_3Points.svg" width=16px> '''Łuk przez trzy punkty'''**.
    -   Wybierz z menu opcję **Kreślenie → Narzędzia łuku → <img src="images/Draft_Arc_3Points.svg" width=16px> Łuk przez trzy punkty**.
    -   Użyj skrótu klawiaturowego: **A**, a następnie **T**. {{Version/pl|0.20}}.
2.  Zostanie otwarty panel zadań **Łuk przez trzy punkty**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
3.  W oknie [widoku 3D](3D_view/pl.md) wybierz pierwszy punkt lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
4.  Wybierz drugi punkt w okine [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
5.  Wybierz trzeci punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.



## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi *(w wersji 0.22)*.

-   Aby ręcznie wprowadzić współrzędne, wprowadź element X, Y i Z i naciśnij **Enter** po każdym z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy uzyskasz żądane wartości. Zaleca się przesunięcie wskaźnika poza obszar okna [widoku 3D](3D_view/pl.md) przed wprowadzeniem współrzędnych.
-   Wciśnij **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne są odniesione do ostatniego punktu, jeśli jest dostępny, w przeciwnym razie są one względne do początku układu współrzędnych.
-   Naciśnij **G** lub kliknij pole wyboru **Globalne**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne odnoszą się do globalnego układu współrzędnych, w przeciwnym razie odnoszą się do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md). {{Version/pl|0.20}}
-   Naciśnij **N** lub kliknij pole wyboru **Kontynuuj**, aby włączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie uruchomi się ponownie po zakończeniu, umożliwiając dalsze tworzenie łuków. {{Version/pl|0.20}}
-   Naciśnij **S**, aby włączyć lub wyłączyć [Przyciąganie](Draft_Snap/pl.md).
-   Naciśnij **Esc** lub przycisk **Zamknij**, aby przerwać wykonywanie polecenia.



## Uwagi

-   Szkic łuku można edytować za pomocą polecenia [Edycja](Draft_Edit/pl.md).



## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Ustawienia](Draft_Preferences/pl.md).

-   Jeśli w oknie ustawień opcja **Edycja → Preferencje ... → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Używaj elementów pierwotnych, gdy jest to możliwe** jest zaznaczona, polecenie utworzy nieedytowalną [cechę](Part_Feature/pl.md) środowiska Część, zamiast okręgu środowiska Rysunek Roboczy.



## Właściwości

Zobacz stronę [Rysunek Roboczy: Okrąg](Draft_Circle/pl#W.C5.82a.C5.9Bciwo.C5.9Bci.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć **Łuk przez trzy punkty**, użyj metody `make_arc_3points` modułu Rysunek Roboczy:


```python
arc = make_arc_3points(points, placement=None, face=False, support=None, map_mode="Deactivated", primitive=False)
```

-   Tworzy obiekt `łuk` z podanej listy `punktów`.
-   Jeśli podano `umiejscowienie`, środek łuku kołowego zostanie przeniesiony do tego miejsca. Więcej informacji można znaleźć na stronie [Umiejscowienie](Placement/pl.md).
-   Jeśli parametr `ściana` ma wartość {{True/pl}}, łuk utworzy twarz, czyli będzie wyglądał na wypełniony.
-   Jeśli podano `podparcie`, jest to `LinkSubList`, czyli lista wskazująca obiekt i element podrzędny tego obiektu. Jest to używane w celu wyświetlenia obiektu z odniesieniem do tego wsparcia.

:   Na przykład: support=[(obj, („Face1”))].

-   Jeżeli podano `map_mode`, jest to ciąg znaków określający rodzaj mapowania, na przykład: map_mode='FlatFace', map_mode='ThreePointsPlane' itp. Zobacz [Edycja dołaczenia](Part_EditAttachment/pl.md), aby uzyskać więcej informacji.
-   Jeśli parametr `primitive` ma wartość {{True/pl}}, utworzony łuk będzie zwykłą [cechą](Part_Feature/pl.md) środowiska Część, a nie złożonym obiektem środowiska Rysunek Roboczy.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

points = [App.Vector(0, 0, 0),
          App.Vector(5, 10, 0),
          App.Vector(10, 0, 0)]

arc = Draft.make_arc_3points(points)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Arc 3Points/pl
