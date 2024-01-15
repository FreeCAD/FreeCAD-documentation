---
 GuiCommand:
   Name: Sketcher ConstrainPointOnObject
   MenuLocation: Sketch , Sketcher constraints , Constrain point onto object
   Workbenches: Sketcher_Workbench
   Shortcut: **O**
   SeeAlso: Sketcher_ConstrainCoincidentUnified, Sketcher_ConstrainCoincident
---

# Sketcher ConstrainPointOnObject

## Description

The <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Sketcher ConstrainPointOnObject](Sketcher_ConstrainPointOnObject.md) command fixes points on edges or axes.


<small>(v0.22)</small> 

: This command is replaced by the [Sketcher ConstrainCoincidentUnified](Sketcher_ConstrainCoincidentUnified.md) command if the **Unify Coincident and PointOnObject** option is selected in the [Sketcher Preferences](Sketcher_Preferences#General.md).

## Usage

1.  Optionally do one of the following:
    -   Select a single point and a single edge (in any order).
    -   Select several points and a single edge (idem).
    -   Select a single point and several edges (idem).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> [Constrain point onto object](Sketcher_ConstrainPointOnObject.md)** button.
    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> Constrain point onto object** option from the menu.
    -   Use the keyboard shortcut: **O**.
3.  To indicate that the command has been activated the cursor shows a white cross and the command icon.
4.  Optionally keep selecting elements. You can only select two elements at a time now.
5.  To finish the command press **Esc** or the right mouse button, or start a another constraints or geometries command.

## Scripting

The constraint can be created from [macros](Macros.md) and from the [Python](Python.md) console by using the following command:


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`is a sketch object.

-    `LineMoving`is the number that designates the line, which contains the point that has to be moved onto the `LineFixed` (the line which is fixed).

-    `PointOfLineMoving`is the number of the vertex of line `LineMoving`, that has to be moved onto the `LineFixed`.

-    `LinedFixed`is the number of the line to be affixed onto the point `PointOfLineMoving`.

The [Sketcher scripting](Sketcher_scripting.md) page explains how to identify the numbers that designate lines and points.




 {{Sketcher_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject
