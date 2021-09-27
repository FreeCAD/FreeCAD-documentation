# Body/ru
## Введение

В FreeCAD слово \"_. Это контейнер, который может содержать [2-х мерный параметрический эскиз](Sketch/ru.md) и [3-х мерные геометрические операции(функций)](PartDesign_Feature/ru.md) для создания твёрдого тела.

Для дальнейшей информации об этом типе объекта см. [PartDesign Body](PartDesign_Body/ru.md).

## Применение

1.  Переключитесь на [верстак PartDesign](PartDesign_Workbench/ru.md).
2.  Нажмите **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body/ru.md)**.
3.  Нажмите **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NewSketch](PartDesign_NewSketch/ru.md)** для создания нового [эскиза](Sketch/ru.md).
4.  Создайте замкнутую полилинию, потом используйте **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad/ru.md)** для выдавливания эскиза и создания базового твёрдого тела.
5.  Добавьте ещё эскизы и выдавливания, и используйте другие инструменты [верстака PartDesign](PartDesign_Workbench/ru.md) для модификации и трансформации исходного тела.

Или, вместо использования <img src=images/PartDesign_AdditiveBox.svg style="width:эскизов](Sketch.md), можно добавить примитивный [PartDesign Features](PartDesign_Feature.md), например, **[16px"> [PartDesign Additive box](PartDesign_AdditiveBox.md)**. Для создания финального объёма можно использовать любое число прибавляющих и вычитающих свойств.

## Примечания

Body требуется при использовании [верстака PartDesign](PartDesign_Workbench/ru.md) с [параметрической](feature_editing/ru.md) методологией.

Body не требуется при использовании [верстака Part](Part_Workbench/ru.md), поскольку этот верстак использует процедуру [конструктивной блочной геометрии](constructive_solid_geometry/ru.md), базирующуюся на [примитивах](Part_Primitives/ru.md) и булевых операциях.


{{PartDesign Tools navi

}} {{Document objects navi}} 

_

---
[documentation index](../README.md) > [Glossary](Category_Glossary.md) > Body/ru
