---
 GuiCommand:
   Name: Sketcher CreateEllipseByCenter
   MenuLocation: Sketch , Sketcher geometries , Create ellipse by center
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **E** **E**
   Version: 0.15
   SeeAlso: Sketcher_CreateArcOfEllipse
---

# Sketcher CreateEllipseByCenter/en

## Description

The <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:24px;"> [Sketcher CreateEllipseByCenter](Sketcher_CreateEllipseByCenter.md) tool creates an ellipse by its center, an endpoint of one of its axes, and a point along the ellipse. <small>(v1.0)</small> : Or optionally by both endpoints of one of its axes and a point along the ellipse.

![](images/Sketcher_CreateEllipseByCenter_Example.png ) 
*Ellipse (white) with internal geometry (dark yellow)*

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md). <small>(v1.0)</small> 
Dim-OVP = Dimensional On-View-Parameters. <small>(v1.0)</small> 

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreateEllipseByCenter.svg" width=16px> [Ellipse by center, radius, rim point](Sketcher_CreateEllipseByCenter.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateEllipseByCenter.svg" width=16px> Create ellipse by center** option from the menu.
    -   Use the keyboard shortcut: **G** then **E**, then **E**.
2.  The cursor changes to a cross with the current tool mode icon.
3.  The **Ellipse parameters** section (<small>(v1.0)</small> ) is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
4.  Optionally press the **M** key or select from the dropdown list in the parameters section to change the tool mode:
    -   <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:16px;"> **Center**:
        1.  Pick the center of the ellipse. Or with Pos-OVP: enter its X and/or Y coordinate.
        2.  Pick an endpoint of one of the axes of the ellipse, this also defines one of its radii. Or with Dim-OVP: enter this radius and/or the angle of this axis.
        3.  Pick a point to define the other radius of the ellipse. Or with Dim-OVP: enter this radius.
    -   <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:16px;"> **Axis endpoints**: <small>(v1.0)</small> 
        1.  Pick the endpoints of one of the axes of the ellipse, this also defines one of its radii. Or with Pos-OVP: enter their X and/or Y coordinates. No constraints are created for these points.
        2.  Pick a point to define the other radius of the ellipse. Or with Pos-OVP: enter its X and/or Y coordinate. No constraint is created for this point.
5.  The ellipse is created, including a set of internal geometry (major axis, minor axis and two foci), and applicable Pos-OVP and Dim-OVP based constraints are added.
6.  If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep creating ellipses.
    2.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   Elements of the internal geometry can be deleted. They can be recreated at any time with [Sketcher RestoreInternalAlignmentGeometry](Sketcher_RestoreInternalAlignmentGeometry.md).
-   Once created, the major and minor axes of an ellipse are strict and cannot be swapped by resizing. This is a consequence of the solver parametrization and the same strict behavior of [OpenCASCADE](OpenCASCADE.md). An ellipse must be rotated to swap its axes.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/en
