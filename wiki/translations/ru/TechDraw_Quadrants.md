---
- GuiCommand:/ru
   Name/ru:Добавить 4-ре вершины по краям окружности
   Name:TechDraw_Quadrants
   MenuLocation:TechDraw → Добавить Вершины → Добавить 4-ре вершины по краям окружности
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Добавить Вспомогательную Вершину](TechDraw_CosmeticVertex/ru.md), [Добавить Средние Вершины](TechDraw_Midpoints/ru.md)
---

# TechDraw Quadrants/ru

## Описание

The Quadrant tool adds [Cosmetic Vertices](TechDraw_CosmeticVertex.md) at the 90/180/270° points of a circular edge. The 0° vertex should already be there as a geometric vertex.

<img alt="" src=images/TechDraw_CosmeticQuadrant_Sample.png  style="width:250px;"> 
*Cosmetic vertices at quadrant points of a circle*

## Применение

1.  Select one or more (circular) Edges in a View.
2.  Press the **<img src="images/TechDraw_Quadrants.svg" width=16px> Add Quadrant Vertices** button.
3.  Cosmetic vertices will be added at the quarter-points of the edges.

**Note:** This tool can be used on any edge, not just circles.

To delete a Quadrant Vertex, select it and use the toolbar button **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Remove Cosmetic Object](TechDraw_CosmeticEraser.md)**.

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
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Quadrants/ru
