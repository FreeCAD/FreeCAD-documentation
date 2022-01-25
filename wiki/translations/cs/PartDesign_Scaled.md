# PartDesign Scaled/cs
---
- GuiCommand:/cs   Name:PartDesign_Scaled   Name/cs:PartDesign Scaled   Workbenches:[[PartDesign Workbench/cs   PartDesign]], Complete|MenuLocation:PartDesign → MultiTransform---


</div>

## Introduction

\'Scale features\' - This tool takes a set of one or more selected features as its input (the \'originals\'), and scales them by a given factor. Since the scaling takes place around the centre of gravity of the selected features, they usually disappear inside the scaled versions. Therefore, normally it is only useful to use scaling as part of the MultiTransform feature.

Starting from FreeCAD 0.15, this operation is not available directly, but was incorporated into the [MultiTransform](PartDesign_MultiTransform.md) tool.

## Options

+++
| ![](images/Scaled_parameters.png ) | When creating a scaled feature, the \'scaled parameters\' dialogue offers the following options:                                             |
|                                                    |                                                                                                                                              |
|                                                    | ### Select originals                                                                                                      |
|                                                    |                                                                                                                                              |
|                                                    | The list view shows the \'originals\', the features that are to be scaled. Clicking on any feature will add it to the list.                  |
|                                                    |                                                                                                                                              |
|                                                    | ### Factor and Occurrences                                                                                          |
|                                                    |                                                                                                                                              |
|                                                    | Specifies the maximum factor which the features are to be scaled to, and the total number of scaled shapes (including the original feature). |
+++




## Limitations

-   Scaling always happens with the centre of gravity of the feature as the base point.
-   A scaled transformation should not be the first in the list
-   The scaled transformation must have the same number of occurrences as the transformation immediately preceding it in the list
-   See [linear pattern feature](PartDesign_LinearPattern.md) for other limitations
-   See [MultiTransform](PartDesign_MultiTransform.md) for more details

## Examples

![c\|center\|800px](images/mt_example2.png ) The smallest pad was first patterned three times in X direction and then scaled to factor two (so the three occurrences have scaling factor 1.0, 1.5 and 2.0). Then a polar pattern was applied with 8 occurrences.

Since the scaling is done with respect to the center of gravity, in the case of a pad, it is necessary that the pad penetrate also in the main body, otherwise the scaled objects are floating, detached from the body. To have a pad that intersects the main body can be used \"two dimensions\" type or \"simmetric to plane\" option.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Scaled/cs
