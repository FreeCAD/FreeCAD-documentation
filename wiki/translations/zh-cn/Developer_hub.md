# <img alt="" src=images/Crystal_Clear_app_tutorials.png  style="width:64px;"> Developer hub/zh-cn



如果你对开发FreeCAD软件有兴趣，想贡献于这个项目的开发，这里正有你该了解的内容。

这些页面还处于开发的早起阶段。如果你找不到想看的信息，如果你在别处看到了有用的信息，而我们没有链接在这里，那么请在[论坛](http://forum.freecadweb.org/index.php?sid=5f84150e79db8842e277b042077097ff)里留下你的评论。会有人仔细看，认真处理它们的（或者，大胆如你，为什么不直接编辑这个页面呢？）。



## 开发者文档

开发者文档由以下部分构成：



### 编译 FreeCAD 


<div class="mw-translate-fuzzy">

-   [Github 代码库](https://github.com/FreeCAD/FreeCAD). 如果你是git新手, 请阅读[Source code management](Source_code_management.md)
-   [用Docker编译](Compile_on_Docker.md)
-   [在Windows上编译](Compile_on_Windows.md)
-   [在Linux上编译](Compile_on_Linux.md)
-   [在Mac OS X上编译](Compile_on_MacOS.md)
-   关于FreeCAD的[许可协议细节](License/zh-cn.md)
-   [第三方程序库](Third_Party_Libraries.md)
-   [第三方工具库](Third_Party_Tools.md)
-   [起始和配置](Start_up_and_Configuration.md)
-   [源文档](Source_documentation/zh-cn.md)
-   当你有问题或你认为发现了一个bug的时候，请使用 [bug tracker](Tracker.md) 。


</div>



### 打包

[打包](Packaging.md) 包括取得编译好的FreeCAD的二进制文件和Python源文件和将他们分发到使用的系统中

-   [Linux 打包](Linux_packaging.md)
    -   [Debian 开发版](Debian_development.md)
    -   [Debian 不稳定版](Debian_Unstable.md)
    -   [Git 构建包](Git_buildpackage.md)
-   [Windows 打包](Windows_packaging.md)
-   [MacOS 打包](MacOS_packaging.md)



### 制作支持工具

-   [FreeCAD构建工具](FreeCAD_Build_Tool/zh-cn.md)
    -   [添加应用模块](Module_Creation/zh-cn.md)给FreeCAD
-   [调试FreeCAD](Debugging/zh-cn.md)
-   [测试FreeCAD](Testing/zh-cn.md)
-   [编译（加速）FreeCAD](Compiling_(Speeding_up)/zh-cn.md)
-   [持续集成](Continuous_Integration/zh-cn.md)



### 修改FreeCAD


<div class="mw-translate-fuzzy">

-   理解[FreeCAD的源代码](The_FreeCAD_source_code.md)
-   向FreeCAD或工作台添加[功能](Gui_Command.md)
-   [品牌化](Branding/zh-cn.md)或者说*如何让FreeCAD看起来很特别*
-   我们为FreeCAD做的[艺术工作](Artwork/zh-cn.md)，你可以自由重用
-   [艺术工作指南](Artwork_Guidelines/zh-cn.md)列出了图标设计的标准
-   [翻译FreeCAD](Localisation/zh-cn.md)
-   [附加Python模块](Extra_python_modules/zh-cn.md)，如何在FreeCAD里扩展Python功能
-   [谷歌代码之夏](Google_Summer_of_Code/zh-cn.md)，参与谷歌的学生支持计划


</div>

-   [Translating an external workbench](Translating_an_external_workbench.md)



### 模块开发者指南

[FreeCAD模块开发指南](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide)：这是一本在Github上写作的电子书。如要贡献，请fork然后发送pull request。

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



### 内部结构



### OpenCascade文档

OpenCascade是一个用于三维曲面和实体建模、CAD数据交换和可视化的软件开发平台，主要采用c++库的形式出现。

-   [Roman Lygin的教程](http://opencascade.wikidot.com/romansarticles)
-   [完整的在线文档](https://dev.opencascade.org/doc/overview/html/index.html)
-   [参考手册](https://dev.opencascade.org/doc/refman/html/index.html)
-   [OpenCascade维基百科](http://opencascade.wikidot.com)



#### 文件格式

[File Format FCStd](File_Format_FCStd.md). The files created with FreeCAD are `.zip` files that include the [BREP](https://en.wikipedia.org/wiki/Boundary_representation) geometry, as well as XML data that describes the document.



#### Sketcher求解器

-   [Sketcher Solver Architecture Booklet](https://forum.freecadweb.org/viewtopic.php?f=10&t=36355) (forum thread), [source](https://github.com/abdullahtahiriyo/FreeCADBooks/tree/master/FreeCAD_Solver_Architecture) in GitHub.
-   [PlaneGCS solver](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/) in the FreeCAD source code; important files are [GCS.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/GCS.cpp) and [SubSystem.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/SubSystem.cpp).
-   [Recent Several Sketcher improvements](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192).

The sketcher solver isn\'t perfect, as there are some issues with numerical precision when using large values, see [Adventure of fixing sketcher solver for large sketches](https://forum.freecadweb.org/viewtopic.php?f=10&t=40502).

The development of a new solver architecture could improve the way the solver is used both in the [Sketcher Workbench](Sketcher_Workbench.md), and for assembly of 3D bodies. See [Reimplementing constraint solver](https://forum.freecadweb.org/viewtopic.php?f=20&t=40525).



## 路线图

FreeCAD虽然在特定领域已经可用了，但是在跨入主流CAD的路途上，它才走了万里长征第一步。要登上与商业软件一争高下的平台，我们还有很多工作要做。

[FreeCAD 1.0 开发周期](FreeCAD_1.0_Development_Cycle.md)



## 社区

-   [IRC channel](ircs://irc.libera.chat:6697/freecad) ,和 [gitter channel](https://gitter.im/FreeCAD/FreeCAD)同步
-   [开发论坛](https://forum.freecad.org/viewforum.php?f=6)


<div class="mw-translate-fuzzy">

-   [开发路线图](Development_roadmap/zh-cn.md)


</div>


<div class="mw-translate-fuzzy">

## 信用

[贡献者](Contributors/zh-cn.md)


</div>



---
⏵ [documentation index](../README.md) > [Hubs](Category_Hubs.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Developer hub/zh-cn
