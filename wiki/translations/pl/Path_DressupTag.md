---
- GuiCommand:
   Name:Path DressupTag
   MenuLocation:Path → Path Dressup → Tag
   Workbenches:[Path](Path_Workbench.md)
   SeeAlso:[Path DressupRampEntry](Path_DressupRampEntry.md), [Path DressupDogbone](Path_DressupDogbone.md), [Path DressupDragKnife](Path_DressupDragKnife.md)
---

# Path DressupTag/pl

## Description

Narzędzie <img alt="" src=images/Path_DressupTag.svg  style="width:24px;"> **Ulepszenie - pola mocujące** koryguje istniejącą ścieżkę *(zazwyczaj ścieżkę skrawania konturu 2D)*, aby pozostawić znaczniki, które utrzymują część w miejscu. Bez nich część *(która nie jest przymocowana do podstawy)* może w sposób niekontrolowany zostać wyrwana z maszyny podczas końcowego skrawania. Znaczniki są przeznaczone do odłamania ręcznie *(lub za pomocą dłuta)*, a następnie spiłowania na płasko w celu wykończenia części.

A video explanation of this feature is given at: <https://www.youtube.com/watch?v=JZ4prlR6sps>

## Usage

1.  Select a contour or profile path objects.
2.  Select the **Path → Path Dressup → <img src="images/Path_DressupTag.svg" width=16px> Tag** option from the menu.

## Options

-   **Angle** : Controls the angle of plunge and ascent when a tag is crated.
-   **Height** : Controls the height of the tag top from the bottom of the profile cut.
-   **Radius** : Radius of the fillet for the tag.
-   **Segmentation Factor** : Number of segments to approximate a rounded tag.
-   **Width** : Overall width of the tag.

Tags are automatically generated evenly spaced along the contour, beginning with the largest edge. You have the option to delete any you don\'t like or change their locations so that they appear on the convex parts of the job where it will be easier to file off the excess material.





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupTag/pl
