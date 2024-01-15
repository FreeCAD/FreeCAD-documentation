---
 GuiCommand:
   Name: Sketcher ConstrainCoincident
   MenuLocation: Sketch , Sketcher constraints , Constrain coincident
   Workbenches: Sketcher_Workbench
   Shortcut: **C**
   SeeAlso: Sketcher_ConstrainCoincidentUnified, Sketcher_ConstrainPointOnObject
---

# Sketcher ConstrainCoincident

## Description

The <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Sketcher ConstrainCoincident](Sketcher_ConstrainCoincident.md) command creates a coincident constraint between points, or (<small>(v0.21)</small> ) a concentric constraint between circles, arcs and/or ellipses (by making their centers coincident).


<small>(v0.22)</small> 

: This command is replaced by the [Sketcher ConstrainCoincidentUnified](Sketcher_ConstrainCoincidentUnified.md) command if the **Unify Coincident and PointOnObject** option is selected in the [Sketcher Preferences](Sketcher_Preferences#General.md).

## Usage

1.  Optionally do one of the following:
    -   Select two or more points.
    -   Select two or more edges of circles, arcs, ellipses or arcs of ellipses.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Sketcher_ConstrainCoincident.svg" width=16px> [Constrain coincident](Sketcher_ConstrainCoincident.md)** button.
    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainCoincident.svg" width=16px> Constrain coincident** option from the menu.
    -   Use the keyboard shortcut: **C**.
3.  To indicate that the command has been activated the cursor shows a white cross and the command icon.
4.  Optionally keep selecting elements. You can only select two elements at a time now.
5.  To finish the command press **Esc** or the right mouse button, or start a another constraints or geometries command.

## Alternatives to Coincident constraint 

Some combinations which are not possible with a coincident constraint can be emulated using other constraints:

-   The <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) constraint can be used to place a start point, end point or center point on the midpoint of a straight line.
-   A midpoint-to-midpoint placement of two straight lines can be achieved by creating a new <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:16px;"> [Point](Sketcher_CreatePoint.md) and using two <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) constraints so that it lies on the midpoint of both lines.
-   A vertex can be constrained to lie along an edge using a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [PointOnObject](Sketcher_ConstrainPointOnObject.md) constraint. Note that with this constraint, the point can lie anywhere on the full extension of a segment or curve (i.e. also before the start point or beyond the end point).
-   A collinear placement of two straight lines can be obtained by applying a <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:16px;"> [Tangent](Sketcher_ConstrainTangent.md) constraint to them, or by combining a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [PointOnObject](Sketcher_ConstrainPointOnObject.md) constraint and a <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:16px;"> [Parallel](Sketcher_ConstrainParallel.md) constraint.

## Scripting

The constraint can be created from [macros](Macros.md) and from the [Python](Python.md) console by using the following command:

 

where :

-    `Sketch`is a sketch object

-    `LineFixed`is the number of the line, that will not move by applying the constraint

-    `PointOfLineFixed`indicates which vertex of `LineFixed` has to fulfill the constraint

-    `LineMoving`is the number of the line, that will move by applying the constraint

-    `PointOfLineMoving`indicates which vertex of `LineMoving` has to fulfill the constraint

As the names `LineFixed` and `LineMoving` indicate, if both constrained vertices are free to move in any direction, the first one (first to be selected in the Gui) will remain fixed and the other one will move. In the presence of existing constraints, however, both edges may move.

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `LineFixed`, `PointOfLineFixed`, `LineMoving` and `PointOfLineMoving`, and contains further examples on how to create constraints from Python scripts.




 {{Sketcher_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident
