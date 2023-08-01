---
- GuiCommand:
   Name:TechDraw ExtensionCreateObliqueCoordDimension
   MenuLocation:TechDraw - Extensions: Dimensions - Create Oblique Coordinate Dimensions
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Shortcut:
   Version:0.20
   SeeAlso:[TechDraw ExtensionCreateHorizCoordDimension](TechDraw_ExtensionCreateHorizCoordDimension.md), [TechDraw ExtensionCreateVertCoordDimension](TechDraw_ExtensionCreateVertCoordDimension.md)
---

# TechDraw ExtensionCreateObliqueCoordDimension

## Description

The **TechDraw ExtensionCreateObliqueCoordDimension** tool creates oblique coordinate dimensions: multiple evenly spaced dimensions starting from the same baseline.

 <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimensionExample.png  style="width:400px;">  
*On the right the created dimensions*

## Usage

1.  Optionally specify the cascade spacing with the <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:16px;"> [TechDraw ExtensionSelectLineAttributes](TechDraw_ExtensionSelectLineAttributes.md) tool.
2.  Select three or more vertexes.
3.  The selection order of the first two vertexes determines the position of the baseline. If the vertex that is selected first is to the left of the second, the baseline is created at the leftmost vertex, else it is created at the rightmost vertex.
4.  The first two vertexes also define the direction.
5.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_ExtensionCreateObliqueCoordDimension.svg" width=16px> [Create Oblique Coordinate Dimensions](TechDraw_ExtensionCreateObliqueCoordDimension.md)** button.
    -   Select the **TechDraw → Extensions: Dimensions → <img src="images/TechDraw_ExtensionCreateObliqueCoordDimension.svg" width=16px> Create Oblique Coordinate Dimensions** option from the menu.
6.  Coordinate dimensions with centered dimension texts are created.




 {{TechDraw_Tools_navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionCreateObliqueCoordDimension
