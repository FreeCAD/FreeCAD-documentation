# Document structure/zh-cn
{{TOCright}}

![](images/Screenshot_treeview.jpg ) 一份 FreeCAD 文档包含了场景中的所有对象。它可以包含组以及所有工作台所创建的对象。因而你可以在工作台之间自由切换，但是仍在同一份 FreeCAD 文档上工作。如果你打算保存你的工作成果，那么 FreeCAD 文档便会被保存到磁盘中。可以在 FreeCAD 中同时打开多份文档，也可以为同一份文档开启多个视图。


<div class="mw-translate-fuzzy">

在文档中，对象可被移入、分组以及唯一化的命名。组、对象、对象命名的管理主要是通过树形视图而实现的。当然，你也可以通过 Python 解释器来完成这些操作。在树状视图中，你可以通过鼠标右键点击树状视图或者对象，进行组的创建、将对象移进组内、删除对象或组等操作；可以使用鼠标左键双击对象的名字进行重命名，也可以进行一些其他的操作，具体依赖于当前的工作台。


</div>


<div class="mw-translate-fuzzy">

FreeCAD 文档内的对象可以是不同类型的。每个工作台都能够创建属于它的对象类型，例如[网格工作台可创建网格对象](Mesh_Workbench/zh-cn.md)，而[零件工作台可创建零件对象](Part_Workbench/zh-cn.md)，还有[草图工作台也可创建零件对象](Draft_Workbench/zh-cn.md)，等等。


</div>

无论 FreeCAD 中开启了一份还是多份文档，总是会仅有一个活动文档，它就是当前显示于三维视图中并且你正在其中工作的文档。

## 应用层与用户界面层


<div class="mw-translate-fuzzy">

与 FreeCAD 其他部分的设计相似，用户界面（GUI）层是与应用层在设计上采用了分离原则。这一原则在 FreeCAD 文档的设计上也有所反映，即文档也被分离成了两部分：应用层文档，它包含了我们的对象；视图层文档，它包含了我们的对象在场景中的表示。


</div>


<div class="mw-translate-fuzzy">

考虑对象的定义发生于两个空间。对象的构造参数（它是立方体？圆锥体？尺寸是多少？）存于应用层文档之中，而其图形表示（使用黑线绘制？面的颜色是蓝色？）则存于视图层文档。为什么要这样设计？这是因为 FreeCAD 可以在没有图形界面的环境中运行，例如 FreeCAD 被嵌入到其他的程序中，而我们必须保证即使不在屏幕上绘制什么也能够操作我们的对象。


</div>

在视图层文档中也包含了三维视图信息。一份文档可以对应于多分被打开的视图，这样你便可以同时通过多个视点来查看文档。你想同时查看你的工作成果的顶视图与前视图么？那么你便需要为同一份文档创建两个视图，它们都会存于视图层文档中。可以通过视图菜单或者右键视图窗口标签来创建或关闭视图。

## 脚本


<div class="mw-translate-fuzzy">

通过 Python 解释器很容易创建、访问以及修改文档。例如：


</div>


```python
FreeCAD.ActiveDocument
```

可返回当前（活动的）文档 
```python
FreeCAD.ActiveDocument.Blob
``` 可访问文档中命名为 \"Blob\" 的对象 
```python
FreeCADGui.ActiveDocument
``` 可返回与当前文档相关的视图层文档 
```python
FreeCADGui.ActiveDocument.Blob
``` 可访问 Blob 对象的图形表示（视图）部分 
```python
FreeCADGui.ActiveDocument.ActiveView
``` 可返回当前视图


<div class="mw-translate-fuzzy">


{{docnav|Mouse Model/zh-cn|Preferences Editor/zh-cn}}


</div>

---
[documentation index](../README.md) > Document structure/zh-cn
