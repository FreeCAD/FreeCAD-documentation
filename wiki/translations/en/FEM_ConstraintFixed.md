---
- GuiCommand:
   Name:FEM ConstraintFixed
   MenuLocation:Model → Mechanical Constraints → Constraint fixed
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM Constraint contact](FEM_ConstraintContact.md)
---

# FEM ConstraintFixed/en

## Description

Creates a FEM constraint for a fixed geometry entry by locking all 6 degrees of freedom of the selected object.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintFixed.svg" width=16px> [FEM ConstraintFixed](FEM_ConstraintFixed.md)** button.
    -   Select the **Model → Mechanical Constraints → <img src="images/FEM_ConstraintFixed.svg" width=16px> Constraint fixed** option from the menu.
2.  In the [3D view](3D_view.md) select the object the constraint should be applied to, which can be a vertex (corner), edge, or face.

## Limitations

You cannot mix object-types within the same constraint. Use one fixed constraint for each object type.

## Notes





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFixed/en
