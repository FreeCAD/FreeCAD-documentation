# Body/ru
## Введение

Во FreeCAD слово \"[Тело](Body/ru.md)\" обычно используется для ссылки на объект [Тело PartDesign](PartDesign_Body/ru.md) (класс `PartDesign   *   *Body`), определённый в [Верстаке PartDesign](PartDesign_Workbench/ru.md). Это контейнер, который может содержать [2D эскизы](Sketch/ru.md) и [3D геометрические операции](PartDesign_Feature/ru.md) для создания твердотельной формы.

Смотри [Тело PartDesign](PartDesign_Body/ru.md) для получения дополнительной информации об этом типе объекта.

## Применение

1.  Переключитесь на [верстак PartDesign](PartDesign_Workbench/ru.md).
2.  Нажмите **[<img src=images/PartDesign_Body.svg style="width   *16px"> [Создать тело](PartDesign_Body/ru.md)**.
3.  Нажмите **[<img src=images/PartDesign_NewSketch.svg style="width   *16px"> [Создать эскиз](PartDesign_NewSketch/ru.md)** для создания нового [эскиза](Sketch/ru.md).
4.  Создайте замкнутую полилинию, потом используйте **[<img src=images/PartDesign_Pad.svg style="width   *16px"> [Выдавливание](PartDesign_Pad/ru.md)** для выдавливания эскиза и создания базового твёрдого тела.
5.  Добавьте ещё эскизы и выдавливания, и используйте другие инструменты [верстака PartDesign](PartDesign_Workbench/ru.md) для модификации и трансформации исходного тела.

В качестве альтернативы, вместо использования [эскизов](Sketch/ru.md), можно добавить [конструктивный элемент PartDesign](PartDesign_Feature.md), например, **[<img src=images/PartDesign_AdditiveBox.svg style="width   *16px"> [Аддитивный куб](PartDesign_AdditiveBox.md)**. Для создания конечной формы можно использовать любое количество аддитивных и субтрактивных конструктивных элементов.

## Примечания

Тело требуется при использовании [Верстака PartDesign](PartDesign_Workbench/ru.md) с методами [редактирования конструктивных элементов](feature_editing/ru.md).

Тело не требуется при использовании [верстака Part](Part_Workbench/ru.md), поскольку этот верстак использует процедуру [конструктивной блочной геометрии](constructive_solid_geometry/ru.md), базирующуюся на [примитивах](Part_Primitives/ru.md) и булевых операциях.


{{PartDesign Tools navi

}} {{Document objects navi}} 

[Category   *Glossary](Category_Glossary.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > Body/ru
