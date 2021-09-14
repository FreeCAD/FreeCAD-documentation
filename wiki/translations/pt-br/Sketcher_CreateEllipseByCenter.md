---
- GuiCommand:
   Name:Sketcher CreateEllipseByCenter
   MenuLocation:Sketch → Sketcher geometries → Create ellipse by center
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Version:0.15
   SeeAlso:[Sketcher Ellipse by 3 Points](Sketcher_CreateEllipseBy3Points.md), [Sketcher Circle](Sketcher_CreateCircle.md), [Sketcher Arc of Ellipse](Sketcher_CreateArcOfEllipse.md)
---

## Description

This tool draws an ellipse by picking three points: the center, the end of major radius, the minor radius. When starting the tool, the mouse pointer changes to a white cross with a red ellipse icon. Besides are coordinates shown in real time.

<img alt="" src=images/Sketcher_EllipseExample1.png‎  style="width:500px;">


*The sequence of clicks is indicated by yellow arrows with numbers. C is the center, a - major diameter, b - minor diameter, F1, F2 are foci.*

## Usage

-   Invoke the command by clicking a toolbar button, picking the menu item, or by using keyboard shortcut (needs to be assigned first in [Interface Customization](Interface_Customization.md)).
-   First click in 3D view sets ellipse center. Second click sets the first radius and orientation of the ellipse. Third click sets the other radius (the distance from the line defined by first two clicks is the second radius).
-   After the third click, the ellipse is created, together with a set of construction geometry aligned to it (major diameter, minor diameter, two foci). The construction geometry can be manually deleted if not needed, and recreated later. See [Internal Alignment Constraint](Sketcher_ConstrainInternalAlignment.md) and [Sketcher Show Hide Internal Geometry](Sketcher_RestoreInternalAlignmentGeometry.md).
-   Pressing **ESC** or clicking the right mouse button cancels the function.

## Peculiarities

-   Major and minor axes of ellipses are strict and cannot be swapped by resizing the ellipse. This is a consequence of the solver parametrization used (center (x,y), focus1 (x,y) and minor radius length (b)) and the same strict behavior of OpenCascade. The ellipse must be rotated to swap the axes.
-   Ellipse can function as a circle when its major and minor diameter lines are deleted, and one of the foci is constrained to coincide with the center. But radius constraint won\'t work on such a circle.
-   Moving the ellipse by edge is the same as moving ellipse\'s center.





{{Sketcher Tools navi

}} 
