---
 TutorialInfo:
   Topic: Finite Element Analysis
   Level: Beginner
   Time: 10 minutes
   Author: http://www.freecadweb.org/wiki/index.php?title=User:Berndhahnebach Bernd
   FCVersion: 0.16.6377 or above
---

# FEM CalculiX Cantilever 3D/en





## Introduction

This example is meant to show how a simple Finite Element Analysis (**FEA**) in FreeCAD\'s [FEM Workbench](FEM_Workbench.md) looks like in the FreeCAD interface and how the results can be visualized. It illustrates how to trigger a FEA and how to change the load value and load direction. Furthermore, since the example file is provided with any FreeCAD installation, it a useful and easy check to run for the purpose of ascertaining if the the FEM Workbench is set up properly.

<img alt="" src=images/FEM_example01_pic10.png  style="width:700px;">

## Requirements

-   A compatible version of FreeCAD designated in the tutorial overview.

    :   Use the **Help → About FreeCAD** to see the version of FreeCAD installed
-   No external software is needed for loading the example file, viewing the mesh and geometry as well as for visualizing the results.
-   For rerunning the FEA the solver software CalculiX has to be installed on your computer. Probably the solver has been installed together with FreeCAD already. If the solver CalculiX is not installed see [FEM Install](FEM_Install.md).

## Set up the example file 

### Load the example file 

-   Start FreeCAD.
-   If the Start Workbench is not activated, load it and open the start page.
-   Open the example \"FemCalculixCantilever3D.FcStd\".

<img alt="" src=images/FEM_example01_pic11.png  style="width:700px;">

### Activate the analysis container 

-   To work with an analysis the analysis has to be activated.
-   In the [tree view](Tree_view.md), double click on the <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> **Analysis**,
-   or right click on the <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> **Analysis** and choose **Activate analysis**.

<img alt="" src=images/FEM_example01_pic12.png  style="width:700px;">

### Analysis container and its objects 

-   If the analysis is activated, FreeCAD itself will change the current workbench to FEM.
-   There are at least 5 objects needed to make a static mechanical analysis.
-   <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> analysis container

1.  <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> a solver
2.  <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> a material
3.  <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:24px;"> a fixed boundary condition
4.  <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> a force load
5.  <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> a FEM mesh

-   In this example, results <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> are already included as well.

### Visualizing Results 

1.  Be sure the analysis is activated.
2.  Be sure the analysis still contains the result object, if not just reload the example file.
3.  Double click the result object <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;">, or select it and click the <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Show result](FEM_ResultShow.md) button in the FEM toolbar.
4.  In the task window, choose `z-Displacement`. It shows `-86.93 mm` in negative z-direction. This makes sense since the force is in negative z-direction as well.
5.  Activate the check box besides the bottom slider of displacement show.
6.  The slider can be used to alter the mesh to view the deformation in a simplified manner.
7.  Choose among the different Result types to view all in the GUI available result types.

<img alt="" src=images/FEM_example01_pic13.png  style="width:400px;">

### Purging Results 

1.  Be sure the analysis is activated.
2.  To remove the results: select in the icon toolbar the <img alt="" src=images/FEM_ResultsPurge.svg  style="width:24px;"> [Purge results](FEM_ResultsPurge.md) button.

### Running the FEA 

-   In the [tree view](Tree_view.md) double click on the solver object <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;">.
-   In the [task panel](Task_panel.md) of the solver object make sure static analysis is selected.
-   Click on **Write .inp file** in the same task window. Watch the log window until it prints \"write completed.\"
-   Click on **Run CalculiX**. Since this is a very small analysis it should take less than a second to run.
-   In the text window it should print in green letters \"CalculiX done without error!\" and in the next line \"loading result sets \...\"
-   You just have finished your first FEA in FreeCAD if there has not been any error message.
-   Click on **Close** in the task window.
-   A new result object should be created. You know how to visualize the results already.
-   If you get an error message no solver binary or similar when triggering the analysis check [FEM Install](FEM_Install.md).

<img alt="" src=images/FEM_example01_pic14.png  style="width:400px;">

### Running the FEA the fast Way 

-   In tree view select the solver object <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> of the analysis <img alt="" src=images/FEM_Analysis.svg  style="width:24px;">.
-   In the icon toolbar click on <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Run solver calculations](FEM_SolverRun.md).
-   The Calculix input file will be written, CalculiX will be triggered and the result object should be created.

### Changing Load Direction and Load Value 

-   In the [tree view](Tree_view.md) expand <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> CCX_Results and select the <img alt="" src=images/FEM_MeshResult.svg  style="width:24px;"> ResultMesh object and press the **Space** key.
    -   **Result:** The visibility of the FEM mesh will be turned off. The geometrical model is still visible.
-   In the [tree view](Tree_view.md) double click on the <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> FEMConstraintForce object to open its [task panel](Task_panel.md)
-   In the task window change the load value to **500000000 N = 500 MN** (**Note:** force unit in task window has to be in N)
-   On the geometrical model click on one of the long edges in x-direction.
-   Click on the **Direction** button.
    -   **Result:** The red arrows that illustrate force will change their direction in x-direction. They indicate the force direction.
-   Since tension should be applied to the box the Reverse Direction needs to be triggered by clicking on it.
-   The red arrows of the force will change their direction.
-   Click on **OK** in task window.

<img alt="" src=images/FEM_example01_pic15.png  style="width:700px;">

-   You know how to trigger an analysis and how to visualize results already.
-   The deformation in x-direction should be 18.95 mm.

<img alt="" src=images/FEM_example01_pic16.png  style="width:400px;">

## What next? 

-   We are now finished with the basic workflow for the [FEM Workbench](FEM_Workbench.md).
-   You are now prepared to do the second [FEM tutorial](FEM_tutorial.md).
-   We will create the CalculiX cantilever by ourselves and compare the results with the beam theory.


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM CalculiX Cantilever 3D/en
