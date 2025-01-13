---
 GuiCommand:-cn
   Name: Arch Add   Name/zh-cn: 建筑添加工具
   MenuLocation: Arch , Add
   Workbenches: Arch_Workbench
   SeeAlso: Arch Remove
---

# Arch Add/zh-cn


</div>



## 描述


<div class="mw-translate-fuzzy">

借助本建筑添加工具您将能够实现以下4种操作：

-   将具有[形状（shape）](Part_Workbench.md)的对象添加至[墙体（wall）](Arch_Wall.md)或[结构构件（structure）](Arch_Structure.md)等建筑构件。这会令那些对象成为建筑构件的一部分，即令您在不改动宽高等属性的情况下，方便地修改其形状。
-   将[墙体（wall）](Arch_Wall.md)或[结构构件（structure）](Arch_Structure.md)等建筑构件添加至基于组织的[楼层（floor）](Arch_Floor.md)等建筑对象。
-   将[建筑坐标系（axis system）](Arch_Axis.md)添加至 [结构构件（structural object）](Arch_Structure.md)。
-   将对象添加至[剖面（section plane）](Arch_SectionPlane.md)。


</div>


<div class="mw-translate-fuzzy">

[建筑移除](Arch_Remove.md)工具与本工具功能相反。


</div>

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;"> 
*将立方体添加至墙体，从而融为一体。*




<div class="mw-translate-fuzzy">

## 如何使用


</div>


<div class="mw-translate-fuzzy">

1.  先选择待添加的（若干）对象。最后选择主建筑对象。
2.  按**<img src="images/Arch_Add.svg" width=16px> [Add](Arch_Add.md)**按钮。


</div>

## Scripting


<div class="mw-translate-fuzzy">

## 脚本


**参阅:**

[Arch API](Arch_API.md) 与 [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md)。


</div>


<div class="mw-translate-fuzzy">

借助下列函数即可在[宏](macros.md)与[Python](Python.md)控制台中使用添加工具：


</div>


:   
    
```python
    addComponents(objectsList, host)
    
```
    


<div class="mw-translate-fuzzy">

-   将`objectsList`中的对象添加至`host`对象。
    -   
        `objectsList`
        
        可以是单个对象或一组对象。


</div>

示例：


```python
import FreeCAD, Arch, Draft, Part

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Arch.addComponents(Wall2, Wall)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Add/zh-cn
