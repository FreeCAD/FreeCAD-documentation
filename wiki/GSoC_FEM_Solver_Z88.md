# GSoC FEM Solver Z88
This page is dedicated to the description of the Google Summer of Code project idea regarding extending FEM solver Z88OS.

**Obsolete**: This page has been moved to <https://github.com/FreeCAD/FreeCAD/issues/8559>

## Outline

FreeCAD is not only a traditional CAD platform but also aims at providing general engeneering functionality. One of the most valuable design tools for modern product development is the finite element method. It provides advanced means for design analysis, stress tests and optimisation. Over the last two years a FEM workbench in FreeCAD has been developed based on the CalculiX solver and already reached a usable state in the 0.16 release. However, since CalculiX has neither real Shell nor real Beam elements, CalculiX has limitations in the regard of these element types. This was the main reason to start an implementation of an additional solver for the FreeCAD FEM workbench. Z88OS was choosen, since it is OpenSource and thus runs on all major plattforms and has real Beam and Shell elements. The solver Z88OS has been integrated in FreeCAD FEM already. But only very limited parameter are supported at the moment. Only fixed constraints in main axis directions and simple node loads are supported on the pre processing side. On the contrary the post processing only the displacements are read into FreeCAD FEM. To really be able to use Z88 as an additional solver more of his capabilities need to be supported by FreeCAD.

The GSoC project aims to exactly do this. On pre processing side of FreeCAD a lot of constraints and boundary conditions are supported by FEM and CalculiX solver. Most of them should be ported to Z88 too. On post processing side the FreeCAD FEM result object supports a wide range of result types as well as viewing them by the use of sophisticated VTK post processing tools. An implementation should be made to read more Z88 results into FreeCAD result object. Furthermore most Z88 solver adjustments are hard coded into FreeCAD FEM. They should be changed in a way they could be changed during run time of FreeCAD FEM.

## Details

1.  Get familiar with FreeCAD FEM workbench its capabilities and its architecture. Furthermore get familiar with Z88OS and its interface text files for pre- and post processing. It is important to have a good understanding of all involved components to be able to make the needed extensions.
2.  Post processing: Extend the importZ88result module to read stress and strains from Z88 result files and add them to the FreeCAD result object.
3.  Pre processing: Implement Z88 input file writing for all three element dimensions (beam, shell, volume) for the following constraints of FreeCAD FEM: fixed, force, pressure, self weight, displacement.
4.  Solver: extend the FreeCAD FEM solver object by FreeCAD properties to hold the the attributes which could be used to make the needed adjustments at Z88 solver binary.




1.  Advanced: add the free-ware solver Z88Aurora (not OpenSource, but free of license fee) as another possibility in FreeCAD FEM in addition to Z88OS. Z88Aurora supports much more constraints and analysis types than Z88OS

## Expected Outcome 

1.  Fully functional advanced postprocessing in FreeCAD based on VTK
2.  Unit tests ensuring the functionality
3.  Documentation and tutorials for post processing

## Future Possibilities 

If this project is finished successfully futher work on the FEM workbench can be done. Advancing the preprocessing with better control over the meshing process come to mind, or integrating different solvers for other analysis types. Also calulix implementation can be advanced, for example allowing nonelinear calculations.

## Project Properties 

### Skills

-   Programming language Python
-   Deep understanding and use of APIs from FreeCAD and Z88OS
-   Knowledge of FEM pre- and postprocessing workflows and needs

### Difficulty

Easy-Medium

### Project size 

175h

### Additional Information



---
⏵ [documentation index](../README.md) > GSoC FEM Solver Z88
