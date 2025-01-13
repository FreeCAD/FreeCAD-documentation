---
 GuiCommand:
   Name: CAM Simulator
   MenuLocation: CAM , CAM Simulator
   Workbenches: CAM_Workbench
   Shortcut: **P** **M**
   SeeAlso: CAM_Inspect
---

# CAM Simulator/en

## Description

The <img alt="" src=images/CAM_Simulator.svg  style="width:24px;"> [Simulator](CAM_Simulator.md) tool allows Simulation of the CAM Job by sweeping 3D Models of the Tools used in each Operation, along the G-Code paths, subtracting material from the Stock, where the stock and tool overlap, providing visualization of the Job. This allows detection and isolation of errors prior to running the Job on a mill.

![](images/Path-Simulation.gif )

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/CAM_Simulator.svg" width=16px> [CAM Simulator](CAM_Simulator.md)** button.
    -   Select the **CAM → <img src="images/CAM_Simulator.svg" width=16px> CAM Simulator** option from the menu.
    -   Use the keyboard shortcut: **P** then **M**.
2.  De-select any **Operations** that are not to be simulated
3.  Tune the **Speed** and **Accuracy** settings.
4.  Select the **Job** for simulation from the drop menu.
5.  Use the **Path Simulator** toolbar to invoke different actions:
    -   Press the <img alt="" src=images/CAM_BPlay.svg  style="width:24px;"> (Play) button to play or playback an animation of the operations.
    -   Press the <img alt="" src=images/CAM_BFastForward.svg  style="width:24px;"> (Fast Forward) button to increase the speed substantially (in order to quickly review complicated paths).
    -   Press the <img alt="" src=images/CAM_BPause.svg  style="width:24px;"> (Pause) button to pause animation for troubleshooting purposes
    -   Press the <img alt="" src=images/CAM_BStep.svg  style="width:24px;"> (Single-Step) button for slowing down the animation, this functionality helps troubleshooting and resolving specific cuts and/or movements.
    -   Press the <img alt="" src=images/CAM_BStop.svg  style="width:24px;"> (Stop) button to stop the animation.
6.  Press the **Cancel** button will remove the stock created for the simulation. If you press **OK** this object will be kept in your Job.

## Properties

-    **Playback Speed**: The speed of the simulation playback, in G-code lines/second

-    **Accuracy**: The accuracy of the simulation expressed as a percentage indicating the simulations deviation from the Job. For interactive simulation, reducing accuracy to 0.3 works much faster.

-    **Job**: The Job used as the basis of the simulation

-    **Operation List**: The list of Operations selected for inclusion in the simulation.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Simulator/en
