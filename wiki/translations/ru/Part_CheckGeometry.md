---
- GuiCommand:/ru
   Name/ru:Проверка геометрии
   Name:Part_CheckGeometry‏‎
   MenuLocation:Деталь → Проверка геометрии
   Workbenches:[Part](Part_Workbench/ru.md)
---

# Part CheckGeometry/ru



## Описание

Инструмент **<img src="images/Part_CheckGeometry.svg" width=16px> [Проверка геометрии](Part_CheckGeometry.md)** выполняет проверку и сообщает, является ли геометрическая форма допустимым твердым телом. Инструмент проверяет, является ли допустимым [граничное представление](https://en.wikipedia.org/wiki/Boundary_representation) (BRep или [B-rep](Глоссарий#B.md)) модели.



## Применение

1.  Select a part (beware to select the whole part and not just a face to check for valid solid)
2.  Invoke the tool by either:
    -   Clicking on the **<img src="images/Part_CheckGeometry.svg" width=16px> [CheckGeometry](Part_CheckGeometry.md)** button available in the Part workbench toolbar.
    -   Using the **Part → <img src="images/Part_CheckGeometry.svg" width=16px> Check geometry** entry from the top menu.
3.  The **Settings** task panel opens, unless **Skip settings page** is enabled. See [Options](#Options.md) for more information. Click **Run check**.

Results will be reported in the [Task panel](Task_panel.md). If the check produced errors: click in the report on a specific error message and the corresponding geometric object (edge, face, etc.) will be highlighted in the [3D view](3D_view.md).



## Опции

### Skip settings page 

If ticked, subsequent invocations of the tool skip showing the **Settings** task panel.

### Run BOP check 

If ticked, additionally a Boolean OPerations (BOP) check is performed.

### Log errors 

If ticked, any errors found are also logged in the [report view](Report_view.md).



## Определение характеристик формы 

В дополнение к обнаружению потенциальных ошибок геометрии, этот инструмент показывает ряд свойств, относящихся к выбранному объекту:

-   Проверенный объект
-   Тип формы
-   Количество геометрических объектов: вершины, ребра, провода, грани, оболочки, твердые тела, составные части, соединения, общие формы
-   Геометрические и массовые свойства:
    -   Площадь
    -   Объем
    -   Масса
    -   Длина
    -   Центр масс
    -   Ориентация
    -   Ось симметрии
    -   Точка симметрии
    -   Моменты
    -   Первая ось инерции
    -   Вторая ось инерции
    -   Третья ось инерции
    -   Радиус вращения
    -   Глобальное размещение



## Примечания

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be checked using this tool. For [App Links](App_Link.md) the shape of the linked object is checked. For [App Part](App_Part.md) containers the visible objects within are checked as compounds. <small>(v0.20)</small> 
-   FreeCAD has no methods to automatically repair geometry. If faults are detected the steps involved to create the model need to be examined and fixed manually.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/ru
