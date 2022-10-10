---
- TutorialInfo   *   Topic   * Finite Element Analysis
   Level   *Beginner
   Time   *
   Author   *[https   *//wiki.freecadweb.org/User   *Sudhanshu_Dubey Sudhanshu Dubey]
   FCVersion   *0.19 or above
   Files   *
---

# FEM Example Capacitance Two Balls/de





## Einleitung

This example is meant to show how to simulate the 6th example of [Elmer GUI Tutorials](https   *//www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf), **Electrostatic equation -- Capacitance of two balls**, using the new [FEM Examples](FEM_Examples.md). It illustrates how to setup the example, study it\'s various parts, solve it using the [Elmer Solver](FEM_SolverElmer.md) and visualize the results using [Clip Filter](FEM_PostFilterClipRegion.md).

<img alt="" src=images/Two_balls_result_2.png  style="width   *1000px;">

## Voraussetzungen

-   A compatible version of FreeCAD designated in the tutorial overview.

       *   Use the **Help → About FreeCAD** to see the version of FreeCAD installed
-   No external software is needed for loading the example, viewing the mesh and geometry as well as for visualizing the results.
-   For solving the finite element analysis (FEA), the solver software Elmer must be installed on your computer. See [this page](FEM_SolverElmer#Installation.md) for how to install Elmer.

## Das Beispiel vorbereiten 

### Arbeitsbereich FEM laden 

-   FreeCAD starten, Der Arbeitsbereich Start sollte geladen werden.
-   Zum Arbeitsbereich <img alt="" src=images/Workbench_FEM.svg  style="width   *32px;"> [FEM](FEM_Workbench/de.md) wechseln.

### Das Beispiel laden 

-   Go to **Utilities → [<img src=images/FEM_Examples.svg style="width   *24px"> Open FEM examples**.
-   When the GUI opens, find and open \"Electrostatics Capacitance Two Balls\". You can easily find the example in **All** or in **Solvers → Elmer**. For opening the example, either double click on it or select it and click **Setup**.

<img alt="" src=images/Two_balls_selection.png  style="width   *300px;">

## Den Simulationsfall verstehen 

This case presents the solution of the capacitance of perfectly conducting balls in free space. A voltage difference between the balls results to electric charge being introduced to the system. The balls have also self-capacitance that comes from the voltage difference with the far field. Therefore a symmetric capacitance matrix with of size 2 × 2 needs to be solved. The capacitances may be computed from two different voltage configurations.

## Das Modell verstehen 

-   The model contains three spheres.

1.  The two smaller ones are the perfectly conducting balls.
2.  The bigger one is to simulate the surrounding air.

-   The two smaller spheres are fused together and then that fusion is is cut from the bigger sphere.

![ 1000px](images/Two_balls_model_full.png )

## Der Analyse-Container und seine Objekte 

-   There are at least the 7 objects needed to make this electrostatic analysis.
-   <img alt="" src=images/FEM_Analysis.svg  style="width   *24px;"> analysis container

1.  <img alt="" src=images/FEM_SolverElmer.svg  style="width   *24px;"> SolverElmer
2.  <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width   *24px;"> Electrostatic, the electrostatics equation
3.  <img alt="" src=images/FEM_MaterialFluid.svg  style="width   *24px;"> FemMaterial, a fluid material to represent the surrounding air
4.  <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width   *24px;"> ElectrostaticPotential, constraints (3 of them)
5.  <img alt="" src=images/Fem-thermomechanical-analysis.svg  style="width   *24px;"> ConstantVaccumPermittivity, optional
6.  <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width   *24px;"> Mesh, a [Gmsh](FEM_MeshGmshFromShape.md) mesh
7.  <img alt="" src=images/FEM_MeshRegion.svg  style="width   *24px;"> MeshRegion, a mesh region for the smaller spheres

![](images/Two_balls_analysis.png )

## Die FEA durchführen 

-   In [Tree view](Tree_view.md) double click on the solver object <img alt="" src=images/FEM_SolverElmer.svg  style="width   *24px;">.
-   Click on **Write** file in the same task window. Watch the log window until it prints \"write completed.\" You can ignore the warning about the vacuum permittivity that might appear.
-   Click on **Run**. Since this is a small analysis it should take a few seconds to run so wait till you see \"ELMER SOLVER FINISHED AT\" in the output.
-   Click on **Close** in the task window after the run is finished.
-   Two new result objects should be created in the tree view, <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width   *24px;"> SolverElmerResult and <img alt="" src=images/TextDocument.svg  style="width   *24px;"> SolverElmerOutput.

If you get an error message on solver binary or similar when triggering the analysis, check [the installation](FEM_SolverElmer#Installation.md) of Elmer.

## Ergebnisse darstellen 

-   Make sure the mesh is invisible. If not, select the <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width   *24px;"> Mesh object and press **Space** to toggle the visibility.
-   Also make sure the Cut object is invisible.
-   Double click on the <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width   *24px;"> SolverElmerResult object to ope its task dialog.
-   Change the \"Field\" to \"potential\" and press **OK**.
-   You will notice that the color of the sphere has changed to blue and that the gradient on the right is showing values from 0 to 1. It should look something like this   *

<img alt="" src=images/Two_balls_potential.png  style="width   *1000px;">

## Die Ergebnisse nachbearbeiten 

-   While we have successfully visualised the potential result, currently we are only seeing the zero potential in the air surrounding the two balls. To view the potential on the balls we need to apply a [clip filter](FEM_PostFilterClipRegion.md).
-   In the tree view select the <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width   *24px;"> SolverElmerResult object and then from the tool bar click on the button **<img src="images/FEM_PostFilterClipRegion.svg" width=20px> Region Clip Filter**.
-   This will open a dialog with the filter configurations. Click there on the button **<img src="images/list-add.svg" width=16px> Create** and choose <img alt="" src=images/Fem-post-geo-plane.svg  style="width   *24px;"> Plane. This adds a plane through the center of the sphere at which the result mesh is cut. To smooth the cut face, check the option **Cut Cells**. Eventually click **Apply**.

<img alt="" src=images/Two_balls_postcreate.png  style="width   *300px;">

-   In the tree view there is a new entry called Functions. It contains the created <img alt="" src=images/Fem-post-geo-plane.svg  style="width   *24px;"> Plane. Make it invisible using **Space**.
-   Double-click on the <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width   *24px;"> Clip object in the tree view.
-   Change the \"Field\" to \"potential\" and press **OK**.
-   Toggle the visibility of the <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width   *24px;"> SolverElmerResult object using **Space** and you should see something like this   *

<img alt="" src=images/Two_balls_result.png  style="width   *1000px;">

Now we can clearly see that potential distribution in and around the balls.

Note that when <img alt="" src=images/FEM_PostApplyChanges.svg  style="width   *24px;"> [Apply Changes](FEM_PostApplyChanges.md) is on, you would have been able to select the \"Field\" in the clip dialog directly and not to reopen it after the plane was created.

## Finding the Capacitance 

-   Our actual focus is to find the capacitance which is contained in the <img alt="" src=images/TextDocument.svg  style="width   *24px;"> SolverElmerOutput.
-   Double click on <img alt="" src=images/TextDocument.svg  style="width   *32px;"> SolverElmerOutput to open it. Scroll down till you find   *




    StatElecSolve   * Capacitance matrix computation performed (i,j,C_ij)
    StatElecSolve   *   1  1    5.07016E+00
    StatElecSolve   *   1  2    1.69328E+00
    StatElecSolve   *   2  2    5.07201E+00

-   Here, our desired result is C~12~ = 1.69328. This value is close to the `1.691` given in the [Elmer GUI Tutorials](https   *//www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf). We can get an even closer value by making a finer [Mesh Region](FEM_MeshRegion.md) but this activity is left for the user. Also, the user is advised to play with the [Clip Filter](FEM_PostFilterClipRegion.md) to get a visual result similar to the first picture of this tutorial.


 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [FEM](Category_FEM.md) > FEM Example Capacitance Two Balls/de
