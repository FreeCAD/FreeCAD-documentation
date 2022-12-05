---
- GuiCommand:/ru
   Name/ru:Добавить вершины по центрам граней
   Name:TechDraw_Midpoints
   MenuLocation:TechDraw → Добавить Вершины → Add Midpoints Vertices
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Добавить вспомогательную вершину](TechDraw_CosmeticVertex/ru.md), [Добавить 4-ре вершины по краям окружности](TechDraw_Quadrants/ru.md)
---

# TechDraw Midpoints/ru

## Описание

The Midpoints tool adds Cosmetic [Vertices](Glossary#V.md) at the midpoints of one or more Edges.

<img alt="" src=images/TechDraw_CosmeticMidpoint_Sample.png  style="width:250px;"> 
*Cosmetic Vertices at midpoints of Edges*

## Применение

1.  Select one or more Edges in a View.
2.  Press the **<img src="images/TechDraw_Midpoints.svg" width=16px> Add Midpoint Vertices** button
3.  Cosmetic Vertices will be added at the mid-point(s) of the Edge(s).

To delete a Midpoint, select it and use the toolbar button **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Remove Cosmetic Object](TechDraw_CosmeticEraser.md)**.

## Свойства

Cosmetic Vertices have no properties of their own, as they are not Document Objects. They share color and size settings with regular geometry vertices.

## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Cosmetic Vertices are not accessible from [macros](Macros.md) or the [Python](Python.md) console at this time. This snippet will remove all Cosmetic Vertices from the View.


```python
>>> v = App.ActiveDocument.View
>>> v.clearCV()
>>> App.activeDocument().recompute()
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Midpoints/ru
