---
- GuiCommand:
   Name:Path DressupDragKnife
   MenuLocation:Path → Path Dressup → DragKnife Dressup
   Workbenches:[Path](Path_Workbench.md)
   SeeAlso:[Path DressupTag](Path_DressupTag.md), [Path DressupRampEntry](Path_DressupRampEntry.md), [Path DressupDogbone](Path_DressupDogbone.md)
---

# Path DressupDragKnife/en

## Description

A drag knife uses a cutting edge on a pivot to cut sheet material like vinyl, cardboard, and leather. The cutting point is not aligned with the center of the spindle but rather follows it as the spindle moves. Because the cutting point is offset, the path must be modified to extend past the endpoint of each segment. Also, the dragknife is incapable of making extremely tight turns. To compensate, a pivot \'corner action\' is inserted which momentarily lifts the blade slightly and then pivots into the new position.

This tool dresses up an existing path to add corner actions and edge extensions for drag knife cutting.

## Usage

1.  Select a contour or profile path [Path](Path_Workbench.md) objects
2.  click the <img alt="" src=images/Path_DressupDragKnife.svg  style="width:16px;"> [Dragknife Dress-up](Path_DressupDragKnife.md) menu item

## Options

-   Filter Angle - Determines how acute an angle must be before a corner action is inserted.
-   Offset - Input how much the blade point is offset from the spindle center.
-   Pivot Height - Determines how high to lift the cutting blade during a corner action. This is material dependent and should be higher for thicker materials. Ideally, the point should remain in the material slightly.





{{Path_Tools_navi

}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupDragKnife/en
