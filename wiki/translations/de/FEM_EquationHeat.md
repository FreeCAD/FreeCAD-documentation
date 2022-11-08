---
- GuiCommand   *
   Name   *FEM EquationHeat
   MenuLocation   *Solve → Heat equation
   Workbenches   *[FEM](FEM_Workbench.md)
   Version   *0.19
   SeeAlso   *[FEM tutorial](FEM_tutorial.md)
---

# FEM EquationHeat/de

## Beschreibung

This equation describes the heat transfer in rigid and fluid bodies.

For info about the math of the equation, see the [Elmer models manual](http   *//www.elmerfem.org/blog/documentation/), section *Heat Equation*.

## Usage

1.  After adding an Elmer solver as described [here](FEM_SolverElmer#Equations.md), select it in the [tree view](Tree_view.md).
2.  Now either use the toolbar button <img alt="" src=images/FEM_EquationHeat.svg  style="width   *24px;"> or the menu **Solve → Heat equation**.
3.  Change the [equation\'s solver settings](#Solver_Settings.md) or the [general solver settings](FEM_SolverElmer_SolverSettings.md) if necessary.

## Solver Settings 

For the general solver settings, see the [Elmer solver settings](FEM_SolverElmer_SolverSettings.md).

The heat equation provides these special settings   *

-    **Bubbles**   * There is also a residual-free-bubbles formulation of the stabilized finite-element method. It is more accurate and does not include any ad hoc terms. However, it may be computationally more expensive. If both **Note**   * If during the *first solver iteration* you get this error   * ERROR   *   * IterSolve   * Numerical Error   * System diverged over maximum tolerance.The **Bubbles** method failed. In this case set **[Stabilize](FEM_SolverElmer_SolverSettings#Base.md)** to *true*.

Equation   *

-    **Convection**   * The type of convection to be used in the heat equation.**Note**   * If this is not set to *None*, **[Stabilize](FEM_SolverElmer_SolverSettings#Base.md)** must be to *true* otherwise the convection term will not be considered for the heat equation.

-    **Phase Change Model**   * The model use for phase changes (ice to water etc.). The model *Spatial 1* is the apparent-heat-capacity method, *Spatial 2* and *Temporal* are effective-heat-capacity methods.For more info about the models, see [this paper](https   *//blog.rwth-aachen.de/gfd/files/2017/07/BT_2013_Schueller_elmer_icemole.pdf) (section 2.5.2.2) (is in German). In the paper it was also shown that *Spatial 1* has numerical problems on larger temperature gradients and that *Spatial 2* was preferred for the phase change ice to water.

## Constraint Information 

The elasticity equation takes the following constraints into account if they are set   *

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width   *32px;"> [Constraint body heat source](FEM_ConstraintBodyHeatSource.md)
-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width   *32px;"> [Constraint initial temperature](FEM_ConstraintInitialTemperature.md)
-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width   *32px;"> [Constraint temperature](FEM_ConstraintTemperature.md)

### Note

Except for calculations in 2D, for all above constraints it is important that they act on a face or a body. Constraints for 3D set to lines or vertices are not recognized by the Elmer solver.

## Result

The result is the temperature in Kelvin.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationHeat/de
