---
- GuiCommand:
   Name:Assembly3 MovePart
   Icon:Assembly_Move.svg
   MenuLocation:Assembly3 → Move part
   Workbenches:[Assembly3](Assembly3_Workbench.md)
   Shortcut:**A** then **M**
---

# Assembly3 MovePart/en

## Description

The <img alt="" src=images/Assembly_Move.svg‎‎  style="width:24px;"> [Move part](Assembly3_MovePart.md) command provides a tool to move a part within an assembly context.  It consists of 3 rings to rotate the part and 6 handles (crossed double arrows) to move the part without rotation.  The rings and handles are positioned and oriented according to the selected object\'s implicit coordinate system (ICS).

<img alt="" src=images/Assembly3_MovePart.png  style="width:400px;">

## Usage

1.  Select either a face, an edge, or a vertex of the 3D part or the whole part in the assembly tree.
2.  Activate the <img alt="" src=images/Assembly_Move.svg‎‎  style="width:16px;"> **Move part** command using one of the following:
    -   The **<img src="images/Assembly_Move.svg‎‎" width=16px> [Move part](Assembly3_MovePart.md)** button.
    -   The **Assembly3 → <img src="images/Assembly_Move.svg‎‎" width=16px> Move part** menu option.
    -   The keyboard shortcut: **A** then **M**.
3.  Drag the rings and handles to reposition the part.
4.  Press **Esc** to fix the position and leave the tool.

## Notes

The handles move the part parallel to one of the basic planes of the selected object\'s ICS; pressing and holding **shift** while dragging limits the movement to one axis.



---
![](images/Button_right.svg) [documentation index](../README.md) > Assembly3 MovePart/en
