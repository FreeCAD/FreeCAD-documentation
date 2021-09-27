---
- GuiCommand:
   Name:FEM SolverElmer
   MenuLocation: Solve → Solver Elmer
   Workbenches:[FEM](FEM_Workbench.md)
   Shortcut:**S** **E**
   SeeAlso:[FEM Solver CalculiX](FEM_SolverCalculiX.md), [FEM Solver Z88](FEM_SolverZ88.md), [FEM tutorial](FEM_tutorial.md)
---

# FEM SolverElmer

## Description

[Elmer](https://www.elmerfem.org) is an open source multiphysical simulation software mainly developed by CSC - IT Center for Science (CSC). Elmer development was started 1995 in collaboration with Finnish Universities, research institutes and industry. After it\'s open source publication in 2005, the use and development of Elmer has become international.

Elmer includes physical models of fluid dynamics, structural mechanics, electromagnetics, heat transfer and acoustics, for example. These are described by partial differential equations which [Elmer](https://www.csc.fi/web/elmer) solves by the Finite Element Method (FEM).

Creating the SolverElmer object in the Analysis container in FreeCAD, gives access to the Elmer Equations for simple or multiphysical analysis.

Since FreeCAD already has an extensive integration of <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:24px;"> _ as solvers for mechanical and thermo-mechanical analysis, Elmer will be preferred for Computational Fluid Dynamics (CFD), Heat, Electrostatics, Magnetostatics and Electrical Forces. It can also be used for mechanical FEA through the Elasticity equation or any combination of the aforementioned equations.

## Installation

Elmer requires two components to be interfaced with FreeCAD:

-   ElmerGrid is the interface handling meshes
-   ElmerSolver is handling the computation.

There are standalone programs for both of these applications but their installation and usage are beyond the scope of the FreeCAD integration.

1.  Go to the CSC binaries resources for Elmer: [binaries](https://www.nic.funet.fi/pub/sci/physics/elmer/bin/) OR [CSC binaries](https://www.csc.fi/web/elmer/binaries)
2.  Download and install the version best suited to your Operating System ([Windows 64](https://www.nic.funet.fi/pub/sci/physics/elmer/bin/windows/) bits or [Linux](https://www.nic.funet.fi/pub/sci/physics/elmer/bin/linux/Readme1st.txt))
3.  In FreeCAD go to **Edit → Preferences → FEM → Elmer**
4.  Link the correct path for both `ElmerGrid` and `ElmerSolver`

    :   ![Elmer Tab in FEM Preferences](images/Preferences-ElmerPath.png )
    :   
        *Above: Elmer preferences dialog menu showing fields to locate important Elmer binaries on Windows OS*
        

You are ready to use Elmer in FreeCAD.

## Usage

1.  Switch to the <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM Workbench](FEM_Workbench.md)
2.  Create an [Analysis](FEM_Analysis.md) container by pressing the <img alt="" src=images/FEM_Analysis.svg  style="width:22px;"> icon.
3.  Create a FEM Solver for Elmer, by pressing the <img alt="" src=images/FEM_SolverElmer.svg  style="width:22px;"> icon.
    -   Note: A successful analysis will require at least a Model (2D or 3D), a Material ([Fluid](FEM_MaterialFluid.md) or [Solid](FEM_MaterialSolid.md)), a [Mesh](FEM_MeshGmshFromShape.md), Equations and Boundary conditions

    :   ![](images/Elmer_typical_file_tree.png )
    :   
        *Above: Example of a [tree view](Tree_view.md) once a Solver for Elmer is activated*
        
4.  Edit the parameters for the solver in the [Property editor](Property_editor.md) **Data** tab of the SolverElmer object in the model [tree view](Tree_view.md)
5.  Double-click on the **<img src="images/FEM_SolverElmer.svg" width=22px> SolverElmer** object to prepare an analysis run

    :   <img alt="" src=images/ElmerSolver_TaskPanel.png  style="width:300px;">
    :   
        *Above: Dialog box to run an Elmer analysis*
        
6.  Select the path to write the analysis in by clicking **...**
7.  Click **Write** to write the case files in the directory selected previously
8.  Click **Run** to start the analysis

### About Equations 

-   To perform the analysis of a particular physical behavior, an Equation must be used (Flow, Heat, Electrostatics\...)
-   Disambiguation: The term *Equation* is used in FreeCAD to describe the different physical mechanisms, the term *Solver* is used in all Elmer documents. Thus when using in FreeCAD the \"Flow Equation\", in reality Elmer uses the \"Flow Solver\" to find a solution to the Navier-Stokes equation.
-   One or several equations can be used at once with Elmer by simply adding the equation object under the SolverElmer object, thus performing multi-physics analyses:

1.  Click on the **<img src="images/FEM_SolverElmer.svg" width=22px> SolverElmer** object in the model [tree view](Tree_view.md)
2.  Select an equation:
    -   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Elasticity equation](FEM_EquationElasticity.md)
    -   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Electricforce equation](FEM_EquationElectricforce.md)
    -   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Electrostatic equation](FEM_EquationElectrostatic.md)
    -   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Flow equation](FEM_EquationFlow.md)
    -   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Flux equation](FEM_EquationFlux.md)
    -   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Heat equation](FEM_EquationHeat.md)

## Notes

-   Parameters for the Solver and for the Equations are independently set through the [Property editor](Property_editor.md) **Data** tab of their respective objects in the [tree view](Tree_view.md).
-   Each equation will have a priority, for example, if trying see the effect of a convective flow of hot air, the equation for Flow should be solved with higher priority than Heat, otherwise the solver will first solve Heat through conduction and then Flow.
-   2D vs 3D cases: Elmer can be used to solve both 2D and 3D cases. However, when defining a 2D case, the faces need to be mapped in the XY plane of FreeCAD, otherwise the solver will try to compute a 3D case on a face, and normal vectors will be under-defined. Further information can be found in the FreeCAD forums: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48175>

## Documentation

The following link gives access to the full [documentation for Elmer](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/). This includes the manuals as well as tutorials. Note that documentation and files appended with \"gui\" generally concern the usage of the Elmer GUI and not the FreeCAD implementation of Elmer.




 {{FEM Tools navi}}

---
[documentation index](../README.md) > FEM SolverElmer
