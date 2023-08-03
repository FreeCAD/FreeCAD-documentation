# Sketcher CreatePolyline/pt
---
 GuiCommand:   Name: Sketcher CreatePolyline   Name/pt: Sketcher CreatePolyline   Workbenches: Sketcher Workbench/pt   Sketcher---


</div>



## Descrição

This tool works like the [Sketcher Line](Sketcher_CreateLine.md) tool, but creates continuous line and arc segments connected by their vertices. When starting the tool, the mouse pointer changes to a white cross with a red polyline icon. The coordinates of the pointer are shown beside it in blue in real time.

![](images/Sketcher_PolylineExample1.png )



*Polyline started with a line, a tangent arc, a perpendicular arc then a tangent line.*

## Usage

The polyline always starts with a straight line segment: click - move the mouse - click. Move the mouse again. After placing the first line segment, the Sketcher polyline tool has multiple modes that can be toggled with the **M** key. For example you can draw tangent or perpendicular arcs following a line or arc segment. Repeatedly pressing the **M** key toggles through these different modes:

1.  Press the **M** key: the new segment is a line which is perpendicular to the previous segment.
2.  Press the **M** key again: the new segment is a line which is tangential to the previous segment.
3.  Press the **M** key again: the new segment is an arc which is tangential to the previous segment.
4.  Press the **M** key again: the new segment is an arc which is perpendicular (left) to the previous segment.
5.  Press the **M** key again: the new segment is an arc which is perpendicular(right) to the previous segment.
6.  Press the **M** key again: You are again in the state where you started; the line is only connected with a coincidence to the previous segment.

-    <small>(v0.18)</small> While in any of the arc modes, holding down the **Ctrl** key (MacOS: **CMD** key) and moving the cursor causes the arc to snap by increments of 45 degrees, relative to the previously created polyline segment.

-   Pick points on an empty area of the 3D view, or on an existing object (auto constraints must be active in TaskView).

-   Pressing **Esc** or clicking the right mouse button *before* closing the polyline to a loop ends the current polyline and you can continue with a new one. Pressing **Esc** or clicking the right mouse button again ends the polyline function.

-   Pressing **Esc** or clicking the right mouse button *after* closing the polyline to a loop ends the polyline function.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePolyline/pt
