---
- GuiCommand:
   Name:FEM ConstraintBodyHeatSource
   MenuLocation: Model → Thermal Constraints → Constraint body heat source
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM ConstraintBodyHeatSource/en

## Description

Defines an internally generated body heat given in W/kg (not J/m³).

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> [FEM ConstraintBodyHeatSource](FEM_ConstraintBodyHeatSource.md)** button.
    -   Select the **Model → Thermal Constraints → <img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> Constraint temperature** option from the menu.
2.  In the [3D view](3D_view.md) select the objects the constraint should be applied to, which can be a vertices (corners), edges, or faces.
3.  Enter a specific heat value to apply to the objects.

## Notes

-   For more information see [this forum thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) and following posts.
-   Elmer examples can also be found in [Elmer GUI Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf).




{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintBodyHeatSource/en
