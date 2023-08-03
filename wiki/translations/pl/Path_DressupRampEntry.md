---
 GuiCommand:
   Name: Path DressupRampEntry
   MenuLocation: Path , Path Dressup , RampEntry
   Workbenches: Path_Workbench
   SeeAlso: Path_DressupTag, Path_DressupDogbone, Path_DressupDragKnife
---

# Path DressupRampEntry/pl

## Description

The tool <img alt="" src=images/Path_DressupRampEntry.svg  style="width:24px;"> [DressupRampEntry](Path_DressupRampEntry.md) dresses up an existing path to add a ramp entry.

## Usage

1.  Select a contour or profile path objects.
2.  Select the **Path → Path Dressup → <img src="images/Path_DressupRampEntry.svg" width=16px> RampEntry** option from the menu.

## Properties

-   **Ramp Feed Rate** : Can either be the current vertical or horizontal feed rate or some other custom value
-   **Angle** : Angle of the ramp against the vertical axis. A smaller value makes the ramp steeper.
-   **Method** : Used to select different modes of ramping:
    -   *RampMethod1*: goes down at the ramp angle and the moves horizontal to the target point
    -   *RampMethod2*: goes horizontal first and then down at the ramp angle to the target point
    -   *RampMethod3*: goes down in a zigzag way
    -   *Helix*: goes down spiraling
-   **Dressup Start Depth** : The distance above the target level where ramping starts
-   **Use Start Depth** : Indicates that the ramping does not start above the stock level. If it is not set to true the first ramp can be steeper than expected.

<img alt="" src=images/Ramp_method_1.png  style="width:" height="250px;"> <img alt="" src=images/Ramp_method_2.png  style="width:" height="250px;"> <img alt="" src=images/Ramp_method_3.png  style="width:" height="250px;"> 
*From left to right: Ramp method 1, 2 and 3*

<img alt="" src=images/Ramp_method_Helix.png  style="width:" height="250px;"> 
*Ramp method Helix*





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupRampEntry/pl
