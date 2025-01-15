---
 GuiCommand:
   Name: Sketcher ConstrainTangent
   Name/es: Croquizador RestringirTangent
   Workbenches: Sketcher Workbench/es
   MenuLocation: Croquis , Restricciones Croquizador ,  Restringir Tangent
   Shortcut: T
   SeeAlso: Sketcher ConstrainPointOnObject/es
---

# Sketcher ConstrainTangent/es


</div>



## Descripción

The <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Sketcher ConstrainTangent](Sketcher_ConstrainTangent.md) tool constrains two edges, or an edge and an axis, to be tangent. Lines are treated as infinite, and open curves are virtually extended as well. The constraint can also connect two edges, forcing them to be tangent at the joint. If two lines are selected, or a line and the endpoint of another line, the lines are made collinear.



## Utilización

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainTangent.svg" width=16px> [Constrain tangent or collinear](Sketcher_ConstrainTangent.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainTangent.svg" width=16px> Constrain tangent or collinear** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Constrain → <img src="images/Sketcher_ConstrainTangent.svg" width=16px> Constrain tangent or collinear** option from the context menu.

    -   Use the keyboard shortcut: **T**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two edges. The edges can be any edge except a B-spline.
    -   Select a point and two edges (in that order).
    -   Select an edge, a point and another edge (idem).
5.  A Tangent constraint is added. If a point and two edges have been selected, up to two [Point on object constraints](Sketcher_ConstrainPointOnObject.md) can also be added. See [Examples](#Between_two_edges_at_point.md).
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
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainTangent.svg" width=16px> Constrain tangent or collinear** option from the context menu.
3.  A Tangent constraint is added. If a point and two edges have been selected, up to two [Point on object constraints](Sketcher_ConstrainPointOnObject.md) can also be added. See [Examples](#Between_two_edges_at_point.md).

## Examples

### Between two edges 

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width:400px;">

The two edges are made tangent. If one of the edges is a [conic](Sketcher_Workbench#Sketcher_CompCreateConic.md), a [Point object](Sketcher_CreatePoint.md) that has a [Point on object constraint](Sketcher_ConstrainPointOnObject.md) with both (extended) edges is added.

It is not recommended to reconstruct the point of tangency by manually creating a point and constraining it to lie on both curves. It will work, but the convergence will be seriously slower, jumpier, and will require about twice as many iterations to converge than normal. If the point of tangency is needed, select two edges and an existing point instead.

### Between two endpoints 

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width:400px;">

The endpoints are made coincident, and the angle between the edges at that point is set to 180° (smooth joint) or 0° (sharp joint), depending on the placement of the edges before the constraint is applied.

### Between edge and endpoint 

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width:400px;">

The endpoint of one edge is constrained to lie on the other edge, and the edges are made tangent at that point.

### Between two edges at point 

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width:400px;">

The two edges are made tangent at a given point. The point can be any point, e.g. the center of a circle, the endpoint of an edge, or the origin, it can belong to one of the edges, and it can also be a [Point object](Sketcher_CreatePoint.md). If required [Point on object constraint(s)](Sketcher_ConstrainPointOnObject.md) are added to ensure the point lies on both (extended) edges. These additional constraints are called [helper constraints](Sketcher_helper_constraint.md).

Compared to direct tangency, this constraint is slower, because there are more degrees of freedom involved, but if the point of tangency is needed, it is recommended because it offers better convergence.

### Between two lines 

<img alt="" src=images/Sketcher_ConstraintTangent_mode5.png  style="width:400px;">

The two lines are made collinear.



## Guión

Tangent Constraint can be created from [macros](Macros.md) and from the [Python](Python.md) console by using the following: 
```python
# direct tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,icurve2))

# point-to-point tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2))

# tangent-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('TangentViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` where:

  - `Sketch` is a sketch object

  - `icurve1`, `icurve2` are two integers identifying the curves to be made tangent. The integers are indices in the sketch (the values, returned by `Sketch.addGeometry`).

  - `pointpos1`, `pointpos2` should be `1` for start point and `2` for end point.

  - `geoidpoint` and `pointpos` in `TangentViaPoint` are the indices specifying the point of tangency.

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `incurve1`, `incurve2`, `pointpos1`, `pointpos2`, `geoidpoint` and `pointpos` and contains further examples on how to create constraints from Python scripts.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainTangent/es
