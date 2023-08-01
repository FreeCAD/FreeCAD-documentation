---
- GuiCommand:
   Name:Sketcher Extend
   MenuLocation:Sketch - Sketcher geometries - Extend edge
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:**G** **Q**
   Version:0.17
   SeeAlso:[Sketcher Trim edge](Sketcher_Trimming.md)
---

# Sketcher Extend/pt-br

## Description

The **extend edge** tool extends an edge to an arbitrary location in the sketch, or to a target edge or point object.

<img alt="" src=images/Sketcher_Extend_example_01.png  style="width:600px;"> 
*Shown on the left (1), the two sketch elements before the operation; in the middle (2), the line is being extended to the arc; to the right (3), the final result.*

## Usage

1.  Press the **[<img src=images/Sketcher_Extend.svg style="width:16px"> [Extend edge](Sketcher_Extend.md)** button.
2.  Select a line or an arc.
3.  In the 3D view, move the mouse pointer toward the direction to extend.
4.  Click on an arbitrary location in space, or
5.  To extend to another edge, place the mouse pointer over the target edge; when it is highlighted and the **[<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> [Point on object](Sketcher_ConstrainPointOnObject.md)** constraint icon appears besides the mouse pointer, click to confirm. A point on object constraint will be added.
6.  To extend to a point in the sketch, place the mouse pointer over the target point; when it is highlighted and the **[<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> [Coincident constraint](Sketcher_ConstrainCoincident.md)** icon appears besides the mouse pointer, click to confirm. A coincident constraint will be added.

## Notes

-   Only arcs and lines can be extended at this time.
-   The target edge or point object may be modified as well if it is not fully constrained.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Extend/pt-br
