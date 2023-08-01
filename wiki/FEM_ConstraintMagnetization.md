---
- GuiCommand:
   Name: FEM ConstraintMagnetization
   MenuLocation:  Model - Electromagnetic Constraints - Constraint magnetization
   Workbenches: [FEM](FEM_Workbench.md)
   Version: 0.21
   SeeAlso: [Magnetodynamic equation](FEM_EquationMagnetodynamic.md), [Magnetodynamic 2D equation](FEM_EquationMagnetodynamic2D.md)
---

# FEM ConstraintMagnetization

## Description

Creates a FEM constraint for the magnetization. To be used together with the [Magnetodynamic](FEM_EquationMagnetodynamic.md) and [Magnetodynamic 2D](FEM_EquationMagnetodynamic2D.md) equations.

## Usage

1.  Press the **<img src="images/FEM_ConstraintMagnetization.svg" width=16px> [FEM ConstraintMagnetization](FEM_ConstraintMagnetization.md)** button or use the menu **Model → Electromagnetic Constraints → <img src="images/FEM_ConstraintMagnetization.svg" width=16px> Constraint magnetization**.
2.  In the [3D view](3D_view.md) select the object the constraint should be applied to.
3.  Press the **Add** button.

## Options

-   **Magnetization\_\*\_1**: The real/imaginary part of the magnetization in x-direction in A/m. For other coordinate systems than Cartesian 3D, this will be the first coordinate of the system instead of x.
-   **Magnetization\_\*\_2**: The real/imaginary part of the magnetization in y-direction in A/m. For other coordinate systems than Cartesian 3D, this will be the second coordinate of the system instead of y.
-   **Magnetization\_\*\_3**: The real/imaginary part of the magnetization in z-direction in A/m. For other coordinate systems than Cartesian 3D, this will be the third coordinate of the system instead of z. If the coordinate system has no third coordinate, this setting will be ignored.
-   **Magnetization\_\*\_\*\_Disabled**: Whether the corresponding parameter is disabled (assumed as unknown by the solver).




 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintMagnetization
