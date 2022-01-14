---
- GuiCommand:
   Name:FEM ConstraintForce
   MenuLocation:Model → Mechanical Constraints → Constraint force
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM ConstraintPressure](FEM_ConstraintPressure.md)
---

# FEM ConstraintForce

## Description

This command applies a force of given value \[N\] to selected target geometry.

## Usage

Applying a force to a face, line or point:

-   In FEM workbench, click on <img alt="Constraint Force" src=images/FEM_ConstraintForce.svg  style="width:24px;"> or select **Model** → **Mechanical Constraints** → **Constraint force** to open Force Constraint properties dialog.

-   If you have Mesh displayed, you need to hide it (select the mesh object and press **spacebar** or right-click and select **Hide item**) and show the original model.

-   Click on a *face*, *line* or *point* to which a force should be applied. It will appear in the list of geometrical objects.

-   Fill in **Load [N]** with a force value in \[N\].

-    **Direction**: In a typical case, you\'ll leave this field empty to apply a force in the normal direction. You can revert the direction of the force by clicking **Reverse direction**. In other cases, you need to pick a face/plane or edge, which serves as reference for force direction.

![](images/FEM_ConstraintForce_example.JPG )

-   Click **OK** to finish the dialog and create **[<img src=images/FEM_ConstraintForce.svg style="width:24px"> ConstraintForce** object.

## Notes

Defined force is applied uniformly to selected objects. For example, if you define one force constraint with 200 N applied to two faces having the same area, each face will be uniformly loaded with 100 N.




 {{FEM Tools navi}}

---
[documentation index](../README.md) > FEM ConstraintForce
