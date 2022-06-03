---
- GuiCommand   */pl
   Name   *Draft Downgrade
   Name/pl   *Rysunek Roboczy   * Rozbij kształt
   MenuLocation   *Modyfikacja → Rozbij kształt
   Workbenches   *[Rysunek Roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Shortcut   ***D** **N**
   SeeAlso   *[Ulepsz kształt](Draft_Upgrade/pl.md), [Wytnij](Part_Cut/pl.md)
---

# Draft Downgrade/pl

## Opis

Narzędzie **<img src="images/Draft_Downgrade.svg" width=16px> [Rozbij kształt](Draft_Downgrade.md)** obniża stopień szczegółowości wybranych obiektów na różne sposoby. Inaczej mówiąc rozbija obiekty do elementów podstawowych, np bryły do wielokątów, kształty do linii.

Polecenie <img alt="" src=images/Draft_Downgrade.svg  style="width   *24px;"> **Rozbij kształt** spowoduje rozbicie wybranych obiektów. Wynik zależy od liczby wybranych obiektów i ich typu. Polecenie może na przykład zdekomponować bryłę 3D na osobne ściany, a linie łamaną na osobne krawędzie. Jeśli wybrane są dwie ściany, to tworzony jest z nich obiekt środowiska Część - [Wytnij](Part_Cut/pl.md). Zauważ, że nie wszystkie obiekty mogą zostać zdekomponowane. To polecenie jest odpowiednikiem polecenia środowiska Rysunek Roboczy [Ulepsz](Draft_Upgrade/pl.md).

<img alt="" src=images/Draft_Downgrade_example.jpg  style="width   *400px;"> 
*Dwie nakładające się powierzchnie są degradowane do obiektu Part Cut, który jest degradowany do powierzchni. Ta ściana jest następnie zdekomponowana do zamkniętej linii łamanej, która jest ostatecznie rozbita do oddzielnych krawędzi.*

## Użycie

1.  Opcjonalnie wybierz jeden lub więcej obiektów.
2.  Polecenie można wywołać na kilka sposobów   *
    -   Naciśnij przycisk **<img src="images/Draft_Downgrade.svg" width=16px> [Rozbij kształt](Draft_Downgrade/pl.md)**,
    -   Z menu wybierz opcję **Modyfikacja → <img src="images/Draft_Downgrade.svg" width=16px> Rozbij kształt
**
    -   Użyj skrótu klawiszowego **D**, a następnie **N**,
3.  Jeśli nie wybrałeś jeszcze obiektu   * wybierz obiekt w oknie [widoku 3D](3D_view/pl.md).

## Tworzenie skryptów 

Zobacz również   * [Dokumentacja API generowana automatycznie](https   *//freecad.github.io/SourceDoc/) oraz

[Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Do obracania obiektów służy metoda `downgrade` środowiska Rysunek Roboczy.


```python
downgrade_list = downgrade(objects, delete=False, force=None)
```

-    `objects`zawiera obiekty, które mają zostać zdegradowane. Może to być pojedynczy obiekt lub lista obiektów.

-   Jeśli parametr `delete` ma wartość `True`, obiekty źródłowe są usuwane.

-    `force`wymusza określony sposób obniżania klasyfikacji poprzez wywołanie określonej funkcji wewnętrznej. Może to być   * `"explode"`, `"shapify"`, `"subtr"`, `"splitFaces"`, `"cut2"`, `"getWire"`, `"splitWires"` lub `"splitCompounds"`.

-   Zwracana jest lista `downgrade_list`. Jest to lista zawierająca dwie listy   * listę nowych obiektów i listę obiektów do usunięcia. Jeśli parametr `delete` ma wartość `True`, to druga lista jest pusta.

### Przykład   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle = Draft.make_circle(1000)
rectangle = Draft.make_rectangle(2000, 800)
doc.recompute()

add_list1, delete_list1 = Draft.upgrade([circle, rectangle], delete=True)

compound = add_list1[0]
add_list2, delete_list2 = Draft.downgrade(compound, delete=False)
face = add_list2[0]
add_list3, delete_list3 = Draft.downgrade(face, delete=False)

box = doc.addObject("Part   *   *Box", "Box")
box.Length = 2300
box.Width = 800
box.Height = 1000

add_list4, delete_list4 = Draft.downgrade(box, delete=True)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Downgrade/pl
