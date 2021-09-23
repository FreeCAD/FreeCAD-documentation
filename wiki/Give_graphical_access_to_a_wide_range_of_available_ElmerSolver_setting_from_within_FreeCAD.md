# Give graphical access to a wide range of available ElmerSolver setting from within FreeCAD
This page is dedicated to the description of the [Google Summer of Code 2017](GSoC2017.md) project idea regarding setting up full-fledged multiphysics simulations from within FreeCAD while using ElmerFEM as external solver.

## Outline

This GSoC project aims at a full integration of ElmerSolver into FreeCAD. Since the graphical user interface of ElmerFEM called ElmerGUI is no more active developed, is the intension to use FreeCAD for geometrical modeling and extended preprocessing and ElmerFEM as external solver.

The goal of this specific project is to implement all necessary objects to completely handle the set-up and execution of multiphysics simulations from within FreeCAD. To handle the variety of solver-settings including boundary- and initial conditions available for ElmerSolver, one has to implement new objects, classes as well as input-GUI "from scratch". Using Projects like ElmerSalomeModule (https://github.com/physici/ElmerSalomeModule) as reference point the student has to take care of a wide range of available interwoven settings and preconditions for running multiphysics simulations in FreeCAD using ElmerFEM.

## Details

1.  Get familiar with FreeCAD, how 3D-models are built up, and how elements of this models can be access via python-console.
2.  Get familiar with ElmerSolver, ElmerGUI to set up basic simulation models and solver-input-files.
3.  Get deep understanding of how ElmerSalomeModule works and how all available settings of ElmerSolver are read from its edf-files.
4.  The student has to be understand pre- and postprocessing related to numeric simulations.
5.  Existing solver objects for other solvers like CalculiX have to be adopted to handle Elmer-specific settings.
6.  Clear structured and easy to use GUI elements for all available boundary- and initial conditions have to be introduced.
7.  GUI-elements have to be introduced to handle all necessary setting for the solver-input-file.
8.  The structure of solver input-files for ElmerSolver has to be known very well and a proper generation has to implemented efficiantly and failsafe.
9.  All mesh related definitions is done using existing tools in FreeCAD's FEM-workbench. For use with ElmerSolver is the mesh exported automated as .unv and processed with ElmerGrid.
10. The evaluation of the simulation output in done in Paraview.

## Expected Outcome 

1.  A easy to use dialog for handling as many Elmer-related settings as possible for building multiphysics simulations including the set-up of boundary conditions and material definitions
2.  Test runs ensuring the functionality
3.  Documentation and tutorials for the workflow

## Future Possibilities 

Since the integration of external solvers is a huge area in constant evolution, the work done in this GSoC will only cover a small part of it. But if the bases are done right, extending them will be easy and could develop very far.

## Project Properties 

### Skills

-   Programming language Python, C++
-   Deep understanding of the APIs from FreeCAD and PyQt as well as the structure of solver-input-files for ElmerSolver
-   Comprehensive knowledge of Python for processing structured text in form of solver-input-file
-   Knowledge of 3D modeling, basics of numerics simulations and computational geometry is a plus

### Difficulty

Hard

### Additional Information 

[Category:Google Summer of Code](Category:Google_Summer_of_Code.md)

---
[documentation index](../README.md) > Give graphical access to a wide range of available ElmerSolver setting from within FreeCAD
