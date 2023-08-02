---
- GuiCommand:
   Name: FEM ConstraintPressure
   MenuLocation: Model -> Mechanical Constraints -> Constraint pressure
   Workbenches: FEM_Workbench
   SeeAlso: FEM_ConstraintForce
---

# FEM ConstraintPressure/pl



## Opis

Nakłada na ścianę warunek nacisku ciśnieniem.



## Użycie

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintPressure.svg" width=16px> [FEM ConstraintPressure](FEM_ConstraintPressure.md)** button.
    -   Select the **Model → Mechanical Constraints → <img src="images/FEM_ConstraintPressure.svg" width=16px> Constraint pressure** option from the menu.
2.  Click on **Add reference** and select face in the [3D view](3D_view.md).
3.  Edit appropriate window to specify pressure load in MPa.
4.  Tick box to reverse direction if necessary.

## Notes

-   Distribution of pressure on face is always uniform and always perpendicular to face.

-   Pressure on faces: <https://github.com/FreeCAD/FreeCAD/issues/5699>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPressure/pl
