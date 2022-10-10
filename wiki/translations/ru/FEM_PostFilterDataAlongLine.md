---
- GuiCommand   */ru
   Name   *FEM PostCreateDataAlongLineFilter
   Name/ru   *FEM PostCreateDataAlongLineFilter
   Icon   *Fem-DataAlongLine.svg
   MenuLocation   * Results → Data along line filter
   |Workbenches   *[FEM](FEM_Workbench/ru.md)
   Shortcut   *
   SeeAlso   *[FEM tutorial](FEM_tutorial/ru.md)
---

# FEM PostFilterDataAlongLine/ru


</div>

## Описание

Plots the values of a field along a specified line.

![](images/FEM_Line-Clip-Filter-Example.png )

*A line clip filter inside a [Region clip filter](FEM_PostFilterClipRegion.md).The Region clip filter is the semi-transparent object.The part of the line outside the Region clip filter is set to a value of zero and therefore appears blue.*

## Применение

1.  Select a previously created [result pipeline](FEM_PostPipelineFromResult.md) or another filter.
2.  Invoke the command either by   *
    -   Pressing the button **<img src="images/FEM_PostFilterDataAlongLine.svg" width=16px> '''Line clip filter'''**.
    -   Using the menu **Results → <img src="images/FEM_PostFilterDataAlongLine.svg" width=16px> Line clip filter**.
3.  Specify the coordinates of two points defining the line along which the results are to be evaluated. Optionally, press the **Select Points** button and pick the points manually on the surface of the mesh.
4.  Optionally, specify the **Resolution**.
5.  Select a **Field** from the expandable list.
6.  Press the **Create Plot** button. An XY plot of the field value vs. the line length will be created in a separate window.
7.  Click the **OK** button to finish the command.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterDataAlongLine/ru
