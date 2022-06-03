# Feature list/zh-cn
<div class="mw-translate-fuzzy">

这是一个庞大的，未完成的 FreeCAD 特性列表。如果你想知道未来规划，可以通过 [开发路线图](Development_roadmap/zh-cn.md) 大概知道接下来有什么新特性。同样，[截图](Screenshots/zh-cn.md) 也是一个好地方值得浏览。


</div>


{{TOCright}}

## 版本说明


<div class="mw-translate-fuzzy">

-   [版本 0.11](Release_notes_0.11/zh-cn.md) - 2011 三月
-   [版本 0.12](Release_notes_0.12/zh-cn.md) - 2011 十二月
-   [版本 0.13](Release_notes_0.13/zh-cn.md) - 2013 一月
-   [版本 0.14](Release_notes_0.14/zh-cn.md) - 2014 三月
-   [版本 0.15](Release_notes_0.15/zh-cn.md) - 2015 三月
-   [版本 0.16](Release_notes_0.16/zh-cn.md) - 2016 四月


</div>

## 关键特性


<div class="mw-translate-fuzzy">

-   ![](images/Feature1.jpg ) 一个完全基于 [Open CASCADE Technology](http   *//en.wikipedia.org/wiki/Open_CASCADE) 的 **几何内核 (geometry kernel)** 允许在复杂的形状类型上执行复杂的 3D 操作，原生支持这些概念：多重曲面 (brep)、非均匀有理B样条 (nurbs curves) 和 曲面 (surfaces)，大量几何实体 (geometric entities)，布尔操作 (boolean operations) 和圆角 (fillets) 和内建支持 STEP 和 IGES 格式 
-   ![](images/Feature3.jpg ) 一个全 **参数化模型 (parametric model)**。所有 FreeCAD 对象是本地原生参数化，意味着他们的形状能基于 [属性](Property/zh-cn.md) 变化 或者 甚至依赖于其它的对象，所有改变在需要时会被自动重新计算，而且由 撤消/重做 栈记录其操作。很容易增加新对象类型，甚至 [全部用 Python 进行编程](Scripted_objects.md)
-   ![](images/Feature4.jpg ) **模块化设计** 允许插件 (模块) 添加功能到核心应用程序中。那些扩展能跟用 C++ 编写整个新应用程度一样复杂或者跟 [Python 脚本](Power_users_hub.md) 一样简单 或者 自己录制 [macros](macros.md)。你能从内建的 **Python** 解释器中完全访问从宏或者外部脚本到 FreeCAD 几乎任何部分，进行 [几何对象创建或变换](Topological_data_scripting/zh-cn.md), 展示几何对象 ([scenegraph](scenegraph.md)) 的 2D 或者 3D 图形甚至控制 [FreeCAD 界面](PySide.md) 
-   ![](images/Feature5.jpg ) 导入/导出到 **标准格式**，例如：[STEP](http   *//en.wikipedia.org/wiki/ISO_10303), [IGES](http   *//en.wikipedia.org/wiki/IGES), [OBJ](http   *//en.wikipedia.org/wiki/Obj), [STL](http   *//en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http   *//en.wikipedia.org/wiki/Dxf), [SVG](http   *//en.wikipedia.org/wiki/Svg), [STL](http   *//en.wikipedia.org/wiki/STL_(file_format)), [DAE](http   *//en.wikipedia.org/wiki/COLLADA), [IFC](http   *//en.wikipedia.org/wiki/Industry_Foundation_Classes) or [OFF](http   *//people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http   *//en.wikipedia.org/wiki/NASTRAN), [VRML](http   *//en.wikipedia.org/wiki/VRML)，另外还有 FreeCAD 的原生 [Fcstd 文件格式](File_Format_FCStd/zh-cn.md). FreeCAD 对每种文件格式的兼容性支持级别有所不同，因为它依赖于实现读写的模块。
-   ![](images/Feature7.jpg ) 一个 [素描器](Sketcher_Workbench/zh-cn.md) 和 约束求解程序，允许勾画几何约束的 2D 图形。目前素描器允许你构建几种几何约束对象，并且利用它们在整个 FreeCAD 中作为构建其它对象的基础。
-   ![](images/Feature9.jpg ) 一个 [机器人模拟](Robot_Workbench/zh-cn.md) 模块用于学习机器人移动行为。这个机器人模块已经有一个扩展的图像界面允许仅限界面的工作流程。
-   ![](images/Feature8.jpg ) 一个 [绘制工作表](Drawing_Workbench/zh-cn.md) 模块允许放置 3D 模型的 2D 视图到一张工作表上。此模块会产生可导出的 SVG 或 PDF 工作表。此模块虽然功能稀少，但此特性已经能增加一个强大的功能到 Python。
-   ![](images/Feature-raytracing.jpg ) 一个 [渲染](Raytracing_Workbench/zh-cn.md) 模块能导出 3D 对象用于外部渲染。当前仅支持 [povray](http   *//en.wikipedia.org/wiki/POV-Ray) 和 [LuxRender](http   *//en.wikipedia.org/wiki/LuxRender), 但期待未来支持其它的渲染器.
-   ![](images/Feature-arch.jpg ) 一个 [建筑学](Arch_Workbench/zh-cn.md) 模块支持类似[BIM](http   *//en.wikipedia.org/wiki/Building_Information_Modeling) 工作流, 与 [IFC](http   *//en.wikipedia.org/wiki/Industry_Foundation_Classes) 兼容.
-   ![](images/Feature-CAM.jpg ) [路径模块](Path_Workbench/zh-cn.md) 专注于机械机器类似 研磨机 (milling, CAM), 并能输出、显示和修改 [G code](http   *//en.wikipedia.org/wiki/G-code).


</div>


<div class="mw-translate-fuzzy">

## 一般特性   *


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD 是跨平台的**. 它在 Windows、Linux 和 macOS 平台上运行和表现完全一致.


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD 是一个全界面应用程序**. FreeCAD 有一个基于著名的 [Qt](http   *//www.qtsoftware.com/) 框架的完整用户界面，和一个基于[Open Inventor](http   *//en.wikipedia.org/wiki/Open_Inventor) 的 3D 查看器，允许快速渲染 3D 场景和一个非常容易理解的场景图形显示。


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD 也能作为命令行程序运行**，使用更低的内存占用。在命令行模式运行时，FreeCAD 没有界面，但拥有所有的几何工具。它能做的事，例如：作为一个服务器为其它应用程序生产内容。


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD 能以 [Python 模块](Embedding_FreeCAD/zh-cn.md)** 形式导入到其它能运行 Python 脚本的应用程序中或在 Python 控制台中。就像在控制台模式，FreeCAD 的界面部分是不可用的，但所有几何工具都可访问。


</div>


<div class="mw-translate-fuzzy">

-   **工作台概念**：在 FreeCAD 界面里，工具由 [工作台](workbenches/zh-cn.md) 进行分组。这样子界面上仅仅显示与完成任务相关的工具组，保持工作区的整洁和响应速度，并且应用程序可以以更快速度加载。


</div>


<div class="mw-translate-fuzzy">

-   **延迟加载 特性/数据类型 的 插件/模块 框架**。FreeCAD 被分为核心应用程序及模块，模块仅在需要时才会被加载。几乎所有工具和几何类型均被存储在模块中。模块类似于插件，并且能从一个已安装的 FreeCAD 中增加或删除。


</div>


<div class="mw-translate-fuzzy">

-   **参数关联的文档对象**：FreeCAD 文档中的所有对象都可以使用参数定义。参数可以随时变动和计算。对象间的关系也会被存储，所以当修改一个对象时，也会同时修改所有依赖它的对象。


</div>


<div class="mw-translate-fuzzy">

-   **参数化原型创建** (长方体、球体、 圆柱体、等等)


</div>


<div class="mw-translate-fuzzy">

-   图像 **修改操作** 在 3D 空间的任意平面进行类似变换、旋转、缩放、镜像、位移（萃取或者[Jung/Shin/Choi](https   *//www.researchgate.net/publication/240754626_Self-intersection_Removal_in_Triangular_Mesh_Offsetting)）或者形状转换。


</div>


<div class="mw-translate-fuzzy">

-   **[布尔操作](http   *//en.wikipedia.org/wiki/Constructive_solid_geometry)** (相并、相差、相交)


</div>


<div class="mw-translate-fuzzy">

-   在 3D 空间的任意平面创建 **简单平面几何** 图形，类似 线、曲线、矩形、弧形、圆形。


</div>


<div class="mw-translate-fuzzy">

-   直线和旋转建模 **拉伸**，**截面** 和 **圆角**。


</div>


<div class="mw-translate-fuzzy">

-   拓扑组件像 **顶点, 边, 曲线** 和 **平面** (通过 Python 脚本)。


</div>


<div class="mw-translate-fuzzy">

-   **测试和修复**网格工具：可靠性测试，非流形测试，自相交测试，孔填充和统一方向。


</div>


<div class="mw-translate-fuzzy">

-   **注解** 就像文字或者尺寸


</div>


<div class="mw-translate-fuzzy">

-   **撤消/重做 框架**   * 任何事情都能被撤消/重做，在撤消栈中，多个步骤能被一次性撤消。


</div>


<div class="mw-translate-fuzzy">

-   **事务管理**   * 撤消/重做栈存储文档事务而不是单一的行为，允许每个工具精确定义什么能被撤消或者重做。


</div>


<div class="mw-translate-fuzzy">

-   **内建[脚本框架](Scripting/zh-cn.md)**   * FreeCAD 内建 [Python](http   *//www.python.org/) 脚本解释器和几乎覆盖整个应用程序，接口，几何和显示 3D 视图的 API。解释器可以单独运行复杂的脚本。实际上，整个模块都可以使用 Python 编程。


</div>


<div class="mw-translate-fuzzy">

-   **内建 Python 终端** 语法高亮，自动补全，类浏览：Python 命令可以直接在 FreeCAD 中发出，并立即返回结果，允许脚本编写者快速测试功能，浏览其内容的模块，方便了解 FreeCAD 内部。


</div>


<div class="mw-translate-fuzzy">

-   **用户和终端交互**   * 所有用户的 FreeCAD 的操作都执行了 python 代码。这些代码都可以在终端中打印出来和记录为宏。


</div>


<div class="mw-translate-fuzzy">

-   **完全的记录和编辑宏**   * 当用户操作时发出 python 命令，这些命令都可以记录，编辑和保存。


</div>


<div class="mw-translate-fuzzy">

-   **(ZIP压缩的)文件保存格式**   * FreeCAD 文档以 .[fcstd](File_Format_FCStd/zh-cn.md) 为扩展名，可以包含多种信息类型，如几何形状信息，脚本以及缩略图图标。这个 .fcstd 文件本身是 ZIP 文档，所以 FreeCAD 文件已经被压缩了。


</div>


<div class="mw-translate-fuzzy">

-   **完全个性化／脚本化的图形界面**。基于 [Qt](http   *//www.qtsoftware.com) 的 FreeCAD 的界面完全可以使用 Python 解释器调用。不但 FreeCAD 自己提供的 workbench 函数可以用 Python 调用，Qt 的界面部分也可以调用，例如创建，添加，修改，删除小工具和工具栏。


</div>


<div class="mw-translate-fuzzy">

-   **缩略图** (当前仅 Linux 系统版本有)   * FreeCAD 文档的图标可以在大多数文档管理器中显示文档的缩略图，例如 Gnome 的 Nautilus。


</div>


<div class="mw-translate-fuzzy">

-   **MSI 安装器** 可以方便 Windows 系统安装 FreeCAD。 Ubuntu 系统上的包也在维护中。


</div>

## Extra Workbenches 


<div class="mw-translate-fuzzy">

## 额外的工作台

高级用户们已经创建了大量的自定义 [外部工作台](external_workbenches/zh-cn.md).


</div>


<div class="mw-translate-fuzzy">


{{docnav|About FreeCAD/zh-cn|Install on Windows/zh-cn}}


</div>




[Category   *User Documentation](Category_User_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Feature list/zh-cn
