---
- GuiCommand   *
   Name   *Arch Rebar Slab Reinforcement
   MenuLocation   *Arch → Rebar tools → Slab Reinforcement<br>3D/BIM → Reinforcement tools → Slab Reinforcement
   Workbenches   *[Arch](Arch_Workbench.md)
   SeeAlso   *[Reinforcement](Reinforcement_Workbench.md), [Arch Rebar](Arch_Rebar.md), [Arch Helical Rebar](Arch_Rebar_Helical.md)
---

# Arch Rebar Slab Reinforcement/en

## Description

The [Slab Reinforcement](Arch_Rebar_Slab_Reinforcement.md) tool allows the user to create reinforcing bars inside a Slab [Arch Structure](Arch_Structure.md) object.

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width   *800px;"> 
*A Example of Slab Reinforcement inside a Slab [Arch Structure](Arch_Structure.md)*

<img alt="" src=images/Right_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width   *800px;"> 
*Right view of the given Slab Reinforcement example*

<img alt="" src=images/Front_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width   *800px;"> 
*Front view of the given Slab Reinforcement example*

## Usage

1\. Select any face of a previously created Slab **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object. as shown in below image.

<img alt="" src=images/Selected_face_for_Slab_Arch_Structure.png  style="width   *400px;"> 
*Selected face for Slab Arch Structure*

2\. Then select **<img src="images/Arch_Rebar_Slab_Reinforcement.svg" width=16px> [Slab Reinforcement](Arch_Rebar_Slab_Reinforcement.md)** from the rebar tools.

3\. A dialog box will pop-out on screen as shown below.

![](images/Slab_Reinforcement_input_dialog_box.png ) 
*Dialog Box for the Slab Reinforcement*

4\. Select the desired type of cover of reinforcement mesh (Top or Bottom).

5\. Select the desired rebar type and other input data for rebars in parallel direction of selected face as show in below image.

![](images/Bent_Shape_rebars_in_parallel_with_distribution_rebars_inputs_for_Slab_Reinforcement.png ) 
*Dialog Box for Slab Reinforcement of the Rebars in parallel direction of selected face*

6\. Now click on **Next** button or select Cross Rebars in list view.

7\. Now select desired data for input data for rabars in cross direction of selected face as show in below image.

![](images/Bent_Shape_rebars_in_cross_direction_with_distribution_rebars.png ) 
*Dialog Box for Slab Reinforcement of the Rebars in cross direction of selected face*

8\. Click **OK** or **Apply** or **Finish** to generate Slab reinforcement.

9\. Click **Cancel** to exit the dialog box.

## Properties

**Properties for Rebars in Parallel Direction to selected face   ***

-    **Mesh Cover Along**   * It represent alignment of rebar mesh along top or bottom face of structure. It can have two values \"Top\" and \"Bottom\".

-    **Rebar Type**   * Type of rebar for parallel rebars for slab reinforcement. It can have four values \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **Front Cover**   * The distance between parallel rebar and selected face.

-    **Left Cover**   * The distance between the left end of the parallel rebar to the left face of the structure.

-    **Right Cover**   * The distance between the right end of the parallel rebar to right face of the structure.

-    **Bottom Cover**   * The distance between parallel rebars from the bottom face of the structure.

-    **Top Cover**   * The distance between parallel rebars from the top face of the structure.

-    **Rear Cover**   * Rear cover for slab reinforcement of parallel rebars.

-    **Anchor Length**   * It represents arm\'s length of bent shape parallel rebar when parallel rebar type is BentShapeRebar.

-    **Bent Angle**   * It represents angle for bent shape parallel rebar when parallel rebar type is BentShapeRebar.

-    **Rounding**   * A rounding value to be applied to the corners of the bars, expressed in times of diameter of parallel rebars.

-    **Diameter**   * Diameter of parallel rebars

-    **Amount**   * It contains count of parallel rebars.

-    **Spacing**   * It contains spacing between parallel rebars.

**Properties of Distribution Rebars for bent shape rebars in parallel Direction to selected face   ***

-    **Amount**   * It contains count of Distribution Rebars for Bent shape rebars in parallel Direction.

-    **Spacing**   * It contains spacing between Distribution Rebars for Bent shape rebars in parallel Direction.

**Properties for Rebars in Cross Direction to selected face   ***

-    **Rebar Type**   * Type of rebar for cross rebars for slab reinforcement. It can have four values \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **Front Cover**   * The distance between cross rebar and selected face.

-    **Left Cover**   * The distance between the left end of the cross rebar to the left face of the structure.

-    **Right Cover**   * The distance between the right end of the cross rebar to right face of the structure.

-    **Bottom Cover**   * The distance between cross rebars from the bottom face of the structure.

-    **Top Cover**   * The distance between cross rebars from the top face of the structure.

-    **Rear Cover**   * Rear cover for slab reinforcement of cross rebars.

-    **Anchor Length**   * It represents arm\'s length of bent shape cross rebar when cross rebar type is BentShapeRebar.

-    **Bent Angle**   * It represents angle for bent shape cross rebar when cross rebar type is BentShapeRebar.

-    **Rounding**   * A rounding value to be applied to the corners of the bars, expressed in times of diameter of cross rebars.

-    **Diameter**   * Diameter of cross rebars

-    **Amount**   * It contains count of cross rebars.

-    **Spacing**   * It contains spacing between cross rebars.

**Properties of Distribution Rebars for bent shape rebars in cross Direction to selected face   ***

-    **Amount**   * It contains count of Distribution Rebars for Bent shape rebars in cross Direction.

-    **Spacing**   * It contains spacing between Distribution Rebars for Bent shape rebars in cross Direction.

## Scripting


**See also   ***

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Slab Reinforcement tool can be used from the [Python](Python.md) console by using the following function   *

### Create Slab Reinforcement 


```python
from SlabReinforcement.SlabReinforcement import makeSlabReinforcement
SlabReinforcementGroup = makeSlabReinforcement(
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    cross_amount_spacing_value,
    cross_rounding = 2,
    cross_bent_bar_length = 50,
    cross_bent_bar_angle = 135,
    cross_l_shape_hook_orintation = "Alternate",
    cross_distribution_rebars_check = False,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 2,
    parallel_rounding = 2,
    parallel_bent_bar_length = 50,
    parallel_bent_bar_angle = 135,
    parallel_l_shape_hook_orintation = "Alternate",
    parallel_distribution_rebars_check = False,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 2,
    mesh_cover_along = "Bottom",
    structure = None,
    facename = None,
)
```

-   Creates a `SlabReinforcementGroup` object from the given `structure`, which is a Slab [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

**Properties for Rebars in Parallel Direction to selected face   ***

-    **parallel_rebar_type**   * Type of rebar for parallel rebars for slab reinforcement. It can have four values \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **parallel_front_cover**   * The distance between parallel rebar and selected face.

-    **parallel_rear_cover**   * Rear cover for slab reinforcement of parallel rebars.

-    **parallel_left_cover**   * The distance between the left end of the parallel rebar to the left face of the structure.

-    **parallel_right_cover**   * The distance between the right end of the parallel rebar to right face of the structure.

-    **parallel_top_cover**   * The distance between parallel rebars from the top face of the structure.

-    **parallel_bottom_cover**   * The distance between parallel rebars from the bottom face of the structure.

-    **parallel_diameter**   * Diameter of parallel rebars.

-    **parallel_amount_spacing_check**   * If is set to True, then value of parallel_amount_spacing_value is used as rebars count else parallel_amount_spacing_value\'s value is used as spacing in parallel rebars.

-    **parallel_amount_spacing_value**   * It contains count of rebars or spacing between parallel rebars based on value of amount_spacing_check.

-    **parallel_rounding**   * A rounding value to be applied to the corners of the bars, expressed in times the parallel_diameter.

-    **parallel_bent_bar_length**   * It represents arm\'s length of bent shape parallel rebar when parallel_rebar_type is BentShapeRebar

-    **parallel_bent_bar_angle**   * It represents angle for bent shape parallel rebar when parallel_rebar_type is BentShapeRebar

-    **parallel_l_shape_hook_orintation**   * It represents orintation of hook of parallel L-Shape rebar if parallel_rebar_type is LShapeRebar. It can have three values \"Left\", \"Right\",\"Alternate\"

-    **parallel_distribution_rebars_check**   * If True add distribution rebars for parallel bent shape rebars. Default is False.

-    **parallel_distribution_rebars_diameter**   * Diameter of distribution rebars for parallel bent shape rebars.

-    **parallel_distribution_rebars_amount_spacing_check**   * If is set to True, then value of parallel_distribution_rebars_amount_spacing_value is used as rebars count else parallel_distribution_rebars_amount_spacing_value\'s value is used as spacing in parallel_distribution_rebars. Default is True.

-    **parallel_distribution_rebars_amount_spacing_value**   * It contains count or spacing between distribution rebars for one side of parallel bent shape rebars based on value of parallel_distribution_rebars_check. Default is 2.

**Properties for Rebars in Cross Direction to selected face   ***

-    **cross_rebar_type**   * Type of rebar for cross rebars for slab reinforcement. It can have four values \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **cross_front_cover**   * The distance between cross rebar and cross_face (face perpendicular to selected face).

-    **cross_rear_cover**   * Rear cover for slab reinforcement of cross rebars.

-    **cross_left_cover**   * The distance between the left end of the cross rebar to the left face of the structure.

-    **cross_right_cover**   * The distance between the right end of the rebar to right face of the structure relative to cross_face.

-    **cross_top_cover**   * The distance between cross rebar from the top face of the structure.

-    **cross_bottom_cover**   * The distance between cross rebar from the bottom face of the structure.

-    **cross_diameter**   * Diameter of cross rebars.

-    **cross_amount_spacing_check**   * If is set to True, then value of cross_amount_spacing_value is used as rebars count else cross_amount_spacing_value\'s value is used as spacing in rebars.

-    **cross_amount_spacing_value**   * It contains count of rebars or spacing between rebars based on value of cross_amount_spacing_check.

-    **cross_rounding**   * A rounding value to be applied to the corners of the bars, expressed in times the cross_diameter.

-    **cross_bent_bar_length**   * It represents arm\'s length of bent shape cross rebar when cross_rebar_type is BentShapeRebar

-    **cross_bent_bar_angle**   * It represents angle for bent shape cross rebar when cross_rebar_type is BentShapeRebar

-    **cross_l_shape_hook_orintation**   * It represents orintation of hook of cross L-Shape rebar if cross_rebar_type is LShapeRebar. It can have three values \"Left\", \"Right\", \"Alternate\"

-    **cross_distribution_rebars_check**   * If True add distribution rebars for cross bent shape rebars. Default is False.

-    **cross_distribution_rebars_diameter**   * Diameter for distribution rebars for cross bent shape rebars.

-    **cross_distribution_rebars_amount_spacing_check**   * If is set to True, then value of cross_distribution_rebars_amount_spacing_value is used as rebars count else cross_distribution_rebars_amount_spacing_value\'s value is used as spacing in cross_distribution_rebars. Default is True.

-    **cross_distribution_rebars_amount_spacing_value**   * It contains count or spacing between distribution rebars for one side of cross bent shape rebars based on value of cross_distribution_rebars_check. Default is 2.

**Common Properties for Parallel and Cross Rebars   ***

-    **mesh_cover_along**   * It can have two values \"Top\" and \"Bottom\". It represent alignment of rebar mesh along top or bottom face of structure.

-    **structure**   * Arch structure object. Default is None

-    **facename**   * selected face of structure. Default is None

### Edition of Slab Reinforcement 

You can change the properties of the Slab Reinforcement with the following function


```python
from SlabReinforcement.SlabReinforcement import editSlabReinforcement
slabReinforcementGroup = editSlabReinforcement(
    slabReinforcementGroup,
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    cross_amount_spacing_value,
    cross_rounding = 2,
    cross_bent_bar_length = 50,
    cross_bent_bar_angle = 135,
    cross_l_shape_hook_orintation = "Alternate",
    cross_distribution_rebars_check = False,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 2,
    parallel_rounding = 2,
    parallel_bent_bar_length = 50,
    parallel_bent_bar_angle = 135,
    parallel_l_shape_hook_orintation = "Alternate",
    parallel_distribution_rebars_check = False,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 2,
    mesh_cover_along   * str = "Bottom",
    structure = None,
    facename = None,
)
```

-    `slabReinforcementGroup`is a previously created `Slab Reinforcement` group object.

-   The other parameters are the same as required by the `makeSlabReinforcement()` function.

### Examples for Slab Reinforcement 

-   [Slab Spanning in Two Directions](Example_Slab_Spanning_in_Two_Directions.md)

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width   *800px;">

-   [Slab Spanning in One Direction](Example_Slab_Spanning_in_One_Direction.md)

<img alt="" src=images/Slab_spanning_in_one_Direction.png  style="width   *800px;">

-   [Slab Having Straight Rebars Reinforcement Mesh](Example_Slab_Having_Mesh_Of_Straight_Rebars.md)

<img alt="" src=images/Slab_having_straight_rebars_in_both_direction.png  style="width   *800px;">

-   [Slab Having U-Shape Rebars Reinforcement Mesh](Example_Slab_Having_UShape_Rebars_Reinforcement_Mesh.md)

<img alt="" src=images/U-shape_rebars_isometric_view.png  style="width   *800px;">

-   [Slab Having L-Shape Rebars Reinforcement Mesh](Example_Slab_Having_LShape_Rebars_Reinforcement_Mesh.md)

<img alt="" src=images/L-Shape_Rebars_isometric_view.png  style="width   *800px;">





 

[Category   *Reinforcement](Category_Reinforcement.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Slab Reinforcement/en
