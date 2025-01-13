# FEM ElementGeometry2D/ro
---
 GuiCommand:   Name: FEM ElementGeometry2D   MenuLocation: Model ,Shell plate tickness   ---


</div>




<div class="mw-translate-fuzzy">

## Descriere


</div>

**ElementGeometry2D** is used to define the thickness of 2D (shell and <small>(v1.0)</small> : plane stress/strain) FEM elements, all or lying on the chosen surface.




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ElementGeometry2D.svg" width=16px> [Shell plate thickness](FEM_ElementGeometry2D.md)** button.
    -   Select the **Model → Element Geometry → <img src="images/FEM_ElementGeometry2D.svg" width=16px> Shell plate thickness** option from the menu.
2.  Specify the shell thickness.
3.  Optionally press the **Add** button in the task panel and then click on the face you want to have a prescribed thickness. If the face selection is empty, all the remaining faces (whose thickness is not defined by other [FEM ElementGeometry2D](FEM_ElementGeometry2D.md) objects) will be automatically assigned.

## Limitations

-   Currently, analyses combining shell elements with solid or edge elements are not supported.

## Properties


**Thickness**

: specifies the thickness of the 2D elements.

## Notes

-   For viewing results from CalculiX solver on the mesh expanded to the prescribed thickness, property `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) need to be set to `True`.
-   This feature uses the [\*SHELL SECTION card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node238.html) for shell elements and [\*SOLID SECTION card](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node239.html) for plane stress/strain elements.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry2D/ro
