---
- GuiCommand:
   Name:Std ViewZoomIn
   MenuLocation:View → Zoom → Zoom In
   Workbenches:All
   Shortcut:**Ctrl**+**+**
   SeeAlso:[Std ViewZoomOut](Std_ViewZoomOut.md), [Std ViewBoxZoom](Std_ViewBoxZoom.md)
---

# Std ViewZoomIn/en

## Description

The **Std ViewZoomIn** command zooms in in the active [3D view](3D_view.md).

## Usage

1.  There are several ways to invoke the command:
    -   Select the **View → Zoom → <img src="images/Std_ViewZoomIn.svg" width=16px> Zoom In** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**+**.

## Notes

-   It is also possible to zoom with the mouse scroll wheel.

## Preferences

-   The zoom factor can be changed in the preferences: **Edit → Preferences... → Display → Navigation → Zoom step**. This setting also affects scroll wheel zoom. See [Preferences Editor](Preferences_Editor#Navigation.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To zoom in use the `zoomIn` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomIn()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewZoomIn/en
