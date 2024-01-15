---
 GuiCommand:
   Name: FEM ConstraintInitialTemperature
   Name/ru: FEM ConstraintInitialTemperature
   MenuLocation: Model , Thermal Constraints , Constraint initial temperature
   Workbenches: FEM_Workbench/ru
   Shortcut: 
   SeeAlso: FEM_tutorial/ru
---

# FEM ConstraintInitialTemperature/ru


</div>



## Описание

Defines an initial temperature for a thermo-mechanical analysis.



## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> [Initial temperature](FEM_ConstraintInitialTemperature.md)** button.
    -   Select the **Model → Thermal boundary conditions and loads → <img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> Initial temperature** option from the menu.
2.  Enter an initial temperature value for the analysis.



## Ограничения

This tool applies the initial temperature to all nodes in the FEA model - it\'s not possible to select individual regions.



## Примечания

-   This tool uses the \*INITIAL CONDITIONS card in CalculiX. It is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node215.html>
-   Initial temperature has to be defined for all thermomechanical analyses performed with CalculiX, even the steady-state ones.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialTemperature/ru
