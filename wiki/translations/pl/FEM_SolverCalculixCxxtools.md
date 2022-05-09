---
- GuiCommand   *
   Name   *FEM SolverCalculixCxxtools
   MenuLocation   *Solve → Solver CalculiX Standard
   Workbenches   *[FEM](FEM_Workbench.md)
   Shortcut   ***S** **X**
   SeeAlso   *[FEM tutorial](FEM_tutorial.md)
---

# FEM SolverCalculixCxxtools/pl

## Description

[CalculiXccxTools](FEM_SolverCalculixCxxtools.md) enables usage of the [CalculiX](https   *//en.wikipedia.org/wiki/Calculix) solver. It may be used for   *

1.  Setting analysis parameters
2.  Selecting working directory
3.  Running the CalculiX solver

## Usage

1.  A <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width   *16px;"> CalculiXcxxTools solver object is created automatically with the creation of an <img alt="" src=images/FEM_Analysis.svg  style="width   *16px;"> [Analysis container](FEM_Analysis.md).
    To create it manually, use one of the following alternatives   *
    -   Select **Solve → <img src="images/FEM_SolverCalculixCxxtools.svg" width=16px> Solver CalculiX Standard** from the menu.
    -   Press the **S** then **X** shortcut keys.
2.  Optionally change the properties of the <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width   *16px;"> CalculiXcxxTools solver object in the [Property editor](Property_editor.md).
3.  Double click the <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width   *16px;"> CalculiXcxxTools solver object.
4.  Select the **Analysis type**.
5.  Click the **Write .inp file** button.
6.  Click the **Run CalculiX** button.

## Options

Click the **Edit .inp file** button to display and edit the CalculiX input file manually before running the analysis. In that case it can be useful to set the **Split Input Writer** property to {{True}}.

## Properties

Default values can be set in the menu **Edit → Preferences → FEM → CalculiX**

-    **Analysis Type**   *

    -   static
    -   frequency
    -   thermomech - for mechanical and thermal loads
    -   check - to check only the mesh <small>(v0.19)</small> 
    -   buckling - for buckling analyses <small>(v0.20)</small> 

-    **Beam Shell Result Output 3D**   * note that CalculiX internally expands 1D and 2D elements into 3D elements to accomplish FE analysis

    -   false - results of 1D and 2D elements will be averaged to the nodes of original 1D or 2D mesh (i.e. purely bended beam will show 0 nodal stresses due to averaging)
    -   true - resulting mesh will contain 1D and 2D elements expanded to 3D elements

-    **Eigenmode High Limit**   * Eigenvalues above this limit will not be calculated; **Note**   * if eigenvalues of the model are above the high limit, CalculiX will finish without output

-    **Eigenmode Low Limit**   * Eigenvalues below this limit will not be calculated

-    **Eigenmodes Count**   * number of lowest eigenmodes to be calculated

-    **Geometric Nonlinearity**   *

    -   linear - linear analysis will be performed if model does not contain nonlinear material
    -   nonlinear - nonlinear analysis will be performed

-    **Iterations Control parameter Cutb**   * defines the second line of [CalculiX\' advanced iteration parameters](http   *//www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Used if **Iterations Control Parameter Time Use** is set to *true*.

-    **Iterations Control Parameter Iter**   * defines the first line of [CalculiX\' advanced iteration parameters](http   *//www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Used if **Iterations Control Parameter Time Use** is set to *true*.

-    **Iterations Control Parameter Time Use**-   true - activates **Iterations Control parameter Cutb** and **Iterations Control Parameter Iter**
    -   false

-    **Iterations Thermo Mech Maximum**   * maximum number of increments in thermomechanical analysis after which the job will be stopped.

-    **Iterations User Defined Incrementations**   *

    -   true - automatic incrementation control will be switched off by DIRECT parameter
    -   false - incrementation control will be automatic

-    **Iterations User Defined Time Step Length**   *

    -   true - activates **Time End** and **Time Initial Step** parameters
    -   false

-    **Material Nonlinearity**   *

    -   linear - only linear material properties will be included in the analysis
    -   nonlinear - nonlinear material properties will be used from **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=24px> '''[Nonlinear mechanical material](FEM_MaterialMechanicalNonlinear.md)'''** object

-    **Matrix Solver Type**   * type of the solver to solve equation system inside FE analysis. It may significantly affect calculation speed and memory demands. Suitability depends on your FE model and available hardware

    -   default - automatically selects matrix solver depending on available solvers (probably it will be Spooles)
    -   spooles - direct solver with support of multiple CPUs. Number of CPUs need to be set in the [preferences](FEM_Preferences#CalculiX.md) at *Solver defaults → Number of CPU\'s to use*.
    -   iterativescaling - iterative solver with least memory demands, suitable if model contains mostly 3D elements
    -   iterativecholesky - iterative solver with preconditioning with and with low memory demands, suitable if model contains mostly 3D elements

-    **Split Input Writer**   *

    -   false - write whole input into one \*.inp file to be used by CalculiX solver
    -   true - split solver inputs into more \*.inp files, that can clarify hand editing

-    **Thermo Mechanical Steady State**   *

    -   true - steady state thermo mechanical analysis
    -   false - transient thermo mechanical analysis

-    **Time End**   * time period of the step, used when parameter **Iterations User Defined Incrementations** or **Iterations User Defined Time Step Length** is *true*

-    **Time Initial Step**   * initial time increment of the step, used when parameter **Iterations User Defined Incrementations** or **Iterations User Defined Time Step Length** is *true*

-    **Working Dir**   * path to the working directory which will be used for CalculiX analysis files.

## Limitations

When running a CalculiX, you might end up with **error 4294977295**. This means you don\'t have enough RAM space. You have then 2 options   *

1.  reduce the number of mesh nodes, preferably by omitting geometry that is not absolutely necessary for your analysis
2.  buy more RAM for your PC

## Notes

Original CalculiX documentation can be found at <http   *//dhondt.de/> in the \"ccx\" paragraph.

## Scripting





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverCalculixCxxtools/pl
