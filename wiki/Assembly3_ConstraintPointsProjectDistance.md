---
- GuiCommand:
   Name:Assembly3 ConstraintPointsProjectDistance
   Icon:Assembly_ConstraintPointsProjectDistance.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintPointsProjectDistance

## Description

The <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg  style="width:16px;"> [Points project distance](Assembly3_ConstraintPointsProjectDistance.md) command constrains the distance of two 2D points in relation to a Straight line.

Based on the line\'s direction (the z axis of its implicit coordinate system (ICS)) setting the distance of two points along the line means to add the distance value to the first point\'s z value to receive the second point\'s z value (and ignoring the x and y values).

## Usage

1.  Select two points (2D or 3D).
2.  Select a straight line (2D or 3D).
3.  Activate the <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg  style="width:16px;"> [Points project distance](Assembly3_ConstraintPointsProjectDistance.md) command using the:
    -   
        **<img src="images/Assembly_ConstraintPointsProjectDistance.svg" width=16px> [Points project distance](Assembly3_ConstraintPointsProjectDistance.md)
**
        
        button.
4.  Press the **<img src="images/Assembly3_workbench_icon.svg" width=16px> [Solve constraints](Assembly3_ResolveConstraints.md)** or the **<img src="images/Assembly_QuickSolve.svg" width=16px> [Quick solve](Assembly3_QuickSolve.md)** button to recompute

:   

    :   (if **<img src="images/Assembly_AutoRecompute.svg" width=16px> [Auto recompute](Assembly3_AutoRecompute.md)** and **<img src="images/Assembly_SmartRecompute.svg" width=16px> [Smart recompute](Assembly3_SmartRecompute.md)** are disabled).

---
[documentation index](../README.md) > Assembly3 ConstraintPointsProjectDistance
