---
- GuiCommand:
   Name: FEM PostCreateFunctionBox
   MenuLocation: Results - Filter Functions - Box
   Workbenches: [FEM](FEM_Workbench.md)
   Version: 0.21
   SeeAlso: [FEM tutorial](FEM_tutorial.md)
---

# FEM PostCreateFunctionBox

## Description

The <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> **FEM PostCreateFunctionBox** function defines how a mesh is cut geometrically. It is used by <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Function cut filter](FEM_PostFilterCutFunction.md) and <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Region clip filter](FEM_PostFilterClipRegion.md).

## Usage

### Create a box function 

1.  Either press the **<img src="images/FEM_PostCreateFunctionBox.svg" width=16px> [Box](FEM_PostCreateFunctionBox.md)** button or select the **Results → Filter functions → <img src="images/FEM_PostCreateFunctionBox.svg" width=16px> Box** option from the menu.
2.  The Implicit function [task panel](Task_panel.md) is opened.
3.  Optionally set the values for the center and size of the section box.
4.  Press the **OK** button to finish.

### Edit a box function 

If the Box object in the [tree view](Tree_view.md) is hidden, select the <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> Box object in the [3D view](3D_view.md) and press **Space** to make it visible, like in this example:

 <img alt="" src=images/FEM_Box-Cut-Function-Example.png  style="width:400px;"> 

#### Move the box 

-   Click and drag a face of the box. The box is defined by blue edges.

#### Rotate and tilt the box 

-   Click and drag one of the 3 lines that pass through the box to rotate and tilt the box around its origin.

#### Scale the box 

-   Click and drag one of the 8 small cubes at the box corners to scale the box.

#### Transform the box 

-   Click and drag one of the 6 small cubes around the center of the box to change the shape of the box.

## Notes

-   Existing functions can be used for different filters and even for different <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [result pipelines](FEM_PostPipelineFromResult.md). It is nevertheless recommended to use a separate set of functions for each pipeline to keep track of the elements in the [tree view](Tree_view.md).




 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionBox
