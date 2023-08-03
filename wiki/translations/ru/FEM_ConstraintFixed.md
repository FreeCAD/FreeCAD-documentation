---
 GuiCommand:
   Name: FEM ConstraintFixed
   Name/ru: FEM ConstraintFixed
   MenuLocation: Model , Mechanical Constraints , Constraint fixed
   Workbenches: FEM_Workbench/ru
   Shortcut: 
   SeeAlso: FEM_tutorial/ru
---

# FEM ConstraintFixed/ru


</div>

## Описание

Creates a FEM constraint for a fixed geometry entry by locking all 6 degrees of freedom of the selected object.

## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintFixed.svg" width=16px> [FEM ConstraintFixed](FEM_ConstraintFixed.md)** button.
    -   Select the **Model → Mechanical Constraints → <img src="images/FEM_ConstraintFixed.svg" width=16px> Constraint fixed** option from the menu.
2.  In the [3D view](3D_view.md) select the object the constraint should be applied to, which can be a vertex (corner), edge, or face.

## Ограничения

You cannot mix object-types within the same constraint. Use one fixed constraint for each object type.

## Примечания





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFixed/ru
