# <img alt="Ikonka FreeCAD dla środowiska pracy Zbrojenie" src=images/Reinforcement_Workbench.svg  style="width   *64px;"> Reinforcement Workbench/pl


{{TOCright}}

## Wprowadzenie

Środowisko pracy [Zbrojenie](Reinforcement_Workbench/pl.md) jest [środowiskiem zewnętrznym](External_workbenches/pl.md), który dostarcza narzędzi do generowania i detalowania zbrojenia. To środowisko robocze zapewnia interfejs i ustawienia wstępne do tworzenia typowych typów prętów zbrojeniowych. Oraz narzędzia do generowania rachunku materiałowego prętów zbrojeniowych, listy cięć kształtu prętów zbrojeniowych, harmonogramu gięcia prętów oraz rysunków i wymiarów prętów zbrojeniowych.

Image   *Arch_Rebar_Straight_example.png\|[Pręty zbrojeniowe proste](Arch_Rebar_Straight/pl.md) Image   *Arch_Rebar_UShape_example.png\|[Pręty zbrojeniowe typu U](Arch_Rebar_UShape/pl.md) Image   *Arch_Rebar_LShape_example.png\|[Pręty zbrojeniowe typu L](Arch_Rebar_LShape/pl.md) Image   *Arch_Rebar_BentShape_example.png\|[Pręty zbrojeniowe wygięte](Arch_Rebar_BentShape/pl.md) Image   *Arch_Rebar_Stirrup_example.png\|[Strzemiona zbrojeniowe](Arch_Rebar_Stirrup/pl.md) Image   *Arch_Rebar_Helical_example.png\|[Pręty zbrojeniowe spiralne](Arch_Rebar_Helical/pl.md) Image   *Arch_Rebar_Circular_ColumnReinforcement_example.png\|[Pręty zbrojeniowe okrągłe, zbrojenie słupów](Arch_Rebar_Circular_ColumnReinforcement/pl.md) Image   *Arch_Rebar_ColumnReinforcement_example.png\|[Pręty zbrojeniowe, zbrojenie słupów](Arch_Rebar_ColumnReinforcement/pl.md) Image   *Arch_Rebar_ColumnReinforcement_TwoTies_example.png\|[Pręty zbrojeniowe, zbrojenie słupa dwa ściągi sześć prętów zbrojeniowych](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/pl.md) Image   *Arch_Rebar_BeamReinforcement_example.png\|[Pręty zbrojeniowe, zbrojenie belek](Arch_Rebar_BeamReinforcement/pl.md) Image   *Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png\|[Pręty zbrojeniowe, zbrojenie płyt stropowych](Arch_Rebar_Slab_Reinforcement/pl.md) Image   *Isometric_view_of_Columns_footing.png\|[Zbrojenie stóp fundamentowych](Arch_Rebar_Footing_Reinforcement/pl.md) Image   *Arch_Rebar_BOM_example.png\|[Zestawienie zbrojenia](Arch_Rebar_BOM/pl.md) Image   *Reinforcement_Bar_Shape_Cut_List_example.svg\|[Kształt prętów zbrojeniowych, lista cięć](Reinforcement_Bar_Shape_Cut_List/pl.md) Image   *Reinforcement_Bar_Bending_Schedule_example.svg\|[Pręty zbrojeniowe, schemat gięcia prętów](Reinforcement_Bar_Bending_Schedule/pl.md) Image   *Arch_Rebar_Drawing_Dimensioning_example.svg\|[Wymiarowanie rysunku zbrojenia](Arch_Rebar_Drawing_Dimensioning/pl.md)

## Instalacja

Środowisko pracy Zbrojenie nie jest dołączone do domyślnego pakietu FreeCAD, ale może być łatwo zainstalowane poprzez <img alt="" src=images/AddonManager.svg  style="width   *24px;"> [Menadżer dodatków](Std_AddonMgr.md). Zainstaluj go za pomocą **Narzędzia → Menadżer dodatków → Reinforcement**. Kod środowiska pracy Zbrojenie jest [hostowany i rozwijany na githubie](https   *//github.com/amrit3701/FreeCAD-Reinforcement) i może być również zainstalowany ręcznie poprzez skopiowanie go do katalogu FreeCAD **MOD**.

## Przybory

### Wytwarzanie zbrojenia 

-   <img alt="" src=images/Arch_Rebar_Straight.png  style="width   *32px;"> [Pręty zbrojeniowe proste](Arch_Rebar_Straight/pl.md)   * Tworzy prosty pręt zbrojeniowy w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Arch_Rebar_UShape.png  style="width   *32px;"> [Pręty zbrojeniowe typu U](Arch_Rebar_UShape/pl.md)   * Tworzy pręt zbrojeniowy w kształcie litery U w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Arch_Rebar_LShape.png  style="width   *32px;"> [Pręty zbrojeniowe typu L](Arch_Rebar_LShape/pl.md)   * Tworzy pręt zbrojeniowy w kształcie litery L w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width   *32px;"> [Pręty zbrojeniowe wygięte](Arch_Rebar_BentShape/pl.md)   * Tworzy pręt zbrojeniowy typu wygiętego w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width   *32px;"> [Strzemiona zbrojeniowe](Arch_Rebar_Stirrup/pl.md)   * Tworzy pręt zbrojeniowy strzemion w wybranym elemencie konstrukcyjnym

-   <img alt="" src=images/Arch_Rebar_Helical.png  style="width   *32px;"> [Pręty zbrojeniowe spiralne](Arch_Rebar_Helical/pl.md)   * Tworzy spiralny pręt zbrojeniowy w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width   *32px;"> [Pręty zbrojeniowe okrągłe, zbrojenie słupów](Arch_Rebar_Circular_ColumnReinforcement/pl.md)   * Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym słupa okrągłego.

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width   *32px;"> [Pręty zbrojeniowe, zbrojenie słupów](Arch_Rebar_ColumnReinforcement/pl.md)   * Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym słupa prostokątnego.

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width   *32px;"> [Pręty zbrojeniowe, zbrojenie słupa dwa ściągi sześć prętów zbrojeniowych](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/pl.md)   * Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym słupa.

-   <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width   *32px;"> [Pręty zbrojeniowe, zbrojenie belek](Arch_Rebar_BeamReinforcement/pl.md)   * Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym belki.

-   <img alt="" src=images/Arch_Rebar_Slab_Reinforcement.svg  style="width   *32px;"> [Pręty zbrojeniowe, zbrojenie płyt stropowych](Arch_Rebar_Slab_Reinforcement/pl.md)   * Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym płyty.

-   <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width   *32px;"> [Zbrojenie stóp fundamentowych](Arch_Rebar_Footing_Reinforcement/pl.md)   * Tworzy pręty zbrojeniowe wewnątrz obiektu konstrukcyjnego ławy fundamentowej.

-   <img alt="" src=images/Arch_Rebar.svg  style="width   *32px;"> [Pręt zbrojeniowy](Arch_Rebar/pl.md)   * Tworzy niestandardowy pręt zbrojeniowy w wybranym elemencie konstrukcyjnym za pomocą szkicu.

### Szczegóły zbrojenia 

-   <img alt="" src=images/Arch_Rebar_BOM.svg  style="width   *32px;"> [Zestawienie zbrojenia](Arch_Rebar_BOM/pl.md)   * Tworzy zestawienie materiałów dla prętów zbrojeniowych.

-   <img alt="" src=images/Reinforcement_Bar_Shape_Cut_List.svg  style="width   *32px;"> [Kształt prętów zbrojeniowych, lista cięć](Reinforcement_Bar_Shape_Cut_List/pl.md)   * Tworzy listę cięć kształtów prętów zbrojeniowych.

-   <img alt="" src=images/Reinforcement_Bar_Bending_Schedule.svg  style="width   *32px;"> [Pręty zbrojeniowe, schemat gięcia prętów](Reinforcement_Bar_Bending_Schedule/pl.md)   * Tworzy schemat gięcia prętów zbrojeniowych.

-   <img alt="" src=images/Arch_Rebar_Drawing_Dimensioning.svg  style="width   *32px;"> [Wymiarowanie rysunku zbrojenia](Arch_Rebar_Drawing_Dimensioning/pl.md)   * Wykonuje rysunki i wymiaruje pręty zbrojeniowe.
    -   <img alt="" src=images/Arch_Rebar_Drawing.svg  style="width   *32px;"> [Rysunek zbrojenia](Arch_Rebar_Drawing_Dimensioning/pl#Rysunek_zbrojeniag.md)   * Tworzy rysunki prętów zbrojeniowych.
    -   <img alt="" src=images/Arch_Rebar_Dimensioning.svg  style="width   *32px;"> [Wymiarowanie zbrojenia](Arch_Rebar_Drawing_Dimensioning/pl#Wymiarowanie_zbrojenia.md)   * Tworzy wymiarowanie prętów zbrojeniowych w [Rysunku zbrojenia](Arch_Rebar_Drawing_Dimensioning/pl#Reinforcement_Drawing/pl.md).




[Category   *Addons](Category_Addons.md) [Category   *External Workbenches](Category_External_Workbenches.md) [Category   *Reinforcement](Category_Reinforcement.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement Workbench/pl
