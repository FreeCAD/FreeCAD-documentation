---
 GuiCommand:
   Name: Sketcher ConstrainPointOnObject
   MenuLocation: Sketch , Sketcher constraints , Constrain point on object
   Workbenches: Sketcher_Workbench
   Shortcut: **O**
   SeeAlso: Sketcher_ConstrainCoincidentUnified, Sketcher_ConstrainCoincident
---

# Sketcher ConstrainPointOnObject/en

## Description

The <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Sketcher ConstrainPointOnObject](Sketcher_ConstrainPointOnObject.md) tool fixes points on edges or axes. Lines are treated as infinite, and open curves are virtually extended as well.


<small>(v1.0)</small> 

: This tool is replaced by the [Sketcher ConstrainCoincidentUnified](Sketcher_ConstrainCoincidentUnified.md) tool if the **Unify Coincident and PointOnObject** option is selected in the [preferences](Sketcher_Preferences#General.md).

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> [Constrain point on object](Sketcher_ConstrainPointOnObject.md)** button.
    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> Constrain point on object** option from the menu.
    -   Use the keyboard shortcut: **O**.
3.  The cursor changes to a cross with the tool icon.
4.  Select a single point and a single edge (in any order).
5.  A constraint is added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Do one of the following:
    -   Select a single point and a single edge (in any order).
    -   Select several points and a single edge (idem).
    -   Select a single point and several edges (idem).
2.  Invoke the tool as explained above.
3.  Depending on the selection one or more constraints are added.

## Scripting

The constraint can be created from [macros](Macros.md) and from the [Python](Python.md) console by using the following command:


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`is a sketch object.

-    `LineMoving`is the number that designates the line, which contains the point that has to be moved on the `LineFixed` (the line which is fixed).

-    `PointOfLineMoving`is the number of the vertex of line `LineMoving`, that has to be moved on the `LineFixed`.

-    `LinedFixed`is the number of the line to be affixed on the point `PointOfLineMoving`.

The [Sketcher scripting](Sketcher_scripting.md) page explains how to identify the numbers that designate lines and points.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/en
