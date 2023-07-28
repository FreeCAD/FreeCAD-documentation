# Tutorials/zh-cn
{{TOCright}}


<div class="mw-translate-fuzzy">

本页展示了一系列精选的高质量图文教程。完整无序的教程集可以在[:Category:Tutorials找到](:Category_Tutorials.md)。


</div>


<div class="mw-translate-fuzzy">

如果您希望为FreeCAD维基文档与教程的编写做出贡献，请参考维基的通用指南[WikiPages](WikiPages.md)，并阅读[tutorial guidelines](tutorial_guidelines.md)。


</div>

请注意每个教程中所用的FreeCAD版本，因为有些教程采用的是老版FreeCAD。尽管常规的建模方式在新版FreeCAD中依然可行，但是某些工具却可能已经发生了变化。

See also [video tutorials](Video_tutorials.md) and [books](Books.md).



## 建筑物与BIM


<div class="mw-translate-fuzzy">

<File:Arch> tutorial 00.jpg\|link=[Arch tutorial](Arch_tutorial.md)\|[建筑工作台教程](Arch_tutorial.md) (v0.14)
本文是一篇针对建筑工作台的基本介绍文章。文中通过DXF格式文件导入图纸，最后构建出对应的3D模型，整个流程大致展示了该工作台的一般工作流程。 <File:Exercise> arch 01.jpg\|link=[Manual:BIM_modeling](Manual_BIM_modeling.md)\|[BIM 建模](Manual_BIM_modeling.md)
本文讨论了如何建立一个小屋的模型、利用TechDraw工作台生成一份蓝图（blueprint），并导出为IFC格式文件。 <File:11_T01_window_all_symbol_top.png%7Clink=>[Tutorial_for_open_windows](Tutorial_for_open_windows.md)\|[打开窗口与门](Tutorial_for_open_windows.md) (v0.18)
本文展示了如何利用elevation与plan符号显示打开的窗口与门，并利用TechDraw工作台生成一个基本的平面图。 <File:17_T02_sketch_2_attached_correctly.png%7Clink=>[Tutorial custom placing of windows and doors](Tutorial_custom_placing_of_windows_and_doors.md)\|[设计自定义窗口](Tutorial_custom_placing_of_windows_and_doors.md) (v0.18)
本文展示了如何利用草图工作台来绘制自定义门窗，并将其调整至墙体中合适的位置。 <File:Arch_panel_tutorial_01.jpg%7Clink=>[Arch panel tutorial](Arch_panel_tutorial.md)\|[建筑面板教程](Arch_panel_tutorial.md) (v0.15)
文中利用草图工作台创建一个微型建筑的屋面板（roof panel）。这里会运用窗口工具与面板工具。 <File:Arch_Wikihouse_01.jpg%7Clink=>[Wikihouse porting tutorial](Wikihouse_porting_tutorial.md)\|[维基房屋（WikiHouse）建模](Wikihouse_porting_tutorial.md)
先导入由SketchUp创建的WikiHouse网格模型，再利用草图工作台与面板工具对其重新建模。


</div>




<div class="mw-translate-fuzzy">

## 零件造型


</div>


<div class="mw-translate-fuzzy">

FreeCAD提供了两种主要工作流程来实现零件造型（modeling part）：

-   利用[零件工作台（Part workbench）中的](Part_Workbench.md)[构造实体几何（constructive solid geometry，简作CSG）](https://en.wikipedia.org/wiki/Constructive_solid_geometry)方法来组合对象（combining objects），以及
-   利用[零件设计工作台进行参数化建模](PartDesign_Workbench.md)，并编辑[feature](Glossary#Feature.md)。


</div>


<div class="mw-translate-fuzzy">

请注意，[零件设计工作台的工作流程自FreeCAD](PartDesign_Workbench.md) 0.17版起有了较大变化，而部分教程还未对此更新，可能仍然采用的是0.16版本。


</div>


<div class="mw-translate-fuzzy">

<File:GGTuto1> Vue.PNG\|link=[Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)\|[利用PartDesign工作台创建一个简单的零件](Creating_a_simple_part_with_PartDesign.md) (v0.17)
本文为PartDesign工作台工作流程的简介，在这里我们要：绘制草图、使用填充（pad）与挖槽（pocket）工具、并移动对象。 PD WB Tutorial018.png\|link=[Basic Part Design Tutorial 017](Basic_Part_Design_Tutorial_017.md)\|[零件设计基础教程](Basic_Part_Design_Tutorial_017.md) (v0.17)
本文利用功能编辑方式来建立一个简单的零件，主要流程为：创建草图，再利用填充、外部引用、挖槽与镜像等工具来生成零件实体。 TBHS-model.png\|link=[Toothbrush Head Stand](Toothbrush_Head_Stand.md)\|[建立电动牙刷头架模型](Toothbrush_Head_Stand.md) (v0.16)
文中使用了多种功能：草图工具、距离约束与重合约束（coincident constraint）工具、填充工具、外部引用工具、倒圆角工具（fillet）, 倒角工具（chamfer）、线性复制（linear pattern）工具与拔模（draft）。 Exercise lego 01.jpg\|link=[Manual:Modeling for product design](Manual_Modeling_for_product_design.md)\|[针对产品设计进行建模](Manual_Modeling_for_product_design.md) (v0.16)
建立对乐高方块模型，要用到的工具有：草图、垂直距离与水平距离的约束、填充、挖槽、外部引用、线性复制与装配工作台。 Exercise table complete.jpg\|link=[Manual:Traditional modeling, the CSG way/zh-cn](Manual:Traditional_modeling,_the_CSG_way/zh-cn.md)\|[传统建模，CSG方式](Manual:Traditional_modeling,_the_CSG_way/zh-cn.md)
利用像立方体与圆柱体这样简单的实体，并辅以布尔运算（模拟"焊接"与"切割"）来创建一个桌子。 TutorialDraftShapeString_Complete.jpg\|link=[Draft ShapeString tutorial](Draft_ShapeString_tutorial.md)\|[底图ShapeString工具教程](Draft_ShapeString_tutorial.md) (v0.16)
在实体上创建雕刻文字：首先挤压底图shapestring对象使之成为实体，再利用布尔运算从另一实体中将其切割，也就是对此文本进行雕刻。 Tutorial WhiffleBall.jpg\|link=[Whiffle Ball tutorial](Whiffle_Ball_tutorial.md)\|[创建一个威浮球（wiffle ball）](Whiffle_Ball_tutorial.md) (v0.16)
对立方体与圆柱体等实体图元进行布尔运算（如并集与切割）来创建一个空心球。 Tutorial-normand06.jpg\|link=[Basic modeling tutorial](Basic_modeling_tutorial.md)\|[建模基本教程](Basic_modeling_tutorial.md)
创建利用两种方式一个角铁：第一种是对实体图元执行布尔运算(CSG);第二种是通过根据平面轮廓图纸进行挤压来实现。


</div>

<File:GGTuto1> Vue.PNG\|link=[Creating a simple part with Draft and Part WB](Creating_a_simple_part_with_Draft_and_Part_WB.md)\|[Creating a simple part with Draft and Part Workbench](Creating_a_simple_part_with_Draft_and_Part_WB.md)
An introduction to modeling solids with Draft Workbench by creating a 2d profile in draft.

<File:GGTuto1> Vue.PNG\|link=[Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)\|[Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md) (v0.17)
An introduction to the PartDesign workflow: tracing a sketch, using pad, pocket, and moving the object. Pd_tut_final_solid.png\|link=[Basic_Part_Design_Tutorial](Basic_Part_Design_Tutorial.md)\|[Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md) (v0.17)
Model a simple part using a feature editing methodology: creating a sketch, using pad, external references, pocket, and mirror. Pd_tut_final_solid.png\|link=[Basic_Part_Design_Tutorial_019](Basic_Part_Design_Tutorial_019.md)\|[Basic Part Design Tutorial 019](Basic_Part_Design_Tutorial_019.md) (v0.19 or above)
An updated version of the previous tutorial that creates the same model using techniques that avoid the [topological naming problem](Topological_naming_problem.md). TBHS-model.png\|link=[Toothbrush_Head_Stand](Toothbrush_Head_Stand.md)\|[Model an electric toothbrush head stand](Toothbrush_Head_Stand.md) (v0.16 or above)
Multiple features used: sketch, distance and coincident constraints, pad, external references, fillet, chamfer, linear pattern, and draft. Exercise lego 01.jpg\|link=[Manual:Modeling_for_product_design](Manual_Modeling_for_product_design.md)\|[Modeling for product design](Manual_Modeling_for_product_design.md) (v0.16)
Modeling a Lego block: sketches, vertical and horizontal distance constraints, pad, pocket, external reference, linear pattern, and assembly. Exercise table complete.jpg\|link=[Manual:Traditional_modeling,\_the_CSG_way](Manual:Traditional_modeling,_the_CSG_way.md)\|[Traditional modeling, the CSG way](Manual:Traditional_modeling,_the_CSG_way.md)
Modeling a table by using simple solids like cubes and cylinders, and performing boolean operations (fusions and cuts) with them. 08_T04_Part_ShapesString_Extrude_final_cut.png\|link=[Draft_ShapeString_tutorial](Draft_ShapeString_tutorial.md)\|[Draft ShapeString tutorial](Draft_ShapeString_tutorial.md) (v0.19)
Create engraved text on a solid: extrude a shapestring to make it solid, then use a boolean cut to carve it from another solid. 10_T03_Part_ball_fillet.png\|link=[Whiffle_Ball_tutorial](Whiffle_Ball_tutorial.md)\|[Create a wiffle ball](Whiffle_Ball_tutorial.md) (v0.19)
Use solid primitives, like cubes and cylinders, and boolean operations, like union and cut, to create a hollowed ball. Tutorial-normand06.jpg\|link=[Basic modeling tutorial](Basic_modeling_tutorial.md)\|[Basic modeling tutorial](Basic_modeling_tutorial.md)
Create an iron angle by two methods: using solid primitives, and boolean operations (CSG); and by extruding a planar profile. <File:HTCaeroplane04.png%7Clink=>[Aeroplane](Aeroplane.md)\|[Aeroplane tutorial](Aeroplane.md)
Understand placements in FreeCAD by creating a simple aeroplane model. Then learn about rotation angles, yaw (Z), pitch (Y), and roll (X). <File:T13_14_Threads_components.png%7Clink=>[Thread_for_Screw_Tutorial](Thread_for_Screw_Tutorial.md)\|[Thread for screw tutorial](Thread_for_Screw_Tutorial.md) (v0.19)
Understand how to create threads with several techniques that include use of the tools [Part Helix](Part_Helix.md), [PartDesign AdditivePipe](PartDesign_AdditivePipe.md), [Part Sweep](Part_Sweep.md), [Part Fuse](Part_Fuse.md), and [Part Cut](Part_Cut.md).

The Raspberry Pi project has made simple tutorials that are easy to follow, particularly for those new to CAD systems:

-   [freecad-dice](https://projects.raspberrypi.org/en/projects/freecad-dice), model a die with six faces, and optionally 3D print it.
-   [freecad-headphone-tidy](https://projects.raspberrypi.org/en/projects/freecad-headphone-tidy), model a spool to organize and store earphones, and optionally 3D print it.
-   [freecad-chess-set](https://projects.raspberrypi.org/en/projects/freecad-chess-set), model and entire chess set in Bauhaus modernist style.
-   [raspberrypilearning](https://github.com/raspberrypilearning?utf8=%E2%9C%93&q=freecad&type=source&language=) repository (CC-BY 4.0) with other examples.



## 绘制底图与草图


<div class="mw-translate-fuzzy">

Exercise cabin 01.jpg\|link=[Manual:Traditional 2D drafting](Manual_Traditional_2D_drafting.md)\|[绘制传统的2D底图](Manual_Traditional_2D_drafting.md)
利用线段、连线、立方体、圆弧绘制建筑平面图，并为之添加填充图案、注释与标注。并将结果导出为DXF文件。 Draft_tutorial_result.png\|link=[Draft tutorial](Draft_tutorial.md)\|[底图教程](Draft_tutorial.md) (v0.16)
本文简单介绍了底图工作台中的常见工具：工作平面、网格、线段、弧线、升级（upgrade）、矩形、圆形、多边形、阵列、标注、注释与shapestring。 Sketcher tutorial result.png\|link=[Basic_Sketcher_Tutorial](Basic_Sketcher_Tutorial.md)\|[草图教程](Basic_Sketcher_Tutorial.md) (v0.16)
本文简单介绍了草图工作台中的常用工具：构建模式（construction mode）、线段、圆形、弧线、约束（等长约束、垂直约束、水平约束、相切约束、距离约束、角度约束、半径约束）。 Constrain3.png\|link=[Sketcher Micro Tutorial - Constraint Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)\|[草图工作台中宏的使用教程](Sketcher_Micro_Tutorial_-_Constraint_Practices.md) (v0.16)
学习高效地对草图进行约束。几何约束较之尺寸约束更受人们青睐。


</div>




<div class="mw-translate-fuzzy">

## 技术制图


</div>


<div class="mw-translate-fuzzy">

TDTut ProjGroup21.png\|link=[Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md)\|[TechDraw工作台基础教程](Basic_TechDraw_Tutorial.md) (v0.17)
本文内容为针对TechDraw工作台中常见工具的基本介绍，如：页（page）、视图（view）、缩放（scale）、垂直标注与水平标注（vertical and horizontal dimensions）、注释（ annotations）、正交投影组（projection groups）以及将标注与3D视图联系起来。 <File:FCTemplateHow.png%7Clink=>[TechDraw_TemplateHowTo](TechDraw_TemplateHowTo.md)\|[创建一个新的背景模板](TechDraw_TemplateHowTo.md) (v0.17)
介绍如何在TechDraw工作台中使用以Inkscape创建的页模板。涉及的步骤有：确定表单的规格大小、为页面绘制布局框架、定义固有的文本并编辑文本域。


</div>

## FEM

FEM example01 pic00.jpg\|link=[FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D.md)\|[CalculiX cantilever FEM analysis](FEM_CalculiX_Cantilever_3D.md) (v0.20)
This in an example included in every installation of FreeCAD; it demonstrates a basic analysis with the CalculiX FE solver. Purge the current result, re-run the solver, and view the displacements and stresses in the deformed mesh in the viewport.

FEM tutorial result.png\|link=[FEM tutorial](FEM_tutorial.md)\|[Simple FEM introduction](FEM_tutorial.md) (v0.20)
This is a short introduction to the steps required to perform an analysis in the FEM Workbench: model your object, create a mesh, add constraints and forces, add a material, run the solver, and visualize the results.

Figure 11 Deformed Mesh.png\|link=[FEM Shear of a Composite Block](FEM_Shear_of_a_Composite_Block.md)\|[FEM shear analysis of a composite block](FEM_Shear_of_a_Composite_Block.md) (v0.17)
Study the deformation of a block made of a hard nucleus surrounded by a softer material: create mesh regions, add materials, set up sliding constraints, add shear loads, run the solver, and visualize the results with a clip plane.

Femconcrete_Wall_3D_rx_PSS.png\|link=[Analysis_of_reinforced_concrete_with_FEM](Analysis_of_reinforced_concrete_with_FEM.md)\|[Analysis of reinforced concrete with FEM](Analysis_of_reinforced_concrete_with_FEM.md) (v0.19)
Estimate the level of reinforcement required in a concrete structure to prevent brittle failure under tension or shear.

Two_balls_result_2-cropped.png\|link=[FEM_Example_Capacitance_Two_Balls](FEM_Example_Capacitance_Two_Balls.md)\|[Electrostatic equation -- Capacitance of two balls](FEM_Example_Capacitance_Two_Balls.md) (v0.19)
This example shows how to simulate a capacitance. It illustrates how to setup the example, study it\'s various parts, solve it using the [Elmer Solver](FEM_SolverElmer.md) and visualize the results using [Clip Filter](FEM_PostFilterClipRegion.md).

FEM_post-processing_Paraview.png\|link=[Post-Processing_of_FEM_Results_with_Paraview](Post-Processing_of_FEM_Results_with_Paraview.md)\|[Post-Processing of FEM results with Paraview](Post-Processing_of_FEM_Results_with_Paraview.md) (v0.19)
This tutorial explains the basics of transferring data from the FEM Workbench to Paraview and shows some of the options and settings for displaying data.



## CNC & 3D打印 

Path-WalkThroughResult.gif\|link=[Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md)\|[Path Workbench for the impatient](Path_Walkthrough_for_the_Impatient.md)
This is a quick presentation of the workflow for the Path Workbench: create a job, define the output, define the milling tool, define the path operations, start the simulation, and generate a G-code output file. Exercise meshing 03.jpg\|link=[Manual:Preparing models for 3D printing](Manual_Preparing_models_for_3D_printing.md)\|[Preparing models for 3D printing](Manual_Preparing_models_for_3D_printing.md) (v0.16)
Convert a solid object to a mesh object using the Mesh Workbench, export the mesh to STL format, and use Slic3r to prepare the G-code. Alternatively use the Cura Workbench or the Path Workbench to generate the G-code.



## 渲染

Exercise raytracing 05.jpg\|link=[Manual:Creating renderings](Manual_Creating_renderings.md)\|[创建渲染文件](Manual_Creating_renderings.md)
如果系统中安装了POV-Ray与LuxRender，就利用它们为您的设计快速地渲染出一幅图像。 Raytracing tutorial result.png\|link=[Raytracing tutorial](Raytracing_tutorial.md)\|[Raytracing tutorial](Raytracing_tutorial.md) (v0.16)
本文描述了在光线追踪工作台中使用POV-Ray或LuxRender的基本工作流程：设置渲染器的工作路径、创建工程、设置摄像机的位置、选择模型、运行渲染器。12_T04_FreeCAD_POVray_render_floor_wood_walls_radiosity_final.png\|link=[Tutorial FreeCAD POV ray](Tutorial_FreeCAD_POV_ray.md)\|[FreeCAD与POV-ray中级教程](Tutorial_FreeCAD_POV_ray.md) (v0.18)
利用POV-Ray生成更佳渲染效果的工作流程：创建工程、添加对象、设置摄像机、保存.pov文件，手动编辑此文件来改良其纹理、表面、光照，最后运行渲染器。 07_T03_FreeCAD_Blender_EEVEE_render.png\|link=[Tutorial_Render_with_Blender](Tutorial_Render_with_Blender.md)\|[利用Blender渲染一个FreeCAD部件](Tutorial_Render_with_Blender.md) (v0.18)
从FreeCAD中将部件导出为Wavefront的.obj格式，再将其导入Blender中，建立一个简单的太阳光源，利用Principled BSDF着色器为之赋予基本材质，最后通过EEVEE与Cycles来生成渲染图片。

## Robot workbench 


<div class="mw-translate-fuzzy">

## 机器人工作台


</div>


<div class="mw-translate-fuzzy">

Robot Tutorial RobotSimulation.gif\|link=[Robot tutorial](Robot_tutorial.md)\|[机器人工作台教程](Robot_tutorial.md) (v0.17)
模拟工业机器人的运动：建立一个机器人的运动轨迹（trajectory）、建立初始位置（home position）、改变机器人的位置、插入各种路点（waypoints），并模拟机器人的运动。


</div>

## Scripting

These are tutorials that are related to scripting or programming. They are geared towards more experienced users, who are already somewhat familiar with the program.

-   [Python scripting tutorial](Python_scripting_tutorial.md)
-   [How to install macros](How_to_install_macros.md)
-   [How to install additional workbenches](How_to_install_additional_workbenches.md)

## Tutorials - Comprehensive list 

Here are listed all the tutorials that are not in the manual **regardless of their quality**. If a tutorial is listed in the [:Category:Tutorials](:Category_Tutorials.md) and not in this table please insert it.

++++++++
| Tutorial                                                                                                                   | Topic                   | Level                 | Time to complete hh:mm | Authors                                                                                        | FreeCAD version     | Example files                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                            |                         |                       |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                            |                         |                       |                        |                                                                                                |                     | \<!\-- Template for new entries                                                                                                                                                                                                                                                                                               |
+============================================================================================================================+=========================+=======================+========================+================================================================================================+=====================+===============================================================================================================================================================================================================================================================================================================================+
| [Tutorial](Tutorial.md)                                                                                            | Topic                   | Level                 | 0:00                   | [Name](User_Name.md)                                                                   | 1.0                 | None \--\>                                                                                                                                                                                                                                                                                                                    |
++++++++
| [Add Button to FEM Toolbar Tutorial](Add_Button_to_FEM_Toolbar_Tutorial.md)                                        | Finite Element Analysis |                       |                        | [JohnWang](User_JohnWang.md)                                                           |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Add FEM Constraint Tutorial](Add_FEM_Constraint_Tutorial.md)                                                      | Finite Element Analysis |                       |                        | [M42kus](User_M42kus.md)                                                               |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Add FEM Equation Tutorial](Add_FEM_Equation_Tutorial.md)                                                          | Finite Element Analysis |                       |                        | [JohnWang](User_JohnWang.md)                                                           |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Adding a new mouse navigation option to FreeCAD (unfinished)](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) | Programming             | Advanced              |                        | [Kunda1](User_Kunda1.md)                                                               | 0.19.x              | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Advanced Attachment OYX](Advanced_Attachment_OYX.md)                                                              | Attachment              | Intermediate/Advanced |                        | [drmacro](User_drmacro.md)                                                             | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Advanced TechDraw Tutorial (unfinished)](Advanced_TechDraw_Tutorial.md)                                           | TechDraw Workbench      | Advanced              |                        | [domad](User_domad.md)                                                                 | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Aeroplane](Aeroplane.md)                                                                                          | Part Workbench          | Beginner              | 0:10                   | Hughthecat                                                                                     |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Analysis of reinforced concrete with FEM](Analysis_of_reinforced_concrete_with_FEM.md)                            | Finite Element Analysis | Intermediate          | 1:00                   | [HarryvL](User_HarryvL.md)                                                             | 0.19 or above       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Arch panel tutorial](Arch_panel_tutorial.md)                                                                      | Arch Workbench          | Beginner              | 1:00                   | Yorik                                                                                          |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Arch tutorial](Arch_tutorial.md)                                                                                  | Modeling                | Intermediate          |                        | [Yorik](User_Yorik.md)                                                                 | 0.14                |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md)                                                          | Attachment              | Beginner/intermediate | 1:00                   | [Bance](User_Bance.md)                                                                 | 0.17 or above       | [Basic Attachment Tutorial.FCStd](https://github.com/BanceFC/Examples/blob/master/Basic_Attachment_Tutorial.FCStd)                                                                                                                                                                                                            |
++++++++
| [Basic modeling tutorial](Basic_modeling_tutorial.md)                                                              | Modelling               | Beginner              | 0:15                   | [NormandC](User_NormandC.md)                                                           | Any                 | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md)                                                        | Modeling                | Beginner              |                        | [Mark Stephen (Quick61)](User_Quick61.md) and [HarryGeier](User_HarryGeier.md) | 0.17 or above       | [Basic Part Design for v0.17](https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd)                                                                                                                                                              |
++++++++
| [Basic Part Design Tutorial 019](Basic_Part_Design_Tutorial_019.md)                                                | Modeling                | Beginner              | 1:00                   | [Carlo Dormeletti](User_Onekk.md) and [Ed Williams](User_Edwilliams16.md)      | 0.19 or above       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md)                                                              | Sketcher Workbench      | Beginner              | 1:00                   | [Drei](User_Drei.md) and [Vocx](User_Vocx.md)                                  | 0.19                | [Basic Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=43594)                                                                                                                                                                                                                                            |
++++++++
| [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md)                                                              | TechDraw Workbench      | Beginner              |                        | [WandererFan](User_WandererFan.md)                                                     | 0.17 or above       | [Basic Part Design for v0.17 Sample](https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd) [Basic TechDraw Tutorial Sample](https://github.com/FreeCAD/Examples/blob/master/Basic_TechDraw_Tutorial_Example_Files/Basic_TechDraw_Tutorial.fcstd) |
++++++++
| [BIM ingame tutorial](BIM_ingame_tutorial.md)                                                                      | Arch Workbench          | Beginner              |                        | [Yorik](User_Yorik.md)                                                                 |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Code snippets](Code_snippets.md)                                                                                  | Python                  | Beginner              |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Creating a simple part with Draft and Part WB](Creating_a_simple_part_with_Draft_and_Part_WB.md)                  | Modeling                | Beginner              | 1:30                   | Heda                                                                                           | \-                  | \-                                                                                                                                                                                                                                                                                                                            |
++++++++
| [Creating a simple part with Part WB](Creating_a_simple_part_with_Part_WB.md)                                      | Modeling                | Beginner              | 2:00                   | Heda                                                                                           | \-                  | \-                                                                                                                                                                                                                                                                                                                            |
++++++++
| [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)                                | Modeling                | Beginner              | 1:00                   | GlouGlou                                                                                       | 0.17 or above       | [Creating a simple PartDesign Body.FCStd](https://github.com/FreeCAD/Examples/blob/master/Creating_a_simple_PartDesign_Body.FCStd)                                                                                                                                                                                            |
++++++++
| [Customize Toolbars](Customize_Toolbars.md)                                                                        | Customization           | Beginner              | 0:05                   | [Mario52](User_Mario52.md)                                                             | Any                 | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md)                                                        | Product Design          | Beginner              | 0:30                   | r-frank and vocx                                                                               | 0.17 or above       | [Draft_Shapestring_Text](https://github.com/FreeCAD/Examples/blob/master/Draft_Shapestring_Tutorial_Examples/Draft_Shapestring_Tutorial_Text.FCStd?raw=true)                                                                                                                                                                  |
++++++++
| [Draft tutorial](Draft_tutorial.md)                                                                                | Draft Workbench         | Beginner              | 0:30                   | [Drei](User_Drei.md) and vocx                                                          | 0.19                | [Draft tutorial updated](https://forum.freecadweb.org/viewtopic.php?f=36&t=43651)                                                                                                                                                                                                                                             |
++++++++
| [Dxf Importer Install](Dxf_Importer_Install.md)                                                                    | Import                  | Intermediate          | 0:05                   | [Mario52](User_Mario52.md)                                                             | Any                 | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Engine Block Tutorial](Engine_Block_Tutorial.md)                                                                  | Part Workbench          | Beginner              | 1:00                   | Andrewbuck40                                                                                   | 0.14.3700           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Example Combined Footing](Example_Combined_Footing.md)                                                            | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Example Slab Having LShape Rebars Reinforcement Mesh](Example_Slab_Having_LShape_Rebars_Reinforcement_Mesh.md)    | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Example Slab Having Mesh Of Straight Rebars](Example_Slab_Having_Mesh_Of_Straight_Rebars.md)                      | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Example Slab Having UShape Rebars Reinforcement Mesh](Example_Slab_Having_UShape_Rebars_Reinforcement_Mesh.md)    | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Example Slab Spanning in One Direction](Example_Slab_Spanning_in_One_Direction.md)                                | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Example Slab Spanning in Two Directions](Example_Slab_Spanning_in_Two_Directions.md)                              | Reinforcement Workbench | Intermediate          |                        | [Shiv Charan](User_Shiv_Charan.md)                                                     | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Export to STL or OBJ](Export_to_STL_or_OBJ.md)                                                                    | Export                  | Beginner              | 0:20                   | r-frank                                                                                        | 0.16.6703           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Extend FEM Module](Extend_FEM_Module.md)                                                                          | Finite Element Analysis |                       |                        | [M42kus](User_M42kus.md)                                                               |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D.md)                                                        | Finite Element Analysis | Beginner              | 0:10                   | [Bernd](User_Bernd.md)                                                                 | 0.16.6377 or above  |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FEM Example Capacitance Two Balls](FEM_Example_Capacitance_Two_Balls.md)                                          | Finite Element Analysis | Beginner              |                        | [Sudhanshu Dubey](User_Sudhanshu_Dubey.md)                                             | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [FEM Shear of a Composite Block](FEM_Shear_of_a_Composite_Block.md)                                                | Finite Element Analysis | Beginner/Intermediate | 0:30                   | [HarryvL](User_HarryvL.md)                                                             | 0.17.12960 or above |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FEM tutorial](FEM_tutorial.md)                                                                                    | Finite Element Analysis | Beginner              | 0:10                   | [Drei](User_Drei.md)                                                                   | 0.17 or above       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FEM Tutorial Python](FEM_Tutorial_Python.md)                                                                      | Finite Element Analysis | Intermediate          | 0:30                   | [Bernd](User_Bernd.md)                                                                 | 0.18.15985 or above |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FreeCAD-Ship s60 tutorial](FreeCAD-Ship_s60_tutorial.md)                                                          | Ship Workbench          | Beginner              |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [FreeCAD-Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md)                                                | Ship Workbench          | Beginner              |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [How to install additional workbenches](How_to_install_additional_workbenches.md)                                  | Programming             | Medium programmer     | 0:15                   | [r-frank](User:R-frank.md)                                                             | Any                 | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [How to install macros](How_to_install_macros.md)                                                                  | Programming             | Medium programmer     | 0:15                   | [Mario52](User_Mario52.md)                                                             | Any                 | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Import from STL or OBJ](Import_from_STL_or_OBJ.md)                                                                | Import                  | Beginner              | 0:30                   | r-frank                                                                                        | 0.16.6703           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Import OpenSCAD code](Import_OpenSCAD_code.md)                                                                    | Import                  | Beginner              | 0:30                   | r-frank                                                                                        | 0.16.6704           | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Import text and geometry from Inkscape](Import_text_and_geometry_from_Inkscape.md)                                | Import                  | Beginner              | 0:30                   | r-frank                                                                                        | 0.16.6704           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Import/Export IFC - compiling IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell.md)                        | Arch Workbench          | Advanced              | 2:00                   | Pablo Gil                                                                                      |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Measurement Of Angles On Holes](Measurement_Of_Angles_On_Holes.md)                                                | TechDraw Workbench      | Beginner              | 0:01                   | AnHi                                                                                           | 0.19                |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [PartDesign Bearingholder Tutorial I](PartDesign_Bearingholder_Tutorial_I.md)                                      | Product design          | Beginner              | 1:00                   | NormandC                                                                                       |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II.md)                                    | Product design          | Beginner              | 1:00                   | NormandC                                                                                       |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [PartDesign tutorial](PartDesign_tutorial.md)                                                                      | Sketcher Workbench      | Beginner              | 0:15                   | [Drei](User_Drei.md)                                                                   | 0.16 or above       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md)                                        | Path Workbench          |                       |                        | Chrisb                                                                                         |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Plot Basic tutorial](Plot_Basic_tutorial.md)                                                                      | Plot Workbench          | Beginner              |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Plot MultiAxes tutorial](Plot_MultiAxes_tutorial.md)                                                              | Plot workbench          | Intermediate          |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Post-Processing of FEM Results with Paraview](Post-Processing_of_FEM_Results_with_Paraview.md)                    | Finite Element Analysis | Intermediate          | 2:00                   | [HarryvL](User_HarryvL.md)                                                             | 0.19                | [Beam](https://forum.freecadweb.org/download/file.php?id=103403) and [wall](https://forum.freecadweb.org/download/file.php?id=103557)                                                                                                                                                                                         |
++++++++
| [Private Preference Packs](Private_Preference_Packs.md)                                                            | Customization           | Intermediate/Advanced |                        | [drmacro](User_Drmacro.md)                                                             | 1.0 or above        |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Python scripting tutorial](Python_scripting_tutorial.md)                                                          | Programming             | Intermediate          |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Raytracing tutorial](Raytracing_tutorial.md)                                                                      | Raytracing Workbench    | Beginner              | 0:10                   | [Drei](User_Drei.md)                                                                   | 0.16 or above       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Robot 6-Axis](Robot_6-Axis.md)                                                                                    | Robot Workbench         | Intermediate          |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Robot tutorial](Robot_tutorial.md)                                                                                | Robot Workbench         | Beginner              |                        | r-frank                                                                                        |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Scripted Parts: Ball Bearing - Part 1](Scripted_Parts:_Ball_Bearing_-_Part_1.md)                                  | Python                  | Beginner              | 0:30                   | r-frank                                                                                        | 0.16.6706           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Scripted Parts: Ball Bearing - Part 2](Scripted_Parts:_Ball_Bearing_-_Part_2.md)                                  | Python                  | Beginner              | 0:30                   | r-frank                                                                                        | 0.16.6706           |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Scripts](Scripts.md)                                                                                              | Python                  | Beginner              |                        | onekk Carlo                                                                                    | 0.19                |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Sketcher Micro Tutorial - Constraint Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)                | Sketcher Workbench      | Beginner              | 0:30                   | [Mark Stephen (Quick61)](User_Quick61.md) and vocx                                     | 0.19                | [Sketcher Constraints practices](https://forum.freecadweb.org/viewtopic.php?f=36&p=371659#p371659)                                                                                                                                                                                                                            |
++++++++
| [Sketcher reference](Sketcher_reference.md)                                                                        | Sketcher Workbench      |                       |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Sketcher requirement for a sketch](Sketcher_requirement_for_a_sketch.md)                                          | Sketcher Workbench      | Beginner              |                        | [Maker](User_Maker.md)                                                                 |                     | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Sketcher Tutorial](Sketcher_Tutorial.md)                                                                          | Sketcher Workbench      | Beginner              |                        | Ulrich                                                                                         |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [TechDraw HowTo Page](TechDraw_HowTo_Page.md)                                                                      | TechDraw Workbench      |                       |                        |                                                                                                | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [TechDraw Pitch Circle Tutorial](TechDraw_Pitch_Circle_Tutorial.md)                                                | TechDraw Workbench      | Beginner              | 0:10                   | Andergrin                                                                                      | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [TechDraw TemplateGenerator](TechDraw_TemplateGenerator.md)                                                        | TechDraw Workbench      | Intermediate          |                        | [FBXL5](User_FBXL5.md)                                                                 | 0.19                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [TechDraw TemplateHowTo](TechDraw_TemplateHowTo.md)                                                                | TechDraw Workbench      | Intermediate          | 1:00                   | wandererfan                                                                                    | 0.17                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Thread for Screw Tutorial](Thread_for_Screw_Tutorial.md)                                                          | Product design          | Advanced              | 1:00                   | [DeepSOIC](User_DeepSOIC.md), [Murdic](User_Murdic.md), vocx                   | 0.19                | [Updated: Thread for screw tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=44668)                                                                                                                                                                                                                                 |
++++++++
| [Toothbrush Head Stand](Toothbrush_Head_Stand.md)                                                                  | Modeling                | Beginner              | 1:00                   | [EmmanuelG](User_EmmanuelG.md)                                                         | 0.16 or above       | [Thingiverse 2403310](https://www.thingiverse.com/thing:2403310)                                                                                                                                                                                                                                                              |
++++++++
| [Topological data scripting](Topological_data_scripting.md)                                                        | Programming             | Intermediate          |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Transient FEM analysis](Transient_FEM_analysis.md)                                                                | Finite Element Analysis |                       |                        |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Tutorial custom placing of windows and doors](Tutorial_custom_placing_of_windows_and_doors.md)                    | Arch Workbench          | Intermediate          | 1:00                   | [Vocx](User_Vocx.md)                                                                   | 0.18 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial for open windows](Tutorial_for_open_windows.md)                                                          | Arch Workbench          | Beginner              | 1:00                   | [Vocx](User_Vocx.md)                                                                   | 0.18 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial FreeCAD POV ray](Tutorial_FreeCAD_POV_ray.md)                                                            | Raytracing Workbench    | Intermediate          | 2:00                   | [Vocx](User_Vocx.md)                                                                   | 0.18 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial KinematicAssembly](Tutorial_KinematicAssembly.md)                                                        | Assembly3 Workbench     | Beginner              | 0:30                   | [FBXL5](User_FBXL5.md)                                                                 | 0.20 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial KinematicController](Tutorial_KinematicController.md)                                                    | Programming             | Intermediate          | 1:00                   | [FBXL5](User_FBXL5.md)                                                                 | 0.20 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial KinematicSkeleton](Tutorial_KinematicSkeleton.md)                                                        | Assembly3 Workbench     | Intermediate          | 0:40                   | [FBXL5](User_FBXL5.md)                                                                 | 0.20                | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [Tutorial Render with Blender](Tutorial_Render_with_Blender.md)                                                    | Rendering               | Intermediate          | 1:00                   | [Vocx](User_Vocx.md)                                                                   | 0.18 or above       | None                                                                                                                                                                                                                                                                                                                          |
++++++++
| [VRML Preparation for Robot Simulation](VRML_Preparation_for_Robot_Simulation.md)                                  | Robot Workbench         | Intermediate          |                        |                                                                                                | 0.11.4252ppa1       |                                                                                                                                                                                                                                                                                                                               |
++++++++
| [Whiffle Ball tutorial](Whiffle_Ball_tutorial.md)                                                                  | Product design          | Beginner              | 0:30                   | r-frank and vocx                                                                               | 0.17 or above       | [WhiffleBall_Tutorial_FCWiki.FCStd](https://github.com/FreeCAD/Examples/blob/master/Whiffle_Ball_Tutorial_ExampleFiles/WhiffleBall_Tutorial_FCWiki.FCStd?raw=true)                                                                                                                                                            |
++++++++
| [Wikihouse porting tutorial](Wikihouse_porting_tutorial.md)                                                        | Import                  | Intermediate/Advanced | 1:00                   |                                                                                                |                     |                                                                                                                                                                                                                                                                                                                               |
++++++++



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Tutorials/zh-cn
