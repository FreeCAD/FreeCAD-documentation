---
- GuiCommand:
   Name:FEM PostFilterClipScalar
   MenuLocation:Results → Scalar clip filter
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM Result pipeline](FEM_PostPipelineFromResult.md), [FEM tutorial](FEM_tutorial.md)
---

# FEM PostFilterClipScalar/en

## Description

Clips a field using a specified scalar value.

<img alt="" src=images/FEM_Scalar-Clip-Filter-Example.png  style="width:400px;">

*A scalar clip filter result.The original pipeline is the semi-transparent object.*

A scalar filter can be combined with other filters. Here is for example a scalar filter on a [warp filter](FEM_PostFilterWarp.md) (semi-transparent):

<img alt="" src=images/FEM_Scalar-Clip-Filter-On-Warp-Example.png  style="width:600px;">

## Usage

1.  Select a previously created [result pipeline](FEM_PostPipelineFromResult.md) or another existing filter.
2.  Invoke the command either by:
    -   Pressing the button **<img src="images/FEM_PostFilterClipScalar.svg" width=16px> '''Scalar clip filter'''**.
    -   Using the menu **Results → <img src="images/FEM_PostFilterClipScalar.svg" width=16px> Scalar clip filter**.
3.  Adjust the **Result display options** like for the [result pipeline](FEM_PostPipelineFromResult.md). Hide that pipeline to see the effect of a Scalar Clip Filter.
4.  Select the **Scalar** type from the expandable list.
5.  Specify the **Clip scalar** value directly or use the slider.
6.  By default, all the regions with field values below the specified one will be hidden. Select the **Clip inside out** option to invert the display and hide the regions with values above the specified one.
7.  Click **OK** button to finish the command.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterClipScalar/en
