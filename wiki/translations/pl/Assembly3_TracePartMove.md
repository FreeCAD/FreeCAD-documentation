---
- GuiCommand:
   Name: Assembly3 TracePartMove
   Icon: Assembly_Trace.svg‎‎
   MenuLocation: Assembly3 - Trace part move
   Workbenches: [Assembly3](Assembly3_Workbench.md)
---

# Assembly3 TracePartMove/pl

## Description

The <img alt="" src=images/Assembly_Trace.svg  style="width:24px;"> [Trace part move](Assembly3_TracePartMove.md) command traces one single point of a kinematic assembly, when one of the assembled objects is moved with either the <img alt="" src=images/Assembly_Move.svg‎‎  style="width:16px;"> [Move part](Assembly3_MovePart.md) tool or the <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:16px;"> [Axial move](Assembly3_AxialMove.md) tool.

## Usage

1.  Optionally select a wire object:
    -   A point to trace itself.
    -   An edge or face to trace the center point of its shape.
2.  Activate the <img alt="" src=images/Assembly_Trace.svg  style="width:16px;"> **Trace part move** command using one of the following:
    -   The **<img src="images/Assembly_Trace.svg" width=16px> [Trace part move](Assembly3_TracePartMove.md)** button.
    -   The **Assembly3 → <img src="images/Assembly_Trace.svg" width=16px> Trace part move** menu option.
3.  Select one object of the assembly and move it using one of the following:
    -   The <img alt="" src=images/Assembly_Move.svg‎‎  style="width:16px;"> [Move part](Assembly3_MovePart.md) tool.
    -   The <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:16px;"> [Axial move](Assembly3_AxialMove.md) tool.
4.  Press the **esc** key or the **OK** button (Axial move only) to finish tracing.
5.  Find an AsmTrace object in the [Tree view](Tree_view.md).

## Notes

-   If you don\'t select any shape in the first step, you will be tracing the shape that was selected in the third step.
-   To change the element to trace, you need to disable this tool before selecting a new element and enabling it again.
-   If you control the movement with another tool such as this [kinematic controller](Tutorial_KinematicController.md) that allows to use a mover tool in parallel, you could use this tool to alter the assembly step by step and use the mover tool to add a point and connecting line on each step. It is possible to use the mover tool as a trigger by picking and dragging any of the arrows - just a tiny bit until the next point and line appears (use transparency if necessary).

:   (I hope there will be a more elegant way in the future)



---
⏵ [documentation index](../README.md) > Assembly3 TracePartMove/pl
