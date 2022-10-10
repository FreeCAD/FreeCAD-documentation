---
- GuiCommand   *
   Name   *TechDraw ShareView
   MenuLocation   *TechDraw → Share View
   Workbenches   *[TechDraw](TechDraw_Workbench.md)
   Version   *0.20
   SeeAlso   *[TechDraw MoveView](TechDraw_MoveView.md)
---

# TechDraw ShareView/en

## Description

The <img alt="" src=images/TechDraw_ShareView.svg  style="width   *24px;"> **TechDraw ShareView** tool makes a View and all its dependents (Balloons, Dimensions, etc) visible on a second Page.

## Usage

1.  Optionally select a View, a from Page and a to Page. The pages must be selected in that order.
2.  There are several ways to invoke the tool   *
    -   Press the **<img src="images/TechDraw_ShareView.svg" width=16px> [Share View](TechDraw_ShareView.md)** button.
    -   Select the **TechDraw → <img src="images/TechDraw_ShareView.svg" width=16px> Share View** option from the menu.
3.  A dialog will open to allow you to select a View, from Page and to Page.
4.  Press the **OK** button.

## Notes

There is only one View object after the share operation. Any changes made to the View will be reflected in both Pages. If the View is deleted from one Page it will also be deleted from the other.

## Scripting


**See also   ***

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The ShareView tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions   *


```python
import TechDrawTools
#MoveView with a True parameter in the last position performs a copy
TechDrawTools.MoveView(viewName, fromPageName, toPageName, True)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShareView/en
