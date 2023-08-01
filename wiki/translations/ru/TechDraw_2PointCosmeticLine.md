---
- GuiCommand:
   Name/ru: Добавить вспомогательную линию между 2-мя точками
   Name: TechDraw_2PointCosmeticLine
   MenuLocation: TechDraw - Добавить Линии - Добавить вспомогательную линию между 2-мя точками
   Workbenches: [TechDraw](TechDraw_Workbench/ru.md)
   Version: 0.19
   SeeAlso: [Добавить осевую линию к граням](TechDraw_FaceCenterLine/ru.md), [Добавить осевую линию между 2 линиями](TechDraw_2LineCenterLine/ru.md)
---

# TechDraw 2PointCosmeticLine/ru


</div>



## Описание

The **TechDraw 2PointCosmeticLine** tool adds a cosmetic line between two points. The points can be 2D or 3D. The resulting line can be used for dimensioning.

<img alt="" src=images/CosLine2PointsSample.png  style="width:200px;">



*Cosmetic line between two points*




<div class="mw-translate-fuzzy">

## Применение


</div>

1.  Select two points in a TechDraw View or two points in the [3D view](3D_view.md).
2.  If you have selected points in the 3D view: add the correct TechDraw View to the selection by selecting it in the [Tree view](Tree_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> [Add Cosmetic Line Through 2 points](TechDraw_2PointCosmeticLine.md)** button.
    -   Select the **TechDraw → Add Lines → <img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> Add Cosmetic Line Through 2 points** option from the menu.
4.  A task panel opens.
5.  Optionally adjust the coordinates of the points.
6.  Press the **OK** button.
7.  A cosmetic line connecting the two points is added. In the case of 3D points, the line connects the projection of the points.

## Usage edit 

To change the endpoints of a cosmetic line:

1.  Select the cosmetic line.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> [Add Cosmetic Line Through 2 points](TechDraw_2PointCosmeticLine.md)** button.
    -   Select the **TechDraw → Add Lines → <img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> Add Cosmetic Line Through 2 points** option from the menu.
3.  A task panel opens.
4.  Adjust the coordinates of the points.
5.  Press the **OK** button.

## Notes

-   To delete a cosmetic line use <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw CosmeticEraser](TechDraw_CosmeticEraser.md).
-   To change the appearance of a cosmetic line use <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [TechDraw DecorateLine](TechDraw_DecorateLine.md).



## Свойства

Cosmetic lines have no properties of their own, as they are not document objects.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Cosmetic lines can be created using the {{Incode|makeCosmeticLine(v1, v2)}} or {{Incode|makeCosmeticLine3d(v1, v2)}} methods of DrawViewPart.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCosmeticLine/ru
