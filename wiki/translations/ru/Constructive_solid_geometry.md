# Constructive solid geometry/ru
{{TOCright}}

## Введение

[Конструктивная Блочная (твердотельня) Геометрия](https:///ru.wikipedia.org/wiki/Конструктивная_сплошная_геометрия) (**КБГ**) это парадигма моделирования, которая используется во многих традиционных САПР. По сути, она состоит из использования примитивных твёрдых объектов и выполнения с ними логических (булевых) операций, таких как слияние, вычитание и пересечение, для создания окончательной формы.

В FreeCAD этот метод в основном используется с <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Верстаком Part](Part_Workbench/ru.md), он позволяет создавать примитивные объекты, такие как <img alt="" src=images/Part_Box.svg  style="width:24px;"> [кубы](Part_Box/ru.md), <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [цилиндры](Part_Cylinder/ru.md), и <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [сферы](Part_Sphere/ru.md), и соединять их вместе или использовать для обрезки других объектов с помощью инструментов, таких как **<img src="images/Part_Cut.svg" width=24px> [Обрезать](Part_Cut/ru.md)**.

<img alt="" src=images/Part_Constructive_Solid_Geometry_workflow.svg  style="width:800px;">



*Рабочий процесс конструктивной блочной (твердотельной) геометрии (КБГ); с этими  примитивами можно выполнить любое количество операций, чтобы создать другие твердотельные объекты, а затем соединить их или обрезать, пока не будет получена окончательная форма.*

В качестве альтернативы <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Верстак PartDesign](PartDesign_Workbench/ru.md) использует более современный подход, чем простой КБГ(CSG); этот метод называется редактированием объектов с помощью [функций редактирования](Feature_editing/ru.md), что означает создание базового твёрдого тела, а затем добавление последовательных параметрических преобразований для получения конечного тела.


**Примечание:**

[Тела](PartDesign_Body/ru.md), созданные с помощью [верстака PartDesign](PartDesign_Workbench/ru.md), также могут учавствовать в логических операциях с другими объектами верстака **Part**.

## Пример

<img alt="" src=images/Part_CGS_workflow_example.svg  style="width:600px;">



*Пример рабочего процесса конструктивной твердотельной геометрии (CSG): примитивные части соединяются (объединение/union); вычисляется пересечение двух других примитивных частей (пересечение/common); и как итог, получается разность (вычитание/cut) двух предыдущих фигур.*

## Учебники

На странице [Учебники/Tutorials](Tutorials/ru.md) приведены некоторые примеры создания твёрдых тел с помощью <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Верстака Part](Part_Workbench/ru.md) который использует метод **КБГ(CSG)**.

-   [Традиционное моделирование методом КБГ](Manual:Traditional_modeling,_the_CSG_way/ru.md)
-   [Wiffle ball (шарик дуновения) руководство](Whiffle_Ball_tutorial/ru.md)
-   [Руководство по базовому моделированию](Basic_modeling_tutorial/ru.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [Part](Category_Part.md) > Constructive solid geometry/ru
