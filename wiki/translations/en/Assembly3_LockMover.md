---
- GuiCommand:
   Name:Assembly3 LockMover
   Icon:Assembly_LockMover.svg‎‎
   MenuLocation:Assembly3 → Lock mover
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 LockMover/en

## Description

The <img alt="" src=images/Assembly_LockMover.svg  style="width:24px;"> [Lock mover](Assembly3_LockMover.md) command is a toggle that prevents parts from being moved if they are fixed with a <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:16px;"> [Locked](Assembly3_ConstraintLock.md) constraint.

When activated, none of the mover commands <img alt="" src=images/Assembly_Move.svg‎‎  style="width:16px;"> [Move part](Assembly3_MovePart.md), <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:16px;"> [Axial move](Assembly3_AxialMove.md), or <img alt="" src=images/Assembly_QuickMove.svg‎‎  style="width:16px;"> [Quick move](Assembly3_QuickMove.md) can be selected as long as the current selection contains a fixed object. This seems not to apply to 2D geometry (see [Notes](#Notes.md)).

## Usage

1.  Activate the <img alt="" src=images/Assembly_LockMover.svg  style="width:16px;"> **Lock mover** command using one of the following:
    -   The **<img src="images/Assembly_LockMover.svg" width=16px> [Lock mover](Assembly3_LockMover.md)** button.
    -   The **Assembly3 → <img src="images/Assembly_LockMover.svg" width=16px> Lock mover** menu option.

## Notes

Selected **2D geometry**, such as Draft lines, arcs, and circles, fixed with the Locked constraint does not deactivate the mover tools. While circles and arcs still keep their position when a mover is applied to them, lines can be relocated and tilted.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 LockMover/en
