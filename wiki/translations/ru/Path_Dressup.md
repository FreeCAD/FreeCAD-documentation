




<img alt="Иконка верстака Path" src=images/Workbench_Path.svg  style="width:128px;">


{{TOCright}}

## Введение


<div class="mw-translate-fuzzy">

<img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Верстак Path](Path_Workbench/ru.md) используется для генерации машинных инструкций для [станков с ЧПУ](https://en.wikipedia.org/wiki/CNC_router) из моделей FreeCAD. В результате мы получаем изделия, изготовленные на станках с ЧПУ, таких как фрезерные, токарные станки, лазерные резаки и так далее. Обычно эти инструкции на языке [G-кодов](https://en.wikipedia.org/wiki/G-code).


</div>

<img alt="" src=images/pathwb.png  style="width:600px;">


<div class="mw-translate-fuzzy">

Рабочий процесс создания инструкций в верстаке FreeCAD Path выглядит следующим образом:

-   3D-модель - это базовый объект, обычно созданный с использованием одного или нескольких верстаков [Part Design](PartDesign_Workbench.md), [Part](Part_Workbench.md) или [Draft](Draft_Workbench.md).
-   В верстаке Path создается [Задание](Path_Job/ru.md). Оно содержит всю информацию, необходимую для генерации G-кода для обработки на станке с ЧПУ: там определен материал, станок имеет определенный [набор инструментов](Path_EditToolsTable.md) и выполняет команды, контролирующие скорость и перемещения (обычно G-Code).
-   Инструменты выбираются в соответствии с требованиями Рабочих Операций.
-   Операции обработки задаются с использованием, например, [Контуров](Path_Profile/ru.md) и [Вырезов](Path_Pocket_3D.md). Эти [Операции обработки](Path_objects.md) используют внутренний диалект FreeCAD G-Code, независимо от станка с ЧПУ.
-   Экспортируйте задание в g-код, соответствующий вашему станку. Этот шаг называется «постобработка», доступны разные постпроцессоры.


</div>

## General concepts 


<div class="mw-translate-fuzzy">

## ОСновные понятия 

Верстак Path генерирует G-код, определяющий траектории движения фрезы, необходимую для фрезерования проекта, представленного 3D-моделью на [FreeCAD диалекте G-Кода](https://www.freecadweb.org/wiki/Path_scripting#FreeCAD.27s_internal_GCode_format), который впоследствии переводится на соответствующий диалект для целевого контроллера ЧПУ путем выбора соответствующего постпроцессора.

G-код генерируется из директив и операций, содержащихся в Задании на обработку. Job Workflow перечисляет их в порядке их выполнения. Список заполняется путем добавления Path Operations, Path Dressups, Path Partial Commands и Path Modifications из Path меню или кнопок GUI.


</div>

The G-code is generated from directives and Operations contained in a Path Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding Path Operations, Path Dressups, Path Supplemental Commands, and Path Modifications from the Path Menu, or GUI buttons.


<div class="mw-translate-fuzzy">

Верстак Path предоставляет Диспетчер инструментов (Библиотека, Таблица инструментов), инструменты контроля G-кода и Симуляции. Он связывает Postprocessor и позволяет импортировать и экспортировать Шаблоны Заданий.


</div>


<div class="mw-translate-fuzzy">

Верстак Path имеет внешние зависимости, включая:

1.  Единицы измерения 3D-модели FreeCAD определены в {{MenuCommand | Правка → Предпочтения → Общие → Настройки единиц измерения на вкладке Единицы Измерения}}. Конфигурация Postprocessor определяет единицы измерения результирующего G-кода.
2.  Путь к файлу макроса и геометрические допуски определяются на вкладке {{MenuCommand | Правка → Параметры → Путь → Параметры задания}}.
3.  Цвета определяются на вкладке {{MenuCommand | Правка → Настройки → Путь → Цвета пути}}.
4.  Содержащие параметры тега определены на вкладке {{MenuCommand | Правка → Настройки → Путь → Dressups}}.
5.  То, что качество базовой 3D-модели соответствует требованиям Path WB, проходит проверку геометрии.


</div>

## Limitations

Some current limitations of which you should be aware are:

-   Most of the Path Tools are not true 3D tools but only 2.5D capable. This means that they take a fixed 2D shape and can cut it down to a given depth. However, there are two tools which produce true 3D paths: **<img src="images/Path_3DPocket.svg" width=24px> [3D Pocket](Path_Pocket_3D.md)** and **<img src="images/Path_3DSurface.svg" width=24px> [3D Surface](Path_3DSurface.md)** (which is still an [experimental feature](Path_experimental.md) as of November 2020).
-   Most of Path workbench is designed for a simple, standard 3-axis (xyz) CNC mill/router, but lathe tools are under development in 0.19\_pre.
-   Most operations in Path workbench will return paths based on a standard endmill tool/bit only, regardless of the tool/bit type assigned in a given tool controller with the exception of the **<img src="images/Path_Engrave.svg" width=24px> [Engrave](Path_Engrave.md)** and **<img src="images/Path_3DSurface.svg" width=24px> [3D Surface](Path_3DSurface.md)** operations.
-   The operations within the Path workbench are not aware of clamping mechanisms in use to secure the model to your machine. Consequently, please review and simulate the paths you generate prior to sending the code to your machine. If necessary, model your clamping mechanisms in FreeCAD in order to better inspect the paths generated. Look for possible collisions with clamps or other obstacles along the paths.

## Единицы измерения 

Обработка единиц измерения в Path может быть запутанной. Есть несколько моментов, которые нужно понять:

1.  Базовыми единицами FreeCAD для длины и времени являются «мм» и «с» соответственно. Скорость, таким образом, измеряется в «мм/с». Это внутренний формат хранения FreeCAD
2.  В схеме единиц измерения по умолчанию используются единицы измерения по умолчанию. Если вы используете схему по умолчанию и вводите скорость подачи без единиц измерения, она будет восприниматься как «мм/с»
3.  Большинство станков с ЧПУ предполагает, что скорость подачи будет в «мм/мин» или «дюйм/мин». Большинство постпроцессоров автоматически конвертируют единицы при генерации gcode.

Schemas:

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

## Heights and depths 


<div class="mw-translate-fuzzy">

## Команды Path 

Многие из команд имеют различные высоты и глубины: <img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Визуальная справка по свойствам Depth (установки)*


</div>

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*

## Commands

Some commands are experimental and not available by default. To enable them see [Path experimental](Path_experimental.md).

### Project Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Проект](Path_Job/ru.md): Создаёт новый проект ЧПУ


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_PostProcess.svg  style="width:32px;"> [Post Process](Path_Post/ru.md): Экспортирует проект в G-код


</div>

-   <img alt="" src=images/Path_Sanity.svg  style="width:32px;"> [Check the path job for common errors](Path_Sanity.md): Checks the selected job for missing values. [**Experimental**](Path_experimental.md). <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width:32px;"> [Экспорт Шаблона](Path_ExportTemplate.md): Экспортирует текущий проект в качестве шаблона


</div>

### Tool Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [G-Code Inspector](Path_Inspect/ru.md): Показывает G-код для проверки


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Simulator.png  style="width:32px;"> [Simulator](Path_Simulator.md):Показывает операции фрезерной обработки, эмулируя станок


</div>

-   <img alt="" src=images/Path_SelectLoop.svg  style="width:32px;"> [Finish Selecting Loop](Path_SelectLoop.md): Completes a loop from two selected edges.

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width:32px;"> [Toggle the Active State of the Operation](Path_OpActiveToggle.md): Activates or de-activates a path operation.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Toggles the ToolBit Dock. <small>(v0.19)</small> 

### Basic Operations 

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profile](Path_Profile.md): Creates a profile operation of the entire model, or from one or more selected faces or edges. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_Pocket_Shape.svg  style="width:32px;"> [Pocket Shape](Path_Pocket_Shape.md): Creates a pocketing operation from one ore more selected pocket(s).

-   <img alt="" src=images/Path_Drilling.svg  style="width:32px;"> [Drilling](Path_Drilling.md): Performs a drilling cycle.

-   <img alt="" src=images/Path_Face.svg  style="width:32px;"> [Face](Path_MillFace.md): Creates a surfacing path.

-   <img alt="" src=images/Path_Helix.svg  style="width:32px;"> [Helix](Path_Helix.md): Creates a helical path.

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptive](Path_Adaptive.md): Creates an adaptive clearing and profiling operation.

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Slot](Path_Slot.md): Creates a slotting operation from selected features or custom points. [**Experimental**](Path_experimental.md). <small>(v0.19)</small> 

-   <img alt="" src=images/Path_Engrave.svg  style="width:32px;"> [Engrave](Path_Engrave.md): Creates a engraving path.

-   <img alt="" src=images/Path_Vcarve.svg  style="width:32px;"> [Vcarve](Path_Vcarve.md): Creates a path for a 3D pocket. <small>(v0.19)</small> 

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

### Supplemental Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Fixture.png  style="width:32px;"> [Крепление](Path_Fixture/ru.md): Изменяет позицию фиксации


</div>

-   <img alt="" src=images/Path_Comment.svg  style="width:32px;"> [Comment](Path_Comment.md): Inserts a comment in the G-code of a path.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Stop.svg  style="width:32px;"> [Остановить](Path_Stop/ru.md): Вставить команду полной остановки машины


</div>

-   <img alt="" src=images/Path_Custom.svg  style="width:32px;"> [Custom](Path_Custom.md): Inserts custom G-code.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Shape.svg  style="width:32px;"> [Gcode from a Shape](Path_Shape/ru.md): Создаёт траекторию из существующего объекта Part


</div>

### Path Modification 

-   <img alt="" src=images/Path_Copy.svg  style="width:32px;"> [Copy the operation in the job](Path_Copy.md): Creates a parametric Copy of a selected path object.

-   <img alt="" src=images/Path_Array.svg  style="width:32px;"> [Array](Path_Array.md): Creates an array by duplicating a selected path.

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width:32px;"> [Simple Copy](Path_SimpleCopy.md): Creates a non-parametric copy of a selected path object.

### Miscellaneous

-   <img alt="" src=images/Path_Area.svg  style="width:32px;"> [Area](Path_Area.md): Creates a feature area from selected objects. [**Experimental**](Path_experimental.md).

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width:32px;"> [Area workplane](Path_Area_Workplane.md): Creates a feature area workplane. [**Experimental**](Path_experimental.md).

### Obsolete


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ToolLibraryEdit.png  style="width:32px;"> [Tool Manager](Path_ToolLibraryEdit.md): Редактировать таблицу инструментов


</div>

## ToolBit architecture 

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture. <small>(v0.19)</small> 

-   [Path Tools](Path_Tools.md)
-   [Path ToolShape](Path_ToolShape.md)
-   [Path ToolBit](Path_ToolBit.md)
-   [Path ToolBit Library](Path_ToolBit_Library.md)
-   [Path ToolController](Path_ToolController.md)

## Other

-   [Path FAQ](Path_FAQ.md): The Path Workbench shares many concepts with other CAM software packages but has its own peculiarities. If something seems wrong this is a good place to start.
-   [Path SetupSheet](Path_SetupSheet.md): You can use a SetupSheet to customize how various property values for operations are calculated.
-   [Path Postprocessor Customization](Path_Postprocessor_Customization.md): If you have a special machine which cannot use one of the available post-processors you may need to write your own post-processor.
-   [Path fourth axis](Path_fourth_axis.md): Experimental four axis milling.
-   [Path Development Roadmap](Path_Development_Roadmap.md): Read this if you are a developer and want to contribute to Path.

## Preferences

-   <img alt="" src=images/Preferences-path.svg  style="width:32px;"> [Preferences\...](Path_Preferences.md): Preferences available for the Path Workbench.

## Скриптование

See [Path scripting](Path_scripting.md).

## Tutorials

-   [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with Path.

## Videos

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): a playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [Path Workbench](Path_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): a playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) a playlist with a series of 8 videos in English by CAD CAM Lessons.





{{Path_Tools_navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
