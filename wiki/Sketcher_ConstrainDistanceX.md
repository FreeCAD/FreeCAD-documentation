---
- GuiCommand   *
   Name   *Sketcher ConstrainDistanceX
   MenuLocation   *Sketch → Sketcher constraints → Constrain horizontal distance
   Workbenches   *[Sketcher](Sketcher_Workbench.md)
   Shortcut   ***L**
   SeeAlso   *[Sketcher Constrain Length](Sketcher_ConstrainDistance.md), [Sketcher Constrain Vertical Distance](Sketcher_ConstrainDistanceY.md)
---

# Sketcher ConstrainDistanceX

## Description

Fixes the horizontal distance between 2 points or line ends. If only one point is selected, the distance is set to the sketch origin.

 ![](images/Constraint_H_Distance.png ) 

## Usage

1.  Pick one or two points or one line.
2.  Invoke the tool several ways   *
    -   Press the **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width   *16px"> [Constrain horizontal distance](Sketcher_ConstrainDistanceX.md)** button in the toolbar.
    -   Use the **L** keyboard shortcut.
    -   Use the **Sketch → Sketcher constraints → [<img src=images/Sketcher_ConstrainDistanceX.svg style="width   *16px"> Constrain horizontal distance** from the top menu.
3.  A pop up dialog opens to edit or confirm the value. Press **OK** to validate.

**Note   *** the constraint tool can also be started with no prior selection, but will require selection of two points or one line. To set the distance to the origin, the sketch origin point needs to be selected as well. By default the command will be in continue mode to create new constraints; press the right mouse button or **Esc** once to quit the command.

## Scripting

Distance from origin   *

 

Distance between two vertices   *

 

Horizontal span of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line)   *

 

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1`, `Edge2`, `Edge`, ` PointOfEdge1`, ` PointOfEdge2`, `PointOfEdge` and `Line`, and contains further examples on how to create constraints from Python scripts.




 {{Sketcher_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceX
