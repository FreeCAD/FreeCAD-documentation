# Mapping of main ElmerSolver setting for mechanical simulations
This page is dedicated to the description of the [Google Summer of Code 2017](Google_Summer_of_Code_2017.md) project idea regarding completely setting up mechanical simulations from within FreeCAD while using ElmerFEM as external solver.

## Outline

This GSoC project aims at building a solid bridge between FreeCAD and ElmerFEM. Since the graphical user interface of ElmerFEM called ElmerGUI is no more active developed, is the intension to use FreeCAD for geometrical modeling and extended preprocessing and ElmerFEM as external solver.

The goal of this specific project is to implement all necessary objects to handle a complete simulation set-up and execution for mechanical problems within FreeCAD. Mechanical Constraints like 'fixed' boundaries, 'force', 'described displacement' or 'pressure' have to be realized and mapped to proper GUI elements. This information about constraints has to be processed along with material definitions to generate a solver-input-file for further execution with ElmerSolver. Optional postprocessing is done with the help of Paraview.

## Details

1.  Get familiar with FreeCAD, how 3D-models are built up, and how elements of this models can be access via python-console.
2.  Get familiar with ElmerSolver, ElmerGUI to set up basic simulation models and solver-input-files.
3.  The student has to be familiar with pre- and postprocessing related to numeric simulations.
4.  Existing solver objects for other solvers like CalculiX have to be adopted to handle Elmer-specific settings.
5.  GUI elements for the needed boundary-conditions have to be introduced.
6.  GUI-elements have to be introduced to handle all necessary setting for the solver-input-file
7.  The structure of solver input-files for ElmerSolver has to be known and a proper generation has to implemented.
8.  All mesh related definitions is done using existing tools in FreeCAD's FEM-workbench. For use with ElmerSolver is the mesh exported as .unv and processed with ElmerGrid.
9.  The evaluation of the simulation output in done in Paraview.

## Expected Outcome 

1.  A easy to use solver-object and self-explaining dialogs for handling all Elmer-related settings related to mechanical simulations including boundary conditions and material definitions
2.  Test runs ensuring the functionality
3.  Documentation and tutorials for the workflow

## Future Possibilities 

Since the integration of external solvers is a huge area in constant evolution, the work done in this GSoC will only cover a small part of it. But if the bases are done right, extending them will be easy and could develop very far.

## Project Properties 

### Skills

-   Programming language Python
-   Good understanding and use of APIs from FreeCAD, and PyQt as well as the structure of solver-input-files for ElmerSolver
-   Good Knowledge of Python for processing structured text in form of solver-input-file
-   Knowledge of 3D modeling, basics of numerics simulations and computational geometry is a plus

### Difficulty

Medium

### Additional Information



---
⏵ [documentation index](../README.md) > Mapping of main ElmerSolver setting for mechanical simulations
