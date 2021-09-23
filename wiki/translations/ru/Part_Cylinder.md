---
- GuiCommand:/ru
   Name/ru:Цилиндр
   MenuLocation:Деталь → Примитивы → Цилиндр
   Workbenches:[Part](Part_Workbench/ru.md)
   SeeAlso:[Создать примитивы](Part_Primitives/ru.md)
---

# Part Cylinder/ru

## Описание

Создаёт простой цилиндр с параметрами расположение, угол, радиус и длина.

## Применение

1.  Нажмите на <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Верстак Part](Part_Workbench/ru.md)
2.  Существует несколько способов вызова команды:
    -   Нажмите на иконку **<img src="images/Part_Cylinder.svg" width=16px> Цилиндр** на панели инструментов.
    -   Выберите из меню **Деталь → Примитивы → <img src="images/Part_Cylinder.svg" width=16px> Цилиндр**.


<div class="mw-translate-fuzzy">

**Результат:** По умолчанию создаётся твердотельный цилиндр с гранью и центром в плоскости глобальной системы координат (точка 0, 0, 0), радиусом 2мм и высотой 10мм.


</div>

The cylinder properties can later be edited, either in the [Property editor](Property_editor.md) or by double-clicking the cylinder in the [Tree view](Tree_view.md).

<img alt="a cylinder created with the Cylinder tool" src=images/cylinder.png  style="width:650px;">

## Свойства

-    **Angle**: This is the rotation angle that permits the creation of a portion of cylinder (it is set to 360° by default)

-    **Height**: The height is the distance in the z-axis

-    **Radius**: The radius defines a plane in x-y.

-    **First Angle**: Angle in first direction. <small>(v0.20)</small> 

-    **Second Angle**: Angle in second direction. <small>(v0.20)</small>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cylinder/ru
