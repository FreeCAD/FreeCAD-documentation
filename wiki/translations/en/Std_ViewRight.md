---
- GuiCommand:
   Name:Std ViewRight
   MenuLocation:View → Standard views → Right
   Workbenches:All
   Shortcut:**3**
   SeeAlso:[Std ViewFront](Std_ViewFront.md), [Std ViewTop](Std_ViewTop.md)
---

# Std ViewRight/en

## Description

The **Std ViewRight** command points the camera in the active [3D view](3D_view.md) in the direction of the negative X axis.

![](images/FreeCAD_views_front.svg ) *Arrow 3 points in the direction of the right view*

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewRight.svg" width=16px> [Std ViewRight](Std_ViewRight.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewRight.svg" width=16px> Right** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewRight.svg" width=16px> Right** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **3**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change to right view use the `viewRight` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRight()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewRight/en
