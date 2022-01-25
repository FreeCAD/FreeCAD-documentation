# <img alt="Логотип верстака Image" src=images/Workbench_Image.svg  style="width:64px;"> Image Workbench/ru


{{TOCright}}

## Введение


{{TOCright}}

[Верстак Image](Image_Workbench/ru.md) обрабатывает различные типы [растровых](bitmap/ru.md) изображений, и позволяет открыть их в FreeCAD.

## Инструменты


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Image-import.svg  style="width:32px;"> [Open](Image_Open/ru.md): открыть изображение в новой точке зрения.
-   <img alt="" src=images/Image-import-to-plane.svg  style="width:32px;"> [Import to plane](Image_CreateImagePlane/ru.md): импортировать изображение на плоскость в окне трёхмерного вида.
-   <img alt="" src=images/Image-scale.svg  style="width:32px;"> [Scaling](Image_Scaling/ru.md): масштабировать изображение, импортированное на плоскость.


</div>

## Особенности

-   Подобно [Sketch](Sketcher_Workbench/ru.md), импортированное изображение может быть присоединено к одной из главных плоскостей XY, XZ или YZ, и иметь положительное или отрицательное смещение.
-   Изображение импортируется в соотношении 1 мм на пиксель.
-   Рекомендуется импортировать изображение в разумном разрешении.

## Workflow


<div class="mw-translate-fuzzy">

## Работа

Основное применение этого верстака в трассировке поверх изображения с помощью инструментов [Draft](Draft_Workbench/ru.md) или [Sketcher](Sketcher_Workbench/ru.md), для генерации твёрдого тела на основе контуров изображения.


</div>

Трассировка эскизированием поверх изображения работает лучше при небольшом отрицательном смещении изображения относительно эскиза, например, -0,1 мм относительно рабочей плоскости. То есть изображение будет немного под плоскостью где Вы рисуете свою двумерную геометрию, так что Вы не рисуете на самом изображении.

Смещение может быть установлено при импорте, или позднее, редактированием положения изображения.





{{Image Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Image](Category_Image.md) > Image Workbench/ru
