---
- GuiCommand:/es
   Icon:Constraint PointOnPoint.svg
   Name/es:Restricción de coincidencia
   Workbenches:[Sketcher](Sketcher_Workbench/es.md)
   Shortcut:C
   MenuLocation:Sketch → Restricciones de croquis → Restricción de coincidencia   SeeAlso:[Restricción de bloqueo](Sketcher_ConstrainLock/es.md), [Punto en objeto](Sketcher_ConstrainPointOnObject/es.md)
---

# Sketcher ConstrainCoincident/es


</div>

## Description


<div class="mw-translate-fuzzy">

\"Crea una restricción de coincidencia en los objetos seleccionados\"

## Descripción

Esta restricción permite hacer dos puntos coincidentes.


</div>

This constraint tool takes two points as its argument and serves to make the two points *coincident*. (Meaning to make them as-one-point).

In practical terms this constraint tool is useful when there is a break in a profile for example - where two lines end near each other and need to be joined - a coincident constraint on their end-points will close the gap.

## Usage


<div class="mw-translate-fuzzy">

## Utilización

1.  Selecciona dos puntos.
2.  Selecciona la restricción \'Coincidencia\' y los dos puntos pasarán a ser coincidentes.


</div>


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


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}}  

[<img src="images/Property.png" style="width:16px"> Sketcher/es](<img src="images/Property.png" style="width:16px"> Sketcher/es.md)

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/es
