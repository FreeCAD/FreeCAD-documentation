# FEM Example Capacitance Two Balls/it
{{TutorialInfo/it
|Topic= Analisi agli elementi finiti
|Level=Base
|Time=
|Author=[https://wiki.freecadweb.org/User:Sudhanshu_Dubey Sudhanshu Dubey]
|FCVersion=0.19 o superiore
|Files=
}}

## Introduzione


<div class="mw-translate-fuzzy">

Questo esempio ha lo scopo di mostrare come simulare il sesto esempio di _. Illustra come impostare l\'esempio, studiarne le varie parti, risolverlo usando il [solver Elmer](FEM_SolverElmer/it.md) e visualizzare i risultati usando [Clip Filter](FEM_PostFilterClipRegion/it.md).


</div>

<img alt="" src=images/Two_balls_result_2.png  style="width:1200px;">

## Requirements

-   A compatible version of FreeCAD designated in the tutorial overview.

    :   Use the **Help → About FreeCAD** to see the version of FreeCAD installed
-   No external software is needed for loading the example, viewing the mesh and geometry as well as for visualizing the results.
-   For solving the FEA, the solver software Elmer must be installed on your computer. See [Elmer Solver](FEM_SolverElmer.md) for how to install Elmer.

## Set up the example 

### Load FEM Workbench 

-   Start FreeCAD, the Start Workbench should be loaded
-   Switch to <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [FEM workbench](FEM_Workbench.md).

### Load the example 

-   Go to **Utilities → <img src=images/FEM_Examples.svg style="width:24px"> Open FEM examples**.
-   When the GUI opens, find and open \"Electrostatics Capacitance Two Balls\". You can easily find the example in **All** or in **Solvers → Elmer**. For opening the example, either double click on it or select it and click **Setup**.

<img alt="" src=images/Two_balls_selection.png  style="width:300px;">

## Understanding the Simulation Case 

This case presents the solution of the capacitance of perfectly conducting balls in free space. A voltage difference between the balls results to electric charge being introduced to the system. The balls have also self-capacitance that comes from the voltage difference with the far field. Therefore a symmetric capacitance matrix with of size 2 × 2 needs to be solved. The capacitances may be computed from two different voltage configurations.

## Understanding the Model 

-   The model contains three spheres.

1.  The two smaller ones are the perfectly conducting balls.
2.  The bigger one is to simulate the surrounding air.

-   The two smaller spheres are fused together and then that fusion is is cut from the bigger sphere.

![ 1200px](images/Two_balls_model_full.png )

## Analysis container and its objects 

-   There are at least the 7 objects needed to make this electrostatic analysis.
-   <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> analysis container

1.  <img alt="" src=images/FEM_SolverElmer.svg  style="width:24px;"> Elmer solver
2.  <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> Electrostatic equation
3.  <img alt="" src=images/FEM_MaterialFluid.svg  style="width:24px;"> a fluid material (to represent the surrounding air)
4.  <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> electrostatic constraint (3 of them)
5.  <img alt="" src=images/Fem-thermomechanical-analysis.svg  style="width:24px;">Constant Vaccum Permittivity
6.  <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> a Gmsh FEM mesh
7.  <img alt="" src=images/FEM_MeshRegion.svg  style="width:24px;"> Mesh region (for the smaller spheres)

<img alt="" src=images/Two_balls_analysis.png  style="width:300px;">

## Running the FEA 

-   In [Tree view](Tree_view.md) double click on the solver object <img alt="" src=images/FEM_SolverElmer.svg  style="width:24px;">.
-   Click on **Write** file in the same task window. Watch the log window until it prints \"write completed.\"
-   Click on **Run**. Since this is a small analysis it should take a few seconds to run so wait till you see \"ELMER SOLVER FINISHED AT\" in the output.
-   Click on **Close** in the task window after the run is finished.
-   Two new result objects should be created, <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult and <img alt="" src=images/TextDocument.svg  style="width:24px;"> SolverElmerOutput.
-   If you get an error message on solver binary or similar when triggering the analysis check installation of [Elmer Solver](FEM_SolverElmer.md).

## Visualizing Results 

-   Be sure the analysis is activated.
-   Be sure the analysis still contains the result object, if not just re-run the solver.
-   Make sure the mesh is invisible. If not, select the mesh object press **Space** to toggle the visibility.
-   Double click on the <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult to load in the [task panel](Task_panel.md).
-   Change the \"Mode\" to \"Surface\" and the \"Field\" to \"potential\". Press **Ok**.
-   You will notice that the colour of the sphere has changed to blue and that the gradient on the right is showing values from 0 to +1. It should look something like this:

<img alt="" src=images/Two_balls_potential.png  style="width:1200px;">

## Post Processing the Result 

-   While we have successfully visualised the potential result, currently we are only seeing the zero potential in the air surrounding the two balls. To view the potential on the balls we need to apply a clip filter.
-   In the [tree view](Tree_view.md) select the <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult and then from the tool bar click on the <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:24px;"> Post Create Clip Filter.
-   This will open the [task panel](Task_panel.md) with the clip filter configurations. Select \"Plane\" in the \"Create\" menu and check the \"Cut Cells\" box. After that click **Apply**.

<img alt="" src=images/Two_balls_postcreate.png  style="width:300px;">

-   Then choose the same configurations (Surface and potential) as you have while visualising the results. Click **Ok**. Toggle the visibility of <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> SolverElmerResult using **Space** and you should see something like this:

<img alt="" src=images/Two_balls_result.png  style="width:1200px;">

-   Now we can clearly see that potential distribution in and around the balls.

## Finding the Capacitance 

-   Our actual focus is to find the capacitance which is contained in the <img alt="" src=images/TextDocument.svg  style="width:24px;"> SolverElmerOutput.
-   Double click on <img alt="" src=images/TextDocument.svg  style="width:32px;"> SolverElmerOutput to open it. Scroll down till you find:




    StatElecSolve: Capacitance matrix computation performed (i,j,C_ij)
    StatElecSolve:   1  1    5.08013E+00
    StatElecSolve:   1  2    1.70071E+00
    StatElecSolve:   2  2    5.07960E+00

-   Here, our desired result is C~12~ = 1.70071. This value is close to the `1.691` given in the _ but this activity is left for the user. Also, the user is advised to play with the [Clip Filter](FEM_PostFilterClipRegion.md) to get a visual result similar to the first picture of this tutorial.


{{Tutorials navi

}} {{FEM Tools navi}}

---
[documentation index](../README.md) > FEM Example Capacitance Two Balls/it
