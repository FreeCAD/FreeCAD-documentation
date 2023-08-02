---
- GuiCommand:
   Name: Constraint PointOnObject
   Name/es: Constraint PointOnObject
   Workbenches: Sketcher Workbench/es, PartDesign Workbench/es
   MenuLocation: Croquizador -> Restricciones del Croquizador -> Punto en objeto
   SeeAlso: Sketcher_ConstrainCoincident/es
---

# Sketcher ConstrainPointOnObject/es


</div>

## Description


<div class="mw-translate-fuzzy">

#### Descrición


</div>


<div class="mw-translate-fuzzy">

#### Usage


</div>

1.  Select a point and an edge in any order.
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> [Constrain point onto object](Sketcher_ConstrainPointOnObject.md)** button in the toolbar.
    -   Use the **O** keyboard shortcut.
    -   Use the **Sketch → Sketcher constraints → [<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> Constrain point onto object** entry in the top menu.

## Scripting

The constraint can be created from [macros](Macros.md) and from the [Python](Python.md) console by using the following command:


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`is a sketch object.

-    `LineMoving`is the number that designates the line, which contains the point that has to be moved onto the `LineFixed` (the line which is fixed).

-    `PointOfLineMoving`is the number of the vertex of line `LineMoving`, that has to be moved onto the `LineFixed`.

-    `LinedFixed`is the number of the line to be affixed onto the point `PointOfLineMoving`.

The [Sketcher scripting](Sketcher_scripting.md) page explains how to identify the numbers that designate lines and points.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/es
