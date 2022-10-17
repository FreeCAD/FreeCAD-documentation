---
- GuiCommand   */pl
   Name/pl   *Draft   * Move
   Name   *Draft Move
   MenuLocation   *Modyfikacja → Przesuń
   Workbenches   *[Rysunek roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Shortcut   ***M** **V**
   Version   *0.7
   SeeAlso   *[Podświetl element podrzędny](Draft_SubelementHighlight/pl.md)
---

# Draft Move/pl

## Opis

Polecenie <img alt="" src=images/Draft_Move.svg  style="width   *24px;"> **Draft   * Przesuń** - przesuwa lub kopiuje wybrane obiekty z jednego punktu do drugiego. W trybie elementu podrzędnego polecenie przesuwa wybrane punkty i krawędzie, lub kopiuje wybrane krawędzie [Linii](Draft_Line/pl.md) i [Polilinii](Draft_Wire/pl.md).

Narzędzie Przesuń może być używane na obiektach 2D utworzonych za pomocą środowisk pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale może być również używane dla wielu typów obiektów 3D, takich jak te utworzone za pomocą środowisk pracy [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md).

<img alt="" src=images/Draft_Move_example.jpg  style="width   *400px;"> 
*Przemieszczanie obiektu z jednego punktu do innego*

## Użycie

Zobacz także strony   * [Rysunek Roboczy   * Przyciąganie](Draft_Snap/pl.md) i [Rysunek Roboczy   * Wiązania](Draft_Constrain/pl.md).

1.  Opcjonalnie wybierz jeden lub więcej obiektów, albo jeden lub więcej elementów podrzędnych typu [linia](Draft_Line/pl.md) lub [polilinia](Draft_Wire/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia   *
    -   Naciśnij przycisk **<img src="images/Draft_Move.svg" width=16px> [Przesuń](Draft_Move/pl.md)**.
    -   Wybierz z menu opcję **Modyfikacja → <img src="images/Draft_Move.svg" width=16px> Przesuń**.
    -   Użyj skrótu klawiaturowego   * **M**, a następnie **V**.
3.  Jeśli nie zaznaczyłeś jeszcze żadnego obiektu   * wybierz obiekt w oknie [widoku 3D](3D_view/pl.md).
4.  Otworzy się panel zadań **Przesuń**. Zobacz [Opcje](#Opcje.md), aby uzyskać więcej informacji.
5.  Jeśli zostały wybrane elementy podrzędne   * zaznacz pole wyboru **Modyfikuj elementy podrzędne**, aby włączyć tryb elementów podrzędnych.
6.  Wybierz pierwszy punkt, punkt bazowy, w oknie widoku [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
7.  Wybierz drugi punkt, punkt docelowy, w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px>. Wprowadź punkt**.

## Opcje

Wspomniane tutaj skróty klawiaturowe mogą być zmienione. Zobacz stronę [Rysunek Roboczy   * Preferencje](Draft_Preferences/pl.md).

-   Aby ręcznie wprowadzić współrzędne, wprowadź składowe X, Y i Z, i naciśnij klawisz **Enter** po każdej z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy masz już żądane wartości. Wskazane jest, aby przed wprowadzeniem współrzędnych wysunąć kursor poza okno [widoku 3D](3D_view/pl.md).
-   Aby użyć współrzędnych biegunowych, wprowadź wartość dla **Długość** i wartość w polu **Kąt**, a następnie naciśnij klawisz **Enter** po każdym z nich.
-   Zaznacz pole wyboru **Kąt**, aby ograniczyć kursor do określonego kąta.
-   Naciśnij **H**, aby zmienić aktywność z pola wprowadzania **X** na pole wprowadzania **Długość** i z powrotem. W zależności od pola wejściowego, które jest aktywne, pole wyboru **Kąt** jest zaznaczane lub odznaczane.
-   Naciśnij klawisz **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne drugiego punktu są zależne od pierwszego punktu, w przeciwnym razie są odniesione do początku układu współrzędnych.
-   Naciśnij klawisz **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne są odniesione do globalnego układu współrzędnych, w przeciwnym razie są one odniesione do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md). {{Version/pl|0.20}}
-   Naciśnij klawisz **T** lub kliknij pole wyboru **Kontynuuj**, aby przełączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie zostanie uruchomione ponownie po zakończeniu. Ten tryb naprawdę ma sens tylko wtedy, gdy włączony jest tryb kopiowania. W zależności od preferencji **Zaznacz obiekty bazowe po skopiowaniu**, albo oryginalne obiekty są wybierane do następnego wywołania polecenia, albo kopie, które zostały utworzone jako ostatnie. Zobacz [Preferencje](#Preferencje.md).
-   Naciśnij klawisz **P** lub kliknij pole wyboru **Kopiuj**, aby przełączyć tryb kopiowania. Jeśli tryb kopiowania jest włączony, polecenie utworzy przeniesione kopie zamiast przenoszenia oryginalnych obiektów.
-   Naciśnij przycisk **D** lub kliknij pole wyboru **Modifikuj elementy podrzędne**, aby przełączyć tryb elementów podrzędnych. Jeśli tryb elementów podrzędnych jest włączony, polecenie będzie używać wybranych elementów podrzędnych zamiast całych obiektów. Elementy podrzędne muszą należeć do [Linii](Draft_Line/pl.md) lub [Polilinii](Draft_Wire/pl.md).
-   Jeśli tryb kopiowania i tryb elementów podrzędnych są włączone, a krawędzie [Polilinii](Draft_Wire/pl.md) są zaznaczone, nowe linie zostaną utworzone z tych krawędzi.
-   Przytrzymanie klawisza **Alt** po wybraniu punktu bazowego spowoduje również przełączenie trybu kopiowania. Gdy trzymasz klawisz **Alt** wciśnięty, możesz wybrać wiele punktów docelowych. Puść klawisz **Alt**, aby zakończyć polecenie i zobaczyć utworzone kopie.
-   Naciśnij **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij klawisz **Esc** lub przycisk **Zamknij**, aby przerwać wykonywanie polecenia.

## Uwagi

-   Obiekt, który jest [umocowany](Part_EditAttachment/pl.md) nie może być przeniesiony za pomocą polecenia Przesuń. Aby go przesunąć, należy przesunąć jego obiekt {{PropertyData/pl|podparcia}} lub zmienić jego {{PropertyData/pl|przesunięcie umocowania}}.

## Ustawienia

Zobacz także strony   * [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy   * Preferencje](Draft_Preferences/pl.md).

-   Aby zmienić liczbę miejsc po przecinku używanych do wprowadzania współrzędnych, długości i kątów   * **Edycja → Preferencje → Ogólne → Jednostki → Ustawienia jednostek → Liczba cyfr po przecinku**.
-   Aby zmienić początkową pozycję z panelu zadań na pole wprowadzania **Długość**   * **Edycja → Preferencje... → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Ustaw fokus na Długość zamiast Współrzędnej X**. Należy pamiętać, że aby zmiana zaczęła obowiązywać, należy przesunąć kursor w oknie [widoku 3D](3D_view/pl.md).
-   Aby zachować i ponownie wykorzystać to samo ustawienie trybu kopiowania w różnych poleceniach   * **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Tryb kopiowania globalny**.
-   Aby ponownie wybrać obiekty bazowe po skopiowaniu obiektów   * **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Zaznacz obiekty bazowe po skopiowaniu**.

## Tworzenie skryptów 

Zobacz również stronę   * [Dokumentacja API generowana automatycznie](https   *//freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Do przesuwania obiektów służy metoda `move` środowiska Rysunek Roboczy.


```python
moved_list = move(objectslist, vector, copy=False)
```

-    `objectslist`zawiera obiekty, które mają zostać przeniesione. Może to być pojedynczy obiekt lub lista obiektów.

-    `vector`wskazuje przemieszczenie.

-   Jeśli `copy` ma wartość `True`, to zamiast przesuwania oryginalnych obiektów tworzone są ich kopie.

-   Lista `moved_list` jest zwracana z oryginalnymi przeniesionymi obiektami lub z nowymi kopiami. Jest to albo pojedynczy obiekt, albo lista obiektów, w zależności od `objectslist`.

Przykład   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon2, App.Vector(1000, -1000, 0))
Draft.move(polygon3, App.Vector(-500, -500, 0))

list1 = [polygon1, polygon2, polygon3]

vector = App.Vector(-2000, -2000, 0)
list2 = Draft.move(list1, vector, copy=True)
list3 = Draft.move(list1, -2*vector, copy=True)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Move/pl
