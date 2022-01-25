---
- GuiCommand:
   Name:TechDraw  MoveView
   MenuLocation:TechDraw → Move View
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.20
   SeeAlso:[TechDraw CopyView](TechDraw_CopyView.md)
---

# TechDraw MoveView

## Description

The CopyView tool moves a View and all its dependents (Balloons, Dimensions, etc) to a different Page.

## Usage

1.  (Optional) Select a View, a from Page and a to Page.
2.  Press the **<img src="images/TechDraw_MoveView.svg" width=16px> [Move View](TechDraw_MoveView.md)** button
3.  A dialog will open to allow you to select a View, from Page and to Page.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The MoveView tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:

 
```python
import TechDrawTools
TechDrawTools.MoveView(viewName, fromPageName, toPageName)
```




 {{TechDraw Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw MoveView
