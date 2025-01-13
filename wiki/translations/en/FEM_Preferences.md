# FEM Preferences/en
## Introduction

The preferences for the <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM Workbench](FEM_Workbench.md) can be found in the [Preferences Editor](Preferences_Editor.md). In the menu select **Edit → Preferences...** and then **<img src="images/Workbench_FEM.svg" width=16px> FEM**. This group is only available if the FEM Workbench has been loaded in the current FreeCAD session.

There are seven pages: [General](#General.md), [Gmsh](#Gmsh.md), [CalculiX](#CalculiX.md), [Elmer](#Elmer.md), [Mystran](#Mystran.md), [Z88](#Z88.md) and [Netgen](#Netgen.md). All pages apart from the first control how FEM interacts with external meshers and solvers.

The currently supported external solvers are:

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [CalculiX](FEM_SolverCalculixCxxtools.md)
-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer.md)
-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Mystran](FEM_SolverMystran.md)
-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Z88](FEM_SolverZ88.md)

## General

<img alt="" src=images/Preferences_FEM_Page_General.png  style="width:350px;">

On this page you can specify the following:

+++
| Name                                                                                   | Description                                                                                                               |
+========================================================================================+===========================================================================================================================+
|                                                                         | In what directory the mesh and solver files should be stored                                                              |
| **Working directory**                                                      |                                                                                                                           |
|                                                                                     |                                                                                                                           |
+++
|                                                                         | If there are several meshes they will be grouped                                                                          |
| **Create mesh groups for analysis reference shapes (highly experimental)** |                                                                                                                           |
|                                                                                     |                                                                                                                           |
+++
|                                                                         | Existing [Result objects](FEM_ResultShow.md) will be kept, otherwise overwritten by a new solver run              |
| **Keep results on calculation re-run**                                     |                                                                                                                           |
|                                                                                     |                                                                                                                           |
+++
|                                                                         | If checked, the [Show result](FEM_ResultShow.md) dialog is opened with the last used dialog settings              |
| **Restore result dialog settings**                                         |                                                                                                                           |
|                                                                                     |                                                                                                                           |
+++
|                                                                         | The constraints will be hidden in the model view when the [Show result](FEM_ResultShow.md) dialog is opened       |
| **Hide analysis features when opening result dialog**                      |                                                                                                                           |
|                                                                                     |                                                                                                                           |
+++
|                                                                         | Default solver to be added when adding an [Analysis container](FEM_Analysis.md). (<small>(v0.21)</small> ) |
| **Default solver**                                                         |                                                                                                                           |
|                                                                                     |                                                                                                                           |
+++

## Gmsh

<img alt="" src=images/Preferences_FEM_Page_Gmsh.png  style="width:350px;">

On this page you can specify the following:

+++
| Name                                               | Description                                                                                                           |
+====================================================+=======================================================================================================================+
|                                     | If checked, FreeCAD will look for the binary of [Gmsh](FEM_MeshGmshFromShape.md) in known (usual) directories |
| **Search in known binary directories** |                                                                                                                       |
|                                                 |                                                                                                                       |
+++
|                                     | The path to the binary of [Gmsh](FEM_MeshGmshFromShape.md)                                                    |
| **Gmsh binary path**                   |                                                                                                                       |
|                                                 |                                                                                                                       |
+++
|                                     | Log verbosity level: Silent, Errors, Warnings, Direct, Information, Status or Debug. <small>(v1.1)</small>     |
| **Log verbosity**                      |                                                                                                                       |
|                                                 |                                                                                                                       |
+++

## CalculiX

<img alt="" src=images/Preferences_FEM_Page_CalculiX.png  style="width:350px;">

On this page you can specify the following:

+++
| Name                                                      | Description                                                                                                                                                                         |
+===========================================================+=====================================================================================================================================================================================+
|                                            | If checked, FreeCAD will look for the binary of [CalculiX](FEM_SolverCalculixCxxtools.md) in known (usual) directories                                                      |
| **Search in known binary directories**        |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | The path to the binary of [CalculiX](FEM_SolverCalculixCxxtools.md)                                                                                                         |
| **ccx binary path**                           |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | If checked, a built-in \*.inp file editor with syntax highlighting is used when editing CalculiX input decks.                                                                       |
| **Use internal editor for *.inp files**       |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | The path to the external \*.inp file editor.                                                                                                                                        |
| **External editor**                           |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | If checked, multiple \*.inp files are written and the main input deck uses the \*INCLUDE keywords to reference the other ones. If unchecked, a single large \*.inp file is written. |
| **Split writing of *.inp**                    |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | Default analysis type: Static, Frequency, Thermomech, Check Mesh or Buckling.                                                                                                       |
| **Type**                                      |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | Number of physical processor cores to use for parallel computing.                                                                                                                   |
| **Number of CPU's to use**                    |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | Default matrix solver: Default, PaStiX, Pardiso, Spooles equation solver, Iterative Scaling or Cholesky iterative solver.                                                           |
| **Matrix solver**                             |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | If checked, geometric nonlinearity is included by default.                                                                                                                          |
| **Non-linear geometry**                       |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | If checked, uses non-default solver controls (not recommended in most cases).                                                                                                       |
| **Time incrementation control parameter**     |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | Maximum number of increments within an analysis step.                                                                                                                               |
| **Maximum number of iterations**              |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | Initial time increment size (can be changed by the solver if automatic incrementation is used).                                                                                     |
| **Time Initial Step**                         |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | Total simulated time.                                                                                                                                                               |
| **Time End**                                  |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | Minimum allowable time increment size.                                                                                                                                              |
| **Time Minimum Step**                         |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | Maximum allowable time increment size.                                                                                                                                              |
| **Time Maximum Step**                         |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | If checked, results for 1D and 2D elements are displayed using 3D representation by default.                                                                                        |
| **Beam, shell element 3D output format**      |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | If checked, thermomechanical analyses are of steady-state type by default.                                                                                                          |
| **Analysis type (transient or steady state)** |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | Default number of requested eigenmodes in frequency analyses.                                                                                                                       |
| **Eigenmode number**                          |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | Default upper limit of evaluated eigenfrequencies in frequency analyses.                                                                                                            |
| **High frequency limit**                      |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++
|                                            | Default lower limit of evaluated eigenfrequencies in frequency analyses.                                                                                                            |
| **Low frequency limit**                       |                                                                                                                                                                                     |
|                                                        |                                                                                                                                                                                     |
+++

## Elmer

<img alt="" src=images/Preferences_FEM_Page_Elmer.png  style="width:350px;">

On this page you can specify the following:

+++
| Name                                                            | Description                                                                                                                                                                                                                                   |
+=================================================================+===============================================================================================================================================================================================================================================+
|                                                  | If checked, FreeCAD will look for the binary of the grid writer utility of the [Elmer](FEM_SolverElmer.md) in known (usual) directories                                                                                               |
| **ElmerGrid: Search in known binary directories**   |                                                                                                                                                                                                                                               |
|                                                              |                                                                                                                                                                                                                                               |
+++
|                                                  | The path to the binary of the grid writer utility of the [Elmer](FEM_SolverElmer.md)                                                                                                                                                  |
| **ElmerGrid binary path**                           |                                                                                                                                                                                                                                               |
|                                                              |                                                                                                                                                                                                                                               |
+++
|                                                  | If checked, FreeCAD will look for the solver binary of [Elmer](FEM_SolverElmer.md) in known (usual) directories                                                                                                                       |
| **ElmerSolver: Search in known binary directories** |                                                                                                                                                                                                                                               |
|                                                              |                                                                                                                                                                                                                                               |
+++
|                                                  | The path to the solver binary of [Elmer](FEM_SolverElmer.md)                                                                                                                                                                          |
| **ElmerSolver binary path**                         |                                                                                                                                                                                                                                               |
|                                                              |                                                                                                                                                                                                                                               |
+++
|                                                  | The number of CPU cores that will be used to perform the solving. **Important:** Elmer divides the mesh into portions. The number of portions is equal to the number of CPU cores used. This can result in side-effects:                      |
| **CPU cores to be used**                            |                                                                                                                                                                                                                                               |
|                                                              | -   Depending on your mesh a smaller number of CPU cores can run faster than using more cores.                                                                                                                                                |
|                                                                 | -   In some cases using e.g. 12 cores does not converge while 8 cores will work fine. The reason is that at some point the mesh portions become too small.                                                                                    |
|                                                                 |                                                                                                                                                                                                                                               |
|                                                                 | So it is often necessary to adjust the number of cores, depending on the mesh.                                                                                                                                                                |
|                                                                 |                                                                                                                                                                                                                                               |
|                                                                 | **Known limitation:** For some simulation types you first need to install Elmer modules to enable multi-threading. Check the Elmer report for info about this. A typical case is that for direct solving one has to install the MUMPS module. |
+++
|                                                  | The mesh volume regions processed by each CPU core will be merged to make the volume boundaries invisible.                                                                                                                                    |
| **Filter results**                                  |                                                                                                                                                                                                                                               |
|                                                              |                                                                                                                                                                                                                                               |
+++
|                                                  | If checked, binary results format is used. Otherwise, ASCII format is used. Binary format may cause lack of results due to a bug. <small>(v1.1)</small>                                                                                |
| **Use binary format**                               |                                                                                                                                                                                                                                               |
|                                                              |                                                                                                                                                                                                                                               |
+++
|                                                  | If checked, the index of geometric entities is saved in the results. <small>(v1.1)</small>                                                                                                                                             |
| **Save geometry IDs**                               |                                                                                                                                                                                                                                               |
|                                                              |                                                                                                                                                                                                                                               |
+++

## Mystran

<img alt="" src=images/Preferences_FEM_Page_Mystran.png  style="width:350px;">

On this page you can specify the following:

+++
| Name                                               | Description                                                                                                              |
+====================================================+==========================================================================================================================+
|                                     | If checked, FreeCAD will look for the binary of the [Mystran](FEM_SolverMystran.md) in known (usual) directories |
| **Search in known binary directories** |                                                                                                                          |
|                                                 |                                                                                                                          |
+++
|                                     | The path to the binary of the [Mystran](FEM_SolverMystran.md)                                                    |
| **Mystran binary path**                |                                                                                                                          |
|                                                 |                                                                                                                          |
+++
|                                     |                                                                                                                          |
| **Write comments to input file**       |                                                                                                                          |
|                                                 |                                                                                                                          |
+++

## Z88

<img alt="" src=images/Preferences_FEM_Page_Z88.png  style="width:350px;">

On this page you can specify the following:

+++
| Name                                               | Description                                                                                                                                                                                                               |
+====================================================+===========================================================================================================================================================================================================================+
|                                     | If checked, FreeCAD will look for the binary named *z88r* of the [Z88 solver](FEM_SolverZ88.md) in known (usual) directories                                                                                      |
| **Search in known binary directories** |                                                                                                                                                                                                                           |
|                                                 |                                                                                                                                                                                                                           |
+++
|                                     | The path to the binary named *z88r* of the [Z88 solver](FEM_SolverZ88.md)                                                                                                                                         |
| **z88r binary path**                   |                                                                                                                                                                                                                           |
|                                                 |                                                                                                                                                                                                                           |
+++
|                                     | The solver method used by the [Z88 solver](FEM_SolverZ88.md) for new simulations.                                                                                                                                 |
| **Solver method**                      |                                                                                                                                                                                                                           |
|                                                 |                                                                                                                                                                                                                           |
+++
|                                     | This is relevant when the solver method *Simple Cholesky* is used. After starting the solver, it might tell you that you need to increase the *MAXGS* value. In this case increase the max places and re-run the solver.  |
| **Max places in stiffness matrix**     |                                                                                                                                                                                                                           |
|                                                 |                                                                                                                                                                                                                           |
+++
|                                     | This is relevant when one of the iterative solver methods is used. After starting the solver, it might tell you that you need to increase the *MAXKOI* value. In this case increase the max places and re-run the solver. |
| **Max places in coincidence vector**   |                                                                                                                                                                                                                           |
|                                                 |                                                                                                                                                                                                                           |
+++

## Netgen

<img alt="" src=images/Preferences_FEM_Page_Netgen.png  style="width:350px;">

On this page you can specify the following:

+++
| Name                          | Description                                                                                                                                                                                                                                                                                             |
+===============================+=========================================================================================================================================================================================================================================================================================================+
|                | If checked, the legacy [Netgen](FEM_MeshNetgenFromShape.md) implementation is used by FreeCAD FEM. This might be needed for users (mostly with older and Windows computers) who can\'t install the Netgen Python bindings necessary for the new implementation. (<small>(v1.0)</small> ) |
| **Legacy Netgen** |                                                                                                                                                                                                                                                                                                         |
|                            |                                                                                                                                                                                                                                                                                                         |
+++





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [FEM](Category_FEM.md) > FEM Preferences/en
