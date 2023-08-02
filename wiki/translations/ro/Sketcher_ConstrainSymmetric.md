---
- GuiCommand:
   Name: Sketcher ConstrainSymmetric
   Workbenches: Sketcher Workbench
   MenuLocation: Sketch -> Sketcher constraints -> Constrain symmetrical
   Shortcut: S
   SeeAlso: Sketcher ConstrainParallel
---

# Sketcher ConstrainSymmetric/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Constrângerea de simetrie obligă două puncte selectate pentru a deveni simetrice cu o anumită linie de simetrie, adică două puncte selectate sunt constrânse să stea pe o linie normală care trece prin cele două puncte și sunt constrânse să fie echidistan0te față de linia de simetrie. Alternativ, poate forța două puncte să fie simetrice față de al treilea.


</div>


<div class="mw-translate-fuzzy">

## Utilizare

<img alt="" src=images/SymmetricConstraint1.png  style="width:256px;">
Selectați două puncte (vârfuri) din schiță și o linie din schiță. Punctele selectate și linia vor fi verde închis.
<img alt="" src=images/SymmetricConstraint2.png  style="width:256px;">
Click pe iconița SymmetricalConstraint <img alt="" src=images/Constraint_Symmetric.png  style="width:16px;"> în bara de instrumente Sketcher sau selectați elementul de meniu Constrain Symmetrical din submeniul Sketcher Costraint din elementul de meniu Sketcher (sau Part Design). Aceasta va aplica constrângerea elementelor selectate.
<img alt="" src=images/SymmetricConstraint3.png  style="width:256px;">
Aceasta este o constrângere geometrică și nu are parametri editabili.


</div>

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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSymmetric/ro
