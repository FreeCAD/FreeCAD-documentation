---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ElementRotation1D
   MenuLocation: Model , Element Geometry , Beam rotation
   Workbenches: FEM_Workbench
   SeeAlso: FEM_tutorial
}}
{{GuiCommandFemInfo
   Solvers: CalculiX
}}
---

# FEM ElementRotation1D/en

## Description

**ElementRotation1D** is used to rotate the beam profile around the axis of beam elements.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ElementRotation1D.svg" width=16px> [Beam rotation](FEM_ElementRotation1D.md)** button.
    -   Select the **Model → Element Geometry → <img src="images/FEM_ElementRotation1D.svg" width=16px> Beam rotation** option from the menu.
2.  Specify the angle by which the beam profile is to be rotated.

## Properties


**Rotation**

: specifies the angle of rotation.

## Limitations

-   Currently, multiple rotations are not supported (a single rotation is applied to all beams in the model).

## Notes

-   To visualize the rotated cross-section it is necessary to set `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) to `True` and run the analysis.
-   This feature uses the [\*BEAM SECTION card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node162.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D/en
