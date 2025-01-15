---
 GuiCommand:
   Name/ru: Ограничение расстояния по горизонтали
   Name: Sketcher_ConstrainDistanceX
   MenuLocation: Sketch , Ограничения эскиза , Ограничение расстояния по горизонтали
   Workbenches: Sketcher_Workbench/ru
   Shortcut: **Shift** + **H**
   SeeAlso: Sketcher_ConstrainDistance/ru, Sketcher_ConstrainDistanceY/ru
---

# Sketcher ConstrainDistanceX/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Фиксирует горизонтальное расстояние между 2 точками или концами отрезка. Если выбрана только одна точка, расстояние устанавливается в точки центра координат эскиза.


</div>

![](images/Constraint_H_Distance.png )



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   
        <small>(v1.0)</small> 
        
        : If the **Dimensioning constraints** [preference](Sketcher_Preferences#General.md) is set to {{Value|Single tool}} (default): press the down arrow to the right of the **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button and select the **<img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Constrain horizontal distance** option from the dropdown.

    -   If this preference has a different value (and in {{VersionMinus|0.21}}): press the **<img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> [Constrain horizontal distance](Sketcher_ConstrainDistanceX.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Constrain horizontal distance** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Dimension → <img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Constrain horizontal distance** option from the context menu.

    -   Use the keyboard shortcut: **L**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two points (one of which can be the origin).
    -   Select a single line.
5.  If a [driving dimensional constraint](Sketcher_ToggleDrivingConstraint.md) is created, depending on the [preferences](Sketcher_Preferences#Display.md), a dialog opens to [edit its value](Sketcher_Workbench#Edit_constraints.md).
6.  A constraint is added.
7.  Optionally keep creating constraints.
8.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Do one of the following:
    -   Select one or two points.
    -   Select a single line.
2.  Invoke the tool as explained above.
3.  Optionally [edit the constraint value](Sketcher_Workbench#Edit_constraints.md).
4.  A constraint is added.



## Программирование

Расстояние от начала координат:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Расстояние между двумя вершинами:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Horizontal span of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, ` PointOfEdge1`, ` PointOfEdge2` and `Line`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceX/ru
