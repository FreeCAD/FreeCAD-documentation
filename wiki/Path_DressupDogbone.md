---
- GuiCommand:
   Name: Path DressupDogbone
   MenuLocation: Path -> Path Dressup -> Dogbone
   Workbenches: Path_Workbench
   SeeAlso: Path_DressupTag, Path_DressupRampEntry, Path_DressupDragKnife 
---

# Path DressupDogbone

## Description

The tool <img alt="" src=images/Path_DressupDogbone.svg  style="width:24px;"> [DressupDogbone](Path_DressupDogbone.md) dresses up an existing path to overcut corners on inside angles of a profile or contour operation. A cylindrical cutter cannot cut all the way into an acute corner without colliding with the model. In certain cases, it may be preferable to violate the model and ensure that the material at the corner is removed. This is especially necessary if parts are going to intersect/interlock with each other.

## Usage

1.  Select a contour or profile path [Path](Path_Workbench.md) objects.
2.  Select the **Path → Path Dressup → <img src="images/Path_DressupDogbone.svg" width=16px> Dogbone** option from the menu.

## Options

-   **Side** : Which side of the path the modification will be added to.
-   **Style** : Style of overcut (Dogbone, T-Bone Horizontal, T-Bone Vertical, T-Bone Long Edge, T-Bone Short Edge).
-   **Incision** : The Algorithm to use calculating the overcut length
-   **Custom** : If Incision is custom, the custom property is used to set the length.

## Limitations

The dogbone dressup needs a straight path segment (G1) before and after the corner where the dressup should be inserted.




 {{Path_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupDogbone
