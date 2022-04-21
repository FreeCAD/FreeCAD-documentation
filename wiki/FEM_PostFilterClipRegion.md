---
- GuiCommand:
   Name:FEM PostFilterClipRegion
   MenuLocation:Results → Region clip filter
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM PostFilterClipRegion

## Description

Clips a field using a sphere or a plane cutting through the model.

## Usage

1.  Select a previously created [result pipeline](FEM_PostPipelineFromResult.md).
2.  Invoke the command in one of the several ways:
    -   Press the **<img src="images/FEM_PostFilterClipRegion.svg" width=16px> [Region clip filter](FEM_PostFilterClipRegion.md)** button.
    -   Select the **Results → <img src="images/FEM_PostFilterClipRegion.svg" width=16px> Region clip filter** option from the menu.
3.  Adjust the **Result display options** like for the [result pipeline](FEM_PostPipelineFromResult.md). Hide that pipeline to see the effect of a Region Clip Filter.
4.  Press the **<img src="images/List-add.svg" width=16px> Create** button and select **<img src="images/Fem-post-geo-plane.svg" width=16px> Plane** or **<img src="images/Fem-post-geo-sphere.svg" width=16px> Sphere**, or choose the existing plane/sphere from the expandable list. If needed, adjust the parameters of the plane/sphere to make sure that it intersects the model.
5.  The model will be clipped using the plane/sphere. Select the **Inside Out** option to invert the cut. Select the **Cut Cells** option to smooth the clipped region by eliminating parts of finite elements that are sticking out.
6.  Click the **OK** button to finish the command.




 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterClipRegion
