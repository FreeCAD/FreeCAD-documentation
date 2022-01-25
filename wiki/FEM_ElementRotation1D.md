---
- GuiCommand:
   Name:FEM ElementRotation1D
   MenuLocation:Model → Element Geometry → Beam rotation
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM ElementRotation1D

## Description

ElementRotation1D is used to rotate the beam profile around the axis of beam elements.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ElementRotation1D.svg" width=16px> [FEM ElementRotation1D](FEM_ElementRotation1D.md)** button.
    -   Select the **Model → Element Geometry → <img src="images/FEM_ElementRotation1D.svg" width=16px> Beam rotation** option from the menu.
2.  Specify the angle by which the beam profile is to be rotated.

## Options

## Properties

## Limitations

-   Currently multiple rotations are not supported (a single rotation is applied to all beams in the model).

## Notes

-   To visualize the rotated cross-section it is necessary to set `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) to `True` and run the analysis.




 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D
