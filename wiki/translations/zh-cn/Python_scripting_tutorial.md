# Python scripting tutorial/zh-cn
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

[Python](http://en.wikipedia.org/wiki/Python_%28programming_language%29)是一门非常简单易学的编程语言。它集开源、多平台于一身，且可以摆脱其他各种工具独立使用，借助简单的shell脚本编程即可实现非常复杂的程序。但是其最广泛的用处是作为一种脚本语言，因为它易于嵌入其他的应用之中。这便是在FreeCAD中用这种语言的原因。您可以通过python控制台或自定义脚本的方式来使用FreeCAD，这也是在非图形用户界面工具下执行非常复杂动作的方法。


</div>


<div class="mw-translate-fuzzy">

例如，通过python脚本您可以：

-   创建新的对象
-   修改已存在的对象
-   修改那些对象的3D表示
-   修改FreeCAD接口


</div>


<div class="mw-translate-fuzzy">

在FreeCAD中有以下几种使用python的不同方式：

-   在[FreeCAD的python解释器中使用脚本](FreeCAD_Scripting_Basics.md)。在此，您可以通过类似于"命令行"样式的界面来发出简单的命令
-   在[宏中使用脚本](macros.md)。这是一种将缺失的工具快速添加至FreeCAD界面的便捷方法
-   借助外部脚本。这可用来编写更复杂的程序。比如编写整个[工作台](Workbenches.md)。


</div>


<div class="mw-translate-fuzzy">

在本教程中，我们将通过若干简单的示例来令您入门，除此之外，本wiki中还存在更多[关于python脚本的文档](Power_users_hub.md)。如果您是一位python新手，希望理解它的工作原理，我们也为您提供了较为基础的[Python简介](introduction_to_Python.md)。


</div>


<div class="mw-translate-fuzzy">

**重要提示!** 在用Python脚本进行处理之前，前往**Edit → Prefences → General → Output**窗口并选中两个选择框：

-   Redirect internal Python output to report view
-   Redirect internal Python errors to report view

再去往**View → Panels**并选中：

-   Report view

这将把您从大量恼人的事情之中解救出来！


</div>


<div class="mw-translate-fuzzy">

## 编写python代码

FreeCAD提供了两种环境供用户方便地编写python代码：python控制台(可从View → Panels → Python console菜单开启)或宏编辑器(Tools → Macros)。在控制台中，您可以逐行地编写python命令，按下回车键后即刻执行。而宏中则可容纳更复杂的多行脚本，只有在执行宏时才会执行相应代码。


</div>

There are two ways to write Python code in FreeCAD. In the [Python console](Python_console.md) (select **View → Panels → Python console** from the menu) or in the [Macro editor](Std_DlgMacroExecute.md) (select **Macro → Macros...** from the menu). In the console you write Python commands one by one, executing them by pressing **Enter**, while macros can contain more complex code made up of several lines, executed only when the macro is executed.

![](images/Screenshot_pythoninterpreter.jpg )


<div class="mw-translate-fuzzy">

![FreeCAD的python控制台](images/Screenshot_pythoninterpreter.jpg )


</div>


<div class="mw-translate-fuzzy">

在此教程中，您可以使用下列两种方式编辑代码：通过在python控制台中单行复制/粘贴代码并按下**回车键**来逐行执行，或在新的宏窗口中复制/粘贴全部代码一次性执行。


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

## 探索FreeCAD

让我们首先来创建一个新的空文档：


</div>

Let\'s start by creating a new empty document:


```python
doc = FreeCAD.newDocument()
```


<div class="mw-translate-fuzzy">

如果您在FreeCAD的python控制台中输入这些内容，会发现仅需敲入"FreeCAD."就会弹出一个窗口，让您快速地自动补齐剩下的代码。更强大的是，自动补齐列表中的每一项都有对应的工具提示来解释其具体使用细节。这便于用户更轻松地浏览可用的各种函数功能。在选择\"newDocument\"之前，您可以顺便查看其它存在的可选项。


</div>

![](images/Screenshot_classbrowser.jpg )


<div class="mw-translate-fuzzy">

![FreeCAD中python控制台的自动补全机制](images/Screenshot_classbrowser.jpg )


</div>


<div class="mw-translate-fuzzy">

现在我们就会创建一个新文档。这就类似于按下工具栏上的\"new document\"按钮。事实上，FreeCAD中的大部分按钮实现的功能也就相当于执行一、两行python代码。更妙的是，您可以通过设置**Edit → Preferences → General → Macro**中的\"show script commands in python console\"选项，在控制台中查看按下每个按钮时所执行的python代码。这对于学习如何用python复现FreeCAD的各种动作是极为有益的。


</div>


<div class="mw-translate-fuzzy">

现在我们把视线重归文档本身。来看看可以对它进行哪些操作：


</div>


```python
doc.
```


<div class="mw-translate-fuzzy">

借此即可阅览各种与文档有关的可选项。通常以大写字母开头为名的是属性，而已小写字母开头的是函数（或称方法），函数会执行"某些操作"。以一个下划线开头的名称通常为模块的内部函数，无需在上面花太多心思。现在，让我们来使用特定方法为刚刚新建的文档添加一个新对象：


</div>


```python
box = doc.addObject("Part::Box", "myBox")
```


<div class="mw-translate-fuzzy">

什么都没有发生。喂神马？这其实是FreeCAD为整体大局而定的策略。在一天里，它将处理数百复杂的对象，而所有的对象又彼此依赖。仅做出一点儿小的改动就可能牵一发而动全身，您也许只想对整个文档重新计算一次，但可能却需要花费很长的时间......出于这个原因，基本上没有任何命令会自动更新场景。因此，您必须手动来实现这件事：


</div>


```python
doc.recompute()
```


<div class="mw-translate-fuzzy">

看到了吗？我们创建的立方体现在粗线惹！FreeCAD中用于添加对象的大多按钮实际上都做了两件事：添加对象，并重新进行计算。如果您按前文所述开启了\"show script commands in python console\"选项，并试着用GUI按钮添加一个球体，您将看到也执行了上述python代码。


</div>

现在让我们来查阅一下所创立方体的有关信息：


```python
box.
```

您将立刻看到一些有趣的东西，例如：


```python
box.Height
```

这将打印当前所创立方体的高度。现在，让我们来尝试更改此属性：


```python
box.Height = 5
```


<div class="mw-translate-fuzzy">

如果用鼠标选中此立方体，您将在属性面板-\>"Data"选项卡-\>"Height"属性中看到此数据。FreeCAD对象的所有属性都将呈现于此(以及后面要提到的\"View\"选项卡中的属性)，利用属性名（例如前面的属性\"Height\"）通过python也可直接访问它们。请尝试改变此立方体的其他规格。


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

## 向量与方位

[向量](http://en.wikipedia.org/wiki/Euclidean_vector)是任何3D应用中最基础的一个概念。它由三个数值构成(x、y与z)，用于描述3D空间中的一个点或一个位置。向量可参与大量不同种类的运算，如加法、减法、投影[等等等等](http://en.wikipedia.org/wiki/Vector_space)。在FreeCAD中，是这样运用向量的：


</div>

[Vectors](https://en.wikipedia.org/wiki/Euclidean_vector) are a very fundamental concept in any 3D application. A vector is a list of 3 numbers (x, y and z), describing a point or position in 3D space. Many things can be done with vectors, such as additions, subtractions, projections and [much more](https://en.wikipedia.org/wiki/Vector_space). In FreeCAD vectors work like this:


```python
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```


<div class="mw-translate-fuzzy">

FreeCAD对象的另一常用特性为它们的 [方位（placement）](Placement.md)。每个对象都有一个方位属性，其中包括了相应对象的位置(基)与方向(旋转)。此属性易于操控，例如让我们来移动所创立方体：


</div>


```python
box.Placement
box.Placement.Base
box.Placement.Base = sumvec
 
otherpla = FreeCAD.Placement()
box.Placement = otherpla
```

现在，在我们进一步讨论之前，您一定了解了上述重要概念。

[top](#top.md)


<div class="mw-translate-fuzzy">

## App 与 Gui 

FreeCAD最开始是一种命令行应用程序，并不具有当前形式的用户接口。因此，其中大多东西都可被划分为\"几何\" 组件与\"可视\"组件。当您在命令行模式下工作时，展示的是几何部分，而把全部可视部分简单地关掉。因此，FreeCAD中的几乎所有对象都由两部分组成：一个Object以及一个ViewObject。


</div>

FreeCAD has been designed so that it can also be used without its user interface, as a command-line application. Almost every object in FreeCAD therefore consists of two parts: an `Object`, its \"geometry\" component, and a `ViewObject`, its \"visual\" component. When you work in command-line mode, the geometry part is present, but the visual part is disabled.


<div class="mw-translate-fuzzy">

为了详述此概念，再来看我们的立方体对象，它的几何属性，如规格、位置等等都存于object中，而它的可视属性，如颜色、线宽等等都存于viewobject中。这两样属性集就对应于属性窗口中的\"Data\"与\"View\"选项卡。对象的viewobject属性可这样来访问：


</div>


```python
vo = box.ViewObject
```


<div class="mw-translate-fuzzy">

现在，您就可以更改\"View\"选项卡中的属性：


</div>


```python
vo.Transparency = 80
vo.hide()
vo.show()
```


<div class="mw-translate-fuzzy">

当您开启FreeCAD时，python控制台已加载了2个基础模块：FreeCAD 与 FreeCADGui (也可从它们的快捷方式App 与 Gui进行访问)。此二者内含文档及其对象工作时所需的一切通用功能。为了阐明这些概念，我们来看FreeCAD 与 FreeCADGui均包括的ActiveDocument属性，它便是当前打开的文档。FreeCAD.ActiveDocument与 FreeCADGui.ActiveDocument并不是同一对象。它们是FreeCAD文档的两种组件，并且其中各有不同的属性与方法。举个栗子，FreeCADGui.ActiveDocument中有ActiveView，这是当前打开的3D视图。而FreeCAD.ActiveDocument中却没有这一项。


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

## 模块

现在，您一定在想，若没有\"Part::Box\"我还能做什么呢？FreeCAD的基本应用程序或多或少来只讲是一个空容器。若没有它的各种模块，充其量也就只能创建新的空文档而已。令FreeCAD真正强大的其实是其各种可靠的模块。它们不止是为界面增添新的工作台那么简单，还有新的python命令以及新的对象类型。其结果是，令多种不同的、甚至完全不兼容的对象类型可以共存于同一文档之中。我们将在本教程中检阅FreeCAD中最重要的几种模块，它们是[零件模块](Part_Workbench.md), [网格模块](Mesh_Workbench.md), [草图模块](Sketcher_Workbench.md) 与 [底图模块](Draft_Workbench.md)。


</div>

The true power of FreeCAD lies in its faithful modules, with their respective workbenches. The FreeCAD base application is more or less an empty container. Without its modules it can do little more than create new, empty documents. Each module not only adds new workbenches to the interface, but also new Python commands and new object types. As a result several different, and even totally incompatible, object types can coexist in the same document. The most important modules in FreeCAD that we\'ll look at in this tutorial are: [Part](Part_Workbench.md), [Mesh](Mesh_Workbench.md), [Sketcher](Sketcher_Workbench.md) and [Draft](Draft_Workbench.md).


<div class="mw-translate-fuzzy">

[草图模块与](Sketcher_Workbench.md)[底图模块均用](Draft_Workbench.md)[零件模块来创建并处理它们的几何体](Part_Workbench.md)，它们都采用BRep（边界表示法）且[网格是完全独立的](Mesh_Workbench.md)，另外，它们总是处理各自的对象。更多细节请参考下文。


</div>

您可以通过下列语法来查询当前文本中可用的基础对象类型：


```python
doc.supportedTypes()
```


<div class="mw-translate-fuzzy">

尽管不同的FreeCAD模块会向FreeCAD添加各自的对象类型，但是它们并不会在python控制台中自动加载。这样就可避免开启速度过慢。只有在需要特定模块的时候才会加载它们。因此，例如为了浏览零件模块中的对象类型，可以这样做：


</div>


```python
import Part
Part.
```

我们将在后面更多地讨论零件模块。

[top](#top.md)


<div class="mw-translate-fuzzy">

## 网格


</div>


<div class="mw-translate-fuzzy">

[网格](http://en.wikipedia.org/wiki/Polygon_mesh)是一种普遍使用在[Sketchup](http://en.wikipedia.org/wiki/SketchUp)、[Blender](http://en.wikipedia.org/wiki/Blender_%28software%29)与[3D studio Max](http://en.wikipedia.org/wiki/Autodesk_3ds_Max)中的简易3D对象。它们由3种元素构成：点(又称顶点), 线段(又称边)以及面。包括FreeCAD在内的大多应用中，面可以仅由3个顶点构成。当然，也没有什么可以阻挡您利用多个共面三角形来创建更大的平面。


</div>


<div class="mw-translate-fuzzy">

网格的结构都很简单，就因为其简单性，便很容易在单个文档中使用数以千计的网格。然而，在FreeCAD中其实很少使用网格，所以您可以从其他应用中导入网格格式(.stl, .obj)的对象。另外，网格模块也常用作FreeCAD生命周期中第一个月的主测试模块。


</div>

网格对象与FreeCAD对象是两种截然不同的东西。您可看到，FreeCAD对象就像是网格对象的一种容器(我们在后面还将看到，对于零件对象也是如此)。因此，为了向FreeCAD添加网格对象，我们必须首先创建一个FreeCAD对象与一个网格对象，随后再向FreeCAD对象添加该网格对象：


```python
import Mesh
mymesh = Mesh.createSphere()
mymesh.Facets
mymesh.Points
 
meshobj = doc.addObject("Mesh::Feature", "MyMesh")
meshobj.Mesh = mymesh
doc.recompute()
```


<div class="mw-translate-fuzzy">

这是个利用createSphere()方法自动创建一个球体的标准示例，但是您也可以通过定义其顶点与面的方式来从头创建一个自定义网格。


</div>

[阅读更多关于网格脚本的文档\...](Mesh_Scripting.md)

[top](#top.md)


<div class="mw-translate-fuzzy">

## 零件

[零件模块（Part Module）是整个FreeCAD中最强大的模块](Part_Workbench.md)。通过它可创建并操纵[BRep](http://en.wikipedia.org/wiki/Boundary_representation)对象。这种对象并不像网格那样，它可以附有大量不同的组件。Brep即边界表示（Boundary Representation），意思是Brep对象都由其表面定义而成；这些表面围起并定义了一个内体积。而一个表面可以是多种不同的东西，如平面或非常复杂的NURBS表面。


</div>

The [Part](Part_Workbench.md) module is the most powerful module in the whole of FreeCAD. It allows you to create and manipulate [BRep](https://en.wikipedia.org/wiki/Boundary_representation) objects. BREP stands for \"Boundary Representation\". A BREP object is defined by surfaces that enclose and define an inner volume. Unlike meshes, BREP objects can have a wide variety of components from planar faces to very complex NURBS surfaces.


<div class="mw-translate-fuzzy">

零件模块基于强大的[OpenCasCade](http://en.wikipedia.org/wiki/Open_CASCADE_Technology)库，借此即可轻松地对其中的各种对象执行大量复杂操作，如布尔运算、倒圆角、放样等等......


</div>

零件模块与网格模块的工作方式相同：首先创建一个FreeCAD对象与一个零件对象，再将零件对象添加至FreeCAD对象：


```python
import Part
myshape = Part.makeSphere(10)
myshape.Volume
myshape.Area

shapeobj = doc.addObject("Part::Feature", "MyShape")
shapeobj.Shape = myshape
doc.recompute()
```


<div class="mw-translate-fuzzy">

零件模块(就像网格模块那样)也存在用来自动创建FreeCAD对象并为之添加特定几何图形的快捷方式，所以您可以将上述代码中的最后三行简作：


</div>


```python
Part.show(myshape)
```


<div class="mw-translate-fuzzy">

通过浏览myshape的内容，您将发现许多有趣的子组件，如表面（Faces）、边（Edges）、顶点（Vertexes）、实体（Solids）与壳体（Shells），以及大量各种不同的几何运算，如裁剪(差集)、 求公共部分(交集)或融合(并集)等操作。[拓扑数据脚本页面详述了有关细节](Topological_data_scripting.md)。


</div>


<div class="mw-translate-fuzzy">

[阅读更多关于零件脚本的内容\...](Topological_data_scripting.md)


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

## 底图

FreeCAD中有许多模块如[草图模块与](Sketcher_Workbench.md)[底图模块也能创建零件对象](Draft_Workbench.md)。这些模块为创建对象的方法添加了额外的参数，或者甚至重新实现了各自处理零件几何图形的整套流程。我们此前的立方体示例就是一个参数化对象的完美范例。您要定义一个立方体只需指定其长宽高参数。系统便会基于这些参数自动为对象计算其零件形状。FreeCAD允许您[以python来创建这些对象](Scripted_objects.md)。


</div>

FreeCAD features many more modules, such as [Sketcher](Sketcher_Workbench.md) and [Draft](Draft_Workbench.md), that also create Part objects. These modules add additional parameters to the objects created, or even implement a whole new way to handle the Part geometry in them. Our box example above is a perfect example of a parametric object. All you need to define the box is to specify the parameters height, width and length. Based on those, the object will automatically calculate its Part shape. FreeCAD allows you to [create such objects in Python](Scripted_objects.md).


<div class="mw-translate-fuzzy">

[底图模块（Draft Workbench）还加入了多种](Draft_Workbench.md)2D参数化对象类型（全都是零件对象），例如线段与圆形，还提供了一些不仅用于制作底图对象还可用于任意零件对象的通用函数。为了探索有哪些可用功能，可以简单地这样做：


</div>


```python
import Draft
rec = Draft.makeRectangle(5, 2)
mvec = FreeCAD.Vector(4, 4, 0)
Draft.move(rec, mvec)
Draft.move(box, mvec)
```

[top](#top.md)


<div class="mw-translate-fuzzy">

## 界面

FreeCAD的用户界面是用 [Qt](http://en.wikipedia.org/wiki/Qt_%28framework%29)制作的，这是一个强大的图形界面系统，可用于绘制所有与3D视图有关的菜单、工具栏与按钮等控件，或处理相关的控制操作。Qt提供了一个模块------PySide，借此可通过python去访问与修改Qt界面，正像FreeCAD所做的那样。让我们试着摆弄下Qt界面并制作一个简单的对话框：


</div>

The FreeCAD user interface is made with [Qt](https://en.wikipedia.org/wiki/Qt_(software)), a powerful graphical interface system, responsible for drawing and handling all the controls, menus, toolbars and buttons around the [3D view](3D_view.md). Qt provides a module, [PySide](PySide.md), which allows Python to access and modify Qt interfaces such as FreeCAD\'s. Let\'s try to fiddle with the Qt interface and produce a simple dialog:


```python
from PySide import QtGui
QtGui.QMessageBox.information(None, "Apollo program", "Houston, we have a problem")
```


<div class="mw-translate-fuzzy">

不难发现，此对话框采用了FreeCAD工具栏中的图标，意即Qt知道这条命令是从FreeCAD应用程序中发出的。因此，我们就能轻松地直接操控FreeCAD界面中的任意部件。


</div>


<div class="mw-translate-fuzzy">

Qt确实是一款非常强大的界面系统，您可以利用它实现非常复杂的东东。Qt中也提供了一些简单易用的工具，如Qt Designer，您能够通过它以图形化的方式设计对话框，再借助几行python代码将它们添加至FreeCAD界面。


</div>

[在此阅读关于PySide的更多内容\...](PySide.md)

[top](#top.md)


<div class="mw-translate-fuzzy">

## 宏

您现在已经对基础知识有了较细致的理解，但是，我们应该在哪里保存自己编写的python脚本？又如何从FreeCAD中方便地执行它们呢？对此，FreeCAD给出了一种名为[宏（Macros）的简易机制](Macros.md)。宏是一种可添加至工具栏且通过点击鼠标即可执行的简单python脚本。FreeCAD为您提供了简单的文本编辑器(Macro → Macros → Create)，在此，您可以编写或粘贴脚本代码。写完脚本后，通过Tools → Customiz → Macros即可定义出添加至工具栏的对应脚本按钮。


</div>

Now that you have a good understanding of the basics, where are we going to keep our Python scripts, and how are we going to launch them inside FreeCAD? There is an easy mechanism for that, called [Macros](Macros.md). A macro is a Python script that can be added to a toolbar and launched via a mouse click. FreeCAD provides you with a simple text editor (**Macro → Macros... → Create**) where you can write or paste scripts. Once the script is done, use **Tools → Customize... → Macros** to define a button for it that can be added to toolbars.


<div class="mw-translate-fuzzy">

恭喜，您已经对FreeCAD脚本有了深入的理解！请前往[发烧友中心进一步深造](Power_users_hub.md)！


</div>

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Python scripting tutorial/zh-cn
