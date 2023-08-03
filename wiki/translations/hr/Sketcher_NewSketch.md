---
 GuiCommand:
   Name: Sketcher NewSketch
   MenuLocation: Sketch , Create sketch
   Workbenches: Sketcher_Workbench
   SeeAlso: PartDesign_NewSketch, Sketcher_MapSketch, Sketcher_ReorientSketch
---

# Sketcher NewSketch/hr

## Description

This will create a new [sketch](Sketcher_Workbench.md).

Note that the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md) has its own [new sketch](PartDesign_NewSketch.md) tool, when working on a [PartDesign body](PartDesign_Body.md) it is preferable to use that tool.

## Usage

Clicking on the icon without a face (pre-)selected will pop up a dialog asking if the sketch should be drawn on the

-   XY-Plane
-   XZ-Plane
-   YZ-Plane

You can change an offset to any of the three planes and the side of the offset.

Clicking on the icon with a (pre-selected) face will cause the sketch to be mapped to the selected face.

## Note

The sketch can be re-mapped to another already existing face using the [Sketcher MapSketch](Sketcher_MapSketch.md) command.

The sketch can be moved in the [3D view](3D_view.md) using [Placement](Placement.md).





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher NewSketch/hr
