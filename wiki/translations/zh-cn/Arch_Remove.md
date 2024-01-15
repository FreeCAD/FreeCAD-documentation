---
 GuiCommand:-cn
   Name: Arch Remove
   Name/zh-cn: 建筑移除工具
   MenuLocation: Arch , Remove
   Workbenches: Arch_Workbench/zh-cn
   SeeAlso: Arch Add/zh-cn
---

# Arch Remove/zh-cn


</div>

## 描述


<div class="mw-translate-fuzzy">

移除工具允许您执行两种操作：

-   从建筑对象中移除一个子构件，例如像[建筑添加工具](Arch_Add.md)示例中那样，将添加至墙体的立方体移除掉。
-   从如[墙体（wall）](Arch_Wall.md)或[结构构件（structure）](Arch_Structure.md)等建筑构件中去掉具有[形状（shape）](Part_Workbench.md)的对象。


</div>


<div class="mw-translate-fuzzy">

[建筑添加](Arch_Add.md)工具与本工具功能相反。


</div>

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;"> 
*从墙体中去掉一个立方体，于是便留下了一个洞。*


<div class="mw-translate-fuzzy">

## 如何使用


</div>


<div class="mw-translate-fuzzy">

1.  选中建筑对象中的某个子构件。
2.  按**<img src="images/Arch_Remove.svg" width=16px> [Remove](Arch_Remove.md)**按钮。


</div>


<div class="mw-translate-fuzzy">

或者

1.  先选择待移除的（若干）对象，最后选择主建筑对象（也就是要从中去掉前面所选的对象）。
2.  按**<img src="images/Arch_Remove.svg" width=16px> [Remove](Arch_Remove.md)**按钮。


</div>


<div class="mw-translate-fuzzy">

## 脚本


**参阅:**

[Arch API](Arch_API.md) 与 [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md)。


</div>


<div class="mw-translate-fuzzy">

通过下列函数就可以在[macros](macros.md)与[Python](Python.md)控制台中使用移除工具：


</div>


```python
removeComponents(objectsList, host=None)
```

-   从父对象中去掉`objectsList`里的诸对象。
-   如果指定了`host`对象，此函数将试图从`host`中去掉与`objectsList`里诸对象的交集。

示例： 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 900
Box.Width = 450
Box.Height = 2000
FreeCAD.ActiveDocument.recompute()

Draft.rotate(Box, 45)
Draft.move(Box, FreeCAD.Vector(1000, 700, 0))

Arch.removeComponents(Box, Wall)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/zh-cn|[Add component](Arch_Add.md)|[Survey](Arch_Survey.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Add.svg |IconC=Workbench_Arch.svg |IconR=Arch_Survey.svg}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Remove/zh-cn
