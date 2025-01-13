---
 GuiCommand:
   Name: Sketcher ConstrainDistance
   Name/pt: Restringir distância
   Workbenches: Sketcher Workbench/pt
   MenuLocation: Sketch , Sketcher constraints , Constrain distance
   Shortcut: Shift + D
   SeeAlso: Sketcher ConstrainDistanceX/pt, Sketcher ConstrainDistanceY/pt
---

# Sketcher ConstrainDistance/pt


</div>

## Description

The <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> [Sketcher ConstrainDistance](Sketcher_ConstrainDistance.md) tool fixes the length of a line, the distance between two points, the perpendicular distance between a point and a line; or, <small>(v0.21)</small> , the distance between the edges of two circles or arcs, or between the edge of a circle or arc and a line; or, <small>(v1.0)</small> , the length of an arc.

![](images/Sketcher_ConstrainDistance_example.png )

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   
        <small>(v1.0)</small> 
        
        : If the **Dimensioning constraints** [preference](Sketcher_Preferences#General.md) is set to {{Value|Single tool}} (default): press the down arrow to the right of the **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button and select the **<img src="images/Sketcher_ConstrainDistance.svg" width=16px> Constrain distance** option from the dropdown.

    -   If this preference has a different value (and in {{VersionMinus|0.21}}): press the **<img src="images/Sketcher_ConstrainDistance.svg" width=16px> [Constrain distance](Sketcher_ConstrainDistance.md)** button.

    -   Select the **Sketch → Sketcher constraints → [<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> Constrain distance** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Dimension → <img src="images/Sketcher_ConstrainDistance.svg" width=16px> Constrain distance** option from the context menu.

    -   Use the keyboard shortcut **K** then **D**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select a single line.
    -   Select two points.
    -   Select a point and a line (in that order).
5.  If a [driving dimensional constraint](Sketcher_ToggleDrivingConstraint.md) is created, depending on the [preferences](Sketcher_Preferences#Display.md), a dialog opens to [edit its value](Sketcher_Workbench#Edit_constraints.md).
6.  A constraint is added.
7.  Optionally keep creating constraints.
8.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool

### Run-once mode 

1.  Do one of the following:
    -   Select a single line.

    -   Select two points.

    -   Select a point and a line (in any order).

    -   Select the edges of two circles or arcs.

    -   Select the edge of a circle or arc and a line (idem).

    -   
        <small>(v1.0)</small> 
        
        : Select the edge of a single arc.
2.  Invoke the tool as explained above.
3.  Optionally [edit the constraint value](Sketcher_Workbench#Edit_constraints.md).
4.  A constraint is added.

## Notes

-   If applicable please consider using [Horizontal distance](Sketcher_ConstrainDistanceX.md) or [Vertical distance](Sketcher_ConstrainDistanceY.md) constraints instead. They are more efficient.

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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/pt
