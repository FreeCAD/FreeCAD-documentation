# App Link/ru
{{TOCright}}

## Введение

<img alt="" src=images/Link.svg  style="width:32px;">

<img alt="" src=images/Link.svg  style="width:32px;"> [App Link](App_Link/ru.md), или, формально, `App::Link`, это тип объекта, который ссылается на другой объект в том же документе в котором он находится или на ссылается на объект который находится в другом документе. Он специально разработан для эффективного многократного дублирования одного объекта, что помогает создавать сложные [сборки](assembly/ru.md) из уже собранных узлов и из множества повторно используемых компонентов, таких как винты, гайки и аналогичные крепежные изделия.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Упрощённая диаграмма отношений между основными объектами программы. Объект `App::Link* это основной компонент системы, он не зависит от какого-либо верстака, но может использоваться в большинстве объектов, созданных во всех верстаках.`

## Применение


<div class="mw-translate-fuzzy">

-   App Links может быть создан нажатием **<img src="images/Std_LinkMake.svg" width=16px> [LinkMake](Std_LinkMake/ru.md)**.


</div>


<div class="mw-translate-fuzzy">


**Примечание:**

[App Link](App_Link/ru.md) это внутренний объект, так что он в основном предназначен для использования разработчиками для создания верстаков сборки. Например, этот объект используют верстаки [Assembly3](Assembly3_Workbench/ru.md) и [Assembly4](Assembly4_Workbench/ru.md).


</div>

## Properties

An [App Link](App_Link.md) (`App::Link` class) is derived from the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class), therefore it shares most of the latter\'s properties.


<div class="mw-translate-fuzzy">

### Данные


</div>


{{Std Base navi

}} {{Document objects navi}}

---
[documentation index](../README.md) > App Link/ru
