# CAM Workbench/ru
<div class="mw-translate-fuzzy">





</div>

<img alt="Логотип верстака Path" src=images/Workbench_CAM.svg  style="width:128px;">






## Введение

<img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [Верстак Path](Path_Workbench/ru.md) используется для создания машинных инструкций для [станков с ЧПУ](https://en.wikipedia.org/wiki/CNC_router) из 3D-моделей FreeCAD. Это позволяет изготавливать реальные вещи на станках с ЧПУ, таких как: фрезерные, токарные станки, лазерные резаки и тому подобном оборудовании. Обычно эти инструкции на языке [G-кодов](https://en.wikipedia.org/wiki/G-code). Здесь представлен [общий пример моделирования траектории движения инструмента на токарном станке с ЧПУ](https://www.ange-softs.com/SIMULCNCHTML/index.html).

<img alt="" src=images/pathwb.png  style="width:600px;">


<div class="mw-translate-fuzzy">

Рабочий процесс создания инструкций в верстаке FreeCAD Path выглядит следующим образом:

-   3D-модель - это базовый объект, обычно созданный с использованием одного или нескольких верстаков [Part Design](PartDesign_Workbench.md), [Part](Part_Workbench.md) или [Draft](Draft_Workbench.md).
-   В верстаке Path создается [Задание](CAM_Job/ru.md). Оно содержит всю информацию, необходимую для генерации G-кода для обработки на станке с ЧПУ: там определен материал, станок имеет определенный [набор инструментов](CAM_ToolBitLibraryOpen.md) и выполняет команды, контролирующие скорость и перемещения (обычно G-Code).
-   Инструменты выбираются в соответствии с требованиями Рабочих Операций.
-   Операции обработки задаются с использованием, например, [Контуров](CAM_Profile/ru.md) и [Вырезов](CAM_Pocket_3D.md). Эти Операции обработки используют внутренний диалект FreeCAD G-Code, независимо от станка с ЧПУ.
-   Экспортируйте задание в g-код, соответствующий вашему станку. Этот шаг называется «постобработка», доступны разные постпроцессоры.


</div>



## Основные понятия 


<div class="mw-translate-fuzzy">

Верстак Path генерирует G-код, определяющий траектории движения фрезы, необходимую для фрезерования проекта, представленного 3D-моделью на [FreeCAD диалекте G-Кода](https://www.freecadweb.org/wiki/Path_scripting#FreeCAD.27s_internal_GCode_format), который впоследствии переводится на соответствующий диалект для целевого контроллера ЧПУ путем выбора соответствующего постпроцессора.


</div>


<div class="mw-translate-fuzzy">

G-код генерируется из директив и операций, содержащихся в Задании на обработку. Job Workflow перечисляет их в порядке их выполнения. Список заполняется путем добавления Path Operations, Path Dressups, Path Partial Commands и Path Modifications из Path меню или кнопок GUI.


</div>


<div class="mw-translate-fuzzy">

Верстак Path предоставляет диспетчер инструментов (библиотека и таблица инструментов), инструменты проверки G-кода и симуляции обработки. Он содержит постпроцессор и позволяет импортировать и экспортировать шаблоны заданий.


</div>


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

-   Большинство инструментов Path Tools не являются настоящими 3D-инструментами, поскольку поддерживают только 2.5D-обработку. Это означает, что они фактически обрабатывают плоскую форму, но могут вырезать ее до заданной глубины. Однако есть два инструмента, которые создают истинные трехмерные пути: **<img src="images/CAM_3DPocket.svg" width=24px> [3D Pocket](CAM_Pocket_3D.md)** и **<img src="images/CAM_Surface.svg" width=24px> [3D Surface](CAM_Surface.md)** (он все еще является [экспериментальной функцией](CAM_experimental.md) по состоянию на ноябрь 2020 г.).
-   Большая часть верстака Path разработана для простых, стандартных 3-осевых (xyz) фрезерных станков и роутеров с ЧПУ, но операции для токарной обработки находятся в разработке в версии 0.19_pre.
-   Большинство операций в верстаке Path будут создавать пути, основанные лишь на стандартной концевой фрезе, независимо от типа инструмента , назначенного в данном контроллере инструмента, за исключением **<img src="images/CAM_Engrave.svg" width=24px> [Engrave](CAM_Engrave.md)** и **<img src="images/CAM_Surface.svg" width=24px> [3D Surface](CAM_Surface.md)**.
-   Операции в верстаке Path не знают о зажимных механизмах, используемых для закрепления заготовки на вашем станке. Следовательно, внимательно просмотрите и симулируйте пути, которые вы создаете, перед отправкой кода на ваш станок. При необходимости смоделируйте свои зажимные механизмы в FreeCAD, чтобы лучше проверять создаваемые пути. Ищите возможные столкновения с зажимами или другими препятствиями на пути движения инструмента.


</div>



## Единицы измерения 


<div class="mw-translate-fuzzy">

Обработка единиц измерения в Path может быть запутанной. Есть несколько моментов, которые нужно понять:

1.  Базовыми единицами FreeCAD для длины и времени являются «мм» и «с» соответственно. Скорость, таким образом, измеряется в «мм/с». Это внутренний формат хранения FreeCAD
2.  В схеме единиц измерения по умолчанию используются единицы измерения по умолчанию. Если вы используете схему по умолчанию и вводите скорость подачи без единиц измерения, она будет восприниматься как «мм/с»
3.  Большинство станков с ЧПУ предполагает, что скорость подачи будет в «мм/мин» или «дюйм/мин». Большинство постпроцессоров автоматически конвертируют единицы при генерации gcode.


</div>


<div class="mw-translate-fuzzy">

Схемы:

1.  Изменение схемы в настройках изменяет строку по умолчанию для полей ввода. Если вы являетесь пользователем Path и предпочитаете проектировать в метрической системе настоятельно рекомендуется использовать схему «Метрические мелкие детали и ЧПУ». Если вы проектируете в единицах США, то будет работать Imperial Decimal и Building US
2.  Изменение предпочитаемой схемы объекта не повлияет на вывод, но поможет избежать ошибок ввода


</div>


<div class="mw-translate-fuzzy">

Вывод:

1.  Генерация правильной единицы измерения в выходном файле является обязанностью постпроцессора и выполняется только в это время.
2.  Единица измерения на выходе полностью не зависимо от выбранной схемы единиц измерения
3.  Постпроцессоры выдают либо метрический (G21) выход, либо Imperial (G20), либо настраиваемый.
4.  Конфигурируемые постпроцессоры по умолчанию для метрики (G21)
5.  Если вы хотите, чтобы ваш настраиваемый постпроцессор выводил имперский gcode (G20), задайте правильный аргумент в конфигурации вывода задания (т.е. \--дюймы для linuxcnc). Это может быть сохранено в шаблоне работы и установлено в качестве шаблона по умолчанию, чтобы сделать его автоматическим для всех будущих работ


</div>


<div class="mw-translate-fuzzy">

Проверка траектории:

1.  Если вы используете инструмент Path Inspect для просмотра g-кода, вы увидите подачу в «мм/с», потому что он не подвергается пост-обработке


</div>



## Высоты и глубины 

Многие из команд имеют различные высоты и глубины:

![](images/Path-DepthsAndHeights_ru.gif ) 
*Визуальное отображение некоторых параметров обработки (для настроек)*



## Команды

Некоторые команды являются экспериментальными и недоступны по умолчанию. Для их включения, см. [CAM experimental](CAM_experimental.md).



### Команды проекта 

-   <img alt="" src=images/CAM_Job.svg  style="width:32px;"> [Проект](CAM_Job.md): Создаёт новую программу для ЧПУ

-   <img alt="" src=images/CAM_Post.svg  style="width:32px;"> [Постобработка](CAM_Post.md): Экспортирует проект в G-код


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Sanity.svg  style="width:32px;"> [Проверить задание на наличие распространенных ошибок](CAM_Sanity.md): проверяет выбранное задание на отсутствие значений.[**Experimental**](CAM_experimental.md). <small>(v0.19)</small> 


</div>

-   <img alt="" src=images/CAM_ExportTemplate.svg  style="width:32px;"> [Экспорт шаблона](CAM_ExportTemplate.md): Экспортирует текущий проект в качестве шаблона



### Инструментальные команды 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Inspect.svg  style="width:32px;"> [Inspect G-code](CAM_Inspect.md): Показывает G-код для проверки


</div>

-   <img alt="" src=images/CAM_Simulator.svg  style="width:32px;"> [CAM Simulator](CAM_Simulator.md): Показывает операции фрезерной обработки, эмулируя станок


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_SimulatorGL.svg  style="width:32px;"> [CAM SimulatorGL](CAM_SimulatorGL.md): Enables the new, improved CAM simulator. <small>(v1.0)</small> 


</div>

-   <img alt="" src=images/CAM_SelectLoop.svg  style="width:32px;"> [Finish Selecting Loop](CAM_SelectLoop.md): Завершает петлю между двумя выбранными кромками.

-   <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:32px;"> [Toggle the Active State of the Operation](CAM_OpActiveToggle.md): Активирует или деактивирует операцию.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](CAM_ToolBitLibraryOpen.md): Открывает редактор для управления библиотеками инструментов ToolBit. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](CAM_ToolBitDock.md): Открывает панель ToolBit. <small>(v0.19)</small> 


</div>



### Основные операции 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Profile.svg  style="width:32px;"> [Profile](CAM_Profile.md): Создает операцию обработки профиля для всей модели или для одной или нескольких выбранных граней или кромок. <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Pocket_Shape.svg  style="width:32px;"> [Pocket Shape](CAM_Pocket_Shape.md): Создает операцию обработки кармана для одного или нескольких выбранных карманов.


</div>

-   <img alt="" src=images/CAM_Drilling.svg  style="width:32px;"> [Drilling](CAM_Drilling.md): Создает цикл сверления.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/CAM_Face.svg  style="width:32px;"> [Face](CAM_MillFace.md): Создает путь обработки поверхности.


</div>

-   <img alt="" src=images/CAM_Helix.svg  style="width:32px;"> [Helix](CAM_Helix.md): Создает спиральную траекторию.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Adaptive.svg  style="width:32px;"> [Adaptive](CAM_Adaptive.md): Creates an adaptive clearing and profiling operation.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Slot.svg  style="width:32px;"> [Slot](CAM_Slot.md): Creates a slotting operation from selected features or custom points. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Engrave.svg  style="width:32px;"> [Engrave](CAM_Engrave.md): Creates an engraving path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Deburr.svg  style="width:32px;"> [Deburr](CAM_Deburr.md): Creates a deburr path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Vcarve.svg  style="width:32px;"> [Vcarve](CAM_Vcarve.md): Creates an engraving path using a V tool shape.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### 3D Operations 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Pocket_3D.svg  style="width:32px;"> [3D Pocket](CAM_Pocket_3D.md): Creates a path for a 3D pocket.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Surface.svg  style="width:32px;"> [3D Surface](CAM_Surface.md): Creates a path for a 3D surface. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Waterline.svg  style="width:32px;"> [Waterline](CAM_Waterline.md): Creates a waterline path for a 3D surface. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Path Dressup 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupAxisMap.svg  style="width:32px;"> [Axis Map](CAM_DressupAxisMap.md): Remaps one axis to another.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupPathBoundary.svg  style="width:32px;"> [Boundary](CAM_DressupPathBoundary.md): Adds a boundary dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupDogbone.svg  style="width:32px;"> [Dogbone](CAM_DressupDogbone.md): Adds a dogbone dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupDragKnife.svg  style="width:32px;"> [DragKnife](CAM_DressupDragKnife.md): Adds a dragknife dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupLeadInOut.svg  style="width:32px;"> [LeadInOut](CAM_DressupLeadInOut.md): Adds a lead-in and/or lead-out point to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupRampEntry.svg  style="width:32px;"> [RampEntry](CAM_DressupRampEntry.md): Adds ramp entry dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupTag.svg  style="width:32px;"> [Tag](CAM_DressupTag.md): Adds a holding tag dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupZCorrect.svg  style="width:32px;"> [Z Depth Correction](CAM_DressupZCorrect.md): Corrects the Z depth using Probe Map.


</div>



### Дополнительные команды 

-   <img alt="" src=images/CAM_Fixture.svg  style="width:32px;"> [Крепление](CAM_Fixture.md): Изменяет позицию крепления

-   <img alt="" src=images/CAM_Comment.svg  style="width:32px;"> [Comment](CAM_Comment.md): Вставляет комментарий в G-код.

-   <img alt="" src=images/CAM_Stop.svg  style="width:32px;"> [Stop](CAM_Stop.md): Вставить команду полной остановки станка.

-   <img alt="" src=images/CAM_Custom.svg  style="width:32px;"> [Custom](CAM_Custom.md): Вставляет пользовательский G-код.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Probe.svg  style="width:32px;"> [Probe](CAM_Probe.md): Creates a Probing Grid from a job stock.


</div>

-   <img alt="" src=images/CAM_Shape.svg  style="width:32px;"> [From Shape](CAM_Shape.md): Создаёт траекторию из существующего объекта Part [**Experimental**](CAM_experimental.md).




<div class="mw-translate-fuzzy">

### Модификация траектории 


</div>

-   <img alt="" src=images/CAM_Copy.svg  style="width:32px;"> [Copy the operation in the job](CAM_Copy.md): Создает параметрическую копию выбранного объекта траектории.

-   <img alt="" src=images/CAM_Array.svg  style="width:32px;"> [Array](CAM_Array.md): Создает массив путем дублирования выбранного участка траектории.

-   <img alt="" src=images/CAM_SimpleCopy.svg  style="width:32px;"> [Simple Copy](CAM_SimpleCopy.md): Создает непараметрическую копию выбранного объекта траектории.


<div lang="en" dir="ltr" class="mw-content-ltr">

### Specialty Operations 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ThreadMilling.svg  style="width:32px;"> [Thread Milling](CAM_ThreadMilling.md): Creates a CAM Thread Milling operation from features of a base object. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Miscellaneous


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Area.svg  style="width:32px;"> [Area](CAM_Area.md): Creates a feature area from selected objects. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Area_Workplane.svg  style="width:32px;"> [Area workplane](CAM_Area_Workplane.md): Creates a feature area workplane. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## ToolBit architecture 


</div>


<div class="mw-translate-fuzzy">

Управляйте инструментами и библиотекой инструментов. Основано на архитектуре ToolBit. <small>(v0.19)</small> 


</div>

-   [CAM Tools](CAM_Tools.md)
-   [CAM ToolShape](CAM_ToolShape.md)
-   [CAM ToolBit](CAM_ToolBit.md)
-   [CAM ToolBit Library](CAM_ToolBit_Library.md)
-   [CAM ToolController](CAM_ToolController.md)



## Прочее


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM FAQ](CAM_FAQ.md): The CAM Workbench shares many concepts with other CAM software packages but has its own peculiarities. If something seems wrong this is a good place to start.
-   [CAM SetupSheet](CAM_SetupSheet.md): You can use a SetupSheet to customize how various property values for operations are calculated.
-   [CAM Postprocessor Customization](CAM_Postprocessor_Customization.md): If you have a special machine which cannot use one of the available post-processors you may need to write your own post-processor.
-   [CAM fourth axis](CAM_fourth_axis.md): Experimental four axis milling.


</div>



## Настройки


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-path.svg  style="width:32px;"> [Настройки\...](CAM_Preferences.md): Настройки, доступные для верстака Path.


</div>



## Скриптование

Смотри [Создание сценариев (скриптов) модуля Part](Part_scripting/ru.md)



## Руководства


<div class="mw-translate-fuzzy">

-   [CAM Walkthrough for the Impatient](CAM_Walkthrough_for_the_Impatient.md): краткое руководство для ознакомления с верстаком Path.


</div>



## Видео


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): A playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [CAM Workbench](CAM_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): A playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ): A playlist with a series of 8 videos in English by CAD CAM Lessons.
-   Also see the [Computer-Aided Manufacturing (CAM) section](Video_tutorials#Computer-Aided_Manufacturing_(CAM).md) of the [Video tutorials](Video_tutorials.md) wiki page.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Roadmap


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Development Roadmap](CAM_Development_Roadmap.md): Read this if you are a developer and want to contribute to CAM.


</div>


<div class="mw-translate-fuzzy">





</div>


{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [CAM](Category_CAM.md) > CAM Workbench/ru
