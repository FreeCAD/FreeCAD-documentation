---
- GuiCommand:
   Name: Std ViewZoomOut
   MenuLocation: View - Zoom - Zoom Out
   Workbenches: All
   Shortcut: **Ctrl**+**-**
   SeeAlso: [Std ViewZoomIn](Std_ViewZoomIn.md), [Std ViewBoxZoom](Std_ViewBoxZoom.md)
---

# Std ViewZoomOut/en

## Description

The **Std ViewZoomOut** command zooms out in the active [3D view](3D_view.md).

## Usage

1.  There are several ways to invoke the command:
    -   Select the **View → Zoom → <img src="images/Std_ViewZoomOut.svg" width=16px> Zoom Out** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**-**.

## Notes

-   It is also possible to zoom with the mouse scroll wheel.

## Preferences

-   The zoom factor can be changed in the preferences: **Edit → Preferences... → Display → Navigation → Zoom step**. This setting also affects scroll wheel zoom. See [Preferences Editor](Preferences_Editor#Navigation.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To zoom out use the `zoomOut` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomOut()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewZoomOut/en
