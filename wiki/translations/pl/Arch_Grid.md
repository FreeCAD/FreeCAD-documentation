---
 GuiCommand:
   Name: Arch Grid
   Name/pl: Architektura: Siatka
   MenuLocation: Opisy , Narzędzia osi , Siatka
   Workbenches: BIM_Workbench/pl
   SeeAlso: Arch_Axis/pl, Arch_AxisSystem/pl
---

# Arch Grid/pl



## Opis

Narzędzie **Siatka** pozwala na umieszczenie w dokumencie obiektu przypominającego siatkę. Obiekt ten ma służyć jako podstawa do budowania obiektów Architektury, które wymagają regularnej, ale złożonej ramy, takich jak okna, ściany osłonowe, siatki kolumn, balustrady itp. Obiekt Siatka jest edytowalny jak arkusz kalkulacyjny, w którym można dodawać lub usuwać kolumny i wiersze, definiować ich rozmiar i łączyć komórki.

Siatka jest obiektem 2D, a zatem może być używana wszędzie tam, gdzie potrzebny jest kształt 2D, taki jak [rysunek roboczy](Draft_Workbench/pl.md) lub [szkic](Sketcher_Workbench/pl.md), ale może również zachowywać się jak [układ osi](Arch_AxisSystem/pl.md) i być używana do umieszczania innych obiektów Architektury.

<img alt="" src=images/Arch_Grid_example.jpg  style="width:600px;"> 
*Układ kolumn, system balustrad i okno, każdy oparty na obiekcie [siatki](Arch_Grid/pl.md).*



## Użycie

1.  Naciśnij przycisk **<img src="images/Arch_Grid.svg" width=16px> '''Siatka'''**.
2.  Ustaw **Szerokość** i **Wysokość** siatki we właściwościach.
3.  Przejdź do trybu edycji, klikając dwukrotnie obiekt siatki w widoku drzewa.
4.  Dodaj wiersze i kolumny.
5.  Ustaw żądaną szerokość i wysokość wierszy i kolumn, klikając dwukrotnie nagłówki wierszy lub kolumn.



## Opcje

-   Szerokość kolumny lub wysokość wiersza równa 0 oznacza, że jej rozmiar zostanie automatycznie dostosowany do całkowitej szerokości / wysokości siatki.
-   Komórki można łączyć i rozdzielać, zaznaczając je i klikając odpowiedni przycisk.
-   W przypadku użycia jako właściwości **Oś** innych obiektów Architektury, siatka będzie sterować pozycjonowaniem tych obiektów. Właściwość **PPunkty wyjściowe** definiuje sposób, w jaki inne obiekty są umieszczane na siatce: W wierzchołkach, punktach środkowych krawędzi lub środkach ścian.
-   Ustawiając właściwości **Automatyczna wysokość** lub **Automatyczna szerokość** na wartość niezerową, całkowita liczba wierszy/kolumn i ich indywidualne wysokości/szerokości są ignorowane. Zamiast tego automatycznie tworzona jest maksymalna liczba kolumn lub wierszy o podanej automatycznej szerokości/wysokości.



## Właściwości

-    **Wiersze**: Ilość wierszy.

-    **Kolumny**: Ilość kolumn.

-    **Rozmiar Wierszy**: Rozmiary wierszy.

-    **Rozmiar Kolumn**: Rozmiary kolumn.

-    **Punkty wyjściowe**: Typ punktów 3D generowanych przez ten obiekt siatki.

-    **Szerokość**: Całkowita szerokość tej siatki.

-    **Wysokość**: Całkowita wysokość tej siatki.

-    **Szerokość automatycznie**: Tworzy automatyczne podziały kolumn *(ustaw na 0, aby wyłączyć)*.

-    **Wysokość automatycznie**: Tworzy automatyczne podziały wierszy *(ustaw na 0, aby wyłączyć)*.

-    **Reorient**: W trybie punktu środkowego krawędzi, określa czy ta siatka musi zmienić orientację swoich elementów podrzędnych wzdłuż normalnych krawędzi, czy nie.

-    **Ukryte ściany**: Indeksy ścian do ukrycia.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Siatka** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
Grid = makeGrid(name="Grid")
```

-   Tworzy obiekt `Grid`.

Atrybuty `Width`, `Height`, `Rows` i `Columns` mogą być zmieniane bezpośrednio w celu zdefiniowania wyglądu siatki.


```python
import FreeCAD, Draft, Arch
Grid = Arch.makeGrid()

Grid.Width = 5000
Grid.Height = 5000
Grid.Rows = 4
Grid.Columns = 6
FreeCAD.ActiveDocument.recompute()

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = Grid
FreeCAD.ActiveDocument.recompute() 
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Grid/pl
