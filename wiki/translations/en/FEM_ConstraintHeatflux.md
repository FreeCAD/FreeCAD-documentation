---
 GuiCommand:
   Name: FEM ConstraintHeatflux
   MenuLocation: Model , Thermal boundary conditions and loads , Heat flux load
   Workbenches: FEM_Workbench
   SeeAlso: FEM_tutorial
---

# FEM ConstraintHeatflux/en

## Description

Defines a convective heat flux load on a surface at a temperature *T* with a film coefficient *h* and with the environment (sink) temperature *T~0~*. The convective heat flux *q* will satisfy: ***q = h(T -T~0~)***. Optionally, can also define a regular surface heat flux load.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [Heat flux load](FEM_ConstraintHeatflux.md)** button.
    -   Select the **Model → Thermal boundary conditions and loads → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Heat flux load** option from the menu.
2.  In the [3D view](3D_view.md) select the face(s) the heat flux load should be applied to.
3.  Enter the desired heat transfer coefficient and environment temperature.

### Option

By default, this feature defines a convective heat flux. By using the option **Surface heat flux**, one can specify a heat flux value in Watts per surface area (W/m\^2).

## Notes

-   The heat flux load uses the \*FILM card in CalculiX. It is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html>
-   The **Surface heat flux** option uses the \*DFLUX card in CalculiX: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node188.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/en
