# Getting started/zh
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## 前言

FreeCAD是一种3D[参数化建模程序](About_FreeCAD/zh.md)。它主要用于机械设计，对所有需要精确建模3D物体并能够控制建模过程的情况都适用。

FreeCAD自2002年起开始开发，它可以提供很多的[功能](Feature_list/zh.md)。 它仍有一些功能缺失，但对于多数业余爱好者和许多小型工厂来说它足够强大。在[FreeCAD论坛](http://forum.freecadweb.org/index.php)有一个由热情的用户组成的快速增长的社区，在那你可以发现许多用FreeCAD开发的项目[示例](https://forum.freecadweb.org/viewforum.php?f=24)。也可以看看[FreeCAD 产品应用](FreeCAD_used_in_production/zh.md)。

像所有开源项目，FreeCAD依靠它的社区的成长、收集功能以及修复缺陷。所以在使用FreeCAD的时候不要忘记这一点，如果你愿意，你可以 [捐献并以各种方式](Donate.md)[帮助FreeCAD](help_FreeCAD/zh.md)，例如编写文档以及进行翻译工作。

查看其他：

-   [将Fusion360集成到FreeCAD](Migrating_to_FreeCAD_from_Fusion360.md)
-   [教程](Tutorials/zh.md)
-   [视频教程](Video_tutorials.md)

## 安装

首先，下载并安装FreeCAD。参见[下载页面获取当前的版本和更新信息](Download.md)，以及适用于你的操作系统的安装说明([Windows](Installing_on_Windows.md), [Linux](Installing_on_Linux.md) or [Mac](Installing_on_Mac.md))。有可用的安装包支持Windows(.msi)，Debian和Ubuntu (.deb), openSUSE (.rpm)以及Mac OSX环境。FreeCAD也可以通过许多Linux发行版的安装包管理器获取。同时还有可以在最新64位Linux系统上运行的独立[AppImage可执行文件](AppImage.md)。FreeCAD是开源的，你也可以获取源代码并且自己[编译它](Compiling.md)。

## 浏览界面

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;"> 
*0.19版标准界面。*


</div>


**在 [界面](Interface.md)中查看完整说明.**


:   1\. The [主视图区域](main_view_area.md), 包含各种Tabbed标签窗口, 主要是 [3D 视图](3D_view.md)。
:   2\. [三D视图](3D_view.md),显示文件中的几何对象.
:   3\. [树视图](tree_view.md) ([组合视图的一部分](combo_view.md)), 显示文档中对象的层次结构和构造历史； 它还可以显示激活的命令的[任务面板](task_panel.md)。
:   4\. [属性编辑器](property_editor.md)（[组合视图的一部分](combo_view.md)），允许查看和修改所选对象的属性。
:   5\. [选择视图](selection_view.md)，表示所选择的对象（顶点，边缘，面）或对象的子元素。
:   6\. [报告视图](report_view.md)（或输出窗口），显示信息，警告和错误。
:   7\. [ Python控制台](Python_console.md)，在这里所有命令的执行都被打印出来，并可以在其中输入[ Python代码](Python.md)。
:   8\. [状态栏](status_bar.md)，其中会显示一些消息和工具提示。
:   9\. 工具栏所在的工具栏区域。
:   10\. [工作台选择器](Std_Workbench.md)，在其中选择[工作台](workbenches.md)。
:   11\. [标准菜单](Standard_Menu.md)，包含程序的基本操作。


<div class="mw-translate-fuzzy">

FreeCAD界面背后的主要概念是它被分成 [工作台](workbenches.md)。一个工作台是一批适用于特定任务的工具的集合，比如使用[网格](Mesh_Workbench.md)、绘制[2D对象](Draft_Workbench.md)、 [带约束的草图](Sketcher_Workbench.md)。你可以通过[工作台选择器切换当前工作台](Std_Workbench.md)。你可以[定制在每个工作台中包含的工具](Interface_Customization.md)、添加其他工作台的工具甚至自己创建工具(我们称之为[宏命令](macros.md))。被广泛使用的设计工作起始点是[零件设计工作台](PartDesign_Workbench.md) 和[零件工作台](Part_Workbench.md).


</div>


<div class="mw-translate-fuzzy">

当你启动FreeCAD的时候，你将会看到启动中心。下面你看到的是0.18版的启动中心:


</div>

<img alt="" src=images/Start_center_0.19_screenshot.png  style="width:600px;">


<div class="mw-translate-fuzzy">

启动中心使你可以快速跳转到常用的工作台，打开最近编辑过的文件或者查看来自FreeCAD世界最近的新闻。你可以在[设置中修改默认工作台](Preferences_Editor.md)。


</div>

## 3D空间操控


<div class="mw-translate-fuzzy">

FreeCAD有许多不同的[鼠标操控模式可用](Mouse_Model.md), 选择不同的操控模式会改变你使用鼠标操控3D视图中对象和改变3D视图方式。操控模式有一个是特别为触控板设计的[触控板](Mouse_Model#Touchpad_Navigation.md), 该模式下鼠标中键不可用. 下列表格中描述了默认操控模式，叫做**CAD操作** (你可以通过在3D视图的空白处右键单击跳出的菜单中进行选择以迅速改变当前操控:)


</div>

预设的视图(顶视图、前视图等)，可以通过试图菜单、视图工具栏和数字快捷键(**1**, **2**, 等等)进行使用。通过右键单击对象或三维视图的空白区域，可以快速使用一些常见操作，例如设置特定视图或在树视图中定位对象。

## 和FreeCAD一起迈进的第一步

Freecad的关注点是让你能够制作高精度的3D模型，对这些模型保持严格的控制（能够回溯建模历史并更改参数），并最终建立这些模型（通过3D打印、CNC加工甚至施工现场）。因此，它与其他一些用于其他目的的3D应用程序非常不同，例如动画电影或游戏。它的学习曲线可能很陡，特别是如果这是你第一次接触三维建模。如果你学习的过程在某个点上被卡住了，不要忘记[freecad论坛](http://forum.freecadweb.org/index.php)上友好的用户社区可能很快就能帮你解决问题。


<div class="mw-translate-fuzzy">

你将在FreeCad中开始使用的工作台取决于你需要做的工作类型：如果你要处理机械模型，或者更一般地说，任何小规模的对象，你可能需要尝试[零件设计工作台](PartDesign_Workbench.md)。如果你将在二维环境工作，请切换到[制图工作台](Draft_Workbench.md)，或 [草图工作台](Sketcher_Workbench.md) 如果你需要约束。如果你想做BIM，启动[Arch工作台](Arch_Workbench.md)。如果你现在在使用Openscad，请尝试[Openscad工作台](OpenSCAD_Workbench.md)。也有一些由社区开发的[扩展工作台](External_Workbenches.md)


</div>


<div class="mw-translate-fuzzy">

你可以随时切换工作台，也可以在你最喜欢的工作台上通过添加其他工作台上的工具[定制你喜欢的工作台](Interface_Customization.md)。


</div>

## 使用零件设计和草图工作台


<div class="mw-translate-fuzzy">

[零件设计工作台是专门为构建复杂对象而设计的](PartDesign_Workbench.md)，从简单的形状开始，然后添加或删除一些而部分（被称为"功能"），直到完成最终对象。在建模过程中应用的所有功能都存储在一个名为[树视图的单独视图中](Document_structure.md)，该视图还包含文档中的其他对象。您可以将零件设计对象视为一系列操作，每个操作都应用于前一个操作的结果，形成一个大链路。在树视图中，可以看到最终对象，但可以展开它并检索所有先前的状态，并更改它们的任何参数，这些参数将自动更新最终对象。


</div>


<div class="mw-translate-fuzzy">

零件设计工作台大量使用另一个工作台，即[草图工作台](Sketcher_Workbench.md)。草图工作台允许你绘制二维形状，通过对二维形状强制约束来定义二维形状。例如，可以绘制一个矩形，并通过对其中一个边强制长度约束来设置边的大小。然后该边的大小无法再调整（除非更改约束）。


</div>

这些使用草图绘制的二维形状在零件设计工作台中被大量使用，例如创建三维体，或在对象的面上绘制图形，然后从其主体中按该图形形状掏出空心。以下是一个典型的零件设计工作流:

1.  创建新草图
2.  绘制闭合形状（确保所有点都已连接）
3.  关闭草图
4.  使用填充工具将草图展开为三维实体
5.  选择实体的一个面
6.  创建第二个草图（这次将在选定面上绘制）
7.  绘制闭合形状
8.  关闭草图
9.  从第一个对象上的第二个草图创建一个开槽

以上操作会给你如下的结果：

<img alt="" src=images/Partdesign_example.jpg  style="width:600px;">

你随时可以选择原始草图并对其进行修改，或者更改"填充"或"挖槽"操作的拉伸参数以更新最终对象。

## 使用绘图和建筑工作台


<div class="mw-translate-fuzzy">

[制图工作台和](Draft_Workbench.md)[建筑工作台的作用与之前提到的其他工作台稍有不同](Arch_Workbench.md)，尽管它们遵循相同的FreeCAD工作台通用的规则。简言之，草图和零件设计主要用于设计单个零件，但在处理多个更简单的对象时，制图和建筑工作台可以简化您的工作。


</div>


<div class="mw-translate-fuzzy">

[制图工作台为你提供了与传统二维制图CAD应用程序](Draft_Workbench.md)（[autocad](https://en.wikipedia.org/wiki/autocad)）中类似的二维制图工具。然而，二维制图远超Freecad所能及的范围，请不要期待着能在这里找到这些专用应用程序提供的全套工具。大多数制图工具不仅在二维平面中工作，而且在整个三维空间中工作，并且受益于特殊的辅助系统，如[工作面和](Draft_SelectPlane.md)[对象捕捉](Draft_Snap.md)。


</div>


<div class="mw-translate-fuzzy">

\[arch module\|建筑工作台\]向freecad添加了[bim](http://en.wikipedia.org/wiki/building_information_modeling)工具，允许您使用参数化对象构建建筑模型。建筑工作台广泛依赖于其他模块，如制图和草图。所有制图工具也都存在于Arch工作台中，并且大多数Arch工具都使用制图工作台的帮助系统。


</div>

使用建筑和制图工作台的典型工作流可能是：

1.  用制图工作台"画线"工具画几条线
2.  选择每一条线并按下"墙体"工具按钮在每一条线上构建墙体
3.  通过选择墙并按"建筑添加"工具连接墙
4.  创建地板对象，并从树视图中移动其中的墙
5.  创建建筑对象，并从树视图中移动其中的楼层
6.  通过单击"窗户"工具创建窗户，在其面板中选择预设值，然后单击墙的某个面。
7.  如有必要，首先设置工作平面，然后使用制图工作台中的"尺寸标注"工具添加尺寸。

你将得到如下结果：

<img alt="" src=images/Arch_workflow_example.jpg  style="width:600px;">

更多信息见[指南页面](Tutorials.md).

## 插件，宏文件和外部工作台


<div class="mw-translate-fuzzy">

Freecad作为一种开放源代码软件，提供了使用插件补充其工作台的可能性。


</div>

[插件原理基于工作台补充的开发](Addon.md)。 任何用户都可以开发出他或她认为自己或自己的社区或最终社区所需的功能。 使用论坛，用户可以在论坛上提出意见和帮助。 它可以根据版权规则定义是否共享其开发对象。 对她或他免费。 为了进行开发，用户具有可用的[脚本功能](scripting.md)。


<div class="mw-translate-fuzzy">

有两种类型的插件： ＃[宏](Macros.md)：提供新工具或功能的Python代码的简短片段。 宏通常以简化或自动化制图或编辑特定对象的任务的方式开始。 如果这些宏中有许多收集在目录中，则整个目录可以作为新工作台分发。 ＃[外部工作台](External_workbenches.md)：用Python或C ++编程的工具的集合，这些工具以一种重要的方式扩展了FreeCAD。 如果工作台充分开发并有充分的文档记录，则它可以作为FreeCAD中的基本工作台之一包含在内。 在[外部工作台下](External_workbenches.md)，您会找到原理和现有库的列表。


</div>

## 脚本编写

最后，FreeCad最强大的功能之一是[脚本编写环境](scripting.md)。从集成的python控制台（或任何其他外部python脚本），您可以控制FreeCAD的几乎任何部分。创建或修改几何图形、修改3D场景中这些对象的表现形式、或控制和修改FreeCAD界面。python脚本也可以用于[宏脚本](Macros.md)，它提供了一种创建自定义命令的简单方法。

## 新特性

-   详细特性清单见[发行说明](Feature_list#Release_notes.md)


<div class="mw-translate-fuzzy">





</div>


{{Userdocnavi/zh}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Getting started/zh
