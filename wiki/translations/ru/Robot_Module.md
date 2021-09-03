





{{VeryImportantMessage|Верстак  Robot в FreeCAD остался без поддержки. Если у Вас есть знания в этом вопросе и интерес к его поддержке, пожалуйста, заявите своё намерение в секции разработчиков на [https://forum.freecadweb.org/index.php форуме FreeCAD].}}

The reason this workbench is still in the master source code is because this workbench is programmed in C++. If this workbench could be programmed in Python, then it could be made an [external workbench](external_workbenches.md) and it could be moved to a separate repository. }}

## Введение

<img alt="Изображение иконки верстака Robot" src=images/Workbench_Robot.svg  style="width:128px;">

<img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Верстак Robot](Robot_Workbench/ru.md) это инструмент для симуляции стандартного [6-ти осевого промышленного робота](Robot_6-Axis/ru.md), такого как [Kuka](http://kuka.com/).

Вы можете выполнять следующие работы:

-   создать среду моделирования с роботом и заготовкой
-   создать и загрузить траекторию
-   разложить часть детали САПР в траекторию
-   имитировать движение робота и его пространственные ограничения
-   экспортировать траекторию в программный файл робота

Начните с [Учебника по роботам](Robot_tutorial/ru.md), и смотрите программный интерфейс в файле примера [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py).


{{TOCright}}

<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## Инструменты

Основные команды которые можно использовать для настройки робота.

### Роботы

Инструменты создания и управления 6-осевыми роботами.

-   <img alt="" src=images/Robot_CreateRobot.svg  style="width:30px;"> [Создать робота](Robot_CreateRobot/ru.md): Поместить нового робота на сцену
-   <img alt="" src=images/Robot_Simulate.svg  style="width:30px;"> [Имитировать траекторию](Robot_Simulate/ru.md): Открыть диалог имитации позволяющий выполнить имитацию
-   <img alt="" src=images/Robot_Export.svg  style="width:30px;"> [Экспортировать траекторию](Robot_Export/ru.md): Экспортировать в программный файл робота
-   <img alt="" src=images/Robot_SetHomePos.svg  style="width:30px;"> [Установить стартовую позицию](Robot_SetHomePos/ru.md): Установить стартовое положение робота
-   <img alt="" src=images/Robot_RestoreHomePos.svg  style="width:30px;"> [Восстановить на исходную](Robot_RestoreHomePos/ru.md): Переместить робота в стартовое положение

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

## Учебники

-   [6-ти осевой робот](Robot_6-Axis/ru.md)
-   [Подготовка VRML для имитации робота](VRML_Preparation_for_Robot_Simulation/ru.md)





{{Robot Tools navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
