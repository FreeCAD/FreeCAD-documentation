# <img alt="Ikonka FreeCAD dla środowiska pracy Wykres" src=images/Workbench_Plot.svg  style="width   *64px;"> Plot Workbench/pl


{{TOCright}}

## Wprowadzenie

FreeCAD jest w stanie wykonywać wykresy przy użyciu biblioteki [Python](Python/pl.md) [matplotlib](https   *//matplotlib.org/). W tym celu w wersji 0.19 dostarczany jest moduł, jako zewnętrzny dodatek a od wersji 0.20 jako podstawowy komponent. Starsze wersje FreeCAD nie są objęte niniejszą dokumentacją.

Generowane wykresy oferują standardowe narzędzia [matplotlib](https   *//matplotlib.org/) do edycji i zapisu. Dodatkowo, środowisko pracy <img alt="" src=images/Workbench_Plot.svg  style="width   *24px;"> [Wykres](Plot_Workbench/pl.md) jest dostarczane jako zewnętrzny dodatek oferujący bardziej kompletne narzędzia do edycji i zapisywania wykresu. Dodatek ten może być zainstalowany za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md).

## Moduł

Moduł można wywołać w konsoli [Python](Python/pl.md) lub w [makrodefinicji](Macros/pl.md). Pierwszą rzeczą, niezbędna do wykonania jest zaimportowanie modułu. We FreeCAD v0.19 musisz najpierw zainstalować środowisko pracy <img alt="" src=images/Workbench_Plot.svg  style="width   *24px;"> [Wykres](Plot_Workbench/pl.md) za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md), a następnie możesz zaimportować pisanie wykresu


```python
from freecad.plot import Plot
```

Od wersji FreeCAD **v0.20** moduł plot jest wbudowany w program, więc nie trzeba instalować żadnego dodatku, a jedynie wpisać


```python
from FreeCAD.Plot import Plot
```

Następnie można wykreślić linię prostą od współrzędnych *(0,0)* do *(1,2)* wpisując po prostu


```python
Plot.plot([0, 1], [0, 2])
```

Bardziej złożone przykłady znajdziesz w poradnikach [Poradnik   * Podstawy dla środowiska pracy Wykres](Plot_Basic_tutorial/pl.md) i [Poradnik   * Wykres wieloosiowy](Plot_MultiAxes_tutorial/pl.md).

## Narzędzia środowiska pracy 

Jeśli zdecydujesz się na zainstalowanie środowiska pracy <img alt="" src=images/Workbench_Plot.svg  style="width   *24px;"> [Wykres](Plot_Workbench/pl.md) za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md), będziesz miał dostępne następujące narzędzia do zarządzania wykresami utworzonymi za pomocą modułu   *

-   <img alt="" src=images/Plot_Save.svg  style="width   *32px;"> [Zapisz wykres](Plot_Save/pl.md)   * Zapisuje wykres w kilku formatach. Możesz również wybrać rozmiar wyjściowy i rozdzielczość.
-   <img alt="" src=images/Plot_Axes.svg  style="width   *32px;"> [Konfiguruj osie](Plot_Axes/pl.md)   * Dodaj, usuń lub edytuj osie wykresu.
-   <img alt="" src=images/Plot_Series.svg  style="width   *32px;"> [Skonfiguruj serie](Plot_Series/pl.md)   * Edycja tytułu i stylów serii.
-   <img alt="" src=images/Plot_Grid.svg  style="width   *32px;"> [Pokaż / ukryj siatkę](Plot_Grid.md)   * Wyświetla / ukrywa siatkę.
-   <img alt="" src=images/Plot_Legend.svg  style="width   *32px;"> [Pokaż / ukryj legendę](Plot_Legend/pl.md)   * Wyświetla / ukrywa legendę.
-   <img alt="" src=images/Plot_Labels.svg  style="width   *32px;"> [Ustaw etykiety](Plot_Labels/pl.md)   * Edycja etykiet.
-   <img alt="" src=images/Plot_Positions.svg  style="width   *32px;"> [Ustaw pozycje i rozmiary](Plot_Positions/pl.md)   * Ustawianie pozycji elementów.

## Tworzenie skryptów 

Ponieważ środowisko pracy Wykres jest nakładką `matplotlib`, możesz swobodnie używać dowolnych funkcji z tej biblioteki na instancjach plot. Aby zobaczyć przykłady, przeczytaj stronę [Skrypty i makrodefinicje](Scripting_and_macros/pl.md).

## Poradniki

-   [Poradnik   * Podstawy dla środowiska pracy Wykres](Plot_Basic_tutorial/pl.md)
-   [Poradnik   * Wykres wieloosiowy](Plot_MultiAxes_tutorial/pl.md)


{{Plot_Tools_navi

}} 

[Category   *External\_Workbenches](Category_External_Workbenches.md) [Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > Plot Workbench/pl
