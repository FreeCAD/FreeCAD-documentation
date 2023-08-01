---
- GuiCommand:
   Name:Sketcher Split
   MenuLocation:Sketch - Sketcher geometries - Split edge
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:**G** **Z**
   Version:0.20
   SeeAlso:[Sketcher Trimming](Sketcher_Trimming.md)
---

# Sketcher Split/en

## Description

This tool splits an edge into two, with existing applicable constraints being copied to the new edge. The position of the point where the edges meet is not constrained. Periodic curves (i.e. circles, ellipses and periodic B-splines) are converted to non-periodic curves (respectively arcs of circles, arcs of ellipses and non-periodic B-splines).

![](images/SketcherSplitExample1.png ) ![](images/SketcherSplitExample2.png ) ![](images/SketcherSplitExample3.png )

## Usage

1.  Press the **[<img src=images/Sketcher_Split.svg style="width:16px"> [Split edge](Sketcher_Split.md)** button. The mouse pointer turns into a white cross with a red split symbol.
2.  Click on the edge in the place where you want to split it.
3.  From the line and arc edges, two new will be created, connected at the point clicked. A circle is converted to an arc with the very same center point and other constraints the original circle had.
4.  Pressing **Esc** or pressing the right mouse button will terminate the function.

## Limitations

-   In {{VersionMinus|0.20}} the action is not supported for ellipses, parabolas, hyperbolas and B-splines.

## Notes

-   All coincidences are transferred - start point, end point and center point (if applicable).
-   Point on object constraint is transferred to the closer newly created edge.
-   Vertical and horizontal constraints are copied to both offsprings.
-   Parallel and perpendicular constraints are copied for both line segments, for arc only once, to the closer part.
-   Equality constraint is transferred only for resulting arc edges, line segments do not receive it.
-   Symmetry constraint is currently not transferred.
-   Block constraint is currently not transferred.
-   Horizontal, vertical and length constraints between points are transferred to the outer points of the new edges.
-   Point distance constraint is assigned only once, to the closer edge segment.
-   Radius and diameter constraints are copied to any resulting arc.
-   Angle constraint is currently not transferred





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Split/en
