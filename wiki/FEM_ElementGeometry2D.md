---
- GuiCommand:
   Name:FEM ElementGeometry2D
   MenuLocation:Model → Element Geometry → Shell plate thickness
   Workbenches:[FEM](FEM_Workbench.md)
   Shortcut:**C** **S**
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM ElementGeometry2D

## Description

**ElementGeometry2D** is used to define thickness of 2D FEM elements, all or lying on the chosen surface.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ElementGeometry2D.svg" width=16px> [FEM ElementGeometry2D](FEM_ElementGeometry2D.md)** button.
    -   Select the **Model → Element Geometry → <img src="images/FEM_ElementGeometry2D.svg" width=16px> Shell plate thickness** option from the menu.
2.  Define a thickness parameter.
3.  Optionally press the **Add** button in the task panel and then click on the face you want to have a prescribed thickness. If the face selection is empty, all remaining faces (whose thickness is not defined by other [FEM ElementGeometry2D](FEM_ElementGeometry2D.md) objects) will be automatically assigned.

## Limitations

-   Analysis combining shell elements with solid or edge elements is not supported in the current version (FreeCAD 0.18).

## Properties


**Thickness**

: specifies the thickness of the shell.

## Scripting

## Notes

For viewing results from CalculiX solver on the mesh expanded to the prescribed thickness, property `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) need to be set to `True`.




 {{FEM Tools navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry2D
