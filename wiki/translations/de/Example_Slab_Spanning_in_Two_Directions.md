---
- TutorialInfo:   Topic:Example Slab Having L-Shape Rebars Reinforcement Mesh
   Level:Intermediate
   Time:
   Author:Shiv Charan
   FCVersion:0.20
   Files:
---

# Example Slab Spanning in Two Directions/de







## Beschreibung

The [Slab Reinforcement](Arch_Rebar_Slab_Reinforcement.md) tool allows the user to create reinforcing bars inside a Slab [Arch Structure](Arch_Structure.md) object.

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

In this example we will create Slab Reinforcement for Slab spanning in two directions as shown in below figure.

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:800px;"> 
*A Example of Slab Reinforcement of spanning in two directions in Slab [Arch Structure](Arch_Structure.md)*

<img alt="" src=images/Right_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:800px;"> 
*Right view of the given Slab Reinforcement example*

<img alt="" src=images/Front_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:800px;"> 
*Front view of the given Slab Reinforcement example*



## Anwendung

1\. Select any face of a previously created Slab **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object. as shown in below image.

<img alt="" src=images/Selected_face_for_Slab_Arch_Structure.png  style="width:400px;"> 
*Selected face for Slab Arch Structure*

2\. Then select **<img src="images/Arch_Rebar_Slab_Reinforcement.svg" width=16px> [Slab Reinforcement](Arch_Rebar_Slab_Reinforcement.md)** from the rebar tools.

3\. A dialog box will pop-out on screen as shown below.

![](images/Slab_Reinforcement_input_dialog_box.png ) 
*Dialog Box for the Slab Reinforcement*

4\. Select the desired type of cover of reinforcement mesh (Top or Bottom) In example Bottom is selected.

5\. Select the BentShapeRebar rebar type and other input data for rebars in parallel direction of selected face as show in below image.

![](images/Bent_Shape_rebars_in_parallel_with_distribution_rebars_inputs_for_Slab_Reinforcement.png ) 
*Dialog Box for Slab Reinforcement of the Rebars in parallel direction of selected face*

6\. Now click on **Next** button or select Cross Rebars in list view.

7\. Now also select BentShapeRebar rebar type and other desired data for input data for rebars in cross direction of selected face as show in below image.

![](images/Bent_Shape_rebars_in_cross_direction_with_distribution_rebars.png ) 
*Dialog Box for Slab Reinforcement of the Rebars in cross direction of selected face*

8\. Click **OK** or **Apply** or **Finish** to generate Slab reinforcement.

9\. Click **Cancel** to exit the dialog box.



## Eigenschaften

**Properties for Rebars in Parallel Direction to selected face:**

-    **Mesh Cover Along**: It represent alignment of rebar mesh along top or bottom face of structure. It can have two values \"Top\" and \"Bottom\".

-    **Rebar Type**: Type of rebar for parallel rebars for slab reinforcement. It can have four values \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **Front Cover**: The distance between parallel rebar and selected face.

-    **Left Cover**: The distance between the left end of the parallel rebar to the left face of the structure.

-    **Right Cover**: The distance between the right end of the parallel rebar to right face of the structure.

-    **Bottom Cover**: The distance between parallel rebars from the bottom face of the structure.

-    **Top Cover**: The distance between parallel rebars from the top face of the structure.

-    **Rear Cover**: Rear cover for slab reinforcement of parallel rebars.

-    **Anchor Length**: It represents arm\'s length of bent shape parallel rebar when parallel rebar type is BentShapeRebar.

-    **Bent Angle**: It represents angle for bent shape parallel rebar when parallel rebar type is BentShapeRebar.

-    **Rounding**: A rounding value to be applied to the corners of the bars, expressed in times of diameter of parallel rebars.

-    **Diameter**: Diameter of parallel rebars

-    **Amount**: It contains count of parallel rebars.

-    **Spacing**: It contains spacing between parallel rebars.

**Properties of Distribution Rebars for bent shape rebars in parallel Direction to selected face:**

-    **Amount**: It contains count of Distribution Rebars for Bent shape rebars in parallel Direction.

-    **Spacing**: It contains spacing between Distribution Rebars for Bent shape rebars in parallel Direction.

**Properties for Rebars in Cross Direction to selected face:**

-    **Rebar Type**: Type of rebar for cross rebars for slab reinforcement. It can have four values \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **Front Cover**: The distance between cross rebar and selected face.

-    **Left Cover**: The distance between the left end of the cross rebar to the left face of the structure.

-    **Right Cover**: The distance between the right end of the cross rebar to right face of the structure.

-    **Bottom Cover**: The distance between cross rebars from the bottom face of the structure.

-    **Top Cover**: The distance between cross rebars from the top face of the structure.

-    **Rear Cover**: Rear cover for slab reinforcement of cross rebars.

-    **Anchor Length**: It represents arm\'s length of bent shape cross rebar when cross rebar type is BentShapeRebar.

-    **Bent Angle**: It represents angle for bent shape cross rebar when cross rebar type is BentShapeRebar.

-    **Rounding**: A rounding value to be applied to the corners of the bars, expressed in times of diameter of cross rebars.

-    **Diameter**: Diameter of cross rebars

-    **Amount**: It contains count of cross rebars.

-    **Spacing**: It contains spacing between cross rebars.

**Properties of Distribution Rebars for bent shape rebars in cross Direction to selected face:**

-    **Amount**: It contains count of Distribution Rebars for Bent shape rebars in cross Direction.

-    **Spacing**: It contains spacing between Distribution Rebars for Bent shape rebars in cross Direction.



## Skripten


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Slab Reinforcement tool can be used from the [Python](Python.md) console by using the following function:

### Create Slab Reinforcementof Slab Spanning in Two directions 

To create Slab reinforcement spanning two direction as shown in above figures you can use makeSlabReinforcement function as follows:


```python
from SlabReinforcement.SlabReinforcement import makeSlabReinforcement
SlabReinforcementGroup = makeSlabReinforcement(
    parallel_rebar_type="BentShapeRebar",
    parallel_front_cover=20,
    parallel_rear_cover=20,
    parallel_left_cover=10,
    parallel_right_cover=10,
    parallel_top_cover=30,
    parallel_bottom_cover=20,
    parallel_diameter=8,
    parallel_amount_spacing_check=True,
    parallel_amount_spacing_value=10,
    cross_rebar_type="BentShapeRebar",
    cross_front_cover=20,
    cross_rear_cover=20,
    cross_left_cover=10,
    cross_right_cover=10,
    cross_top_cover=29,
    cross_bottom_cover=20,
    cross_diameter=8,
    cross_amount_spacing_check=True,
    cross_amount_spacing_value=10,
    cross_rounding=2,
    cross_bent_bar_length=150,
    cross_bent_bar_angle=135,
    cross_distribution_rebars_check = True,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 4,
    parallel_rounding=2,
    parallel_bent_bar_length=150,
    parallel_bent_bar_angle=135,
    parallel_distribution_rebars_check = True,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 4,
    mesh_cover_along = "Bottom",
    structure=App.getDocument("slab").getObject("Beam"),
    facename='Face4',
)
```

-   Creates a `SlabReinforcementGroup` object for slab spanning in two direction from the given `structure`, which is a Slab [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

**Properties used for slab spanning in two direction for scripting**

**Properties for Rebars in Parallel Direction to selected face:**

-    **parallel_rebar_type**: Type of rebar for parallel rebars for slab reinforcement. It can have four values \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **parallel_front_cover**: The distance between parallel rebar and selected face.

-    **parallel_rear_cover**: Rear cover for slab reinforcement of parallel rebars.

-    **parallel_left_cover**: The distance between the left end of the parallel rebar to the left face of the structure.

-    **parallel_right_cover**: The distance between the right end of the parallel rebar to right face of the structure.

-    **parallel_top_cover**: The distance between parallel rebars from the top face of the structure.

-    **parallel_bottom_cover**: The distance between parallel rebars from the bottom face of the structure.

-    **parallel_diameter**: Diameter of parallel rebars.

-    **parallel_amount_spacing_check**: If is set to True, then value of parallel_amount_spacing_value is used as rebars count else parallel_amount_spacing_value\'s value is used as spacing in parallel rebars.

-    **parallel_amount_spacing_value**: It contains count of rebars or spacing between parallel rebars based on value of amount_spacing_check.

-    **parallel_rounding**: A rounding value to be applied to the corners of the bars, expressed in times the parallel_diameter.

-    **parallel_bent_bar_length**: It represents arm\'s length of bent shape parallel rebar when parallel_rebar_type is BentShapeRebar

-    **parallel_bent_bar_angle**: It represents angle for bent shape parallel rebar when parallel_rebar_type is BentShapeRebar

-    **parallel_distribution_rebars_check**: If True add distribution rebars for parallel bent shape rebars. Default is False.

-    **parallel_distribution_rebars_diameter**: Diameter of distribution rebars for parallel bent shape rebars.

-    **parallel_distribution_rebars_amount_spacing_check**: If is set to True, then value of parallel_distribution_rebars_amount_spacing_value is used as rebars count else parallel_distribution_rebars_amount_spacing_value\'s value is used as spacing in parallel_distribution_rebars. Default is True.

-    **parallel_distribution_rebars_amount_spacing_value**: It contains count or spacing between distribution rebars for one side of parallel bent shape rebars based on value of parallel_distribution_rebars_check. Default is 2.

**Properties for Rebars in Cross Direction to selected face:**

-    **cross_rebar_type**: Type of rebar for cross rebars for slab reinforcement. It can have four values \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **cross_front_cover**: The distance between cross rebar and cross_face (face perpendicular to selected face).

-    **cross_rear_cover**: Rear cover for slab reinforcement of cross rebars.

-    **cross_left_cover**: The distance between the left end of the cross rebar to the left face of the structure.

-    **cross_right_cover**: The distance between the right end of the rebar to right face of the structure relative to cross_face.

-    **cross_top_cover**: The distance between cross rebar from the top face of the structure.

-    **cross_bottom_cover**: The distance between cross rebar from the bottom face of the structure.

-    **cross_diameter**: Diameter of cross rebars.

-    **cross_amount_spacing_check**: If is set to True, then value of cross_amount_spacing_value is used as rebars count else cross_amount_spacing_value\'s value is used as spacing in rebars.

-    **cross_amount_spacing_value**: It contains count of rebars or spacing between rebars based on value of cross_amount_spacing_check.

-    **cross_rounding**: A rounding value to be applied to the corners of the bars, expressed in times the cross_diameter.

-    **cross_bent_bar_length**: It represents arm\'s length of bent shape cross rebar when cross_rebar_type is BentShapeRebar

-    **cross_bent_bar_angle**: It represents angle for bent shape cross rebar when cross_rebar_type is BentShapeRebar

-    **cross_distribution_rebars_check**: If True add distribution rebars for cross bent shape rebars. Default is False.

-    **cross_distribution_rebars_diameter**: Diameter for distribution rebars for cross bent shape rebars.

-    **cross_distribution_rebars_amount_spacing_check**: If is set to True, then value of cross_distribution_rebars_amount_spacing_value is used as rebars count else cross_distribution_rebars_amount_spacing_value\'s value is used as spacing in cross_distribution_rebars. Default is True.

-    **cross_distribution_rebars_amount_spacing_value**: It contains count or spacing between distribution rebars for one side of cross bent shape rebars based on value of cross_distribution_rebars_check. Default is 2.

**Common Properties for Parallel and Cross Rebars:**

-    **mesh_cover_along**: It can have two values \"Top\" and \"Bottom\". It represent alignment of rebar mesh along top or bottom face of structure.

-    **structure**: Arch structure object. Default is None

-    **facename**: selected face of structure. Default is None

### Edition of Slab Reinforcement of Slab Spanning in Two directions 

You can change the properties of the Slab Reinforcement for slab spanning in two direction by using editSlabReinforcement function as follows


```python
from SlabReinforcement.SlabReinforcement import editSlabReinforcement
SlabReinforcementGroup = editSlabReinforcement(
    SlabReinforcementGroup,
    parallel_rebar_type="BentShapeRebar",
    parallel_front_cover=20,
    parallel_rear_cover=20,
    parallel_left_cover=10,
    parallel_right_cover=10,
    parallel_top_cover=30,
    parallel_bottom_cover=20,
    parallel_diameter=8,
    parallel_amount_spacing_check=True,
    parallel_amount_spacing_value=15,
    cross_rebar_type="BentShapeRebar",
    cross_front_cover=20,
    cross_rear_cover=20,
    cross_left_cover=10,
    cross_right_cover=10,
    cross_top_cover=29,
    cross_bottom_cover=20,
    cross_diameter=8,
    cross_amount_spacing_check=True,
    cross_amount_spacing_value=15,
    cross_rounding=2,
    cross_bent_bar_length=150,
    cross_bent_bar_angle=135,
    cross_distribution_rebars_check = True,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 4,
    parallel_rounding=2,
    parallel_bent_bar_length=150,
    parallel_bent_bar_angle=135,
    parallel_distribution_rebars_check = True,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 4,
    mesh_cover_along = "Bottom",
    structure=App.getDocument("slab").getObject("Beam"),
    facename='Face4',
)
```

-    `slabReinforcementGroup`is a previously created `Slab Reinforcement` group object.

-   The other parameters are the same as required by the `makeSingleTieFourRebars()` function.

Here we are editing count of rebars in parallel and cross. But you can change any property to edit Slab Reinforcement.



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Category_Arch.md) > Example Slab Spanning in Two Directions/de
