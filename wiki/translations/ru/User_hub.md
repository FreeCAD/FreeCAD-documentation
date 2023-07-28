# User hub/ru
{{TOCright}} <img alt="" src=images/User_hub.png  style="width:64px;">



Это основное место помощи для новичков во FreeCAD.

FreeCAD находится в непрерывной разработке, поэтому информация может отсутствовать или устаревать.Если вы не можете найти нужную информацию, не стесняйтесь спрашивать на [форуме FreeCAD](http://forum.freecadweb.org).

Если хотите внести вклад в FreeCAD, пожалуйста, [помогите](donate/ru.md), и смотрите страницу [помощи FreeCAD](Help_FreeCAD/ru.md) для других видов содействия. Если хотите редактировать эту вики, запросите аккаунт с правами редактирования [на форуме](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830), и читайте общие указания, которым нужно следовать, на странице [WikiPages](WikiPages/ru.md).

Если вы хотите узнать, с чего начался FreeCAD в прежние годы, посетите страницу [История](History/ru.md).



## Применение FreeCAD 



### Введение

-   [Обзор приложения](About_FreeCAD/ru.md): Общий обзор FreeCAD
-   [Установка](Installing/ru.md): Как установить FreeCAD на [Windows](Install_on_Windows/ru.md), [Linux](Install_on_Linux/ru.md) или [Mac](Install_on_Mac/ru.md)
-   [Установка справочных файлов](Installing_Helpfile/ru.md): как установить документацию для работы оффлайн, базирующуюся на этих страницах wiki.
-   [Установка дополнительных компонентов](Installing_additional_components/ru.md): как установить дополнительные сторонние компоненты, которые могут работать вместе с FreeCAD.
-   [С чего начать?](Getting_started/ru.md): Краткий обзор доступных инструментов
-   [FAQ](FAQ/ru.md): Часто задаваемые вопросы
-   [Учебники](Tutorials/ru.md) по различным частям FreeCAD



#### Переход с других САПР 

-   [Обходные решения](Workarounds/ru.md)
-   [Переход в FreeCAD с Fusion 360](Migrating_to_FreeCAD_from_Fusion360/ru.md)
-   [Переход в FreeCAD с OnShape](Migrating_to_FreeCAD_from_OnShape/ru.md)
-   [Переход в FreeCAD с SolidWorks](Migrating_to_FreeCAD_from_SolidWorks/ru.md)
-   [Переход в FreeCAD с Revit](Migrating_to_FreeCAD_from_Revit/ru.md)
-   [Руководство по миграции FreeCAD BIM](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [Таблица совместимости приложений BIM](BIM_application_compatibility_table/ru.md)



### Основные элементы Приложения 

-   [Интерфейс](Interface/ru.md): интерфейс FreeCAD составлен из различных графических элементов на экране, включая [трёхмерный вид](3D_view/ru.md), [древо проекта](Tree_view/ru.md), [редактор свойств](Property_editor/ru.md), [панель задач](Task_panel/ru.md), и [консоль Python](Python_console/ru.md).
-   [Навигация мышью](Mouse_navigation/ru.md): различные способы использования мыши или трэкпада для навигации в панели трёхмерного вида.
-   [Методы выделения](Selection_methods/ru.md): различные методы выделения объектов в программе.
-   [Именование объектов](Object_name/ru.md): Объекты FreeCAD имеют атрибут только для чтения `Name`, который уникально идентифицирует их, и `Label`, редактируемый пользователем.
-   [Редактор настроек](Preferences_Editor/ru.md): система, позволяющая управлять множеством свойств базовой системы и отдельных верстаков.
-   [Форматы файлов](Import_Export/ru.md): различные форматы файлов, которые FreeCAD может читать и записывать



### Верстаки

[Верстаки](Workbenches/ru.md) - это наборы инструментов, используемые для решения определенных задач. Далее перечислены базовые верстаки, идущие в комплекте с каждой установкой FreeCAD:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Стандартные инструменты](Std_Base/ru.md). Эти команды и инструменты присутствуют во всех верстаках.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Верстак Arch](Arch_Workbench/ru.md) для работы с элементами архитектуры.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Верстак Draft](Draft_Workbench/ru.md) содержит 2D-инструменты и основные операции 2D и 3D CAD.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [Верстак FEM](FEM_Workbench/ru.md) обеспечивает рабочий процесс анализа Методом Конечных Элементов (МКЭ).

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> [Верстак Inspection](Inspection_Workbench/ru.md) создан для того, чтобы дать вам специальные инструменты для проверки форм. Все еще находится на ранних стадиях разработки.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> [Верстак Mesh](Mesh_Workbench/ru.md) для работы с триангулярными (разбитыми на треугольники) сетками.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> [Верстак OpenSCAD](OpenSCAD_Workbench/ru.md) обеспечивает совместимость с OpenSCAD и восстановление истории модели [конструктивной твердотельной геометрии](constructive_solid_geometry/ru.md) (CSG).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [ Верстак Part](Part_Workbench/ru.md) для работы с геометрическими примитивами и булевыми операциями.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [ Верстак Part Design](PartDesign_Workbench/ru.md) для построения фигур деталей из эскизов.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> [Верстак Path](Path_Workbench/ru.md) используется для создания инструкций G-Code.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> [Верстак Points](Points_Workbench/ru.md) для работы с облаками точек.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> [Верстак Reverse Engineering](Reverse_Engineering_Workbench/ru.md) предназначен для предоставления специальных инструментов для преобразования форм/тел/сеток в параметрические элементы, совместимые с FreeCAD.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> [Верстак Robot](Robot_Workbench/ru.md) для изучения движений робота. Не обновляется

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Верстак Sketcher](Sketcher_Workbench/ru.md) для работы с геометрически ограниченными эскизами.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> [Верстак Spreadsheet](Spreadsheet_Workbench/ru.md) предназначен для создания и обработки данных электронных таблиц.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> [Верстак Start Center](Start_Workbench/ru.md) позволяет быстро перейти к одному из наиболее распространённых верстаков.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> [Верстак Surface](Surface_Workbench/ru.md) предоставляет инструменты для создания и изменения поверхностей. Он похож на опцию Грань из отрезков [Построителя Форм](Part_Builder/ru.md).

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> [Верстак TechDraw](TechDraw_Workbench/ru.md) для создания технических чертежей из 3D-моделей.

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> [Верстак Test Framework](Testing/ru.md) предназначен для отладки FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> [Верстак Web](Web_Workbench/ru.md) предоставляет окно браузера вместо [3D вида](3D_view/ru.md) FreeCAD.



### Макросы

[Макросы](macros/ru.md) это небольшие куски кода [Python](Python/ru.md) для выполнения простых или сложных задач, не доступных в базовой системе FreeCAD.

Опытные пользователи написали различные [макросы](macros.md) для расширения возможностей FreeCAD.

Начиная с версии FreeCAD 0.17,многие макросы можно установить с помощью [Менеджера Дополнений](Std_AddonMgr/ru.md). Список макросов приведен на странице [рецепты макросов](Macros_recipes/ru.md). Для ручной установки см. [Как установить макросы](How_to_install_macros/ru.md).



### Внешние верстаки 

Когда много макросов и функций разрабатываются вместе, и организуются в панели инструментов и меню, они становятся новыми верстаками.

К [сторонним верстакам](External_workbenches/ru.md) относят собрания функций, которые не входят в базовую систему FreeCAD, обычно разрабатываемые опытными пользователями и ориентированные на особые потребности.

Начиная с FreeCAD 0.17, многие рабочие верстаки можно установить с помощью [Менеджера Дополнений](Std_AddonMgr/ru.md). Для ручной установки см. [Как установить дополнительные верстаки](How_to_install_additional_workbenches/ru.md).



## Ссылки

-   [Справочник команд](List_of_Commands/ru.md): Полный список доступных команд FreeCAD.



## Онлайн помощь 

Это официальная онлайновая помощь по FreeCAD. Пожалуйста, обратите внимание, что вся справочная система в настоящее время на стадии разработки. Она будет использоваться для создания файла .CHM, которые будут распределены с бинарными пакетами FreeCAD. На данный момент на сайте помощи приведены некоторые из наиболее полных описаний.

-   [Справочная система онлайн - Содержание](Online_Help_Toc/ru.md)



## Дополнительно

-   [Центр опытных пользователей](Power_users_hub/ru.md) - это раздел, который следует посетить, если вы хотите узнать о более продвинутых способах работы в FreeCAD.
-   На [Портал сообщества FreeCAD](FreeCAD_Community_Portal/ru.md) содержит в себе проекты, созданные членами сообщества FreeCAD.
-   Не понять смысл того или иного термина или выражения, применямого в FreeCAD? Попробуйте найти ответ в [Справочнике](Glossary/ru.md) .



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/ru
