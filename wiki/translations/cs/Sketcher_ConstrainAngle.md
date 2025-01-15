---
 GuiCommand:
   Name: Constraint InternalAngle
   Name/cs: Constraint InternalAngle
   Workbenches: Sketcher Workbench/cs, PartDesign Workbench/cs
   Shortcut: A
   MenuLocation: Sketch , Sketcher constraints , Constrain angle
   SeeAlso: Sketcher_ConstrainDistance/cs, Sketcher_ConstrainPerpendicular/cs
---

# Sketcher ConstrainAngle/cs


</div>

## Description

The <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;"> [Sketcher ConstrainAngle](Sketcher_ConstrainAngle.md) tool fixes the angle between two edges (lines are then treated as infinite, and open curves are virtually extended as well), the angle of a line with the horizontal axis of the sketch, or the aperture angle of a circular arc.

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   
        <small>(v1.0)</small> 
        
        : If the **Dimensioning constraints** [preference](Sketcher_Preferences#General.md) is set to {{Value|Single tool}} (default): press the down arrow to the right of the **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button and select the **<img src="images/Sketcher_ConstrainAngle.svg" width=16px> Constrain angle** option from the dropdown.

    -   If this preference has a different value (and in {{VersionMinus|0.21}}): press the **<img src="images/Sketcher_ConstrainAngle.svg" width=16px> [Constrain angle](Sketcher_ConstrainAngle.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainAngle.svg" width=16px> Constrain angle** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Dimension → <img src="images/Sketcher_ConstrainAngle.svg" width=16px> Constrain angle** option from the context menu.

    -   Use the keyboard shortcut: **K** then **A**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two lines.
    -   Select a point and two edges (in that order).
    -   Select an edge, a point and an edge (idem).
5.  If a [driving dimensional constraint](Sketcher_ToggleDrivingConstraint.md) is created, depending on the [preferences](Sketcher_Preferences#Display.md), a dialog opens to [edit its value](Sketcher_Workbench#Edit_constraints.md). A negative value will reverse the angle direction.
6.  An Angle constraint is added. If a point and two edges have been selected, up to two [Point to object constraints](Sketcher_ConstrainPointOnObject.md) can also be added. See [Examples](#Between_two_edges_at_point.md).
7.  Optionally keep creating constraints.
8.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Do one of the following:
    -   Select a single line.
    -   Select a single circular arc.
    -   Select two lines.
    -   Select a point and two edges (in any order).
2.  Invoke the tool as explained above.
3.  Optionally [edit the constraint value](Sketcher_Workbench#Edit_constraints.md).
4.  An Angle constraint is added. If a point and two edges have been selected, up to two [Point on object constraints](Sketcher_ConstrainPointOnObject.md) can also be added. See [Examples](#Between_two_edges_at_point.md).

## Examples

### Single line 

<img alt="" src=images/Sketcher_ConsraintAngle_mode1.png  style="width:400px;">

The angle of the line with the positive X axis of the sketch is fixed.

### Single circular arc 

<img alt="" src=images/Sketcher_ConsraintAngle_mode2.png  style="width:400px;">

The aperture angle of the arc is fixed.

### Between two lines 

<img alt="" src=images/Sketcher_ConsraintAngle_mode3.png  style="width:400px;">

The angle between the two lines is fixed. It is not required that the lines intersect.

### Between two edges at point 

<img alt="" src=images/Sketcher_ConsraintAngle_mode4.png  style="width:400px;">

The angle between the two edges at a given point is fixed. The point can be any point, e.g. the center of a circle, the endpoint of an edge, or the origin, it can belong to either or both edges, and it can also be a [Point object](Sketcher_CreatePoint.md). If required [Point on object constraint(s)](Sketcher_ConstrainPointOnObject.md) are added to ensure the point lies on both (extended) edges. These additional constraints are called [helper constraints](Sketcher_helper_constraint.md).

## Scripting

Angle Constraint can be created from [macros](Macros.md) and from the [Python](Python.md) console by using the following: 
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

  - `Sketch` is a sketch object

  - `iline, iline1, iline2` are integers specifying the lines by their ordinal numbers in `Sketch`.

  - `pointpos1, pointpos2` should be 1 for start point and 2 for end point. The choice of endpoints allows to set internal angle (or external), and it affects how the constraint is drawn on the screen.

  - `geoidpoint` and `pointpos` in `AngleViaPoint` are the indexes specifying the point of intersection.

  - `angle` is the angle value in radians. The angle is counted between tangent vectors in counterclockwise direction. Tangent vectors are pointing from start to end for the lines (or vice versa if ending point is supplied in angle between lines mode), and along counterclockwise direction for circles, arcs and ellipses. Quantity is also accepted as an angle (e.g. `App.Units.Quantity('45 deg')`)

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `iline`, `iline1`, `iline2`, `pointpos1`, `pointpos2`, `geoidpoint` and `pointpos` and contains further examples on how to create constraints from Python scripts.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainAngle/cs
