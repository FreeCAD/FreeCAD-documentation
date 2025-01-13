---
 GuiCommand:
   Name: Constraint Perpendicular
   Name/cs: Constraint Perpendicular
   Workbenches: Sketcher Workbench/cs, PartDesign Workbench/cs
   MenuLocation: Sketch , Sketcher constraints , Constrain perpendicular
   Shortcut: N
   SeeAlso: Sketcher_ConstrainAngle/cs
---

# Sketcher ConstrainPerpendicular/cs


</div>

## Description

The <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:24px;"> [Sketcher ConstrainPerpendicular](Sketcher_ConstrainPerpendicular.md) tool constrains two lines to be perpendicular, or two edges, or an edge and an axis, to be perpendicular at their intersection. Lines are treated as infinite, and open curves are virtually extended as well. The constraint can also connect two edges, forcing them to be perpendicular at the joint.

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> [Constrain perpendicular](Sketcher_ConstrainPerpendicular.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> Constrain perpendicular** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Constrain → <img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> Constrain perpendicular** option from the context menu.

    -   Use the keyboard shortcut: **N**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two edges. One of the edges must be a straight line or an axis. The other can be any edge except a B-spline.
    -   Select a point and two edges (in that order).
    -   Select an edge, a point and another edge (idem).
5.  A Perpendicular constraint is added. If a point and two edges have been selected, up to two [Point on object constraints](Sketcher_ConstrainPointOnObject.md) can also be added. See [Examples](#Between_two_edges_at_point.md).
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Do one of the following:
    -   Select two edges (see above).
    -   Select two endpoints belonging to different edges.
    -   Select an edge and the endpoint of another edge (in any order).
    -   Select a point and two edges (idem).
2.  Invoke the tool as explained above, or with the following additional option:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> Constrain perpendicular** option from the context menu.
3.  A Perpendicular constraint is added. If a point and two edges have been selected, up to two [Point on object constraints](Sketcher_ConstrainPointOnObject.md) can also be added. See [Examples](#Between_two_edges_at_point.md).

## Examples

### Between two edges 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode1.png  style="width:400px;">

The two edges are made perpendicular at their (virtual) intersection. If one of the edges is a [conic](Sketcher_Workbench#Sketcher_CompCreateConic.md), a [Point object](Sketcher_CreatePoint.md) that has a [Point on object constraint](Sketcher_ConstrainPointOnObject.md) with both (extended) edges is added.

### Between two endpoints 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode2.png  style="width:400px;">

The endpoints are made coincident, and the edges are made perpendicular at that point.

### Between edge and endpoint 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode3.png  style="width:400px;">

The endpoint of one edge is constrained to lie on the other edge, and the edges are made perpendicular at that point.

### Between two edges at point 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode4.png  style="width:400px;">

The two edges are made perpendicular at a given point. The point can be any point, e.g. the center of a circle, the endpoint of an edge, or the origin, it can belong to one of the edges, and it can also be a [Point object](Sketcher_CreatePoint.md). If required [Point on object constraint(s)](Sketcher_ConstrainPointOnObject.md) are added to ensure the point lies on both (extended) edges. These additional constraints are called [helper constraints](Sketcher_helper_constraint.md).

## Scripting

Perpendicular Constraint can be created from [macros](Macros.md) and from the python console by using the following: 
```python
# direct perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,icurve2))

# point-to-point perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2))

# perpendicular-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('PerpendicularViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` where:

  - `Sketch` is a sketch object

  - `icurve1`, `icurve2` are two integers identifying the curves to be made perpendicular. The integers are indexes in the sketch (the value, returned by `Sketch.addGeometry`).

  - `pointpos1`, `pointpos2` should be `1` for start point and `2` for end point.

  - `geoidpoint` and `pointpos` in PerpendicularViaPoint are the indexes specifying the point of perpendicularity.

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `icurve1`, `icurve2`, `pointpos1`, `pointpos2` and `geoidpoint`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPerpendicular/cs
