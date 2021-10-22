# Constructive solid geometry/pl
{{TOCright}}

## Wprowadzenie

[Constructive solid geometry](https://en.wikipedia.org/wiki/Constructive_solid_geometry) *(**CSG**)* to paradygmat modelowania, który jest używany w wielu tradycyjnych systemach CAD. Zasadniczo polega on na użyciu pierwotnych obiektów bryłowych i wykonywaniu na nich operacji logicznych, takich jak łączenie, odejmowanie i przecinanie, w celu utworzenia ostatecznego kształtu.

W programie FreeCAD metoda ta jest najczęściej wykorzystywana przy użyciu środowiska pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> _, <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> _ oraz łączenia ich ze sobą, lub używania ich do cięcia innych obiektów za pomocą takich narzędzi środowiska pracy Część jak **<img src="images/Part_Cut.svg" width=24px> [Wytnij](Part_Cut/pl.md)**.

<img alt="" src=images/Part_Constructive_Solid_Geometry_workflow.svg  style="width:800px;">



*Konstruktywna geometria bryłowa ''(CSG)''. Można wykonać dowolną liczbę operacji na bryłach pierwotnych, aby utworzyć inne obiekty bryłowe, a następnie połączyć je lub wyciąć, aż do uzyskania ostatecznego kształtu.*

Alternatywnie, środowisko pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md) używa bardziej nowoczesnego podejścia niż proste CSG. Metoda ta jest nazywana [Edycja cech](Feature_editing/pl.md), co oznacza tworzenie bryły bazowej, a następnie dodawanie sekwencyjnych przekształceń parametrycznych w celu uzyskania ostatecznej zawartości.


**Note:**

[Zawartość](PartDesign_Body/pl.md) utworzone za pomocą środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md) może być również użyta w operacji logicznej z innymi obiektami..

## Przykład

<img alt="" src=images/Part_CGS_workflow_example.svg  style="width:600px;">



*Przykład przepływu pracy z wykorzystaniem geometrii brył konstrukcyjnych ''(CSG)'': <br>elementy pierwotne są łączone ''(połączenie)''. Obliczany jest punkt przecięcia dwóch innych elementów pierwotnych ''(wspólny)'',
<br>otrzymywana jest różnica ''(przecięcie)'' dwóch poprzednich kształtów.*

## Poradniki

Strona _, które wykorzystują metodę **CSG**.

-   _
-   [Poradnik: Kula Whiffle](Whiffle_Ball_tutorial/pl.md)
-   [Poradnik: Podstawy modelowania](Basic_modeling_tutorial/pl.md)

 

_

---
[documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > Constructive solid geometry/pl
