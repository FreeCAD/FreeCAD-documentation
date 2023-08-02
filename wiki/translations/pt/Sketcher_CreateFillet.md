# Sketcher CreateFillet/pt
---
- GuiCommand:   Name: Sketcher CreateFillet   Name/pt: Sketcher CreateFillet   Workbenches: Sketcher Workbench/pt   Sketcher|Shortcut: F   MenuLocation: Sketch -> Sketcher geometries -> Create fillet---


</div>

## Description

This tool creates a fillet between two lines.

When starting the tool, selections are cleared and the mouse pointer changes to a white cross with a red fillet icon. It stays active so you can do multiple fillets.

![](images/SketcherCreateFilletExample.png‎ )

## Usage

1.  Press the **[<img src=images/Sketcher_CreateFillet.svg style="width:16px"> [Create fillet](Sketcher_CreateFillet.md)** button.
2.  Pick a vertex connecting two non-parallel lines, or pick two lines that are not parallel.
3.  If a vertex is selected the fillet radius is derived from the length of the shortest line. If two lines are selected the radius is the distance from the first clicked point to the (extended) intersection of the lines.
4.  Pressing **Esc** or clicking the right mouse button cancels or terminates the function.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/pt
