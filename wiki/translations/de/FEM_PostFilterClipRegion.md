---
 GuiCommand:
   Name: FEM PostFilterClipRegion
   MenuLocation: Results , Region clip filter
   Workbenches: FEM_Workbench
   SeeAlso: FEM_PostPipelineFromResult, FEM_PostCreateFunctions, FEM_tutorial
---

# FEM PostFilterClipRegion/de

## Description

Clips a field using a sphere or a plane cutting through the model.

<img alt="" src=images/FEM_Region-Cut-Filter-Example.png  style="width:400px;">

*A region cut filter with a sphere as cut function.The original pipeline is the semi-transparent object.*

## Usage

1.  Select a previously created [result pipeline](FEM_PostPipelineFromResult.md).
2.  Invoke the command either by:
    -   Pressing the button **<img src="images/FEM_PostFilterClipRegion.svg" width=16px> '''Region clip filter'''** button.
    -   Using the menu **Results → <img src="images/FEM_PostFilterClipRegion.svg" width=16px> Region clip filter** option from the menu.
3.  Adjust the **Result display options** like for the [result pipeline](FEM_PostPipelineFromResult.md). You might need to hide the pipeline to see the effect of the filter in the preview.
4.  Either
    -   If there is no [filter function](FEM_PostCreateFunctions.md) defined yet, press the **<img src="images/List-add.svg" width=16px> Create
** button and select **<img src="images/FEM_PostCreateFunctionPlane.svg" width=16px> Plane** or **<img src="images/FEM_PostCreateFunctionSphere.svg" width=16px> Sphere**
    -   Choose an existing filter function from the list. If needed, adjust the cut parameters to make sure that it intersects the model. Note that changed cut parameters will also change the parameters of the used filter function.
5.  The model will be clipped using the filter function. Select the **Inside Out** option to invert the cut. Select the **Cut Cells** option to smooth the clipped region by eliminating parts of finite elements that are sticking out.
6.  Click the **OK** button to finish the command.

**Note**: A **Field** can only be set if a filter function exists and has been applied with <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:16px;"> [Apply Changes](FEM_PostApplyChanges.md). Alternatively you can reopen the filter dialog.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterClipRegion/de
