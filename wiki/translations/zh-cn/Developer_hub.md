# <img alt="" src=images/Crystal_Clear_app_tutorials.png  style="width:64px;"> Developer hub/zh-cn





如果你对开发FreeCAD软件有兴趣，想贡献于这个项目的开发，这里正有你该了解的内容。

这些页面还处于开发的早起阶段。如果你找不到想看的信息，如果你在别处看到了有用的信息，而我们没有链接在这里，那么请在[论坛](http://forum.freecadweb.org/index.php?sid=5f84150e79db8842e277b042077097ff)里留下你的评论。会有人仔细看，认真处理它们的（或者，大胆如你，为什么不直接编辑这个页面呢？）。

## Developer Documentation 


<div class="mw-translate-fuzzy">

## 开发者文档

开发者文档由以下部分构成：


</div>

### Compiling FreeCAD 


<div class="mw-translate-fuzzy">

### 请自助：编译FreeCAD

-   [源代码管理](Source_code_management/zh-cn.md)
-   当你遇到了一个问题，或者认为你可能找到了一个Bug，你可以[寻找帮手](Tracker.md)。
-   [在Windows上编译](Compile_on_Windows/zh-cn.md)
-   [在Unix上编译](Compile_on_Linux/zh-cn.md)
-   [在Mac OS X上编译](Compile_on_MacOS/zh-cn.md)
-   关于FreeCAD的[许可协议细节](Licence/zh-cn.md)
-   [第三方程序库](Third_Party_Libraries/zh-cn.md)
-   [第三方工具库](Third_Party_Tools/zh-cn.md)
-   [起始和配置](Start_up_and_Configuration/zh-cn.md)
-   [源文档](Source_documentation/zh-cn.md)


</div>

### Packaging

[Packaging](Packaging.md) consists in taking the compiled binaries and Python source files of FreeCAD, and distributing them for use in a particular system.

-   [Linux packaging](Linux_packaging.md)
    -   [Debian development](Debian_development.md)
    -   [Debian Unstable](Debian_Unstable.md)
    -   [Git buildpackage](Git_buildpackage.md)
-   [Windows packaging](Windows_packaging.md)
-   [MacOS packaging](MacOS_packaging.md)

### Build Support Tools 


<div class="mw-translate-fuzzy">

### 制作支持工具

-   [FreeCAD制作工具](FreeCAD_Build_Tool/zh-cn.md)
    -   [添加应用模块给FreeCAD](Module_Creation/zh-cn.md)
-   [纠错FreeCAD](Debugging/zh-cn.md)
-   [测试FreeCAD](Testing/zh-cn.md)
-   [编译（加速）FreeCAD](Compiling_(Speeding_up)/zh-cn.md)
-   [持续集成](Continuous_Integration/zh-cn.md)


</div>

### Modifying FreeCAD 


<div class="mw-translate-fuzzy">

### 改装FreeCAD

-   理解[FreeCAD的源代码](The_FreeCAD_source_code.md)
-   向FreeCAD或工作台添加[功能](Gui_Command.md)
-   [品牌化或者说](Branding/zh-cn.md)*如何让FreeCAD看起来很特别*
-   我们为FreeCAD做的[艺术工作](Artwork/zh-cn.md)，你可以自由重用
-   [艺术工作指南列出了图标设计的标准](Artwork_Guidelines/zh-cn.md)
-   [翻译FreeCAD](Localisation/zh-cn.md)
-   [附加Python模块](Extra_python_modules/zh-cn.md)，如何在FreeCAD里扩展Python功能
-   [谷歌代码之夏](Google_Summer_of_Code/zh-cn.md)，参与谷歌的学生支持计划


</div>

-   [Translating an external workbench](Translating_an_external_workbench.md)

### Module developer\'s guide 


<div class="mw-translate-fuzzy">

### 模块开发者指南

[FreeCAD模块开发指南](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide)：这是一本电子书，在Github上写作。请分支出去，然后发送拉取请求，来为它贡献内容。


</div>

章节：

-   总体情况和软件架构
-   源代码结构
-   Base和App模块
-   Gui模块
-   Python包封
-   模块设计
-   FEM模块源代码分析（混合了C++和Python）
-   CFD模块的开发（纯Python）
-   模块测试和纠错
-   通过git贡献代码

这个git仓库的最新pdf预览版，可以在[pdf文件夹](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide/tree/master/pdf)下载到。

### Internals


<div class="mw-translate-fuzzy">

### OpenCascade文档

-   [Roman Lygin的教程](http://opencascade.wikidot.com/romansarticles)
-   [完整的在线文档](https://dev.opencascade.org/doc/overview/html/index.html)
-   [参考手册](https://dev.opencascade.org/doc/refman/html/index.html)
-   [OpenCascade维基百科](http://opencascade.wikidot.com)


</div>

OpenCascade is a software development platform for 3D surface and solid modeling, CAD data exchange, and visualization, mostly in the form of C++ libraries.

-   [Roman Lygin\'s tutorials](http://opencascade.wikidot.com/romansarticles)
-   [Full Online Documentation](https://dev.opencascade.org/cdoc/overview/html/index.html)
-   [Reference Manual](https://dev.opencascade.org/doc/refman/html/index.html)
-   [The openCascade wiki](http://opencascade.wikidot.com) (currently containing ?? Chinese spam)

#### File format 

[File Format FCStd](File_Format_FCStd.md). The files created with FreeCAD are `.zip` files that include the [BREP](https://en.wikipedia.org/wiki/Boundary_representation) geometry, as well as XML data that describes the document.

#### Sketcher solver 

-   [Sketcher Solver Architecture Booklet](https://forum.freecadweb.org/viewtopic.php?f=10&t=36355) (forum thread), [source](https://github.com/abdullahtahiriyo/FreeCADBooks/tree/master/FreeCAD_Solver_Architecture) in GitHub.
-   [PlaneGCS solver](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/) in the FreeCAD source code; important files are [GCS.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/GCS.cpp) and [SubSystem.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/SubSystem.cpp).
-   [Recent Several Sketcher improvements](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192).

The sketcher solver isn\'t perfect, as there are some issues with numerical precision when using large values, see [Adventure of fixing sketcher solver for large sketches](https://forum.freecadweb.org/viewtopic.php?f=10&t=40502).

The development of a new solver architecture could improve the way the solver is used both in the [Sketcher Workbench](Sketcher_Workbench.md), and for assembly of 3D bodies. See [Reimplementing constraint solver](https://forum.freecadweb.org/viewtopic.php?f=20&t=40525).

## Roadmap


<div class="mw-translate-fuzzy">

## 路线图

FreeCAD虽然在特定领域已经可用了，但是在跨入主流CAD的路途上，它才走了万里长征第一步。要登上与商业软件一争高下的平台，我们还有很多工作要做。


</div>

[0.20 Development Cycle](0.20_Development_Cycle.md)

## Community

-   [IRC channel](irc://chat.freenode.net/freecad) ,synchronized with [gitter channel](https://gitter.im/FreeCAD/FreeCAD)
-   [Development forum](https://forum.freecadweb.org/viewforum.php?f=6)


<div class="mw-translate-fuzzy">

-   [开发路线图](Development_roadmap/zh-cn.md)


</div>


<div class="mw-translate-fuzzy">

## 信用

[贡献者](Contributors/zh-cn.md)


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Hubs](Category_Hubs.md) > [Developer Documentation](Category_Developer Documentation.md) > Developer hub/zh-cn
