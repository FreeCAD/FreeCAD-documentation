---
- GuiCommand:
   Name:FEM PostCreateFunctionCylinder
   MenuLocation:Results - Filter Functions - Cylinder
   Workbenches:[FEM](FEM_Workbench.md)
   Version:0.21
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM PostCreateFunctionCylinder/pl


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Description


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> **FEM PostCreateFunctionCylinder** function defines how a mesh is cut geometrically. It is used by <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Function cut filter](FEM_PostFilterCutFunction.md) and <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Region clip filter](FEM_PostFilterClipRegion.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Usage


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Create a cylinder function 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Either press the **<img src="images/FEM_PostCreateFunctionCylinder.svg" width=16px> [Cylinder](FEM_PostCreateFunctionCylinder.md)** button or select the **Results → Filter functions → <img src="images/FEM_PostCreateFunctionCylinder.svg" width=16px> Cylinder** option from the menu.
2.  The Implicit function [task panel](Task_panel.md) is opened.
3.  Optionally set the values for the center and the radius of the section cylinder.
4.  Press the **OK** button to finish.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Edit a cylinder function 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

If the Cylinder object in the [tree view](Tree_view.md) is hidden, select the <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> Cylinder object in the [3D view](3D_view.md) and press **Space** to make it visible, like in this example:


</div>

<img alt="" src=images/FEM_Cylinder-Cut-Function-Example.png  style="width:400px;">


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Move the cylinder 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Click and drag the big white cuboid to move the cylinder along its normal vector.
-   Click and drag the white grid.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Rotate and tilt the cylinder 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Click and drag a line that connects the small cubes with the big white cuboid to rotate and tilt the cylinder around its origin.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Scale the cylinder 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Click and drag one of the 6 small cubes to scale the cylinder.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Notes


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Existing functions can be used for different filters and even for different <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [result pipelines](FEM_PostPipelineFromResult.md). It is nevertheless recommended to use a separate set of functions for each pipeline to keep track of the elements in the [tree view](Tree_view.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionCylinder/pl
