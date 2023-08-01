---
- GuiCommand:
   Name:Part_Thickness
   Name/ru:Толщина
   MenuLocation:Деталь → Толщина
   Workbenches:[Верстак Part](Part_Workbench/ru.md)
   SeeAlso:[Смещение](Part_Offset/ru.md)
---

# Part Thickness/ru



## Описание

Инструмент <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Полость](Part_Thickness/ru.md) преобразует твёрдое тела в полый объект, задавая каждой из имеющихся граней определенную толщину. Это позволяет значительно ускорить работу, а также позволяет избежать применения выдавливаний и вырезов.



## Применение

1.  Создайте твердое тело
2.  Выберите одну или несколько граней
3.  Нажмите на инструмент **<img src="images/Part_Thickness.svg" width=16px> '''Полость'''
**
4.  Установите параметры (см. [Параметры](#Параметры.md))
5.  Нажмите **OK** для подтверждения, создайте операцию и выйдите из функции
6.  В таблице свойств так же можно настроить параметры, если это необходимо



## Параметры


<div class="mw-translate-fuzzy">

-   Толщина: Толщина стенки получаемого объекта, установите нужное значение
    -   Положительное значение сместит грани наружу
    -   Отрицательное значение сместит грани внутрь
-   Режим
    -   Скин: Выберите этот вариант, если хотите получить предмет, похожий на вазу, без головы, но с дном.
    -   Труба: выберите этот вариант, если хотите получить объект, похожий на трубу, без головы и без дна. В этом случае может быть удобно выбрать удаляемые грани перед запуском инструмента. Помощь с предопределенными кнопками просмотра или с помощью цифровых клавиш.
    -   Лицевая сторона:
-   Тип соединения
    -   Дуга: удаляет внешние края и создает скругление с радиусом, равным заданной толщине.
    -   Тангенс:
    -   Пересечение:
-   Пересечение:
-   Самопересечение: включает самопересечение
-   Грань / Готово: выберите грани, которые нужно удалить, затем нажмите «Готово».
-   Обновить вид: автоматически обновляет вид в режиме реального времени.


</div>



## Примечания

-   [App Link](App_Link.md) objects linked to the appropriate object types can also be used as source objects. <small>(v0.20)</small> 
-   Complex shapes may produce bizarre, hard to predict results. Carefully inspect the resulting shape and save your work before applying the operation.



## Ссылки

A good example on how to use this tool on the forum: [Re: Help designing a simple enclosure](http://forum.freecadweb.org/viewtopic.php?f=3&t=3766&p=29741&hilit=enclosure#p29547)



## Примеры

**Hollow cylinder**

1.  Create **<img src="images/Part_Cylinder.svg" width=16px> [Cylinder](Part_Cylinder.md)** with radius 10mm and height 20mm
2.  Select the top and bottom surface of the cylinder
3.  Click on the **<img src="images/Part_Thickness.svg" width=16px> Thickness
** button (no need to change default settings) and press **OK**

Notes:

-   For this shape, consider using **<img src="images/Part_Tube.svg" width=16px> [Tube](Part_Tube.md)** instead.
-   Select the cylinder\'s top surface only to create a receptacle.

![](images/ThicknessEsempio1.png )

![](images/ThicknessEsempio2.png )

**Box-Enclosure**

![](images/ThicknessEsempio3.png )

![](images/ThicknessEsempio4.png )



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Thickness/ru
