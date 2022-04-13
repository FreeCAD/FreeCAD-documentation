---
- GuiCommand:
   Name:FEM PostFilterClipScalar
   MenuLocation:Results → Scalar clip filter
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM PostFilterClipScalar

## Description

Clips a field using a specified scalar value.

## Usage

1.  Select a previously created [result pipeline](FEM_PostPipelineFromResult.md).
2.  Invoke the command in one of the several ways:
    -   Press the **<img src="images/FEM_PostFilterClipScalar.svg" width=16px> [Scalar clip filter](FEM_PostFilterClipScalar.md)** button.
    -   Select the **Results → <img src="images/FEM_PostFilterClipScalar.svg" width=16px> Scalar clip filter** option from the menu.
3.  Adjust the **Result display options** like for the [result pipeline](FEM_PostPipelineFromResult.md). Hide that pipeline to see the effect of a Scalar Clip Filter.
4.  Select the scalar type from the expandable list.
5.  Specify the value of the scalar for clipping directly or use the slider.
6.  By default, all the regions with field values below the specified one will be hidden. Press the **Clip inside out** button to invert the display and hide the regions with values above the specified one.
7.  Click **OK** button to close the tool\'s menu.




 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterClipScalar
