# <img alt="Reinforcement workbench icon" src=images/Reinforcement_Workbench.svg  style="width:64px;"> Reinforcement Workbench/pt-br




## Introdução

The [Reinforcement workbench](Reinforcement_Workbench.md) is an [external workbench](External_workbenches.md) that provides tools for Reinforcement Generation and Detailing. This workbench provides an interface and presets for the creation of common rebar types. And tools to generate rebars bill of material, rebar shape cut list, bar bending schedule, and rebars drawing and dimension.

Image:Arch_Rebar_Straight_example.png\|[Straight Rebar](Arch_Rebar_Straight.md) Image:Arch_Rebar_UShape_example.png\|[UShape Rebar](Arch_Rebar_UShape.md) Image:Arch_Rebar_LShape_example.png\|[LShape Rebar](Arch_Rebar_LShape.md) Image:Arch_Rebar_BentShape_example.png\|[BentShape Rebar](Arch_Rebar_BentShape.md) Image:Arch_Rebar_Stirrup_example.png\|[Stirrup Rebar](Arch_Rebar_Stirrup.md) Image:Arch_Rebar_Helical_example.png\|[Helical Rebar](Arch_Rebar_Helical.md) Image:Arch_Rebar_Circular_ColumnReinforcement_example.png\|[Circular Column Reinforcement](Arch_Rebar_Circular_ColumnReinforcement.md) Image:Arch_Rebar_ColumnReinforcement_example.png\|[Single Tie Column Reinforcement](Arch_Rebar_ColumnReinforcement.md) Image:Arch_Rebar_ColumnReinforcement_TwoTies_example.png\|[Two Ties Six Rebars Column Reinforcement](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars.md) Image:Arch_Rebar_BeamReinforcement_example.png\|[Beam Reinforcement](Arch_Rebar_BeamReinforcement.md) Image:Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png\|[Slab Reinforcement](Arch_Rebar_Slab_Reinforcement.md) Image:Isometric_view_of_Columns_footing.png\|[Footing Reinforcement](Arch_Rebar_Footing_Reinforcement.md) Image:Arch_Rebar_BOM_example.png\|[Bill Of Material](Arch_Rebar_BOM.md) Image:Reinforcement_Bar_Shape_Cut_List_example.svg\|[Rebar Shape Cut List](Reinforcement_Bar_Shape_Cut_List.md) Image:Reinforcement_Bar_Bending_Schedule_example.svg\|[Reinforcement Bar Bending Schedule](Reinforcement_Bar_Bending_Schedule.md) Image:Arch_Rebar_Drawing_Dimensioning_example.svg\|[Reinforcement Drawing Dimensioning](Arch_Rebar_Drawing_Dimensioning.md)

## Instalação

The Reinforcement workbench is not bundled with the default FreeCAD package, but can easily be installed via the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md). Install it from **Tools → Addon manager → Reinforcement**. The Reinforcement workbench code is [hosted and developed on github](https://github.com/amrit3701/FreeCAD-Reinforcement) and can also be installed manually by copying it into FreeCAD\'s **MOD** directory.

## Ferramentas

### Reinforcement Generation 

-   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Straight Rebar](Arch_Rebar_Straight.md): Creates a Straight reinforcement bar in a selected structural element

-   <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [UShape Rebar](Arch_Rebar_UShape.md): Creates a UShape reinforcement bar in a selected structural element

-   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [LShape Rebar](Arch_Rebar_LShape.md): Creates a LShape reinforcement bar in a selected structural element

-   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Bent Shape Rebar](Arch_Rebar_BentShape.md): Creates a Bent Shape reinforcement bar in a selected structural element

-   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Stirrup Rebar](Arch_Rebar_Stirrup.md): Creates a Stirrup reinforcement bar in a selected structural element

-   <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Helical Rebar](Arch_Rebar_Helical.md): Creates a Helical reinforcement bar in a selected structural element

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Circular ColumnReinforcement](Arch_Rebar_Circular_ColumnReinforcement.md): Creates reinforcing bars in a selected circular column structural element

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [ColumnReinforcement](Arch_Rebar_ColumnReinforcement.md): Creates reinforcing bars in a selected rectangular column structural element

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [ColumnReinforcement TwoTiesSixRebars](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars.md): Creates reinforcing bars in a selected column structural element

-   <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [BeamReinforcement](Arch_Rebar_BeamReinforcement.md): Creates reinforcing bars in a selected beam structural element

-   <img alt="" src=images/Arch_Rebar_Slab_Reinforcement.svg  style="width:32px;"> [SlabReinforcement](Arch_Rebar_Slab_Reinforcement.md): Creates reinforcing bars in a selected slab structural element

-   <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width:32px;"> [FootingReinforcement](Arch_Rebar_Footing_Reinforcement.md): Creates reinforcing bars inside a Footing Arch Structure object

-   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Rebar](Arch_Rebar.md): Creates a custom reinforcement bar in a selected structural element using a sketch

### Reinforcement Detailing 

-   <img alt="" src=images/Arch_Rebar_BOM.svg  style="width:32px;"> [Lista de ferros (BOM)](Arch_Rebar_BOM/pt-br.md): Cria lista de material de barras de reforço

-   <img alt="" src=images/Reinforcement_Bar_Shape_Cut_List.svg  style="width:32px;"> [Lista de materiais para reforço](Reinforcement_Bar_Shape_Cut_List/pt-br.md): Cria a lista de corte de vergalhões em forma de barras de reforço

-   <img alt="" src=images/Reinforcement_Bar_Bending_Schedule.svg  style="width:32px;"> [Cronograma de dobra da barra de reforço](Reinforcement_Bar_Bending_Schedule/pt-br.md): Cria um calendário de dobra de barras de reforço

-   <img alt="" src=images/Arch_Rebar_Drawing_Dimensioning.svg  style="width:32px;"> [Desenhar e dimensionar um reforço](Arch_Rebar_Drawing_Dimensioning/pt-br.md): Cria desenho e dimensionamento de barras de reforço
    -   <img alt="" src=images/Arch_Rebar_Drawing.svg  style="width:32px;"> [Desenho de Reforço](Arch_Rebar_Drawing_Dimensioning#Reinforcement_Drawing/pt-br.md): Cria desenho de barras de reforço
    -   <img alt="" src=images/Arch_Rebar_Dimensioning.svg  style="width:32px;"> [Dimensionamento de Reforço](Arch_Rebar_Drawing_Dimensioning#Reinforcement_Dimensioning/pt-br.md): Cria o dimensionamento de barras de reforço em [Desenho de Reforço](Arch_Rebar_Drawing_Dimensioning#Reinforcement_Drawing/pt-br.md)



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement Workbench/pt-br
