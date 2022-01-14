---
- GuiCommand:
   Name:Std ViewTrimetric
   MenuLocation:View → Standard views → Axonometric → Trimetric
   Workbenches:All
   SeeAlso:[Std ViewIsometric](Std_ViewIsometric.md), [Std ViewDimetric](Std_ViewDimetric.md)
---

# Std ViewTrimetric/pl

## Description

The **Std ViewTrimetric** command realigns the camera in the active [3D view](3D_view.md) to obtain a [trimetric](https://en.wikipedia.org/wiki/Axonometric_projection#Three_types) view. For a truly trimetric view the 3D view must be in [orthographic mode](Std_OrthographicCamera.md), but the command also works if the view is in [perspective mode](Std_PerspectiveCamera.md).

![](images/Std_ViewTrimetric_example.svg ) 
*The [axis cross](Std_AxisCross.md) and a cube in trimetric view*

## Usage

1.  Select the **View → Standard views → Axonometric → <img src="images/Std_ViewTrimetric.svg" width=16px> Trimetric** option from the menu.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change to trimetric view use the `viewTrimetric` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewTrimetric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewTrimetric/pl
