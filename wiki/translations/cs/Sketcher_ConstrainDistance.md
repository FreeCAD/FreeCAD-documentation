---
- GuiCommand:/cs
   Name:Sketcher ConstrainDistance
   Name/cs:Constraint Length
   Workbenches:[Sketcher](Sketcher_Workbench/cs.md)
   MenuLocation:Sketch → Vazby náčrtu → Vazba vzdálenosti
   Shortcut:Shift + D
   SeeAlso:[Constrain  horizontal distance](Sketcher_ConstrainDistanceX/cs.md), [Constrain vertical distance](Sketcher_ConstrainDistanceY/cs.md)
---

# Sketcher ConstrainDistance/cs


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Vazba Délka nastavuje délku přímky, kolmou vzdálenost mezi bodem a přímkou nebo vzdálenost mezi dvěma body.


</div>

![](images/Sketcher_ConstrainDistance_example.png )


<div class="mw-translate-fuzzy">

## Použití


</div>

1.  Pick two points or one line or one point and one line.
2.  Invoke the command several ways:
    -   Press the **[<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> [Constrain distance](Sketcher_ConstrainDistance.md)** button in the Sketcher toolbar.
    -   Use the **K** then **D** keyboard shortcut.
    -   Use the **Sketch → Sketcher constraints → [<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> Constrain distance** entry from the top menu.
3.  A pop up dialog opens to edit or confirm the value. Press **OK** to validate.

**Note:** the constraint tool can also be started with no prior selection. To set the perpendicular distance between a point and a line, the point needs to be selected first. By default the command will be in continue mode to create new constraints; press the right mouse button or **Esc** once to quit the command.

### Hint


<div class="mw-translate-fuzzy">

### Rada

Pokud uvažujete o její aplikaci, zamyslete se raději nad použitím vazeb [Horizontální vzdálenost](Sketcher_ConstrainDistanceX.md) nebo [vertikální vzdálenost](Sketcher_ConstrainDistanceY.md). Tyto vazby jsou robustnější a mají rychlejší výpočet než zde popisovaná vazba Délka.


</div>

## Scripting

Distance from origin:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, App.Units.Quantity('123.0 mm')))```

Distance between two vertices:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Length of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Distance from point (`Edge, PointOfEdge`) to nearest point on line (`Line`):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, Line, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1`, `Edge2`, `Edge`, `PointOfEdge1`, `PointOfEdge2`, `PointOfEdge` and `Line`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/cs
