---
- GuiCommand:
   Name:Sketcher CreatePoint
   MenuLocation:Sketch → Sketcher geometries → Create point
   Workbenches:[Sketcher](Sketcher_Workbench.md)
---

# Sketcher CreatePoint/en

## Description

The Point tool creates a point in the current sketch, which can be used for constructing geometry elements. The point is always an construction element and does not show up in the 3D-view.

_ 

## Usage

-   Click on the button **<img src="images/Sketcher_CreatePoint.svg" width=24px> Create point**, to activate the function.
-   Clicking in the sketch creates a point.
-   Pressing **Esc** or clicking the right mouse button cancels the function.

## Options

A mode to snap to the grid can be set in the [Sketcher Preferences](Sketcher_Preferences.md). The point snaps then to the grid, if it has less than 25% grid distance to a grid line. The snap mode does not fix them to the grid. The points can be moved with the mouse or constraints to other locations.

## Limitations

The created point is not available outside of the sketch. In case a point is needed in the 3D-view, use the [PartDesign Point](PartDesign_Point.md) for a datum point or the [Part Point](Part_Point.md) instead.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/en
