---
- GuiCommand:
   Name:Part Box
   MenuLocation:Part → Primitives → Cube
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Primitives](Part_Primitives.md)
---

# Part Box/zh-cn

## Description


<div class="mw-translate-fuzzy">

## 概述

利用[零件工作台（Part Workbench）中的立方体命令可向处于活动状态的文档中插入一个参数化](Part_Workbench.md) [长方体](http://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid)几何图元。默认情况下，此立方体命令会在原点处插入一个10x10x10 mm且附有\"cube\"标签的立方体。在添加立方体对象后还可以修改这些参数。


</div>

<img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;">

## Usage


<div class="mw-translate-fuzzy">

## 如何使用

-   在零件工作台中点选立方体图标**<img src="images/Part_Box.png" width=30px>**。
-   或者，您也可以从菜单栏中选择**Part → Primitives → Cube**。


</div>

**Result:** The default result is a box with an equal length, width and height of 10 mm. It is attached to the global xy-plane and one edge is coincident with the global z-axis.

The box properties can later be edited, either in the property editor or by double-clicking on the box in the model tree.

## Properties


{{Properties_Title|Box}}


<div class="mw-translate-fuzzy">


{{Properties_Title|Box}}

-    **Length**: 此长度参数是立方体在x轴方向上的尺寸。

-    **Width**: 此宽度参数是立方体在y轴方向上的尺寸。

-    **Height**: 此高度参数是立方体在z轴方向上的尺寸。


</div>

## Scripting


<div class="mw-translate-fuzzy">

## 脚本

通过下列函数即可在[宏以及python控制台中使用立方体命令](macros.md)：


</div>


```python
box = FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```


<div class="mw-translate-fuzzy">

-   其中的\"myBox\"为立方体对象的标签。
-   这段代码会返回一个新创建的立方体类型对象。


</div>


<div class="mw-translate-fuzzy">

您可以访问并修改立方体对象的属性。例如，利用下列代码即可修改长度、宽度与高度参数。


</div>


```python
box.Length = 25
box.Width = 15
box.Height = 30
```

您还可以通过下列代码修改立方体对象的方位：


```python
box.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Box/zh-cn
