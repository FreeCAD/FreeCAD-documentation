---
- GuiCommand:/pt-br
   Name:Constraint Symmetric
   Name/pt-br:Constraint Symmetric
   Workbenches:[Sketcher](Sketcher_Workbench/pt-br.md), [PartDesign](PartDesign_Workbench/pt-br.md)
   MenuLocation:Sketch → Sketcher constraints → Constrain symmetrical
   SeeAlso:[Constraint Parallel](Sketcher_ConstrainParallel/pt-br.md)
---

# Sketcher ConstrainSymmetric/pt-br


</div>

## Description

The **Symmetrical Constraint** constrains two selected points to be symmetrical around a given line, i.e., both selected points are constrained to lie on a normal to the line through both points and are constrained to be equidistant from the line. Alternatively it can constrain two points to be symmetric with respect to a third one.

## Usage

<img alt="" src=images/SymmetricConstraint1.png  style="width:500px;">

Select two points (vertexes) in the sketch and a line in the sketch. The selected points and the line will be dark green.

<img alt="" src=images/SymmetricConstraint2.png  style="width:500px;">

Click on **[<img src=images/Sketcher_ConstrainSymmetric.svg style="width:16px"> [Constrain symmetric](Sketcher_ConstrainSymmetric.md)** or select the Constrain Symmetrical menu item from the Sketcher Constraints sub menu of the Sketcher (or Part Design) menu item.

This will apply the constraint to the selected items.

<img alt="" src=images/SymmetricConstraint3.png  style="width:500px;">


**Note:**

Before Version 0.19 (see fix [1](https://github.com/FreeCAD/FreeCAD/pull/3746)), if you want to define a symmetry constraint with respect to a point, the order of the selection is important, depending on if you select the tool at the beginning or at the end.

-   If you click the tool first: select the first point, then the symmetry reference point, and finally the second point.
-   If you click the tool last: select the first point, then the second point, and finally the symmetry reference point.

See the tracker [issue #4144](https://freecadweb.org/tracker/view.php?id=4144), and [forum thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=39611).

## Scripting

Two points and a symmetry line:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, SymmetryLine))```

Two points and a symmetry point:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, LineS, PointOfLineS))```

A line and a symmetry point (In the GUI one can select a line and a point, but it uses internally the same form as above, with the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line, 1, Line, 2, LineS, PointOfLineS))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line1`, `Line2`, `LineS`, `Line`, `PointOfLine1`, `PointOfLine2` and `PointOfLineS`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSymmetric/pt-br
