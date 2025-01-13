---
 GuiCommand:
   Name: Sketcher ConstrainCoincidentUnified
   MenuLocation: Sketch , Sketcher constraints , Constrain coincident
   Workbenches: Sketcher_Workbench
   Shortcut: **C**
   Version: 1.0
   SeeAlso: Sketcher_ConstrainCoincident, Sketcher_ConstrainPointOnObject
---

# Sketcher ConstrainCoincidentUnified/pt-br


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Description


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:24px;"> [Sketcher ConstrainCoincidentUnified](Sketcher_ConstrainCoincidentUnified.md) tool creates a coincident constraint between points, fixes points on edges or axes (lines are then treated as infinite, and open curves are virtually extended as well), or creates a concentric constraint between circles, arcs and/or ellipses (by making their centers coincident).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

This tool replaces the [Sketcher ConstrainCoincident](Sketcher_ConstrainCoincident.md) and [Sketcher ConstrainPointOnObject](Sketcher_ConstrainPointOnObject.md) tools if the **Unify Coincident and PointOnObject** option is selected in the [preferences](Sketcher_Preferences#General.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Usage


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> [Constrain coincident](Sketcher_ConstrainCoincidentUnified.md)** button.
    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Constrain coincident** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **Constrain → <img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Constrain coincident** option from the context menu.
    -   Use the keyboard shortcut: **C**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two points.
    -   Select two edges of circles, arcs, ellipses or arcs of ellipses.
    -   Select a single point and a single edge (in any order).
5.  A constraint is added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.


</div>



### Modo de execução única 


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Do one of the following:
    -   Select two or more points.
    -   Select two or more edges of circles, arcs, ellipses or arcs of ellipses.
    -   Select a single point and a single edge (in any order).
    -   Select several points and a single edge (idem).
    -   Select a single point and several edges (idem).
2.  Invoke the tool as explained above, or with the following additional option:
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Constrain coincident** option from the context menu.
3.  Depending on the selection one or more constraints are added.


</div>



## Notas


<div lang="en" dir="ltr" class="mw-content-ltr">

-    <small>(v1.0)</small> : Points with Coincident constraints are marked with the **Constraint symbols** [color](Sketcher_Preferences#Display.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincidentUnified/pt-br
