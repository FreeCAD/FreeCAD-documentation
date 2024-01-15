---
 TutorialInfo:s
   Topic:  Finite Element Analysis
   Level:  Beginner/Intermediate
   Time:  30 minutes
   Author: http://www.freecadweb.org/wiki/index.php?title=User: HarryvL
   FCVersion: 0.17.12960 or above
   Files: 
---

# FEM Shear of a Composite Block/es




<div class="mw-translate-fuzzy">




</div>

## Introduction


<div class="mw-translate-fuzzy">

### Introducción

En este tutorial, analizamos la deformación por corte de un bloque compuesto que consiste en un núcleo rígido incrustado en una matriz blanda. Demuestra el uso de BooleanFragments y CompoundFilter para crear sólidos para el bloque y la matriz a partir de dos cubos concéntricos. Este flujo de trabajo garantiza que se puedan definir MeshRegions, materiales y condiciones de contorno separadas para el bloque y la matriz circundante. Para seleccionar regiones internas nos hacemos de la macro por Markus Hovorka (https://github.com/drhooves/SelectionTools). Los resultados de CalculiX muestran claramente el efecto del núcleo rígido en la respuesta del bloque compuesto.


</div>

## Geometry


<div class="mw-translate-fuzzy">

### Geometría

Primero creamos dos cubos concéntricos, un tamaño de 10 mm y el otro tamaño de 5 mm. Esto se hace en el banco de trabajo \"Part\". Por defecto, el cubo se coloca en el origen \[0, 0, 0\], por lo que el cubo más pequeño debe reducirse y cambiarse cambiando la configuración en la pestaña Datos del panel de propiedades. Para hacer visible el núcleo, la transparencia del bloque exterior se establece en 50 en la pestaña Ver del panel de propiedades. El resultado se muestra a continuación.


</div>

<img alt="" src=images/Pic1.png  style="width:700px;">

Next highlight the two blocks in the tree and create a BooleanFragments object (**Part → Split → Boolean Fragments**). In the \"Property Window - Data Tab\" change Mode to CompSolid. Now highlight the BooleanFragments in the Object tree and create a CompoundFilter (**Part → Compound → Compound Filter**).

<img alt="" src=images/Pic2.png  style="width:700px;">

## Mesh and Mesh Regions 

From workbench FEM we create an Analysis container. This will contain all definitions required for the CalculiX analysis and its results. Note that this Analysis container needs to be activated (right-click and select \"Activate analysis\") whenever re-loading the file or after switching back from other analyses. To start the meshing process, highlight the CompoundFilter in the Object Tree and activate the meshing dialog **Mesh → FEM mesh from shape by Gmsh**. Leave the dialog by clicking OK.

A Mesh object is now created in the Object Tree. Highlight this object and create a Mesh Region object via **Mesh → FEM mesh region**. Open the dialog box for this Mesh Region by double clicking and tick the radio button for Solid. Next click the \"Add Reference\" button and select the CompoundFilter object in the Graphical Window. This should add a reference to \"CompoundFilter:Solid1\" in the object list of the Mesh Region. Finally specify the maximum element size for this region (5mm in the current analysis). Leave the dialog by clicking OK.

<img alt="" src=images/Pic3.png  style="width:700px;">

Next create a new Mesh object as above and use the selection macro (shortcut S, E) to select the Cube_Core object in the Graphical Window. This time the reference list should show \"CompoundFilter:Solid2\", as below. Alternatively, you can hide the Compound object and show the Cube_Core object (by expanding the Compound in the tree, selecting each of them and pressing the Spacebar). We chose a maximum element size of 1mm.

Note1: Selection of \"CompoundFilter:Solid2\" requires selection of one of its faces.

Note2: If you have difficulty selecting \"CompoundFilter:Solid2\" it may be because you forgot to set the BooleanFragments mode to CompSolid.

<img alt="" src=images/Pic4.png  style="width:700px;">

## Material Assignment 

Material is assigned to Mesh Regions via a SolidMaterial object. In this tutorial we assign two materials; one for the Matrix and one for the Core.

Start by selecting the CompoundFilter in the object tree. Then create a SolidMaterial object via menu option **Model → FEM material for solid**. Open the dialog and tick the radio button for Solid, press \"Add Reference\" and select the CompoundFilter object from the Graphical Window. The reference list should now show \"CompoundFilter:Solid1\", as before. We assign ABS material to the Matrix, with a Young\'s modulus approximately 1% of that of steel.

<img alt="" src=images/Pic5.png  style="width:700px;">

Repeat the above procedure for the Core (\"CompoundFilter:Solid2\") with the help of the selection macro or the alternative approach discussed before. This time we assign CalculiX-Steel, which is much stiffer than the ABS material for the Matrix.

## Sliding Support 

To create a \"Simple Shear\" condition for the composite block the deformations at the boundaries need to be unconstrained. To achieve this, the block is placed on a sliding support. This leaves three degrees of freedom in the plane of the support (2 translations and a rotation) and those will be constrained later. (Note: as the plane prevents warping of the face, it still induces a minor constraint, which could be eliminated by a different choice of boundary conditions). To create a sliding boundary condition add a FemConstraintDisplacement object (**Model → Mechanical boundary conditions and loads → Displacement boundary condition**). With the dialog box open first select the face to which the boundary condition is to be applied and then click the Add button. As the block is allowed to slide in the x-y plane, only the \"Fixed\" radio button for \"Displacement z\" is selected and the other radio buttons are all left as \"Free\".

<img alt="" src=images/Pic6.png  style="width:700px;">

## Fixed Nodes 

To prevent rigid body motion in the plane of sliding, three independent degrees of freedom need to be eliminated. To achieve this, one vertex in the plane of sliding is constrained in x and y direction (eliminating 2 degrees of freedom) and one vertex is fixed in the x direction (eliminating the last degree of freedom). For this purpose two additional FemConstraintDisplacement objects are created and the result is shown below.

<img alt="" src=images/Pic7.png  style="width:700px;">

## Shear Forces 

The final step in the Analysis definition is the application of loads. To create a Simple Shear condition, a set of shear loads is applied as shown below. Each load is chosen as 1000 N and considering the directions of application, force and moment equilibrium is achieved for all translation and rotational degrees of freedom. In FC this requires addition of four FemConstraintForce objects (**Model → Mechanical boundary conditions and loads → Force load**) - one for each face. With the dialog box open first press the Add Reference button and then select the face to which the boundary condition is to be applied (Note: this is a different sequence than with FemConstraintDisplacement). By default, this creates a set of forces perpendicular to the face (i.e. a normal force). To change this to a shear force, press the direction button and select a cube edge that runs in the desired direction. If the resulting force points in opposite direction of what is required, then select the radio button for \"Reverse direction\".

<img alt="" src=images/Pic8.png  style="width:700px;">

## CalculiX Analysis 

Now all mesh regions, material and boundary conditions have been defined we are ready to analyse the deformation of the block with CalculiX. Activate the Analysis by right clicking \"Activate analysis\", open the CalculiX dialog by double clicking the CalculiXccxTools object and select a directory for the temporary files created by both FC and CCX. Write CCX Input file and check for any warning or error messages.

<img alt="" src=images/PIC9.png  style="width:700px;">

After that the analysis can be started by pressing the RunCalculiX button. If all goes well, the CCX output window should show the following messages.

<img alt="" src=images/Pic10.png  style="width:700px;">

## CalculiX Results 

Upon completion of the analysis double click the \"CalculiX_static_results\" object and select the \"Abs displacement\" option. The maximum displacement of \~ 0.08mm will show up in the relevant output box. As the maximum displacement is relatively small compared to the dimensions of the block (\<1% of the block size), the displacements need to be scaled up. This can be done under the heading \"Displacement\" by ticking the \"Show\" radio button and scaling the displacement by a factor of -say- 20. The maximum displacement will now be exaggerated to approximately 20% of the box size. After closing the dialog window, the deformed mesh can be made visible again by highlighting the Result_mesh object and pressing the space bar.

<img alt="" src=images/Figure_11_Deformed_Mesh.png  style="width:700px;">

To investigate the deformation of the core we have to slice the block. This can be done by creating a clip filter. To activate this functionality, we first need to create a \"post processing pipeline\" by highlighting the \"CalculiX_static_results\" object and choosing **Results → Post Pipeline from Result** from the menu. Next, with the Pipeline selected create a Warp Filter (Results → Warp filter), set Vector=Displacement and Value=20 to scale the displacement and Display Mode = \"Surface with Edges\", Coloring Field = \"Displacement\", Vector = \"Magnitude\" to show colored displacement contours. Press Apply and OK. As a final step add a Clip Filter (Results → Clip filter) and create a plane with origin \[5.0,2.5,5.0\] and normal \[0,1,0\], i.e. at a core face with normal in the y-direction. Tick the \"Cut Cells\" radio button to create a flat surface. As before set Display Mode = \"Surface with Edges\", Coloring Field = \"Displacement\", Vector = \"Magnitude\" to show colored displacement contours. Press Apply and OK. Finally switch the Warp Filter to invisible to only show the cut block.

<img alt="" src=images/Figure12_Deformed_Mesh_Clipped_View_(2).png  style="width:700px;">

From the result it is clear that the core remains largely undeformed and helps to resist the deformation of the soft matrix (compare the shear angle of the blue colored part to that of the green colored part). What it also highlights though is that under Simple Shear conditions the faces of the composite block do warp, implying that the sliding boundary condition at the base of the cube does provide an undue constraint.

## Further work 

The following challenges may be interesting to take up as a further exercise:

1\) Correct for the undue constraint imposed by the sliding boundary condition

2\) Try and create contact boundary conditions between the core and the matrix to see if separation occurs

The FC file for this tutorial is attached below as a starting point.

<https://forum.freecadweb.org/viewtopic.php?f=18&t=26517&start=20>

Que te diviertas !


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Shear of a Composite Block/es
