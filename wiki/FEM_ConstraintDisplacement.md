---
- GuiCommand:
   Name:FEM ConstraintDisplacement
   MenuLocation:Model → Mechanical Constraints → Constraint displacement
   Workbenches:[FEM](FEM_Workbench.md)
   Shortcut:
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM ConstraintDisplacement

## Description

Creates a FEM constraint for a prescribed displacement of a selected object for a specified degree of freedom.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintDisplacement.svg" width=16px> [FEM ConstraintDisplacement](FEM_ConstraintDisplacement.md)** button.
    -   Select the **Model → Mechanical Constraints → <img src="images/FEM_ConstraintDisplacement.svg" width=16px> Constraint displacement** option from the menu.
2.  In the [3D view](3D_view.md) select the object the constraint should be applied to, which can be a vertex (corner), edge, or face.
3.  Choose a degree of freedom or prescribe a displacement.

## Notes

1.  The constraint uses the \*BOUNDARY card in CalculiX. Fixing a degree of freedom is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node164.html> and prescribing a displacement for a degree of freedom is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node165.html>




 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintDisplacement
