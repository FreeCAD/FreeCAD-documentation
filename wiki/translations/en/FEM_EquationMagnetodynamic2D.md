---
- GuiCommand:
   Name:FEM EquationMagnetodynamic2D
   MenuLocation:Solve → Electromagnetic Equations → Magnetodynamic2D equation
   Workbenches:[FEM](FEM_Workbench.md)
   Version:1.0
   SeeAlso:[Magnetodynamic equation](FEM_EquationMagnetodynamic.md)
---

# FEM EquationMagnetodynamic2D/en

This equation performs analyses using a 2D version of the [Maxwell\'s equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations) when the unknown is the z-component (or φ-component).

For info about the math of the equation, see the [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 2D*.

For more general analyses in 3D using the Maxwell\'s equations FreeCAD supports Elmer\'s [Magnetodynamic equation](FEM_EquationMagnetodynamic.md). Nevertheless, if it is possible to perform the analysis in 2D, this is recommended since the math behind this is then more simple and the calculation time is therefore faster.

## Usage

1.  After adding an Elmer solver as described [here](FEM_SolverElmer#Equations.md), select it in the [tree view](Tree_view.md).
2.  Now either use the toolbar button <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:24px;"> or the menu **Solve → Electromagnetic Equations → Magnetodynamic2D equation**.
3.  Change the [equation\'s solver settings](#Solver_Settings.md) or the [general solver settings](FEM_SolverElmer_SolverSettings.md) if necessary.

## Solver Settings 

For the general solver settings, see the [Elmer solver settings](FEM_SolverElmer_SolverSettings.md).

The magnetodynamic 2D equation provides these special settings:

-    **Angular Frequency**: The harmonic actuation frequency. It only used if **Is Harmonic** is set to *true*.

-    **Calculate Current Density**: Calculates the [current density](https://en.wikipedia.org/wiki/Current_density).

-    **Calculate Electric Field**: Calculates the [Electric vector field](https://en.wikipedia.org/wiki/Electric_field).

-    **Calculate Elemental Fields**: Calculates the electromagnetic fields for every mesh element. This is useful to see discontinuities in meshes.**Note**: at the moment FreeCAD cannot display these results properly. Therefore it is at the moment of no practical use.

-    **Calculate Harmonic Loss**: Calculates the linear and quadratic harmonic power loss. See the [Elmer models manual](https://www.elmerfem.org/blog/documentation/), section *Loss Estimation Using the Fourier Series* for details

-    **Calculate Joule Heating**: Calculates the [Joule heating](https://en.wikipedia.org/wiki/Joule_heating).

-    **Calculate Magnetic Strength**: Calculates the [Magnetic field strength](https://en.wikipedia.org/wiki/Magnetic_field).

-    **Calculate Maxwell Stress**: Calculates the [Maxwell stress tensor](https://en.wikipedia.org/wiki/Maxwell_stress_tensor) field.

-    **Calculate Nodal Fields**: Calculates the fields for every mesh node. The default is *true*. If no other **Calculate *** is set to *true*, it only calculates the magnetic flux density.

-    **Calculate Nodal Forces**: Calculates the forces for every mesh node. The results can be used for further mechanical analysis.

-    **Calculate Nodal Heating**: Calculates the Joule heating scalar field for every mesh node.

-    **Is Harmonic**: If the driving force is harmonically actuated (AC current). If set to *true*, **Angular Frequency** must have a value \> 0.

## Constraint Information 

The magnetodynamic 2D equation takes the following constraints into account if they are set:

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [Electrostatic potential constraint](FEM_ConstraintElectrostaticPotential.md)
-   <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:24px;"> [Current density constraint](FEM_ConstraintCurrentDensity.md)
-   <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:24px;"> [Magnetization constraint](FEM_ConstraintMagnetization.md)
-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:24px;"> [Constant vacuum permittivity](FEM_ConstantVacuumPermittivity.md)

## Results

The available results depend on the [solver settings](#Solver_Settings.md). If none of the **Calculate *** settings was set to *true*, only the electric electric potential (called **av** in the results) is calculated. Otherwise also the corresponding results will be available.

The possible results are:

-   Current density in $\rm A/m^2$
-   Electric field vector values in $\rm V/m$
-   Harmonic power loss in $\rm W$
-   Magnetic flux density in $\rm T$
-   Maxwell stress tensor values in $\rm As/m^3$
-   Magnetic field strength in $\rm A/m$
-   Nodal force in $\rm N$
-   Joule heating in $\rm J$
-   Potential in $\rm V$





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationMagnetodynamic2D/en
