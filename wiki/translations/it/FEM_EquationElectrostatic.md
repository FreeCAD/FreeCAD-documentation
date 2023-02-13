# FEM EquationElectrostatic/it
---
- GuiCommand:/it   Name:FEM_EquationElectrostatic   Name/it:Equazione elettrostatica   Icon:Fem-equation-electrostatic.svg   MenuLocation: Solve → Equazione elettrostatica   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial/it|Tutorial FEM](FEM_Workbench/it___FEM]].md)---


</div>


<div class="mw-translate-fuzzy">

Da fare


</div>

For info about the math of the equation, see the [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Electrostatics*.

## Usage

1.  After adding an Elmer solver as described [here](FEM_SolverElmer#Equations.md), select it in the [tree view](Tree_view.md).
2.  Now either use the toolbar button <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> or the menu **Solve → Electromagnetic Equations → Electrostatic equation**.
3.  Change the [equation\'s solver settings](#Solver_Settings.md) or the [general solver settings](FEM_SolverElmer_SolverSettings.md) if necessary.

## Solver Settings 

For the general solver settings, see the [Elmer solver settings](FEM_SolverElmer_SolverSettings.md).

The electrostatic equation provides these special settings:

-    **Calculate Capacitance Matrix**: Calculates the capacitance matrix. The matrix contains the the point charges of the mesh knots.

-    **Calculate Electric Energy**: Calculates the [electric potential energy](https://en.wikipedia.org/wiki/Electric_potential_energy).

-    **Calculate Electric Field**: Calculates the [electric field](https://en.wikipedia.org/wiki/Electric_field).

-    **Calculate Electric Flux**: Calculates the [electric flux](https://en.wikipedia.org/wiki/Electric_flux).

-    **Calculate Surface Charge**: Calculates the [surface charge](https://en.wikipedia.org/wiki/Surface_charge).

-    **Capacitance Matrix Filename**: File in which the capacitance matrix is being saved. It is only used if **Calculate Capacitance Matrix** is set to *true*.

-    **Constant Weights**: If constant weighting for results is used.

-    **Potential Difference**: Potential difference in Volt for which the capacitance is calculated. It is only used if **Calculate Capacitance Matrix** is set to *false*. Therefore in fact this setting specifies the voltage between the electrodes of a simple capacitor. Note that the given voltage has to be consistent with the potentials defined in the boundary conditions.

## Constraint Information 

The electrostatic equation takes the following constraints into account if they are set:

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [Electrostatic potential constraint](FEM_ConstraintElectrostaticPotential.md)
-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:24px;"> [Constant vacuum permittivity](FEM_ConstantVacuumPermittivity.md)

### Note

Except for calculations in 2D, for <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [electrostatic potential constraints](FEM_ConstraintElectrostaticPotential.md) it is important that they act on a face or body. Constraints for 3D set to lines or vertices are not recognized by the Elmer solver.

## Results

The available results depend on the [solver settings](#Solver_Settings.md). If none of the **Calculate *** settings was set to *true*, only the electric force density and the electric potential are calculated. Otherwise also the corresponding results will be available.

The possible results are:

-   Electric energy density in $\rm J/m^3$
-   Electric field in $\rm V/m$
-   Electric flux in $\rm A\cdot s/m^2$
-   Electric force density in $\rm N/m^2$
-   Potential in $\rm V$
-   Potential loads in $\rm C$


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationElectrostatic/it
