# FEM Shear of a Composite Block/pl
---
 TutorialInfo:
   Topic:  Finite Element Analysis
   Level:  Beginner/Intermediate
   Time:  30 minutes
   Author: http://www.freecadweb.org/wiki/index.php?title=User: HarryvL
   FCVersion: 0.17.12960 or above
}}

## Introduction

In this tutorial we analyse the shear deformation of a composite block consisting of a stiff core embedded in a soft matrix. It demonstrates the use of BooleanFragments and CompoundFilter to create solids for the block and the matrix from two concentric cubes. This workflow ensures that separate MeshRegions, Materials and Boundary Conditions can be defined for the block and the surrounding matrix. To select internal regions we make us of the macro by Markus Hovorka . The CalculiX results clearly show the effect of the stiff core on the response of the composite block.

## Geometry

First we create two concentric cubes, one size 10mm and the other size 5mm. This is done in the workbench \"Part\". By default the cube is placed at the origin \0, 0, 0\, so the smaller cube needs to be scaled down and shifted by changing the settings in the Data tab of the property panel. To make the core visible, the Transparency of the outer block is set to 50 in the View tab of the property panel. The result is shown below.

!{width="700"}

Next highlight the two blocks in the tree and create a BooleanFragments object . In the \"Property Window - Data Tab\" change Mode to CompSolid. Now highlight the BooleanFragments in the Object tree and create a CompoundFilter .

!{width="700"}

## Mesh and Mesh Regions 

From workbench FEM we create an Analysis container. This will contain all definitions required for the CalculiX analysis and its results. Note that this Analysis container needs to be activated  whenever re-loading the file or after switching back from other analyses. To start the meshing process, highlight the CompoundFilter in the Object Tree and activate the meshing dialog \"Mesh , FEM mesh from shape by Gmsh\". Leave the dialog by clicking OK.

A Mesh object is now created in the Object Tree. Highlight this object and create a Mesh Region object via \"Mesh , FEM mesh region\". Open the dialog box for this Mesh Region by double clicking and tick the radio button for Solid. Next click the \"Add Reference\" button and select the CompoundFilter object in the Graphical Window. This should add a reference to \"CompoundFilter:Solid1\" in the object list of the Mesh Region. Finally specify the maximum element size for this region . Leave the dialog by clicking OK.

!{width="700"}

Next create a new Mesh object as above and use the selection macro  to select the Cube_Core object in the Graphical Window. This time the reference list should show \"CompoundFilter:Solid2\", as below. We chose a maximum element size of 1mm.

Note1: Selection of \"CompoundFilter:Solid2\" requires selection of one of its faces.

Note2: If you have difficulty selecting \"CompoundFilter:Solid2\" it may be because you forgot to set the BooleanFragments mode to CompSolid.

!{width="700"}

## Material Assignment 

Material is assigned to Mesh Regions via a SolidMaterial object. In this tutorial we assign two materials; one for the Matrix and one for the Core.

Start by selecting the CompoundFilter in the object tree. Then create a SolidMaterial object via menu option \"Model , FEM material for solid\". Open the dialog and tick the radio button for Solid, press \"Add Reference\" and select the CompoundFilter object from the Graphical Window. The reference list should now show \"CompoundFilter:Solid1\", as before. We assign ABS material to the Matrix, with a Young\'s modules approximately 1% that of steel.

!{width="700"}

Repeat the above procedure for the Core  with the help of the selection macro. This time we assign CalculiX-Steel, which is much stiffer than the ABS material for the Matrix.

## Sliding Support 

To create a \"Simple Shear\" condition for the composite block the deformations at the boundaries need to be unconstrained. To achieve this, the block is placed on a sliding support. This leaves three degrees of freedom in the plane of the support  and those will be constrained later. . To create a sliding boundary condition add a FemConstraintDisplacement object . With the dialog box open first select the face to which the boundary conditions is to be applied and then click the Add button. As the block is allowed to slide in the x-y plane, only the \"Fixed\" radio button for \"Displacement z\" is selected and the other radio buttons are all left as \"Free\".

!{width="700"}

## Fixed Nodes 

To prevent rigid body motion in the plane of sliding, three independent degrees of freedom need to be eliminated. To achieve this, one vertex in the plane of sliding is constrained in x and y direction  and one vertex is fixed in the x direction . For this purpose two additional FemConstraintDisplacement objects are created and the result is shown below.

!{width="700"}

## Shear Forces 

The final step in the Analysis definition is the application of loads. To create a Simple Shear condition, a set of shear loads is applied as shown below. Each load is chosen as 1000 N and considering the directions of application, force and moment equilibrium is achieved for all translation and rotional degrees of freedom. In FC this requires addition of four FemConstraintForce objects  - one for each face. With the dialog box open first press the Add Reference button and then select the face to which the boundary condition is to be applied . By default, this creates a set of forces perpendicular to the face . To change this to a shear force, press the direction button and select a cube edge that runs in the desired direction. If the resulting force points in opposite direction of what is required, then select the radio button for \"Reverse direction\".

!{width="700"}

## CalculiX Analysis 

Now all mesh regions, material and boundary conditions have been defined we are ready to analyse the deformation of the block with CalculiX. Activate the Analysis by right clicking \"Activate analysis\", open the CalculiX dialog by double clicking the CalculiXccxTools object and select a directory for the temporary files created by both FC and CCX. Write CCX Input file and check for any warning or error messages.

!{width="700"}

After that the analysis can be started by pressing the RunCalculiX button. If all goes well, the CCX output window should show the following messages.

!{width="700"}

## CalculiX Results 

Upon completion of the analysis double click the \"CalculiX_static_results\" object and select the \"Abs displacement\" option. The maximum displacement of \~ 0.08mm will show up in the relevant output box. As the maximum displacement is relatively small compared to the dimensions of the block , the displacements need to be scaled up. This can be done under the heading \"Displacement\" by ticking the \"Show\" radio button and scaling the displacement by a factor of -say- 20. The maximum displacement will now be exaggerated to approximately 20% of the box size. After closing the dialog window, the deformed mesh can be made visible again by highlighting the Result_mesh object and pressing the space bar.

!{width="700"}

To investigate the deformation of the core we have to slice the block. This can be done by creating a clip filter. To activate this functionality, we first need to create a \"post processing pipeline\" by highlighting the \"CalculiX_static_results\" object and choosing \"Results , Post Pipeline from Result\" from the menu. Next, with the Pipeline selected create a Warp Filter , set Vector=Displacement and Value=20 to scale the displacement and Display Mode = \"Surface with Edges\", Coloring Field = \"Displacement\", Vector = \"Magnitude\" to show colored displacement contours. Press Apply and OK. As a final step add a Clip Filter  and create a plane with origin \5.0,2.5,5.0\ and normal \0,1,0\, i.e. at a core face with normal in the y-direction. Tick the \"Cut Cells\" radio button to create a flat surface. As before set Display Mode = \"Surface with Edges\", Coloring Field = \"Displacement\", Vector = \"Magnitude\" to show colored displacement contours. Press Apply and OK. Finally switch the Warp Filter to invisible to only show the cut block.

!.png "Figure12_Deformed_Mesh_Clipped_View_.png"){width="700"}

From the result it is clear that the core remains largely undeformed and helps to resist the deformation of the soft matrix . What it also highlights though is that under Simple Shear conditions the faces of the composite block do warp, implying that the sliding boundary condition at the base of the cube does provide an undue constraint.

## Further work 

The following challenges may be interesting to take up as a further exercise:

1\) Correct for the undue constraint imposed by the sliding boundary condition

2\) Try and create contact boundary conditions between the core and the matrix to see if separation occurs

The FC file for this tutorial is attached below as a starting point.

<https://forum.freecadweb.org/viewtopic.php?f=18&t=26517&start=20>

Have fun !


{{FEM Tools navi

}} {{Userdocnavi
---



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Shear of a Composite Block/pl
