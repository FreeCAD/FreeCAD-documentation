# CAM Workbench/zh-cn
<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="CAM workbench icon" src=images/Workbench_CAM.svg  style="width:128px;">


</div>






## 简介


<div class="mw-translate-fuzzy">

路径工作台用于从 FreeCAD 3D模型中生成 [数控机床](https://en.wikipedia.org/wiki/CNC_router) 的机器指令。这些产品在数控机床 (如铣刀、车床、激光切割机或类似设备) 上生产真实世界的 3D 物体。通常，指令集是[G 代码](https://en.wikipedia.org/wiki/G-Code) 的方言。


</div>

<img alt="" src=images/pathwb.png  style="width:600px;">


<div class="mw-translate-fuzzy">

FreeCAD 路径工作台工作流程以以下方式创建机器指令:

-   3D 模型是基本对象, 通常使用一个或多个 [零件设计](PartDesign_Workbench.md), [零件](Part_Workbench.md) 或 [底图](Draft_Workbench.md) 工作台。
-   [作业](CAM_Job.md) 是在路径工作台中创建的。这包含了所有信息用于生成数控机床上处理作业的必要 G 代码: 有库存材料, 铣削有一个确定的 [工具集](CAM_ToolBitLibraryOpen.md), 它遵循某些命令控制速度和动作 (通常是 G 代码)。
-   根据作业操作的要求选择工具。
-   铣削路径的创建使用例如 [轮廓](CAM_Profile.md) 和 [袖珍](CAM_Pocket_3D.md) 操作。这些 路径对象 使用内部 FreeCAD G 代码方言, 独立于数控机床。


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## General concepts 


</div>


<div class="mw-translate-fuzzy">

## 一般概念

路径工作台生成 G 代码，定义了在目标中铣削由 3D 模型表示的项目所需要的路径---在 [路径作业操作 FreeCAD G 代码方言](https://www.freecadweb.org/wiki/Path_scripting#FreeCAD.27s_internal_GCode_format)，然后通过选择合适的后处理器, 将其转换为目标数控控制器的相应方言。

G 代码是从路径作业中包含的指令和操作生成的。 作业工作流按将执行的顺序列出这些任务。通过添加路径操作、路径装饰、路径部分命令和路径修改---从路径菜单或 GUI 按钮。


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The G-code is generated from directives and Operations contained in a CAM Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding CAM Operations, Path Dressups, Supplemental Commands, and Path Modifications from the CAM Menu, or GUI buttons.


</div>


<div class="mw-translate-fuzzy">

路径工作台提供了一个工具管理器（库，工具表），和 G 代码检查，和模拟工具。它链接到后处理器，和允许导入和导出工作模板。


</div>


<div class="mw-translate-fuzzy">

路径工作台有一个外部依赖：

1.  FreeCAD 3D 模型单位是在 Edit-\>Preference\...-\>General-\>Units 选项卡的单位进行设置。后处理器配置定义了最终的 G 代码单位。
2.  宏文件路径和几何公差是在Edit-\>Preferences\...-\>Path-\>Job Preferences 选项卡中定义
3.  颜色在 Edit-\>Preferences\...-\>Path-\>Path colors 选项卡中设置
4.  保存标记参数在 Edit-\>Preferences\...-\>Path-\>Dressups 选项卡中设置
5.  基本 3D 模型质量支持路径 WB 要求-通过检查几何。


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Limitations


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Some current limitations of which you should be aware are:

-   Most of the CAM Tools are not true 3D tools but only 2.5D capable. This means that they take a fixed 2D shape and can cut it down to a given depth. However, there are two tools which produce true 3D paths: **<img src="images/CAM_3DPocket.svg" width=24px> [3D Pocket](CAM_Pocket_3D.md)** and **<img src="images/CAM_Surface.svg" width=24px> [3D Surface](CAM_Surface.md)** (which is still an [experimental feature](CAM_experimental.md) as of November 2020).
-   Most of CAM workbench is designed for a simple, standard 3-axis (xyz) CNC mill/router, but lathe tools are under development in 0.19_pre.
-   Most operations in CAM workbench will return paths based on a standard endmill tool/bit only, regardless of the tool/bit type assigned in a given tool controller with the exception of the **<img src="images/CAM_Engrave.svg" width=24px> [Engrave](CAM_Engrave.md)** and **<img src="images/CAM_Surface.svg" width=24px> [3D Surface](CAM_Surface.md)** operations.
-   The operations within the CAM workbench are not aware of clamping mechanisms in use to secure the model to your machine. Consequently, please review and simulate the paths you generate prior to sending the code to your machine. If necessary, model your clamping mechanisms in FreeCAD in order to better inspect the paths generated. Look for possible collisions with clamps or other obstacles along the paths.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Units


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Unit handling in CAM can be confusing. There are several points to understand:

1.  FreeCAD base units for length and time are \'mm\' and \'s\' respectively. Velocity is thus \'mm/s\'. This is what FreeCAD stores internally regardless of anything else
2.  The default unit schema uses the default units. If you\'re using the default schema and you enter a feed rate without a unit string, it will get entered as \'mm/s\'
3.  Most CNC machines expect feed rate in the form of either \'mm/min\' or \'in/min\'. Most post-processors will automatically convert the unit when generating gcode.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Schemas:

1.  Changing schema in preferences changes default unit string for the input fields. If you\'re a CAM user and prefer to design in metric, it\'s highly recommended that you use the \"Metric Small Parts & CNC\" schema. If you design in US units, either the Imperial Decimal and Building US will work.
2.  Changing your preferred unit schema will have no effect on output but will help avoid input errors.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Output:

1.  Generating the correct unit in output is the responsibility of the post-processor and is done only at that time.
2.  Machine output unit is completely unrelated to your selected unit schema.
3.  Post-processors produce either metric (G21) output, Imperial (G20) output or are configurable.
4.  Configurable post-processors default to metric (G21).
5.  If you want your configurable post-processor to output imperial G-code (G20), set the correct argument in your job output configuration (ie \--inches for linuxcnc). This can be stored in a job template and set as your default template to make it automatic for all future jobs.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

CAM Inspection:

1.  If you use the CAM Inspect tool to look at G-code, you will see it in \'mm/s\' because it is not being post-processed.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Heights and depths 


</div>


<div class="mw-translate-fuzzy">

## 路径命令


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Commands


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Some commands are experimental and not available by default. To enable them see [CAM experimental](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Project Commands 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Job.png  style="width:32px;"> [Job](CAM_Job.md): 创建一个新的 CNC 作业


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_PostProcess.png  style="width:32px;"> [Post Process](CAM_Post.md): 导出一个项目到 G 代码


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Sanity.png  style="width:32px;"> [CAM Errors](CAM_Sanity.md): 检查已选择的作业是否有缺失值


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-ExportTemplate.png  style="width:32px;"> [Export Template](CAM_ExportTemplate.md): 导出当前作业作为一个模板


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Tool Commands 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Inspect.png  style="width:32px;"> [G-Code Inspector](CAM_Inspect.md): 显示 G 代码以便检查


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Simulator.png  style="width:32px;"> [Simulator](CAM_Simulator.md): 显示铣削操作, 就像在机器上做的那样


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_SimulatorGL.svg  style="width:32px;"> [CAM SimulatorGL](CAM_SimulatorGL.md): Enables the new, improved CAM simulator. <small>(v1.0)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-CompleteLoop.png  style="width:32px;"> [Complete Loop](CAM_SelectLoop.md): 从两个选定的边完成一个循环


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:32px;"> [Toggle the Active State of the Operation](CAM_OpActiveToggle.md): Activates or de-activates a path operation.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](CAM_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](CAM_ToolBitDock.md): Toggles the ToolBit Dock.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Basic Operations 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Profile.svg  style="width:32px;"> [Profile](CAM_Profile.md): Creates a profile operation of the entire model, or from one or more selected faces or edges.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Pocket_Shape.svg  style="width:32px;"> [Pocket Shape](CAM_Pocket_Shape.md): Creates a pocketing operation from one or more selected pocket(s).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Drilling.png  style="width:32px;"> [Drilling](CAM_Drilling.md): 执行钻孔循环


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_MillFace.svg  style="width:32px;"> [Face](CAM_MillFace.md): Creates a surfacing path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Helix.svg  style="width:32px;"> [Helix](CAM_Helix.md): Creates a helical path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Adaptive.svg  style="width:32px;"> [Adaptive](CAM_Adaptive.md): Creates an adaptive clearing and profiling operation.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Slot.svg  style="width:32px;"> [Slot](CAM_Slot.md): Creates a slotting operation from selected features or custom points. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Engrave.svg  style="width:32px;"> [Engrave](CAM_Engrave.md): Creates an engraving path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Deburr.svg  style="width:32px;"> [Deburr](CAM_Deburr.md): Creates a deburr path.


</div>


<div class="mw-translate-fuzzy">

### 路径装饰


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### 3D Operations 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Pocket_3D.svg  style="width:32px;"> [3D Pocket](CAM_Pocket_3D.md): Creates a path for a 3D pocket.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-3DSurface.png  style="width:32px;"> [3D Surface](CAM_Surface.md): 为 3D 表面创建路径


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Waterline.svg  style="width:32px;"> [Waterline](CAM_Waterline.md): Creates a waterline path for a 3D surface. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Path Dressup 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupAxisMap.svg  style="width:32px;"> [Axis Map](CAM_DressupAxisMap.md): Remaps one axis to another.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupPathBoundary.svg  style="width:32px;"> [Boundary](CAM_DressupPathBoundary.md): Adds a boundary dressup modification to a selected path.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Dressup.png  style="width:32px;"> [Dogbone Dressup](CAM_DressupDogbone.md): Adds a dogbone dressup modification to a selected path


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupDragKnife.svg  style="width:32px;"> [DragKnife](CAM_DressupDragKnife.md): Adds a dragknife dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupLeadInOut.svg  style="width:32px;"> [LeadInOut](CAM_DressupLeadInOut.md): Adds a lead-in and/or lead-out point to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupRampEntry.svg  style="width:32px;"> [RampEntry](CAM_DressupRampEntry.md): Adds ramp entry dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupTag.svg  style="width:32px;"> [Tag](CAM_DressupTag.md): Adds a holding tag dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupZCorrect.svg  style="width:32px;"> [Z Depth Correction](CAM_DressupZCorrect.md): Corrects the Z depth using Probe Map.


</div>




<div class="mw-translate-fuzzy">

### 部分命令


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Fixture.png  style="width:32px;"> [Fixture](CAM_Fixture.md): 改变夹具的位置


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Comment.png  style="width:32px;"> [Comment](CAM_Comment.md): 插入一个注释到路径的 G 代码中


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Stop.png  style="width:32px;"> [Stop](CAM_Stop.md): 插入一个全部停止机器指令


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Custom.png  style="width:32px;"> [Custom](CAM_Custom.md): 插入自定义 G 代码


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Probe.svg  style="width:32px;"> [Probe](CAM_Probe.md): Creates a Probing Grid from a job stock.


</div>

-   <img alt="" src=images/CAM_Shape.svg  style="width:32px;"> [From Shape](CAM_Shape/zh-cn.md): Creates a path object from a selected Part object. [**Experimental**](CAM_experimental.md).




<div class="mw-translate-fuzzy">

### 路径修改


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Copy.png  style="width:32px;"> [Copy](CAM_Copy.md): 创建选定路径对象的参数化副本


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Array.png  style="width:32px;"> [Array](CAM_Array.md): 通过复制选定路径创建数组


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_SimpleCopy.png  style="width:32px;"> [Simple Copy](CAM_SimpleCopy.md): 创建选定路径对象的非参数副本


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Specialty Operations 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ThreadMilling.svg  style="width:32px;"> [Thread Milling](CAM_ThreadMilling.md): Creates a CAM Thread Milling operation from features of a base object. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Miscellaneous


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Area.png  style="width:32px;"> [Feature area](CAM_Area.md): 从从所选对象创建一个特征区域


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Area-Workplane.png  style="width:32px;"> [Feature area workplane](CAM_Area_Workplane.md): 创建一个特征区域工作面


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## ToolBit architecture 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Tools](CAM_Tools.md)
-   [CAM ToolShape](CAM_ToolShape.md)
-   [CAM ToolBit](CAM_ToolBit.md)
-   [CAM ToolBit Library](CAM_ToolBit_Library.md)
-   [CAM ToolController](CAM_ToolController.md)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Other


</div>


<div class="mw-translate-fuzzy">

路径工作台与其它 CAM 软件包共享很多概念但是它有自己的特性。如果有什么不对劲的地方, 这可能是一个很好的开始。


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Preferences


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Preferences-cam.svg  style="width:32px;"> [Preferences\...](CAM_Preferences.md): Preferences available for the CAM Workbench.


</div>



## 脚本


<div lang="en" dir="ltr" class="mw-content-ltr">

See [CAM scripting](CAM_scripting.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Tutorials


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Walkthrough for the Impatient](CAM_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with CAM.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Videos


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): A playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [CAM Workbench](CAM_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): A playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ): A playlist with a series of 8 videos in English by CAD CAM Lessons.
-   Also see the [Computer-Aided Manufacturing (CAM) section](Video_tutorials#Computer-Aided_Manufacturing_(CAM).md) of the [Video tutorials](Video_tutorials.md) wiki page.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Roadmap


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Development Roadmap](CAM_Development_Roadmap.md): Read this if you are a developer and want to contribute to CAM.


</div>


<div class="mw-translate-fuzzy">


</div>


{{CAM_Tools_navi

}} 

[分类:用户文档](Category:User_Documentation/zh-cn.md)



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [CAM](Category_CAM.md) > CAM Workbench/zh-cn
