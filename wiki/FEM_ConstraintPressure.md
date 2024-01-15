---
 GuiCommand:
   Name: FEM ConstraintPressure
   MenuLocation: Model , Mechanical boundary conditions and loads , Pressure load
   Workbenches: FEM_Workbench
   SeeAlso: FEM_ConstraintForce
---

# FEM ConstraintPressure

## Description

Applies a pressure load to a face.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Pressure load](FEM_ConstraintPressure.md)** button.
    -   Select the **Model → Mechanical boundary conditions and loads → <img src="images/FEM_ConstraintPressure.svg" width=16px> Pressure load** option from the menu.
2.  Click on **Add** and select face in the [3D view](3D_view.md).
3.  Edit appropriate window to specify pressure load in MPa.
4.  Tick box to reverse direction if necessary.

## Notes

-   Distribution of the pressure on a face is always uniform and always perpendicular to the face.

-   Pressure on shells: <https://github.com/FreeCAD/FreeCAD/issues/5699>




 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPressure
