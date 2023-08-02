---
- GuiCommand:-cn
   Name: 通过中心创建椭圆
   MenuLocation: Sketch -> 草图几何体 -> 通过中心创建椭圆
   Workbenches: Sketcher_Workbench/zh-cn
   Shortcut: **G** **E** **E**
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseBy3Points/zh-cn, Sketcher_CreateCircle/zh-cn, Sketcher_CreateArcOfEllipse/zh-cn
---

# Sketcher CreateEllipseByCenter/zh-cn



## 描述

本工具会根据用户拾取的三个点：中点、长半轴点与短半轴点来绘制一个椭圆。 在开启此工具时，鼠标指针会变为一个附有红色椭圆图标的白色十字。同时还会将当前的指针坐标实时显现在侧。

<img alt="" src=images/Sketcher_EllipseExample1.png‎  style="width:500px;"> 
*The sequence of clicks is indicated by yellow arrows with numbers.<br>
C is the center, a the major diameter, b the minor diameter, F1 and F2 are foci.*




<div class="mw-translate-fuzzy">

## 如何使用


</div>


<div class="mw-translate-fuzzy">

-   通过点击工具按钮，选择对应菜单项或借助键盘快捷键（首先需要在[Interface Customization中为之分配快捷键](Interface_Customization.md)）来调用对应绘制椭圆命令。
-   在3D视图中第一次点击所设置的是椭圆的中心。第二次点击所设置的是椭圆的第一个半径及其方向。第三次点击所设置的是另一种半径（前两次点击所定义的直线至第三次点击位置的距离即为第二个半径）。
-   第三次点击后，椭圆就创建好了，与之共存的还有一系列对齐于它的构造几何对象（长轴、短轴、两个焦点）如果不需要这些构造几何对象，可将其手动删除，以后还可以重新创建。参见[在草图工作台中显示隐藏的内部几何图形](Sketcher_RestoreInternalAlignmentGeometry.md)。
-   按**ESC**键或单击鼠标右键来退出此功能。


</div>

## Peculiarities


<div class="mw-translate-fuzzy">

## 特性

-   长轴与短轴是严格界定的，调整椭圆时并不能交换两者。这是求解器参数化椭圆时所用的信息（中点(x,y)、焦点focus1(x,y)以及短半轴长度(b)），OpenCascade也严格遵循相同的行为。因此，必须通过旋转的方式来交换椭圆的两轴。
-   当椭圆的长轴与短轴被删，且焦点之一被约束为与中点重合，则该椭圆将变为一个圆。但是此圆中的半径约束却无法生效。
-   通过拖动边来移动椭圆与移动椭圆的中点效果相同。


</div>





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/zh-cn
