---
- GuiCommand:
   Name: FEM PostFilterLinearizedStresses
   MenuLocation: Results -> Stress linearization plot
   Workbenches: FEM_Workbench
   SeeAlso: FEM_PostPipelineFromResult, FEM_PostFilterDataAlongLine, FEM_tutorial
---

# FEM PostFilterLinearizedStresses/pl

## Description

Creates a stress linearization plot.

To learn more about stress linearization plots, you can read [this description](https://www.graspengineering.com/what-is-stress-linearization/).

<img alt="" src=images/FEM_Stress-Linearization-Plot-Example.png  style="width:500px;">

*A stress linearization plot.*

## Usage

1.  Select a previously created [Line clip filter](FEM_PostFilterDataAlongLine.md).
2.  Invoke the command either by:
    -   Pressing the button **<img src="images/FEM_PostFilterLinearizedStresses.svg" width=16px> '''Stress linearization plot'''**.
    -   Using the menu **Results → <img src="images/FEM_PostFilterLinearizedStresses.svg" width=16px> Stress linearization plot**.
3.  An XY plot with linearized stress values (membrane, membrane+bending and total) along the line will be created in a separate window.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterLinearizedStresses/pl
