# CfdOF Features
## Current Features 

The CfdOF Workbench currently has the following features.

### Flow physics 

-   Incompressible, laminar flow (simpleFoam, pimpleFoam)
-   Support for various RANS, LES and DES turbulent flow models
-   Incompressible free-surface flow (interFoam, multiphaseInterFoam)
-   Compressible buoyant flow (buoyantSimpleFoam, buoyantPimpleFoam)
-   High-speed compressible flow ([HiSA](https://hisa.gitlab.io/))
-   Porous regions and porous baffles
-   Basic material database
-   Flow initialisation with a potential solver
-   Solution of arbitrary passive scalar transport functions

### Meshing

-   Cut-cell Cartesian meshing with boundary layers (cfMesh)
-   Cut-cell Cartesian meshing with baffles (snappyHexMesh)
-   Tetrahedral meshing using Gmsh, including conversion to polyhedral dual mesh
-   Post-meshing check mesh
-   Support for dynamic mesh adaptation for supported solvers

### Post-processing and monitoring 

-   Postprocessing using Paraview
-   Basic support for force-based function objects (Forces, Force Coefficients)
-   Basic support for probes

### Other features 

-   Runs on Windows 7-11 and Linux
-   Unit/regression testing
-   Case builder using an extensible template structure
-   Macro scripting
-   Support for distributed parallel (cluster) runs via mpiexec & \--hostfile





{{CfdOF Tools navi}}



---
⏵ [documentation index](../README.md) > [CfdOF](Category_CfdOF.md) > CfdOF Features
