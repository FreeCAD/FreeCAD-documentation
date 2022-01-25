---
- GuiCommand:
   Name:Std ViewRotateLeft
   MenuLocation:View → Standard views → Rotate Left
   Workbenches:All
   Shortcut:**Shift**+**Left**
   SeeAlso:[Std ViewRotateRight](Std_ViewRotateRight.md)
---

# Std ViewRotateLeft/pl

## Description

The **Std ViewRotateLeft** command rotates the camera in the active [3D view](3D_view.md) around the view direction in 90-degree increments towards the left (counterclockwise).

## Usage

1.  There are several ways to invoke the command:
    -   Select the **View → Standard views → <img src="images/Std_ViewRotateLeft.svg" width=16px> Rotate Left** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewRotateLeft.svg" width=16px> Rotate Left** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Shift**+**Left**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To rotate the view to the left use the `viewRotateLeft` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateLeft()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewRotateLeft/pl
