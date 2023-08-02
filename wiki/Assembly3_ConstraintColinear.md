---
- GuiCommand:
   Name: Assembly3 ConstraintColinear
   Icon: Assembly_ConstraintColinear.svg
   Workbenches: Assembly3_Workbench
---

# Assembly3 ConstraintColinear

## Description

The <img alt="" src=images/Assembly_ConstraintColinear.svg  style="width:16px;"> [Colinear](Assembly3_ConstraintColinear.md) command constrains two 2D lines such as non-subdivided wires made with the Draft workbench in relation with a work plane.

It links the positions of both 2D lines in a way that the origin of one line\'s implicit coordinate system (ICS) lies on the z axis of the other line\'s ICS with both z axes pointing in the same direction.

## Usage

1.  Select two 2D lines.
2.  Activate the <img alt="" src=images/Assembly_ConstraintColinear.svg  style="width:16px;"> [Colinear](Assembly3_ConstraintColinear.md) command using the:
    -   
        **<img src="images/Assembly_ConstraintColinear.svg" width=16px> [Colinear](Assembly3_ConstraintColinear.md)
**
        
        button.
3.  Press the **<img src="images/Assembly3_workbench_icon.svg" width=16px> [Solve constraints](Assembly3_ResolveConstraints.md)** or the **<img src="images/Assembly_QuickSolve.svg" width=16px> [Quick solve](Assembly3_QuickSolve.md)** button to recompute

:   

    :   (if **<img src="images/Assembly_AutoRecompute.svg" width=16px> [Auto recompute](Assembly3_AutoRecompute.md)** and **<img src="images/Assembly_SmartRecompute.svg" width=16px> [Smart recompute](Assembly3_SmartRecompute.md)** are disabled).

## Notes

This tool accepts a 3D elements as well e.g. edges or center lines.

-   2D/3D or 3D/2D: Instead of the 3D elements z axis the projection of that axis onto the 2D line\'s workplane is used to position the lines.
-   Both 3D: The lines are positioned to one another but I can\'t figure out how\...



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintColinear
