# <img alt="Ikonka FreeCAD dla środowiska pracy Zbrojenie" src=images/Reinforcement_Workbench.svg  style="width:64px;"> Reinforcement Workbench/pl






## Wprowadzenie

Środowisko pracy [Zbrojenie](Reinforcement_Workbench/pl.md) jest [środowiskiem zewnętrznym](External_workbenches/pl.md), który dostarcza narzędzi do generowania i detalowania zbrojenia. To środowisko robocze zapewnia interfejs i ustawienia wstępne do tworzenia typowych typów prętów zbrojeniowych. Oraz narzędzia do generowania rachunku materiałowego prętów zbrojeniowych, listy cięć kształtu prętów zbrojeniowych, harmonogramu gięcia prętów oraz rysunków i wymiarów prętów zbrojeniowych.

Image:Arch_Rebar_Straight_example.png\|[Pręty zbrojeniowe proste](Reinforcement_StraightRebar/pl.md) Image:Arch_Rebar_UShape_example.png\|[Pręty zbrojeniowe typu U](Reinforcement_UShapeRebar/pl.md) Image:Arch_Rebar_LShape_example.png\|[Pręty zbrojeniowe typu L](Reinforcement_LShapeRebar/pl.md) Image:Arch_Rebar_Stirrup_example.png\|[Strzemiona](Reinforcement_StirrupRebar/pl.md) Image:Arch_Rebar_BentShape_example.png\|[Pręty zbrojeniowe wygięte](Reinforcement_BentShapeRebar/pl.md)

Image:Arch_Rebar_Helical_example.png\|[Pręty zbrojeniowe spiralne](Reinforcement_HelicalRebar/pl.md) Image:Arch_Rebar_Circular_ColumnReinforcement_example.png\|[Pręty zbrojeniowe okrągłe, zbrojenie słupów](Arch_Rebar_Circular_ColumnReinforcement/pl.md) Image:Arch_Rebar_ColumnReinforcement_TwoTies_example.png\|[Zbrojenie słupa dwa ściągi sześć prętów zbrojeniowych](Reinforcement_ColumnRebars_TwoTiesSixRebars/pl.md) Image:Arch_Rebar_Circular_ColumnReinforcement_example.png\|[Pręty zbrojeniowe, zbrojenie słupa dwa ściągi sześć prętów zbrojeniowych](Reinforcement_ColumnRebars_Circular/pl.md) Image:Arch_Rebar_BeamReinforcement_example.png\|[Pręty zbrojeniowe, zbrojenie belek](Reinforcement_BeamRebars/pl.md) Image:Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png\|[Pręty zbrojeniowe, zbrojenie płyt stropowych](Reinforcement_SlabRebars/pl.md) Image:Isometric_view_of_Columns_footing.png\|[Zbrojenie stóp fundamentowych](Reinforcement_FootingRebars/pl.md) Image:Arch_Rebar_BOM_example.png\|[Zestawienie zbrojenia](Reinforcement_BillOfMaterial/pl.md) Image:Reinforcement_Bar_Shape_Cut_List_example.svg\|[Kształt prętów zbrojeniowych, lista cięć](Reinforcement_BarShapeCutList/pl.md) Image:Reinforcement_Bar_Bending_Schedule_example.svg\|[Pręty zbrojeniowe, schemat gięcia prętów](Reinforcement_BarBendingSchedule/pl.md) Image:Arch_Rebar_Drawing_Dimensioning_example.svg\|[Wymiarowanie rysunku zbrojenia](Reinforcement_DrawingDimensioning/pl.md)



## Instalacja

Środowisko pracy Zbrojenie nie jest dołączone do domyślnego pakietu FreeCAD, ale może być łatwo zainstalowane poprzez <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Menadżer dodatków](Std_AddonMgr.md). Zainstaluj go za pomocą **Narzędzia → Menadżer dodatków → Reinforcement**. Kod środowiska pracy Zbrojenie jest [hostowany i rozwijany na githubie](https://github.com/amrit3701/FreeCAD-Reinforcement) i może być również zainstalowany ręcznie poprzez skopiowanie go do katalogu FreeCAD **MOD**.



## Przybory



### Wytwarzanie zbrojenia 

-   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Pręt zbrojeniowy](Arch_Rebar/pl.md): Tworzy niestandardowy pręt zbrojeniowy w wybranym elemencie konstrukcyjnym za pomocą szkicu.

-   <img alt="" src=images/Reinforcement_StraightRebar.svg  style="width:32px;"> [Pręty zbrojeniowe proste](Reinforcement_StraightRebar/pl.md): Tworzy prosty pręt zbrojeniowy w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Reinforcement_UShapeRebar.svg  style="width:32px;"> [Pręty zbrojeniowe typu U](Reinforcement_UShapeRebar/pl.md): Tworzy pręt zbrojeniowy w kształcie litery U w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Reinforcement_LShapeRebar.svg  style="width:32px;"> [Pręty zbrojeniowe typu L](Reinforcement_LShapeRebar/pl.md): Tworzy pręt zbrojeniowy w kształcie litery L w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Reinforcement_StirrupRebar.svg  style="width:32px;"> [Strzemiona zbrojeniowe](Reinforcement_StirrupRebar/pl.md): Tworzy pręt zbrojeniowy strzemion w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Reinforcement_BentShapeRebar.svg  style="width:32px;"> [Pręty zbrojeniowe wygięte](Reinforcement_BentShapeRebar/pl.md): Tworzy pręt zbrojeniowy typu wygiętego w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Reinforcement_HelicalRebar.svg  style="width:32px;"> [Pręty zbrojeniowe spiralne](Reinforcement_HelicalRebar/pl.md): Tworzy spiralny pręt zbrojeniowy w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Reinforcement_ColumnRebars.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie słupów](Reinforcement_ColumnRebars/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym słupa prostokątnego.

-   <img alt="" src=images/Reinforcement_BeamRebars.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie belek](Reinforcement_BeamRebars/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym belki.

-   <img alt="" src=images/Reinforcement_SlabRebars.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie płyt stropowych](Reinforcement_SlabRebars/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym płyty.

-   <img alt="" src=images/Reinforcement_FootingRebars.svg  style="width:32px;"> [Zbrojenie stóp fundamentowych](Reinforcement_FootingRebars/pl.md): Tworzy pręty zbrojeniowe wewnątrz obiektu konstrukcyjnego ławy fundamentowej.



### Szczegóły zbrojenia 

-   <img alt="" src=images/Reinforcement_BillOfMaterial.svg  style="width:32px;"> [Zestawienie zbrojenia](Reinforcement_BillOfMaterial/pl.md): Tworzy zestawienie materiałów dla prętów zbrojeniowych.

-   <img alt="" src=images/Reinforcement_BarShapeCutList.svg  style="width:32px;"> [Kształt prętów zbrojeniowych, lista cięć](Reinforcement_BarShapeCutList/pl.md): Tworzy listę cięć kształtów prętów zbrojeniowych.

-   <img alt="" src=images/Reinforcement_BarBendingSchedule.svg  style="width:32px;"> [Pręty zbrojeniowe, schemat gięcia prętów](Reinforcement_BarBendingSchedule/pl.md): Tworzy schemat gięcia prętów zbrojeniowych.

-   <img alt="" src=images/Reinforcement_DrawingDimensioning.svg  style="width:32px;"> [Wymiarowanie rysunku zbrojenia](Reinforcement_DrawingDimensioning/pl.md): Wykonuje rysunki i wymiaruje pręty zbrojeniowe.



---
⏵ [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement Workbench/pl
