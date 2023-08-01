# Shape/ru
## Введение

В FreeCAD слово \"Форма\" обычно используется для обозначения [Part TopoShape (Топологической Геометрии Детали)](Part_TopoShape/ru.md) (Part::TopoShape класса), типа объекта, который даёт элементу его трёхмерное геометрическое и параметрическое представление (куб, пирамида, сфера, цилиндр, слияние и т. Д.).

По существу, все объекты, отображаемые в [3D виде](3D_view/ru.md), имеют [TopoShape(Топологическую Форму)](Part_TopoShape/ru.md), за исключением \"[Сеток](Mesh/ru.md)\", которые имеют (Mesh::MeshObject клас) MeshObject .

Смотри [Part TopoShape (Топологическая Геометрия Детали)](Part_TopoShape/ru.md) для получения дополнительной информации об этом типе объектов.

![](images/Shape_and_mesh.svg )



*Слева: параметрическая [форма](Shape/ru.md), определяемая свойствами. Справа: [сетка](Mesh/ru.md), определяемая вершинами и треугольными поверхностями.*



## Применение

Формы обычно создаются внутренними функциями [Верстака Part](Part_Workbench/ru.md) и в конечном счёте определяются ядром [OpenCASCADE Технологии](OpenCASCADE/ru.md) (OCCT).

Как только фигура создана, она может быть использована и изменена всеми [верстаками](Workbenches/ru.md) путём создания [скриптовых объектов](scripted_objects/ru.md) вокруг этой фигуры.

По сути, каждый объект, производный от [Функций Part (Feature)](Part_Feature/ru.md) (`Part::Feature` класса), содержит и манипулирует Формой.

Any OpenCascade Shape has a tesselation mainly to view the Shape on screen. More information about this can be found in this German [forum post](https://forum.freecad.org/viewtopic.php?t=77521&start=10#p674947) and in the [OpenCascad Mesh documentation](https://dev.opencascade.org/doc/overview/html/occt_user_guides__mesh.html).



## Примечания

В неофициальном употреблении \"Фигурой\" может быть любая геометрическая фигура, видимая в [3D-виде](3D_view/ru.md), и поэтому её понятие можно спутать с понятием \"[Тело](Body/ru.md)\" или \"[Деталь](Part/ru.md)\".

Однако, когда требуется более точное определение, различие должно быть сделано.

-   \"[Тело](Body/ru.md)\" это объект полученный [Функцией Part](Part_Feature/ru.md) (`Part::Feature` класса), созданный с помощью [Версткак PartDesign](PartDesign_Workbench/ru.md).
-   \"Форма\" - это внутренний объект, встроенный в \"[Тело](Body/ru.md)\".
-   \"[Деталь](Part/ru.md)\" используется для группировки нескольких \"[Тел](Body/ru.md)\" чтобы сформировать [сборку](assembly/ru.md). \"Деталь\" состоит из набора \"Форм\", но не имеет собственной \"Формы\" как таковой.


 {{Document objects navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Part](Category_Part.md) > Shape/ru
