---
- GuiCommand:
   Icon: Zoom-in.svg
   Name: Std ViewZoomIn
   MenuLocation: Std View Menu -> Zoom‏‎ -> Zoom In
   Workbenches: All
   Shortcut: Ctrl + +
   SeeAlso: Std ViewZoomOut, Std ViewBoxZoom
---

# Std ViewZoomIn/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Face conținutul să apară mai mare în vizualizarea 3D.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

-   Go to **View → Zoom‏‎ → <img alt="" src=images/Zoom-in.svg  style="width:24px;"> Zoom In** or press **Ctrl** + **+**.
-   The view can also be zoomed in with the mouse scroll wheel.


</div>

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
⏵ [documentation index](../README.md) > Std ViewZoomIn/ro
