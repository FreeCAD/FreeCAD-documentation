---
- GuiCommand   */de
   Name   *FEM EquationElasticity
   Name/de   *FEM Elastizitätsgleichung
   MenuLocation   *Lösen → Elastizitätsgleichung
   Workbenches   *[FEM](FEM_Workbench/de.md)
   SeeAlso   *[FEM Tutorial](FEM_tutorial/de.md)
---

# FEM EquationElasticity/de


</div>

## Beschreibung

This equation describes the mechanical properties of rigid bodies.

For info about the math of the equation, see the [Elmer models manual](http   *//www.elmerfem.org/blog/documentation/), section *Linear Elasticity*.

## Usage

1.  After adding an Elmer solver as described [here](FEM_SolverElmer#Equations.md), select it in the [tree view](Tree_view.md).
2.  Now either use the toolbar button <img alt="" src=images/FEM_EquationElasticity.svg  style="width   *24px;"> or the menu **Solve → Elasticity equation**.
3.  Change the [equation\'s solver settings](#Solver_Settings.md) or the [general solver settings](FEM_SolverElmer_SolverSettings.md) if necessary.

## Solver Settings 

For the general solver settings, see the [Elmer solver settings](FEM_SolverElmer_SolverSettings.md).

The elasticity equation provides these special settings   *

-    **Calculate Pangle**   * If the principal angles should be calculated.

-    **Calculate Principal**   * If all stresses should be calculated.

-    **Calculate Strains**   * If strains will be calculated. This will also calculate the stresses, even if **Calculate Principal** or **Calculate Stresses** is *false*.

-    **Calculate Stresses**   * If stresses should be calculated. Compared to **Calculate Principal** the Tresca yield criterion and the principal stress will not be calculated.

-    **Constant Bulk System**   * See the Elmer manual for more info.

-    **Displace Mesh**   * If mesh can be deformed. This is by default *true* and must be set to *false* for eigenfrequency analyses.

-    **Fix Displacement**   * If displacements or forces are set. thereby **Model Lumping** is automatically used.

-    **Geometric Stiffness**   * Considers the geometric stiffness of the body.

-    **Incompressible**   * Computation of incompressible material in connection with viscoelastic Maxwell material and a custom **Variable**.

-    **Maxwell Material**   * Compute the viscoelastic material model.

-    **Model Lumping**   * Uses [model lumping](https   *//en.wikipedia.org/wiki/Lumped-element_model).

-    **Model Lumping Filename**   * File to save the results from the model lumping.

-    **Stability Analysis**   * If *true* **Eigen Analysis** becomes a stability analysis (buckling analysis). Otherwise a modal analysis is performed.

-    **Update Transient System**   * See the Elmer manual for more info.

-    **Variable**   * The variable for the elasticity equation. Only change this if **Incompressible** is set to *true* in accordance to the Elmer manual.

Eigenvalues   *

-    **Eigen Analysis**   * If an eigen analysis should be performed (calculation of eigenmodes and eigenfrequencies).

-    **Eigen System Complex**   * Should be *true* if the eigen system is complex. it must be *false* for a damped eigen value analyses.

-    **Eigen System Compute Residuals**   * Computes residuals of the eigen value system.

-    **Eigen System Damped**   * Set a damped eigen analysis. Can only be used if **[Linear Solver Type](FEM_SolverElmer_SolverSettings#Linear_System.md)** is *Iterative*.

-    **Eigen System Select**   * Selection of which eigenvalues are computed. Note that the selection of *Largest\** cause an infinite run for recent Elmer solver (as of August 2022).

-    **Eigen System Tolerance**   * Convergence tolerance for iterative eigensystem solve. The default is 100 times the **[Linear Tolerance](FEM_SolverElmer_SolverSettings#Linear_System.md)**.

-    **Eigen System Values**   * The number of the highest eigenmode that should be calculated.

Equation   *

-    **Plane Stress**   * Computes solution according to the plane stress situation. Applies only for 2D geometry.

## Constraint Information 

The elasticity equation takes the following constraints into account if they are set   *

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width   *32px;"> [Constraint fixed](FEM_ConstraintFixed.md)
-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width   *32px;"> [Constraint displacement](FEM_ConstraintDisplacement.md)
-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width   *32px;"> [Constraint force](FEM_ConstraintForce.md)
-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width   *32px;"> [Constraint pressure](FEM_ConstraintPressure.md)
-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width   *32px;"> [Constraint self weight](FEM_ConstraintSelfWeight.md)
-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width   *32px;"> [Constraint initial temperature](FEM_ConstraintInitialTemperature.md)

### Note

For all above constraints it is important that they act on a face. Constraints set to lines or vertices are not recognized by the Elmer solver.

## Eigenmode Analysis 

To perform an eigenmode analysis (calculation if the eigenmodes and eigenfrequencies), you need to

1.  Set **Eigen Analysis**   * to *true*
2.  Set **Displace Mesh**   * to *false*
3.  Set **Eigen System Values**   * to the highest number of eigenmodes you are interested in. The smaller this number the shorter the solver runtime since higher modes can be omitted from computation.
4.  Add a [constraint fixed](FEM_ConstraintFixed.md) and set at least one face of the body as fixed.
5.  Run the solver.

**Note**   * If you use more than one CPU core for the solver (Also note that iterative solving is not recommended for eigenmode analysis. Therefore either only use one CPU core or install the *MUMPS* module to Elmer.

## Buckling Analysis 

To perform a buckling analysis, you need to do the same as for an [Eigenmode Analysis](#Eigenmode_Analysis.md), and additionally   *

-   Set **Stability Analysis** to *true*

## Results

The available results depend on the [solver settings](#Solver_Settings.md). If none of them was set to *true*, only the displacement is calculated. Otherwise also the corresponding results will be available. If **Eigen Analysis** was set to *true* all results will be available for every calculated eigenmode.

If **Eigen Analysis** was set to *true*, the eigenfrequencies are output at the end of the solver log in the solver dialog and also in the document **SolverElmerOutput** that will be created in the tree view after the solver has finished.

**Note   *** The eigenmode displacement $\vec{d}$ vector has an arbitrary value since the result is

$\quad
\vec{d} = c\cdot\vec{u}$

whereas $\vec{u}$ is the eigenvector and $c$ is a complex number.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationElasticity/de
