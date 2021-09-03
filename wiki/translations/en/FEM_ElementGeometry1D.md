---
- GuiCommand:
   Name:FEM ElementGeometry1D
   MenuLocation:Model → Element Geometry → Beam cross section
   Workbenches:[FEM](FEM_Workbench.md)
   Shortcut:**C** **B**
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

## Description

ElementGeometry1D is used to define cross sections for beam elements. Currently the following types of cross sections are available: rectangular, circular and pipe.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ElementGeometry1D.svg" width=16px> [FEM ElementGeometry1D](FEM_ElementGeometry1D.md)** button.
    -   Select the **Model → Element Geometry → <img src="images/FEM_ElementGeometry1D.svg" width=16px> Beam cross section** option from the menu.
2.  Choose the type of cross section and specify the necessary dimensions:
    -   Rectangular: width and height,
    -   Circular: diameter,
    -   Pipe: diameter and thickness.
3.  Optionally press the **Add** button in the task panel and then click on the edge you want to have a prescribed cross section. If the edge selection is free, all remaining edges (whose cross section is not defined by other [FEM ElementGeometry1D](FEM_ElementGeometry1D.md) objects) will be automatically assigned.

## Options

## Properties

## Limitations

## Notes

-   For viewing results from CalculiX solver on the mesh expanded to the prescribed cross section, property `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) need to be set to `True`.

## Scripting





{{FEM Tools navi

}}  
