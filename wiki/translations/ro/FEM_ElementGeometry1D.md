# FEM ElementGeometry1D/ro
---
- GuiCommand:   Name: FEM ElementGeometry1D   MenuLocation: Model -> Beam cross section   ---


</div>

## Descriere

**ElementGeometry1D** is used to define cross sections for beam elements. Currently the following types of cross sections are available: rectangular, circular and pipe.


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ElementGeometry1D.svg" width=16px> [FEM ElementGeometry1D](FEM_ElementGeometry1D.md)** button.
    -   Select the **Model → Element Geometry → <img src="images/FEM_ElementGeometry1D.svg" width=16px> Beam cross section** option from the menu.
2.  Choose the type of cross section and specify the necessary dimensions:
    -   Rectangular: width and height,
    -   Circular: diameter,
    -   Pipe: diameter and thickness.
3.  Optionally press the **Add** button in the task panel and then click on the edge you want to have a prescribed cross section. If the edge selection is free, all remaining edges (whose cross section is not defined by other [FEM ElementGeometry1D](FEM_ElementGeometry1D.md) objects) will be automatically assigned.

## Opţiuni

## Proprietăți

## Limite

## Notă

-   For viewing results from CalculiX solver on the mesh expanded to the prescribed cross section, property `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) need to be set to `True`.

## Scrip-Programare 





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry1D/ro
