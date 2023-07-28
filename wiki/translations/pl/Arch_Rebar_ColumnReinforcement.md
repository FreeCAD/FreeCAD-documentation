---
- GuiCommand:
   Name:Arch Rebar ColumnReinforcement
   MenuLocation:Arch → Rebar tools → Column Reinforcement<br>3D/BIM → Reinforcement tools → Column Reinforcement
   Workbenches:[Arch](Arch_Workbench.md), [BIM](BIM_Workbench.md)
   Version:0.19
   SeeAlso:[Reinforcement](Reinforcement_Workbench.md), [Arch Rebar](Arch_Rebar.md), [Arch Helical Rebar](Arch_Rebar_Helical.md), [Arch ColumnReinforcement TwoTiesSixRebars](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars.md)
---

# Arch Rebar ColumnReinforcement/pl

## Description

The [Column Reinforcement](Arch_Rebar_ColumnReinforcement.md) tool allows the user to create reinforcing bars inside a Column [Arch Structure](Arch_Structure.md) object.

The [Column Reinforcement](Arch_Rebar_ColumnReinforcement.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_ColumnReinforcement_example.png  style="width:400px;"> 
*Column Reinforcement inside a Column [Arch Structure](Arch_Structure.md)*

## Usage

1\. Select any face of a previously created **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object.
2. Then select **<img src="images/Arch_Rebar_ColumnReinforcement.svg" width=16px> [Column Reinforcement](Arch_Rebar_ColumnReinforcement.md)** from the rebar tools.
3. A dialog box will pop-out on screen as shown below.
<img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;">
*Dialog Box for the Arch Rebar ColumnReinforcement tool*

4\. Select the desired type of column reinforcement.
5. Give inputs for data related to ties.
6. Click **Next** and the dialog box will be updated as shown below.
<img alt="" src=images/ColumnReinforcementDialog_MainRebars.png  style="width:700px;">
*Dialog Box for Main Rebars data*

7\. Select desired rebar type and fill data for main rebars.
8. Click **Next** and the dialog box will be updated as shown below.
<img alt="" src=images/ColumnReinforcementDialog_XDirRebars.png  style="width:700px;">
*Dialog Box for XDirection Rebars data*

9\. Select desired rebar type and fill data for xdirection rebars.
10. Click **Next** and the dialog box will be updated as shown below.
<img alt="" src=images/ColumnReinforcementDialog_YDirRebars.png  style="width:700px;">
*Dialog Box for YDirection Rebars data*

11\. Select desired rebar type and fill data for ydirection rebars.
12. Click **OK** or **Apply** to generate column reinforcement.
13. Click **Cancel** to exit the dialog box.

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

**Main Rebars:** Rebars present at corners of tie

-    **Rebar Type**: Type of main rebars.

-    **Hook Orientation**: Orientation of LShaped hooks.

-    **Hook Extend Along**: Direction for hook extension.

-    **Hook Extension**: Length of hook of LShape rebars.

-    **Rounding**: A rounding value to be applied to the corners of the LShape rebars, expressed in times the diameter.

-    **Top Offset**: The distance between rebar from the top face of the structure.

-    **Bottom Offset**: The distance between rebar from the bottom face of the structure.

-    **Diameter**: Diameter of the main rebars.

**XDir Secondary Rebars:** Rebars along x-direction except main rebars

-    **Rebar Type**: Type of x-direction rebars.

-    **Hook Orientation**: Orientation of LShaped hooks.

-    **Hook Extension**: Length of hook of LShape rebars.

-    **Rounding**: A rounding value to be applied to the corners of the LShape rebars, expressed in times the diameter.

-    **Top Offset**: The distance between rebar from the top face of the structure.

-    **Bottom Offset**: The distance between rebar from the bottom face of the structure.

-    **Number#Diameter**: Number#Diameter set of the x-direction rebars.

**YDir Secondary Rebars:** Rebars along y-direction except main rebars

-    **Rebar Type**: Type of y-direction rebars.

-    **Hook Orientation**: Orientation of LShaped hooks.

-    **Hook Extension**: Length of hook of LShape rebars.

-    **Rounding**: A rounding value to be applied to the corners of the LShape rebars, expressed in times the diameter.

-    **Top Offset**: The distance between rebar from the top face of the structure.

-    **Bottom Offset**: The distance between rebar from the bottom face of the structure.

-    **Number#Diameter**: Number#Diameter set of the y-direction rebars.

## Scripting


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The ColumnReinforcement tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:

### Create Single Tie Four Rebars 


```python
RebarGroup = makeSingleTieFourRebars(
    l_cover_of_tie,
    r_cover_of_tie,
    t_cover_of_tie,
    b_cover_of_tie,
    offset_of_tie,
    bent_angle,
    extension_factor,
    dia_of_tie,
    number_spacing_check,
    number_spacing_value,
    dia_of_rebars,
    t_offset_of_rebars,
    b_offset_of_rebars,
    rebar_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    structure=None,
    facename=None,
).rebar_group

```

-   Creates a `RebarGroup` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `l_cover_of_tie`, `r_cover_of_tie`, `t_cover_of_tie`, `b_cover_of_tie` and `offset_of_tie` are inner offset distances for the tie elements with respect to the faces of the structure. They are respectively the left, right, top, bottom and front/rear offsets.

-    `bent_angle`define the angle of the tip of the reinforcement loop.

-    `extension_factor`define the length of the tip of the reinforcement loop, expressed in times the diameter.

-    `dia_of_tie`is the diameter of the ties.

-    `number_spacing_check`if it is `True` it will create as many ties as given by `number_spacing_value`; if it is `False` it will create ties separated by the numerical value of `number_spacing_value`.

-    `number_spacing_value`specifies the number of ties, or the value of the separation between them, depending on `number_spacing_check`.

-    `dia_of_rebars`is the diameter of the main rebars.

-    `t_offset_of_rebars`and `b_offset_of_rebars` are inner offset distances for the main rebars with respect to the top and bottom faces of the structure, respectively.

-    `rebar_type`is the type of the main rebars; it can be `"StraightRebar"` or `"LShapeRebar"`.

-    `hook_orientation`specifies the orientation of LShaped hook; it can be: `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` or `"Bottom Left"`.

-    `hook_extend_along`specifies direction for hook extension; it can be `"x-axis"` or `"y-axis"`.

-    `l_rebar_rounding`is the parameter that determines the bending radius of the LShaped main rebars, expressed as times the diameter.

-    `hook_extension`is the length of hook of LShaped rebars.

#### Example


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import SingleTie

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# For Straight Rebars

RebarGroup = SingleTie.makeSingleTieFourRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=40,
    b_offset_of_rebars=40,
    rebar_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    structure=Structure,
    facename="Face6",
).rebar_group

# For LShaped Rebars with hook along x-axis

RebarGroup = SingleTie.makeSingleTieFourRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    rebar_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    structure=Structure,
    facename="Face6",
).rebar_group

# For LShaped Rebars with hook along y-axis

RebarGroup = SingleTie.makeSingleTieFourRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    rebar_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="y-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    structure=Structure,
    facename="Face6",
).rebar_group

```

### Create Single Tie Multiple Rebars 


```python
RebarGroup = makeSingleTieMultipleRebars(
    l_cover_of_tie,
    r_cover_of_tie,
    t_cover_of_tie,           
    b_cover_of_tie,                      
    offset_of_tie,                       
    bent_angle,                          
    extension_factor,
    dia_of_tie,     
    number_spacing_check,
    number_spacing_value,
    dia_of_main_rebars,
    main_rebars_t_offset,
    main_rebars_b_offset,
    main_rebars_type="StraightRebar",
    main_hook_orientation="Top Inside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=None,
    main_hook_extension=None,
    sec_rebars_t_offset=None,
    sec_rebars_b_offset=None,
    sec_rebars_number_diameter=None,
    sec_rebars_type=("StraightRebar", "StraightRebar"),
    sec_hook_orientation=("Top Inside", "Top Inside"),
    l_sec_rebar_rounding=None,
    sec_hook_extension=None,
    structure=None,
    facename=None,
)

```

-   Creates a `RebarGroup` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `l_cover_of_tie`, `r_cover_of_tie`, `t_cover_of_tie`, `b_cover_of_tie` and `offset_of_tie` are inner offset distances for the tie elements with respect to the faces of the structure. They are respectively the left, right, top, bottom and front/rear offsets.

-    `bent_angle`define the angle of the tip of the reinforcement loop.

-    `extension_factor`define the length of the tip of the reinforcement loop, expressed in times the diameter.

-    `dia_of_tie`is the diameter of the ties.

-    `number_spacing_check`if it is `True` it will create as many ties as given by `number_spacing_value`; if it is `False` it will create ties separated by the numerical value of `number_spacing_value`.

-    `number_spacing_value`specifies the number of ties, or the value of the separation between them, depending on `number_spacing_check`.

-    `dia_of_main_rebars`is the diameter of the main rebars.

-    `main_rebars_t_offset`and `main_rebars_b_offset` are inner offset distances for the main rebars with respect to the top and bottom faces of the structure, respectively.

-    `main_rebars_type`is the type of the main rebars; it can be `"StraightRebar"` or `"LShapeRebar"`.

-    `main_hook_orientation`specifies the orientation of main LShaped hook; it can be: `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` or `"Bottom Left"`.

-    `main_hook_extend_along`specifies direction for main hook extension; it can be `"x-axis"` or `"y-axis"`.

-    `l_main_rebar_rounding`is the parameter that determines the bending radius of the LShaped main rebars, expressed as times the diameter.

-    `main_hook_extension`is the length of hook of main LShaped rebars.

-    `sec_rebars_t_offset`and `sec_rebars_b_offset` are tuples (xdir_rebars_t\_offset, ydir_rebars_t\_offset) and (xdir_rebars_b\_offset, ydir_rebars_b\_offset) respectively, that defines inner offset distances for the secondary x-direction and y-direction rebars with respect to the top and bottom faces of the structure, respectively.

-    `sec_rebars_number_diameter`is a tuple (xdir_rebars_number_diameter, ydir_rebars_number_diameter) that defines number#diameter set of the secondary x-direction and y-direction rebars, respectively.

-    `sec_rebars_type`is a tuple (xdir_rebars_type, ydir_rebars_type) that defines the type of secondary x-direction and y-direction rebars ,respectively; it can have `"StraightRebar"` or `"LShapeRebar"` as rebar type.

-    `sec_hook_orientation`is a tuple (xdir_hook_orientation, ydir_hook_orientation) that defines the orientation of secondary x-direction and y-direction LShaped hook; it can have `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` or `"Bottom Left"` as hook_orientation.

-    `l_sec_rebar_rounding`is a tuple (l_xdir_rebar_rounding, l_ydir_rebar_rounding) that determines the bending radius of the LShaped secondary x-direction and y-direction LShaped rebars, expressed as times the diameter of x-direction and y-direction LShaped rebars, respectively.

-    `sec_hook_extension`is a tuple (xdir_hook_extension, ydir_hook_extension) that defines the length of hook of secondary x-direction and y-direction LShaped rebars.

#### Example 


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import SingleTieMultipleRebars

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

RebarGroup = SingleTieMultipleRebars.makeSingleTieMultipleRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    main_rebars_t_offset=-40,
    main_rebars_b_offset=-40,
    main_rebars_type="LShapeRebar",
    main_hook_orientation="Top Outside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=2,
    main_hook_extension=40,
    sec_rebars_t_offset=(-40, -40),
    sec_rebars_b_offset=(-40, -40),
    sec_rebars_number_diameter=("2#20mm+1#16mm+2#20mm", "1#20mm+1#16mm+1#20mm"),
    sec_rebars_type=("LShapeRebar", "LShapeRebar"),
    sec_hook_orientation=("Top Outside", "Top Outside"),
    l_sec_rebar_rounding=(2, 2),
    sec_hook_extension=(40, 40),
    structure=Structure,
    facename="Face6",
)

```

### Edition of Single Tie Four Rebars 

You can change the properties of the ties and rebars with the following function


```python
rebar_group = editSingleTieFourRebars(
    rebar_group,
    l_cover_of_tie,
    r_cover_of_tie,    
    t_cover_of_tie,           
    b_cover_of_tie,
    offset_of_tie,
    bent_angle,
    extension_factor,
    dia_of_tie,
    number_spacing_check,
    number_spacing_value,
    dia_of_rebars,
    t_offset_of_rebars,
    b_offset_of_rebars,
    rebar_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    structure=None,
    facename=None,
)

```

-    `rebar_group`is a previously created `ColumnReinforcement` group object.

-   The other parameters are the same as required by the `makeSingleTieFourRebars()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.

#### Example 


```python
from ColumnReinforcement import SingleTie

rebar_group = SingleTie.editSingleTieFourRebars(
    rebar_group,                                
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    rebar_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    structure=None,
    facename=None,
)

```

### Edition of Single Tie Multiple Rebars 

You can change the properties of the ties and rebars with the following function


```python
rebar_group = editSingleTieMultipleRebars(
    rebar_group,
    l_cover_of_tie,      
    r_cover_of_tie,       
    t_cover_of_tie,                       
    b_cover_of_tie,                       
    offset_of_tie,                        
    bent_angle,
    extension_factor,
    dia_of_tie,
    number_spacing_check,
    number_spacing_value,
    dia_of_main_rebars,
    main_rebars_t_offset,
    main_rebars_b_offset,
    main_rebars_type="StraightRebar",
    main_hook_orientation="Top Inside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=None,
    main_hook_extension=None,
    sec_rebars_t_offset=None,
    sec_rebars_b_offset=None,
    sec_rebars_number_diameter=None,
    sec_rebars_type=("StraightRebar", "StraightRebar"),
    sec_hook_orientation=("Top Inside", "Top Inside"),
    l_sec_rebar_rounding=None,
    sec_hook_extension=None,
    structure=None,
    facename=None,
)

```

-    `rebar_group`is a previously created `ColumnReinforcement` group object.

-   The other parameters are the same as required by the `makeSingleTieMultipleRebars()` function.

-    `structure`and `facename` may be omitted so that the reinforcement stays in the original structure.

#### Example 


```python
from ColumnReinforcement import SingleTieMultipleRebars

rebar_group = SingleTieMultipleRebars.editSingleTieMultipleRebars(
    rebar_group,                                
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    main_rebars_t_offset=-40,
    main_rebars_b_offset=-40,
    main_rebars_type="LShapeRebar",
    main_hook_orientation="Top Outside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=2,
    main_hook_extension=40,
    sec_rebars_t_offset=(-40, -40),
    sec_rebars_b_offset=(-40, -40),
    sec_rebars_number_diameter=("2#20mm+1#16mm+2#20mm", "1#20mm+1#16mm+1#20mm"),
    sec_rebars_type=("StraightRebar", "StraightRebar"),
    sec_hook_orientation=None,
    l_sec_rebar_rounding=None,
    sec_hook_extension=None,
    structure=None,
    facename=None,
)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar ColumnReinforcement/pl
