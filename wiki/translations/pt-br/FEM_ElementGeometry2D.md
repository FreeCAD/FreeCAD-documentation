---
- GuiCommand:
   Name:FEM ElementGeometry2D
   MenuLocation:Model → Element Geometry → Shell plate thickness
   Workbenches:[FEM](FEM_Workbench.md)
   Shortcut:**C** **S**
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

## Descrição

ElementGeometry2D is used to define thickness of 2D FEM elements, all or laying on the chosen surface.

## Utilização

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ElementGeometry2D.svg" width=16px> [FEM ElementGeometry2D](FEM_ElementGeometry2D.md)** button.
    -   Select the {{MenuCommand|Model → Element Geometry → <img src="images/FEM_ElementGeometry2D.svg" width=16px> Shell plate thickness}} option from the menu.
2.  Define a thickness parameter.
3.  Optionally press the **Add** button in the task panel and then click on the face you want to have a prescribed thickness. If the face selection is free, all remaining faces (whose thickness is not defined by other [FEM ElementGeometry2D](FEM_ElementGeometry2D.md) objects) will be automatically assigned.

## Limitações

-   Analysis combining shell elements with solid or edge elements is not supported in the current version (FreeCAD 0.18).

## Propriedades


**Thickness**

: specifies the thickness of the shell.

## Scripting

## Notas

For viewing results from CalculiX solver on the mesh expanded to the prescribed thickness, property `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) need to be set to `True`.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}  
