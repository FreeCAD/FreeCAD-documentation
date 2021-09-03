---
- GuiCommand:
   Name:Part Cylinder
   MenuLocation:Part → Primitives → Cylinder
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Primitives](Part_Primitives.md)
---

## Description


<div class="mw-translate-fuzzy">

## 描述

利用位置、角度、半径与高度参数创建一个简单的参数化圆柱体。


</div>


<div class="mw-translate-fuzzy">

## 如何使用

在[零件工作台中点击此图标](Part_Workbench.md)<img alt="" src=images/Part_Cylinder.png  style="width:32px;">。默认情况下，此工具会创建一个对齐于坐标轴的半径为2mm且高度为10mm的完整圆柱体，并令其中心与全局原点(point 0,0,0)重合。


</div>

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md)
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Cylinder.svg" width=16px> Cylinder** button in the toolbar.
    -   Select {{MenuCommand|Part → Primitives → <img src="images/Part_Cylinder.svg" width=16px> Cylinder}} entry from the top menu

**Result:** The default result is a full cylinder with a radius of 2 mm and height of 10 mm, centered along the global z-axis and attached to the global xy-plane.

The cylinder properties can later be edited, either in the [Property editor](Property_editor.md) or by double-clicking the cylinder in the [Tree view](Tree_view.md).

<img alt="以圆柱体工具创建的一个圆柱体" src=images/cylinder.png  style="width:650px;">


<div class="mw-translate-fuzzy">

## 选项

创建圆柱体后，用户可编辑其数据选项卡中的各属性：


</div>

-    **Angle**: This is the rotation angle that permits the creation of a portion of cylinder (it is set to 360° by default)

-    **Height**: The height is the distance in the z-axis

-    **Radius**: The radius defines a plane in x-y.

-    **First Angle**: Angle in first direction. <small>(v0.20)</small> 

-    **Second Angle**: Angle in second direction. <small>(v0.20)</small> 





 
