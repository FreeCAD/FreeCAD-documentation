# Workbenches/zh-cn
<div class="mw-translate-fuzzy">


{{docnav|[Property editor](Property_editor.md)|[Arch Module](Arch_Workbench.md)|IconL=|IconR=Workbench_Arch.svg}}


</div>

像许多现代设计应用程序，如[Revit或](wikipedia_Revit.md)[CATIA](wikipedia_CATIA.md)，FreeCAD基于[工作台的概念](wikipedia_Workbench.md)。工作台可以被认为是为特定任务分组的一组工具。在一个传统的家具车间里，你有一个工作桌子给木材工作的人，另一张桌子给金属件工作的人，也可能有第三张桌子给把所有这些部件组装在一起的人。

在FreeCAD中，相同的概念也适用。工具根据其相关任务分为工作台。

当您从一个工作台切换到另一个工作台时，界面上可用的工具发生变化。工具栏，命令栏和界面的其他部分可以切换到新的工作台，但是您的场景的内容不会改变。例如，您可以使用草图工作台开始绘制2D形状，然后使用零件工作台进一步处理它们。


<div class="mw-translate-fuzzy">

请注意，有时工作台被称为"模块"。但是，工作台和模块是不同的实体。模块是FreeCAD的任何扩展，而Workbench是一个特殊的GUI配置，可以组合一些工具栏和菜单。通常每个模块都包含自己的工作台，因此交叉使用名称。


</div>

## 内建的工作台


<div class="mw-translate-fuzzy">

每个FreeCAD安装都可以使用以下工作台：


</div>

-   <img alt="" src=images/Freecad.svg  style="width   *32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width   *32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width   *32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width   *32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Image.svg  style="width   *32px;"> The [Image Workbench](Image_Workbench.md) for working with bitmap images.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width   *32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. It is still under development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width   *32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width   *32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width   *32px;"> The [Part Workbench](Part_Workbench.md) for working with CAD parts.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width   *32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Path.svg  style="width   *32px;"> The [Path Workbench](Path_Workbench.md) is used to produce G-Code instructions. It is still under development.

-   <img alt="" src=images/Workbench_Points.svg  style="width   *32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width   *32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) for working with ray-tracing (rendering).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width   *32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features. It is still under development.

-   <img alt="" src=images/Workbench_Robot.svg  style="width   *32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width   *32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width   *32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width   *32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width   *32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width   *32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width   *32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width   *32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Deprecated

The following workbenches are still included in the base installation for compatibility purposes, but they should no longer be used.

-   <img alt="" src=images/Workbench_Complete.svg  style="width   *32px;"> The [Complete Workbench](Complete_Workbench.md) holds all commands and features from all workbenches that met certain quality criteria. {{Obsolete|0.17}}

-   <img alt="" src=images/Workbench_Drawing.svg  style="width   *32px;"> The [Drawing Workbench](Drawing_Workbench.md) was used for producing technical drawings but has now been deprecated. It is still needed to read old FreeCAD files that contain objects created with this workbench. The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement. {{Obsolete|0.17}}

## 外部工作台

FreeCAD工作台很容易在[Python](http   *//www.python.org)中编程，所以很多人在FreeCAD代码库之外开发了额外的工作台。


<div class="mw-translate-fuzzy">

[外部工作台页面有一些关于其中的一些信息和教程](External_workbenches/zh-cn.md)，[FreeCAD Addons](https   *//github.com/FreeCAD/FreeCAD-addons)项目旨在收集它们，并使其可以从FreeCAD中轻松安装。亦可用[Addon Manager进行安装](Std_AddonMgr.md)，它在菜单中的位置为**Tools → <img src="images/Std_AddonMgr.svg" width=24px> Addon manager**。


</div>

新的工作台正在开发中，敬请期待！


<div class="mw-translate-fuzzy">


{{docnav|Property editor/zh-cn|PartDesign Workbench/zh-cn}}


</div>




[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/zh-cn
