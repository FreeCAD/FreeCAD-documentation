---
- GuiCommand:
   Name: Sketcher CreatePoint
   MenuLocation: Sketch -> Sketcher geometries -> Create point
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **Y**
---

# Sketcher CreatePoint/hr

## Description

The Point tool creates a point in the current sketch, which can be used for constructing geometry elements.

[480px\|Point in the sketcher](IMAGE:Sketcher_Point_fr_01.png.md)

## Usage

-   Click on the **<img src="images/Sketcher_CreatePoint.svg" width=24px> Create point** button to activate the function.
-   Clicking in the sketch creates a point.
-   Pressing **Esc** or clicking the right mouse button cancels the function.

## Options

-   By default points are created as construction geometry and therefore are not visible outside of Sketch editing mode. Use the <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:16px;"> [Toggle Construction](Sketcher_ToggleConstruction.md) tool to change them to normal geometry.
-   A mode to snap to the grid can be set in the [Sketcher Preferences](Sketcher_Preferences.md). The point then snaps to the grid, if it has less than 25% grid distance to a grid line. The snap mode does not fix the point to the grid. It still has two degrees of freedom and can be moved with the mouse or constrained to other locations.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/hr
