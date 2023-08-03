---
 GuiCommand:
   Name: Assembly3 ConstraintLengthDifference
   Icon: Assembly_ConstraintLengthDifference.svg
   Workbenches: Assembly3_Workbench
---

# Assembly3 ConstraintLengthDifference

## Description

This tool constrains the length of a 2D line like a non-subdivided wire made with the Draft workbench in relation with a work plane.

It links the length of the 2D line with the length of either another 2D line or a 3D line e.g. a straight edge element or a sketch line.

The length value of the first selected line equals the length value of the second line plus a difference value.

:   (Or the length value of the second selected line equals the length value of the first line minus a difference value.)

## Usage

1.  Select two lines, of which at least one should be a 2D line.
2.  Press the **<img src="images/Assembly_ConstraintLengthDifference.svg" width=16px> [Length difference](Assembly3_ConstraintLengthDifference.md)** button.
3.  Set the **Difference** value in the properties panel.
4.  Press the **<img src="images/Assembly3_workbench_icon.svg" width=16px> [Solve constraints](Assembly3_ResolveConstraints.md)** or the **<img src="images/Assembly_QuickSolve.svg" width=16px> [Quick solve](Assembly3_QuickSolve.md)** button to recompute

:   

    :   (if **<img src="images/Assembly_AutoRecompute.svg" width=16px> [Auto recompute](Assembly3_AutoRecompute.md)** and **<img src="images/Assembly_SmartRecompute.svg" width=16px> [Smart recompute](Assembly3_SmartRecompute.md)** are disabled).



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintLengthDifference
