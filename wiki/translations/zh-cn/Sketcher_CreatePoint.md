---
- GuiCommand:
   Name:Sketcher CreatePoint
   MenuLocation:Sketch → Sketcher geometries → Create point
   Workbenches:[Sketcher](Sketcher_Workbench.md)
---

# Sketcher CreatePoint/zh-cn

## 描述

通过此点工具可在当前的草图中创建一个点，而所创建的点可作为构造几何图形的元素。创建的点将一直作为构造要素，且不会在3D视图中显示出来。

_ 


<div class="mw-translate-fuzzy">

## 如何使用


</div>

-   点击**<img src="images/Sketcher_CreatePoint.png" width=24px> Create point**按钮来激活此功能。
-   通过在草图中单击来创建一个点。
-   按**Esc**键或点击鼠标右键来关闭此功能。

## 选项

可通过设置[草图首选项（Sketcher Preferences）中的选项在捕捉网格模式下创建点](Sketcher_Preferences.md)。此时，如果所创点距网格线的距离小于网格间距的25%，则将被捕捉至网格上。 捕捉模式并不会把它们固定至网格上。可以通过鼠标移动或约束的方式把点移至其他地方。

## 限制

不能在草图的范围之外创建点。如需在3D视图中创建点，请以[零件工作台中的点工具（PartDesign Point）创建基准点](PartDesign_Point.md)，或用[零件工作台中的点工具（Part Point）加以取代](Part_Point.md)。





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/zh-cn
