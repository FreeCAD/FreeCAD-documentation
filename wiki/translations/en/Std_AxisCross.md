---
- GuiCommand:
   Name: Std AxisCross
   MenuLocation: View - Toggle axis cross
   Workbenches: All
   Shortcut: **A** **C**
---

# Std AxisCross/en

## Description

The **Std AxisCross** command toggles the axis cross in the active [3D view](3D_view.md).

The axis cross consists of three arrows representing the positive X, Y and Z axis of the global coordinate system. Their common start point is the origin of the global coordinate system.

![](images/Std_AxisCross_example.svg ) 
*The axis cross (the letters are not part of the axis cross)*

## Usage

1.  There are several ways to invoke the command:
    -   Select the **View → <img src="images/Std_AxisCross.svg" width=16px> Toggle axis cross** option from the menu.
    -   Use the keyboard shortcut: **A** then **C**.

## Notes

-   FreeCAD can display a smaller coordinate system indicator in the bottom right corner of 3D views: **Edit → Preferences... → Display → 3D View → Show coordinate system in the corner**. See [Preferences Editor](Preferences_Editor#3D_View.md).
-   The [Navigation Cube](Navigation_Cube.md) also includes a coordinate system indicator.

## Preferences

-   The default for the axis cross can be changed in the preferences: **Edit → Preferences... → Display → 3D view → Show axis cross by default**. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To toggle the axis cross use the `setAxisCross` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setAxisCross(True)
FreeCADGui.ActiveDocument.ActiveView.hasAxisCross()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std AxisCross/en
