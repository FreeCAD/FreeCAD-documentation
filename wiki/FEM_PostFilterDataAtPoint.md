---
- GuiCommand   *
   Name   *FEM PostFilterDataAtPoint
   MenuLocation   *Results → Data at point clip filter
   Workbenches   *[FEM](FEM_Workbench.md)
   SeeAlso   *[FEM Result pipeline](FEM_PostPipelineFromResult.md), [FEM tutorial](FEM_tutorial.md)
---

# FEM PostFilterDataAtPoint

## Description

Displays the value of a selected field at a picked point.

## Usage

1.  Select a previously created [result pipeline](FEM_PostPipelineFromResult.md) or another filter (except of a line filter).
2.  Invoke the command either by   *
    -   Pressing the button **<img src="images/FEM_PostFilterDataAtPoint.svg" width=16px> '''Data at point clip filter'''**.
    -   Using the menu **Results → <img src="images/FEM_PostFilterDataAtPoint.svg" width=16px> Data at point clip filter**.
3.  Select a result **Field**.
4.  Now
    -   either click the **Select Point** button and subsequently pick the desired point in the mesh.
    -   change the point coordinate.

The value at this point for the given **Field** is output to the dialog. The value of the data point is also anytime accessible via the [property](Property_editor.md) **Point Data**.




 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterDataAtPoint
