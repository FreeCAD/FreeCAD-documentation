---
- GuiCommand:
   Name/ru: Добавить вершины по центрам граней
   Name: TechDraw_Midpoints
   MenuLocation: TechDraw - Добавить Вершины - Add Midpoints Vertices
   Workbenches: [TechDraw](TechDraw_Workbench/ru.md)
   Version: 0.19
   SeeAlso: [Добавить вспомогательную вершину](TechDraw_CosmeticVertex/ru.md), [Добавить 4-ре вершины по краям окружности](TechDraw_Quadrants/ru.md)
---

# TechDraw Midpoints/ru


</div>



## Описание

The **TechDraw Midpoints** tool adds [cosmetic vertices](TechDraw_CosmeticVertex.md) at the midpoint of one or more selected edges.

<img alt="" src=images/TechDraw_CosmeticMidpoint_Sample.png  style="width:250px;"> 
*Cosmetic vertices at the midpoint of edges*



## Применение

1.  Select one or more edges in a view.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_Midpoints.svg" width=16px> [Add Midpoint Vertices](TechDraw_Midpoints.md)** button.
    -   Select the **TechDraw → Add Vertices → <img src="images/TechDraw_Midpoints.svg" width=16px> Add Midpoint Vertices** option from the menu.

## Notes

-   The created cosmetic vertices are not parametrically linked to the selected edges.
-   To delete a cosmetic vertex use <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw CosmeticEraser](TechDraw_CosmeticEraser.md).



## Свойства

Cosmetic vertices have no properties of their own, as they are not document objects. They share color and size settings with regular geometry vertices.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Cosmetic vertices are not accessible from [macros](Macros.md) or the [Python](Python.md) console at this time. This snippet will remove all cosmetic vertices from the view.


```python
v = App.ActiveDocument.View
v.clearCV()
App.ActiveDocument.recompute()
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Midpoints/ru
