---
- GuiCommand:
   Name:Sketcher ConstrainCoincident
   MenuLocation:Sketch → Sketcher constraints → Constrain coincident
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:**C**
   SeeAlso:[Sketcher Constrain Lock](Sketcher_ConstrainLock.md), [Sketcher Constrain Point onto Object](Sketcher_ConstrainPointOnObject.md)
---

## Description

Create a coincident constraint on the selected item

This constraint tool takes two points as its argument and serves to make the two points *coincident*. (Meaning to make them as-one-point).

In practical terms this constraint tool is useful when there is a break in a profile for example - where two lines end near each other and need to be joined - a coincident constraint on their end-points will close the gap.

## Usage

As stated above, this tool takes two arguments - both are points.

1.  First, it is necessary to highlight two distinct points. (**Note:** this will not work if, for example, you attempt to select the start and end point of the same straight line; selecting the start and end points of an arc will produce a closed circle or ellipse but will constrain the location of the seam to be on that point).
2.  Highlighting of a drawing item is achieved by moving the mouse over the item and clicking the left-mouse-button.
3.  It is also possible to highlight all items inside a rectangle by clicking and dragging. When dragging from left to right (with any vertical motion), only the shapes which are entirely contained within the rectangle will be highlighted; in the other direction all shapes which intersect with the selection rectangle will be highlighted. This can be used to select only the vertices without selecting the edges, by dragging a small recangle around some vertices from left to right, as long as there are no edges which are fully contained within the rectangle.
4.  A highlighted item will change its color to green. (This color can be customized in **Editing → Preference → Display → Colors → Selection**)
5.  Subsequent items can be highlighted by repeating the above procedure(s). **Note:** it\'s unnecessary to hold-down any special key like **Ctrl** to achieve multiple item selection in a drawing.
6.  Once you have two points highlighted, you can invoke the command using several methods:
    -   Pressing on the **<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> [Coinstrain coincident](Sketcher_ConstrainCoincident.md)** constraint button in the toolbar.
    -   Using the **C** keyboard shortcut.
    -   Using the **Sketch → Sketcher constraints → Constrain coincident** entry in the top menu.


**Result:**

the command will cause the two points to become *coincident* and be replaced by a single point.


**Note:**

In order to make two points coincident, FreeCAD must out of necessity move one (or both) of the original points.

## Alternatives to Coincident constraint 

The two constrained items of a [Coincident](Sketcher_ConstrainCoincident.md) constraint must be start point or end point vertices, or center points of arcs, circles or ellipses. Some combinations which are not possible with a coincident constraint can be emulated using other constraints:

-   The <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) constraint can be used to place a start point, end point or center point on the midpoint of a straight line.
-   A midpoint-to-midpoint placement of two straight lines can be achieved by creating a new <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:24px;"> [Point](Sketcher_CreatePoint.md) and using two <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) constraints so that it lies on the midpoint of both lines.
-   A vertex can be constrained to lie along an edge using a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;">[PointOnObject](Sketcher_ConstrainPointOnObject.md) constraint. Note that with this constraint, the point can lie anywhere on the full extension of a segment or curve (i.e. also before the start point or beyond the end point).
-   A collinear placement of two straight lines can be obtained by applying a <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Tangent](Sketcher_ConstrainTangent.md) constraint to them, or by combining a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [PointOnObject](Sketcher_ConstrainPointOnObject.md) constraint and a <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> [Parallel](Sketcher_ConstrainParallel.md) constraint.
-   Two edges can be made identical by using two <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident](Sketcher_ConstrainCoincident.md) constraints, one for each pair of extremities.
-   Two circles can be made identical by using a <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident](Sketcher_ConstrainCoincident.md) constraint to merge the centers, and applying an <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> [Equal](Sketcher_ConstrainEqual.md) constraint to their edges. For arcs, this will ensure both arcs are part of the same circle, while allowing them to have different start and end points.

## Scripting

The constraint can be created from [macros](Macros.md) and from the [Python](Python.md) console by using the following command:


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```

where :

-    `Sketch`is a sketch object

-    `LineFixed`is the number of the line, that will not move by applying the constraint

-    `PointOfLineFixed`indicates which vertex of `LineFixed` has to fulfill the constraint

-    `LineMoving`is the number of the line, that will move by applying the constraint

-    `PointOfLineMoving`indicates which vertex of `LineMoving` has to fulfill the constraint

As the names `LineFixed` and `LineMoving` indicate, if both constrained vertices are free to move in any direction, the first one (first to be selected in the Gui) will remain fixed and the other one will move. In the presence of existing constraints, however, both edges may move.

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `LineFixed`, `PointOfLineFixed`, `LineMoving` and `PointOfLineMoving`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}  
