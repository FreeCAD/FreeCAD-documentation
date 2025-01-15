# Tutorials/pt-br
<div class="mw-translate-fuzzy">

Esta página apresenta uma seleção de tutoriais escritos de alta qualidade. Uma lista completa e não classificada de tutoriais pode ser encontrada em [:Category:Tutorials](:Category_Tutorials.md), uma lista completa e classificável pode ser encontrada em [tabela abaixo](#Tutoriais_-_Lista_completa.md).


</div>


<div class="mw-translate-fuzzy">

Se você gostaria de contribuir escrevendo documentação e tutoriais wiki, veja as diretrizes gerais do wiki em [PaginasWiki](WikiPages/pt-br.md), e leia as [orientações para tutoriais](tutorial_guidelines/pt-br.md).


</div>

Observe a versão do FreeCAD usada no tutorial, pois alguns tutoriais podem usar uma versão antiga do programa. Embora o processo de modelagem geral ainda possa funcionar, algumas ferramentas podem ter mudado.

See also [video tutorials](Video_tutorials.md) and [books](Books.md).



## Arquitetura e BIM 

<File:Arch> tutorial 00.jpg\|link=[Arch_tutorial](Arch_tutorial.md)\|[Arch_tutorial](Arch_tutorial.md) (v0.14)
This is the essential introduction to the Arch Workbench. It is extensive and showcases a typical workflow, from importing plans in DXF format to building the 3D model.

<File:Exercise> arch 01.jpg\|link=[Manual:BIM_modeling](Manual_BIM_modeling.md)\|[BIM modeling](Manual_BIM_modeling.md)
How to model a small house, produce a blueprint with TechDraw, and export to IFC.

<File:11_T01_window_all_symbol_top.png%7Clink=>[Tutorial_for_open_windows](Tutorial_for_open_windows.md)\|[Open windows and doors](Tutorial_for_open_windows.md) (v0.18)
How to display windows and doors as open, with elevation and plan symbols, and produce a basic floor plan with TechDraw.

<File:17_T02_sketch_2_attached_correctly.png%7Clink=>[Tutorial_custom_placing_of_windows_and_doors](Tutorial_custom_placing_of_windows_and_doors.md)\|[Design custom windows](Tutorial_custom_placing_of_windows_and_doors.md) (v0.18)
How to draw custom doors and windows using the Sketcher, and adjust their normals to correctly place them in walls.

<File:Arch_panel_tutorial_01.jpg%7Clink=>[Arch_panel_tutorial](Arch_panel_tutorial.md)\|[Arch panel tutorial](Arch_panel_tutorial.md) (v0.15)
Modeling a microhouse roof panel by using the Sketcher, the Window tool, and the Panel tool.

<File:Arch_Wikihouse_01.jpg%7Clink=>[Wikihouse_porting_tutorial](Wikihouse_porting_tutorial.md)\|[WikiHouse modelling](Wikihouse_porting_tutorial.md)
Re-modeling the WikiHouse project using sketches and panels, starting from importing a mesh model created in SketchUp.



## Modelagem de peças 

FreeCAD provides two main workflows to modeling parts:

-   combining objects, a method called [Constructive solid geometry](Constructive_solid_geometry.md) (CSG) using the [Part Workbench](Part_Workbench.md), and
-   using parametric modelling and [feature editing](Feature_editing.md) with the [PartDesign Workbench](PartDesign_Workbench.md).

Observe que o fluxo de trabalho [Bancadas de trabalho PartDesign](PartDesign_Workbench/pt-br.md) foi consideravelmente alterado do FreeCAD 0.17 em diante; alguns dos tutoriais não foram atualizados e podem se referir à versão 0.16.


<div class="mw-translate-fuzzy">

<File:GGTuto1> Vue.PNG\|link=[Creating a simple part with Part WB](Creating_a_simple_part_with_Part_WB.md)\|[Criando uma peça simples com a bancada Part](Creating_a_simple_part_with_Part_WB/pt-br.md)
Uma introdução ao FreeCAD e Bancada Part usando sólidos primitivos.


</div>

<File:GGTuto1> Vue.PNG\|link=[Creating_a_simple_part_with_Draft_and_Part_WB](Creating_a_simple_part_with_Draft_and_Part_WB.md)\|[Creating a simple part with Draft and Part Workbench](Creating_a_simple_part_with_Draft_and_Part_WB.md)
An introduction to modeling solids with Draft Workbench by creating a 2d profile in draft.

<File:GGTuto1> Vue.PNG\|link=[Creating_a_simple_part_with_PartDesign](Creating_a_simple_part_with_PartDesign.md)\|[Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md) (v0.17)
An introduction to the PartDesign workflow: tracing a sketch, using pad, pocket, and moving the object.

Pd_tut_final_solid.png\|link=[Basic_Part_Design_Tutorial](Basic_Part_Design_Tutorial.md)\|[Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md) (v0.17)
Model a simple part using a feature editing methodology: creating a sketch, using pad, external references, pocket, and mirror.

Pd_tut_final_solid.png\|link=[Basic_Part_Design_Tutorial_019](Basic_Part_Design_Tutorial_019.md)\|[Basic Part Design Tutorial 019](Basic_Part_Design_Tutorial_019.md) (v0.19 or above)
An updated version of the previous tutorial that creates the same model using techniques that avoid the [topological naming problem](Topological_naming_problem.md).

TBHS-model.png\|link=[Toothbrush_Head_Stand](Toothbrush_Head_Stand.md)\|[Model an electric toothbrush head stand](Toothbrush_Head_Stand.md) (v0.16 or above)
Multiple features used: sketch, distance and coincident constraints, pad, external references, fillet, chamfer, linear pattern, and draft.

Exercise lego 01.jpg\|link=[Manual:Modeling_for_product_design](Manual_Modeling_for_product_design.md)\|[Modeling for product design](Manual_Modeling_for_product_design.md) (v0.16)
Modeling a Lego block: sketches, vertical and horizontal distance constraints, pad, pocket, external reference, linear pattern, and assembly.

Exercise table complete.jpg\|link=[Manual:Traditional_modeling,\_the_CSG_way](Manual:Traditional_modeling,_the_CSG_way.md)\|[Traditional modeling, the CSG way](Manual:Traditional_modeling,_the_CSG_way.md)
Modeling a table by using simple solids like cubes and cylinders, and performing boolean operations (fusions and cuts) with them.

08_T04_Part_ShapesString_Extrude_final_cut.png\|link=[Draft_ShapeString_tutorial](Draft_ShapeString_tutorial.md)\|[Draft ShapeString tutorial](Draft_ShapeString_tutorial.md) (v0.19)
Create engraved text on a solid: extrude a shapestring to make it solid, then use a boolean cut to carve it from another solid.

10_T03_Part_ball_fillet.png\|link=[Whiffle_Ball_tutorial](Whiffle_Ball_tutorial.md)\|[Create a wiffle ball](Whiffle_Ball_tutorial.md) (v0.19)
Use solid primitives, like cubes and cylinders, and boolean operations, like union and cut, to create a hollowed ball.

Tutorial-normand06.jpg\|link=[Basic_modeling_tutorial](Basic_modeling_tutorial.md)\|[Basic modeling tutorial](Basic_modeling_tutorial.md)
Create an iron angle by two methods: using solid primitives, and boolean operations (CSG); and by extruding a planar profile.

<File:HTCaeroplane04.png%7Clink=>[Aeroplane](Aeroplane.md)\|[Aeroplane tutorial](Aeroplane.md)
Understand placements in FreeCAD by creating a simple aeroplane model. Then learn about rotation angles, yaw (Z), pitch (Y), and roll (X).

<File:T13_14_Threads_components.png%7Clink=>[Thread_for_Screw_Tutorial](Thread_for_Screw_Tutorial.md)\|[Thread for screw tutorial](Thread_for_Screw_Tutorial.md) (v0.19)
Understand how to create threads with several techniques that include use of the tools [Part Helix](Part_Helix.md), [PartDesign AdditivePipe](PartDesign_AdditivePipe.md), [Part Sweep](Part_Sweep.md), [Part Fuse](Part_Fuse.md), and [Part Cut](Part_Cut.md).

The Raspberry Pi project has made simple tutorials that are easy to follow, particularly for those new to CAD systems:

-   [freecad-dice](https://projects.raspberrypi.org/en/projects/freecad-dice), model a die with six faces, and optionally 3D print it.
-   [freecad-headphone-tidy](https://projects.raspberrypi.org/en/projects/freecad-headphone-tidy), model a spool to organize and store earphones, and optionally 3D print it.
-   [freecad-chess-set](https://projects.raspberrypi.org/en/projects/freecad-chess-set), model and entire chess set in Bauhaus modernist style.
-   [raspberrypilearning](https://github.com/raspberrypilearning?utf8=%E2%9C%93&q=freecad&type=source&language=) repository (CC-BY 4.0) with other examples.



## Esboço e desenho 

Exercise cabin 01.jpg\|link=[Manual:Traditional_2D_drafting](Manual_Traditional_2D_drafting.md)\|[Traditional 2D drafting](Manual_Traditional_2D_drafting.md)
Draw a floor plan with lines, wires, rectangles, circular arcs, and add hatch patterns, annotations, and dimensions. Export the result to DXF.

00_Dr01_Draft_Tutorial_final.png\|link=[Draft_tutorial](Draft_tutorial.md)\|[Draft tutorial](Draft_tutorial.md) (v0.19)
This is a basic introduction to the tools of the [Draft Workbench](Draft_Workbench.md): working plane, grid, line, arc, upgrade, rectangle, circle, polygon, arrays, dimensions, annotations, and shapestring.

Sketcher_reference.png\|link=[Sketcher_Lecture](Sketcher_Lecture.md)\|[Sketcher Lecture](Sketcher_Lecture.md) (v0.19)
This is a more than 80 page PDF document that serves as a detailed manual for the [Sketcher Workbench](Sketcher_Workbench.md). It explains the basics of Sketcher usage, and goes into a lot of detail about the creation of geometrical shapes, and each of the constraints.

09b_Sk01_Sketcher_fully_constrained_clean.png\|link=[Basic_Sketcher_Tutorial](Basic_Sketcher_Tutorial.md)\|[Basic_Sketcher_Tutorial](Basic_Sketcher_Tutorial.md) (v0.19)
This is a basic introduction to the tools of the Sketcher Workbench: construction mode, line, circle, arc, constraints (equality, vertical, horizontal, tangential, distance, angle, radius).

03d_Sk02_Sketcher_Rectangle_constrained_length.png\|link=[Sketcher_Micro_Tutorial\_-\_Constraint_Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)\|[Sketcher constraints practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md) (v0.19)
Learn to efficiently constrain a sketch. Prefer geometric constraints over datum constraints.

## Technical Drawings 

TDTut ProjGroup21.png\|link=[Basic_TechDraw_Tutorial](Basic_TechDraw_Tutorial.md)\|[Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md) (v0.17)
This is the essential introduction to the tools of the TechDraw Workbench: page, view, scale, vertical and horizontal dimensions, annotations, projection groups, linking dimensions to the 3D view.

<File:FCTemplateHow.png%7Clink=>[TechDraw_TemplateHowTo](TechDraw_TemplateHowTo.md)\|[Creating a new background template](TechDraw_TemplateHowTo.md) (v0.17)
Instructions to create a page template in Inkscape for using it with the TechDraw Workbench. Determine the size of the sheet, draw a frame for the page, define fixed text, and editable text fields.

<File:AnHi1.png%7Clink=>[Measurement_Of_Angles_On_Holes](Measurement_Of_Angles_On_Holes.md)\|[Measurement Of Angles On Holes](Measurement_Of_Angles_On_Holes.md) (v0.19)
Instructions for adding center lines and subsequent angle representations on holes.

## FEM

FEM locally refined mesh.PNG\|link=[FEM_Geometry_Preparation_and_Meshing](FEM_Geometry_Preparation_and_Meshing.md)\|[FEM Geometry Preparation and Meshing](FEM_Geometry_Preparation_and_Meshing.md) (v0.21)
This is a general reference for the most common issues related to geometry preparation and meshing for FEM. It contains several tips and explains the current capabilities of the FEM workbench in terms of geometry and mesh handling.

FEM example01 pic00.jpg\|link=[FEM_CalculiX_Cantilever_3D](FEM_CalculiX_Cantilever_3D.md)\|[CalculiX cantilever FEM analysis](FEM_CalculiX_Cantilever_3D.md) (v0.20)
This is an example included in every installation of FreeCAD; it demonstrates a basic analysis with the CalculiX FE solver. Purge the current result, re-run the solver, and view the displacements and stresses in the deformed mesh in the viewport.

FEM tutorial result.png\|link=[FEM_tutorial](FEM_tutorial.md)\|[Simple FEM introduction](FEM_tutorial.md) (v0.20)
This is a short introduction to the steps required to perform an analysis in the FEM Workbench: model your object, create a mesh, add constraints and forces, add a material, run the solver, and visualize the results.

Figure 11 Deformed Mesh.png\|link=[FEM_Shear_of_a_Composite_Block](FEM_Shear_of_a_Composite_Block.md)\|[FEM shear analysis of a composite block](FEM_Shear_of_a_Composite_Block.md) (v0.17)
Study the deformation of a block made of a hard nucleus surrounded by a softer material: create mesh regions, add materials, set up sliding constraints, add shear loads, run the solver, and visualize the results with a clip plane.

Femconcrete_Wall_3D_rx_PSS.png\|link=[Analysis_of_reinforced_concrete_with_FEM](Analysis_of_reinforced_concrete_with_FEM.md)\|[Analysis of reinforced concrete with FEM](Analysis_of_reinforced_concrete_with_FEM.md) (v0.19)
Estimate the level of reinforcement required in a concrete structure to prevent brittle failure under tension or shear.

Two_balls_result_2-cropped.png\|link=[FEM_Example_Capacitance_Two_Balls](FEM_Example_Capacitance_Two_Balls.md)\|[Electrostatic equation -- Capacitance of two balls](FEM_Example_Capacitance_Two_Balls.md) (v0.19)
This example shows how to simulate a capacitance. It illustrates how to setup the example, study its various parts, solve it using the [Elmer Solver](FEM_SolverElmer.md) and visualize the results using [Clip Filter](FEM_PostFilterClipRegion.md).

FEM_post-processing_Paraview.png\|link=[Post-Processing_of_FEM_Results_with_Paraview](Post-Processing_of_FEM_Results_with_Paraview.md)\|[Post-Processing of FEM results with Paraview](Post-Processing_of_FEM_Results_with_Paraview.md) (v0.19)
This tutorial explains the basics of transferring data from the FEM Workbench to Paraview and shows some of the options and settings for displaying data.



## CNC & Impressão 3D 

Path-WalkThroughResult.gif\|link=[CAM_Walkthrough_for_the_Impatient](CAM_Walkthrough_for_the_Impatient.md)\|[CAM Workbench for the impatient](CAM_Walkthrough_for_the_Impatient.md)
This is a quick presentation of the workflow for the CAM Workbench: create a job, define the output, define the milling tool, define the path operations, start the simulation, and generate a G-code output file.

Exercise meshing 03.jpg\|link=[Manual:Preparing_models_for_3D_printing](Manual_Preparing_models_for_3D_printing.md)\|[Preparing models for 3D printing](Preparing_models_for_3D_printing.md) (v0.16)
Convert a solid object to a mesh object using the Mesh Workbench, export the mesh to STL format, and use Slic3r to prepare the G-code. Alternatively use the Cura Workbench or the CAM Workbench to generate the G-code.



## Renderização

Exercise raytracing 05.jpg\|link=[Manual:Creating_renderings](Manual_Creating_renderings.md)\|[Creating renderings](Manual_Creating_renderings.md)
Quickly produce a rendered image of your bodies with POV-Ray and LuxRender, if they are installed in your system.

Raytracing tutorial result.png\|link=[Raytracing_tutorial](Raytracing_tutorial.md)\|[Raytracing_tutorial](Raytracing_tutorial.md) (v0.16)
Describes the basic workflow of the Raytracing Workbench using POV-Ray or LuxRender: set the path to the renderers, create a project, set the camera position, select the model, run the renderer.

12_T04_FreeCAD_POVray_render_floor_wood_walls_radiosity_final.png\|link=[Tutorial_FreeCAD_POV_ray](Tutorial_FreeCAD_POV_ray.md)\|[Intermediate FreeCAD and POV-ray tutorial](Tutorial_FreeCAD_POV_ray.md) (v0.18)
Workflow to produce a better render with POV-Ray: create a project, add objects, set the camera, save the .pov file, manually edit the file to improve the textures, planes, lights, and then run the renderer.

07_T03_FreeCAD_Blender_EEVEE_render.png\|link=[Tutorial_Render_with_Blender](Tutorial_Render_with_Blender.md)\|[Rendering a FreeCAD assembly with Blender](Tutorial_Render_with_Blender.md) (v0.18)
Export bodies from FreeCAD to Wavefront .obj, import the file into Blender, set up a simple Sun light, assign basic materials with the Principled BSDF shader, and produce a rendered image with EEVEE and Cycles.

## Robot workbench 


<div class="mw-translate-fuzzy">

## Bancada de trabalho Robot 


</div>

Robot Tutorial RobotSimulation.gif\|link=[Robot_tutorial](Robot_tutorial.md)\|[Robot tutorial](Robot_tutorial.md) (v0.17)
Simulate the movement of an industrial robot: set up a trajectory, set up home position, change the robot position, insert various waypoints, and simulate the robot movement.

## Scripting

These are tutorials that are related to scripting or programming. They are geared towards more experienced users, who are already somewhat familiar with the program.

-   [Python scripting tutorial](Python_scripting_tutorial.md)
-   [How to install macros](How_to_install_macros.md)
-   [How to install additional workbenches](How_to_install_additional_workbenches.md)

## Tutorials - Comprehensive list 


<div class="mw-translate-fuzzy">

## Tutoriais - Lista completa 

Aqui estão listados todos os tutoriais que não estão no manual *\"independentemente de sua qualidade\"*. Se um tutorial estiver listado no [:Category:Tutorials/pt-br](:Category:Tutorials/pt-br.md) e não nesta tabela, favor inseri-lo aqui.


</div>

++++++++
| Tutorial                                                                                                                | Topic                   | Level                 | Time to complete hh:mm | Authors                                                                                        | FreeCAD version     | Example files                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                         |                         |                       |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                         |                         |                       |                        |                                                                                                |                     | \<!\-- Template for new entries                                                                                                                                                                                                                                                                                               |
+=========================================================================================================================+=========================+=======================+========================+================================================================================================+=====================+===============================================================================================================================================================================================================================================================================================================================+
| [Tutorial](Tutorial.md)                                                                                         | Topic                   | Level                 | 0:00                   | [Name](User_Name.md)                                                                   | 1.0                 | None \--\>                                                                                                                                                                                                                                                                                                                    |
++++++++
| [Add Button to FEM Toolbar Tutorial](Add_Button_to_FEM_Toolbar_Tutorial.md)                                     | Finite Element Analysis |                       |                        | [JohnWang](User_JohnWang.md)                                                           |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Add FEM Constraint Tutorial](Add_FEM_Constraint_Tutorial.md)                                                   | Finite Element Analysis |                       |                        | [M42kus](User_M42kus.md)                                                               |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Add FEM Equation Tutorial](Add_FEM_Equation_Tutorial.md)                                                       | Finite Element Analysis |                       |                        | [JohnWang](User_JohnWang.md)                                                           |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Advanced Attachment OYX](Advanced_Attachment_OYX.md)                                                           | Attachment              | Intermediate/Advanced |                        | [drmacro](User_drmacro.md)                                                             | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Advanced TechDraw Tutorial (unfinished)](Advanced_TechDraw_Tutorial.md)                                        | TechDraw Workbench      | Advanced              |                        | [domad](User_domad.md)                                                                 | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Aeroplane](Aeroplane.md)                                                                                       | Part Workbench          | Beginner              | 0:10                   | Hughthecat                                                                                     |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Analysis of reinforced concrete with FEM](Analysis_of_reinforced_concrete_with_FEM.md)                         | Finite Element Analysis | Intermediate          | 1:00                   | [HarryvL](User_HarryvL.md)                                                             | 0.19 or above       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Arch panel tutorial](Arch_panel_tutorial.md)                                                                   | BIM Workbench           | Beginner              | 1:00                   | Yorik                                                                                          |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Arch tutorial](Arch_tutorial.md)                                                                               | BIM Workbench           | Intermediate          |                        | [Yorik](User_Yorik.md)                                                                 | 0.14                |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md)                                                       | Attachment              | Beginner/intermediate | 1:00                   | [Bance](User_Bance.md)                                                                 | 0.17 or above       | [Basic Attachment Tutorial.FCStd](https://github.com/BanceFC/Examples/blob/master/Basic_Attachment_Tutorial.FCStd)                                                                                                                                                                                                            |
++++++++
| [Basic modeling tutorial](Basic_modeling_tutorial.md)                                                           | Modelling               | Beginner              | 0:15                   | [NormandC](User_NormandC.md)                                                           | Any                 | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md)                                                     | Modeling                | Beginner              |                        | [Mark Stephen (Quick61)](User_Quick61.md) and [HarryGeier](User_HarryGeier.md) | 0.17 or above       | [Basic Part Design for v0.17](https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd)                                                                                                                                                              |
++++++++
| [Basic Part Design Tutorial 019](Basic_Part_Design_Tutorial_019.md)                                             | Modeling                | Beginner              | 1:00                   | [Carlo Dormeletti](User_Onekk.md) and [Ed Williams](User_Edwilliams16.md)      | 0.19 or above       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md)                                                           | Sketcher Workbench      | Beginner              | 1:00                   | [Drei](User_Drei.md) and [Vocx](User_Vocx.md)                                  | 0.19                | [Basic Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=43594)                                                                                                                                                                                                                                            |
++++++++
| [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md)                                                           | TechDraw Workbench      | Beginner              |                        | [WandererFan](User_WandererFan.md)                                                     | 0.17 or above       | [Basic Part Design for v0.17 Sample](https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd) [Basic TechDraw Tutorial Sample](https://github.com/FreeCAD/Examples/blob/master/Basic_TechDraw_Tutorial_Example_Files/Basic_TechDraw_Tutorial.fcstd) |
++++++++
| [BIM ingame tutorial](BIM_ingame_tutorial.md)                                                                   | BIM Workbench           | Beginner              |                        | [Yorik](User_Yorik.md)                                                                 |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [CAM Walkthrough for the Impatient](CAM_Walkthrough_for_the_Impatient.md)                                       | CAM Workbench           |                       |                        | Chrisb                                                                                         |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Code snippets](Code_snippets.md)                                                                               | Python                  | Beginner              |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Configuration Tables](Configuration_Tables.md)                                                                 | Product design          | Beginner              | 0:30                   | Gbroques                                                                                       | 0.20 or above       | [ConfigurationTableExample.FCStd](https://forum.freecad.org/download/file.php?id=270593)                                                                                                                                                                                                                                      |
++++++++
| [Creating a simple part with Draft and Part WB](Creating_a_simple_part_with_Draft_and_Part_WB.md)               | Modeling                | Beginner              | 1:30                   | Heda                                                                                           | \-                  | \-                                                                                                                                                                                                                                                                                                                            |
++++++++
| [Creating a simple part with Part WB](Creating_a_simple_part_with_Part_WB.md)                                   | Modeling                | Beginner              | 2:00                   | Heda                                                                                           | \-                  | \-                                                                                                                                                                                                                                                                                                                            |
++++++++
| [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)                             | Modeling                | Beginner              | 1:00                   | GlouGlou                                                                                       | 0.17 or above       | [Creating a simple PartDesign Body.FCStd](https://github.com/FreeCAD/Examples/blob/master/Creating_a_simple_PartDesign_Body.FCStd)                                                                                                                                                                                            |
++++++++
| [Customize Toolbars](Customize_Toolbars.md)                                                                     | Customization           | Beginner              | 0:05                   | [Mario52](User_Mario52.md)                                                             | Any                 | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md)                                                     | Product Design          | Beginner              | 0:30                   | r-frank and vocx                                                                               | 0.17 or above       | [Draft_Shapestring_Text](https://github.com/FreeCAD/Examples/blob/master/Draft_Shapestring_Tutorial_Examples/Draft_Shapestring_Tutorial_Text.FCStd?raw=true)                                                                                                                                                                  |
++++++++
| [Draft tutorial](Draft_tutorial.md)                                                                             | Draft Workbench         | Beginner              | 0:30                   | [Drei](User_Drei.md) and vocx                                                          | 0.19                | [Draft tutorial updated](https://forum.freecadweb.org/viewtopic.php?f=36&t=43651)                                                                                                                                                                                                                                             |
++++++++
| [Engine Block Tutorial](Engine_Block_Tutorial.md)                                                               | Part Workbench          | Beginner              | 1:00                   | Andrewbuck40                                                                                   | 0.14.3700           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Example Combined Footing](Example_Combined_Footing.md)                                                         | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Example Slab Having LShape Rebars Reinforcement Mesh](Example_Slab_Having_LShape_Rebars_Reinforcement_Mesh.md) | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Example Slab Having Mesh Of Straight Rebars](Example_Slab_Having_Mesh_Of_Straight_Rebars.md)                   | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Example Slab Having UShape Rebars Reinforcement Mesh](Example_Slab_Having_UShape_Rebars_Reinforcement_Mesh.md) | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Example Slab Spanning in One Direction](Example_Slab_Spanning_in_One_Direction.md)                             | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Example Slab Spanning in Two Directions](Example_Slab_Spanning_in_Two_Directions.md)                           | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Export to STL or OBJ](Export_to_STL_or_OBJ.md)                                                                 | Export                  | Beginner              | 0:20                   | r-frank                                                                                        | 0.16.6703           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Extend FEM Module](Extend_FEM_Module.md)                                                                       | Finite Element Analysis |                       |                        | [M42kus](User_M42kus.md)                                                               |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D.md)                                                     | Finite Element Analysis | Beginner              | 0:10                   | [Bernd](User_Bernd.md)                                                                 | 0.16.6377 or above  |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FEM Example Capacitance Two Balls](FEM_Example_Capacitance_Two_Balls.md)                                       | Finite Element Analysis | Beginner              |                        | [Sudhanshu Dubey](User_Sudhanshu_Dubey.md)                                             | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [FEM Geometry Preparation and Meshing](FEM_Geometry_Preparation_and_Meshing.md)                                 | Finite Element Analysis | Beginner              |                        | [NewJoker](User_NewJoker.md)                                                           | 0.21                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [FEM Shear of a Composite Block](FEM_Shear_of_a_Composite_Block.md)                                             | Finite Element Analysis | Beginner/Intermediate | 0:30                   | [HarryvL](User_HarryvL.md)                                                             | 0.17.12960 or above |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FEM tutorial](FEM_tutorial.md)                                                                                 | Finite Element Analysis | Beginner              | 0:10                   | [Drei](User_Drei.md)                                                                   | 0.17 or above       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FEM Tutorial Python](FEM_Tutorial_Python.md)                                                                   | Finite Element Analysis | Intermediate          | 0:30                   | [Bernd](User_Bernd.md)                                                                 | 0.18.15985 or above |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FreeCAD-Ship s60 tutorial](FreeCAD-Ship_s60_tutorial.md)                                                       | Ship Workbench          | Beginner              |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FreeCAD-Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md)                                             | Ship Workbench          | Beginner              |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [How to install additional workbenches](How_to_install_additional_workbenches.md)                               | Programming             | Medium programmer     | 0:15                   | [r-frank](User:R-frank.md)                                                             | Any                 | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [How to install macros](How_to_install_macros.md)                                                               | Programming             | Medium programmer     | 0:15                   | [Mario52](User_Mario52.md)                                                             | Any                 | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Import from STL or OBJ](Import_from_STL_or_OBJ.md)                                                             | Import                  | Beginner              | 0:30                   | r-frank                                                                                        | 0.16.6703           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Import OpenSCAD code](Import_OpenSCAD_code.md)                                                                 | Import                  | Beginner              | 0:30                   | r-frank                                                                                        | 0.16.6704           | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Import text and geometry from Inkscape](Import_text_and_geometry_from_Inkscape.md)                             | Import                  | Beginner              | 0:30                   | r-frank                                                                                        | 0.16.6704           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Import/Export IFC - compiling IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell.md)                     | BIM Workbench           | Advanced              | 2:00                   | Pablo Gil                                                                                      |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Measurement Of Angles On Holes](Measurement_Of_Angles_On_Holes.md)                                             | TechDraw Workbench      | Beginner              | 0:01                   | AnHi                                                                                           | 0.19                |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [PartDesign Bearingholder Tutorial I](PartDesign_Bearingholder_Tutorial_I.md)                                   | Product design          | Beginner              | 1:00                   | NormandC                                                                                       |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II.md)                                 | Product design          | Beginner              | 1:00                   | NormandC                                                                                       |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [PartDesign tutorial](PartDesign_tutorial.md)                                                                   | Sketcher Workbench      | Beginner              | 0:15                   | [Drei](User_Drei.md)                                                                   | 0.16 or above       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Plot Basic tutorial](Plot_Basic_tutorial.md)                                                                   | Plot Workbench          | Beginner              |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Plot MultiAxes tutorial](Plot_MultiAxes_tutorial.md)                                                           | Plot workbench          | Intermediate          |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Post-Processing of FEM Results with Paraview](Post-Processing_of_FEM_Results_with_Paraview.md)                 | Finite Element Analysis | Intermediate          | 2:00                   | [HarryvL](User_HarryvL.md)                                                             | 0.19                | [Beam](https://forum.freecadweb.org/download/file.php?id=103403) and [wall](https://forum.freecadweb.org/download/file.php?id=103557)                                                                                                                                                                                         |
++++++++
| [Private Preference Packs](Private_Preference_Packs.md)                                                         | Customization           | Intermediate/Advanced |                        | [drmacro](User_Drmacro.md)                                                             | 1.0 or above        |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Python scripting tutorial](Python_scripting_tutorial.md)                                                       | Programming             | Intermediate          |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Raytracing tutorial](Raytracing_tutorial.md)                                                                   | Raytracing Workbench    | Beginner              | 0:10                   | [Drei](User_Drei.md)                                                                   | 0.16 or above       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Robot 6-Axis](Robot_6-Axis.md)                                                                                 | Robot Workbench         | Intermediate          |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Robot tutorial](Robot_tutorial.md)                                                                             | Robot Workbench         | Beginner              |                        | r-frank                                                                                        |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Scripted Parts: Ball Bearing - Part 1](Scripted_Parts:_Ball_Bearing_-_Part_1.md)                               | Python                  | Beginner              | 0:30                   | r-frank                                                                                        | 0.16.6706           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Scripted Parts: Ball Bearing - Part 2](Scripted_Parts:_Ball_Bearing_-_Part_2.md)                               | Python                  | Beginner              | 0:30                   | r-frank                                                                                        | 0.16.6706           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Scripts](Scripts.md)                                                                                           | Python                  | Beginner              |                        | onekk Carlo                                                                                    | 0.19                |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Sketcher Lecture](Sketcher_Lecture.md)                                                                         | Sketcher Workbench      |                       |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Sketcher Micro Tutorial - Constraint Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)             | Sketcher Workbench      | Beginner              | 0:30                   | [Mark Stephen (Quick61)](User_Quick61.md) and vocx                                     | 0.19                | [Sketcher Constraints practices](https://forum.freecadweb.org/viewtopic.php?f=36&p=371659#p371659)                                                                                                                                                                                                                            |
++++++++
| [Sketcher requirement for a sketch](Sketcher_requirement_for_a_sketch.md)                                       | Sketcher Workbench      | Beginner              |                        | [Maker](User_Maker.md)                                                                 |                     | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Sketcher Tutorial](Sketcher_Tutorial.md)                                                                       | Sketcher Workbench      | Beginner              |                        | Ulrich                                                                                         |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [TechDraw HowTo Page](TechDraw_HowTo_Page.md)                                                                   | TechDraw Workbench      |                       |                        |                                                                                                | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [TechDraw Pitch Circle Tutorial](TechDraw_Pitch_Circle_Tutorial.md)                                             | TechDraw Workbench      | Beginner              | 0:10                   | Andergrin                                                                                      | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [TechDraw TemplateGenerator](TechDraw_TemplateGenerator.md)                                                     | TechDraw Workbench      | Intermediate          |                        | [FBXL5](User_FBXL5.md)                                                                 | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [TechDraw TemplateHowTo](TechDraw_TemplateHowTo.md)                                                             | TechDraw Workbench      | Intermediate          | 1:00                   | wandererfan                                                                                    | 0.17                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Thread for Screw Tutorial](Thread_for_Screw_Tutorial.md)                                                       | Product design          | Advanced              | 1:00                   | [DeepSOIC](User_DeepSOIC.md), [Murdic](User_Murdic.md), vocx                   | 0.19                | [Updated: Thread for screw tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=44668)                                                                                                                                                                                                                                 |
++++++++
| [Toothbrush Head Stand](Toothbrush_Head_Stand.md)                                                               | Modeling                | Beginner              | 1:00                   | [EmmanuelG](User_EmmanuelG.md)                                                         | 0.16 or above       | [Thingiverse 2403310](https://www.thingiverse.com/thing:2403310)                                                                                                                                                                                                                                                              |
++++++++
| [Topological data scripting](Topological_data_scripting.md)                                                     | Programming             | Intermediate          |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Transient FEM analysis](Transient_FEM_analysis.md)                                                             | Finite Element Analysis |                       |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Tutorial custom placing of windows and doors](Tutorial_custom_placing_of_windows_and_doors.md)                 | BIM Workbench           | Intermediate          | 1:00                   | [Vocx](User_Vocx.md)                                                                   | 0.18 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial for open windows](Tutorial_for_open_windows.md)                                                       | BIM Workbench           | Beginner              | 1:00                   | [Vocx](User_Vocx.md)                                                                   | 0.18 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial FreeCAD POV ray](Tutorial_FreeCAD_POV_ray.md)                                                         | Raytracing Workbench    | Intermediate          | 2:00                   | [Vocx](User_Vocx.md)                                                                   | 0.18 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial KinematicAssembly](Tutorial_KinematicAssembly.md)                                                     | Assembly3 Workbench     | Beginner              | 0:30                   | [FBXL5](User_FBXL5.md)                                                                 | 0.20 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial KinematicController](Tutorial_KinematicController.md)                                                 | Programming             | Intermediate          | 1:00                   | [FBXL5](User_FBXL5.md)                                                                 | 0.20 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial KinematicSkeleton](Tutorial_KinematicSkeleton.md)                                                     | Assembly3 Workbench     | Intermediate          | 0:40                   | [FBXL5](User_FBXL5.md)                                                                 | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial Render with Blender](Tutorial_Render_with_Blender.md)                                                 | Rendering               | Intermediate          | 1:00                   | [Vocx](User_Vocx.md)                                                                   | 0.18 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [VRML Preparation for Robot Simulation](VRML_Preparation_for_Robot_Simulation.md)                               | Robot Workbench         | Intermediate          |                        |                                                                                                | 0.11.4252ppa1       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Whiffle Ball tutorial](Whiffle_Ball_tutorial.md)                                                               | Product design          | Beginner              | 0:30                   | r-frank and vocx                                                                               | 0.17 or above       | [WhiffleBall_Tutorial_FCWiki.FCStd](https://github.com/FreeCAD/Examples/blob/master/Whiffle_Ball_Tutorial_ExampleFiles/WhiffleBall_Tutorial_FCWiki.FCStd?raw=true)                                                                                                                                                            |
++++++++
| [Wikihouse porting tutorial](Wikihouse_porting_tutorial.md)                                                     | Import                  | Intermediate/Advanced | 1:00                   |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++



---
⏵ [documentation index](../README.md) > [Tutorials]], uma lista completa e classificável pode ser encontrada em ](Category_Tutorials]],%20uma%20lista%20completa%20e%20classificável%20pode%20ser%20encontrada%20em%20.md) > [Tutorials](Category_Tutorials.md) > Tutorials/pt-br
