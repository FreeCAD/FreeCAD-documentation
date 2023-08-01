# Getting started/zh-cn
{{TOCright}}



## 前言


<div class="mw-translate-fuzzy">

## 引言

FreeCAD是面向CAD/CAE的3D[参数化建模应用程序](About_FreeCAD/zh-cn.md)。它主要用于机械设计，还可用于您需要精确建模3D对象并控制建模历史的所有其他用途。


</div>


<div class="mw-translate-fuzzy">

FreeCAD已经开发了一段时间，它提供了大量（并且不断增长）的[特征列表](Feature_list/zh-cn.md)，但仍然能力不足，特别是将其与商业解决方案进行比较，它并未开发完整，因此不足以用于大多数生产环境。对于大多数爱好者而言，还有很多较小的工场环境，它**是**足够强大的。这里有一个快速增长的[社区](http://forum.freecadweb.org/index.php)，由热情的用户组成。你可以找到使用FreeCAD开发高质量项目的[许多例子](http://forum.freecadweb.org/viewtopic.php?f=8&t=1222)。


</div>


<div class="mw-translate-fuzzy">

像所有的开放源码项目一样，FreeCAD 项目不是开发人员向您发送的单向工作。它取决于其社区的成长，获取功能和稳定（修复错误）。所以当开始使用 FreeCAD 的时候不要忘记这个，如果你喜欢，可以直接影响和[帮助项目](Help_FreeCAD/zh-cn.md)！


</div>

See also:

-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)
-   [Which workbench should I choose?](Which_workbench_should_I_choose.md)
-   [Tutorials](Tutorials.md)
-   [Video tutorials](Video_tutorials.md)



## 安装


<div class="mw-translate-fuzzy">

（如果还没有完成）首先请下载并安装FreeCAD。有关如何安装FreeCAD的信息，请参阅[下载页面](Download/zh-cn.md)，了解有关当前版本和更新的信息；请参阅[安装页面](Installing/zh-cn.md)，了解怎样安装FreeCAD的信息。有安装包可用于 Windows（.msi）、Ubuntu、Debian（.deb）、openSUSE（.rpm）和Mac OSX。 在其他Linux发布版上，FreeCAD可以通过安装包管理器来安装；还有一个独立的可执行文件**AppImage**，可以运行于大多数64位的Linux系统上。FreeCAD是开源的，因此，如果你是喜欢冒险的，想看看现在开发的全新功能，你还可以自己抓取源代码和[编译FreeCAD](Compiling.md)。


</div>




<div class="mw-translate-fuzzy">

## 探索 FreeCAD 


</div>

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_interface.png  style="width:1024px;">


</div>


<div class="mw-translate-fuzzy">

1.  3D视图，显示文档的内容
2.  树视图，显示文档中所有对象的层次结构和构造历史
3.  [属性编辑器](Property/zh-cn.md)，允许您查看和修改所选对象的属性
4.  报表视图（或输出窗口），这是FreeCAD打印消息，警告和错误的地方
5.  python控制台，其中打印所有由FreeCAD执行的命令，以及可以在那里输入python代码
6.  [工作台选择器](Workbenches/zh-cn.md)，您可以在其中选择活动的工作台


</div>


<div class="mw-translate-fuzzy">

FreeCAD接口背后的主要概念是将它分成[工作台](workbenches/zh-cn.md)。工作台是适用于特定任务的工具集合，例如使用[网格或绘图](Mesh_Workbench/zh-cn.md)[2D对象或](Draft_Workbench/zh-cn.md)[约束草图](Sketcher_Workbench/zh-cn.md)。您可以使用工作台选择器切换当前的工作台 (6)。您可以通过[自定义每个工作台中包含的工具](Interface_Customization/zh-cn.md)，从其他工作台中添加工具，甚至自行创建的工具，我们称之为[宏](macros/zh-cn.md)。广泛使用的起点是[零件设计工作台和](PartDesign_Workbench/zh-cn.md)[零件工作台](Part_Workbench/zh-cn.md)。


</div>


<div class="mw-translate-fuzzy">

当您第一次启动FreeCAD时，会显示起始中心。这是起始中心的大概样子：


</div>

<img alt="" src=images/Start_center_0.19_screenshot.png  style="width:600px;">


<div class="mw-translate-fuzzy">

起始中心允许您快速跳转到最常见的工作台之一，打开最近的文件之一，或查看 FreeCAD 世界的最新消息。您可以在[首选项中更改默认工作台](Preferences_Editor/zh-cn.md)。


</div>



## 在3D空间中导航


<div class="mw-translate-fuzzy">

FreeCAD有几种不同的[导航模式可用](Mouse_Model/zh-cn.md)，改变了您使用鼠标与3D视图和视图本身中的对象进行交互的方式。其中一个专为[触摸板而设计](Mouse_Model/zh-cn#Touchpad_Navigation.md)，其中中间的鼠标按钮不被使用。下表描述了默认模式，称为**CAD导航**（您可以通过右键单击3D视图的空白区域来快速更改当前的导航模式）：


</div>


<div class="mw-translate-fuzzy">

您还可以在视图菜单和视图工具栏以及数字快捷键（**1**，**2**等）中提供多个视图预设（顶视图，前视图等），并且通过右键单击3D视图的对象或空白区域，您可以快速访问一些常见的操作，例如设置特定视图或在树视图中查找对象。


</div>



## 与 FreeCAD 的第一步 


<div class="mw-translate-fuzzy">

FreeCAD的重点是允许您制作高精度3D模型，以便对这些模型进行严格的控制（能够回溯到建模历史记录和更改参数），并最终建立这些模型（通过3D打印，CNC加工甚至是施工现场）。因此，与其他用途的其他3D应用程序（例如动画电影或游戏）非常不同。它的学习曲线可能很陡，特别是如果这是您第一次接触3D建模。如果您在某些时候遇到任何问题，请不要忘记，[FreeCAD论坛](http://forum.freecadweb.org/index.php)上友好的社区用户们可能会随时救你出来。


</div>


<div class="mw-translate-fuzzy">

您将在FreeCAD中开始使用的工作台取决于您需要做的工作类型：如果要使用机械模型，或者更常用的任何小型对象，则可能需要尝试[零件设计工作台](PartDesign_Workbench/zh-cn.md)。如果您将在2D中工作，则如果需要约束，则切换到[草图工作台或](Draft_Workbench/zh-cn.md)[素描工作台](Sketcher_Workbench/zh-cn.md)。如果你想做BIM，启动[建筑工作台](Arch_Workbench/zh-cn.md)。如果您正在使用船舶设计，那么您将会有一个特殊的[船舶工作台](Ship_Workbench/zh-cn.md)。如果您来自OpenSCAD世界，请尝试[OpenSCAD 工作台](OpenSCAD_Workbench/zh-cn.md)。


</div>


<div class="mw-translate-fuzzy">

您可以随时切换工作台，还可以通过[自定义您最喜欢的工作台来添加其他工作台的工具](Interface_Customization/zh-cn.md)。


</div>



## 在零件设计工作台和构图工作台 中工作 


<div class="mw-translate-fuzzy">

[零件设计工作台专门用于构建复杂的对象](PartDesign_Workbench/zh-cn.md)，从简单的形状开始，添加或删除零件（我们称之为"特性"），直到找到最终的对象。您在建模过程中应用的所有功能都存储在名为[树视图的单独视图中](Document_structure/zh-cn.md)，该视图还包含文档中的其他对象。您可以将PartDesign对象视为一系列操作，每个操作都应用于前一个操作的结果，形成一个大链。在树视图中，您可以看到最终的对象，但可以展开它并检索所有先前的状态，并更改任何参数，这些参数会自动更新到最终对象。


</div>


<div class="mw-translate-fuzzy">

零件设计工作台大量使用另一个工作台，[素描工作台](Sketcher_Workbench/zh-cn.md)。素描器允许您绘制2D形状，通过将约束应用于 2D 形状来定义。例如，您可以绘制一个矩形，并通过将长度约束应用于其中一边来设置边的大小。那边那边不能再调整大小了（除非修改了约束）。


</div>

使用素描绘制器制作的2D形状在零件设计工作台中使用很多，例如创建3D卷，或者绘制对象面上的区域，然后将其从主卷空心化。这是一个典型的零件设计工作流程：

1.  创建一个新的素描
2.  绘制一个封闭的形状（确保所有点都被连接起来）
3.  关闭素描
4.  使用垫工具将素描展开成3D立体
5.  选择固体的一个面
6.  创建一个第二个素描（这一次将在所选的面上绘制）
7.  画一个封闭的形状
8.  关闭素描
9.  从第二个素描，在第一个对象上创建一个口袋

这给你一个这样的对象：

<img alt="" src=images/Partdesign_example.jpg  style="width:600px;">

在任何时候，您可以选择原始素描并进行修改，或更改垫或挤压操作的缩放参数，这将更新最终对象。



## 在草图和建筑工作台中工作


<div class="mw-translate-fuzzy">

虽然它们遵循与所有FreeCAD相同的规则，但[草图工作台和](Draft_Workbench/zh-cn.md)[建筑工作台的作用与其他工作台略有不同](Arch_Workbench/zh-cn.md)。简而言之，素描和零件设计主要是为了设计单件，但是在使用几个更简单的对象时，草稿和建筑是为了简化您的工作。


</div>


<div class="mw-translate-fuzzy">

[草图工作台为您提供了](Draft_Workbench/zh-cn.md)2D工具，它们类似于传统2D CAD应用程序（例如[AutoCAD](https://en.wikipedia.org/wiki/AutoCAD)）。然而，2D绘图绝非FreeCAD的使用范围，不要指望它会提供这些专用应用程序所提供的各种工具。大多数草图工具不仅可以在2D平面中工作，还能在完整的3D空间中工作，还可以从[工作面和](Draft_SelectPlane/zh-cn.md)[物体捕捉等特殊辅助系统中受益](Draft_Snap/zh-cn.md)。


</div>


<div class="mw-translate-fuzzy">

[建筑工作台将](Arch_Workbench/zh-cn.md)[BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling)工具添加到FreeCAD中，允许您使用参数对象构建架构模型。 Arch工作台高度依赖于其他模块，如草图和素描。所有的草图工具也都存在于建筑工作台中，大多数建筑工具都使用了草图辅助系统。


</div>

建筑和草图工作台的典型工作流程可能是：

1.  使用"草图线"工具绘制几行
2.  选择每一行，然后按墙壁工具在每个行上构建一个墙
3.  通过选择墙壁并按下拱形添加工具来加入墙壁
4.  创建一个楼层对象，并从树视图中移动它的墙壁
5.  创建一个建筑对象，并从树视图中移动你的楼层
6.  通过单击窗口工具创建一个窗口，在面板中选择一个预设，然后点击墙上的一个面
7.  通过首先设置工作平面（如有必要），然后使用草图尺寸工具，添加尺寸

这样做会给你这个：

<img alt="" src=images/Arch_workflow_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

More on the [指南](Tutorials/zh-cn.md) page.


</div>




<div class="mw-translate-fuzzy">

## 脚本


</div>

FreeCAD, as an open source software, offers the possibility to supplement its workbenches with addons.

The [Addon](Addon.md) principle is based on the development of a workbench complement. Any user can develop a function that he or she deems to be missing for her/his own needs or, ultimately, for the community. With the forum, the user can request an opinion, help on the forum. It can share, or not, the object of its development according to copyright rules to define. Free to her/him. To develop, the user has available [scripting](scripting.md) functions.

There are two types of addons:

1.  [Macros](Macros.md): short snippets of Python code that provide a new tool or functionality. Macros usually start as a way to simplify or automate the task of drawing or editing a particular object. If many of these macros are collected inside a directory, the entire directory may be distributed as a new workbench.
2.  [External workbenches](External_workbenches.md): collections of tools programmed in Python or C++ that extend FreeCAD in an important way. If a workbench is sufficiently developed and is well documented, it may be included as one of the base workbenches in FreeCAD. Under [External workbenches](External_workbenches.md), you\'ll find the principle and a list of existing library.

## Scripting


<div class="mw-translate-fuzzy">

最后，FreeCAD最强大的功能之一是[脚本环境](scripting/zh-cn.md)。从集成的python控制台（或任何其他外部Python脚本），您可以访问FreeCAD的几乎任何部分，创建或修改几何对象，修改3D场景中的对象的表示或访问和修改FreeCAD界面。 Python脚本也可以在[宏中使用](macros/zh-cn.md)，它提供了一种创建自定义命令的简单方法。


</div>




<div class="mw-translate-fuzzy">

## 版本更新


</div>


<div class="mw-translate-fuzzy">

-   [版本 0.17 发行说明](Release_notes_0.17/zh-cn.md) : 检查 FreeCAD 发行版 0.17 的新特性
-   [版本 0.16 发行说明](Release_notes_0.16/zh-cn.md) : 检查 FreeCAD 发行版 0.16 的新特性
-   [版本 0.15 发行说明](Release_notes_0.15/zh-cn.md) : 检查 FreeCAD 发行版 0.15 的新特性
-   [版本 0.14 发行说明](Release_notes_0.14/zh-cn.md) : 检查 FreeCAD 发行版 0.14 的新特性
-   [版本 0.13 发行说明](Release_notes_0.13/zh-cn.md) : 检查 FreeCAD 发行版 0.13 的新特性
-   [版本 0.12 发行说明](Release_notes_0.12/zh-cn.md) : 检查 FreeCAD 发行版 0.12 的新特性
-   [版本 0.11 发行说明](Release_notes_0.11/zh-cn.md) : 检查 FreeCAD 发行版 0.11 的新特性


</div>


<div class="mw-translate-fuzzy">


{{docnav|Install on Mac/zh-cn|Mouse Model/zh-cn}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > Getting started/zh-cn
