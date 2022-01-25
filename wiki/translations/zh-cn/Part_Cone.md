---
- GuiCommand:
   Name:Part Cone
   MenuLocation:Part → Primitives → Cone
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Primitives](Part_Primitives.md)
---

# Part Cone/zh-cn

## Description


<div class="mw-translate-fuzzy">

## 描述

在零件工作台中，可以通过零件工具栏、Part菜单（中的primitives子菜单）或Create Primitives（创建图元）对话框来创建参数化的截断零件圆锥图元。


</div>

<img alt="" src=images/Otherwisedefault270degree_Part_Cone.png  style="width:300px;">


<div class="mw-translate-fuzzy">

下图展示了\"Angle\"为270度且其他参数为默认值的效果。


</div>

## Usage


<div class="mw-translate-fuzzy">

## 如何使用

点击位于零件工作台中的图标<img alt="" src=images/Part_Cone.png  style="width:32px;">。


</div>


<div class="mw-translate-fuzzy">

默认值是根据定义的两个半径radius1、radius2、高度以及角度参数来创建一个截断的参数化圆锥。默认的圆锥被创建在原点(point 0,0,0)处。角度参数确定了所创建的部分圆锥（默认设置值为360°）, 而radius1与radius2则分别对应于截断圆柱体底部与顶部的半径。


</div>

The cone properties can later be edited, either in the [Property editor](Property_editor.md) or by double-clicking the cone in the [Tree view](Tree_view.md).


<div class="mw-translate-fuzzy">

## 选项

+++
| ![](images/PartConeProperty_en.png ) |                                                                                                                                                                  |
|                                                        | **Cone**                                                                                                                                                                    |
|                                                        |                                                                                                                                                                              |
|                                                        | -   Radius 1 - 定义底面弧或圆的半径                                                                                                                                             |
|                                                        | -   Radius 2 - 定义顶面弧或圆的半径                                                                                                                                             |
|                                                        | -   Height - 零件圆锥体的高度                                                                                                                                                   |
|                                                        | -   Angle - 定义截断圆锥体顶面与底面上弧或圆的角度值。默认值360创建的顶底皆为圆面，较小值将创建出不完整的部分圆锥，具体形状取决于实际角度与两个半径所定义的弧，乃至顶面与底面。 |
+++


</div>

-    **Radius 1**: Radius of the arc or circle defining the lower face

-    **Radius 2**: Radius of the arc or circle defining the upper face

-    **Height**: Height of the Part Cone

-    **Angle**: Number of degrees of the arc or circles defining the upper and lower faces of the truncated cone. The default 360° creates circular faces, a lower value will create a portion of a cone as defined by upper and lower faces each with edges defined by an arc of the number of degrees and two radii.

## Scripting

A Part Cone can be created using the following function:


```python
cone = FreeCAD.ActiveDocument.addObject("Part::Cone", "myCone")
```

-   Where {{Incode|"myCone"}} is the name for the object.
-   The function returns the newly created object.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cone/zh-cn
