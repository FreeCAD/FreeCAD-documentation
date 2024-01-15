---
 GuiCommand:
   Name: Sketcher CreateRectangle
   MenuLocation: Sketch , Sketcher geometries , Create rectangle
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **R**
   SeeAlso: Sketcher_CreateOblong, Sketcher_CreatePolyline
---

# Sketcher CreateRectangle

## Description

This tool draws a rectangle by picking two opposite points. When starting the tool, the mouse pointer changes to a white cross with a red rectangle icon. The coordinates of the pointer are shown beside it in blue in real time.

To define a rectangle via a center point and an edge point, use the [Centered rectangle](Sketcher_CreateRectangle_Center.md) tool.

 ![](images/SketcherCreateRectangleExample.png‎ ) 

## Usage

-   After pressing the <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> **Create rectangle** toolbar button, click once to set the first corner, then move the mouse and click a second time to set the opposite corner.
-   Pressing **Esc** or clicking the right mouse button cancels the function.

## Notes

-   When launched the rectangle tools add a **Rectangle parameters** section at the top of the Sketcher [Task panel](Task_panel.md) (<small>(v0.22)</small> ). It contains:

1.  A **Mode** spinbox to chose one of the modes to draw the rectangle:
    -   Corner, length & width
    -   Center, length & width
    -   3 corners
    -   Center and two corners
2.  A **Rounded corners** checkbox to apply round corners to the rectangle.
3.  A **Frame** checkbox to add a contour with a constant offset to the (rounded) rectangle.

-   All three buttons in this selection now launch the same tool but with different preset combinations of mode and options that can still be altered after the first click.
-   If **Rounded corners** is enabled, the offset is inward, and the offset value is larger than the corner radius, the offset contour will be created without fillets.
-   The modes **3 corners**, and **Center and two corners** create parallelograms rather than rectangles.




 {{Sketcher_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRectangle
