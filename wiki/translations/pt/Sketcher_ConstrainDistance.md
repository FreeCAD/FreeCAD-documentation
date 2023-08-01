---
- GuiCommand:/pt
   Name:Sketcher ConstrainDistance
   Name/pt:Restringir distância
   Workbenches:[Sketcher](Sketcher_Workbench/pt.md)
   MenuLocation:Sketch → Sketcher constraints → Constrain distance
   Shortcut:Shift + D
   SeeAlso:[Constraint HorizontalDistance](Sketcher_ConstrainDistanceX/pt.md), [Constraint VerticalDistance](Sketcher_ConstrainDistanceY/pt.md)
---

# Sketcher ConstrainDistance/pt


</div>

## Description

**Constrain distance** defines the length of a line, the perpendicular distance between a point and a line, the distance between two points, or, <small>(v0.21)</small> , the distance between the edges of two circles or between the edge of a circle and a line.

![](images/Sketcher_ConstrainDistance_example.png )

## Usage

1.  Pick one line, or one point and one line, or two points, or the edges of two circles, or the edge of one circle and one line.
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> [Constrain distance](Sketcher_ConstrainDistance.md)** button in the Sketcher toolbar.
    -   Use the **K** then **D** keyboard shortcut.
    -   Use the **Sketch → Sketcher constraints → [<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> Constrain distance** entry from the top menu.
3.  A pop up dialog opens to edit or confirm the value. Press **OK** to validate.

**Note:** the constraint tool can also be started with no prior selection (apart from circle to circle and circle to line cases). To set the perpendicular distance between a point and a line, the point needs to be selected first. By default the command will be in continue mode to create new constraints; press the right mouse button or **Esc** once to quit the command.

### Hint

If applicable please consider using the **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Horizontal distance](Sketcher_ConstrainDistanceX.md)** or **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Vertical distance](Sketcher_ConstrainDistanceY.md)** constraints instead. These constraints are more robust and faster to calculate than the **ConstrainDistance** tool.

## Scripting

Distance from origin:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distance between two vertices:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Length of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Distance from point (`Edge, PointOfEdge`) to perpendicular point on line (`Line`):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, Line, 0, App.Units.Quantity('123.0 mm')))```

Distance between the edges of two circles:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Circle1, 0, Circle2, 0, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, `PointOfEdge1`, `PointOfEdge2`, `Line`, `Circle1` and `Circle2`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/pt
