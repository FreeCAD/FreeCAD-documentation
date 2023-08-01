---
- GuiCommand:
   Name:FEM ConstraintPlaneRotation
   MenuLocation:Model → Geometrical Constraints → Constraint plane rotation
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM Constraint transform](FEM_ConstraintTransform.md)
---

# FEM ConstraintPlaneRotation

## Description

Creates a FEM constraint for keeping the nodes in a planar surface in the same plane.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> '''FEM ConstraintPlaneRotation'''** button.
    -   Select the **Model → Geometrical Constraints → <img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> Constraint plane rotation** option from the menu.
2.  In the [3D view](3D_view.md) select the object the constraint should be applied to, which can be a face.

## Limitations

1.  Plane rotation constraint can only be applied to a single planar face.
2.  When a plane rotation constraint is applied to the same face as a displacement/fixed constraint, the displacement/fixed constraint takes preference.

## Notes

1.  The constraint uses the \*MPC card in CalculiX. The card is explained in detail at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node220.html>




 {{FEM Tools navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPlaneRotation
