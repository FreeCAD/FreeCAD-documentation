---
- GuiCommand:
   Name:Std ViewRotateRight
   MenuLocation:View → Standard views → Rotate Right
   Workbenches:All
   Shortcut:**Shift**+**Right**
   SeeAlso:[Std ViewRotateLeft](Std_ViewRotateLeft.md)
---

# Std ViewRotateRight/en

## Description

The **Std ViewRotateRight** command rotates the camera in the active [3D view](3D_view.md) around the view direction in 90-degree increments towards the right (clockwise).

## Usage

1.  There are several ways to invoke the command:
    -   Select the **View → Standard views → <img src="images/Std_ViewRotateRight.svg" width=16px> Rotate Right** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewRotateRight.svg" width=16px> Rotate Right** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Shift**+**Right**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To rotate the view to the right use the `viewRotateRight` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateRight()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewRotateRight/en
