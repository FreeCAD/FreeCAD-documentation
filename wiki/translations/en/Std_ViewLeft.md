---
- GuiCommand:
   Name:Std ViewLeft
   MenuLocation:View → Standard views → Left
   Workbenches:All
   Shortcut:**6**
   SeeAlso:[Std ViewRear](Std_ViewRear.md), [Std ViewBottom](Std_ViewBottom.md)
---

## Description

The **Std ViewLeft** command points the camera in the active [3D view](3D_view.md) in the direction of the positive X axis.

![](images/FreeCAD_views_rear.svg ) *Arrow 6 points in the direction of the left view*

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewLeft.svg" width=16px> [Std ViewLeft](Std_ViewLeft.md)** button.
    -   Select the {{MenuCommand|View → Standard views → <img src="images/Std_ViewLeft.svg" width=16px> Left}} option from the menu.
    -   Select the {{MenuCommand|Standard views → <img src="images/Std_ViewLeft.svg" width=16px> Left}} option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **6**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change to left view use the `viewLeft` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewLeft()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}  
