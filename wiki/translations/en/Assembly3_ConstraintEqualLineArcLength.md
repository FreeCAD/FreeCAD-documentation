---
- GuiCommand:
   Name:Assembly3 ConstraintEqualLineArcLength
   Icon:Assembly_ConstraintEqualLineArcLength.svg
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 ConstraintEqualLineArcLength/en

## Description

The <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg  style="width:16px;"> _ tools in relation with a <img alt="" src=images/Assembly_Workplane.svg  style="width:16px;"> workplane.

It links the length of the 2D line with the length of an arc (2D or 3D?).

The length value of the selected line equals the length of selected arc.

Since I couldn't get this tool working here's the statement of the tool tip: 

Add an \"EqualLineArcLength\" constraint to make a line of the same length as an arc.

## Usage

1.  Select the 2D line to be constrained.
2.  Select a 2D arc to read its length value.
3.  Activate the <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg  style="width:16px;"> [Equal Line Arc Length](Assembly3_ConstraintEqualLineArcLength.md) command using the:
    -   
        **<img src="images/Assembly_ConstraintEqualLineArcLength.svg" width=16px> [Equal Line Arc Length](Assembly3_ConstraintEqualLineArcLength.md)
**
        
        button.
4.  Press the **<img src="images/Assembly3_workbench_icon.svg" width=16px> [Solve constraints](Assembly3_ResolveConstraints.md)** or the **<img src="images/Assembly_QuickSolve.svg" width=16px> [Quick solve](Assembly3_QuickSolve.md)** button to recompute

:   

    :   (if **<img src="images/Assembly_AutoRecompute.svg" width=16px> [Auto recompute](Assembly3_AutoRecompute.md)** and **<img src="images/Assembly_SmartRecompute.svg" width=16px> [Smart recompute](Assembly3_SmartRecompute.md)** are disabled).

Depending on the order of the selected line types following **errors** appear:

Constraint "EqualLineArcLength" requires the 1st element to be a linear edge
Constraint "EqualLineArcLength" requires the 2nd element to be an arc edge
Constraint "EqualLineArcLength" requires the 2nd element to be a circular edge

---
[documentation index](../README.md) > Assembly3 ConstraintEqualLineArcLength/en
