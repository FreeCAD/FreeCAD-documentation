---
- GuiCommand:
   Name:Sketcher CreateLine
   MenuLocation:Sketch - Sketcher geometries - Create line
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:**G** **L**
   SeeAlso:[Sketcher Polyline](Sketcher_CreatePolyline.md)
---

# Sketcher CreateLine/hr

## Description

This tool draws a line by picking two points in the [3D view](3D_view.md). When starting the tool, the mouse pointer changes to a white cross with a red line icon. Besides are coordinates shown in real time.

![](images/Sketcher_LineExample1.png‎ )

The created line object starts and ends at the given points, but the line is infinite regarding the constraints [Tangent](Sketcher_ConstrainTangent.md), [Point On Object](Sketcher_ConstrainPointOnObject.md) and [Internal Angle](Sketcher_ConstrainAngle.md). This means for example, that a point with the constraint [Point On Object](Sketcher_ConstrainPointOnObject.md) may not be located between the two given points but can lie outside of the two points on the extension of the drawn line.

## Usage

-   Pick points on an empty area of the 3d view, or on an existing object (auto constraints must be active in [Task panel](Task_panel.md)).
-   Pressing **Esc** or clicking the right mouse button cancels the function.





{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/hr
