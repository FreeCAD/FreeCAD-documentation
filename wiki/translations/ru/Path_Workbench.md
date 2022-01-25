# <img alt="Логотип верстака Path" src=images/Workbench_Path.svg  style="width:64px;"> Path Workbench/ru


{{TOCright}}

## Введение

<img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Верстак Path](Path_Workbench/ru.md) используется для создания машинных инструкций для [станков с ЧПУ](https://en.wikipedia.org/wiki/CNC_router) из 3D-моделей FreeCAD. Это позволяет изготавливать реальные вещи на станках с ЧПУ, таких как: фрезерные, токарные станки, лазерные резаки и тому подобном оборудовании. Обычно эти инструкции на языке [G-кодов](https://en.wikipedia.org/wiki/G-code). Здесь представлен [общий пример моделирования траектории движения инструмента на токарном станке с ЧПУ](https://www.ange-softs.com/SIMULCNCHTML/index.html).

<img alt="" src=images/pathwb.png  style="width:600px;">

Рабочий процесс создания инструкций в верстаке FreeCAD Path выглядит следующим образом:

-   3D-модель - это базовый объект, обычно созданный с использованием одного или нескольких верстаков [Part Design](PartDesign_Workbench.md), [Part](Part_Workbench.md) или [Draft](Draft_Workbench.md).
-   В верстаке Path создается [Задание](Path_Job/ru.md). Оно содержит всю информацию, необходимую для генерации G-кода для обработки на станке с ЧПУ: там определен материал, станок имеет определенный [набор инструментов](Path_ToolLibraryEdit.md) и выполняет команды, контролирующие скорость и перемещения (обычно G-Code).
-   Инструменты выбираются в соответствии с требованиями Рабочих Операций.
-   Операции обработки задаются с использованием, например, [Контуров](Path_Profile/ru.md) и [Вырезов](Path_Pocket_3D.md). Эти Операции обработки используют внутренний диалект FreeCAD G-Code, независимо от станка с ЧПУ.
-   Экспортируйте задание в g-код, соответствующий вашему станку. Этот шаг называется «постобработка», доступны разные постпроцессоры.

## Основные понятия 

Верстак Path генерирует G-код, определяющий траектории движения фрезы, необходимую для фрезерования проекта, представленного 3D-моделью на [FreeCAD диалекте G-Кода](https://www.freecadweb.org/wiki/Path_scripting#FreeCAD.27s_internal_GCode_format), который впоследствии переводится на соответствующий диалект для целевого контроллера ЧПУ путем выбора соответствующего постпроцессора.

G-код генерируется из директив и операций, содержащихся в Задании на обработку. Job Workflow перечисляет их в порядке их выполнения. Список заполняется путем добавления Path Operations, Path Dressups, Path Partial Commands и Path Modifications из Path меню или кнопок GUI.

Верстак Path предоставляет диспетчер инструментов (библиотека и таблица инструментов), инструменты проверки G-кода и симуляции обработки. Он содержит постпроцессор и позволяет импортировать и экспортировать шаблоны заданий.


<div class="mw-translate-fuzzy">

Верстак Path имеет внешние зависимости, включая:

1.  Единицы измерения 3D-модели FreeCAD определены в {{MenuCommand | Правка → Предпочтения → Общие → Настройки единиц измерения на вкладке Единицы Измерения}}. Конфигурация Postprocessor определяет единицы измерения результирующего G-кода.
2.  Путь к файлу макроса и геометрические допуски определяются на вкладке {{MenuCommand | Правка → Параметры → Путь → Параметры задания}}.
3.  Цвета определяются на вкладке {{MenuCommand | Правка → Настройки → Путь → Цвета пути}}.
4.  Содержащие параметры тега определены на вкладке {{MenuCommand | Правка → Настройки → Путь → Dressups}}.
5.  То, что качество базовой 3D-модели соответствует требованиям Path WB, проходит проверку геометрии.


</div>

## Ограничения


<div class="mw-translate-fuzzy">

Некоторые текущие ограничения, о которых вам следует знать:

-   Большинство инструментов Path Tools не являются настоящими 3D-инструментами, поскольку поддерживают только 2.5D-обработку. Это означает, что они фактически обрабатывают плоскую форму, но могут вырезать ее до заданной глубины. Однако есть два инструмента, которые создают истинные трехмерные пути: **<img src="images/Path_3DPocket.svg" width=24px> [3D Pocket](Path_Pocket_3D.md)** и **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** (он все еще является [экспериментальной функцией](Path_experimental.md) по состоянию на ноябрь 2020 г.).
-   Большая часть верстака Path разработана для простых, стандартных 3-осевых (xyz) фрезерных станков и роутеров с ЧПУ, но операции для токарной обработки находятся в разработке в версии 0.19\_pre.
-   Большинство операций в верстаке Path будут создавать пути, основанные лишь на стандартной концевой фрезе, независимо от типа инструмента , назначенного в данном контроллере инструмента, за исключением **<img src="images/Path_Engrave.svg" width=24px> [Engrave](Path_Engrave.md)** и **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)**.
-   Операции в верстаке Path не знают о зажимных механизмах, используемых для закрепления заготовки на вашем станке. Следовательно, внимательно просмотрите и симулируйте пути, которые вы создаете, перед отправкой кода на ваш станок. При необходимости смоделируйте свои зажимные механизмы в FreeCAD, чтобы лучше проверять создаваемые пути. Ищите возможные столкновения с зажимами или другими препятствиями на пути движения инструмента.


</div>

## Единицы измерения 

Обработка единиц измерения в Path может быть запутанной. Есть несколько моментов, которые нужно понять:

1.  Базовыми единицами FreeCAD для длины и времени являются «мм» и «с» соответственно. Скорость, таким образом, измеряется в «мм/с». Это внутренний формат хранения FreeCAD
2.  В схеме единиц измерения по умолчанию используются единицы измерения по умолчанию. Если вы используете схему по умолчанию и вводите скорость подачи без единиц измерения, она будет восприниматься как «мм/с»
3.  Большинство станков с ЧПУ предполагает, что скорость подачи будет в «мм/мин» или «дюйм/мин». Большинство постпроцессоров автоматически конвертируют единицы при генерации gcode.

Схемы:

1.  Изменение схемы в настройках изменяет строку по умолчанию для полей ввода. Если вы являетесь пользователем Path и предпочитаете проектировать в метрической системе настоятельно рекомендуется использовать схему «Метрические мелкие детали и ЧПУ». Если вы проектируете в единицах США, то будет работать Imperial Decimal и Building US
2.  Изменение предпочитаемой схемы объекта не повлияет на вывод, но поможет избежать ошибок ввода

Вывод:

1.  Генерация правильной единицы измерения в выходном файле является обязанностью постпроцессора и выполняется только в это время.
2.  Единица измерения на выходе полностью не зависимо от выбранной схемы единиц измерения
3.  Постпроцессоры выдают либо метрический (G21) выход, либо Imperial (G20), либо настраиваемый.
4.  Конфигурируемые постпроцессоры по умолчанию для метрики (G21)
5.  Если вы хотите, чтобы ваш настраиваемый постпроцессор выводил имперский gcode (G20), задайте правильный аргумент в конфигурации вывода задания (т.е. \--дюймы для linuxcnc). Это может быть сохранено в шаблоне работы и установлено в качестве шаблона по умолчанию, чтобы сделать его автоматическим для всех будущих работ

Проверка траектории:

1.  Если вы используете инструмент Path Inspect для просмотра g-кода, вы увидите подачу в «мм/с», потому что он не подвергается пост-обработке

## Высоты и глубины 

Многие из команд имеют различные высоты и глубины:

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Визуальная справка по свойствам Depth (установки)*

## Команды

Некоторые команды являются экспериментальными и недоступны по умолчанию. Для их включения, см. [Path experimental](Path_experimental.md).

### Команды проекта 

-   <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Проект](Path_Job.md): Создаёт новую программу для ЧПУ

-   <img alt="" src=images/Path_Post.svg  style="width:32px;"> [Постобработка](Path_Post.md): Экспортирует проект в G-код

-   <img alt="" src=images/Path_Sanity.svg  style="width:32px;"> [Проверить задание на наличие распространенных ошибок](Path_Sanity.md): проверяет выбранное задание на отсутствие значений.[**Experimental**](Path_experimental.md). <small>(v0.19)</small> 

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width:32px;"> [Экспорт шаблона](Path_ExportTemplate.md): Экспортирует текущий проект в качестве шаблона

### Инструментальные команды 

-   <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [Inspect G-code](Path_Inspect.md): Показывает G-код для проверки

-   <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [CAM Simulator](Path_Simulator.md): Показывает операции фрезерной обработки, эмулируя станок

-   <img alt="" src=images/Path_SelectLoop.svg  style="width:32px;"> [Finish Selecting Loop](Path_SelectLoop.md): Завершает петлю между двумя выбранными кромками.

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width:32px;"> [Toggle the Active State of the Operation](Path_OpActiveToggle.md): Активирует или деактивирует операцию.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Открывает редактор для управления библиотеками инструментов ToolBit. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Открывает панель ToolBit. <small>(v0.19)</small> 

### Основные операции 

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profile](Path_Profile.md): Создает операцию обработки профиля для всей модели или для одной или нескольких выбранных граней или кромок. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_Pocket_Shape.svg  style="width:32px;"> [Pocket Shape](Path_Pocket_Shape.md): Создает операцию обработки кармана для одного или нескольких выбранных карманов.

-   <img alt="" src=images/Path_Drilling.svg  style="width:32px;"> [Drilling](Path_Drilling.md): Создает цикл сверления.

-   <img alt="" src=images/Path_Face.svg  style="width:32px;"> [Face](Path_MillFace.md): Создает путь обработки поверхности.

-   <img alt="" src=images/Path_Helix.svg  style="width:32px;"> [Helix](Path_Helix.md): Создает спиральную траекторию.

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptive](Path_Adaptive.md): Creates an adaptive clearing and profiling operation.

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Slot](Path_Slot.md): Creates a slotting operation from selected features or custom points. [**Experimental**](Path_experimental.md). <small>(v0.19)</small> 

-   <img alt="" src=images/Path_Engrave.svg  style="width:32px;"> [Engrave](Path_Engrave.md): Creates an engraving path.

-   <img alt="" src=images/Path_Vcarve.svg  style="width:32px;"> [Vcarve](Path_Vcarve.md): Creates an engraving path using a V tool shape. <small>(v0.19)</small> 

### 3D Operations 

-   <img alt="" src=images/Path_3DPocket.svg  style="width:32px;"> [3D Pocket](Path_Pocket_3D.md): Creates a path for a 3D pocket.

-   <img alt="" src=images/Path_Surface.svg  style="width:32px;"> [3D Surface](Path_Surface.md): Creates a path for a 3D surface. [**Experimental**](Path_experimental.md). <small>(v0.19)</small> 

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> [Waterline](Path_Waterline.md): Creates a waterline path for a 3D surface. [**Experimental**](Path_experimental.md). <small>(v0.19)</small> 

### Path Dressup 

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Boundary Dressup](Path_DressupPathBoundary.md): Adds a boundary dressup modification to a selected path.

-   <img alt="" src=images/Path_DressupDogbone.svg  style="width:32px;"> [Dogbone Dressup](Path_DressupDogbone.md): Adds a dogbone dressup modification to a selected path.

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width:32px;"> [DragKnife Dressup](Path_DressupDragKnife.md): Adds a dragknife dressup modification to a selected path.

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width:32px;"> [LeadInOut Dressup](Path_DressupLeadInOut.md): Adds a lead-in and/or lead-out point to a selected path.

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width:32px;"> [RampEntry Dressup](Path_DressupRampEntry.md): Adds ramp entry dressup modification to a selected path.

-   <img alt="" src=images/Path_DressupTag.svg  style="width:32px;"> [Tag Dressup](Path_DressupTag.md): Adds a holding tag dressup modification to a selected path.

### Дополнительные команды 

-   <img alt="" src=images/Path_Fixture.svg  style="width:32px;"> [Крепление](Path_Fixture.md): Изменяет позицию крепления

-   <img alt="" src=images/Path_Comment.svg  style="width:32px;"> [Comment](Path_Comment.md): Вставляет комментарий в G-код.

-   <img alt="" src=images/Path_Stop.svg  style="width:32px;"> [Stop](Path_Stop.md): Вставить команду полной остановки станка.

-   <img alt="" src=images/Path_Custom.svg  style="width:32px;"> [Custom](Path_Custom.md): Вставляет пользовательский G-код.

-   <img alt="" src=images/Path_Shape.svg  style="width:32px;"> [From Shape](Path_Shape.md): Создаёт траекторию из существующего объекта Part [**Experimental**](Path_experimental.md).

### Модификация траектории 

-   <img alt="" src=images/Path_Copy.svg  style="width:32px;"> [Copy the operation in the job](Path_Copy.md): Создает параметрическую копию выбранного объекта траектории.

-   <img alt="" src=images/Path_Array.svg  style="width:32px;"> [Array](Path_Array.md): Создает массив путем дублирования выбранного участка траектории.

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width:32px;"> [Simple Copy](Path_SimpleCopy.md): Создает непараметрическую копию выбранного объекта траектории.

### Miscellaneous

-   <img alt="" src=images/Path_Area.svg  style="width:32px;"> [Area](Path_Area.md): Creates a feature area from selected objects. [**Experimental**](Path_experimental.md).

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width:32px;"> [Area workplane](Path_Area_Workplane.md): Creates a feature area workplane. [**Experimental**](Path_experimental.md).

### Obsolete

-   <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:32px;"> [Диспетчер инструментов](Path_ToolLibraryEdit.md): Редактор таблицу инструментов. «Устаревшая» система работы с инструментами.{{VersionMinus|0.18}}

## ToolBit architecture 

Управляйте инструментами и библиотекой инструментов. Основано на архитектуре ToolBit. <small>(v0.19)</small> 

-   [Path Tools](Path_Tools.md)
-   [Path ToolShape](Path_ToolShape.md)
-   [Path ToolBit](Path_ToolBit.md)
-   [Path ToolBit Library](Path_ToolBit_Library.md)
-   [Path ToolController](Path_ToolController.md)

## Прочее

-   [Path FAQ](Path_FAQ.md): The Path Workbench shares many concepts with other CAM software packages but has its own peculiarities. If something seems wrong this is a good place to start.
-   [Path SetupSheet](Path_SetupSheet.md): You can use a SetupSheet to customize how various property values for operations are calculated.
-   [Path Postprocessor Customization](Path_Postprocessor_Customization.md): If you have a special machine which cannot use one of the available post-processors you may need to write your own post-processor.
-   [Path fourth axis](Path_fourth_axis.md): Experimental four axis milling.
-   [Path Development Roadmap](Path_Development_Roadmap.md): Read this if you are a developer and want to contribute to Path.

## Настройки

-   <img alt="" src=images/Preferences-path.svg  style="width:32px;"> [Настройки\...](Path_Preferences.md): Настройки, доступные для верстака Path.

## Скриптование

Смотри [Создание сценариев (скриптов) модуля Part](Part_scripting/ru.md)

## Руководства

-   [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md): краткое руководство для ознакомления с верстаком Path.

## Видео

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): a playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [Path Workbench](Path_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): a playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) a playlist with a series of 8 videos in English by CAD CAM Lessons.





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/ru
