---
- GuiCommand:
   Name/ru: Добавить 4-ре вершины по краям окружности
   Name: TechDraw_Quadrants
   MenuLocation: TechDraw - Добавить Вершины - Добавить 4-ре вершины по краям окружности
   Workbenches: [TechDraw](TechDraw_Workbench/ru.md)
   Version: 0.19
   SeeAlso: [Добавить Вспомогательную Вершину](TechDraw_CosmeticVertex/ru.md), [Добавить Средние Вершины](TechDraw_Midpoints/ru.md)
---

# TechDraw Quadrants/ru


</div>



## Описание

The **TechDraw Quadrant** tool adds three [cosmetic vertices](TechDraw_CosmeticVertex.md) along the length of one or more selected edges. The vertices are placed at 25%, 50% and 75% of the length of the edges. For a circular edge this results in cosmetic vertices at 90°, 180° and 270°, in addition to its geometric vertex at 0°.

<img alt="" src=images/TechDraw_CosmeticQuadrant_Sample.png  style="width:250px;"> 
*Cosmetic vertices at quadrant points of a circle*



## Применение

1.  Select one or more edges in a view. Any edge can be selected, not just circles.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_Quadrants.svg" width=16px> [Add Quadrant Vertices](TechDraw_Quadrants.md)** button.
    -   Select the **TechDraw → Add Vertices → <img src="images/TechDraw_Quadrants.svg" width=16px> Add Quadrant Vertices** option from the menu.

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
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Quadrants/ru
