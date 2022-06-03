---
- GuiCommand   *
   Name   *Path DressupTag
   MenuLocation   *Path → Path Dressup → Tag Dressup
   Workbenches   *[Path](Path_Workbench.md)
   SeeAlso   *[Path DressupRampEntry](Path_DressupRampEntry.md), [Path DressupDogbone](Path_DressupDogbone.md), [Path DressupDragKnife](Path_DressupDragKnife.md)
---

# Path DressupTag/pt-br

## Description

This tool dresses up an existing path (usually a 2D contour cutting path) to leave tags that hold the part in place. Without them a part (which is not fixed to the base) is liable to fly off the machine uncontrollably as the final cut is made. The tags are intended to be broken off by hand (or using a chisel) and then filed flat to finish the part.

A video explanation of this feature is given at   * <https   *//www.youtube.com/watch?v=JZ4prlR6sps>

## Usage

1.  Select a contour or profile path [Path](Path_Workbench.md) objects
2.  Click the <img alt="" src=images/Path_DressupTag.svg  style="width   *16px;"> [Tag Dress-up](Path_DressupTag.md) menu item

## Options

-   Angle - Controls the angle of plunge and ascent when a tag is crated.
-   Height - Controls the height of the tag top from the bottom of the profile cut.
-   Radius - Radius of the fillet for the tag.
-   Segmentation Factor - Number of segments to approximate a rounded tag
-   Width - Overall width of the tag

Tags are automatically generated evenly spaced along the contour, beginning with the largest edge. You have the option to delete any you don\'t like or change their locations so that they appear on the convex parts of the job where it will be easier to file off the excess material.





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupTag/pt-br
