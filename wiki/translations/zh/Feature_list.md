# Feature list/zh
<div class="mw-translate-fuzzy">

这是FreeCAD实现的广泛但不完整的功能列表。如果您想展望未来，请参阅[开发路线图](Development_roadmap.md)，快速了解接下来会发生什么。此外，[截图集锦是一个不错的去处](Screenshots.md)。


</div>


{{TOCright}}



## 版本记录


<div class="mw-translate-fuzzy">

-   [0.11发布](Release_notes_0.11.md) - 2011年3月
-   [0.12发布](Release_notes_0.12.md) - 2011年12月
-   [0.13发布](Release_notes_0.13.md) - 2013年1月
-   [0.14发布](Release_notes_0.14.md) - 2014年3月
-   [0.15发布](Release_notes_0.15.md) - 2015年3月
-   [0.16发布](Release_notes_0.16.md) - 2016年4月
-   [0.17发布](Release_notes_0.17.md) - 2018年4月
-   [0.18发布](Release_notes_0.18.md) - 2019年3月
-   [0.19发布](Release_notes_0.19.md) - 2021年3月


</div>



## 关键特点


<div class="mw-translate-fuzzy">

-   ![](images/Feature1.jpg )完全基于[开源CASCADE技术](http://en.wikipedia.org/wiki/Open_CASCADE) 的**几何内核**，允许在复杂形状上进行复杂的3D操作，原生支持[边界表示法](https://en.wikipedia.org/wiki/Boundary_representation)（brep）、[非均匀有理B样条](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline)（nurbs）曲线和曲面、广泛的几何实体、布尔运算、[1](https://en.wikipedia.org/wiki/Fillet_(mechanics）倒圆角)，并且内建支持[STEP](https://en.wikipedia.org/wiki/ISO_10303)和[IGES](https://en.wikipedia.org/wiki/IGES)格式。
-   ![](images/Feature3.jpg )完全**参数化建模**。所有FreeCAD对象都是原生参数化的，这意味着它们的形状可以基于[属性](Property.md)，甚至基于其他对象。所有更改都会根据需要重新计算，并由撤消/重做堆栈记录。添加新对象类型非常容易，甚至可以[全部用python编程](Scripted_objects.md)。
-   ![](images/Feature4.jpg )**模块化架构**，允许向核心应用程序插入扩展（模块）以添加功能。扩展可以复杂地像完整地C++程序，也可以简单地像[Python脚本或录制的](Power_users_hub.md)[宏](macros.md)。您可以从内置的**Python**解释器，宏脚本或外部脚本中完全操作FreeCAD的任何部分，无论它是[几何体创建与变换](Topological_data_scripting.md)，几何的2D或3D显示（[场景图](scenegraph.md))还是[FreeCAD界面](PySide.md)。 
-   ![ left](images/Feature5.jpg )导入/导出，除了FreeCAD原生文件格式 **[FCStd](File_Format_FCStd.md)**之外还有一些**标准格式**，例如[STEP](http://en.wikipedia.org/wiki/ISO_10303)、[IGES](http://en.wikipedia.org/wiki/IGES)，[OBJ](http://en.wikipedia.org/wiki/Obj)、[STL](http://en.wikipedia.org/wiki/STL_%28file_format%29)、[DXF](http://en.wikipedia.org/wiki/Dxf)、[SVG](http://en.wikipedia.org/wiki/Svg)、[STL](http://en.wikipedia.org/wiki/STL_(file_format))、[DAE](http://en.wikipedia.org/wiki/COLLADA)、[IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes)或者[OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html)、[NASTRAN](http://en.wikipedia.org/wiki/NASTRAN),、[VRML](http://en.wikipedia.org/wiki/VRML)。 FreeCAD与给定文件格式之间的兼容程度可能会有所不同，因为它取决于实现它的模块。
-   ![ left](images/Feature7.jpg )具有集成约束求解器的[草图工作台](Sketcher_Workbench.md)，允许您绘制具有几何约束的2D形状。然后，使用草图工作台构建的受约束2D形状可用作构建FreeCAD中其他对象的基础。
-   ![ left](images/Feature9.jpg ) [机器人工仿真模块](Robot_Workbench.md)，可让您在图形环境中研究机器人的运动。
-   ![ left](images/Feature8.jpg )[技术制图模块](TechDraw_Workbench.md)，包含详细视图，横截面视图，尺寸标注等选项，允许您生成现有3D模型的2D视图。模块进一步可生成可导出的SVG或PDF文件。较旧的[绘图模块具有不多的的Gui命令](Drawing_Workbench.md)，但却有强大的Python功能。
-   ![ left](images/Feature-raytracing.jpg )一个[渲染模块](Raytracing_Workbench.md)，可以导出3D对象以便使用外部渲染器进行渲染。它目前仅支持[povray](http://en.wikipedia.org/wiki/POV-Ray)和[LuxRender](http://en.wikipedia.org/wiki/LuxRender)，但预计今后将扩展到其他渲染器。
-   ![ left](images/Feature-arch.jpg ) [建筑模块](Arch_Workbench.md)，可实现兼容[IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes)的[建筑信息模型](http://en.wikipedia.org/wiki/Building_Information_Modeling)（BIM）类似的工作流。
-   ![ left](images/Feature-CAM.jpg ) [刀路模块专门用于](Path_Workbench.md)[计算机辅助制造](https://en.wikipedia.org/wiki/Computer-aided_manufacturing)（CAM）。使用刀路模块，您可以输出，显示和调整用于控制目标机器的[G代码](http://en.wikipedia.org/wiki/G-code)。
-   ![ left](images/Feature_spreadsheet.png ) [集成电子表格和](Spreadsheet_Workbench.md)[表达式解析器](Expressions.md)，可用于驱动基于公式的模型创建并在集中的位置组织模型数据。 


</div>




<div class="mw-translate-fuzzy">

## 一般特点


</div>

-   **多平台支持**。 FreeCAD在Windows，Linux，macOS和其他平台上的运行并且功能完全相同。

-   **完整的图形用户界面(GUI)应用程序**。 FreeCAD有一个完整的基于[Qt](https://www.qt.io/)框架的图形用户界面，包含一个基于[Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor)的3D视图，能够快速渲染3D场景并且非常容易访问场景图呈现。

-   **作为命令行应用程序运行**。在命令行模式下，FreeCAD在没有其界面的情况下运行所有几何体工具。在此模式下，它具有相对较低的内存占用，并且可以用作如为其他应用程序生成内容的服务器。


<div class="mw-translate-fuzzy">

-   **可以作为[python模块被导入](Embedding_FreeCAD.md)。** FreeCAD可以被导入到任何其他可以运行python脚本的应用程序。与命令行模式一样，这时FreeCad的界面不可用，但所有几何工具都可以访问。


</div>


<div class="mw-translate-fuzzy">

-   **工作台概念**。在FreeCad界面中，工具按[工作台分组](workbenches.md)。这允许您只显示用于完成特定任务的工具，保持工作区整洁和且相应迅速，并允许应用程序快速加载。


</div>

-   **用于延迟加载功能/数据类型的插件/模块框架**。FreeCad被分为核心应用程序和只有在需要时才加载的模块。几乎所有工具和几何图形类型都存储在模块中。模块的作用类似于插件；除了延迟加载之外，还可以将单个模块添加到FreeCad的现有安装中或从中删除。

-   **以参数化形式关联文档对象**。FreeCad文档中的所有对象都可以通过参数定义。这些参数可以随时修改和重新计算。由于保持了对象关系，因此对一个对象的修改将自动传播到任何依赖它的对象。

-   **参数化创建基础元素**。可以通过指定其几何约束来创建基本对象，如长方体、球体、圆柱体等。


<div class="mw-translate-fuzzy">

-   **图形修改操作**。Freecad可以在三维空间的任何平面执行平移、旋转、缩放、镜像、偏移（甚至更细小的或如[jung/shin/choi](https://www.researchgate.net/publication/240754626-self-intersection-removal-in-triangular-mesh-offseting)所述的操作）或形状转换。


</div>

-   **[构造实体几何](Constructive_solid_geometry.md)（布尔运算）**。Freecad可以进行构造实体几何模型操作（联合、差分、相交）。


<div class="mw-translate-fuzzy">

-   **平面几何的图形创建**。 可以在3D空间的任何平面中以图形方式创建线，线，矩形，b样条和圆形或椭圆弧。


</div>

-   **直线或选择建模** **拉伸**, **截面**和**倒角**.

-   **拓扑组件**类似于**顶点**、**边**、**线**和**平面**。


<div class="mw-translate-fuzzy">

-   **测试和修复**。 FreeCAD具有测试网格（实体测试，非双流形测试，自相交测试）和修复网格（孔填充，均匀定向）的工具。


</div>


<div class="mw-translate-fuzzy">

-   **注释**。 FreeCAD可以插入文本或尺寸注释。


</div>

-   **撤消/重做框架**。 FreeCAD中的所有操作都是撤消/可重做的，用户可以访问撤消堆栈。可以一次撤消多个步骤。

-   **面向事务处理**。撤消/重做堆栈存储的是文档事务，而不是单个操作，它允许每个工具准确定义必须撤消或重做的内容。

-   **内置[脚本框架](Scripting.md)**。Freecad具有内置的[Python](http://www.python.org/)解释器，其API几乎涵盖了应用程序的任何部分,接口、几何图形以及3D查看器中该几何图形的表示。解释器可以运行复杂的脚本和单个命令；整个模块可以完全用Python编程来开发。


<div class="mw-translate-fuzzy">

-   **内置python控制台**。python解释器包括一个带有语法高亮显示、自动补齐和类浏览器的控制台。python命令可以直接在freecad中发出，并立即返回结果。它允许脚本编写人员动态测试功能，探索freecad模块的内容，并轻松了解freecad内部。


</div>


<div class="mw-translate-fuzzy">

-   **镜像用户交互**。用户在FreeCAD界面中所做的一切都会执行Python代码，这些代码可以在控制台上打印并记录在宏中脚本。


</div>

-   **完整的[宏记录和编辑](Macros.md)**功能。当用户操作界面时发出的python命令可以被记录、编辑（如果需要），并保存以备日后复制。


<div class="mw-translate-fuzzy">

-   *复合（基于zip）文档保存格式*。FreeCad文档以**.[FCStd](File_Format_FCStd.md)** 扩展名的形式保存。文档可以包含许多不同类型的信息，如几何图形、脚本或缩略图图标。 **.FCStd** 文件本身就是一个zip容器；已保存的freecad文件已被压缩。


</div>

-   **完全可自定义/脚本化的图形用户界面**。FreeCad基于 [Qt](https://www.qt.io)的界面完全可以通过python解释器访问。除了FreeCad本身为工作台提供的简单功能外，整个Qt框架是可访问的。用户可以在GUI上执行任何操作，例如创建、添加、停靠、修改或删除小部件和工具栏。

-   **缩略图**. （目前只有在Linux系统中可用）在大多数文件管理器应用程序（如GNOME的Nautilus）中Freecad文档图标显示文件的内容。


<div class="mw-translate-fuzzy">

-   **模块化MSI安装程序**。FreeCad的安装程序可以被灵活地安装在Windows系统上。Ubuntu系统的软件包一直在维护。


</div>

## Extra Workbenches 


<div class="mw-translate-fuzzy">

## 补充功能工作台

超级用户创建了各种自定义[外部工作台](external_workbenches.md)。


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Feature list/zh
