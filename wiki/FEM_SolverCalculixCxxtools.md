---
 GuiCommand:
   Name: FEM SolverCalculixCxxtools
   MenuLocation: Solve , Solver CalculiX Standard
   Workbenches: FEM_Workbench
   Shortcut: **S** **X**
   SeeAlso: FEM_tutorial
---

# FEM SolverCalculixCxxtools

## Description

[CalculiXccxTools](FEM_SolverCalculixCxxtools.md) enables usage of the [CalculiX](https://en.wikipedia.org/wiki/Calculix) solver. It may be used for:

1.  Setting analysis parameters
2.  Selecting working directory
3.  Running the CalculiX solver

## Usage

1.  A <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> CalculiXcxxTools solver object is created automatically with the creation of an <img alt="" src=images/FEM_Analysis.svg  style="width:16px;"> [Analysis container](FEM_Analysis.md).
    To create it manually, use one of the following alternatives:
    -   Press the **<img src="images/FEM_SolverCalculixCxxtools.svg" width=16px> [Solver CalculiX Standard](FEM_SolverCalculixCxxtools.md)** button.
    -   Select **Solve → <img src="images/FEM_SolverCalculixCxxtools.svg" width=16px> Solver CalculiX Standard** from the menu.
    -   Press the **S** then **X** shortcut keys.
2.  Optionally change the properties of the <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> CalculiXcxxTools solver object in the [Property editor](Property_editor.md).
3.  Double click the <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> CalculiXcxxTools solver object.
4.  Select the **Analysis type**.
5.  Click the **Write .inp file** button.
6.  Click the **Run CalculiX** button.

## Options

Click the **Edit .inp file** button to display and edit the CalculiX input file manually before running the analysis. In that case it can be useful to set the **Split Input Writer** property to {{True}}.

## Properties

Default values can be set in the menu **Edit → Preferences → FEM → CalculiX**

-    **Analysis Type**:

    -   static - static stress analysis
    -   frequency - modal (natural frequency) analysis
    -   thermomech - thermo-mechanical analysis
    -   check - no calculation, performs input deck checks
    -   buckling - linear buckling analysis <small>(v0.20)</small> 

-    **Beam Reduced Integration**\- <small>(v1.0)</small> :

    -   true - uses beam elements with reduced integration (B31R or B32R), required when pipe beam section is used, can also make it possible to obtain [accurate results with plasticity](https://forum.freecad.org/viewtopic.php?t=61233)
    -   false - uses regular (fully-integrated) beam elements

-    **Beam Shell Result Output 3D**: note that CalculiX internally expands 1D and 2D elements into 3D elements to accomplish finite element analysis

    -   true - resulting mesh will contain 1D and 2D elements expanded to 3D elements
    -   false - results of 1D and 2D elements will be averaged to the nodes of original 1D or 2D mesh (i.e. purely bended beam will show 0 nodal stresses due to averaging)

-    **Buckling Accuracy**\- <small>(v1.1)</small> : defines the accuracy of buckling eigenvalue evaluation. In most cases it can be left with the default value (0.01) but sometimes it might be necessary to lower it (e.g. to 0.0001) to capture the first eigenvalue.

-    **Eigenmode High Limit**: Eigenvalues above this limit will not be calculated; **Note**: if eigenvalues of the model are above the high limit, CalculiX will finish without output

-    **Eigenmode Low Limit**: Eigenvalues below this limit will not be calculated

-    **Eigenmodes Count**: number of lowest eigenmodes to be calculated

-    **Geometric Nonlinearity**:

    -   linear - linear analysis will be performed if the model does not contain nonlinear material
    -   nonlinear - nonlinear analysis will be performed

-    **Iterations Control parameter Cutb**: defines the second line of [CalculiX\' advanced iteration parameters](http://www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Used if **Iterations Control Parameter Time Use** is set to *true*.

-    **Iterations Control Parameter Iter**: defines the first line of [CalculiX\' advanced iteration parameters](http://www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Used if **Iterations Control Parameter Time Use** is set to *true*.

-    **Iterations Control Parameter Time Use**-   true - activates **Iterations Control parameter Cutb** and **Iterations Control Parameter Iter**
    -   false

-    **Iterations Maximum**: maximum number of increments after which the job will be stopped.

-    **Iterations User Defined Incrementations**:

    -   true - automatic incrementation control will be switched off by DIRECT parameter
    -   false - incrementation control will be automatic

-    **Iterations User Defined Time Step Length**:

    -   true - activates **Time End** and **Time Initial Step** parameters
    -   false

-    **Material Nonlinearity**:

    -   linear - only linear material properties will be included in the analysis
    -   nonlinear - nonlinear material properties will be used from **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=24px> [Nonlinear mechanical material](FEM_MaterialMechanicalNonlinear.md)** object

-    **Matrix Solver Type**: type of the solver to solve equation system inside finite element analysis. It may significantly affect calculation speed and memory demands. Suitability depends on your finite element model and available hardware

    -   default - automatically selects matrix solver depending on the available solvers (typically it is Spooles)

    -   
        <small>(v1.0)</small> 
        
        : pastix - one of the fastest solvers (along with Pardiso), available (and default) in official builds since ccx 2.18, may still cause occasional issues

    -   
        <small>(v1.0)</small> 
        
        : pardiso - one of the fastest solvers (along with PaStiX) but not open-source, requires a different build of CalculiX (ccx_dynamic) and additional libraries not provided with FreeCAD, more reliable than PaStiX

    -   spooles - direct solver with the support of multiple CPUs. The number of CPUs needs to be set in the [preferences](FEM_Preferences#CalculiX.md) at *Solver defaults → Number of CPU\'s to use*.

    -   iterativescaling - iterative solver with the lowest memory demands, suitable if the model contains mostly 3D elements

    -   iterativecholesky - iterative solver with preconditioning with and with low memory demands, suitable if the model contains mostly 3D elements

-    **Model Space**\- <small>(v1.0)</small> : switches between 3D and 2D analyses, the latter require surface geometry on the XY plane (on the right of the Y axis in the axisymmetric case) with [thickness definition](FEM_ElementGeometry2D.md) (value ignored in the axisymmetric case) and proper boundary conditions ([displacement boundary condition](FEM_ConstraintDisplacement.md) with degrees of freedom X and Y has to be used instead of [fixed boundary condition](FEM_ConstraintFixed.md)) and in-plane loads applied to edges

    -   3D - three-dimensional solid/shell/beam elements are used
    -   plane stress - plane stress 2D solid elements are used
    -   plane strain - plane strain 2D solid elements are used
    -   axisymmetric - axisymmetric 2D solid elements are used

-    **Output Frequency**\- <small>(v1.0)</small> : defines the frequency of results writing in increments (the default setting of 1 means that the results are written every increment, setting 2 would save the results every 2 increments and so on), particularly useful for nonlinear and transient simulations, helps reduce the clutter in the tree since currently a pair of results objects (CCX_Results and Pipeline_CCX_Results) is created for each results frame

-    **Split Input Writer**:

    -   false - write whole input into one \*.inp file to be used by CalculiX solver
    -   true - split solver inputs into more \*.inp files, that can clarify hand editing

-    **Thermo Mech Steady State**:

    -   true - steady state thermo-mechanical analysis
    -   false - transient thermo-mechanical analysis

-    **Thermo Mech Type**\- <small>(v1.0)</small> :

    -   coupled - coupled thermo-mechanical analysis
    -   uncoupled - uncoupled thermo-mechanical analysis
    -   pure heat transfer - purely thermal analysis (*\*HEAT TRANSFER*)

-    **Time End**: time period of the step, used when parameter **Iterations User Defined Incrementations** or **Iterations User Defined Time Step Length** is *true*

-    **Time Initial Step**: initial time increment of the step, used when parameter **Iterations User Defined Incrementations** or **Iterations User Defined Time Step Length** is *true*

-    **Time Maximum Step**\- <small>(v1.0)</small> : maximum time increment of the step, used when parameter **Iterations User Defined Incrementations** or **Iterations User Defined Time Step Length** is *true*

-    **Time Minimum Step**\- <small>(v1.0)</small> : minimum time increment of the step, used when parameter **Iterations User Defined Incrementations** or **Iterations User Defined Time Step Length** is *true*

-    **Working Dir**: path to the working directory which will be used for CalculiX analysis files.

## Limitations

When running a CalculiX, you might end up with **error 4294977295**. This means you don\'t have enough RAM space. You have then 2 options:

1.  reduce the number of mesh nodes, preferably by omitting geometry that is not absolutely necessary for your analysis
2.  buy more RAM for your PC

## Notes

Original CalculiX documentation can be found at <http://dhondt.de/> in the \"ccx\" paragraph.

## Scripting




 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverCalculixCxxtools
