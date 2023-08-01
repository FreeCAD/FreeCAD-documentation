---
- GuiCommand:
   Name:Curves EditableSpline
   MenuLocation:Curves → Freehand BSpline
   Workbenches:[Curves](Curves_Workbench.md)
---

# Curves EditableSpline/pl

## Description

The <img alt="" src=images/Curves_EditableSpline.svg  style="width:24px;"> [Curves EditableSpline](Curves_EditableSpline.md) creates a freehand B-spline curve. This tool is part of the [external workbench](External_workbenches.md) called [Curves](Curves_Workbench.md).

## Usage

1.  Switch to the <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench.md) workbench (install from <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) is necessary, if not previously installed).
2.  Optionally select vertexes, edges and/or faces:
    -   The number of vertexes of the spline will match the number of selected elements.
    -   The spline vertexes will be snapped to the selected vertexes, and to the midpoints of the selected edges and faces.
3.  To invoke the command, do one of the following:
    -   Press the <img alt="" src=images/Curves_EditableSpline.svg  style="width:24px;"> button in the Curves toolbar.
    -   Use the **Curves → Freehand BSpline** entry in the dropdown menu.

## Options

During the command a special edit mode is active and there are several actions and behaviors that can be controlled by keys and mouse clicks.

-   To move a vertex or guide line (guide lines are the straight lines between vertexes) press and hold down the left mouse button on it, and move the mouse.
-   The **A** key selects or deselects all vertexes and guide lines.
-   The **I** key will add a vertex to the segment belonging to the selected guide line. The new vertex will be selected.
-   The **T** key sets or un-sets tangent mode for the selected vertexes or guide lines (relative to the view direction).
-   The **P** key aligns selected objects.
-   The **S** key can be used to snap a vertex to a vertex belonging to another B-spline. With a vertex of the B-spline being edited selected, hold down the **Ctrl** key and add the target vertex to the selection, then hit the **S** key. The vertexes are snapped together.
-   To unsnap vertexes, select the snapped vertex pair and again hit the **S** key. The vertex of the B-spline being edited remains selected and can now be moved.
-   The **L** key sets or un-sets the linear interpolation.
-   The **X**, **Y** or **Z** keys can be used to constrain the movement of the object being dragged. While dragging, hit the desired axis key. Hit the same key again to disable the constraint.
-   The **Q** key finishes the command and exits edit mode.

## Limitations

## Properties

## Scripting





{{Curves Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves EditableSpline/pl
