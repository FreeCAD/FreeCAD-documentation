---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintPressure
   MenuLocation: Model , Mechanical boundary conditions and loads , Pressure load
   Workbenches: FEM_Workbench
   SeeAlso: FEM_ConstraintForce
}}
{{GuiCommandFemInfo
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintPressure

## Description

Applies a pressure load to a face.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Pressure load](FEM_ConstraintPressure.md)** button.
    -   Select the **Model → Mechanical boundary conditions and loads → <img src="images/FEM_ConstraintPressure.svg" width=16px> Pressure load** option from the menu.
2.  Press the **Add** button and select face(s) in the [3D view](3D_view.md). Optionally press the **Remove** and click on the faces that you want to remove from the selection.
3.  Edit the appropriate window to specify the pressure load in MPa.
4.  Tick the box to reverse the direction if necessary.

## Notes

-   Distribution of the pressure on a face is always uniform and always perpendicular to the face.

-    {{VersionMinus|0.21}}: Pressure load can be applied to shells but only when [Gmsh](FEM_MeshGmshFromShape.md) is used for meshing and group meshing is set to true. It is hardcoded as true so the user doesn\'t have to worry about that. However, due to a bug, pressure load may require remeshing to work on shells.

-   This feature uses the [\*DLOAD card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node190.html).




 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPressure
