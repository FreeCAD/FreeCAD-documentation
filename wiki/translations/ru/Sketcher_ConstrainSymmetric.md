---
 GuiCommand:
   Name/ru: Ограничение симметричности
   Name: Sketcher_ConstrainSymmetric
   MenuLocation: Sketch , Ограничения эскиза , Ограничение симметричности
   Workbenches: Sketcher_Workbench/ru
   Shortcut: S
   SeeAlso: Sketcher_ConstrainParallel/ru
---

# Sketcher ConstrainSymmetric/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

**Ограничение симметричности** требует от двух выделенных точек быть симметричными относительно данной линии, то есть от обеих точек требуется лежать на нормали к линии через обе точки на одинаковом расстоянии от линии. Альтернативно, она может наложить ограничение на две точки быть симметричными относительно третьей.


</div>



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> [Constrain symmetric](Sketcher_ConstrainSymmetric.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Constrain symmetric** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Constrain → <img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Constrain symmetric** option from the context menu.

    -   Use the keyboard shortcut: **S**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two points and a symmetry point (in that order).
    -   Select two points and a symmetry line (idem).
    -   Select a point, a symmetry line and another point (idem).
    -   Select a line and a symmetry point (idem).
5.  A constraint is added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Do one of the following:
    -   Select two points and a symmetry point (in that order).
    -   Select two points and a symmetry line (in any order).
    -   Select a line and a symmetry point (idem).
2.  Invoke the tool as explained above, or with the following additional option:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Constrain symmetric** option from the context menu.
3.  A constraint is added.

## Notes

-   The arrows of this constraint show the color of the dimensional constraints.



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



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSymmetric/ru
