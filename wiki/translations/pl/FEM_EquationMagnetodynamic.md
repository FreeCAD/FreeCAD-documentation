---
- GuiCommand:
   Name:FEM EquationMagnetodynamic
   MenuLocation:Solve → Electromagnetic Equations → Magnetodynamic equation
   Workbenches:[FEM](FEM_Workbench.md)
   Version:1.0
   SeeAlso:[Magnetodynamic 2D equation](FEM_EquationMagnetodynamic2D.md)
---

# FEM EquationMagnetodynamic/pl


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

This equation perform analyses using the [Maxwell\'s equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

For info about the math of the equation, see the [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D*.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

If it is possible to calculate in 2D, simpler math can be used resulting in faster solving times. For 2D, FreeCAD supports therefore Elmer\'s [Magnetodynamic 2D equation](FEM_EquationMagnetodynamic2D.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Usage


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  After adding an Elmer solver as described [here](FEM_SolverElmer#Equations.md), select it in the [tree view](Tree_view.md).
2.  Now either use the toolbar button <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:24px;"> or the menu **Solve → Electromagnetic Equations → Magnetodynamic equation**.
3.  Change the [equation\'s solver settings](#Solver_Settings.md) or the [general solver settings](FEM_SolverElmer_SolverSettings.md) if necessary.
4.  It is recommend to set in the [Linear System solver settings](FEM_SolverElmer_SolverSettings#Linear_System.md) the **Linear Iterative Method** to **BiCGStabl**, the **BiCGstabl Degree** to **4** and **Linear Preconditioning** to **None**. This assures the equation can be solved in most cases. If so, these parameters can be changed if necessary.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Solver Settings 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

For the general solver settings, see the [Elmer solver settings](FEM_SolverElmer_SolverSettings.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The magnetodynamic equation provides these special settings:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Linear System 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-    **Linear System Refactorize**: Refactorizes the system matrix.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Magnetodynamic


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-    **Angular Frequency**: The harmonic actuation frequency. It only used if **Is Harmonic** is set to *true*.

-    **Automated Source Projection BCs**: See Elmer [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D* for info.

-    **FixInput Current Density**: Ensures divergence-freeness of current density.

-    **Is Harmonic**: If the driving force is harmonically actuated (AC current). If set to *true*, **Angular Frequency** must have a value \> 0.

-    **Lagrange Gauge Penalization Coefficient**: See Elmer [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D* for info.

-    **Quadratic Approximation**: Enables second-order approximation of driving current.**Note:** The default order of [Gmsh meshes](FEM_MeshGmshFromShape.md) in FreeCAD is 2nd order. When using 2nd order meshes, it is mandatory to set this option to *true*. Otherwise you will get this error: *ERROR:: GetEdgeBasis: Can\'t handle but linear elements, sorry.*However, for most applications, a 1st order mesh is sufficient. An exception is the case when an Isocontour filter should be applied to visualize the results. In this case using a 2nd order mesh and thus setting **Quadratic Approximation** to *true* is recommended.

-    **Static Conductivity**: See Elmer [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D* for info.

-    **Use Lagrange Gauge**: See Elmer [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D* for info.

-    **Use Piola Transform**: Must be *true* if basis functions for edge element interpolation are selected to be members of optimal edge element family or if second-order approximation is used.

-    **Use Tree Gauge**: See Elmer [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D* for info. Will be ignored if **Use Piola Transform** is *true*.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Results


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

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


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Constraint Information 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The magnetodynamic equation takes the following constraints into account if they are set:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [Electrostatic potential constraint](FEM_ConstraintElectrostaticPotential.md)
-   <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:24px;"> [Current density constraint](FEM_ConstraintCurrentDensity.md)
-   <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:24px;"> [Magnetization constraint](FEM_ConstraintMagnetization.md)
-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:24px;"> [Constant vacuum permittivity](FEM_ConstantVacuumPermittivity.md)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Results 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The available results depend on the [solver settings](#Solver_Settings.md). If none of the **Calculate *** settings was set to *true*, only the electric electric (called **av** in the results) potential is calculated. Otherwise also the corresponding results will be available.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

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


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationMagnetodynamic/pl
