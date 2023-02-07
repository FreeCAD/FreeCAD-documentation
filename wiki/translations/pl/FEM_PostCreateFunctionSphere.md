---
- GuiCommand:
   Name:FEM PostCreateFunctionSphere
   Icon:Fem-post-geo-sphere.svg
   MenuLocation:Results → Filter Functions → Sphere
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM PostCreateFunctionSphere/pl

## Description

The <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:24px;"> **FEM PostCreateFunctionSphere** function defines how a mesh is cut geometrically. It is used by <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Function cut filter](FEM_PostFilterCutFunction.md) and <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Region clip filter](FEM_PostFilterClipRegion.md).

## Usage

### Create a sphere function 

1.  There are several ways to create a function:
    -   Press the **<img src="images/Fem-post-geo-sphere.svg" width=16px> [Sphere](FEM_PostCreateFunctionSphere.md)** button.
    -   Select the **Results → Filter functions → <img src="images/Fem-post-geo-sphere.svg" width=16px> Sphere** option from the menu.
2.  The Implicit function [task panel](Task_panel.md) is opened.
3.  Optionally set the values for the origin and the radius of the section sphere.
4.  Press the **OK** button to finish.

### Edit a sphere function 

If the Sphere object in the [tree view](Tree_view.md) is hidden, select the <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:24px;"> Sphere object in the [3D view](3D_view.md) and press **Space** to make it visible, like in this example:

<img alt="" src=images/FEM_Sphere-Cut-Function-Example.png  style="width:400px;">

#### Move the sphere 

-   Click and drag the spherical grid to move the sphere.

#### Scale the sphere 

-   Click and drag one of the 8 small cubes around the spherical grid to adjust the sphere size.

## Notes

-   Existing functions can be used for different filters and even for different <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [result pipelines](FEM_PostPipelineFromResult.md). It is nevertheless recommended to use a separate set of functions for each pipeline to keep track of the elements in the [tree view](Tree_view.md).





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionSphere/pl
