# FEM SolverElmer SolverSettings/en
This page describes the possible settings for [solver Elmer](FEM_SolverElmer.md).

# General

Elmer is a multiphysics solver. Therefore you can use several main equations to solve problems. The different equations are listed [here](FEM_SolverElmer#About_Equations.md).

There are solver settings, available for all equations. These are described here. Settings only available for a particular equation are described in the pages of the corresponding equation.

Elmer offers the [solving types](#Type.md) *steady-state* and *transient* and two main solving systems, [linear system](#Linear_System.md) and [nonlinear system](#Nonlinear_System.md). The nonlinear system is used for the <img alt="" src=images/FEM_EquationFlow.svg  style="width   *24px;"> [Flow equation](FEM_EquationFlow.md) and <img alt="" src=images/FEM_EquationHeat.svg  style="width   *24px;"> [Heat equation](FEM_EquationHeat.md).

# Editing Settings 

The solver settings can be found in the [property editor](Property_editor.md) after clicking on an equation in the [tree view](Tree_view.md). You can edit them there directly like any other property.

## Solver

### Timestepping

For transient simulations the time steps need to be defined. This is done by the following settings   *

-    **BDFOrder**   * Order for the method *BDF* ([Backward Differentiation Formula](https   *//en.wikipedia.org/wiki/Backward_differentiation_formula)). It is currently only used for the <img alt="" src=images/FEM_EquationHeat.svg  style="width   *24px;"> [Heat equation](FEM_EquationHeat.md). It is recommended to use use the default of 2.

-    **Timestep Intervals**   * An array of calculations per time interval.The solver will perform one time interval after another. For example if the solver should calculate the first 10 seconds in steps of 0.1 second, then 50 seconds in steps of 1 second and then stop, you need to set the timestep intervals \[100, 50\] and the timestep size intervals \[0.1, 1.0\].

-    **Timestep Sizes**   * An array of timestep sizes. The time unit is second. The array corresponds to the **Timestep Intervals**.

### Type

-    **Simulation type**   * If the simulation is *Steady state*, *Transient* or just *Scanning*. Transient means the development over time is calculated. See section [Timestepping](#Timestepping.md) for the necessary settings.

-    **Steady State Max Iterations**   * The maximum number of steady-state solver runs.

-    **Steady State Min Iterations**   * The minimum number of steady-state solver runs.

## Equation

### Base

All equations have these properties   *

-    **Label**   * Name of the equation in the tree view.

-    **Priority**   * Number determining the priority of this equation to the other equations in the analysis. The equation with the highest number in the analysis will be solved as first. If two equations have the same priority number, the one that is first in the tree view will solved first.

-    **Stabilize**   * If set to *true*, the solver will use stabilized finite element method when solving the heat equation with a convection term. If set to *false*, the Residual Free Bubble (RFB) stabilization is used instead. If convection dominates, stabilization must be used in order to successfully solve the equation.

### Linear System 

This system has the following properties   *

-    **BiCGstabl Degree**   * Polynomial degree for the iterative solver method *BiCGStabl*. This has only an effect if **Linear Solver Type** is *Iterative* and **Linear Iterative Method** is *BiCGStabl*. Starting with the default of 2 is recommended.

-    **Idrs Parameter**   * Parameter for the iterative solver method *Idrs*. This has only an effect if **Linear Solver Type** is *Iterative* and **Linear Iterative Method** is *Idrs*. Starting with the default of 2 is recommended. Setting the parameter to 3 might increase the solving speed a bit. For flow analyses the *Idrs* method is up to 30 % faster than the default *BiCGStab* method.

-    **Linear Direct Method**   * Method used for direct solving. This has only an effect if The possible methods are *Banded*, *MUMPS* and *Umpfpack*. Note that *MUMPS* usually needs to be installed before you can use it.**Note**   * when you use more than one CPU core for the solver (<small>(v1.0)</small> ) only *MUMPS* can be used.

-    **Linear Iterations**   * Maximal number of iterations for an iterative solver run. This has only an effect if **Linear Solver Type** is *Iterative*.

-    **Linear Iterative Method**   * Method used for iterative solving. This has only an effect if **Linear Solver Type** is *Iterative*.

-    **Linear Preconditioning**   * Method used for the preconditioning. For info about preconditioning, see [this presentation](http   *//www.nic.funet.fi/index/elmer/slides/ElmerLinearSolvers.pdf) (page 8) from Elmer.

-    **Linear Solver Type**   * If the solving is done *Direct* or *Iterative*.

-    **Linear System Solver Disabled**   * Disables the linear solver. Only use this for special cases.It can be used to disable temporarily an equation since its solving is then not performed. There are, however cases there the solver is send to an infinite loop instead.

-    **Linear Tolerance**   * The tolerance for the solver to stop. If the error is smaller than the tolerance, the solver run will be is finished. Otherwise the full number of In the Elmer solver log you see how the error is minimized while the solver is running. (Look in the log at the end off every solver iteration for the value behind *Relative Change*). In case it does not go down below a certain value but reaches a value above the current tolerance that is acceptable for you, you can increase the tolerance.

### Nonlinear System 

This system is iterative and has the following properties   *

-    **Nonlinear Iterations**   * Maximal number of iterations.

-    **Nonlinear Newton After Iterations**   *

-    **Nonlinear Newton After Tolerance**   *

-    **Nonlinear Tolerance**   * The tolerance for the solver to stop. If the error is smaller than the tolerance, the solver run will be is finished. Otherwise the full number of In the Elmer output you see in how the error is minimized while the solver is running. In case it does not go down below a certain value that is acceptable but above the current tolerance, you can increase the tolerance.

-    **Relaxation Factor**   * This is THE most important setting in case the solver does not converge   *

#### Relaxation Factor 

If the solver iteration results oscillate numerically, the solver results cannot converge to a final, stable value. To avoid that, the calculated variable $T_{i}$ of the i-th iteration/solver run is not taken as input for the next iteration, but $T_{i}^{'}$, a value that is \"damped\" with the result from the previous iteration. The relaxation factor $\lambda$ is thereby defined as

$\quad
T_{i}^{'} = \lambda T_{i}+\left(1-\lambda\right)T_{i-1}$

So for the default of 1.0, no damping is used. The smaller $\lambda$, the greater the damping and the the longer the convergence time. Therefore if the solver does not converge, start changing the relaxation factor to 0.9, then to 0.8 and so on. Values below 0.3 are unusual and if you need this, you should have a closer look to the math of your analysis. For cases, where you get a proper convergence you can set $\lambda$ above 1.0 to speed the convergence up.

### Steady State 

This part of the settings has only one property   *

-    **Steady State Tolerance**   * The specific steady state or coupled system convergence tolerance. All the equation solvers must meet their own tolerances for the variable $\omega^2$ they calculate, before the whole system is deemed converged. The tolerance criterion is   *

$\quad
\left\Vert u_{i}-u_{i-1}\right\Vert <\epsilon\left\Vert u_{i}\right\Vert$

whereas $\epsilon$ is the steady state tolerance and $u_{i}$ is the calculated variable in the i-th iteration/solver run.


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverElmer SolverSettings/en
