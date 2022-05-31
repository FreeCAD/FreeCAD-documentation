# <img alt="Ikonka FreeCAD dla środowiska pracy Powierzchnia" src=images/Workbench_Surface.svg  style="width   *64px;"> Surface Workbench/pl


{{TOCright}}

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Surface.svg  style="width   *24px;"> **Powierzchnia** udostępnia narzędzia do tworzenia i modyfikowania prostych powierzchni [NURBS](https   *//en.wikipedia.org/wiki/Non-uniform_rational_B-spline). Narzędzia te mają podobną funkcjonalność do narzędzia **[<img src=images/Part_Builder.svg style="width   *16px"> [Konstruktor kształtu](Part_Builder/pl.md)**, gdy używana jest opcja **Ściana z krawędzi**. Jednak w przeciwieństwie do tego narzędzia, narzędzia środowiska pracy Powierzchnia są parametryczne i zapewniają dodatkowe opcje. Pod tym względem narzędzia w tym środowisku roboczym są podobne do **[<img src=images/PartDesign_AdditiveLoft.svg style="width   *16px"> [Wyciągnięcie przez profile](PartDesign_AdditiveLoft/pl.md)** i **[<img src=images/PartDesign_AdditivePipe.svg style="width   *16px"> [Wyciągnięcie po ścieżce](PartDesign_AdditivePipe/pl.md)**.

Niektóre z dostępnych funkcji to   *

-   Tworzenie powierzchni z krawędzi brzegowych.
-   Wyrównywanie krzywizn z sąsiednich powierzchni.
-   Ograniczanie powierzchni do dodatkowych krzywych i wierzchołków.
-   Rozszerzanie powierzchni.
-   Siatka może być użyta jako szablon do utworzenia krzywych złożonych na jej powierzchni.

<img alt="" src=images/Surface_example.png  style="width   *350px;">

## Użycie

Środowisko pracy Powierzchnia umożliwia tworzenie powierzchni za pomocą kształtów, co nie jest możliwe przy użyciu standardowych narzędzi w innych środowiskach pracy.

<img alt="" src=images/Toy_Duck.png  style="width   *350px;">



*Powierzchnia utworzona na podstawie szkiców umieszczonych w płaszczyznach odniesienia za pomocą narzędzi środowiska [Projekt Części](PartDesign_Workbench/pl.md).*

Środowisko pracy Powierzchnia integruje się z innymi środowiskami pracy programu FreeCAD. Powyższy przykład został utworzony ze **[<img src=images/Sketcher_NewSketch.svg style="width   *16px"> [Szkicu](Sketch.md)** umieszczonego na **[<img src=images/PartDesign_Plane.svg style="width   *16px"> [Płaszczyźnie odniesienia](PartDesign_Plane/pl.md)** w środowisku <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [Projekt Części](PartDesign_Workbench/pl.md). Projekt może być w pełni parametryczny, jeśli wszystkie płaszczyzny odniesienia i szkice są odpowiednio zdefiniowane. W większości przypadków wystarczy narysować zamknięty szkic, aby zdefiniować granicę powierzchni, a następnie użyć różnych opcji do dalszej modyfikacji jej kształtu.

Wygenerowana powierzchnia nie może być umieszczona wewnątrz **[<img src=images/PartDesign_Body.svg style="width   *16px"> [Zawartości](PartDesign_Body/pl.md)**. Jednakże, wygenerowana powierzchnia może być zawarta wewnątrz **[<img src=images/Std_Part.svg style="width   *16px"> [Części](Std_Part/pl.md)** wraz z powiązaną z nią **[<img src=images/PartDesign_Body.svg style="width   *16px"> [Zawartością](PartDesign_Body/pl.md)**, która przechowuje płaszczyzny odniesienia i szkice. Nieparametryczne narzędzie **[<img src=images/Part_Builder.svg style="width   *16px"> [Konstruktor kształtu](Part_Builder/pl.md)** może być następnie użyte w celu utworzenia [powłoki](Glossary#Shell.md) i wreszcie [bryły](Glossary#Solid.md).

## Przybory

-   <img alt="Wypełnianie" src=images/Surface_Filling.svg  style="width   *32px;"> [Wypełnianie](Surface_Filling/pl.md)   * wypełnia serię krzywych brzegowych powierzchnią.

-   <img alt="Wypełnianie krzywych granicznych" src=images/Surface_GeomFillSurface.svg  style="width   *32px;"> [Wypełnianie krzywych granicznych](Surface_GeomFillSurface/pl.md)   * tworzy powierzchnię z dwóch, trzech lub czterech krawędzi granicznych.

-   <img alt="Przekrój powierzchni" src=images/Surface_Sections.svg  style="width   *32px;"> [Przekrój powierzchni](Surface_Sections/pl.md)   * tworzy powierzchnię z krawędzi, które reprezentują przekroje poprzeczne powierzchni. {{Version/pl|0.19}}

-   <img alt="Rozszerz powierzchnię\|Rozszerz powierzchnię" src=images/Surface_ExtendFace.svg  style="width   *32px;"> [Rozszerz powierzchnię](Surface_ExtendFace/pl.md)   * ekstrapoluje powierzchnię na granicach za pomocą lokalnego parametru **U** i parametru **V**.

-   <img alt="Krzywa na siatce" src=images/Surface_CurveOnMesh.svg  style="width   *32px;"> [Krzywa na siatce](Surface_CurveOnMesh/pl.md)   * tworzy aproksymowane segmenty krzywej złożonej na wybranej [siatce](Mesh_Workbench/pl.md).





{{Surface Tools navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Surface](Category_Surface.md) > Surface Workbench/pl
