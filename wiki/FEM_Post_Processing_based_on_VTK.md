# FEM Post Processing based on VTK
This page is dedicated to the description of the [Google Summer of Code](Google_Summer_of_Code.md) project idea regarding FEM post processing based on the VTK library.

## Outline

FreeCAD is not only a traditional CAD platform but also aims at providing general engineering functionality. One of the most valuable design tools for modern product development is the finite element method. It provides advanced means for design analysis, stress tests and optimisation. Over the last two years a FEM workbench in FreeCAD has been developed based on the calculix solver and already reached a usable state in the 0.16 release. However, the typical FEM workflow involving Pre and Post processing and the problem solving itself is a huge area and not fully handled by the small community. This is why FreeCAD tries to utilize other open source projects as much as possible in order to minimize work and maximise quality and functionality. This has been done with the SMESH and Netgen components for preprocessing, Calculix for solving. For postprocessing FreeCAD relies on VTK, but the integration currently lacks a few important points.

The GSoC project aims at including the well known and powerful VTK library better into FreeCAD for FEM postprocessing. The basics of this have been laid out in the current implementation, showing the feasibility of the approach. This implementation has to be adopted to the updated SMESH data structure, a python interface has to be designed around it and the whole functionality should be further incorporated into the FEM workbench.

## Details

1.  Get familiar with VTKs dataprocessing capabilities and its architecture. Furthermore get familiar with FreeCADs internal working and the available FEM VTK implementation. It is important to have a good understanding of all involved components to create a welll fitting architecture
2.  Create a new result data structure based on the SMESH mesh datastructure, which internally uses VTK unstructured grid. Add postprocessing functions to this result object and design a python interface around it.
3.  Port the post processing features to the new result object and expose the functionality to the GUI
4.  Extend the current functionality with new filters, with more functions and sources. Futhermore include the available spredsheet and plot module for data analysis of certain filter types
5.  Advanced: Replace the current custom implemented result object and make all postprocessing work unified with vtk
6.  Advanced: Make the preprocessing filters work with the default mesh data structure so that postprocessing can make use of the VTK tools

## Expected Outcome 

1.  Fully functional advanced postprocessing in FreeCAD based on VTK
2.  Unit tests ensuring the functionality
3.  Documentation and tutorials for post processing

## Future Possibilities 

If this project is finished successfully futher work on the FEM workbench can be done. Advancing the preprocessing with better control over the meshing process come to mind, or integrating different solvers for other analysis types. Also calulix implementation can be advanced, for example allowing nonelinear calculations.

## Project Properties 

### Skills

-   Programming language C++
-   Deep understanding and use of APIs from FreeCAD and VTK
-   Knowledge of FEM postprocessing workflows and needs

### Difficulty

Medium

### Additional Information 

[Category:Google Summer of Code](Category:Google_Summer_of_Code.md)

---
[documentation index](../README.md) > FEM Post Processing based on VTK
