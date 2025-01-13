# <img alt="Workbench CfdOF Icon" src=images/Workbench_CfdOF.svg  style="width:64px;"> CfdOF Workbench

## Introduction

The CfdOF Workbench provides a [Computational Fluid Dynamics (CFD)](https://en.wikipedia.org/wiki/Computational_fluid_dynamics) workflow for FreeCAD. This workbench aims to help users set up and run CFD analyses within the FreeCAD modeller, and serves as a front-end (GUI) for the popular OpenFOAM® CFD toolkit ([www.openfoam.org](http://www.openfoam.org), [www.openfoam.com](http://www.openfoam.com)). It guides the user in selecting the relevant physics, specifying the material properties, generating a mesh, assigning boundary conditions and choosing the solver settings before running the simulation. Best practices are specified to maximise the stability of the solvers.

## Features

For a list of current features, please visit the [CfdOF Features](CfdOF_Features.md) page.

## Installation

The CfdOF Workbench can be used on Linux, Windows, and Mac OSX -- although not widely tested. Since the workbench makes use of external solvers, the amount of manual setup will depend on the operating system that you are using.

See [CfdOF Install](CfdOF_Install.md) for instructions on how to install and set up the CfdOF Workbench.

## Workflow

The steps to carry out a Computational Fluid Dynamics are:

1.  Pre-processing: setting up the analysis problem.
    1.  Modelling the geometry: creating the geometry with FreeCAD, or importing it from a different application.
    2.  Creating an analysis.
        1.  Selecting suitable models for the interesting physical and chemical phenomena.
        2.  Defining the fluid properties.
        3.  Specifying the appropriate chemical and physical boundary conditions at cells which coincide with or touch the domain boundary
        4.  Creating and checking the mesh for the geometrical model.
2.  Solving: running an external OpenFOAM® solver from within FreeCAD.
3.  Post-processing: exporting the results so they can be postprocessed with [ParaView](https://www.paraview.org/).

<img alt="Workflow of the CfdOF Workbench" src=images/CfdOF_Workbench_workflow.svg  style="width:600px;">



*Workflow of the CfdOF Workbench*

## Menu: CfdOF 

-   <img alt="" src=images/CfdOF_analysis.svg  style="width:32px;"> [Analysis Container](CfdOF_Analysis.md): Creates a new container for Computational Fluid Dynamics.

  -<img alt="" src=images/CfdOF_Physics_Model.svg  style="width:32px;"> [Physics Model](CfdOF_Physics_Model.md): Lets you select the solver that is to be used in the CFD study.

  -<img alt="" src=images/CfdOF_Fluid_Properties.svg  style="width:32px;"> [Fluid Properties](CfdOF_Fluid_Properties.md): Lets you input the properties of the fluids to be used in the simulation.

  -<img alt="" src=images/CfdOF_CFD_Mesh.svg  style="width:32px;"> [CFD Mesh](CfdOF_CFD_Mesh.md): Lets you build the backgroud, or base, mesh from the geometry.

  -<img alt="" src=images/CfdOF_Mesh_Refinement.svg  style="width:32px;"> [Mesh Refinement](CfdOF_Mesh_Refinement.md): Lets you refine the mesh on the surface and for a volume. Also lets you extrude a mesh.

  -<img alt="" src=images/CdfOF_Mesh_Dynamic.svg  style="width:32px;"> [Interface Dynamic Refinement & Shockwave Dynamic Refinement](CfdOF_Interface_Dynamic_Refinement_&_Shockwave_Dynamic_Refinement.md): Lets you\...

  -<img alt="" src=images/CfdOF_Fluid_Boundary.svg  style="width:32px;"> [Fluid Boundary](CfdOF_Fluid_Boundary.md): Lets you\...

  -<img alt="" src=images/CfdOF_Initialise_Flow_Fields.svg  style="width:32px;"> [Initialise Flow Fields](CfdOF_Initialise_Flow_Fields.md): Lets you\...

  -<img alt="" src=images/CfdOF_Initialisation_Zones.svg  style="width:32px;"> [Initialisation Zones](CfdOF_Initialisation_Zones.md): Lets you\...

  -<img alt="" src=images/CfdOF_Porous_Zone.svg  style="width:32px;"> [Porous Zone](CfdOF_Porous_Zone.md): Lets you\...

  -<img alt="" src=images/CfdOF_Reporting_Function.svg  style="width:32px;"> [Reporting Function](CfdOF_Reporting_Function.md): Lets you\...

  -<img alt="" src=images/CfdOF_Scalar_Transport_Function.svg  style="width:32px;"> [Scalar Transport Function](CfdOF_Scalar_Transport_Function.md): Lets you\...

  -<img alt="" src=images/CfdOF_CFD_Solver.svg  style="width:32px;"> [CFD Solver](CfdOF_CFD_Solver.md): Lets you\...

## Information

The following pages give further information on different topics of the CfdOF Workbench.

-   [Meshing](CfdOF_Meshing.md): tips regarding meshing.
-   [Viewing Mesh](CfdOF_Viewing_Mesh.md):
-   [Checking Mesh](CfdOF_Checking_Mesh.md):
-   [Solver](CfdOF_Solver.md):
-   [Paraview](CfdOF_Paraview.md):

## Tutorials

## Disclaimer

This offering is not approved or endorsed by OpenCFD Limited, producer and distributor of the OpenFOAM software via [www.openfoam.com](http://www.openfoam.com), and owner of the OPENFOAM® and OpenCFD® trade marks.





{{CfdOF Tools navi}}



---
⏵ [documentation index](../README.md) > [CfdOF](Category_CfdOF.md) > CfdOF Workbench
