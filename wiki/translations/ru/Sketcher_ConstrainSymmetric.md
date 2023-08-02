---
- GuiCommand:
   Name/ru: Ограничение симметричности
   Name: Sketcher_ConstrainSymmetric
   MenuLocation: Sketch -> Ограничения эскиза -> Ограничение симметричности
   Workbenches: Sketcher_Workbench/ru
   Shortcut: S
   SeeAlso: Sketcher_ConstrainParallel/ru
---

# Sketcher ConstrainSymmetric/ru


</div>

## Описание

**Ограничение симметричности** требует от двух выделенных точек быть симметричными относительно данной линии, то есть от обеих точек требуется лежать на нормали к линии через обе точки на одинаковом расстоянии от линии. Альтернативно, она может наложить ограничение на две точки быть симметричными относительно третьей.

## Применение

<img alt="" src=images/SymmetricConstraint1.png  style="width:500px;">

Выделите в эскизе две точки (вершины) и линию. Выделенные точки и линия станут тёмно-зелёными.

<img alt="" src=images/SymmetricConstraint2.png  style="width:500px;">


<div class="mw-translate-fuzzy">

Кликните на иконке SymmetricalConstraint <img alt="" src=images/Constraint_Symmetric.png  style="width:16px;"> на панели инструментов Sketcher или выделите меню Constrain Symmetrical в субменю Sketcher Constraints в разделе меню Sketcher (или Part Design).


</div>

Это назначит ограничения для выделенных элементов.

<img alt="" src=images/SymmetricConstraint3.png  style="width:500px;">


**Note:**

Before Version 0.19 (see fix [1](https://github.com/FreeCAD/FreeCAD/pull/3746)), if you want to define a symmetry constraint with respect to a point, the order of the selection is important, depending on if you select the tool at the beginning or at the end.

-   If you click the tool first: select the first point, then the symmetry reference point, and finally the second point.
-   If you click the tool last: select the first point, then the second point, and finally the symmetry reference point.

See the tracker [issue #4144](https://freecadweb.org/tracker/view.php?id=4144), and [forum thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=39611).

## Программирование

Two points and a symmetry line:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, SymmetryLine))```

Two points and a symmetry point:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, LineS, PointOfLineS))```

A line and a symmetry point (In the GUI one can select a line and a point, but it uses internally the same form as above, with the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line, 1, Line, 2, LineS, PointOfLineS))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line1`, `Line2`, `LineS`, `Line`, `PointOfLine1`, `PointOfLine2` and `PointOfLineS`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSymmetric/ru
