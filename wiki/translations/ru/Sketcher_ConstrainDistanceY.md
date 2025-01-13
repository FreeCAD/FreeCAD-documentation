---
 GuiCommand:
   Name/ru: Ограничение расстояния по вертикали
   Name: Sketcher_ConstrainDistanceY
   MenuLocation: Sketch , Ограничения эскиза , Ограничение расстояния по вертикали
   Workbenches: Sketcher_Workbench/ru
   Shortcut: **I**
   SeeAlso: Sketcher_ConstrainDistanceX/ru, Sketcher_ConstrainDistance/ru
---

# Sketcher ConstrainDistanceY/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Фиксирует вертикальное расстояние между 2 точками или концами отрезка. Если выбрана только одна точка, расстояние устанавливается в точки центра координат эскиза.


</div>

![](images/Sketcher_ConstraintDistanceY_example.png )



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   
        <small>(v1.0)</small> 
        
        : If the **Dimensioning constraints** [preference](Sketcher_Preferences#General.md) is set to {{Value|Single tool}} (default): press the down arrow to the right of the **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button and select the **<img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Constrain vertical distance** option from the dropdown.

    -   If this preference has a different value (and in {{VersionMinus|0.21}}): press the **<img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> [Constrain vertical distance](Sketcher_ConstrainDistanceY.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Constrain vertical distance** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Dimension → <img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Constrain vertical distance** option from the context menu.

    -   Use the keyboard shortcut: **I**.
3.  For further steps see [Sketcher ConstrainDistanceX](Sketcher_ConstrainDistanceX#Continue_mode.md)

### Run-once mode 

See [Sketcher ConstrainDistanceX](Sketcher_ConstrainDistanceX#Run-once_mode.md).



## Программирование

Расстояние от начала координат:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Расстояние между двумя вершинами:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Vertical span of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, ` PointOfEdge1`, ` PointOfEdge2` and `Line`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceY/ru
