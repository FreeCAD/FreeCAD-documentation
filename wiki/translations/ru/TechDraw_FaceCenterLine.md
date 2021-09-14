---
- GuiCommand:/ru
   Name/ru:Добавить осевую линию к Граням
   Name:TechDraw_FaceCenterLine
   MenuLocation:TechDraw → Добавить Линии → Add Centerline to Face(s)
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Добавить Вспомогательную Вершину](TechDraw_CosmeticVertex/ru.md), [Добавить осевую линию между 2 линиями](TechDraw_2LineCenterLine/ru.md), [Добавить осевую линию между 2 точками](TechDraw_2PointCenterLine/ru.md), [Удалить Вспомогательный Объект](TechDraw_CosmeticEraser/ru.md)
---

## Описание

The FaceCenterLine tool adds a centerline to selected faces.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;"> 
*Centerline added to face*

## Применение

1.  Select one or more Faces in a View.
2.  Press the **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Add Centerline to Face(s)** button
3.  A dialog will open where you can specify attributes of the new centerline.
4.  A centerline will be added at the midpoint of the bounding box of the selected Face(s).

To delete a Centerline, select it and use the toolbar button **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Remove Cosmetic Object](TechDraw_CosmeticEraser.md)**.

## Правка Осевой Линии 

Any of the centerline command buttons (**<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Add Centerline to Face(s)**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Add Centerline between 2 Lines](TechDraw_2LineCenterLine.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Add Centerline between 2 Points](TechDraw_2PointCenterLine.md)**) can be used to edit any centerline.

1.  Select a centerline.
2.  Press any centerline command button.
3.  A dialog will open where you can change attributes of the centerline.
4.  Press **OK** to see your changes.

## Свойства

Centerlines have no properties of their own, as they are no document objects. They have attributes that can be changed in the centerline edit dialog.

1.  Mode (radio buttons):
    -   **Vertical**: Forces a centerline vertical
    -   **Horizontal**: Forces a centerline horizontal
    -   ***Aligned**: This option is not possible for centerline to faces*
2.  **Shift Horiz**: Moves the centerline left or right of its normal position
3.  **Shift Vert**: Moves the centerline up or down from its normal position
4.  **Rotate**: Rotates the centerline around its center (degrees. + counterclockwise, - clockwise)
5.  **Extend**: Makes the centerline longer by this amount
6.  **Color**: Color of centerline
7.  **Weight**: Thickness of the centerline
8.  **Style**: <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continuous, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Dash, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Dot, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> DashDot, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> DashDotDot

## Сценарии


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Centerlines are not accessible from [macros](Macros.md) or the [Python](Python.md) console at this time.

## Примечания

-   FaceCenterLine will eventually replace two View properties:
    -   
        **HorizCenterLine**
        
        : Show a horizontal centerline through view.

    -   
        **VertCenterLine**
        
        : Show a vertical centerline through view.





{{TechDraw Tools navi

}}  
