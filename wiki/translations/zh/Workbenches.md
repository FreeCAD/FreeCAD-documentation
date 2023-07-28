# Workbenches/zh
<div class="mw-translate-fuzzy">

FreeCad和许多现代设计应用程序一样，如[Revit或](wikipedia_Revit.md) [CATIA](wikipedia_CATIA.md)，都基于 [工作台的概念](wikipedia_Workbench.md)。工作台可以看作是为某个任务专门归类的一组工具。在一个传统的家具车间里，你会有一张工作台给木材工人，另一张给金属件工人，也许还有第三张给把所有零件组装在一起的工人。


</div>

在FreeCad中，同样的概念也适用。工具根据与之相关的任务分组归类到工作台中。

当您从一个工作台切换到另一个工作台时，界面上可用的工具会发生变化。工具栏、命令栏和界面的其他部分会切换到新的工作台，但是场景的内容不会改变。例如，您可以使用草图工作台开始绘制二维形状，然后使用零件工作台对它们进行进一步处理。


<div class="mw-translate-fuzzy">

请注意，有时工作台被称为"模块"。但是，工作台和模块是不同的实体。模块是FreeCad的任何扩展，而工作台是一个特殊的GUI配置，它对一些工具栏和菜单进行分组。通常每个模块都包含自己的工作台，因此它们的名称被交叉使用。


</div>



## 内建工作台

### Current


<div class="mw-translate-fuzzy">

Freecad安装后具有以下工作台：


</div>

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. Still in the early stages of development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](Constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with geometric primitives and boolean operations.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> The [Path Workbench](Path_Workbench.md) is used to produce G-Code instructions.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements. Currently unmaintained.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Obsolete

The following workbenches are no longer included after version 0.20:

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> The [Drawing Workbench](Drawing_Workbench.md) was used for producing technical drawings. The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) was used for working with bitmap images. It functionality has been integrated in [Std Base](Std_Base.md). See [Std Import](Std_Import.md) and [Std ViewLoadImage](Std_ViewLoadImage.md).

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) was used for ray-tracing (rendering). The external [Render Workbench](https://github.com/FreeCAD/FreeCAD-render) should be used instead.



## 外部工作台

FreeCAD工作台易于通过[Python进行编程开发](Python.md)，因此FreeCAD主要开发领域之外的很多人自己开发额外的工作台。


<div class="mw-translate-fuzzy">

[外部工作台页面列出了该社区已知的所有内容](external_workbenches.md)。 大多数功能都可以使用菜单 **工具 → <img src="images/Std_AddonMgr.svg" width=24px> 插件管理器**下的[插件管理器从FreeCAD轻松安装](Std_AddonMgr.md)。


</div>


<div class="mw-translate-fuzzy">


{{docnav
|[属性编辑器](Property_editor.md)
|[建筑模块](Arch_Workbench.md)
|IconL=
|IconR=Workbench_Arch.svg
}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/zh
