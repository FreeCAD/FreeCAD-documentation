---
- GuiCommand:
   Name:Sketcher CreateArcOfEllipse
   MenuLocation:Sketch - Sketcher geometries - Create arc of ellipse
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:**G** **E** **A**
   Version:0.15
   SeeAlso:[Sketcher Ellipse by center](Sketcher_CreateEllipseByCenter.md), [Sketcher Arc](Sketcher_CompCreateArc.md)
---

# Sketcher CreateArcOfEllipse

## Description

This tool draws an arc of ellipse by picking four points: the center, the end of major radius, the start point and the end point. When starting the tool, the mouse pointer changes to a white cross with a red ellipse arc icon. Besides are coordinates shown in real time.

 <img alt="" src=images/Sketcher_ArcOfEllipseExample1.png‎  style="width:500px;">  
*The sequence of clicks is indicated by yellow arrows with numbers.<br>
C is the center, a the major diameter, b the minor diameter, F1 and F2 are foci.*

## Usage

-   Press the **[<img src=images/Sketcher_CreateArcOfEllipse.svg style="width:16px"> [Create arc of ellipse](Sketcher_CreateArcOfEllipse.md)** button.
-   First click in 3D view sets ellipse center. Second click sets the first radius and orientation of the ellipse. Third click sets the other radius and the start of the arc. The fourth click sets the end of the arc.
-   After the fourth click, the arc of ellipse is created, together with a set of construction geometry aligned to it (major diameter, minor diameter, two foci). The construction geometry can be manually deleted if not needed, and recreated later. See [Sketcher Show Hide Internal Geometry](Sketcher_RestoreInternalAlignmentGeometry.md).
-   Pressing **ESC** or clicking the right mouse button cancels the function.

## Peculiarities

-   Major and minor axes of underlying ellipse are strict and cannot be swapped by resizing. The underlying ellipse must be rotated to swap the axes.
-   Unlike ellipse that can be constrained to become a circle, ellipse arc cannot represent an arc of circle.
-   Moving the arc of ellipse by edge is the same as moving ellipse\'s center.




 {{Sketcher Tools navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse
