---
- GuiCommand:
   Name: Path Simulator
   MenuLocation: Path -> CAM Simulator
   Workbenches: Path_Workbench
   Shortcut: **P** **M**
   SeeAlso: Path_Inspect
---

# Path Simulator/de



## Beschreibung

The <img alt="" src=images/Path_Simulator.svg  style="width:24px;"> [Simulator](Path_Simulator.md) tool allows Simulation of the Path Job by sweeping 3D Models of the Tools used in each Operation, along the G-Code paths, subtracting material from the Stock, where the stock and tool overlap, providing visualization of the Job. This allows detection and isolation of errors prior to running the Job on a mill.

![](images/Path-Simulation.gif )

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Path_Simulator.svg" width=16px> [Path Simulator](Path_Simulator.md)** button.
    -   Select the **Path → <img src="images/Path_Simulator.svg" width=16px> CAM Simulator** option from the menu.
    -   Use the keyboard shortcut: **P** then **M**.
2.  De-select any **Operations** that are not to be simulated
3.  Tune the **Speed** and **Accuracy** settings.
4.  Select the **Job** for simulation from the drop menu.
5.  Use the **Path Simulator** toolbar to invoke different actions:
    -   Press the <img alt="" src=images/Path_BPlay.svg  style="width:24px;"> (Play) button to play or playback an animation of the operations.
    -   Press the <img alt="" src=images/Path_BFastForward.svg  style="width:24px;"> (Fast Forward) button to increase the speed substantially (in order to quickly review complicated paths).
    -   Press the <img alt="" src=images/Path_BPause.svg  style="width:24px;"> (Pause) button to pause animation for troubleshooting purposes
    -   Press the <img alt="" src=images/Path_BStep.svg  style="width:24px;"> (Single-Step) button for slowing down the animation, this functionality helps troubleshooting and resolving specific cuts and/or movements.
    -   Press the <img alt="" src=images/Path_BStop.svg  style="width:24px;"> (Stop) button to stop the animation.
6.  Press the **Cancel** button will remove the stock created for the simulation. If you press **OK** this object will be kept in your Job.

## Properties

-    **Playback Speed**: The speed of the simulation playback, in G-code lines/second

-    **Accuracy**: The accuracy of the simulation expressed as a percentage indicating the simulations deviation from the Job. For interactive simulation, reducing accuracy to 0.3 works much faster.

-    **Job**: The Job used as the basis of the simulation

-    **Operation List**: The list of Operations selected for inclusion in the simulation.





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Simulator/de
