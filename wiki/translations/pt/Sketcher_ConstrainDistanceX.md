---
- GuiCommand:/pt
   Name:Sketcher ConstrainDistanceX
   Name/pt:Sketcher ConstrainDistanceX
   Workbenches:[Sketcher](Sketcher_Workbench/pt.md)
   MenuLocation:Sketch → Sketcher constraints → Constrain horizontal distance
   Shortcut:Shift + H
   SeeAlso:[Constraint Length](Sketcher_ConstrainDistance/pt.md), [Constraint VerticalDistance](Sketcher_ConstrainDistanceY/pt.md)
---


</div>

## Description

Fixes the horizontal distance between 2 points or line ends. If only one point is selected, the distance is set to the sketch origin.

![](images/Constraint_H_Distance.png )

## Usage

1.  Pick one or two points or one line.
2.  Invoke the tool several ways:
    -   Press the **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Constrain horizontal distance](Sketcher_ConstrainDistanceX.md)** button in the toolbar.
    -   Use the **Shift** + **H** keyboard shortcut. (**H** is for **H**orizontal)
    -   Use the {{MenuCommand|Sketch → Sketcher constraints → <img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> Constrain horizontal distance}} from the top menu.
3.  A pop up dialog opens to edit or confirm the value. Press **OK** to validate.

**Note:** the constraint tool can also be started with no prior selection, but will require selection of two points or one line. To set the distance to the origin, the sketch origin point needs to be selected as well. By default the command will be in continue mode to create new constraints; press the right mouse button or **Esc** once to quit the command.

## Scripting

Distance from origin:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, App.Units.Quantity('123.0 mm')))```

Distance between two vertices:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Horizontal span of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1`, `Edge2`, `Edge`, ` PointOfEdge1`, ` PointOfEdge2`, `PointOfEdge` and `Line`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}  
