---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintTransform
   MenuLocation: Model , Geometrical analysis features , Local coordinate system
   Workbenches: FEM_Workbench
   SeeAlso: FEM_ConstraintPlaneRotation
}}
{{GuiCommandFemInfo
   Solvers: CalculiX
}}
---

# FEM ConstraintTransform

## Description

Transforms the coordinate system of a face to a user-defined coordinate system - rectangular or cylindrical. This coordinate system affects the boundary condition and load definitions. For example, you can use it to fix the displacements in the normal direction of an inclined face. Just select the proper component of the [displacement boundary condition](FEM_ConstraintDisplacement.md).

## Usage

1.  Apply the [displacement boundary condition](FEM_ConstraintDisplacement.md) to a face first.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintTransform.svg" width=16px> [Local coordinate system](FEM_ConstraintTransform.md)** button.
    -   Select the **Model → Geometrical analysis features → <img src="images/FEM_ConstraintTransform.svg" width=16px> Local coordinate system** option from the menu.
3.  Select rectangular or cylindrical transform. The former can be applied to any face, the latter is available only for the cylindrical faces.
4.  Select a face to which the displacement boundary condition was previously applied. Press the **Add** button.
5.  For rectangular transform, specify a rotation about each of the three axes. Arrows displayed on the face represent the new directions (X - red, Y - green and Z - blue).

## Limitations

-   Cylindrical transform can be applied only to cylindrical faces.

## Notes

-   This feature can be used to simulate torsion but only for cylindrical bars or parts containing such bars used to transmit torque.
-   The feature uses the [\*TRANSFORM card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node253.html).




 {{FEM_Tools_navi}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTransform
