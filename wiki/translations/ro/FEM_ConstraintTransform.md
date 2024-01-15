# FEM ConstraintTransform/ro
---
 GuiCommand:   Name: FEM ConstraintTransform   MenuLocation:  Model , Mechanical constraints , Constraint transform   ---


</div>




<div class="mw-translate-fuzzy">

De completat


</div>

Transforms the coordinate system of a face to a particular coordinate system - rectangular or cylindrical.

## Usage

1.  Apply the [Displacement boundary condition](FEM_ConstraintDisplacement.md) to a face first.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintTransform.svg" width=16px> [Local coordinate system](FEM_ConstraintTransform.md)** button.
    -   Select the **Model → Geometrical analysis features → <img src="images/FEM_ConstraintTransform.svg" width=16px> Local coordinate system** option from the menu.
3.  Select rectangular or cylindrical transform. The former can be applied to any face, the latter is available only for the cylindrical faces.
4.  Select a face to which the displacement boundary condition was previously applied. Press the **Add** button.
5.  For rectangular transform, specify a rotation about each of the three axes.

## Limitations

-   Cylindrical transform can be applied only to cylindrical faces.

## Notes

-   This feature can be used to simulate torsion but only for cylindrical bars or parts containing such bars used to transmit torque.
-   The feature uses the \*TRANSFORM card in CalculiX.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTransform/ro
