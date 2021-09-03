


{{TutorialInfo
|Topic=Finite Element Analysis
|Level=Beginner
|Time=10 minutes + Solver time
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
|FCVersion=0.16.6700 or above
}}

## Introduction

This tutorial is meant to introduce the reader to the basic workflow of the FEM Workbench, as well as most of the tools that are available to perform a static analysis.

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">

## Requirements

-   FreeCAD version 0.16.6700 or above
-   [Netgen](http://sourceforge.net/projects/netgen-mesher/) and/or [GMSH](http://geuz.org/gmsh/) is installed on the system
-   In the case of GMSH, install [Macro GMSH](Macro_GMSH.md) from the [AddonManager](Std_AddonMgr.md), developed by [psicofil](https://github.com/psicofil/Macros_FreeCAD)
-   [Calculix](http://www.calculix.de/) is installed on the system
-   The reader has the basic knowledge to use the [Part](Part_Workbench.md) and [PartDesign Workbenches](PartDesign_Workbench.md)

## Procedure

### Modeling

In this example a Cube is used as the study object, but models created in the Part or PartDesign Workbenches can be used instead.

1.  Create a [new document](Std_New.md) (press on the <img alt="" src=images/Std_New.svg  style="width:24px;"> button)
2.  Activate the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md)
3.  Create a Cube
4.  Change its **Dimensions** to the following:
    1.  Height: 1.000 mm
    2.  Length: 8.000 mm
    3.  Width: 1.000 mm

Now we have a model with which to work with.

### Creating the Analysis {#creating_the_analysis}

#### Netgen

1.  Select the model
2.  Click <img alt="" src=images/FEM_Analysis.svg  style="width:24px;"> [New mechanical analysis](FEM_Analysis.md) from the menu to create an analysis from the object that was selected
3.  In the meshing dialog, click **OK**

You can also drag and drop a mesh to a Mechanical Analysis that does not have a mesh within the [Tree view](Tree_view.md).

#### GMSH

The usage of psicofil\'s macro is recommended, and is used for this example.

1.  Activate the macro
2.  Select the object you wish to use, in this case our Cube
3.  Check the box **Create Mechanical Analysis from mesh**
4.  Click **OK**

We have now meshed our object and are ready to add constraints and forces.

### Constraints and Forces {#constraints_and_forces}

1.  Hide the mesh from the Tree View.
2.  Show the original model
3.  Select <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:24px;"> [Create FEM fixed constraint](FEM_ConstraintFixed.md)
4.  Select the back face of the Cube (face on the **YZ** axis) and click OK
5.  Select <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> [Create FEM force constraint](FEM_ConstraintForce.md)
6.  Select the front face of the Cube (the face parallel to the back face) and set the **Area load** value to 9000000.00
7.  Set the **Direction** to **-Z** by selecting one of the face edges parallel to that direction.
8.  Click OK

We now have established the restrictions and forces for our static study.

### Final preparations {#final_preparations}

1.  Select <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> [Mechanical material\...](FEM_MaterialSolid.md) and choose Calculix as the material
2.  Click **OK**

### Running the Solver {#running_the_solver}

#### Standard Procedure {#standard_procedure}

1.  Select the solver object <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> contained in the 
**Mechanical Analysis**
2.  Select <img alt="" src=images/FEM_SolverControl.svg  style="width:24px;"> [Start calculation](FEM_SolverControl.md) from the menu
3.  Select **Write Calculix Input File**
4.  Select **Run Calculix**
5.  Click **Close**

#### Quick Procedure {#quick_procedure}

1.  Select the solver object <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> contained in the 
**Mechanical Analysis**
2.  Click on <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Quick Analysis](FEM_SolverRun.md).

### Analyzing Results {#analyzing_results}

1.  From the **Object Tree**, select the **Results** object
2.  Select <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Show result](FEM_ResultShow.md)
3.  Choose among the different Result types to view the results
4.  The slider at the bottom can be used to alter the mesh visualization. This allows us to visualize the deformation experienced by the object, keep in mind that this is an approximation.
5.  To remove the results select <img alt="" src=images/FEM_ResultsPurge.svg  style="width:24px;"> [Purge results](FEM_ResultsPurge.md)


{{Note|Comparison to previous example file|If you select the '''Z displacement''' result type, you can see that the obtained value is almost identical to the test example provided by FreeCAD. Differences may occur due to the quality of the mesh and the number of nodes it possesses.}}

We are now finished with the basic workflow for the [FEM Workbench](FEM_Workbench.md).


{{Tutorials navi

}} {{FEM Tools navi}} 
