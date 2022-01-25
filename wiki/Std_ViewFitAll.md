---
- GuiCommand:
   Name:Std ViewFitAll
   MenuLocation:View → Standard views → Fit all
   Workbenches:All
   Shortcut:**V** **F**
   SeeAlso:[Std ViewFitSelection](Std_ViewFitSelection.md)
---

# Std ViewFitAll

## Description

The **Std ViewFitAll** command zooms and pans the camera so that all visible objects fit inside the active [3D view](3D_view.md).

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewFitAll.svg" width=16px> [Std ViewFitAll](Std_ViewFitAll.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewFitAll.svg" width=16px> Fit all** option from the menu.
    -   Select the **<img src="images/Std_ViewFitAll.svg" width=16px> Fit all** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **V** then **F**.

## Notes

-   It is also possible to zoom to \'fit all\' via the Mini-cube menu of the [Navigation Cube](Navigation_Cube.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change the view to \'fit all\' use the `fitAll` method of the ActiveView object. This method is not available if FreeCAD is in console mode.

 
```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.fitAll()
```

Alternatively the `SendMsgToActiveView` method of the FreeCADGui object can be used. This method is not available if FreeCAD is in console mode.

 
```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewFit')
```




 {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewFitAll
