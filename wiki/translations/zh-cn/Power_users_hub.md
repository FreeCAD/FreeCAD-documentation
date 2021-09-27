# <img alt="" src=images/Power_user_hub.png  style="width:64px;"> Power users hub/zh-cn

------------------------------------------------------------------------




<div class="mw-translate-fuzzy">

如果你想深入理解FreeCAD，这里就是你该来的地方。你能学到如何为你的需求定制FreeCAD。


</div>


<div class="mw-translate-fuzzy">

FreeCAD最秒的好处之一，就是它给你的灵活性。你不需要作任何编译，不需要接触源代码，就可以写脚本，就可以作扩展，可触范围极广。所有的脚本都用[Python](http://en.wikipedia.org/wiki/Python_(programming_language))完成。它是一门强大而简洁的编程语言。有了简洁的Python脚本，你有权触及FreeCAD的任何部分。比如说，你可以：

-   **创建和修改几何体**：有没有这种情况？你需要的特殊对象，没有出现在FreeCAD的默认安装包里？你可以轻松创建一个新对象类型，既可以写脚本，也可以调配一个已有的类型。
-   **创建定制的工具和命令**：目前，FreeCAD已经有了很广泛的功能，但是给终端用户的工具和命令还不是很多。不过，你已经可以很容易地创建自己的工具包了。
-   **修改界面**：FreeCAD的用户界面还处于十分基础的阶段。但是如果你要有所扩展，工具都给你准备好了。比如说，你可以创建一个工具条，把你的工具都放进去；你也可以创建一个特殊面板，用来与你的工具互动，诸如此类。
-   **修改场景表现**：建立和计算几何体，在屏幕上显示那个几何体，这件事在FreeCAD里有不同的流程来处理。场景元素显示在屏幕上的方式，你对此有完全控制权。所以，你可以修改那个表现，与它交互，或者加入各种各样的定制行为和屏幕组件。举几个例子，信息、拖拽、锚定或者暂时实体。


</div>


<div class="mw-translate-fuzzy">

这些页面还远没有成熟。如果你没找到你要找的信息，或者你在别的地方发现了有用的信息，而我们没有链接在这里，那为什么不[自己添加进来](Help_FreeCAD.md)？同时，请在[论坛](http://forum.freecadweb.org/)留下你的意见。


</div>

## 定制FreeCAD


<div class="mw-translate-fuzzy">

-   [界面定制](Interface_Customization.md): 从头开始：工具栏和快捷方式
-   [用宏工作](Macros.md): 轻松录制多遍任务或Python代码
-   [宏菜单](Macros_recipes.md)
-   [定制工具栏](Customize_Toolbars.md)
-   [安装更多工作台](Installing_more_workbenches.md)
-   [插件装载器](http://forum.freecadweb.org/viewtopic.php?t=10556)
-   [Addons installer.FCMacro](https://github.com/FreeCAD/FreeCAD-addons)


</div>

## 在FreeCAD里写脚本

### General


<div class="mw-translate-fuzzy">

### 通则

-   [ 介绍Python](Introduction_to_Python.md) - 在页面底端还有其他Python教程。
-   [FreeCAD脚本教程](Python_scripting_tutorial.md) - 概略看一下在FreeCAD中用Python写脚本。
-   [FreeCAD脚本基础](FreeCAD_Scripting_Basics.md) - 好吧，基本的东西......
-   [Gui命令](Gui_Command.md) - 向GUI添加定制的命令。
-   在FreeCAD里使用混合[单位](Units.md)。


</div>

### 模块


<div class="mw-translate-fuzzy">

在FreeCAD中，功能性的东西被划分到各个模块，处理特定的数据类型和应用。FreeCAD有内建模块和扩展模块（插件）。插件模块一旦安装，它们就和内建模块一样方便触达。下面讲的是默认模块，FreeCAD的每一个安装包都包含了。


</div>


<div class="mw-translate-fuzzy">

-   [内建模块是FreeCAD的主体模块](Builtin_modules.md)。里面的工具，可以调整FreeCAD的一般配置、文档和内容。
-   [创建工作台展示给你如何创建自己的工作台](Workbench_creation.md)。


</div>

#### Working with Meshes 


<div class="mw-translate-fuzzy">

### 网格类工作

-   [网格脚本](Mesh_Scripting.md)：怎样与[网格模块交互](Mesh_Workbench.md)。


</div>

#### Working with Parts 


<div class="mw-translate-fuzzy">

### 零件类工作

-   [零件模块](Part_Workbench.md)：[开源CASCADE技术](http://en.wikipedia.org/wiki/Open_CASCADE)的工具和体系如何用在FreeCAD中。
-   [拓扑数据脚本](Topological_data_scripting.md)：怎样与零件模块交互。
-   [PythonOCC](PythonOCC.md)：怎样释放开源CASCADE的全部能量。
-   [网格到零件](Mesh_to_Part.md)：转换对象类型。


</div>

#### Accessing the Coin scenegraph 


<div class="mw-translate-fuzzy">

### 触达Coin的场景图

-   [Coin/Inventor的场景图](Scenegraph.md)：FreeCAD的场景表现如何运作。
-   [Pivy](Pivy.md)：如何触达和变更场景图。


</div>

### Controlling the Qt interface 


<div class="mw-translate-fuzzy">

### 控制Qt接口

-   [PySide](PySide.md)：如何触达接口，并修改它的内容。
-   在另一个Qt应用里，通过PyQt，来[使用FreeCAD的GUI](Embedding_FreeCADGui.md)。


</div>


<div class="mw-translate-fuzzy">

### 参数对象类工作

-   [脚本化的对象](Scripted_objects.md)：在FreeCAD里如何制作100%的Python脚本化的对象。
-   [制图模块](Drawing_Workbench.md)：让3D到2D的过程实现自动化。


</div>

-   [Scripted objects](Scripted_objects.md): how to make 100% Python-scripted objects.
    -   [Scripted objects with attachment](Scripted_objects_with_attachment.md): how to make scripted objects attachable to other objects.
    -   [Scripted objects saving attributes](Scripted_objects_saving_attributes.md): how to save and restore attributes of the proxy class with `__getstate__` and `__setstate__`.
    -   [Scripted objects migration](Scripted_objects_migration.md): how to migrate old scripted objects to a new class.

### Examples


<div class="mw-translate-fuzzy">

### 例子

-   [代码片段](Code_snippets.md)：搜集了一些FreeCAD的Python代码段，作为你的脚本的配料......
-   [画线函数](Line_drawing_function.md)：如何建造一个简单工具，来画线。
-   [创建对话](Dialog_creation.md)：如何用Qt设计器来建造对话框，把它们用在FreeCAD里。
-   [嵌入式FreeCAD](Embedding_FreeCAD.md)：在其他应用里，如何载入FreeCAD，作为一个Python模块。
-   [绘图模块为FreeCAD加入了](Draft_Workbench.md)2D绘图函数。它整个都是用Python写的，所以如果你想写自己的模块，它就是个好例子。
-   [FreeCAD向量数学程序库](FreeCAD_vector_math_library.md)：几个很顺手的函数，来操控FreeCAD的向量。这个函数库也包含在绘图模块里面了。


</div>

## API函数

FreeCAD完整的API文档放在http://www.freecadweb.org/api/中。它既有C++也有Python的API，还没有完全格式化好。当你想找只含Python的代码，就会发现那里有点乱。更便于浏览的版本在_。注意，它可能并不完整，因为它得用人工更新。要找更精确信息的话，直接在FreeCAD的Python控制台里浏览相应模块吧。

Related: [Exposing C++ to Python](Exposing_C%2B%2B_to_Python.md)

## 高级修改


<div class="mw-translate-fuzzy">

-   [启动和配置](Start_up_and_Configuration.md)：启动和命令行选项。
-   [在Windows上安装](Install_on_Windows.md)：使用Windows安装器。
-   [在Windows上编译FreeCAD](CompileOnWindows.md)，[在Unix上编译FreeCAD](CompileOnUnix.md)
-   [品牌化](Branding.md)：简单变更FreeCAD的源代码，改变FreeCAD的一些方面。
-   [额外的Python模块](Extra_python_modules.md)：用这些强大的模块，来扩展FreeCAD的Python解释器。


</div>

## Python教程

这些是通用教程，都很棒。它们不是特殊为FreeCAD制作的，如果你完全没接触过Python，它们可能对你有益处。


<div class="mw-translate-fuzzy">

**Python**

-   [官方Python2.7教程](https://docs.python.org/2.7/tutorial/index.html) - 发现Python之旅的完全指南。
-   [非程序员的Python教程](http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python) - 超赞的维基书。
-   [为新手写的Python](http://npt.cc.rsu.ru/user/wanderer/ODP/Python_for_Newbies.htm) - 一本大型指南，涵盖了方方面面的基础内容。


</div>

**PySide** - 怎样通过Python创建和管理FreeCAD的Qt用户交互界面。

-   [PySide教程](http://zetcode.com/gui/pysidetutorial/)：一个平台不可知论者的教程，通过很多例子，展示PySide的用法。
-   [PySide/PyQt教程](http://www.pythoncentral.io/series/python-pyside-pyqt-tutorial/)：一个PySide和PyQt教程，很容易读，有例子。
-   [PySide文档](http://qt-project.org/wiki/PySideDocumentation)：来自于Qt项目（全部都是那些人写的）。
-   [在PySide里使用QtCreator](http://qt-project.org/wiki/QtCreator_and_PySide)：也是来自于Qt项目。
-   [PySide参考](http://srinikom.github.io/pyside-docs/index.html)：无微不至地详解PySide和Qt的各种小细节，一个可靠的参考源。
-   [PySide代码片段](http://nullege.com/codes/search?cq=PySide)：一个可以搜索的PySide代码片段数据库。


<div class="mw-translate-fuzzy">

下面两个参考源，是PyQt特定的（不是PySide），但它们可能给了一些有用的信息：

-   [基础PyQt教程](http://www.cs.usfca.edu/~afedosov/qttut/)：一个基于Linux的简短教程，解释了怎样使用PyQt和Qt Designer。
-   [用Python编程Qt应用](http://vizzzion.org/?id=pyqt)：一个更深入的教程，涵盖了用Qt和Python工作的所有方面。


</div>


<div class="mw-translate-fuzzy">

**Pivy** - 怎样与FreeCAD的3D场景交互

-   [基础Pivy教程](http://pivy.coin3d.org/documentation/pycon)：来自官方Pivy站点，非常简单的教程。
-   [介绍Pivy给studierstube](http://www.google.com.br/url?sa=U&start=3&q=http://studierstube.icg.tu-graz.ac.at/doc/pdf/PivyStudierstubeTutorial.pdf&ei=XyC1Sc2wOeCKmQem_eHnBQ&usg=AFQjCNEYhb-0DcUc6OxFVijAe1epBb-4aA)：这份文档算不上是教程，但是它很好地展示了Pivy是怎样工作的。


</div>

## 社区项目


<div class="mw-translate-fuzzy">

在[社区入口](FreeCAD_Community_Portal.md)，你会找到其它基于FreeCAD的项目，它们由FreeCAD用户社区运行。如果你正开始一个新的FreeCAD项目，一定要登记上去。如果你愿意[帮助FreeCAD](Help_FreeCAD.md)，我们也准备了那个页面，列出了你可以做的事情。


</div>

-   [Scientific literature](Scientific_literature.md): articles that reference or use the FreeCAD system in different ways.


{{Powerdocnavi

}}

_

---
[documentation index](../README.md) > [Hubs](Category_Hubs.md) > Power users hub/zh-cn
