---
- GuiCommand:
   Name:Draft Snap Perpendicular
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   SeeAlso:[Draft Snap](Draft_Snap.md), [Draft Snap Lock](Draft_Snap_Lock.md)
---

# Draft Snap Perpendicular/zh-cn

## Description


<div class="mw-translate-fuzzy">

## 描述

此方法将捕捉一条线段、边或二者的延长线，从而创建出对应的垂线段。


</div>

This snap option will also find points on the extension of straight edges. Circular edges are always treated as full circles, if a circular edge is an arc the point that is found may not lie on the actual edge.

![](images/Draft_Snap_Perpendicular_example.png )


<div class="mw-translate-fuzzy">


*将线段的第二个端点捕捉至另一（黄色）线段的延长线上，借此令前者垂直于后者*


</div>

## 如何使用

For general information about snapping see [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

1.  确定开启了**<img src="images/Snap_Lock.svg" width=16px> [Draft ToggleSnap](Draft_ToggleSnap.md)**与**<img src="images/Snap_Perpendicular.svg" width=16px> [Snap Perpendicular](Draft_Perpendicular.md)**。
2.  选中[底图线段工具进行绘制](Draft_Line.md)。先输入第一个端点。
3.  将鼠标指针移至某线段或另一个对象的边上，下面来选取垂足（也就是确定线段的第二个端点）。
4.  鼠标下的边将变为高亮黄色，且此边上有一个描述垂足的白色小圈；或者小圈位于目标边的延长线上，第二个端点将自动定位于两者的垂足。
5.  点击鼠标将创建的第二个端点附于此处。


</div>

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Perpendicular/zh-cn
