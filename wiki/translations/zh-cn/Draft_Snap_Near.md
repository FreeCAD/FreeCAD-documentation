---
- GuiCommand:
   Name: Draft Snap Near
   Workbenches: [Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   SeeAlso: [Draft Snap](Draft_Snap.md), [Draft Snap Lock](Draft_Snap_Lock.md)
---

# Draft Snap Near/zh-cn

## Description


<div class="mw-translate-fuzzy">

## 描述

此方法将捕捉最近点或最近对象的边。


</div>

![](images/Draft_Snap_Near_example.png )


<div class="mw-translate-fuzzy">



*将线段的第二个端点捕捉至一个矩形的边上。*


</div>

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

## 如何使用

1.  确保开启了**<img src="images/Draft_Snap_Lock.svg" width=16px> [Draft ToggleSnap](Draft_Snap_Lock.md)** 与 **<img src="images/Draft_Snap_Near.svg" width=16px> [Snap Near](Draft_Snap_Near.md)**。
2.  选中底图工具来绘制一个几何图形。
3.  将鼠标指针移至希望将点所附对象的附近。
4.  一个小黄圈将出现，指示的是目标点将放置的位置；目标点所附对象可以是一个顶点或一个边。
5.  点击鼠标将创建的点附于此处。


</div>




<div class="mw-translate-fuzzy">

### 备注


</div>


<div class="mw-translate-fuzzy">

若开启多种捕捉方法的话，将首先尝试其他方法；如果其他捕捉方法都无法使用，则鼠标指针将附于目标对象上的最近点（也就是说，最近点捕捉方法优先级最低）。


</div>

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Near/zh-cn
