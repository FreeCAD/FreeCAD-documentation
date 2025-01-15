---
 GuiCommand:
   Name: Sketcher ConstrainTangent
   Workbenches: Sketcher Workbench
   MenuLocation: Sketch , Sketcher constraints , Constrain tangent
   Shortcut: T
   SeeAlso: Sketcher ConstrainPointOnObject
---

# Sketcher ConstrainTangent/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Tangent Constraint makes two curves to touch each other (be tangent). Lines are treated infinite, and arcs are treated as full circles/ellipses. The constraint is also capable of connecting two curves, forcing them tangent at the joint, thus making the joint smooth.


</div>

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainTangent.svg" width=16px> [Constrain tangent or collinear](Sketcher_ConstrainTangent.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainTangent.svg" width=16px> Constrain tangent or collinear** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Constrain → <img src="images/Sketcher_ConstrainTangent.svg" width=16px> Constrain tangent or collinear** option from the context menu.

    -   Use the keyboard shortcut: **T**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two edges. The edges can be any edge except a B-spline.
    -   Select a point and two edges (in that order).
    -   Select an edge, a point and another edge (idem).
5.  A Tangent constraint is added. If a point and two edges have been selected, up to two [Point on object constraints](Sketcher_ConstrainPointOnObject.md) can also be added. See [Examples](#Between_two_edges_at_point.md).
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Do one of the following:
    -   Select two edges (see above).
    -   Select two endpoints belonging to different edges.
    -   Select an edge and the endpoint of another edge (in any order).
    -   Select a point and two edges (idem).
2.  Invoke the tool as explained above, or with the following additional option:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainTangent.svg" width=16px> Constrain tangent or collinear** option from the context menu.
3.  A Tangent constraint is added. If a point and two edges have been selected, up to two [Point on object constraints](Sketcher_ConstrainPointOnObject.md) can also be added. See [Examples](#Between_two_edges_at_point.md).

## Examples




<div class="mw-translate-fuzzy">

### Între două curbe (direct tangency) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width:600px;">


</div>

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width:400px;">

The two edges are made tangent. If one of the edges is a [conic](Sketcher_Workbench#Sketcher_CompCreateConic.md), a [Point object](Sketcher_CreatePoint.md) that has a [Point on object constraint](Sketcher_ConstrainPointOnObject.md) with both (extended) edges is added.


<div class="mw-translate-fuzzy">

Nu se recomandă reconstruirea punctului de tangență prin crearea unui punct și constrângerea lui de a se afla pe ambele curbe. It will work, but the convergence will be seriously slower, jumpier, and will require about twice as many iterations to converge than normal. Use other modes of this constraint if the point of tangency is needed.


</div>




<div class="mw-translate-fuzzy">

### Între două puncte finale (point-to-point tangency) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width:600px;">


</div>

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width:400px;">

The endpoints are made coincident, and the angle between the edges at that point is set to 180° (smooth joint) or 0° (sharp joint), depending on the placement of the edges before the constraint is applied.




<div class="mw-translate-fuzzy">

### Între curbă și punct final (point-to-curve tangency) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width:600px;">


</div>

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width:400px;">


<div class="mw-translate-fuzzy">

În acest mod, un punct final al unei curbe este constrâns să stea pe cealaltă curbă, and the curves are forced tangent at the point. This mode is applied when a curve and an endpoint of another curve were selected.


</div>




<div class="mw-translate-fuzzy">

### Între două curbe la punct (tangent-via-point) (v0.15) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width:600px;">


</div>

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width:400px;">


<div class="mw-translate-fuzzy">

În acest mod, două curbe sunt tangente și punctul de tangență este urmărit. Acest mod se aplică atunci când au fost selectate două curbe și un punct.


</div>


<div class="mw-translate-fuzzy">

În comparație cu tangența directă, această constrângere este mai lentă, deoarece există mai multe grade de libertate implicate, dar dacă este necesar punctul de tangență, acesta este modul recomandat deoarece oferă o convergență mai bună comparativ cu tangența directă + punct pe două curbe.


</div>

### Between two lines 

<img alt="" src=images/Sketcher_ConstraintTangent_mode5.png  style="width:400px;">

The two lines are made collinear.



## Script


<div class="mw-translate-fuzzy">

Tangent Constraint poate fi creată din [macros](macros.md) și din consola python folosind următoarele:


</div>


```python
# direct tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,icurve2))

# point-to-point tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2))

# tangent-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('TangentViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
```


<div class="mw-translate-fuzzy">

unde:

  - Sketch is a sketch object

  - icurve1, icurve2 are two integers identifying the curves to be made tangent. The integers are indexes in the sketch (the value, returned by Sketch.addGeometry).

  - pointpos1, pointpos2 should be 1 for start point and 2 for end point.

  - geoidpoint and pointpos in TangentViaPoint are the indexes specifying the point of tangency.


</div>

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `incurve1`, `incurve2`, `pointpos1`, `pointpos2`, `geoidpoint` and `pointpos` and contains further examples on how to create constraints from Python scripts.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainTangent/ro
