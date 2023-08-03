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

This tool removes axes alignments (<img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [Horizontal](Sketcher_ConstrainHorizontal.md), <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [Vertical](Sketcher_ConstrainVertical.md) constraints) from the selected elements by trying to preserve the constraint relationship.

## Usage

1.  Select geometry with axes alignments, for example a [rectangle](Sketcher_CreateRectangle.md).
2.  Press the <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> **Remove axes alignment** toolbar button.

As result the (horizontal, vertical constraints) will be removed. In the example of a rectangle, it stays a rectangle but becomes rotatable.

<img alt="" src=images/SketcherRemoveAxesAlignmentStart.png  style="width:300px;"> 
*A selected rectangle with horizontal and vertical constraints.*

<img alt="" src=images/SketcherRemoveAxesAlignmentResult.png  style="width:300px;"> 
*The rectangle after the usage of Remove Axes Alignment.*





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RemoveAxesAlignment/en
