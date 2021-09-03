---
- GuiCommand:
   Name:Arch Rebar ColumnReinforcement
   MenuLocation:Reinforcement → Column Reinforcement, Arch → Rebar tools
   Workbenches:[Arch](Arch_Workbench.md), [BIM](BIM_Workbench.md)
   Version:0.19
   SeeAlso:[Reinforcement](Reinforcement_Workbench.md), [Arch ColumnReinforcement TwoTiesSixRebars](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars.md), [Arch Rebar](Arch_Rebar.md)
---

## Descrição

The [Column Reinforcement](Arch_Rebar_Circular_ColumnReinforcement.md) tool allows the user to create reinforcing bars inside a Column [Arch Structure](Arch_Structure.md) object.

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_Circular_ColumnReinforcement_example.png  style="width:400px;"> 
*Circular Column Reinforcement inside a Column [Arch Structure](Arch_Structure.md)*

## Utilização

1\. Select top face of a previously created **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object.
2. Then select **<img src="images/Arch_Rebar_ColumnReinforcement.svg" width=16px> [Column Reinforcement](Arch_Rebar_ColumnReinforcement.md)** from the rebar tools.
3. A dialog box will pop-out on screen as shown below.

<img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;"> 
*Dialog Box for the Arch Rebar ColumnReinforcement tool*

4\. Select the Circular Column radio button in column reinforcement dialog.

<img alt="" src=images/CircularColumnReinforcementDialog.png  style="width:700px;"> 
*Dialog Box for Circular Column Reinforcement*

5\. Give inputs for data related to circular column reinforcement.
6. Click **OK** or **Apply** to generate circular column reinforcement.

7\. Click **Cancel** to exit the dialog box.

## Propriedades

**Helical Rebars:**

-    **Side Cover**: The distance between rebar to the curved face.

-    **Top Cover**: The distance between rebar from the top face of the structure.

-    **Bottom Cover**: The distance between rebar from the bottom face of the structure.

-    **Pitch**: The pitch of a helix is the height of one complete helix turn, measured parallel to the axis of the helix.

-    **Diameter**: Diameter of the rebar.

**Main Rebars:**

-    **Top Offset**: The distance between rebars from the top face of the structure.

-    **Bottom Offset**: The distance between rebars from the bottom face of the structure.

-    **Diameter**: Diameter of the main rebars.

-    **Number**: The number of main rebars.

-    **Angle**: The angular distance between ties.

## Scripting


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The ColumnReinforcement tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function:

### Create Circular Column Reinforcement 


```python
RebarGroup = CircularColumn.makeReinforcement(
    s_cover,
    helical_rebar_t_offset,
    helical_rebar_b_offset,
    pitch,
    dia_of_helical_rebar,
    main_rebars_t_offset,
    main_rebars_b_offset,
    dia_of_main_rebars,
    number_angle_check,
    number_angle_value,
    structure=None,
    facename=None,
)

```

-   Creates a `RebarGroup` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `s_cover`, `helical_rebar_t_offset`, and `helical_rebar_b_offset` are inner offset distances for the helical rebar with respect to the faces of the structure. They are respectively the side, top and bottom offsets.

-    `pitch`is the parameter that determines how close or far apart each helical loop is to each other.

-    `dia_of_helical_rebar`is the diameter of the helical rebar inside the structure.

-    `main_rebars_t_offset`and `main_rebars_b_offset` are inner offset distances for the main rebars with respect to the top and bottom faces of the structure, respectively.

-    `dia_of_main_rebars`is the diameter of the main rebars.

-    `number_angle_check`if it is `True` it will create as many main rebars as given by `number_angle_value`; if it is `False` it will create main rebars at an angle of `number_spacing_value`, specified in degrees.

-    `number_angle_value`specifies the number of main rebars, or the value of the angle between the main rebars, depending on `number_angle_check`.

#### Exemplo


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import CircularColumn

Circle = Draft.makeCircle(radius=250)
Structure = Arch.makeStructure(Circle)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

RebarGroup = CircularColumn.makeReinforcement(
    s_cover=20,
    helical_rebar_t_offset=40,
    helical_rebar_b_offset=40,
    pitch=50,
    dia_of_helical_rebar=8,
    main_rebars_t_offset=20,
    main_rebars_b_offset=20,
    dia_of_main_rebars=16,
    number_angle_check=True,
    number_angle_value=6,
    structure=Structure,
    facename="Face3",
).rebar_group

```

### Edition of Circular Column Reinforcement 

You can change the properties of the helical and main rebars with the following function


```python
rebar_group = editReinforcement(
    rebar_group,
    s_cover,
    helical_rebar_t_offset,
    helical_rebar_b_offset,
    pitch,
    dia_of_helical_rebar,
    main_rebars_t_offset,
    main_rebars_b_offset,
    dia_of_main_rebars,
    number_angle_check,
    number_angle_value,
    structure=None,
    facename=None,
)

```

-    `rebar_group`is a previously created `ColumnReinforcement` group object.

-   The other parameters are the same as required by the `makeSingleTieFourRebars()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.

#### Exemplo 


```python
from ColumnReinforcement import CircularColumn

rebar_group = CircularColumn.editReinforcement(
    rebar_group,
    s_cover=30,
    helical_rebar_t_offset=30,
    helical_rebar_b_offset=30,
    pitch=60,
    dia_of_helical_rebar=10,
    main_rebars_t_offset=-30,
    main_rebars_b_offset=-30,
    dia_of_main_rebars=18,
    number_angle_check=False,
    number_angle_value=45,
    structure=Structure,
    facename="Face3",
)

```


<div class="mw-translate-fuzzy">





</div>







[Category:Reinforcement{{\#translation:}}](Category:Reinforcement.md)
