# Sketcher ConstrainAngle/pt
---
- GuiCommand:/pt   Name:Constraint InternalAngle   Name/pt:Constraint InternalAngle   Workbenches:_, [Constraint Perpendicular](Constraint_Perpendicular/pt.md)---


</div>

## Description

Angle constraint is a [datum constraint](Sketcher_Workbench#Sketcher_Constraints.md) intended to fix angles in sketch. It is capable of setting slopes of individual lines, angles between lines, angles of intersections of curves, and angle spans of circular arcs.

## Usage

There are four different ways the constraint can be applied:

-   to individual lines
-   between lines
-   to intersections of curves
-   to arcs of circles

To apply angle constraint, one should the follow the steps:

1.  Select one, two or three entities in the sketch. The mode will be chosen depending on the selection.
2.  Invoke the constraint using several methods:
    -   Pressing the **<img src=images/Sketcher_ConstrainAngle.svg style="width:16px"> [Constrain angle](Sketcher_ConstrainAngle.md)** button in the toolbar.
    -   Using the **A** keyboard shortcut. (**A** is for **A**ngle)
    -   Using the **Sketch → Sketcher constraints → <img src=images/Sketcher_ConstrainAngle.svg style="width:16px"> Constrain angle** form the top menu entry
3.  A datum edit dialog box pops up.
4.  Modify the angle if necessary. **Note:** The angle can be entered as an expression that will be evaluated and the result will be stored.
5.  Click **OK**

As with any datum constraint, it is possible to change the angle value later by double-clicking the constraint in constraint list or 3d view. Entering a negative value will cause the angle direction to flip.

## Constraint modes 

### Line slope angle 

**Accepted selection:** line

<img alt="" src=images/Sketcher_ConsraintAngle_mode1.png  style="width:600px;">

The constraint sets the polar angle of line\'s direction. It is the angle between the line and X axis of the sketch.

### Arc span (v0.15) 

**Accepted selection:** arc of circle

<img alt="" src=images/Sketcher_ConsraintAngle_mode2.png  style="width:600px;">

In this mode, the constraint fixes angular span of a circular arc.

### Between lines 

**Accepted selection:** line + line

<img alt="" src=images/Sketcher_ConsraintAngle_mode3.png  style="width:600px;">

In this mode, the constraint sets the angle between two lines. It is not required that the lines intersect.

### Between curves at intersection (angle-via-point) (v0.15) 

**Accepted selection:** any line/curve + any line/curve + any point

<img alt="" src=images/Sketcher_ConsraintAngle_mode4.png  style="width:600px;">

In this mode, angle between two curves is constrained at the point of their intersection. The intersection point can be on curves\' extensions. The point should be specified explicitly, since curves typically intersect in more than one point.

For the constraint to work correctly, the point must be on both curves. So, as the constraint is invoked, the point will be automatically constrained onto both curves ([helper constraints](Sketcher_helper_constraint.md) will be added, if necessary), and the angle between curves will be constrained at the point. These [helper constraints](Sketcher_helper_constraint.md) are plain regular constraints. They can be added manually, or deleted. There are no helper constraints on the example picture above, because the point selected is already the intersection of curves.

## Scripting

Angle Constraint can be created from [macros](Macros.md) and from the python console by using the following: 
```python
# line slope angle
Sketch.addConstraint(Sketcher.Constraint('Angle',iline,angle))

# angular span of arc
Sketch.addConstraint(Sketcher.Constraint('Angle',iarc,angle))

# angle between lines
Sketch.addConstraint(Sketcher.Constraint('Angle',iline1,pointpos1,iline2,pointpos2,angle))

# angle-via-point (no helper constraints are added automatically when from python)
Sketch.addConstraint(Sketcher.Constraint('AngleViaPoint',icurve1,icurve2,geoidpoint,pointpos,angle))
``` where:

:\* `Sketch` is a sketch object

:\* `iline, iline1, iline2` are integers specifying the lines by their ordinal numbers in `Sketch`.

:\* `pointpos1, pointpos2` should be 1 for start point and 2 for end point. The choice of endpoints allows to set internal angle (or external), and it affects how the constraint is drawn on the screen.

:\* `geoidpoint` and `pointpos` in `AngleViaPoint` are the indexes specifying the point of intersection.

:\* `angle` is the angle value in radians. The angle is counted between tangent vectors in counterclockwise direction. Tangent vectors are pointing from start to end for the lines (or vice versa if ending point is supplied in angle between lines mode), and along counterclockwise direction for circles, arcs and ellipses. Quantity is also accepted as an angle (e.g. `App.Units.Quantity('45 deg')`)

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `iline`, `iline1`, `iline2`, `pointpos1`, `pointpos2`, `geoidpoint` and `pointpos` and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainAngle/pt
