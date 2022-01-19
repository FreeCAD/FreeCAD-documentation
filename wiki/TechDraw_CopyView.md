---
- GuiCommand:
   Name:TechDraw  CopyView
   MenuLocation:TechDraw → Copy View
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.20
   SeeAlso:[TechDraw MoveView](TechDraw_MoveView.md)
---

# TechDraw CopyView

## Description

The CopyView tool copies a View and all its dependents (Balloons, Dimensions, etc) to a second Page.

## Usage

1.  (Optional) Select a View, a from Page and a to Page.
2.  Press the **<img src="images/TechDraw_CopyView.svg" width=16px> [Copy View](TechDraw_CopyView.md)** button
3.  A dialog will open to allow you to select a View, from Page and to Page.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The CopyView tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:

 
```python
import TechDrawTools
#MoveView with a True parameter in the last position performs a copy
TechDrawTools.MoveView(viewName, fromPageName, toPageName, True)
```

## Notes

There is only one View object after the copy operation. Any changes made to the View will be reflected in both Pages. If the View is deleted from one Page it will also be deleted from the other.




 {{TechDraw Tools navi}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw CopyView
