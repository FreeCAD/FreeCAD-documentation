# Reinforcement Workbench/en


<img alt="Reinforcement workbench icon" src=images/Reinforcement_Workbench.svg  style="width:128px;">


{{TOCright}}

## Introduction

The [Reinforcement workbench](Reinforcement_Workbench.md) is an [external workbench](External_workbenches.md) that provides tools for Reinforcement Generation and Detailing. This workbench provides an interface and presets for the creation of common rebar types. And tools to generate rebars bill of material, rebar shape cut list, bar bending schedule, and rebars drawing and dimension.

Image:Arch\_Rebar\_Straight\_example.png\|[Straight Rebar](Arch_Rebar_Straight.md) Image:Arch\_Rebar\_UShape\_example.png\|[UShape Rebar](Arch_Rebar_UShape.md) Image:Arch\_Rebar\_LShape\_example.png\|[LShape Rebar](Arch_Rebar_LShape.md) Image:Arch\_Rebar\_BentShape\_example.png\|[BentShape Rebar](Arch_Rebar_BentShape.md) Image:Arch\_Rebar\_Stirrup\_example.png\|[Stirrup Rebar](Arch_Rebar_Stirrup.md) Image:Arch\_Rebar\_Helical\_example.png\|[Helical Rebar](Arch_Rebar_Helical.md) Image:Arch\_Rebar\_Circular\_ColumnReinforcement\_example.png\|[Circular Column Reinforcement](Arch_Rebar_Circular_ColumnReinforcement.md) Image:Arch\_Rebar\_ColumnReinforcement\_example.png\|[Single Tie Column Reinforcement](Arch_Rebar_ColumnReinforcement.md) Image:Arch\_Rebar\_ColumnReinforcement\_TwoTies\_example.png\|[Two Ties Six Rebars Column Reinforcement](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars.md) Image:Arch\_Rebar\_BeamReinforcement\_example.png\|[Beam Reinforcement](Arch_Rebar_BeamReinforcement.md) Image:Isometric\_view\_of\_Bent\_Shape\_rebars\_in\_parallel\_and\_cross\_direction\_with\_distribution\_rebars.png\|[Slab Reinforcement](Arch_Rebar_Slab_Reinforcement.md) Image:Isometric view of Columns footing.png\|[Footing Reinforcement](Arch_Rebar_Footing_Reinforcement.md) Image:Arch\_Rebar\_BOM\_example.png\|[Bill Of Material](Arch_Rebar_BOM.md) Image:Reinforcement\_Bar\_Shape\_Cut\_List\_example.svg\|[Rebar Shape Cut List](Reinforcement_Bar_Shape_Cut_List.md) Image:Reinforcement\_Bar\_Bending\_Schedule\_example.svg\|[Reinforcement Bar Bending Schedule](Reinforcement_Bar_Bending_Schedule.md) Image:Arch\_Rebar\_Drawing\_Dimensioning\_example.svg\|[Reinforcement Drawing Dimensioning](Arch_Rebar_Drawing_Dimensioning.md)

## Installing

The Reinforcement workbench is not bundled with the default FreeCAD package, but can easily be installed via the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md). Install it from **Tools → Addon manager → Reinforcement**. The Reinforcement workbench code is [hosted and developed on github](https://github.com/amrit3701/FreeCAD-Reinforcement) and can also be installed manually by copying it into FreeCAD\'s {{FileName|MOD}} directory.

## Tools

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

-   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Rebar](Arch_Rebar.md): Creates a custom reinforcement bar in a selected structural element using a sketch

### Reinforcement Detailing 

-   <img alt="" src=images/Arch_Rebar_BOM.svg  style="width:32px;"> [Bill Of Material](Arch_Rebar_BOM.md): Creates bill of material of reinforcing bars

-   <img alt="" src=images/Reinforcement_Bar_Shape_Cut_List.svg  style="width:32px;"> [Rebar Shape Cut List](Reinforcement_Bar_Shape_Cut_List.md): Creates rebar shape cut list of reinforcing bars

-   <img alt="" src=images/Reinforcement_Bar_Bending_Schedule.svg  style="width:32px;"> [Reinforcement Bar Bending Schedule](Reinforcement_Bar_Bending_Schedule.md): Creates bar bending schedule of reinforcing bars

-   <img alt="" src=images/Arch_Rebar_Drawing_Dimensioning.svg  style="width:32px;"> [Reinforcement Drawing Dimensioning](Arch_Rebar_Drawing_Dimensioning.md): Creates drawing and dimensioning of reinforcing bars
    -   <img alt="" src=images/Arch_Rebar_Drawing.svg  style="width:32px;"> [Reinforcement Drawing](Arch_Rebar_Drawing_Dimensioning#Reinforcement_Drawing.md): Creates drawing of reinforcing bars
    -   <img alt="" src=images/Arch_Rebar_Dimensioning.svg  style="width:32px;"> [Reinforcement Dimensioning](Arch_Rebar_Drawing_Dimensioning#Reinforcement_Dimensioning.md): Creates dimensioning of reinforcing bars in [Reinforcement Drawing](Arch_Rebar_Drawing_Dimensioning#Reinforcement_Drawing.md)




[Category:Addons](Category:Addons.md) [Category:External Workbenches](Category:External_Workbenches.md) [Category:Reinforcement](Category:Reinforcement.md)
