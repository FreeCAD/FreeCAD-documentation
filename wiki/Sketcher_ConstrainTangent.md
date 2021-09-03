---
- GuiCommand:
   Name:Sketcher ConstrainTangent
   MenuLocation:Sketch → Sketcher constraints → Constrain tangent
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:**T**
   SeeAlso:[Sketcher Constraint point on object](Sketcher_ConstrainPointOnObject.md)
---

## Description

Tangent Constraint makes two curves to touch each other (be tangent). Lines are treated infinite, and arcs are treated as full circles/ellipses. The constraint is also capable of connecting two curves, forcing them tangent at the joint, thus making the joint smooth.

Tangent Constraint can also be used with two lines to make them colinear.

## Usage

There are five different ways the constraint can be applied:

1.  between two curves (available not for all curves)
2.  between two endpoints of a curve, making a smooth joint
3.  between a curve and an endpoint of another curve
4.  between two curves at user-defined point
5.  between two lines to create a collinear condition

To apply tangent constraint, one should the follow the steps:

-   Select two or three entities in the sketch.
-   Invoke the constraint by clicking its icon on the toolbar, or selecting the menu item, or using keyboard shortcut.

### Between two curves (direct tangency) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width:600px;">

Two curves will be made tangent, and the point of tangency will be implicit. This mode is applied if two curves were selected.

**Accepted selection:**

-   line + line, circle, arc, ellipse, arc-of-ellipse
-   circle, arc + circle, arc

If direct tangency between selected curves is not supported (e.g. between a circle and an ellipse), a helper point will be added to sketch automatically, and tangency-via-point will be applied.

It is not recommended to reconstruct the point of tangency by creating a point and constraining it to lie on both curves. It will work, but the convergence will be seriously slower, jumpier, and will require about twice as many iterations to converge than normal. Use other modes of this constraint if the point of tangency is needed.

### Between two endpoints (point-to-point tangency) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width:600px;">

In this mode, the endpoints are made coincident, and the joint is made tangent (C1-smooth, or \"sharp\", depending on the placement of curves before the constraint is applied). This mode is applied when two endpoints of two curves were selected. If you want this kind of tangency you must not use concidence plus the tangency between the curves/lines. The solver cannot create stable solutions for this combination and replaces the constraints appropriately.

**Accepted selection:**

-   endpoint of line/arc/arc-of-ellipse + endpoint of line/arc/arc-of-ellipse (i.e., two endpoints of any two curves)

### Between curve and endpoint (point-to-curve tangency) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width:600px;">

In this mode, an endpoint of one curve is constrained to lie on the other curve, and the curves are forced tangent at the point. This mode is applied when a curve and an endpoint of another curve were selected.

**Accepted selection:**

-   line, circle, arc, ellipse, arc-of-ellipse + endpoint of line/arc/arc-of-ellipse (i.e., any curve + endpoint of any curve)

### Between two curves at point (tangent-via-point) (v0.15) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width:600px;">

In this mode, two curves are made tangent, and the point of tangency is tracked. This mode is applied when two curves and a point were selected.

**Accepted selection:**

-   any line/curve + any line/curve + any point

\"Any point\" can be a lone point, or a point of something, e.g. a center of a circle, an endpoint of an arc, or the origin.

For the constraint to work correctly, the point must be on both curves. So, as the constraint is invoked, the point will be automatically constrained onto both curves ([helper constraints](Sketcher_helper_constraint.md) will be added, if necessary), and the curves will be forced tangent at the point. These [helper constraints](Sketcher_helper_constraint.md) are plain regular constraints. They can be added manually, or deleted.

Compared to direct tangency, this constraint is slower, because there are more degrees of freedom involved, but if the point of tangency is needed, it is the recommended mode because it offers better convergence compared to direct tangency + point on two curves.

The placement of the point before the constraint is applied is a hint for the solver for where the tangency should be. With this constraint, one can constrain two ellipses to touch each other in two places.

### Between two lines (collinear) 

<img alt="" src=images/Sketcher_ConstraintTangent_mode5.png  style="width:600px;">

**Accepted selection:**

-   any line/vertex + any line/vertex

## Scripting

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

:\* `Sketch` is a sketch object

:\* `icurve1`, `icurve2` are two integers identifying the curves to be made tangent. The integers are indexes in the sketch (the value, returned by `Sketch.addGeometry`).

:\* `pointpos1`, `pointpos2` should be 1 for start point and 2 for end point.

:\* `geoidpoint` and `pointpos` in `TangentViaPoint` are the indexes specifying the point of tangency.

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `incurve1`, `incurve2`, `pointpos1`, `pointpos2`, `geoidpoint` and `pointpos` and contains further examples on how to create constraints from Python scripts.




 {{Sketcher Tools navi}}  
