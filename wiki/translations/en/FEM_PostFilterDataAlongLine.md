---
- GuiCommand:
   Name:FEM PostFilterDataAlongLine
   MenuLocation: Results → Line clip filter
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM PostFilterDataAlongLine/en

## Description

Plots the values of a field along a specified line.

## Usage

1.  Select a previously created [result pipeline](FEM_PostPipelineFromResult.md).
2.  Invoke the command in one of the several ways:
    -   Press the **<img src="images/FEM_PostFilterDataAlongLine.svg" width=16px> [Line clip filter](FEM_PostFilterDataAlongLine.md)** button.
    -   Select the **Results → <img src="images/FEM_PostFilterDataAlongLine.svg" width=16px> Line clip filter** option from the menu.
3.  Specify the coordinates of two points defining the line along which the results are to be evaluated. Optionally, press the **Select Points** button and pick the points manually on the surface of the mesh.
4.  Optionally, specify the **Resolution**.
5.  Select a **Field** from the expandable list.
6.  Press the **Create Plot** button. An XY plot of the field value vs the line length will be created in a separate window.
7.  Click the **OK** button to finish the command.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterDataAlongLine/en
