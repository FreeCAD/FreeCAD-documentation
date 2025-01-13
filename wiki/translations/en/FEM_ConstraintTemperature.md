---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintTemperature
   MenuLocation: Model , Thermal boundary conditions and loads , Temperature boundary condition
   Workbenches: FEM_Workbench
   SeeAlso: FEM_tutorial
}}
{{GuiCommandFemInfo
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintTemperature/en

## Description

Defines a temperature boundary condition or, optionally, a concentrated heat flux load.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintTemperature.svg" width=16px> [Temperature boundary condition](FEM_ConstraintTemperature.md)** button.
    -   Select the **Model → Thermal boundary conditions and loads → <img src="images/FEM_ConstraintTemperature.svg" width=16px> Temperature boundary condition** option from the menu.
2.  Press the **Add** button.
3.  In the [3D view](3D_view.md) select the objects the boundary condition should be applied to, which can be vertices, edges, or faces. Optionally, press the **Remove** button and click on the objects that you want to remove from the selection.
4.  Choose the constraint type and specify its parameter:
    -   *Temperature* (default) - temperature boundary condition, enter the *Temperature* (K)
    -   *CFlux* - concentrated heat flux load, enter the *Concentrated heat flux* (mW) - this value will be divided by the number of nodes on the underlying geometrical entity to achieve a total flux of a given magnitude on that entity

## Notes

-   The temperature boundary condition uses the \*BOUNDARY card in CalculiX. It is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html>
-   The **Concentrated heat flux** option uses the \*CFLUX card in CalculiX: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node168.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTemperature/en
