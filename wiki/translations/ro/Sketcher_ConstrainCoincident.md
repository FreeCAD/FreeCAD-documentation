---
 GuiCommand:
   Name: Sketcher ConstrainCoincident
   Icon: Constraint_PointOnPoint.svg
   Workbenches: Sketcher Workbench/ro
   Shortcut: C
   MenuLocation: Sketch , Sketcher constraints , Constrain coincident
   SeeAlso: Sketcher_ConstrainLock/ro, Sketcher ConstrainPointOnObject/ro
---

# Sketcher ConstrainCoincident/ro


</div>

## Description

The <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Sketcher ConstrainCoincident](Sketcher_ConstrainCoincident.md) tool creates a coincident constraint between points, or (<small>(v0.21)</small> ) a concentric constraint between circles, arcs and/or ellipses (by making their centers coincident).


<small>(v1.0)</small> 

: This tool is replaced by the [Sketcher ConstrainCoincidentUnified](Sketcher_ConstrainCoincidentUnified.md) tool if the **Unify Coincident and PointOnObject** option is selected in the [preferences](Sketcher_Preferences#General.md).

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainCoincident.svg" width=16px> [Constrain coincident](Sketcher_ConstrainCoincident.md)** button.
    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainCoincident.svg" width=16px> Constrain coincident** option from the menu.
    -   Use the keyboard shortcut: **C**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two points.
    -   Select two edges of circles, arcs, ellipses or arcs of ellipses.
5.  A constraint is added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Do one of the following:
    -   Select two or more points.
    -   Select two or more edges of circles, arcs, ellipses or arcs of ellipses.
2.  Invoke the tool as explained above.
3.  Depending on the selection one or more constraints are added.

## Notes

-    <small>(v1.0)</small> : Points with Coincident constraints are marked with the **Constraint symbols** [color](Sketcher_Preferences#Display.md).




<div class="mw-translate-fuzzy">

### General scripting 

Constrângerea poate fi creată din macrocomenzi și din consola Python folosind următoarea comandă:


</div>

The constraint can be created from [macros](Macros.md) and from the [Python](Python.md) console by using the following command:


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```


<div class="mw-translate-fuzzy">

unde :

-   Sketch este un obiect sketch
-   LineFixed este numărul liniei care nu se mișcă prin aplicarea constrângerii
-   PointOfLineFixed este numărul liniei liniei Fixed care trebuie să îndeplinească constrângerea
-   LineMoving este numărul liniei care se va deplasa prin aplicarea constrângerii
-   PointOfLineMoving este numărul liniei este LineMoving, care trebuie să îndeplinească constrângerea


</div>

As the names `LineFixed` and `LineMoving` indicate, if both constrained vertices are free to move in any direction, the first one (first to be selected in the Gui) will remain fixed and the other one will move. In the presence of existing constraints, however, both edges may move.

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `LineFixed`, `PointOfLineFixed`, `LineMoving` and `PointOfLineMoving`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">


</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/ro
