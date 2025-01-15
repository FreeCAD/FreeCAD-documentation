---
 GuiCommand:
   Name: Sketcher CreatePoint
   MenuLocation: Sketch , Sketcher geometries , Create point
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **Y**
---

# Sketcher CreatePoint

## Description

The <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:24px;"> [Sketcher CreatePoint](Sketcher_CreatePoint.md) tool creates a point.

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md). <small>(v1.0)</small> 

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreatePoint.svg" width=16px> [Create point](Sketcher_CreatePoint.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreatePoint.svg" width=16px> Create point** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_CreatePoint.svg" width=16px> Create point** option from the context menu.
    -   Use the keyboard shortcut: **G** then **Y**.
2.  The cursor changes to a cross with the tool icon.
3.  Pick a point. Or with Pos-OVP: enter its X and/or Y coordinate.
4.  The point is created and applicable Pos-OVP based constraints are added.
5.  If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep creating points.
    2.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-    {{VersionMinus|0.21}}: Points are always created as construction geometry. Optionally change them to normal geometry with [Sketcher ToggleConstruction](Sketcher_ToggleConstruction.md) to make them visible outside of Sketch editing mode.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint
