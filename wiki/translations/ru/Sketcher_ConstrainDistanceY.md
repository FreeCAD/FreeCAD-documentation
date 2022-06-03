---
- GuiCommand   */ru
   Name/ru   *Ограничение расстояния по вертикали
   Name   *Sketcher_ConstrainDistanceY
   MenuLocation   *Sketch → Ограничения эскиза → Ограничение расстояния по вертикали
   Workbenches   *[Sketcher](Sketcher_Workbench/ru.md)
   Shortcut   ***Shift** + **V**
   SeeAlso   *[Ограничение расстояния по горизонтали](Sketcher_ConstrainDistanceX/ru.md), [Ограничить расстояние](Sketcher_ConstrainDistance/ru.md)
---

# Sketcher ConstrainDistanceY/ru


</div>

## Описание

Fixes the vertical distance between 2 points or line ends. If only one point is selected, the distance is set to the sketch origin.

![](images/Sketcher_ConstraintDistanceY_example.png )

## Применение

1.  Pick one or two points or one line.
2.  Invoke the command several ways   *
    -   Press the **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width   *16px"> [Constrain vertical distance](Sketcher_ConstrainDistanceY.md)** button.
    -   Use the **I** keyboard shortcut.
    -   Use the **Sketch → Sketcher constraints → [<img src=images/Sketcher_ConstrainDistanceY.svg style="width   *16px"> Constrain vertical distance** entry from the top menu.
3.  A pop up dialog opens to edit or confirm the value. Press **OK** to validate.

**Note   *** the constraint tool can also be started with no prior selection, but will require selection of two points or one line. To set the distance to the origin, the sketch origin point needs to be selected as well. By default the command will be in continue mode to create new constraints; press the right mouse button or **Esc** once to quit the command.

## Программирование

Distance from origin   *


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge, PointOfEdge, App.Units.Quantity('123.0 mm')))```

Дистанция между двумя вершинами   *


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Vertical span of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line)   *


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1`, `Edge2`, `Edge`, ` PointOfEdge1`, ` PointOfEdge2`, `PointOfEdge` and `Line`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceY/ru
