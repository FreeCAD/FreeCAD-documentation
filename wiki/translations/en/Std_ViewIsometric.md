---
 GuiCommand:
   Name: Std ViewIsometric
   MenuLocation: View , Standard views , Axonometric , Isometric
   Workbenches: All
   Shortcut: **0**
   SeeAlso: Std_ViewDimetric, Std_ViewTrimetric
---

# Std ViewIsometric/en

## Description

The **Std ViewIsometric** command realigns the camera in the active [3D view](3D_view.md) to obtain an [isometric](https://en.wikipedia.org/wiki/Isometric_projection) view. For a truly isometric view the 3D view must be in [orthographic mode](Std_OrthographicCamera.md), but the command also works if the view is in [perspective mode](Std_PerspectiveCamera.md).

![](images/Std_ViewIsometric_example.svg ) 
*The [axis cross](Std_AxisCross.md) and a cube in isometric view*

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewIsometric.svg" width=16px> [Std ViewIsometric](Std_ViewIsometric.md)** button.
    -   Select the **View → Standard views → Axonometric → <img src="images/Std_ViewIsometric.svg" width=16px> Isometric** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewIsometric.svg" width=16px> Isometric** option from the [3D view](3D_view.md) context menu.
    -   Select the **<img src="images/Std_ViewIsometric.svg" width=16px> Isometric** option from the Mini-cube menu of the [Navigation Cube](Navigation_Cube.md).
    -   Use the keyboard shortcut: **0**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change to isometric view use the `viewIsometric` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewIsometric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIsometric/en
