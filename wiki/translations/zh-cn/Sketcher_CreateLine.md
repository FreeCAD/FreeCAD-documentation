---
 GuiCommand:
   Name: Sketcher CreateLine
   MenuLocation: Sketch , Sketcher geometries , Create line
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **L**
   SeeAlso: Sketcher_CreatePolyline
---

# Sketcher CreateLine/zh-cn



## 描述


<div class="mw-translate-fuzzy">

此工具会根据用户在3D视图中拾取的两个点来绘制一条线。 在开启此工具时，鼠标指针会变为具有一个红色线条图标的白色十字。侧面还会实时显示当前指针的坐标。


</div>

![](images/Sketcher_LineExample1.png‎ )


<div class="mw-translate-fuzzy">

此工具创建的线条对象的首尾都位于用户指定的对应点处，但是对于[切线（Tangent）](Sketcher_ConstrainTangent.md), [对象上的点（Point On Object）](Sketcher_ConstrainPointOnObject.md)与[内角（Internal Angle）](Sketcher_ConstrainAngle.md)约束而言，此线条却是无限长的。 这就意味着，例如，有着[对象上的点（Point On Object）](Sketcher_ConstrainPointOnObject.md)约束的点可能并不位于用户指定的两点之间，但是却可能位于两点所绘线段的延长线上。


</div>




<div class="mw-translate-fuzzy">

## 如何使用


</div>


<div class="mw-translate-fuzzy">

-   从3d视图中的某个空白区域或从一个已存在的对象上（一定要激活TaskView中的自动约束（auto constraints。译注：0.18版中自动约束设置位于底图的首选项中））拾取两点。
-   按**Esc**键或点击鼠标右键退出此功能。


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/zh-cn
