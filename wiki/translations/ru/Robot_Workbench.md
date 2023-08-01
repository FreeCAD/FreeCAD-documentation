# Robot Workbench/ru
**Верстак  Robot в FreeCAD остался без поддержки. Если у Вас есть знания в этом вопросе и интерес к его поддержке, пожалуйста, заявите своё намерение в секции разработчиков на [https://forum.freecadweb.org/index.php форуме FreeCAD].**


**Причина, по которой этот верстак все ещё находится в основном исходном коде, заключается в том, что этот верстак запрограммирован на C++. Если бы этот верстак можно было запрограммировать на Python, то его можно было бы сделать [внешним верстаком](external_workbenches/ru.md) и переместить в отдельный репозиторий. **



## Введение

<img alt="Логотип верстака Robot" src=images/Workbench_Robot.svg  style="width:128px;">

<img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Верстак Robot](Robot_Workbench/ru.md) это инструмент для симуляции стандартного [6-ти осевого промышленного робота](Robot_6-Axis/ru.md), такого как [Kuka](http://kuka.com/).

Вы можете выполнять следующие работы:

-   создать среду моделирования с роботом и заготовкой
-   создать и загрузить траекторию
-   разложить часть детали САПР в траекторию
-   имитировать движение робота и его пространственные ограничения
-   экспортировать траекторию в программный файл робота

Начните с [Учебника по роботам](Robot_tutorial/ru.md), и смотрите программный интерфейс в файле примера [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py).




<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## Инструменты

Основные команды которые можно использовать для настройки робота.

### Роботы

Инструменты создания и управления 6-осевыми роботами.

-   <img alt="" src=images/Robot_CreateRobot.svg  style="width:30px;"> [Добавить робота](Robot_CreateRobot/ru.md): Добавляет нового робота в текущую сцену
-   <img alt="" src=images/Robot_Simulate.svg  style="width:30px;"> [Воспроизвести движение инструмента по траектории](Robot_Simulate/ru.md): Открывает диалог позволяющий выполнить симуляцию движения рабочего инструмента робота по заданной траектории
-   <img alt="" src=images/Robot_Export.svg  style="width:30px;"> [Экспортировать траекторию](Robot_Export/ru.md): Экспортировать траекторию в файл
-   <img alt="" src=images/Robot_SetHomePos.svg  style="width:30px;"> [Сохранить текущее положение как исходное](Robot_SetHomePos/ru.md): Сохранить текущее положение робота как исходное
-   <img alt="" src=images/Robot_RestoreHomePos.svg  style="width:30px;"> [Вернуть в исходное положение](Robot_RestoreHomePos/ru.md): Возвращает робота в исходное положение

### Траектории

Инструменты для создания и управления траекториями. Траектории могут быть параметрические и непараметрические.

#### Не параметрические траектории 

-   <img alt="" src=images/Robot_CreateTrajectory.svg  style="width:30px;"> [Создать траекторию](Robot_CreateTrajectory/ru.md): Поместить на сцену новый объект-траекторию
-   <img alt="" src=images/Robot_SetDefaultOrientation.svg  style="width:30px;"> [Установить ориентацию по умолчанию](Robot_SetDefaultOrientation/ru.md): Создать промежуточные точки-ориентации по умолчанию
-   <img alt="" src=images/Robot_SetDefaultValues.svg  style="width:30px;"> [Установить значения по умолчанию](Robot_SetDefaultValues/ru.md): Установить настройки по умолчанию для создания промежуточных точек
-   <img alt="" src=images/Robot_InsertWaypoint.svg  style="width:30px;"> [Вставить в траекторию](Robot_InsertWaypoint/ru.md): Вставить в траекторию текущее положение робота
-   <img alt="" src=images/Robot_InsertWaypointPre.svg  style="width:30px;"> [Вставить в траекторию предвыбранную](Robot_InsertWaypointPre/ru.md): Вставить в траекторию точку текущего положения курсора мыши

#### Параметрические траектории 

-   <img alt="" src=images/Robot_Edge2Trac.svg  style="width:30px;"> [Край траектории](Robot_Edge2Trac/ru.md): Поместить новый объект, который раскладывается на ребра для траектории
-   <img alt="" src=images/Robot_TrajectoryDressUp.svg  style="width:30px;"> [Настройка траектории](Robot_TrajectoryDressUp/ru.md): Изменить одно и более свойств траектории
-   <img alt="" src=images/Robot_TrajectoryCompound.svg  style="width:30px;"> [Объединение траекторий](Robot_TrajectoryCompound/ru.md): Создать объединение из нескольких одиночных траекторий



## Составление скриптов 

Смотрите на странице [Robot API example](Robot_API_example/ru.md) описания функций, используемых для моделирования расположения робота.

## Учебные материалы 

-   [6-ти осевой робот](Robot_6-Axis/ru.md)
-   [Подготовка VRML для имитации робота](VRML_Preparation_for_Robot_Simulation/ru.md)





{{Robot Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Robot](Category_Robot.md) > Robot Workbench/ru
