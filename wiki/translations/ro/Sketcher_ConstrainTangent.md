---
- GuiCommand:
   Name:Sketcher ConstrainTangent
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   MenuLocation:Sketch → Sketcher constraints → Constrain tangent
   Shortcut:T
   SeeAlso:[Constraint point on object](Sketcher_ConstrainPointOnObject.md)
---

# Sketcher ConstrainTangent/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Tangent Constraint makes two curves to touch each other (be tangent). Lines are treated infinite, and arcs are treated as full circles/ellipses. The constraint is also capable of connecting two curves, forcing them tangent at the joint, thus making the joint smooth.


</div>

Tangent Constraint can also be used with two lines to make them colinear.

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

sunt patru moduri diferite în cae contrângerea poate fi aplicată:

1.  between two curves (available not for all curves)
2.  between two endpoints of a curve, making a smooth joint
3.  between a curve and an endpoint of another curve
4.  between two curves at user-defined point


</div>

Pentru a aplica constrângerile de tangență, trebuie să urmați pașii:

-   Select two or three entities in the sketch.
-   Invoke the constraint by clicking its icon on the toolbar, or selecting the menu item, or using keyboard shortcut.

### Între două curbe (direct tangency) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width:600px;">

două curbe vor fi făcute tangente, and the point of tangency will be implicit. This mode is applied if two curves were selected.

**Accepted selection:**

-   line + line, circle, arc, ellipse, arc-of-ellipse
-   circle, arc + circle, arc

Dacă nu este acceptată tangența directă între curbele selectate (de exemplu, între un cerc și o elipsă), va fi adăugat un punct de ajutor pentru a schița automat și se va aplica tangența-prin-punct.

Nu se recomandă reconstruirea punctului de tangență prin crearea unui punct și constrângerea lui de a se afla pe ambele curbe. It will work, but the convergence will be seriously slower, jumpier, and will require about twice as many iterations to converge than normal. Use other modes of this constraint if the point of tangency is needed.

### Între două puncte finale (point-to-point tangency) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width:600px;">


<div class="mw-translate-fuzzy">

În acest mod, punctele finale se fac coincidente, and the joint is made tangent (C1-smooth, or \"sharp\", depending on the placement of curves before the constraint is applied). Acest mod se aplică atunci când au fost selectate două puncte finale de două curbe.


</div>

**Accepted selection:**

-   endpoint of line/arc/arc-of-ellipse + endpoint of line/arc/arc-of-ellipse (i.e., two endpoints of any two curves)

### Între curbă și punct final (point-to-curve tangency) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width:600px;">

În acest mod, un punct final al unei curbe este constrâns să stea pe cealaltă curbă, and the curves are forced tangent at the point. This mode is applied when a curve and an endpoint of another curve were selected.

**Accepted selection:**

-   line, circle, arc, ellipse, arc-of-ellipse + endpoint of line/arc/arc-of-ellipse (i.e., any curve + endpoint of any curve)

### Între două curbe la punct (tangent-via-point) (v0.15) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width:600px;">

În acest mod, două curbe sunt tangente și punctul de tangență este urmărit. Acest mod se aplică atunci când au fost selectate două curbe și un punct.

**Accepted selection:**

-   any line/curve + any line/curve + any point

\"Any point\" can be a lone point, or a point of something, e.g. a center of a circle, an endpoint of an arc, or the origin.


<div class="mw-translate-fuzzy">

Pentru ca constrângerea să funcționeze corect, punctul trebuie să fie pe ambele curbe.So, as the constraint is invoked, the point will be automatically constrained onto both curves ([helper constraints](Sketcher_helper_constraint.md) will be added, if necessary), and the curves will be forced tangent at the point. These [helper constraints](Sketcher_helper_constraint.md) are plain regular constraints. They can be added manually, or deleted.


</div>

În comparație cu tangența directă, această constrângere este mai lentă, deoarece există mai multe grade de libertate implicate, dar dacă este necesar punctul de tangență, acesta este modul recomandat deoarece oferă o convergență mai bună comparativ cu tangența directă + punct pe două curbe.

Plasarea punctului înaintea aplicării constrângerii este o sugestie pentru rezolvitor pentru locul unde ar trebui să fie tangența. Cu această constrângere, se pot constrânge două elipse să se atingă reciproc în două locuri.

### Between two lines (collinear) 

<img alt="" src=images/Sketcher_ConstraintTangent_mode5.png  style="width:600px;">

**Accepted selection:**

-   any line/vertex + any line/vertex

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





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainTangent/ro
