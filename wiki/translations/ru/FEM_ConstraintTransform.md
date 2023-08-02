---
- GuiCommand:
   Name: FEM ConstraintTransform
   Name/ru: FEM ConstraintTransform
   MenuLocation:  Model -> Geometrical constraints -> Constraint transform
   Workbenches: FEM_Workbench/ru
   SeeAlso: FEM_ConstraintPlaneRotation/ru
---

# FEM ConstraintTransform/ru


</div>

## Описание

Transforms the coordinate system of a face to a particular coordinate system - rectangular or cylindrical.

## Применение

1.  Apply the [Constraint displacement](FEM_ConstraintDisplacement.md) to a face first.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintTransform.svg" width=16px> [FEM ConstraintTransform](FEM_ConstraintTransform.md)** button.
    -   Select the **Model → Geometrical Constraints → <img src="images/FEM_ConstraintTransform.svg" width=16px> Constraint transform** option from the menu.
3.  Select rectangular or cylindrical transform. The former can be applied to any face, the latter is available only for the cylindrical faces.
4.  Select a face to which the displacement constraint was previously applied. Press the **Add** button.
5.  For rectangular transform, specify a rotation about each of the three axes.

## Limitations

-   Cylindrical transform can be applied only to cylindrical faces.

## Notes

-   This constraint can be used to simulate torsion but only for cylindrical bars or parts containing such bars used to transmit torque.
-   The constraint uses the \*TRANSFORM card in CalculiX.


<div class="mw-translate-fuzzy">





</div>


{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTransform/ru
