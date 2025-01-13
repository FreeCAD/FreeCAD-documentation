# <img alt="FEM workbench icon" src=images/Workbench_FEM.svg  style="width:64px;"> FEM Workbench/zh-cn




## Introduction

The [FEM Workbench](FEM_Workbench.md) provides a modern [finite element analysis](https://en.wikipedia.org/wiki/Finite_element_analysis) (FEA) workflow for FreeCAD. Mainly this means all tools to make an analysis are combined into one graphical user interface (GUI).

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">

## Workflow

The steps to carry out a finite element analysis are:

1.  Preprocessing: setting up the analysis problem.
    1.  Modeling the geometry: creating the geometry with FreeCAD, or importing it from a different application.
    2.  Creating an analysis.
        1.  Adding simulation constraints such as loads and fixed supports to the geometric model.
        2.  Adding materials to the parts of the geometric model.
        3.  Creating a finite element mesh for the geometrical model, or importing it from a different application.
2.  Solving: running an external solver from within FreeCAD.
3.  Postprocessing: visualizing the analysis results from within FreeCAD, or exporting the results so they can be postprocessed with another application.

The FEM Workbench can be used on Linux, Windows, and Mac OSX. Since the workbench makes use of external solvers, the amount of manual setup will depend on the operating system that you are using. See [FEM Install](FEM_Install.md) for instructions on setting up the external tools.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;">



*Workflow of the FEM Workbench; the workbench calls two external programs to perform meshing of a solid object, and perform the actual solution of the finite element problem*

## Menu: Model 

-   <img alt="" src=images/FEM_Analysis.svg  style="width:32px;"> [Analysis container](FEM_Analysis.md): Creates a new container for a mechanical analysis. If a solid is selected in the tree view before clicking on it, the meshing dialog will be opened next.

### Materials

  - <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> [Material for solid](FEM_MaterialSolid.md): Lets you select a solid material from the database.

  - <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Material for fluid](FEM_MaterialFluid.md): Lets you select a fluid material from the database.

  - <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Nonlinear mechanical material](FEM_MaterialMechanicalNonlinear.md): Lets you add a nonlinear mechanical material model.

  - <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Reinforced material (concrete)](FEM_MaterialReinforced.md): Lets you select reinforced materials consisting of a matrix and a reinforcement from the database.

  - <img alt="" src=images/FEM_MaterialEditor.svg  style="width:32px;"> [Material editor](FEM_MaterialEditor.md): Lets you open the material editor to edit materials.

### Element Geometry 

  - <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Beam cross section](FEM_ElementGeometry1D.md): Used to define cross sections for beam elements.

  - <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Beam rotation](FEM_ElementRotation1D.md): Used to rotate cross sections of beam elements.

  - <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Shell plate thickness](FEM_ElementGeometry2D.md): Used to define shell element thickness.

  - <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Fluid section for 1D flow](FEM_ElementFluid1D.md): Used to create fluid section element for pneumatic and hydraulic networks.

### Electromagnetic boundary conditions 

  - <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Electrostatic potential boundary condition](FEM_ConstraintElectrostaticPotential.md): Used to define electrostatic potential.

  - <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:32px;"> [Current density boundary condition](FEM_ConstraintCurrentDensity.md): Used to define a current density. <small>(v0.21)</small> 

  - <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:32px;"> [Magnetization boundary condition](FEM_ConstraintMagnetization.md): Used to define a magnetization. <small>(v0.21)</small> 

### Fluid boundary conditions 

  - <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Initial flow velocity condition](FEM_ConstraintInitialFlowVelocity.md): Used to define an initial flow velocity for a body (volume).

  - <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Initial pressure condition](FEM_ConstraintInitialPressure.md): Used to define an initial pressure for a body (volume). <small>(v0.21)</small> 

  - <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Flow velocity boundary condition](FEM_ConstraintFlowVelocity.md): Used to define a flow velocity as a boundary condition at an edge (2D) or face (3D).

### Geometrical analysis features 

  - <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Plane multi-point constraint](FEM_ConstraintPlaneRotation.md): Used to define a constraint for keeping the nodes in a planar surface in the same plane.

  - <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Section print feature](FEM_ConstraintSectionPrint.md): Used to print the predefined facial output variables (forces and moments) to the data file.

  - <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Local coordinate system](FEM_ConstraintTransform.md): Used to define a transform constraint on a face.

### Mechanical boundary conditions and loads 

  - <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Fixed boundary condition](FEM_ConstraintFixed.md): Used to define a fixed constraint on point/edge/face(s).

  - <img alt="" src=images/FEM_ConstraintRigidBody.svg  style="width:32px;"> [Rigid body constraint](FEM_ConstraintRigidBody.md): Used to apply the CalculiX\'s rigid body constraint that constrains the motion of the nodes of a selected geometrical entity to the motion of a reference point positioned by the user. <small>(v1.0)</small> 

  - <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Displacement boundary condition](FEM_ConstraintDisplacement.md): Used to define a displacement constraint on point/edge/face(s).

  - <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Contact constraint](FEM_ConstraintContact.md): Used to define a contact constraint between two faces.

  - <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Tie constraint](FEM_ConstraintTie.md): Used to define a tie constraint (\"bonded contact\") between two faces, or, <small>(v1.0)</small> , cyclic symmetry.

  - <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Spring](FEM_ConstraintSpring.md): Used to define a spring. <small>(v0.20)</small> 

  - <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Force load](FEM_ConstraintForce.md): Used to define a force in \[N\] applied uniformly to a selectable face in a definable direction.

  - <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Pressure load](FEM_ConstraintPressure.md): Used to define a pressure constraint.

  - <img alt="" src=images/FEM_ConstraintCentrif.svg  style="width:32px;"> [Centrifugal load](FEM_ConstraintCentrif.md): Used to define a centrifugal body load constraint. <small>(v0.20)</small> 

  - <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Gravity load](FEM_ConstraintSelfWeight.md): Used to define a gravity acceleration acting on a model.

### Thermal boundary conditions and loads 

  - <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Initial temperature](FEM_ConstraintInitialTemperature.md): Used to define the initial temperature of a body.

  - <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Heat flux load](FEM_ConstraintHeatflux.md): Used to define a heat flux constraint on a face(s).

  - <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Temperature boundary condition](FEM_ConstraintTemperature.md): Used to define a temperature constraint on a point/edge/face(s).

  - <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Body heat source](FEM_ConstraintBodyHeatSource.md): Used to define an internally generated body heat.

### Overwrite Constants 

  - <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Constant vacuum permittivity](FEM_ConstantVacuumPermittivity.md): Used to overwrite the [permittivity of vacuum](https://en.wikipedia.org/wiki/Vacuum_permittivity) with a custom value.

## Menu: Mesh 

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [FEM mesh from shape by Netgen](FEM_MeshNetgenFromShape.md): Generates a finite element mesh for a model using Netgen.

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md): Generates a finite element mesh for a model using Gmsh.

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [FEM mesh boundary layer](FEM_MeshBoundaryLayer.md): Creates anisotropic meshes for accurate calculations near boundaries.

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [FEM mesh region](FEM_MeshRegion.md): Creates a localized area(s) to mesh which highly optimizes analysis time.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [FEM mesh group](FEM_MeshGroup.md): Groups and labels elements of a mesh (vertex, edge, surface) together, useful for exporting the mesh to external solvers.

-   <img alt="" src=images/FEM_CreateElementsSet.svg  style="width:32px;"> [Erase Elements](FEM_CreateElementsSet.md): Hides elements selected by a polygon from the mesh. <small>(v1.0)</small> 

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [FEM mesh to mesh](FEM_FemMesh2Mesh.md): Converts surfaces of 3D elements or whole 2D elements of a selected FEM mesh to surface mesh.

## Menu: Solve 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solver CalculiX Standard](FEM_SolverCalculixCxxtools.md): Creates a new solver for this analysis.

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md): Creates the solver controller for Elmer.

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Solver Mystran](FEM_SolverMystran.md): Creates the solver controller for the MYSTRAN solver. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Solver Z88](FEM_SolverZ88.md): Creates the solver controller for Z88.

### Mechanical equations 

  - <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Elasticity equation](FEM_EquationElasticity.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform linear mechanical analyses.

  - <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [Deformation equation](FEM_EquationDeformation.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform nonlinear mechanical analyses (deformations). <small>(v0.21)</small> 

### Electromagnetic equations 

  - <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Electrostatic equation](FEM_EquationElectrostatic.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform electrostatic analyses.

  - <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Electricforce equation](FEM_EquationElectricforce.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to calculate the electric force on surfaces.

  - <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:32px;"> [Magnetodynamic equation](FEM_EquationMagnetodynamic.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to calculate magnetodynamics. <small>(v0.21)</small> 

  - <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:32px;"> [Magnetodynamic 2D equation](FEM_EquationMagnetodynamic2D.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to calculate magnetodynamics in 2D. <small>(v0.21)</small> 

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Flow equation](FEM_EquationFlow.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform flow analyses.

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Flux equation](FEM_EquationFlux.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform flux analyses.

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Heat equation](FEM_EquationHeat.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform heat transfer analyses.

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Solver job control](FEM_SolverControl.md): Opens the menu to adjust and start the selected solver.

-   <img alt="" src=images/FEM_SolverRun.svg  style="width:32px;"> [Run solver calculations](FEM_SolverRun.md): Runs the selected solver of the active analysis.

## Menu: Results 

-   <img alt="" src=images/FEM_ResultsPurge.svg  style="width:32px;"> [Purge results](FEM_ResultsPurge.md): Deletes the results of the active analysis.

-   <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Show result](FEM_ResultShow.md): Used to display the result of an analysis. This dialog is not available for the [Solver Elmer](FEM_SolverElmer.md) as this solver visualizes using the [Post pipeline from result](FEM_PostPipelineFromResult.md) object only.

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Apply changes to pipeline](FEM_PostApplyChanges.md): Toggles if changes to pipelines and filters are applied immediately.

-   <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:32px;"> [Post pipeline from result](FEM_PostPipelineFromResult.md): Used to add a new graphical representation of FEM analysis results (color scale and more display options).

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Warp filter](FEM_PostFilterWarp.md): Used to visualize the scaled deformed shape of the model.

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Scalar clip filter](FEM_PostFilterClipScalar.md): Used to clip a field with a specified scalar value.

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Function cut filter](FEM_PostFilterCutFunction.md): Used to display the results on a sphere or a plane cutting through the model.

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Region clip filter](FEM_PostFilterClipRegion.md): Used to clip a field with a sphere or a plane cutting through the model.

-   <img alt="" src=images/FEM_PostFilterContours.svg  style="width:32px;"> [Contours filter](FEM_PostFilterContours.md): Used to display iso-lines (for analyses in 2D) or iso-contours. <small>(v0.21)</small> 

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Line clip filter](FEM_PostFilterDataAlongLine.md): Used to plot the values of a field along a specified line.

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Stress linearization plot](FEM_PostFilterLinearizedStresses.md): Creates a stress linearization plot.

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Data at point clip filter](FEM_PostFilterDataAtPoint.md): Used to display value of a selected field at a given point.

### Filter functions 

  - <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:32px;"> [Plane](FEM_PostCreateFunctionPlane.md): Cuts the result mesh with a plane.

  - <img alt="" src=images/FEM_PostCreateFunctionSphere.svg  style="width:32px;"> [Sphere](FEM_PostCreateFunctionSphere.md): Cuts the result mesh with a sphere.

  - <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:32px;"> [Cylinder](FEM_PostCreateFunctionCylinder.md): Cuts the result mesh with a cylinder. <small>(v0.21)</small> 

  - <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:32px;"> [Box](FEM_PostCreateFunctionBox.md): Cuts the result mesh with a box. <small>(v0.21)</small> 

## Menu: Utilities 

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Clipping plane on face](FEM_ClippingPlaneAdd.md): Adds a clipping plane for the whole model view.

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Remove all clipping planes](FEM_ClippingPlaneRemoveAll.md): Removes all existing [clipping planes](FEM_ClippingPlaneAdd.md).

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [Open FEM examples](FEM_Examples.md): Open the GUI to access FEM examples.

## Context Menu 

-   <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [Clear FEM mesh](FEM_MeshClear.md): Deletes the mesh file from the FreeCAD file. Useful to make a FreeCAD file lighter.

-   <img alt="" src=images/FEM_MeshDisplayInfo.svg  style="width:32px;"> [Display FEM mesh info](FEM_MeshDisplayInfo.md): Displays basic statistics of existing mesh - number of nodes and elements of each type.

## Obsolete tools 

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Fluid boundary condition](FEM_ConstraintFluidBoundary.md): Used to define a fluid boundary condition. Did not have a solver. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Constraint bearing](FEM_ConstraintBearing.md): Used to define a bearing constraint. Did not have a solver. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Constraint gear](FEM_ConstraintGear.md): Used to define a gear constraint. Did not have a solver. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Constraint pulley](FEM_ConstraintPulley.md): Used to define a pulley constraint. Did not have a solver. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Solver CalculiX (new framework)](FEM_SolverCalculiX.md): Same as the original framework <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solver CalculiX Standard](FEM_SolverCalculixCxxtools.md) with extra checks. Tool was unfinished. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [Nodes set](FEM_CreateNodesSet.md): Creates/defines a node set from FEM mesh. Tool was unfinished and couldn\'t be used. Not available in <small>(v1.0)</small> .

## Preferences

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferences\...](FEM_Preferences.md): Preferences available in FEM Tools.

## Information

The following pages explain different topics of the FEM Workbench.

[FEM Install](FEM_Install.md): a detailed description on how to set up the external programs used in the workbench.

[FEM Geometry Preparation and Meshing](FEM_Geometry_Preparation_and_Meshing.md): tips regarding geometry preparation for FEM and meshing.

[FEM Mesh](FEM_Mesh.md): details about meshes in the FEM workbench.

[FEM Solver](FEM_Solver.md): further information on the different solvers available in the workbench, and those that could be used in the future.

[FEM CalculiX](FEM_CalculiX.md): further information on CalculiX, the default solver used in the workbench for structural analysis.

[FEM Concrete](FEM_Concrete.md): interesting information on the topic of simulating concrete structures.

## Tutorials

Tutorial 1: [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D.md); basic simply supported beam analysis.

Tutorial 2: [FEM Tutorial](FEM_tutorial.md); simple tension analysis of a structure.

Tutorial 3: [FEM Tutorial Python](FEM_Tutorial_Python.md); set up the cantilever example entirely through scripting in Python, including the mesh.

Tutorial 4: [FEM Shear of a Composite Block](FEM_Shear_of_a_Composite_Block.md); see the deformation of a block that is comprised of two materials.

Tutorial 5: [Transient FEM analysis](Transient_FEM_analysis.md)

Tutorial 6: [Post-Processing of FEM Results with Paraview](Post-Processing_of_FEM_Results_with_Paraview.md)

Tutorial 7: [FEM Example Capacitance Two Balls](FEM_Example_Capacitance_Two_Balls.md); Elmer\'s GUI tutorial 6 \"Electrostatics Capacitance Two Balls\" using FEM Examples.

Coupled thermal mechanical analysis tutorials by [openSIM](https://opensimsa.github.io/training.html)

Video tutorial 1: [FEM video for beginner](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353) (including YouTube link)

Video tutorial 2: [FEM video for beginner](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321) (including YouTube link)

Many video tutorials: [anisim Open Source Engineering Software](https://www.youtube.com/channel/UCnvFCm2BbXOVI3ObfXcxXhw) (in German)

## Extending the FEM Workbench 

The FEM Workbench is under constant development. An objective of the project is to find ways to easily interact with various FEM solvers, so that the end user can streamline the process of creating, meshing, simulating, and optimizing an engineering design problem, all within FreeCAD.

The following information is aimed at power users and developers who want to extend the FEM Workbench in different ways. Familiarity with C++ and Python is expected, and also some knowledge of the \"document object\" system used in FreeCAD is necessary; this information is available in the [Power users hub](Power_users_hub.md) and the [Developer hub](Developer_hub.md). Please notice that since FreeCAD is under active development, some articles may be too old, and thus obsolete. The most up to date information is discussed in the [FreeCAD forums](https://forum.freecadweb.org/index.php), in the Development section. For FEM discussions, advice or assistance in extending the workbench, the reader should refer to the [FEM subforum](https://forum.freecadweb.org/viewforum.php?f=18).

The following articles explain how the workbench can be extended, for example, by adding new types of boundary conditions (constraints), or equations.

-   [Extend FEM Module](Extend_FEM_Module.md)
-   [Onboarding FEM Devs](Onboarding_FEM_Devs.md) attempts to orient new devs on how to contribute to the FEM workbench.
-   [Add FEM Constraint Tutorial](Add_FEM_Constraint_Tutorial.md)
-   [Add FEM Equation Tutorial](Add_FEM_Equation_Tutorial.md)

A developer\'s guide has been written to help power users in understanding the complex FreeCAD codebase and the interactions between the core elements and the individual workbenches. The book is hosted at github so multiple users can contribute to it and keep it updated.

-   [Early preview of ebook: Module developer\' guide to FreeCAD source](https://forum.freecadweb.org/viewtopic.php?t=17581) forum thread.
-   [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) github repository.

## Extending the FEM Workbench documentation 

-   More information regarding extending or missing FEM documentation can be found in the forum: [FEM documentation missing on the Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [FEM](Category_FEM.md) > FEM Workbench/zh-cn
