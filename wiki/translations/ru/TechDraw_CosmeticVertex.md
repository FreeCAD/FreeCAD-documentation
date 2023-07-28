---
- GuiCommand:/ru
   Name/ru:Добавить вспомогательную вершину
   Name:TechDraw_CosmeticVertex
   MenuLocation:TechDraw → Добавить Вершины → Добавить вспомогательную вершину 
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Добавить вершины по центрам граней](TechDraw_Midpoints/ru.md), [Добавить 4-ре вершины по краям окружности](TechDraw_Quadrants/ru.md)
---

# TechDraw CosmeticVertex/ru



## Описание

The **TechDraw CosmeticVertex** tool adds a [vertex](Glossary#V.md), which is not part of the source geometry, to a view. This vertex behaves like any other vertex and can be used for dimensioning.

<img alt="" src=images/TechDraw_CosmeticVertex_Sample.png  style="width:300px;"> 
*Cosmetic vertices used to create an otherwise impossible dimension*



## Применение

1.  Select a view.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_CosmeticVertex.svg" width=16px> [Add Cosmetic Vertex](TechDraw_CosmeticVertex.md)** button.
    -   Select the **TechDraw → Add Vertices → <img src="images/TechDraw_CosmeticVertex.svg" width=16px> Add Cosmetic Vertex** option from the menu.
3.  A task panel opens.
4.  Optionally press the **Point Picker** button and pick a point on the page. Press the **Escape picking** button to cancel this operation.
5.  Optionally change or specify the X and Y coordinates of the point. The coordinates are relative to the center of the view.
6.  Press the **OK** button.

## Notes

-   You cannot change the position of an existing cosmetic vertex. At the moment there is no other way than to delete it and create a new one.
-   To delete a cosmetic vertex use <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw CosmeticEraser](TechDraw_CosmeticEraser.md).



## Свойства

Cosmetic vertices have no properties of their own, as they are not document objects. They share color and size settings with regular geometry vertices.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Cosmetic vertices are available to [macros](Macros.md) or the [Python](Python.md) console.


```python
dvp = App.ActiveDocument.View
org = App.Vector(0.0, 0.0, 0.0)
dvp.makeCosmeticVertex(org);

#lines too!
start = FreeCAD.Vector (1.0, 5.0, 0.0)
end = FreeCAD.Vector(1.0, -5.0, 0.0)
style = 2
weight = 0.75
pyGreen = (0.0, 0.0, 1.0, 0.0)
dvp.makeCosmeticLine(start,end,style, weight, pyGreen)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw CosmeticVertex/ru
