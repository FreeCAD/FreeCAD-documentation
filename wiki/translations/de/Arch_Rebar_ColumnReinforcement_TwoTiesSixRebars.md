---
- GuiCommand:/de
   Name:Arch Rebar ColumnReinforcement
   Name/de:Architektur Bewehrung SäulenVerstärkung
   MenuLocation:Arch → Rebar tools → Säulenverstärkung oder 3D/BIM → Reinforcement tools → Stützenbewehrung
   Workbenches:[Arch](Arch_Workbench/de.md), [BIM](BIM_Workbench/de.md)
   SeeAlso:[Reinforcement](Reinforcement_Workbench/de.md), [Arch Rebar](Arch_Rebar/de.md),[Säulen Verstärkung](Arch_Rebar_ColumnReinforcement/de.md), [Balken Verstärkung](Arch_Rebar_BeamReinforcement/de.md)
   Version:0.19
---

# Arch Rebar ColumnReinforcement TwoTiesSixRebars/de

## Beschreibung

The [Column Reinforcement TwoTiesSixRebars](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars.md) tool allows the user to create reinforcing bars (Two Ties Six Rebars) inside a Column [Arch Structure](Arch_Structure.md) object.

The [Column Reinforcement TwoTiesSixRebars](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_ColumnReinforcement_TwoTies_example.png  style="width:400px;">



*TwoTiesSixRebars Column Reinforcement inside a Column [Arch Structure](Arch_Structure.md)*

## Usage

1\. Select any face of a previously created **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object.
2. Then select **<img src="images/Arch_Rebar_ColumnReinforcement.svg" width=16px> [Column Reinforcement](Arch_Rebar_ColumnReinforcement.md)** from the rebar tools.
3. A dialog box will pop-out on screen as shown below.
<img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;">



*Dialog Box for the Arch Rebar ColumnReinforcement tool*

4\. Select the TwoTiesSixRebars type of column reinforcement from drop down menu on right side.
<img alt="" src=images/TwoTiesColumnReinforcementDialog_Ties.png  style="width:700px;">



*Dialog Box for the TwoTiesSixRebars ColumnReinforcement*

5\. Give inputs for data related to ties.
6. Click **Next** and the dialog box will be updated as shown below.
<img alt="" src=images/TwoTiesColumnReinforcementDialog_MainRebars.png  style="width:700px;">



*Dialog Box for Main Rebars data*

7\. Select desired rebar type and fill data for main rebars.
8. Click **OK** or **Apply** to generate column reinforcement.
9. Click **Cancel** to exit the dialog box.

## Properties

**Ties:**

-    **Left Cover**: The distance between the left end of the tie to the left face of the structure.

-    **Right Cover**: The distance between the right end of the tie to right face of the structure.

-    **Top Cover**: The distance between tie from the top face of the structure.

-    **Bottom Cover**: The distance between tie from the bottom face of the structure.

-    **Offset**: The distance between tie from the top/bottom face of the structure.

-    **Diameter**: Diameter of the tie.

-    **Bent Angle**: Bent angle defines the angle at the ends of a tie.

-    **Extension Factor**: Extension Factor defines length of end of tie, expressed in times the diameter.

-    **Number**: The number of ties.

-    **Spacing**: The distance between the axes of each tie.

-    **Ties Sequence**: The sequence of ties from top to bottom with respect to front view.

**Main Rebars:** Rebars present at corners of tie

-    **Rebar Type**: Type of main rebars.

-    **Hook Orientation**: Orientation of LShaped hooks.

-    **Hook Extend Along**: Direction for hook extension.

-    **Hook Extension**: Length of hook of LShape rebars.

-    **Rounding**: A rounding value to be applied to the corners of the LShape rebars, expressed in times the diameter.

-    **Top Offset**: The distance between rebar from the top face of the structure.

-    **Bottom Offset**: The distance between rebar from the bottom face of the structure.

-    **Diameter**: Diameter of the main rebars.

## Skripten


**Siehe auch:**

[Architektur API](Arch_API/de.md), [Bewehrung API](Reinforcement_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Säulenverstärkungswerkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md)-Konsole mit der folgenden Funktion verwendet werden:

### Create Two Ties Six Rebars 


```python
RebarGroup = makeTwoTiesSixRebars(
    l_cover_of_ties,
    r_cover_of_ties,
    t_cover_of_ties,
    b_cover_of_ties,
    offset_of_ties,
    bent_angle_of_ties,
    extension_factor_of_ties,
    dia_of_ties,
    number_spacing_check,
    number_spacing_value,
    dia_of_main_rebars,
    t_offset_of_rebars,
    b_offset_of_rebars,
    main_rebars_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    ties_sequence=("Tie1", "Tie2"),
    structure=None,
    facename=None,
)

```

-   Creates a `RebarGroup` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `l_cover_of_ties`, `r_cover_of_ties`, `t_cover_of_ties`, `b_cover_of_ties` and `offset_of_ties` are inner offset distances for the tie elements with respect to the faces of the structure. They are respectively the left, right, top, bottom and front/rear offsets.

-    `bent_angle_of_ties`define the angle of the tip of the reinforcement loop of tie elements.

-    `extension_factor_of_ties`define the length of the tip of the reinforcement loop of tie elements, expressed in times the diameter of tie elements.

-    `dia_of_ties`is the diameter of the tie elements.

-    `number_spacing_check`if it is `True` it will create as many two ties sets as given by `number_spacing_value`; if it is `False` it will create two ties sets separated by the numerical value of `number_spacing_value`.

-    `number_spacing_value`specifies the number of two ties sets, or the value of the separation between the sets, depending on `number_spacing_check`.

-    `dia_of_main_rebars`is the diameter of the main rebars.

-    `t_offset_of_rebars`and `b_offset_of_rebars` are inner offset distances for the main rebars with respect to the top and bottom faces of the structure, respectively.

-    `main_rebars_type`is the type of the main rebars; it can be `"StraightRebar"` or `"LShapeRebar"`.

-    `hook_orientation`specifies the orientation of LShaped hook; it can be: `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` or `"Bottom Left"`.

-    `hook_extend_along`specifies direction for hook extension; it can be `"x-axis"` or `"y-axis"`.

-    `l_rebar_rounding`is the parameter that determines the bending radius of the LShaped main rebars, expressed as times the diameter.

-    `hook_extension`is the length of hook of LShaped rebars.

-    `ties_sequence`is the sequence of ties from top to bottom with respect to front view; it can be `("Tie1", "Tie2")` or `("Tie2", "Tie1")`.

#### Example


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# For Straight Rebars

RebarGroup = TwoTiesSixRebars.makeTwoTiesSixRebars(
    l_cover_of_ties=40,        
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=40,
    b_offset_of_rebars=40,
    main_rebars_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    ties_sequence=("Tie1", "Tie2"),
    structure=Structure,
    facename="Face6",
)

# For LShaped Rebars with hook along x-axis

RebarGroup = TwoTiesSixRebars.makeTwoTiesSixRebars(
    l_cover_of_ties=40,
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    main_rebars_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    ties_sequence=("Tie1", "Tie2"),
    structure=Structure,
    facename="Face6",
)

# For LShaped Rebars with hook along y-axis and tie sequence
 
("Tie2", "Tie1")

RebarGroup = TwoTiesSixRebars.makeTwoTiesSixRebars(
    l_cover_of_ties=40,        
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    main_rebars_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="y-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    ties_sequence=("Tie2", "Tie1"),
    structure=Structure,
    facename="Face6",
)

```

### Edition of Two Ties Six Rebars 

You can change the properties of the ties and rebars with the following function


```python
rebar_group = editTwoTiesSixRebars(
    rebar_group,
    l_cover_of_ties,
    r_cover_of_ties,
    t_cover_of_ties,
    b_cover_of_ties,
    offset_of_ties,
    bent_angle_of_ties,
    extension_factor_of_ties,
    dia_of_ties,
    number_spacing_check,
    number_spacing_value,
    dia_of_main_rebars,
    t_offset_of_rebars,
    b_offset_of_rebars,
    main_rebars_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    ties_sequence=("Tie1", "Tie2"),
    structure=None,
    facename=None,
)

```

-    `rebar_group`is a previously created `ColumnReinforcement` group object.

-   The other parameters are the same as required by the `makeSingleTieFourRebars()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.

#### Example 


```python
from ColumnReinforcement import TwoTiesSixRebars

rebar_group = TwoTiesSixRebars.editTwoTiesSixRebars(
    rebar_group,                                
    l_cover_of_ties=40,        
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    main_rebars_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    ties_sequence=("Tie2", "Tie1"),
    structure=None,
    facename=None,
)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar ColumnReinforcement TwoTiesSixRebars/de
