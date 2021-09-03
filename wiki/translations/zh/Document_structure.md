





{{TOCright}}

FreeCad文档包含场景的所有对象。它可以包含组和使用任何工作台生成的对象。您可以在工作台之间切换但仍然编辑同一文档。文档是进行保存操作时存储到磁盘上的内容。您还可以在FreeCad中同时打开多个文档，并打开同一文档的多个视图。


<div class="mw-translate-fuzzy">

在文档中，可以将对象移动到组中，并赋予唯一的名称。管理组、对象和对象名主要是从树视图中完成的。当然，就像freecad中的所有操作一样，它也可以通过[Python解释器完成](python.md)。在树视图中，可以创建组、将对象移动到组、删除对象或组、在树视图中或对象上单击鼠标右键、通过双击对象的名称重命名对象或其他的操作（取决于当前工作台）。


</div>


<div class="mw-translate-fuzzy">

FreeCad文档中的对象可以是不同类型的。每个工作台都可以创建自己的对象类型，例如[网格工作台用来创建网格对象](Mesh_Workbench.md)，[零件工作台用来创建零件对象](Part_Workbench.md)，[草稿工作台也可以用来创建零件对象等](Draft_Workbench.md)。


</div>

如果在FreeCad中至少有一个打开的文档，则始终只有一个活动文档。这是显示在当前三维视图中的文档，即当前正在处理的文档。

## 应用程序和用户界面

与FreeCad中的其他功能一样，图形用户界面部分（GUI）与基本应用程序部分（app）是分开的。这对文件也是有效的。文档也由两部分组成：包含对象的应用程序文档和包含对象在屏幕上的表示方式的视图文档。

把它想象成两个空间，在其中定义对象。它们的构造参数存储在应用程序文档中（是立方体吗？一个圆锥体？多大？），而它们的图形表示形式存储在视图文档中（用黑线绘制？蓝色的面？）。为什么会这样？因为FreeCad也可以在{{emphasis|没有}}图形界面的情况下使用，例如，在其他程序中运行Freecad，即使屏幕上没有绘制任何内容，我们也必须能够操控我们的对象。

视图文档中包含的另一个内容是三维视图。一个文档可以打开多个视图，因此您可以同时从多个视图检查文档。也许你想同时看到你工作的俯视图和俯视图。然后，您将拥有同一文档的两个视图，它们都存储在视图文档中。可以从"视图"菜单或右键单击"视图"选项卡来创建新视图或关闭视图。

## 编程


<div class="mw-translate-fuzzy">

可以通过[Python解释器轻松创建](python.md)、访问和修改文档。例如：


</div>


```python
FreeCAD.ActiveDocument
```

将返回当前（激活）文档 
```python
FreeCAD.ActiveDocument.Blob
``` 会访问你的文档中一个叫做"Blob"的对象。 
```python
FreeCADGui.ActiveDocument
``` 将返回与当前文档关联的视图文档 
```python
FreeCADGui.ActiveDocument.Blob
``` 将访问对象Blob的图形表示（视图）部分 
```python
FreeCADGui.ActiveDocument.ActiveView
``` 将返回当前视图


<div class="mw-translate-fuzzy">


{{docnav|Mouse Model/zh|Preferences Editor/zh}}


</div>



