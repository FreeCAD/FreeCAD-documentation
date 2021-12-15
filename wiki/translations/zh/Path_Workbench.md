# <img alt="Path workbench icon" src=images/Workbench_Path.svg  style="width:64px;"> Path Workbench/zh


{{TOCright}}

## 简介


<div class="mw-translate-fuzzy">

刀路工作台用于从FreeCAD 3D模型生成[CNC机器](https://en.wikipedia.org/wiki/CNC_router)指令。它们可以在CNC机床上生产真实的3D产品，如铣床，车床，激光切割机等。 通常，指令是[G-Code](https://en.wikipedia.org/wiki/G-Code)语言。


</div>

<img alt="" src=images/pathwb.png  style="width:600px;">


<div class="mw-translate-fuzzy">

FreeCAD刀路工作台按如下工作流程创建这些机器指令：

-   使用[零件设计工作台](PartDesign_Workbench/zh.md)，[零件工作台 或](Part_Workbench/zh.md)[草图工作台中的一个或多个创建作为基础对象的](Draft_Workbench/zh.md)3D模型。
-   在[刀路工作台中创建](Path_Workbench.md)[刀路作业](Path_Job/zh.md)。 这包含用于生成在CNC铣床上处理作业的G-code所有必要的信息：有库存材料，工厂有一定的[刀具包](Path_ToolLibraryEdit/zh.md)，它遵循某些命令(通常是G-Code)控制速度和运动。
-   根据作业操作的要求选择刀具。
-   使用例如 [轮廓线和](Path_Profile/zh.md)[开槽操作创建铣削路径](Path_Pocket_3D/zh.md)。 这些刀路对象使用FreeCAD内部独立于CNC机器的G-Code语言。
-   使用与您的机器匹配的G-Code形式导出作业。


</div>

## General concepts 


<div class="mw-translate-fuzzy">

## 一般概念

刀路工作台生成G-code，用于定义铣削产品的刀具运行路径，产品外形通过[刀路作业操作 FreeCAD G-Code指令](https://www.freecadweb.org/wiki/Path_scripting#FreeCAD.27s_internal_GCode_format)模拟铣削后的3D数模所呈现，该G-code指令通过选择适合的前置处理程序被转换为适合目标CNC控制器的指令。 G-code由包含在刀路作业中的指令和操作生成。作业工作流将这些指令和操作按其执行顺序列出。该列表通过添加刀路操作、刀路修剪、刀路分步命令和通过刀路菜单或者图形界面按钮刀路修改完成。


</div>

The G-code is generated from directives and Operations contained in a Path Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding Path Operations, Path Dressups, Path Supplemental Commands, and Path Modifications from the Path Menu, or GUI buttons.


<div class="mw-translate-fuzzy">

刀路工作台提供刀具管理器（库，刀具表），G-code检查和铣削模拟工具。它连接前置处理程序并允许导入和导出工作模板。


</div>


<div class="mw-translate-fuzzy">

刀路工作台的外部依赖包括：

1.  在 **编辑 → 首选项 → General → 单位标签的单位设定**中设置的FreeCAD的3D数模尺寸单位。前置处理程序设置定义了最终的G-code尺寸单位。
2.  宏文件路径和几何公差在**编辑 → 首选项 → 刀路 → 作业偏好设定**标签中设置.
3.  颜色在**编辑 → 首选项 → 刀路 → 刀路颜色**标签中设置.
4.  持有标记参数在**编辑 → 首选项 → 刀路 → 修剪**标签中设置.
5.  基础3D数模品质支持刀路WB需求，通过几何体检查。


</div>

## Limitations

Some current limitations of which you should be aware are:

-   Most of the Path Tools are not true 3D tools but only 2.5D capable. This means that they take a fixed 2D shape and can cut it down to a given depth. However, there are two tools which produce true 3D paths: **<img src="images/Path_3DPocket.svg" width=24px> [3D Pocket](Path_Pocket_3D.md)** and **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** (which is still an [experimental feature](Path_experimental.md) as of November 2020).
-   Most of Path workbench is designed for a simple, standard 3-axis (xyz) CNC mill/router, but lathe tools are under development in 0.19\_pre.
-   Most operations in Path workbench will return paths based on a standard endmill tool/bit only, regardless of the tool/bit type assigned in a given tool controller with the exception of the **<img src="images/Path_Engrave.svg" width=24px> [Engrave](Path_Engrave.md)** and **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** operations.
-   The operations within the Path workbench are not aware of clamping mechanisms in use to secure the model to your machine. Consequently, please review and simulate the paths you generate prior to sending the code to your machine. If necessary, model your clamping mechanisms in FreeCAD in order to better inspect the paths generated. Look for possible collisions with clamps or other obstacles along the paths.

## 单位

刀路工作台中的单位处理可能会令人感到困惑。 有几点需要了解：

1.  FreeCAD基本单位的长度和时间分别为\'mm\'和\'s\'。 因此速度单位为\'mm/s\'。 这就是FreeCAD内部存储的东西，与其他无关。
2.  默认单位模式使用默认单位。如果您使用默认模式并输入没有单位给进率，则给进率的单位为\'mm/s\'
3.  大多数数控机床都需要的进给速率为"mm/min"或"in/min"。 大多数后置处理程序会在生成G-code时自动转换单位。

模式：

1.  更改首选项中的模式会更改输入字段的默认单位。 如果您是刀路工作台用户并且更喜欢以公制设计，则强烈建议您使用"公制小零件和CNC"模式。 如果您使用美国单位进行设计，可以使用英制十进制和美制
2.  更改首选单元模式对输出没有影响，但有助于避免输入错误

输出：

1.  在输出中生成正确的单位是后处理器的责任，且这一操作仅在那时完成
2.  机器输出单元与您选择的单元模式完全无关
3.  后处理程序产生公制（G21）或英制（G20）输出，还可进行配置。
4.  可配置的后处理程序默认为公制（G21）
5.  如果您希望可配置的后处理器输出英制G-code（G20），请在作业输出配置中设置正确的参数（即\--incs for linuxcnc）。 这可以存储在作业模板中，并设置为默认模板，以使其自动适用于所有未来的作业。

刀路检查

1.  如果你使用刀路检查工具查看G-code，你将在其中看到\'mm/s\'，应为它还没有被进行后置处理。

## Heights and depths 


<div class="mw-translate-fuzzy">

## 刀路命令


</div>

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*

## Commands

Some commands are experimental and not available by default. To enable them see [Path experimental](Path_experimental.md).

### Project Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Job.png  style="width:32px;"> [刀路作业](Path_Job/zh.md):创建一个新的CNC作业。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_PostProcess.png  style="width:32px;"> [后置处理](Path_Post/zh.md): 将一个项目导出为G-code。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Sanity.png  style="width:32px;"> [刀路错误](Path_Sanity.md): 检查选定作业中的缺失值


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-ExportTemplate.png  style="width:32px;"> [导出模板](Path_ExportTemplate/zh.md): 将当前作业导出为模板。


</div>

### Tool Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Inspect.png  style="width:32px;"> [G-Code检查器](Path_Inspect/zh.md): 显示需要检查的G-code。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Simulator.png  style="width:32px;"> [刀路模拟](Path_Simulator/zh.md): 展示铣削操作在机器上的运行。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-CompleteLoop.png  style="width:32px;"> [收尾循环](Path_SelectLoop/zh.md): 在选定的两个边上完成收尾循环。


</div>

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width:32px;"> [Toggle the Active State of the Operation](Path_OpActiveToggle.md): Activates or de-activates a path operation.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Toggles the ToolBit Dock. <small>(v0.19)</small> 

### Basic Operations 

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profile](Path_Profile.md): Creates a profile operation of the entire model, or from one or more selected faces or edges. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Pocket.png  style="width:32px;"> [开槽](Path_Pocket_Shape/zh.md):创建选定的一个或多个选定挖槽的开槽操作。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Drilling.png  style="width:32px;"> [钻孔](Path_Drilling.md): 执行钻孔循环


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Face.png  style="width:32px;"> [面铣削](Path_MillFace.md): 创建一个面铣削刀路


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Helix.png  style="width:32px;"> [螺旋](Path_Helix.md): 创建螺旋刀路。


</div>

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptive](Path_Adaptive.md): Creates an adaptive clearing and profiling operation.

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> _. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Engrave.png  style="width:32px;"> [雕刻](Path_Engrave.md):创建雕刻刀路


</div>


<div class="mw-translate-fuzzy">

### 刀路修剪


</div>

### 3D Operations 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-3DPocket.png  style="width:32px;"> [3D开槽](Path_Pocket_3D.md):创建3D开槽刀路


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-3DSurface.png  style="width:32px;"> [3D面](Path_Surface.md): 创建3D面刀路


</div>

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> _. <small>(v0.19)</small> 

### Path Dressup 

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Boundary Dressup](Path_DressupPathBoundary.md): Adds a boundary dressup modification to a selected path.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDogbone.png  style="width:32px;"> [避位角修剪](Path_DressupDogbone.md): 在选定的刀路上添加避位角修剪。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDragKnife.png  style="width:32px;"> [拖刀修剪](Path_DressupDragKnife.md): 在选定刀路上添加一个拖刀修剪。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupLeadInOut.png  style="width:32px;"> [引入引出点修剪](Path_DressupLeadInOut.md): 在选定道路上添加引入引出点。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupRampEntry.png  style="width:32px;"> [斜坡修剪](Path_DressupRampEntry.md): 在选定的刀路上添加斜坡修剪。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupTag.png  style="width:32px;"> [夹持耳修剪](Path_DressupTag.md) 在选定刀路上添加一个夹持耳修剪。


</div>

### Supplemental Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Fixture.png  style="width:32px;"> [夹具](Path_Fixture.md): 改变夹具位置


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Comment.png  style="width:32px;"> [备注](Path_Comment.md): 在刀路G-code中加入备注


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Stop.png  style="width:32px;"> [停止](Path_Stop.md): 插入机器停止指令


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Custom.png  style="width:32px;"> [自定义](Path_Custom.md): 插入自定义G-code


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_GcodeFromShape.png  style="width:32px;"> [从形状生成的Gcode](Path_Shape.md): 从选定的零件对象创建刀路对象


</div>


<div class="mw-translate-fuzzy">

### 刀路修改


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Copy.png  style="width:32px;"> [副本](Path_Copy.md): 创建所选刀路对象的参数化副本。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Array.png  style="width:32px;"> [数组](Path_Array.md): 通过复制选定的刀路创建数组。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_SimpleCopy.png  style="width:32px;"> [简化副本](Path_SimpleCopy.md): 创建选定刀路的非参数化副本。


</div>

### Miscellaneous


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Area.png  style="width:32px;"> [特征区域](Path_Area.md):为所选对象创建特征区域


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Area-Workplane.png  style="width:32px;"> [特征区域工作面](Path_Area_Workplane.md): 创建一个特征区域工作面


</div>

### Obsolete


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ToolLibraryEdit.png  style="width:32px;"> [刀具管理器](Path_ToolLibraryEdit/zh.md): 编辑刀具管理器


</div>

## ToolBit architecture 

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture. <small>(v0.19)</small> 

-   [Path Tools](Path_Tools.md)
-   [Path ToolShape](Path_ToolShape.md)
-   [Path ToolBit](Path_ToolBit.md)
-   [Path ToolBit Library](Path_ToolBit_Library.md)
-   [Path ToolController](Path_ToolController.md)

## Other


<div class="mw-translate-fuzzy">

刀路工作台与其他CAM软件包共享许多概念，但有其独特之处。 如果出现问题，这个特点可能是一个很好的排错起点。


</div>


<div class="mw-translate-fuzzy">

### 首选项


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [首选项\...](Path_Preferences.md): 刀路工具中的首选项。


</div>

## 脚本编写


<div class="mw-translate-fuzzy">

见 [刀路脚本页](Path_scripting.md)。


</div>

## Tutorials

-   [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with Path.

## Videos

-   _.
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): a playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) a playlist with a series of 8 videos in English by CAD CAM Lessons.


<div class="mw-translate-fuzzy">


</div>


{{Path_Tools_navi

}} 

_ _

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/zh
