# FEM CalculiX
## Introduction

This page collects information on the [CalculiX](http://www.calculix.de/) finite element solver, the default solver in the <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM Workbench](FEM_Workbench.md) for structural and thermo-mechanical analysis. Depending on the operating system you are working with, you\'ll need to install CalculiX before running your first simulation. Please see [FEM Install](FEM_Install.md).

The solver is able to do linear and non-linear calculations, for static, dynamic, and thermal problems. The solver operates on an Abaqus-like input file (`.inp`), which means it can be used with different pre-processors that support this format. The program includes its own graphical preprocessor which, however, is not used by FreeCAD, only the solver itself.

CalculiX is designed to run on Unix platforms like Linux and Irix computers but also on MS-Windows. CalculiX was developed by engineers from MTU Aero Engines, Munich, Germany, to assist them in designing machinery such as jet turbines. The software is currently released to the public on the terms of the GPL version 2.

## Integration with FreeCAD 

Interaction between the [FEM Workbench](FEM_Workbench.md) and CalculiX is done through writing and reading text files. The sequence of operations is as follows:

1.  A CalculiX input file is created with details required to run the simulation
2.  The CalculiX solver is started with this input file
3.  The output from the solver is logged
4.  The output files from the solver are read, if they are available

The [FEM Control Solver](FEM_SolverControl.md) tool manages the whole process. User interaction in the process is possible.

## Preprocessing interface 

The input file that CalculiX uses can be prepared and edited before the solver is started. The units used in the input file are independent of the units set in FreeCAD; they will always be millimeters (mm) and Newton (N).


**(ToDo: check this. What happens with the mesh if inch is used in FreeCAD? As density was introduced, with this we have kg and s and no longer N?! how about this?!)**

The CalculiX interface supports the following objects:

### FEM Elements 

-   Tet4 and Tet10
-   S3 and S6
-   B31 and B32
-   and those described in [FEM Mesh CalculiX](FEM_Mesh_CalculiX.md)

### Analysis

-   Linear and nonlinear static analysis
-   Frequency analysis
-   Linear buckling analysis
-   Coupled thermal-structural analysis

### Materials

-   Linear elastic isotropic materials (uniformity in all directions)
-   Plasticity with isotropic hardening

## Postprocessing interface 

The FEM Workbench loads CalculiX results into a [result object](FEM_ResultShow.md) which will contain:

-   Displacements
-   Stresses
-   Strains
-   Equivalent plastic strain (PEEQ) -- if nonlinear material was used
-   Temperature -- for thermomechanical analysis

FreeCAD reads results from ***.frd** file which was created by CalculiX. If these results contain multiple time steps, each time step is imported to FreeCAD as a new result object. Same behavior applies for Frequency or Buckling analysis with multiple eigenvalues.

Reaction forces can be found in *ccx_dat_file* which contains reaction force components (fx, fy, fz) for each fixed boundary condition and for each displacement boundary condition which constrains translation degrees of freedom.

## Related

-   [FEM Mesh CalculiX](FEM_Mesh_CalculiX.md)
-   [CalculiX preferences](FEM_Preferences#CalculiX.md) dialog menu in the FEM Workbench preferences menu

 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [Developer](Category_Developer.md) > [FEM](Category_FEM.md) > FEM CalculiX
