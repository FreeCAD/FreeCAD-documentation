---
 GuiCommand:
   Name: Sketcher RemoveAxesAlignment
   MenuLocation: Sketch , Sketcher tools , Remove axes alignment
   Workbenches: Sketcher_Workbench
   Shortcut: **Z** **R**
   Version: 0.20
---

# Sketcher RemoveAxesAlignment/en

## Description

The <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> [Sketcher RemoveAxesAlignment](Sketcher_RemoveAxesAlignment.md) tool removes the axes alignment of selected edges by replacing [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) constraints with [Parallel](Sketcher_ConstrainParallel.md) and [Perpendicular](Sketcher_ConstrainPerpendicular.md) constraints. The edges can then be rotated without losing their orthogonal relationship.

## Usage

1.  Select two or more edges with Horizontal or Vertical constraints, for example a [rectangle](Sketcher_CreateRectangle.md).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_RemoveAxesAlignment.svg" width=16px> [Remove axes alignment](Sketcher_RemoveAxesAlignment.md)** button.
    -   Select the **Sketch → Sketcher tools → <img src="images/Sketcher_RemoveAxesAlignment.svg" width=16px> Remove axes alignment** option from the menu.
    -   Use the keyboard shortcut: **Z** then **R**.

## Example

<img alt="" src=images/SketcherRemoveAxesAlignmentStart.png  style="width:300px;"> 
*A selected rectangle with horizontal and vertical constraints.*

<img alt="" src=images/SketcherRemoveAxesAlignmentResult.png  style="width:300px;"> 
*The rectangle after using the tool.*



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RemoveAxesAlignment/en
