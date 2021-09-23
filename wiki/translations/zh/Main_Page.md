# Main Page/zh
<div class="mw-translate-fuzzy">

# FreeCAD


<div class="main-menu">


{{Languages-top| {{cn|Main Page/cn}} {{de|Main Page/de}} {{es|Main Page/es}} {{fr|Main Page/fr}} {{it|Main Page/it}} {{pl|Main Page/pl}} {{ru|Main Page/ru}}  {{tr|Main Page/tr}} }}


{{menu}}


</div>


<div class="main-toolbox">


{{screenshot|FreeCAD011.png|0.11 版本的屏幕截图}}


{{newsbox}}

Loading latest commits\...


{{mantisbox}}

Loading facebook widget\...


</div>


<div class="main-content">

**FreeCAD** 是通用且[开源](http://en.wikipedia.org/wiki/Open_source)的三维 [CAD/MCAD](http://en.wikipedia.org/wiki/CAD)/[CAx](http://en.wikipedia.org/wiki/CAx)/[CAE](http://en.wikipedia.org/wiki/Computer-aided_engineering)/[PLM](http://en.wikipedia.org/wiki/Product_Lifecycle_Management) 建模工具, 目标直指[机械工程](http://en.wikipedia.org/wiki/Mechanical_engineering)与[产品设计](http://en.wikipedia.org/wiki/Product_design)，也面向更广泛的工程应用，例如建筑或其他工程领域。FreeCAD 以参数化特征建模为核心功能，基于模块化的软件架构而实现，可在不改动系统核心的的前提下进行功能扩展。

FreeCAD 建立于强大的几何核心 [OpenCasCade](http://en.wikipedia.org/wiki/Open_CASCADE) 之上，采用 [Coin 3D](http://en.wikipedia.org/wiki/Coin3D) 提供的与 [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) 兼容的三维场景模型，并提供丰富的 [Python](http://en.wikipedia.org/wiki/Python_(programming_language)) 应用程序接口，其图形交互界面基于 [Qt](http://en.wikipedia.org/wiki/Qt_(framework)) 实现。FreeCAD 能够确保在 Windows, Mac OS X 与 Linux 平台上运行时用户交互界面的一致性。

![](images/Right_arrow.png ) [了解更多\...](About_FreeCAD/cn.md)

## 核心功能

-   ![](images/Feature1.jpg ) 基于 [Open CASCADE Technology](http://en.wikipedia.org/wiki/Open_CASCADE) 的完整的**几何核心**，对 brep, nurbs, 布尔运算与倒角 (fillet) 等概念提供原生支持，可完成复杂形状类型的三维运算 

-   ![](images/Feature6.jpg ) 支持以插件（模块）形式对核心功能进行扩展的**模块化的软件架构**。所实现的扩展可以像一个全新的应用程序那样复杂，也可像 [Python 脚本](Scripting.md) 或所录制的 [macros](macros.md) 那样简单 

-   ![](images/Feature3.jpg ) 健全的**参数化模型**，支持任意类型的参数驱动对象定制，甚至可[完全用 Python 编程实现](Scripted_objects.md)

-   ![](images/Feature4.jpg ) 可通过内建的 **Python** 解析器，宏或外部脚本操纵 FreeCAD 的全部功能，例如 [几何模型创建与坐标变换](Topological_data_scripting.md), 几何体的二维与三维表示 ([scenegraph](scenegraph.md)) 甚至 [FreeCAD 图形界面](PySide.md) 

-   ![](images/Feature5.jpg ) 支持**标准格式**的数据导入与导出，例如 [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://en.wikipedia.org/wiki/Obj), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://en.wikipedia.org/wiki/Svg), [U3D](http://en.wikipedia.org/wiki/Universal_3D) 与 [STL](http://en.wikipedia.org/wiki/STL_(file_format)) 

## 尚在开发的功能

-   ![](images/Feature7.jpg ) 具备约束求值的[草图 (Sketcher)](Sketcher_Workbench.md) 模块，以实现具有几何约束的二维形状草图建模。目前 草图模块支持多种几何约束类型，可使用它们作为 FreeCAD 中其他对象的构建基础。

-   ![](images/Feature8.jpg ) [工程制图 (Drawing sheets)模块](Drawing_Workbench.md)，用于生成三维模型的二维视图，并能以 SVG 或 PDF 格式输出。该模块虽然仍缺乏许多功能，但是已经具备了强大的 Python 接口支持。

-   ![](images/Feature9.jpg ) [机器人仿真模块](Robot_Workbench.md)，可用于研究机器人运动。该模块目前已具备一个宽泛的图形界面，可仅仅通过图形交互界面进行机器人运动仿真。

-   ![](images/Feature-raytracing.jpg ) [渲染模块](Raytracing_Workbench.md)，可导出三维对象，以供外部渲染工具实现模型渲染，目前仅支持[povray](http://en.wikipedia.org/wiki/POV-Ray)，但是将来有望扩展到其他渲染工具。

-   ![](images/Feature-arch.jpg ) [建筑模块](Arch_Workbench.md)，支持 [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) 风格的工作流程，并兼容 [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes)。建筑模块的设计与实现还在社区讨论阶段，见[这里](http://forum.freecadweb.org/viewtopic.php?f=10&t=821)。

## 手册

FreeCAD 手册提供致力于提供有关 FreeCAD 使用的最好的文档，依赖于社区的努力该文当尚在撰写中，目前已有多种语言的版本。这份文档依然缺乏许多信息，如果你有空闲时间请给予[帮助](Help_FreeCAD.md)!

+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| -   ![](images/Flag-en.jpg ) [Table of contents](Online_Help_Toc.md)       | -   ![](images/Flag-fr.jpg ) [Table des matières](Online_Help_Toc/fr.md) | -   ![](images/Flag-ru.jpg ) [Содержание](Online_Help_Toc/ru.md)           |
| -   ![](images/Flag-pl.jpg ) [Spis Treści](Online_Help_Toc/pl.md)          | -   ![](images/Flag-de.jpg ) [Inhaltsverzeichnis](Online_Help_Toc/de.md) | -   ![](images/Flag-jp.jpg ) [目次](Online_Help_Toc/jp.md)                 |
| -   ![](images/Flag-es.jpg ) [Índice de contenidos](Online_Help_Toc/es.md) | -   ![](images/Flag-tr.jpg ) [İçindekiler](Online_Help_Toc/tr.md)        | -   ![](images/Flag-it.jpg ) [Indice dei contenuti](Online_Help_Toc/it.md) |
| -   ![](images/Flag-cn.jpg ) [目录](Online_Help_Toc/cn.md)                 |                                                                                            |                                                                                              |
+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

## 其他

### 开发动态

从[开发路线页面可获得有关开发计划的一些新闻](Development_roadmap.md)，在[更改记录](http://www.freecadweb.org/tracker/changelog_page.php) 与 [路线图](http://www.freecadweb.org/tracker/roadmap_page.php)页面中可获得当前版本至下一版本发行过程中的一些动态，或者在[项目统计](http://www.ohloh.net/p/freecad)页面查阅有关 FreeCAD 代码库的更为详细的信息。有关开发的所有事宜通过[论坛](http://forum.freecadweb.org/)沟通交流，如果你有兴趣，那么一定要前往。

### 源代码

FreeCAD 可通过 cMake 或 autotools 进行编译，SVN 代码仓库地址位于 <https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk> ，编译指南可根据操作系统环境参考 [Windows](CompileOnWindows.md), [Unix/Linux](CompileOnUnix.md) 与 [MacOSX](CompileOnMac.md)。

### FreeCAD 项目需要你的帮助 

FreeCAD 会[受益于你的帮助](Help_FreeCAD.md), 可以参与测试与[Bug 报告](http://www.freecadweb.org/tracker/main_page.php)，或者参与[指南的撰写](tutorials.md)。我们也缺乏 Mac OS X 平台的用户，如果你有一台 mac 机器，请[帮助我们](CompileOnMac.md)！另外，也欢迎你参与[FreeCAD 本地化翻译工作](Localisation.md)。如果你熟悉 C++ 或 Python 编程并且愿意参与开发，那就更好了，请到[论坛](http://forum.freecadweb.org/)联系我们！

### 订阅 FreeCAD! 

<img alt="" src=images/Twitter.png ) ![](images/Facebook.png ) ![](images/Youtube.png ) ![](images/Googleplus.png  style="width:24px;">


</div>



This is the documentation wiki of [FreeCAD](http://www.freecadweb.org). The information contained here is what forms the offline documentation shipped with FreeCAD itself. You have two main ways to browse through the documentation: by exploring user hubs, or by following the manual. It is a work in progress, written by the community of users and developers of FreeCAD. If you find information that is wrong or missing, please [help](Help_FreeCAD.md)!


</div>

## The hubs 

<img alt="Crystal_Clear_app_display.png" src=images/Crystal_Clear_app_display.png  style="width:64px;"> [Users hub](User_hub.md): This page contains documentation useful for FreeCAD users in general: a list of all the workbenches, detailed instructions on how to install and use the FreeCAD application, tutorials, and all you need to get started.





<img alt="" src=images/Crystal_Clear_app_terminal.png  style="width:64px;"> [Power users hub](Power_users_hub.md): This page gathers documentation for advanced users and people interested in writing python scripts. There you will also find a repository of macros, instructions on how to install and use them, and more information about customizing FreeCAD to your specific needs. 
 <img alt="" src=images/Crystal_Clear_app_tutorials.png  style="width:64px;"> [Developers hub](Developer_hub.md): This section contains material for developers: How to compile FreeCAD yourself, how the FreeCAD source code is structured, how to navigate the source code, how to develop new workbenches, and embed FreeCAD in your own application. 


## Manual

<img alt="Crystal_Clear_manual.png" src=images/Crystal_Clear_manual.png  style="width:64px;"> [The FreeCAD manual](Manual:Introduction.md)  is another, more linear way to present the information contained in this wiki. It is designed to be read like a book, and will gently introduce you to many other pages from the hubs above. [ebook versions](https://www.gitbook.com/book/yorikvanhavre/a-freecad-manual/details) are also available, as well as [a couple of translations in pdf format](https://www.freecadweb.org/manual/).





## Table of contents 

The following table lists all the articles of this wiki that form the backbone of the offline documentation shipped with the FreeCAD application. It is already available in several languages:

+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| -   ![](images/Flag-en.jpg ) [Table of contents](Online_Help_Toc.md)       | -   ![](images/Flag-fr.jpg ) [Table des matières](Online_Help_Toc/fr.md) | -   ![](images/Flag-pt.jpg ) [Tabela de conteúdos](Online_Help_Toc/pt.md) pt |
| -   ![](images/Flag-bg.jpg ) [Съдържание](Online_Help_Toc/bg.md)           | -   ![](images/Flag-hr.jpg ) [Sadržaj](Online_Help_Toc/hr.md)            | -   ![](images/Flag-pt-br.jpg ) [Índice](Online_Help_Toc/pt-br.md) pt-br  |
| -   ![](images/Flag-cn.jpg‎ ) [目錄](Online_Help_Toc/zh.md) zh            | -   ![](images/Flag-id.jpg ) [Daftar isi](Online_Help_Toc/id.md)         | -   ![](images/Flag-ro.jpg ) [Cuprins](Online_Help_Toc/ro.md)                |
| -   ![](images/Flag-cn.jpg ) [目录](Online_Help_Toc/zh-cn.md) zh-cn        | -   ![](images/Flag-it.jpg ) [Sommario](Online_Help_Toc/it.md)           | -   ![](images/Flag-ru.jpg ) [Содержание](Online_Help_Toc/ru.md)             |
| -   ![](images/Flag-cn.jpg‎ ) [目錄](Online_Help_Toc/zh-tw.md) zh-tw      | -   ![](images/Flag-jp.jpg ) [目次](Online_Help_Toc/ja.md) ja            | -   ![](images/Flag-sv.jpg ) [Innehallsforteckning](Online_Help_Toc/sv.md)   |
| -   ![](images/Flag-cs.jpg ) [Obsah](Online_Help_Toc/cs.md)                | -   ![](images/Flag-ko.jpg ) [온라인 도움말](Online_Help_Toc/ko.md)      | -   ![](images/Flag-tr.jpg ) [İçindekiler](Online_Help_Toc/tr.md)            |
| -   ![](images/Flag-de.jpg ) [Inhaltsverzeichnis](Online_Help_Toc/de.md)   | -   ![](images/Flag-pl.jpg ) [Spis Treści](Online_Help_Toc/pl.md)        | -   ![](images/Flag-uk.jpg ) [Інтернет Допомога](Online_Help_Toc/uk.md)      |
| -   ![](images/Flag-es.jpg ) [Índice de contenidos](Online_Help_Toc/es.md) |                                                                                            |                                                                                                |
+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+

## Get involved 

### How to participate 

There is plenty to do inside the FreeCAD project, if you are interested in helping us. Of course, there are programming tasks for C++ or Python programmers, but there are also many things you can do even if you cannot code, such as

-   writing documentation and [editing the wiki (en)](WikiPages.md)
-   helping newcomers
-   translating the application and documentation
-   helping with the packaging of the latest release of FreeCAD for your favourite operating system
-   helping other people around you to discover FreeCAD.

The [help FreeCAD](Special:MyLanguage/help_FreeCAD.md) page describes it all with more details. Starting from 2016, FreeCAD also participates in the [Google Summer of Code](Google_Summer_of_Code.md). The [Contributors hub](Contributors_hub.md) page is another effort to gather the possible ways to help and contribute to the FreeCAD project.

### Source code 

FreeCAD can be compiled on all platforms using [CMake](https://cmake.org/). The source code is [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)-licensed and hosted on [GitHub](https://github.com/FreeCAD/FreeCAD) and mirrored on [GitLab](https://gitlab.com/freecad/FreeCAD) and [CodeBerg](https://codeberg.org/FreeCAD/FreeCAD). There are build instructions for [Windows](Compile_on_Windows.md), [Linux](Compile_on_Linux.md) and [MacOS](Compile_on_MacOS.md). The source code documentation is [hosted here](http://www.freecadweb.org/api/), generated by [Doxygen](Doxygen.md), and [documented on the wiki](Source_documentation.md).

### About the development 

Check the [Development roadmap](Development_roadmap.md) for news about what is being planned, the [Changelog](http://www.freecadweb.org/tracker/changelog_page.php) and [Roadmap](http://www.freecadweb.org/tracker/roadmap_page.php) pages on the [FreeCAD tracker](http://www.freecadweb.org/tracker) to see the progress towards next release, or the [Project statistics](http://www.ohloh.net/p/freecad) for even more information about the FreeCAD codebase. All the development communication happens on the [forum](http://forum.freecadweb.org), so be sure to visit it if you are interested in participating.




[Category:Documentation](Category:Documentation.md)

---
[documentation index](../README.md) > [Documentation](Category:Documentation.md) > Main Page/zh
