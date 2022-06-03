---
- GuiCommand   *
   Icon   *Zoom-out.svg
   Name   *Std ViewZoomOut
   MenuLocation   *[View](Std_View_Menu.md) → Zoom‏‎ → Zoom Out
   Workbenches   *All
   Shortcut   *Ctrl + -
   SeeAlso   *[Zoom In](Std_ViewZoomIn.md), [Zoom box](Std_ViewBoxZoom.md)
---

# Std ViewZoomOut/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Face să apară conținutul mai mic în vizualizarea 3D .


</div>

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

-   Go to **View → Zoom‏‎ → <img alt="" src=images/Zoom-out.svg  style="width   *24px;"> Zoom Out** or press **Ctrl** + **-**.
-   The view can also be zoomed out with the mouse scroll wheel.


</div>

## Notes

-   It is also possible to zoom with the mouse scroll wheel.

## Preferences

-   The zoom factor can be changed in the preferences   * **Edit → Preferences... → Display → Navigation → Zoom step**. This setting also affects scroll wheel zoom. See [Preferences Editor](Preferences_Editor#Navigation.md).

## Scripting


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To zoom out use the `zoomOut` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomOut()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewZoomOut/ro
