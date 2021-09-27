# <img alt="Path workbench icon" src=images/Workbench_Path.svg  style="width:64px;"> Path Workbench/zh-cn


{{TOCright}}

## 简介


<div class="mw-translate-fuzzy">

路径工作台用于从 FreeCAD 3D模型中生成 [数控机床](https://en.wikipedia.org/wiki/CNC_router) 的机器指令。这些产品在数控机床 (如铣刀、车床、激光切割机或类似设备) 上生产真实世界的 3D 物体。通常，指令集是[G 代码](https://en.wikipedia.org/wiki/G-Code) 的方言。


</div>

<img alt="" src=images/pathwb.png  style="width:600px;">


<div class="mw-translate-fuzzy">

FreeCAD 路径工作台工作流程以以下方式创建机器指令:

-   3D 模型是基本对象, 通常使用一个或多个 [零件设计](PartDesign_Workbench.md), [零件](Part_Workbench.md) 或 [底图](Draft_Workbench.md) 工作台。
-   _, 它遵循某些命令控制速度和动作 (通常是 G 代码)。
-   根据作业操作的要求选择工具。
-   铣削路径的创建使用例如 [轮廓](Path_Profile.md) 和 [袖珍](Path_Pocket_3D.md) 操作。这些 [路径对象](Path_objects.md) 使用内部 FreeCAD G 代码方言, 独立于数控机床。


</div>

## General concepts 


<div class="mw-translate-fuzzy">

## 一般概念

路径工作台生成 G 代码，定义了在目标中铣削由 3D 模型表示的项目所需要的路径---在 [路径作业操作 FreeCAD G 代码方言](https://www.freecadweb.org/wiki/Path_scripting#FreeCAD.27s_internal_GCode_format)，然后通过选择合适的后处理器, 将其转换为目标数控控制器的相应方言。

G 代码是从路径作业中包含的指令和操作生成的。 作业工作流按将执行的顺序列出这些任务。通过添加路径操作、路径装饰、路径部分命令和路径修改---从路径菜单或 GUI 按钮。


</div>

The G-code is generated from directives and Operations contained in a Path Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding Path Operations, Path Dressups, Path Supplemental Commands, and Path Modifications from the Path Menu, or GUI buttons.


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

## Limitations

Some current limitations of which you should be aware are:

-   Most of the Path Tools are not true 3D tools but only 2.5D capable. This means that they take a fixed 2D shape and can cut it down to a given depth. However, there are two tools which produce true 3D paths: **<img src="images/Path_3DPocket.svg" width=24px> [3D Pocket](Path_Pocket_3D.md)** and **<img src="images/Path_3DSurface.svg" width=24px> [3D Surface](Path_3DSurface.md)** (which is still an [experimental feature](Path_experimental.md) as of November 2020).
-   Most of Path workbench is designed for a simple, standard 3-axis (xyz) CNC mill/router, but lathe tools are under development in 0.19\_pre.
-   Most operations in Path workbench will return paths based on a standard endmill tool/bit only, regardless of the tool/bit type assigned in a given tool controller with the exception of the **<img src="images/Path_Engrave.svg" width=24px> [Engrave](Path_Engrave.md)** and **<img src="images/Path_3DSurface.svg" width=24px> [3D Surface](Path_3DSurface.md)** operations.
-   The operations within the Path workbench are not aware of clamping mechanisms in use to secure the model to your machine. Consequently, please review and simulate the paths you generate prior to sending the code to your machine. If necessary, model your clamping mechanisms in FreeCAD in order to better inspect the paths generated. Look for possible collisions with clamps or other obstacles along the paths.

## Units

Unit handling in Path can be confusing. There are several points to understand:

1.  FreeCAD base units for length and time are \'mm\' and \'s\' respectively. Velocity is thus \'mm/s\'. This is what FreeCAD stores internally regardless of anything else
2.  The default unit schema uses the default units. If you\'re using the default schema and you enter a feed rate without a unit string, it will get entered as \'mm/s\'
3.  Most CNC machines expect feed rate in the form of either \'mm/min\' or \'in/min\'. Most post-processors will automatically convert the unit when generating gcode.

Schemas:

1.  Changing schema in preferences changes default unit string for the input fields. If you\'re a Path user and prefer to design in metric, it\'s highly recommended that you use the \"Metric Small Parts & CNC\" schema. If you design in US units, either the Imperial Decimal and Building US will work
2.  Changing your preferred unit schema will have no effect on output but will help avoid input errors

Output:

1.  Generating the correct unit in output is the responsibility of the post-processor and is done only at that time
2.  Machine output unit is completely unrelated to your selected unit schema
3.  Post-processors produce either metric (G21) output, Imperial (G20) output or are configurable.
4.  Configurable post-processors default to metric (G21)
5.  If you want your configurable post-processor to output imperial gcode (G20), Set the correct argument in your job output configation (ie \--inches for linuxcnc). This can be stored in a job template and set as your default template to make it automatic for all future jobs

Path Inspection:

1.  If you use the Path Inspect tool to look at g-code, you will see it in \'mm/s\' because it is not being post-processed

## Heights and depths 


<div class="mw-translate-fuzzy">

## 路径命令


</div>

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*

## Commands

Some commands are experimental and not available by default. To enable them see [Path experimental](Path_experimental.md).

### Project Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Job.png  style="width:32px;"> [Job](Path_Job.md): 创建一个新的 CNC 作业


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_PostProcess.png  style="width:32px;"> [Post Process](Path_Post.md): 导出一个项目到 G 代码


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Sanity.png  style="width:32px;"> [Path Errors](Path_Sanity.md): 检查已选择的作业是否有缺失值


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-ExportTemplate.png  style="width:32px;"> [Export Template](Path_ExportTemplate.md): 导出当前作业作为一个模板


</div>

### Tool Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Inspect.png  style="width:32px;"> [G-Code Inspector](Path_Inspect.md): 显示 G 代码以便检查


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Simulator.png  style="width:32px;"> [Simulator](Path_Simulator.md): 显示铣削操作, 就像在机器上做的那样


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-CompleteLoop.png  style="width:32px;"> [Complete Loop](Path_SelectLoop.md): 从两个选定的边完成一个循环


</div>

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width:32px;"> [Toggle the Active State of the Operation](Path_OpActiveToggle.md): Activates or de-activates a path operation.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Toggles the ToolBit Dock. <small>(v0.19)</small> 

### Basic Operations 

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profile](Path_Profile.md): Creates a profile operation of the entire model, or from one or more selected faces or edges. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_Pocket_Shape.svg  style="width:32px;"> [Pocket Shape](Path_Pocket_Shape.md): Creates a pocketing operation from one ore more selected pocket(s).


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Drilling.png  style="width:32px;"> [Drilling](Path_Drilling.md): 执行钻孔循环


</div>

-   <img alt="" src=images/Path_Face.svg  style="width:32px;"> [Face](Path_MillFace.md): Creates a surfacing path.

-   <img alt="" src=images/Path_Helix.svg  style="width:32px;"> [Helix](Path_Helix.md): Creates a helical path.

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptive](Path_Adaptive.md): Creates an adaptive clearing and profiling operation.

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> _. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_Engrave.svg  style="width:32px;"> [Engrave](Path_Engrave.md): Creates an engraving path.


<div class="mw-translate-fuzzy">

### 路径装饰


</div>

### 3D Operations 

-   <img alt="" src=images/Path_3DPocket.svg  style="width:32px;"> [3D Pocket](Path_Pocket_3D.md): Creates a path for a 3D pocket.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-3DSurface.png  style="width:32px;"> [3D Surface](Path_Surface.md): 为 3D 表面创建路径


</div>

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> _. <small>(v0.19)</small> 

### Path Dressup 

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Boundary Dressup](Path_DressupPathBoundary.md): Adds a boundary dressup modification to a selected path.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Dressup.png  style="width:32px;"> [Dogbone Dressup](Path_DressupDogbone.md): Adds a dogbone dressup modification to a selected path


</div>

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width:32px;"> [DragKnife Dressup](Path_DressupDragKnife.md): Adds a dragknife dressup modification to a selected path.

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width:32px;"> [LeadInOut Dressup](Path_DressupLeadInOut.md): Adds a lead-in and/or lead-out point to a selected path.

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width:32px;"> [RampEntry Dressup](Path_DressupRampEntry.md): Adds ramp entry dressup modification to a selected path.

-   <img alt="" src=images/Path_DressupTag.svg  style="width:32px;"> [Tag Dressup](Path_DressupTag.md): Adds a holding tag dressup modification to a selected path.


<div class="mw-translate-fuzzy">

### 部分命令


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Fixture.png  style="width:32px;"> [Fixture](Path_Fixture.md): 改变夹具的位置


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Comment.png  style="width:32px;"> [Comment](Path_Comment.md): 插入一个注释到路径的 G 代码中


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Stop.png  style="width:32px;"> [Stop](Path_Stop.md): 插入一个全部停止机器指令


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Custom.png  style="width:32px;"> [Custom](Path_Custom.md): 插入自定义 G 代码


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_GcodeFromShape.png  style="width:32px;"> [Gcode From a Shape](Path_FromShapes.md): 从选择部分对象创建路径对象


</div>


<div class="mw-translate-fuzzy">

### 路径修改


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Copy.png  style="width:32px;"> [Copy](Path_Copy.md): 创建选定路径对象的参数化副本


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Array.png  style="width:32px;"> [Array](Path_Array.md): 通过复制选定路径创建数组


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_SimpleCopy.png  style="width:32px;"> [Simple Copy](Path_SimpleCopy.md): 创建选定路径对象的非参数副本


</div>

### Miscellaneous


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Area.png  style="width:32px;"> [Feature area](Path_Area.md): 从从所选对象创建一个特征区域


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path-Area-Workplane.png  style="width:32px;"> [Feature area workplane](Path_Area_Workplane.md): 创建一个特征区域工作面


</div>

### Obsolete


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ToolLibraryEdit.png  style="width:32px;"> [Tool Manager](Path_ToolLibraryEdit.md): 编辑工作管理器


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

路径工作台与其它 CAM 软件包共享很多概念但是它有自己的特性。如果有什么不对劲的地方, 这可能是一个很好的开始。


</div>

## Preferences

-   <img alt="" src=images/Preferences-path.svg  style="width:32px;"> [Preferences\...](Path_Preferences.md): Preferences available for the Path Workbench.

## 脚本

See [Path scripting](Path_scripting.md).

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
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/zh-cn
