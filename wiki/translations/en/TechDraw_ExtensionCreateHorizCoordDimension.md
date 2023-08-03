---
 GuiCommand:
   Name: TechDraw ExtensionCreateHorizCoordDimension
   MenuLocation: TechDraw , Extensions: Dimensions , Create Horizontal Coordinate Dimensions
   Workbenches: TechDraw_Workbench
   Shortcut: 
   Version: 0.20
   SeeAlso: TechDraw_ExtensionCreateVertCoordDimension, TechDraw_ExtensionCreateObliqueCoordDimension
---

# TechDraw ExtensionCreateHorizCoordDimension/en

## Description

The **TechDraw ExtensionCreateHorizCoordDimension** tool creates horizontal coordinate dimensions: multiple evenly spaced dimensions starting from the same baseline.

<img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimensionExample.png  style="width:400px;"> 
*On the right the created dimensions*

## Usage

1.  Optionally specify the cascade spacing with the <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:16px;"> [TechDraw ExtensionSelectLineAttributes](TechDraw_ExtensionSelectLineAttributes.md) tool.
2.  Select three or more vertexes.
3.  The selection order of the first two vertexes determines the position of the baseline. If the vertex that is selected first is to the left of the second, the baseline is created at the leftmost vertex, else it is created at the rightmost vertex.
4.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_ExtensionCreateHorizCoordDimension.svg" width=16px> [Create Horizontal Coordinate Dimensions](TechDraw_ExtensionCreateHorizCoordDimension.md)** button.
    -   Select the **TechDraw → Extensions: Dimensions → <img src="images/TechDraw_ExtensionCreateHorizCoordDimension.svg" width=16px> Create Horizontal Coordinate Dimensions** option from the menu.
5.  Coordinate dimensions with centered dimension texts are created.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionCreateHorizCoordDimension/en
