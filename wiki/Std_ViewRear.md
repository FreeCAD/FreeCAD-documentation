---
- GuiCommand:
   Name:Std ViewRear
   MenuLocation:View - Standard views - Rear
   Workbenches:All
   Shortcut:**4**
   SeeAlso:[Std ViewBottom](Std_ViewBottom.md), [Std ViewLeft](Std_ViewLeft.md)
---

# Std ViewRear

## Description

The **Std ViewRear** command points the camera in the active [3D view](3D_view.md) in the direction of the negative Y axis.

 ![](images/FreeCAD_views_rear.svg )  
*Arrow 4 points in the direction of the rear view*

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewRear.svg" width=16px> [Std ViewRear](Std_ViewRear.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewRear.svg" width=16px> Rear** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewRear.svg" width=16px> Rear** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **4**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change to rear view use the `viewRear` method of the ActiveView object. This method is not available if FreeCAD is in console mode.

 
```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRear()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```




 {{Std Base navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewRear
