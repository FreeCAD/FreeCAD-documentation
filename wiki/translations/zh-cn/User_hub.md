# <img alt="" src=images/User_hub.png  style="width:64px;"> User hub/zh-cn



这是 FreeCAD 为新手提供主要帮助的区域。


<div class="mw-translate-fuzzy">

FreeCAD 正在持续发展当中，所以可能存在缺少或过时的信息。如果你找不到你想要的信息，请不要犹豫，马上在 [FreeCAD 论坛](https://forum.freecadweb.org) 中进行咨询。


</div>


<div class="mw-translate-fuzzy">

如果你想要为 FreeCAD 作出贡献，请[捐赠](donate.md)，或者参阅 [帮助FreeCAD](Help_FreeCAD/zh-cn.md)页面。如果你想编辑这个维基，请到 [论坛](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830) 中请求一个具有编辑权限的维基账号，并且你遵循 [WikiPages](WikiPages.md) 中描述的通用指引进行编辑。


</div>

如果你有兴趣了解FreeCAD的开发是怎么开始，多年来是怎么进行的，请访问[历史](History.md)页面。



## FreeCAD 的使用 



## 简介

-   [应用总览](About_FreeCAD/zh-cn.md): FreeCAD概况的一个通览。
-   [安装应用](Installing/zh-cn.md): 怎样把FreeCAD安装在[Windows](Install_on_Windows/zh-cn.md), [Linux](Install_on_Linux/zh-cn.md)和[Mac](Install_on_Mac/zh-cn.md)系统上。
-   [帮助文件的安装](Installing_Helpfile/zh-cn.md): 怎样安装基于这个维基的离线文档
-   [起步入门](Getting_started/zh-cn.md): 对各种好用的工具建立一个总体印象。
-   [常见提问](Frequently_asked_questions/zh-cn.md): 经常被问到的题目，这里有答案。
-   [指导教程](Tutorials/zh-cn.md)涉及到了FreeCAD的不同方面。



#### 从其他软件迁移过来？

-   [解决办法](Workarounds/zh-cn.md)
-   [从 Fusion360 迁移至 FreeCAD](Migrating_to_FreeCAD_from_Fusion360/zh-cn.md)
-   [从 OnShape 迁移至 FreeCAD](Migrating_to_FreeCAD_from_OnShape/zh-cn.md)
-   [从 SolidWorks 迁移至 FreeCAD](Migrating_to_FreeCAD_from_SolidWorks/zh-cn.md)
-   [从 Revit 迁移至 FreeCAD](Migrating_to_FreeCAD_from_Revit/zh-cn.md)
-   [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [BIM应用兼容性表](BIM_application_compatibility_table.md)



### 基础应用

-   [界面](Interface/zh-cn.md)：FreeCAD的界面由屏幕上的各种图形元素组成，包括[3D 视图](3D_view/zh-cn.md)、[树视图](Tree_view/zh-cn.md)、[属性编辑器](Property_editor/zh-cn.md)、[任务面板](Task_panel/zh-cn.md) 和[Python 控制台](Python_console/zh-cn.md)。
-   [鼠标导航](Mouse_navigation/zh-cn.md)：使用鼠标或触控板在三维视图中导航的不同类型。
-   [选择方法](Selection_methods/zh-cn.md)：在软件中选择对象的不同方法。
-   [对象名称](Object_name/zh-cn.md)： FreeCAD对象有一个只读的`Name`，可以唯一地识别它们，还有一个`Label`，可以由用户编辑。
-   [首选项编辑器](Preferences_Editor/zh-cn.md)：该系统允许你控制基本系统和各个工作台的许多属性。
-   [文件格式](Import_Export/zh-cn.md)：FreeCAD可以读取和写入的不同文件格式。



### 工作台

[工作台](Workbenches/zh-cn.md)是用于特定任务的工具集合。这些是与每个FreeCAD安装捆绑在一起的基本工作台：

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [标准工具](Std_Base.md). 这些命令和工具存在于所有工作台中。

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> The [Assembly Workbench](Assembly_Workbench.md) for building and solving mechanical assemblies. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> The [BIM Workbench](BIM_Workbench.md) for working with architectural elements and creating [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) models. It combines the Arch Workbench and the formerly external BIM Workbench available in {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> The [CAM Workbench](CAM_Workbench.md) is used to produce G-Code instructions. This workbench was called \"Path Workbench\" in {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [草图工作台](Draft_Workbench.md) 包含 2D 工具和基本的 2D 和 3D CAD 操作。

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [FEM 工作台](FEM_Workbench.md) 提供有限元分析 (FEA) 工作流程。

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> [Inspection Workbench](Inspection_Workbench.md) 旨在为您提供用于检查形状的特定工具。 它仍在开发中。

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> The [Material Workbench](Material_Workbench.md) handles the FreeCAD material system. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> [Mesh Workbench](Mesh_Workbench.md) 用于处理三角网格。

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> [OpenSCAD 工作台](OpenSCAD_Workbench.md) 与 OpenSCAD 的互操作性和修复 [构造立体几何](Constructive_solid_geometry.md) (CSG) 模型历史。

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [零件工作台](Part_Workbench.md) 用于处理几何图元和布尔运算。

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [零件设计工作台](PartDesign_Workbench.md) 用于从草图构建零件形状。

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> 用于处理点云的 [Points Workbench](Points_Workbench.md)。

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> [逆向工程工作台](Reverse_Engineering_Workbench.md) 旨在提供将形状/实体/网格转换为参数化 FreeCAD 兼容功能的特定工具。

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> 用于研究机器人运动的 [Robot Workbench](Robot_Workbench.md)。目前没有被维护

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Sketcher Workbench](Sketcher_Workbench.md) 用于处理几何约束草图。

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> [Spreadsheet Workbench](Spreadsheet_Workbench.md) 用于创建和操作电子表格数据。

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> [Surface Workbench](Surface_Workbench.md) 提供创建和修改表面的工具。 它类似于 [Part Builder](Part_Builder.md) Face from edges 选项。

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> [TechDraw Workbench](TechDraw_Workbench.md) 用于从 3D 模型生成技术图纸。

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> [测试框架工作台](Testing.md) 用于调试 FreeCAD。



### 宏

[Macros](Macros.md) 是相对较小的 [Python](Python.md) 代码片段，用于执行基本 FreeCAD 系统中不可用的简单或复杂任务。

高级用户编写了各种 [macros](macros.md) 来增强 FreeCAD 的更多功能。

从 FreeCAD 0.17 开始，可以使用 [Addon Manager](Std_AddonMgr.md) 安装许多宏。 有关宏列表，请参阅 [宏食谱](Macros_recipes.md) 页面。 对于手动安装，请参阅[如何安装宏](How_to_install_macros.md)。



### 外挂工作台

发烧友们为FreeCAD创建了各种各样的外挂工作台，他们虽然还没有集成到FreeCAD的源代码中，但是他们很容易安装到本地的FreeCAD上面。你可以 [在这里](External_workbenches/zh-cn.md)看到所有已经可用的的工作台。 对于安装这些工作台的指导说明，你可以参考教程[如何安装附加工作台](How_to_install_additional_workbenches.md)。

当许多宏或函数一起开发，并组织在工具栏和菜单中时，它们可以成为一个新的工作台。

[外部工作台](External_workbenches.md) 是不属于基本 FreeCAD 系统一部分的功能集合，通常由经验丰富的用户开发，并针对特定需求。

从 FreeCAD 0.17 开始，可以使用 [Addon Manager](Std_AddonMgr.md) 安装许多工作台。 对于手动安装，请参阅[如何安装附加工作台](How_to_install_additional_workbenches.md)。



## 参考

-   [命令参考](List_of_Commands.md)：FreeCAD可用命令的一份完整清单。



## 在线帮助

这是FreeCAD的官方在线帮助文档。请注意整个在线帮助系统正在重造。它将用来生成一个.CHM格式的文件，附着于FreeCAD二进制安装文件分发。目前，这个在线帮助总结了这个wiki最完整的的一些部分。

-   [在线帮助系统 - 内容目录](Online_Help_Toc/zh-cn.md)



## 更多内容

-   如果你想看到更多FreeCAD的高级用法，就应该去[发烧友入口](Power_users_hub/zh-cn.md)看看。
-   [建筑工作流程](http://yorik.uncreated.net/guestblog.php?tag=freecad)：给出了一个实例，说明FreeCAD开始能在建筑工作流程中找到一席之地了。
-   如果你想帮助FreeCAD项目，请直奔[帮助FreeCAD](Help_FreeCAD/zh-cn.md)页面。
-   [FreeCAD社区贡献大厅](FreeCAD_Community_Portal.md)列出了一些项目，它们围绕FreeCAD，都是社区成员自己做的。
-   不明白一个词或说法在FreeCAD中的意思？试试查阅[词汇表](Glossary.md)吧。



---
⏵ [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/zh-cn
