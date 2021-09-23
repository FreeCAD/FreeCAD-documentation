# Manual:Creating FEM analyses/de
{{Manual:TOC/de}}

FEM stands for [Finite Element Method](https://en.wikipedia.org/wiki/Finite_element_method). It is a vast mathematical subject, but in FreeCAD we can think of it as a way to calculate propagations inside a 3D object, by cutting it into small pieces, and analyzing the impact of each small piece on its neighbours. This has several uses in the engineering and electromagnetism fields, but we will focus on one use that is already well developed in FreeCAD, which is simulating deformations in objects which are submitted to forces and weights.

Obtaining such simulation is done in FreeCAD with the [FEM Workbench](FEM_Workbench.md). There are a number of steps: Preparing the geometry, setting its material, performing the meshing, division into smaller parts, like we did in the [Preparing objects for 3D printing](Manual:Preparing_models_for_3D_printing.md) chapter, and finally calculating the simulation.

<img alt="" src=images/Exercise_fem_01.jpg  style="width:600px;">

### Preparing FreeCAD 

The simulation itself is done by another piece of software, that is used by FreeCAD to obtain the results. As there are several interesting open source FEM simulation applications available, the [FEM Workbench](FEM_Workbench.md) allows you to choose between them. However, currently only [CalculiX](http://www.calculix.de/) is fully implemented. Another piece of software, called [NetGen](https://sourceforge.net/projects/netgen-mesher/), which is responsible for generating the subdivision mesh, is also required. Detailed instructions to install these two components are provided [in the FreeCAD documentation](FEM_Install.md).

### Preparing the geometry 

We will start with the house we modeled in the [BIM modeling](Manual:BIM_modeling.md) chapter. However, some changes have to be made to make the model suitable for FEM calculations. This involves, basically, discarding the objects that we don\'t want to include in the calculation, such as the door and window, and joining all the remaining objects into one.

-   Load the [house model](https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd) we modeled earlier
-   Delete or hide the page object, the section planes and the dimensions, leaving only our model
-   Hide the window, the door and the ground slab
-   Also hide the metal beams on the roof. They are very different objects from the rest of the house so we will simplify our calculation by not including them. Instead, we will assume that the roof slab is placed directly on top of the wall.
-   Now move the roof slab down so it rests on top of the wall: Edit the **Rectangle** object that we used as a base of the roof slab, and change its **Placement-\>Position-\>X** value from 3.18m to 3.00m
-   Our model is now clean:

:   <img alt="" src=images/Exercise_fem_02.jpg  style="width:600px;">

-   The FEM Workbench can currently only calculate deformations on a single object. Therefore, we need to join our two objects (the wall and the slab). Switch to the [Part Workbench](Part_Workbench.md), select the two objects, and press the **<img src="images/Part_Fuse.svg" width=16px> [Union](Part_Fuse.md)** button. We have now obtained a fused object:

:   <img alt="" src=images/Exercise_fem_03.jpg  style="width:600px;">

### Creating the analysis 

-   We are now ready to start a FEM analysis. Let\'s switch to the [FEM Workbench](FEM_Workbench.md)
-   Select the fused object
-   Press the **<img src="images/FEM_Analysis.svg" width=16px> [New Analysis](FEM_Analysis.md)** button
-   A new analysis will be created and a settings panels opened. Here you can define the meshing parameters to be used to produce the FEM mesh. The main setting to edit is the **Max Size** which defines the maximum size (in millimeters) of each piece of the mesh. For now, we can leave the default value of 1000:

:   <img alt="" src=images/Exercise_fem_04.jpg  style="width:600px;">

-   After pressing the **OK** button and a few seconds of calculation, our FEM mesh is now ready:

:   <img alt="" src=images/Exercise_fem_05.jpg  style="width:600px;">

-   We can now define the material to be applied to our mesh. This is important because depending on the material strength, our object will react differently to forces applied to it. Select the analysis object, and press the **<img src="images/FEM_MaterialSolid.svg" width=16px> [New Material](FEM_MaterialSolid.md)** button.
-   A task panel will open to allow us to choose a material. In the Material drop-down list, choose the **Concrete-generic** material, and press the **OK** button.

:   <img alt="" src=images/Exercise_fem_06.jpg  style="width:600px;">

-   We are now ready to apply forces. Let\'s start by specifying which faces are fixed into the ground and can therefore not move. Press the **<img src="images/FEM_ConstraintFixed.svg" width=16px> [Constraint fixed](FEM_ConstraintFixed.md)** button.
-   Click on the bottom face of our building and press the **OK** button. The bottom face is designated as unmovable:

:   <img alt="" src=images/Exercise_fem_07.jpg  style="width:600px;">

-   We will now add a load on the top face, that could represent, for example, a massive weight being placed on the roof. For this we will use a pressure constraint. Press the **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Constraint pressure](FEM_ConstraintPressure.md)** button.
-   Click the top face of the roof, set the pressure to **10MPa** (the pressure is applied by square millimeter) and press the **OK** button. Our force is now applied:

:   <img alt="" src=images/Exercise_fem_08.jpg  style="width:600px;">

-   We are now ready to start the calculation. Select the **CalculiX** object in the tree view, and press the **<img src="images/FEM_SolverControl.svg" width=16px> [Start Calculation](FEM_SolverControl.md)** button.
-   In the task panel that will open, click first the **Write .inp file** button to create the input file for CalculiX, then the **Run CalculiX** button. A few moments later, the calculation will be done:

:   <img alt="" src=images/Exercise_fem_09.jpg  style="width:600px;">

-   We can now look at the results. Close the task panel, and see that a new **Results** object has been added to our analysis.
-   Double-click the Results object
-   Set the type of result that you want to see on the mesh, for example \"absolute displacement\", tick the **show** checkbox under **Displacement**, and move the slider next to it. You will be able to see the deformation growing as you apply more force:

:   <img alt="" src=images/Exercise_fem_10.jpg  style="width:600px;">

The results displayed by the FEM workbench are of course currently not enough to perform real-life decisions about structures dimensioning and materials. However, they can already give precious information about how the forces flow through a structure, and which are the weak areas that will feel the most stress.

**Downloads**

-   The file created during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/fem.FCStd>

**Read more**

-   [The FEM Workbench](FEM_Workbench.md)
-   [Installing required FEM components](FEM_Install.md)
-   [CalculiX](http://www.calculix.de)
-   [NetGen](https://sourceforge.net/projects/netgen-mesher)





{{Tutorials navi

}}

---
[documentation index](../README.md) > Manual:Creating FEM analyses/de
