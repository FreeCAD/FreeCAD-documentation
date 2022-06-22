---
- GuiCommand   */ru
   Name   *FEM SolverElmer
   Name/ru   *FEM SolverElmer
   Icon   *Fem-elmer.svg
   MenuLocation   * Solve → solver Elmer
   Workbenches   *[FEM](FEM_Workbench/ru.md)
   Shortcut   *
   SeeAlso   *[FEM Solver CalculiX](FEM_SolverCalculiX/ru.md), [FEM Solver Z88](FEM_SolverZ88/ru.md), [Учебник МКЭ](FEM_tutorial/ru.md)
---

# FEM SolverElmer/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Elmer - это программное обеспечение для мультифизического моделирования с открытым исходным кодом, которое в основном разрабатывается CSC - IT Center for Science (CSC). Разработка Elmer началась в 1995 году в сотрудничестве с финскими университетами, исследовательскими институтами и промышленностью. После публикации с открытым исходным кодом в 2005 году использование и развитие Elmer стало международным.


</div>


<div class="mw-translate-fuzzy">

Элмер включает, в частности, физические модели гидродинамики, строительной механики, электромагнетизма, теплопередачи и акустики. Они описываются уравнениями в частных производных, которые Элмер решает методом конечных элементов (МКЭ). <https   *//www.csc.fi/web/elmer>


</div>

Создание объекта SolverElmer в контейнере анализа в FreeCAD дает доступ к уравнениям Elmer для простого или мультифизического анализа.

Since FreeCAD already has an extensive integration of <img alt="" src=images/FEM_SolverCalculiX.svg  style="width   *24px;"> [Calculix](FEM_SolverCalculixCxxtools.md) and <img alt="" src=images/FEM_SolverZ88.svg  style="width   *24px;"> [Z88](FEM_SolverZ88.md) as solvers for mechanical and thermo-mechanical analysis, Elmer will be preferred for Computational Fluid Dynamics (CFD), Heat, Electrostatics, Magnetostatics and Electrical Forces. It can also be used for mechanical FEA through the Elasticity equation or any combination of the aforementioned equations.

## Установка

Elmer requires two components to be interfaced with FreeCAD   *

-   ElmerGrid is the interface handling meshes
-   ElmerSolver is handling the computation.

There are standalone programs for both of these applications but their installation and usage are beyond the scope of the FreeCAD integration.

1.  Go to the CSC binaries resources for Elmer   * [binaries](https   *//www.nic.funet.fi/pub/sci/physics/elmer/bin/) OR [CSC binaries](https   *//www.csc.fi/web/elmer/binaries)
2.  Download and install the version best suited to your Operating System ([Windows](https   *//www.nic.funet.fi/pub/sci/physics/elmer/bin/windows/) or [Linux](https   *//www.nic.funet.fi/pub/sci/physics/elmer/bin/linux/Readme1st.txt)). It is recommended to install the `mpi` version to get multi CPU core support.
3.  In FreeCAD go to **Edit → Preferences → FEM → Elmer**
4.  Link the correct path for both `ElmerGrid` and `ElmerSolver` or, to make Elmer use all available CPU cores, `ElmerSolver_mpi`.

       *   ![Elmer Tab in FEM Preferences](images/Preferences-ElmerPath.png )
       *   
        
*Above   * Elmer preferences dialog menu showing fields to locate important Elmer binaries on Windows OS*
        

You are ready to use Elmer in FreeCAD.


{{VersionMinus|0.19}}

   * Now start FreeCAD and change the units scheme to *MKS* in the [preferences](Preferences_Editor#Units.md). See [Notes](#Notes.md).

## Использование

1.  Switch to the <img alt="" src=images/Workbench_FEM.svg  style="width   *24px;"> [FEM Workbench](FEM_Workbench.md)
2.  Create an [Analysis](FEM_Analysis.md) container by pressing the <img alt="" src=images/FEM_Analysis.svg  style="width   *22px;"> icon.
3.  Create a FEM Solver for Elmer, by pressing the <img alt="" src=images/FEM_SolverElmer.svg  style="width   *22px;"> icon.
    -   Note   * A successful analysis will require at least a Model (2D or 3D), a Material ([Fluid](FEM_MaterialFluid.md) or [Solid](FEM_MaterialSolid.md)), a [Mesh](FEM_MeshGmshFromShape.md), Equations and Boundary conditions

       *   ![](images/Elmer_typical_file_tree.png )
       *   
        
*Above   * Example of a [tree view](Tree_view.md) once a Solver for Elmer is activated*
        
4.  Edit the parameters for the solver in the [Property editor](Property_editor.md) **Data** tab of the SolverElmer object in the model [tree view](Tree_view.md)
5.  Double-click on the **<img src="images/FEM_SolverElmer.svg" width=22px> SolverElmer** object to prepare an analysis run

       *   <img alt="" src=images/ElmerSolver_TaskPanel.png  style="width   *300px;">
       *   
        
*Above   * Dialog box to run an Elmer analysis*
        
6.  Select the path to write the analysis in by clicking **...**
7.  Click **Write** to write the case files in the directory selected previously
8.  Click **Run** to start the analysis

### About Equations 

-   To perform the analysis of a particular physical behavior, an Equation must be used (Flow, Heat, Electrostatics\...)
-   Disambiguation   * The term *Equation* is used in FreeCAD to describe the different physical mechanisms, the term *Solver* is used in all Elmer documents. Thus when using in FreeCAD the \"Flow Equation\", in reality Elmer uses the \"Flow Solver\" to find a solution to the Navier-Stokes equation.
-   One or several equations can be used at once with Elmer by simply adding the equation object under the SolverElmer object, thus performing multi-physics analyses   *

1.  Click on the **<img src="images/FEM_SolverElmer.svg" width=22px> SolverElmer** object in the model [tree view](Tree_view.md)
2.  Select an equation   *
    -   <img alt="" src=images/FEM_EquationElasticity.svg  style="width   *32px;"> [Elasticity equation](FEM_EquationElasticity.md)
    -   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width   *32px;"> [Electricforce equation](FEM_EquationElectricforce.md)
    -   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width   *32px;"> [Electrostatic equation](FEM_EquationElectrostatic.md)
    -   <img alt="" src=images/FEM_EquationFlow.svg  style="width   *32px;"> [Flow equation](FEM_EquationFlow.md)
    -   <img alt="" src=images/FEM_EquationFlux.svg  style="width   *32px;"> [Flux equation](FEM_EquationFlux.md)
    -   <img alt="" src=images/FEM_EquationHeat.svg  style="width   *32px;"> [Heat equation](FEM_EquationHeat.md)

## Notes

-   **Important**   * in order to get sensible results and to be able to exchange the Elmer input files (named *case.sif*) with others, all values in the input files must be in SI units. In FreeCAD version 0.19 and earlier this is only the case if you use the unit scheme MKS in the [preferences](Preferences_Editor#Units.md).
-   Parameters for the Solver and for the Equations are independently set through the [Property editor](Property_editor.md) **Data** tab of their respective objects in the [tree view](Tree_view.md).
-   Each equation will have a priority, for example, if trying see the effect of a convective flow of hot air, the equation for Flow should be solved with higher priority than Heat, otherwise the solver will first solve Heat through conduction and then Flow.
-   2D vs 3D cases   * Elmer can be used to solve both 2D and 3D cases. However, when defining a 2D case, the faces need to be mapped in the XY plane of FreeCAD, otherwise the solver will try to compute a 3D case on a face, and normal vectors will be under-defined. Further information can be found in the FreeCAD forums   * <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=48175>

## Документация

The following link gives access to the full [documentation for Elmer](https   *//www.nic.funet.fi/pub/sci/physics/elmer/doc/). This includes the manuals as well as tutorials. Note that documentation and files appended with \"gui\" generally concern the usage of the Elmer GUI and not the FreeCAD implementation of Elmer.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverElmer/ru
