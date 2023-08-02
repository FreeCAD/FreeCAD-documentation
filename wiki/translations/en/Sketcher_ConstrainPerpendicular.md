---
- GuiCommand:
   Name: Sketcher ConstrainPerpendicular
   MenuLocation: Sketch -> Sketcher constraints -> Constrain perpendicular
   Workbenches: Sketcher_Workbench
   Shortcut: **N**
   SeeAlso: Sketcher_ConstrainAngle
---

# Sketcher ConstrainPerpendicular/en

## Description

The Perpendicular Constraint makes two lines to be perpendicular (i.e. orthogonal) to each other, or two curves to be perpendicular at their intersection. Lines are treated infinite, and arcs are treated as full circles/ellipses. The constraint is also capable of connecting two curves, forcing them perpendicular at the joint, similarly to **[<img src=images/Sketcher_ConstrainTangent.svg style="width:16px"> [Constrain tangent](Sketcher_ConstrainTangent.md)**.

## Usage

There are four different ways the constraint can be applied:

1.  between two curves (available not for all curves)
2.  between two endpoints of a curve
3.  between a curve and an endpoint of another curve
4.  between two curves at user-defined point

To apply perpendicular constraint, one should the follow the steps:

-   Select two or three entities in the sketch.
-   Invoke the constraint by clicking its icon on the toolbar, or selecting the menu item, or using keyboard shortcut.

### Between two curves (direct perpendicularity) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode1.png  style="width:600px;">

Two curves will be made perpendicular at point of their intersection (either real, or of curves\' extensions), and the point of intersection will be implicit. This mode is applied if two curves were selected.

**Accepted selection:**

-   line + line, circle, arc
-   circle, arc + circle, arc

If direct perpendicularity between selected curves is not supported (e.g. between a line and an ellipse), a helper point will be added to sketch automatically, and perpendicular-via-point will be applied.

Unlike for tangency, it is perfectly fine to reconstruct the point of perpendicularity by creating a point and constraining it to lie on both curves (thus constraining the point to the intersection).

### Between two endpoints (point-to-point perpendicularity) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode2.png  style="width:600px;">

In this mode, the endpoints are made coincident, and the joint is made to be right angle. This mode is applied when two endpoints of two curves were selected.

**Accepted selection:**

-   endpoint of line/arc/arc-of-ellipse + endpoint of line/arc/arc-of-ellipse (i.e., two endpoints of any two curves)

### Between curve and endpoint (point-to-curve perpendicularity) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode3.png  style="width:600px;">

In this mode, an endpoint of one curve is constrained to lie on the other curve, and the curves are forced perpendicular at the point. This mode is applied when a curve and an endpoint of another curve were selected.

**Accepted selection:**

-   line, circle, arc, ellipse, arc-of-ellipse + endpoint of line/arc/arc-of-ellipse (i.e., any curve + endpoint of any curve)

### Between two curves at point (perpendicular-via-point) (v0.15) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode4.png  style="width:600px;">

In this mode, two curves are made perpendicular, and the point of perpendicularity is tracked. This mode is applied when two curves and a point were selected.

**Accepted selection:**

-   any line/curve + any line/curve + any point

\"Any point\" can be a lone point, or a point of something, e.g. a center of a circle, an endpoint of an arc, or the origin.

For the constraint to work correctly, the point must be on both curves. So, as the constraint is invoked, the point will be automatically constrained onto both curves ([helper constraints](Sketcher_helper_constraint.md) will be added, if necessary), and the curves will be forced perpendicular at the point. These [helper constraints](Sketcher_helper_constraint.md) are plain regular constraints. They can be added manually, or deleted.

Compared to direct perpendicular, this constraint is slower, because there are mode degrees of freedom involved, but it supports ellipses.

The placement of the point before the constraint is applied is a hint for the solver for where the perpendicularity should be.

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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPerpendicular/en
