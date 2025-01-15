---
 GuiCommand:
   Name: Sketcher Extend
   MenuLocation: Sketch , Sketcher tools , Extend edge
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **Q**
   Version: 0.17
   SeeAlso: Sketcher_Trimming
---

# Sketcher Extend/en

## Description

The <img alt="" src=images/Sketcher_Extend.svg  style="width:24px;"> [Sketcher Extend](Sketcher_Extend.md) tool extends or shortens a line or an arc to an arbitrary location, or to a target edge or point.

<img alt="" src=images/Sketcher_Extend_example_01.png  style="width:600px;"> 
*Shown on the left (1), the two sketch elements before the operation; in the middle (2), the line is being extended to the arc; on the right (3), the final result.*

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_Extend.svg" width=16px> [Sketcher Extend edge](Sketcher_Extend.md)** button.
    -   Select the **Sketcher → Sketcher tools → <img src="images/Sketcher_Extend.svg" width=16px> Extend edge** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_Extend.svg" width=16px> Extend edge** option from the context menu.
    -   Use the keyboard shortcut: **G** then **Q**.
2.  If there is a previous selection it is cleared. The tool does not accept a pre-selection.
3.  The cursor changes to a cross with the tool icon.
4.  Select a line or an arc.
5.  Move the cursor in the direction to extend or shorten.
6.  Do one of the following:
    -   Click an arbitrary point.
    -   To extend/shorten to another edge ([Auto constraints](Sketcher_Workbench#Auto_constraints.md) must be enabled): Place the cursor over the target edge. When it is highlighted and the <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Point on object constraint](Sketcher_ConstrainPointOnObject.md) icon appears besides the cursor, click to confirm. The constraint is added.
    -   To extend/shorten to a point (Auto constraints must be enabled): Place the cursor over the target point. when it is highlighted and the <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Coincident constraint](Sketcher_ConstrainCoincident.md) icon appears besides the cursor, click to confirm. The constraint is added.
7.  If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep extending/shortening edges.
    2.  To finish, click in an empty area in the [3D view](3D_view.md), right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   If not fully constrained, the target edge or point may be modified as well.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Extend/en
