# PartDesign Feature/ru
## Введение

[Конструктивный элемент PartDesign](PartDesign_Feature/ru.md) является «шагом» в процессе моделирования, происходящим внутри [Тела PartDesign](PartDesign_Body/ru.md). Например, каждый раз, когда вы добавляете Куб с помощью [PartDesign AdditiveBox](PartDesign_AdditiveBox/ru.md), вы добавляете констуктивный элемент; когда вы добавляете фаску к кромке с помощью [PartDesign Chamfer](PartDesign_Chamfer/ru.md), вы добавляете еще один конструктивный элемент; когда вы вырезаете отверстие с помощью [sketch](Sketch/ru.md) и [PartDesign Pocket](PartDesign_Pocket/ru.md), вы добавляете ещё один конструктивный элемент.

<img alt="" src=images/PartDesign_Feature_example.png  style="width   *600px;"> 
*Изменение [PartDesign Тела](PartDesign_Body/ru.md) последовательностью из трех конструктивных элементов.*

Есть много типов элементов, которые могут добавить или удалить объем исходного твердого тела. Слово «элемент» относится к самой операции, а также к твёрдому телу, полученному после этой операции.

Чтобы узнать больше о создании твердотельных объектов с помощью [верстака PartDesign](PartDesign_Workbench/ru.md), смотрите [редактирование конструктивных элементов](feature_editing/ru.md).

## Применение

Почти все инструменты в [верстаке PartDesign](PartDesign_Workbench/ru.md) предназначены для добавления элементов в [PartDesign Body](PartDesign_Body/ru.md). Доступ к этим инструментам можно получить из меню и кнопок панели инструментов, когда выбран объект или подэлемент (вершина, кромка, грань).

Элементы могут быть вставлены в различные категории   *

-   Feature base   * относится к объекту Base Feature, который может быть создан в [PartDesign Body](PartDesign_Body/ru.md).
-   Аддитивные и субтрактивные
    -   Примитивные фигуры   * [Box](PartDesign_AdditiveBox/ru.md), [Cone](PartDesign_AdditiveCone/ru.md), [Cylinder](PartDesign_AdditiveCylinder/ru.md), [Ellipsoid](PartDesign_AdditiveEllipsoid/ru.md), [Prism](PartDesign_AdditivePrism/ru.md), [Sphere](PartDesign_AdditiveSphere/ru.md), [Torus](PartDesign_AdditiveTorus/ru.md) и [Wedge](PartDesign_AdditiveWedge/ru.md).
    -   Вычитание примитивных фигур   * [Subtractive Box](PartDesign_SubtractiveBox/ru.md), [Subtractive Cone](PartDesign_SubtractiveCone/ru.md), [Subtractive Cylinder](PartDesign_SubtractiveCylinder/ru.md), [Subtractive Ellipsoid](PartDesign_SubtractiveEllipsoid/ru.md), [Subtractive Prism](PartDesign_SubtractivePrism/ru.md), [Subtractive Sphere](PartDesign_SubtractiveSphere/ru.md), [Subtractive Torus](PartDesign_SubtractiveTorus/ru.md) и [Subtractive Wedge](PartDesign_SubtractiveWedge/ru.md).
    -   На основе профиля   * [Pad](PartDesign_Pad/ru.md), [Revolution](PartDesign_Revolution/ru.md), [Loft](PartDesign_AdditiveLoft/ru.md), [Pipe](PartDesign_AdditivePipe/ru.md).
    -   Вычитание профиля   * [Pocket](PartDesign_Pocket/ru.md), [Hole](PartDesign_Hole/ru.md), [Groove](PartDesign_Groove/ru.md), [Subtractive Loft](PartDesign_SubtractiveLoft/ru.md), [Subtractive Pipe](PartDesign_SubtractivePipe/ru.md).
-   [Boolean](PartDesign_Boolean/ru.md), включая fuse, cut, и common.
-   Украшения
    -   [Chamfer](PartDesign_Chamfer/ru.md)
    -   [Draft](PartDesign_Draft/ru.md)
    -   [Fillet](PartDesign_Fillet/ru.md)
    -   [Thickness](PartDesign_Thickness/ru.md)
-   Трансформации
    -   [Linear pattern](PartDesign_LinearPattern/ru.md)
    -   [Mirrored](PartDesign_Mirrored/ru.md)
    -   [Multi-transformed](PartDesign_MultiTransform/ru.md)
    -   [Polar pattern](PartDesign_PolarPattern/ru.md)
    -   [Scaled](PartDesign_Scaled/ru.md)

## Наследование

<img alt="" src=images/FreeCAD_core_objects.svg  style="width   *800px;">



*Упрощенная диаграмма взаимосвязей между основными объектами в программе. Объекты `PartDesign   *   *Feature* используются для построения параметрических трёхмерных тел и, таким образом, являются производными от базового объекта {{incode|Part   *   *Feature`.}}

## Scripting


**См. так же   ***

[Основы скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md), и [скриптовые объекты](scripted_objects/ru.md).

Смотрите [элементы Part](Part_Feature/ru.md) ждя получения общей информации о добавлении объектов из [консоли Python](Python_console/ru.md).

Смотрите [PartDesign Body](PartDesign_Body/ru.md) для получения общей информации о добавлении тела. Когда тело существует, к нему можно прикрепить элементы с помощью метода Body `addObject()`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject('PartDesign   *   *Body', 'Body')
obj.Label = "Custom label"

feature = App.ActiveDocument.addObject('PartDesign   *   *AdditiveBox', 'Box')
feature.Width = 200
feature.Length = 300
feature.Height = 500
obj.addObject(feature)
App.ActiveDocument.recompute()

feature2 = App.ActiveDocument.addObject('PartDesign   *   *SubtractiveBox', 'Box')
feature2.Width = 50
feature2.Length = 200
feature2.Height = 400
obj.addObject(feature2)
App.ActiveDocument.recompute()
```


{{PartDesign Tools navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Feature/ru
