---
- TutorialInfo:   Topic:Example Slab Having U-Shape Rebars Reinforcement Mesh
   Level:Intermediate
   Time:
   Author:Shiv Charan
   FCVersion:0.20
   Files:
---

# Example Slab Having UShape Rebars Reinforcement Mesh/pl





## Description

The [Slab Reinforcement](Arch_Rebar_Slab_Reinforcement.md) tool allows the user to create reinforcing bars inside a Slab [Arch Structure](Arch_Structure.md) object.

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

In this example we will create Slab Reinforcement having U-Shape Rebars for both direction as shown in below figure.

<img alt="" src=images/U-shape_rebars_isometric_view.png  style="width:800px;"> 
*A Example of Slab Reinforcement having U-Shape Rebars in Slab [Arch Structure](Arch_Structure.md)*

## Usage

1\. Select any face of a previously created Slab **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object. as shown in below image.

<img alt="" src=images/Selected_face_for_Slab_Arch_Structure.png  style="width:400px;"> 
*Selected face for Slab Arch Structure*

2\. Then select **<img src="images/Arch_Rebar_Slab_Reinforcement.svg" width=16px> [Slab Reinforcement](Arch_Rebar_Slab_Reinforcement.md)** from the rebar tools.

3\. A dialog box will pop-out on screen as shown below.

![](images/Slab_Reinforcement_input_dialog_box.png ) 
*Dialog Box for the Slab Reinforcement*

4\. Select the desired type of cover of reinforcement mesh (Top or Bottom) In example Bottom is selected.

5\. Select the UShapeRebar rebar type and other input data for radars in parallel direction of selected face as show in below image.

![](images/U-shape_parallel_rebars_inputs.png ) 
*Dialog Box for Slab Reinforcement of the Rebars in parallel direction of selected face*

6\. Now click on **Next** button or select Cross Rebars in list view.

7\. Now select UShapeRebar rebar type and other desired data for input data for rebars in cross direction of selected face as show in below image.

![](images/U-Shape_rebars_in_cross_direction_inputs.png ) 
*Dialog Box for Slab Reinforcement of the Rebars in cross direction of selected face*

8\. Click **OK** or **Apply** or **Finish** to generate Slab reinforcement.

9\. Click **Cancel** to exit the dialog box.

## Properties Used for Slab Reinforcement Having U-Shape Rebars 

**Properties for Rebars in Parallel Direction to selected face:**

-   {{ PropertyData\|Mesh Cover Along}}: It represent alignment of rebar mesh along top or bottom face of structure. It can have two values \"Top\" and \"Bottom\".
-   {{ PropertyData\|Rebar Type}}: Type of rebar for parallel rebars for slab reinforcement. It can have four values \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.
-   {{ PropertyData\|Front Cover}}: The distance between parallel rebar and selected face.
-   {{ PropertyData\|Left Cover}}: The distance between the left end of the parallel rebar to the left face of the structure.
-   {{ PropertyData\|Right Cover}}: The distance between the right end of the parallel rebar to right face of the structure.
-   {{ PropertyData\|Bottom Cover}}: The distance between parallel rebars from the bottom face of the structure.
-   {{ PropertyData\|Top Cover}}: The distance between parallel rebars from the top face of the structure.
-   {{ PropertyData\|Rear Cover}}: Rear cover for slab reinforcement of parallel rebars.
-   {{ PropertyData\|Diameter}}: Diameter of parallel rebars.
-   {{ PropertyData\|Rounding}}: A rounding value to be applied to the corners of the bars, expressed in times of diameter of parallel rebars.
-   {{ PropertyData\|Amount}}: It contains count of parallel rebars.
-   {{ PropertyData\|Spacing}}: It contains spacing between parallel rebars.

**Properties for Rebars in Cross Direction to selected face:**

-   {{ PropertyData\|Rebar Type}}: Type of rebar for cross rebars for slab reinforcement. It can have four values \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.
-   {{ PropertyData\|Front Cover}}: The distance between cross rebar and selected face.
-   {{ PropertyData\|Left Cover}}: The distance between the left end of the cross rebar to the left face of the structure.
-   {{ PropertyData\|Right Cover}}: The distance between the right end of the cross rebar to right face of the structure.
-   {{ PropertyData\|Bottom Cover}}: The distance between cross rebars from the bottom face of the structure.
-   {{ PropertyData\|Top Cover}}: The distance between cross rebars from the top face of the structure.
-   {{ PropertyData\|Rear Cover}}: Rear cover for slab reinforcement of cross rebars.
-   {{ PropertyData\|Rounding}}: A rounding value to be applied to the corners of the bars, expressed in times of diameter of cross rebars.
-   {{ PropertyData\|Diameter}}: Diameter of cross rebars
-   {{ PropertyData\|Amount}}: It contains count of cross rebars.
-   {{ PropertyData\|Spacing}}: It contains spacing between cross rebars.

## Scripting


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Slab Reinforcement tool can be used from the [Python](Python.md) console by using the following function:

### Create Slab Reinforcement of U-Shape Rebars 

To create Slab reinforcement U-Shape Rebars as shown in above figures you can use makeSlabReinforcement function as follows:


```python
from SlabReinforcement.SlabReinforcement import makeSlabReinforcement
SlabReinforcementGroup = makeSlabReinforcement(
    parallel_rebar_type="UShapeRebar",
    parallel_front_cover=20,
    parallel_rear_cover=20,
    parallel_left_cover=10,
    parallel_right_cover=10,
    parallel_top_cover=30,
    parallel_bottom_cover=20,
    parallel_rounding=2,
    parallel_diameter=8,
    parallel_amount_spacing_check=True,
    parallel_amount_spacing_value=12,
    cross_rebar_type="UShapeRebar",
    cross_front_cover=20,
    cross_rear_cover=20,
    cross_left_cover=10,
    cross_right_cover=10,
    cross_top_cover=20,
    cross_bottom_cover=20,
    cross_rounding=2,
    cross_diameter=8,
    cross_amount_spacing_check=True,
    cross_amount_spacing_value=12,
    mesh_cover_along = "Bottom",
    structure=App.getDocument("slab").getObject("Beam"),
    facename='Face4',
)
```

-   Creates a `SlabReinforcementGroup` object for slab reinforcement having U-Shape rebars for the given `structure`, which is a Slab [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

**Properties used for slab reinforcement having U-Shape rebars for scripting reinforcement**

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

**Common Properties for Parallel and Cross Rebars:**

-    **mesh_cover_along**: It can have two values \"Top\" and \"Bottom\". It represent alignment of rebar mesh along top or bottom face of structure.

-    **structure**: Arch structure object. Default is None

-    **facename**: selected face of structure. Default is None

### Edition of Slab Reinforcement having U-Shape Rebars 

You can change the properties of the Slab Reinforcement having U-Shape Rebars by using editSlabReinforcement function as follows:


```python
from SlabReinforcement.SlabReinforcement import editSlabReinforcement
SlabReinforcementGroup = editSlabReinforcement(
    SlabReinforcementGroup,
    parallel_rebar_type="UShapeRebar",
    parallel_front_cover=20,
    parallel_rear_cover=20,
    parallel_left_cover=10,
    parallel_right_cover=10,
    parallel_top_cover=30,
    parallel_bottom_cover=20,
    parallel_rounding=2,
    parallel_diameter=8,
    parallel_amount_spacing_check=True,
    parallel_amount_spacing_value=15,
    cross_rebar_type="UShapeRebar",
    cross_front_cover=20,
    cross_rear_cover=20,
    cross_left_cover=10,
    cross_right_cover=10,
    cross_top_cover=20,
    cross_bottom_cover=20,
    cross_rounding=2,
    cross_diameter=8,
    cross_amount_spacing_check=True,
    cross_amount_spacing_value=15,
    mesh_cover_along = "Bottom",
    structure=App.getDocument("slab").getObject("Beam"),
    facename='Face4',
)
```

-    `slabReinforcementGroup`is a previously created `Slab Reinforcement` group object.

-   The other parameters are the same as required by the `makeSingleTieFourRebars()` function.

you can change any property to edit Slab Reinforcement.


  \[\[Category:Reinforcement\]



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Category_Arch.md) > Example Slab Having UShape Rebars Reinforcement Mesh/pl
