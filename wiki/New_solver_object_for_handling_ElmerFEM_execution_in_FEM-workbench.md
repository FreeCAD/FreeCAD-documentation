# New solver object for handling ElmerFEM execution in FEM-workbench
This page is dedicated to the description of the [Google Summer of Code 2017](GSoC2017.md) project idea regarding accessing of ElmerFEM from within FreeCAD.

## Outline

This GSoC project aims at building a first bridge between FreeCAD and ElmerFEM. The intension is to use FreeCAD for geometrical modeling and basic preprocessing and ElmerFEM as external solver, since the graphical user interface of ElmerFEM called ElmerGUI is no more active developed.

A new solver object has to be implemented based on existing objects. The execution of ElmerSolver is handled by this new solver-object from within FreeCAD. All solver-specific information is provided by an externally generated solver-input-file which has to be selected with a proper graphical user interface. The definition of boundaries and domains inside the model is done by using existing FEMMesh-Groups while presenting the user supportive information extracted from the provided solver-input-file.

## Details

1.  Get familiar with FreeCAD, how 3D-models are built up, and how elements of this models can be access via python-console.
2.  Get familiar with ElmerSolver, ElmerGUI to set up basic simulation models and solver-input-files.
3.  The student has to be familiar with pre- and postprocessing related to numeric simulations.
4.  Existing solver objects for other solvers like CalculiX have to be adopted to handle Elmer-specific settings.
5.  All mesh related definitions is done using existing tools in FreeCAD's FEM-workbench.
6.  The evaluation of the simulation output in done in Paraview.
7.  Basic GUI-elements have to be introduced to handle the externally provided solver-input-file for running the simulation with ElmerSolver.

## Expected Outcome 

1.  A easy to use solver-object and self-explaining dialogs for handling all external Elmer-related processes
2.  Test runs ensuring the functionality
3.  Documentation and tutorials for the workflow

## Future Possibilities 

Since the integration of external solvers is a huge area in constant evolution, the work done in this GSoC will only cover a small part of it. But if the bases are done right, extending them will be easy and could develop very far.

## Project Properties 

### Skills

-   Programming language Python
-   Good understanding and use of APIs from FreeCAD, and PyQt as well as the structure of solver-input-files for ElmerSolver
-   Knowledge of 3D modeling, basics of numerics simulations and computational geometry is a plus

### Difficulty

Easy

### Additional Information 

_

---
[documentation index](../README.md) > New solver object for handling ElmerFEM execution in FEM-workbench
