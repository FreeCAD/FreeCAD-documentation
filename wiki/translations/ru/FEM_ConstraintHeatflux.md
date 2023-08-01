---
- GuiCommand:/ru
   Name:FEM ConstraintHeatflux
   Name/ru:FEM ConstraintHeatflux
   MenuLocation:Model → Thermal Constraints → Constraint heatflux
   Workbenches:[FEM](FEM_Workbench/ru.md)
   Shortcut:
   SeeAlso:[FEM tutorial](FEM_tutorial/ru.md)
---

# FEM ConstraintHeatflux/ru


</div>

## Description

This constraint specifies film heat transfer of a surface at temperature *T* and with a film coefficient *h* to the environment or sink at temperature *T~0~*. The convective heat flux *q* will satisfy: ***q = h(T -T~0~)***

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [FEM ConstraintHeatflux](FEM_ConstraintHeatflux.md)** button.
    -   Select the **Model → Thermal Constraints → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Constraint heatflux** option from the menu.
2.  In the [3D view](3D_view.md) select the face(s) the constraint should be applied to.
3.  Enter the desired surface temperature, heat transfer coefficient and environment temperature.

## Notes

-   The constraint uses the \*FILM card in CalculiX. The heatflux constraint is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html>





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/ru
