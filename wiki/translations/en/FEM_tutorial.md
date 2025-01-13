---
 TutorialInfo:
   Topic: Finite Element Analysis
   Level: Beginner
   Time: 10 minutes + Solver time
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei
   FCVersion: 0.17 or above
---

# FEM tutorial/en





## Introduction

This tutorial is meant to introduce the reader to the basic workflow of the FEM Workbench, as well as most of the tools that are available to perform a static analysis.

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">

## Requirements

-   FreeCAD version 0.17 or above.
-   [Netgen](http://sourceforge.net/projects/netgen-mesher/) and/or [GMSH](http://geuz.org/gmsh/) is installed on the system (included in the FreeCAD installation).
-   [Calculix](http://www.calculix.de/) is installed on the system (included in the FreeCAD installation).
-   The reader has the basic knowledge to use the [Part](Part_Workbench.md) and [PartDesign](PartDesign_Workbench.md) Workbenches.

## Procedure

### Modeling

In this example a Cube is used as the study object, but any model created in the Part or PartDesign Workbenches can be used instead.

1.  Press the **![](images/)_[Std_New](Std_New.md)** button to create a new document.
2.  Activate the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md).
3.  Create a Cube.
4.  Change its **Dimensions** to the following:
    1.  Length: 8.000 m.
    2.  Width: 1.000 m.
    3.  Height: 1.000 m.

Now we have a model to work with.

### Creating the Analysis 

1.  Activate the <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM Workbench](FEM_Workbench.md).
2.  Select the **Model → <img src="images/FEM_Analysis.svg" width=16px> Analysis container‏‎** option from the menu.

### Constraints and Forces 

1.  Hide the mesh from the Tree View.
2.  Show the original model.
3.  Select <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:24px;"> [Create FEM fixed constraint](FEM_ConstraintFixed.md).
4.  Click **Add**, select the back face of the Cube object (face on the **YZ** axis) and click **OK**.
5.  Select <img alt="" src=images/FEM_ConstraintForce.svg  style="width:24px;"> [Create FEM force constraint](FEM_ConstraintForce.md).
6.  Click **Add**, select the front face of the Cube object (the face parallel to the back face) and set the **Force \[N\]** value to 9000000.
7.  Set the **Direction** to **-Z** by selecting one of the face edges parallel to that direction.
8.  Click **OK**.

We now have established the restrictions and forces for our static study.

### Material

1.  Select <img alt="" src=images/FEM_MaterialSolid.svg  style="width:24px;"> [Material for solid](FEM_MaterialSolid.md) and choose Calculix-Steel as the material.
2.  Click **OK**.

### Meshing

It is recommended to make a mesh as the last step in the analysis preparations due to association to a geometry in FreeCAD. Depending on FreeCAD installation, there can be Netgen or GMSH meshers, you can use any of them.

#### Netgen

1.  Select the model.
2.  <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:24px;"> [FEM mesh from shape by Netgen](FEM_MeshNetgenFromShape.md): Generates a finite element mesh for a model using Netgen.
3.  In the meshing dialog, click **Apply** and **OK**.

You can also drag and drop a mesh to a Mechanical Analysis that does not have a mesh within the [Tree view](Tree_view.md).

#### GMSH

1.  Select the model
2.  <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md): Generates a finite element mesh for a model using Gmsh.
3.  In the meshing dialog, click **Apply** and **OK**.

We have now meshed our object and are ready to add constraints and forces.

### Running the Solver 

#### Standard Procedure 

1.  Select the solver object <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> contained in the **Analysis** container.
2.  Select <img alt="" src=images/FEM_SolverControl.svg  style="width:24px;"> [Solver job control](FEM_SolverControl.md) from the menu.
3.  Select **Write .inp File**.
4.  Select **Run CalculiX**.
5.  Click **OK**.

#### Quick Procedure 

1.  Select the solver object <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> contained in the **Analysis** container.
2.  Click on <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Run solver calculations](FEM_SolverRun.md).

### Analyzing Results 

1.  From the **Object Tree**, select the **CCX_Results** object.
2.  Select <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Show result](FEM_ResultShow.md).
3.  Choose among the different Result types to view the results.
4.  The slider at the bottom can be used to alter the mesh visualization. This allows us to visualize the deformation experienced by the object, keep in mind that this is an approximation.
5.  To remove the results select <img alt="" src=images/FEM_ResultsPurge.svg  style="width:24px;"> [Purge results](FEM_ResultsPurge.md).


{{Note|Comparison to previous example file|If you select the '''Z displacement''' result type, you can see that the obtained value is almost identical to the test example provided by FreeCAD. Differences may occur due to the quality of the mesh and the number of nodes it possesses.}}

We are now finished with the basic workflow for the [FEM Workbench](FEM_Workbench.md).

## Notes

-   For a video tutorial based on this written tutorial watch: [FEM MaterialReinforced tutorial](https://www.youtube.com/watch?v=SZTIqhfCSVc).


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM tutorial/en
