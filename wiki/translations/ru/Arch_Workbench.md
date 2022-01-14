# <img alt="Логотип верстака Arch" src=images/Workbench_Arch.svg  style="width:64px;"> Arch Workbench/ru


{{TOCright}}

## Введение

<img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Архитектурный верстак](Arch_Workbench/ru.md) обеспечивает современный процесс [информационного моделирования здания](http://ru.wikipedia.org/wiki/BIM) (Building Information Modeling, BIM) внутри FreeCAD, c поддержкой таких функций как полностью параметрические архитектурные элементы вроде стен, балок, крыш, окон, лестниц, труб и фурнитуры. Он поддерживает Industry Foundation Classes ([IFC](Arch_IFC/ru.md)) данные, и создание двумерных планов строений совместно с [верстаком TechDraw](TechDraw_Workbench/ru.md).

Верстак Arch импортирует все инструменты из [верстака Draft](Draft_Workbench/ru.md), используя двумерные объекты для построения архитектурных объектов. В то же время Arch так же использует твердотельные объекты, созданные в других верстаках вроде [Part](Part_Workbench/ru.md) и [PartDesign](PartDesign_Workbench/ru.md).

Функциональность [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) во FreeCAD сейчас постепенно разделяется на описываемый верстак Arch, который содержит все архитектурные инструменты, и [верстак BIM](BIM_Workbench/ru.md), который можно установить через [Addon Manager](Std_AddonMgr/ru.md). Этот верстак добавит новые инструменты в интерфейсе программы поверх инструментов Архитектурного Модуля, с тем чтобы сделать рабочий процесс BIM в FreeCAD более интуитивно понятным и удобным для пользователя.

The developers of Draft, Arch, and BIM also collaborate with the greater [OSArch community](https://osarch.org), with the ultimate goal of improving building design by using entirely free software.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

## Инструменты

Эти инструменты используются для создания архитектурных объектов.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Стена](Arch_Wall/ru.md): создаёт стену с нуля или использует выбранный объект в качестве основы
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Curtain Wall](Arch_CurtainWall/ru.md): creates a curtain wall from scratch or using a selected object as a base. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Структура](Arch_Structure/ru.md): создаёт структурный элемент с нуля или использует выбранный объект в качестве основы

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Rebar tools](Arch_CompRebarStraight/ru.md): Аддон Арматуры дополняет структуры верстака Arch.
    -   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Прямая Арматура](Arch_Rebar_Straight/ru.md): Создает прямой арматурный стержень в выбранном структурном элементе
    -   <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [U-образная Арматура](Arch_Rebar_UShape/ru.md): Создает U-образный арматурный стержень в выбранном структурном элементе
    -   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [L-образная Арматура](Arch_Rebar_LShape/ru.md): Создает L-образный арматурный стержень в выбранном структурном элементе
    -   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Изогнутая Арматура](Arch_Rebar_BentShape/ru.md): Создает изогнутый арматурный стержень в выбранном структурном элементе
    -   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Кольцевая Арматура](Arch_Rebar_Stirrup/ru.md): Создает кольцевой арматурный стержень в выбранном структурном элементе
    -   <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Спиральная Арматура](Arch_Rebar_Helical/ru.md): Создает спиральный арматурный стержень в выбранном структурном элементе
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:24px;"> [ColumnReinforcement](Arch_Rebar_ColumnReinforcement/ru.md): создаёт арматуру внутри колонны.
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:24px;"> [ColumnReinforcement TwoTiesSixRebars](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/ru.md): создаёт арматуру внутри колонны.
    -   <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [BeamReinforcement](Arch_Rebar_BeamReinforcement/ru.md): создаёт арматуру внутри балки.
    -   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Арматура](Arch_Rebar/ru.md): Создает произвольный арматурный стержень в выбранном структурном элементе с использованием эскиза

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Этаж](Arch_Floor/ru.md): Создает этаж, включающий выбранные объекты
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Building Part](Arch_BuildingPart/ru.md): Создает часть здания, включающее выбранные объекты
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Building](Arch_Building/ru.md): Создает здание, включающее выбранные объекты
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Site](Arch_Site/ru.md): Создает участок, включающий выбранные объекты
-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Project](Arch_Project.md): Создает проект, включающий выбранные объекты
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Reference](Arch_Reference/ru.md): Связывает объекты из другого файла FreeCAD с этим документом
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Window](Arch_Window/ru.md): Создает окно используя выбранный объект в качестве основы
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Сечение](Arch_SectionPlane/ru.md): Добавляет секущую плоскость в документ


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Axis tools](Arch_CompAxis/ru.md): Инструменты Осей позволяют создать в текущем документе последовательность осевых линий
    -   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Оси](Arch_Axis/ru.md): Добавляет однонаправленный массив осей в документ
    -   <img alt="" src=images/Arch_Axis_System.svg  style="width:32px;"> [Система осей](Arch_AxisSystem/ru.md): Добавляет в документ систему осей, состоящую из нескольких осей
    -   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Сетка](Arch_Grid/ru.md): Добавляет в документ объект в виде сетки


</div>

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Крыша](Arch_Roof/ru.md): Создает наклонную крышу от выбранной грани
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Пространство](Arch_Space/ru.md): Создаёт в документе объект - пространство
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Лестница](Arch_Stairs/ru.md): Создаёт в документе объект - лестница

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Panel tools](Arch_CompPanel/ru.md): Позволяет создать все виды панелеподобных элементов
    -   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Панель](Arch_Panel/ru.md): Создает объект панель из выбранного 2D объекта
    -   <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Проекция панели](Arch_Panel_Cut/ru.md): Создает 2D-проекцию панели <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Лист панелей](Arch_Panel_Sheet/ru.md): Создает 2D-лист панелей включая проекции панелей или другие 2D-объекты <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Группа однородных предметов](Arch_Nest/ru.md): Создает группу плоских однородных предметов внутри контейнера <small>(v0.17)</small> 

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Каркас](Arch_Frame/ru.md): Создает объект каркас из выбранного макета
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Fence](Arch_Fence/ru.md): Создаёт объект забор из выбранных элементов и пути. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Truss](Arch_Truss/ru.md): Создает ферму из выбранных обводов с нуля. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Оборудование](Arch_Equipment/ru.md): Создаёт объекты оборудование или мебель.

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Инструменты создания труб](Arch_CompPipe/ru.md) <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Труба](Arch_Pipe/ru.md): Создает трубу<small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Соединитель труб](Arch_PipeConnector/ru.md): Создает угловое двойное или тройное соединение между двумя или тремя трубами

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Material tools](Arch_CompSetMaterial/ru.md): Инструменты создания материалов позволяют добавить материал в текущий документ
    -   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Материал](Arch_SetMaterial/ru.md): Создает материал и привязывает его к выбранным объектам, если они есть
    -   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Многослойный Материал](Arch_MultiMaterial/ru.md): Создает многослойный материал и привязывает его к выбранным объектам, если они есть <small>(v0.17)</small> 
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Список](Arch_Schedule/ru.md): Создает различные типы списков

### Инструменты изменения 

Эти инструменты предназначены для изменения архитектурных объектов.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Cut with a line](Arch_CutLine.md): Cut an object according to a line.
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Обрезать по сечению](Arch_CutPlane/ru.md): Вырежьте архитектурный объект в соответствии с плоскостью.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Добавить компонент](Arch_Add/ru.md): Добавляет объекты к компоненту
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Удалить компонент](Arch_Remove/ru.md): Вычитает или удаляет объекты из компонента
-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Осмотр](Arch_Survey/ru.md): Вход или выход из режима осмотра

### Утилиты

Это дополнительные инструменты, которые помогут вам в решении конкретных задач.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Компонент](Arch_Component/ru.md): Создает непараметрический Архитектурный компонент
-   <img alt="" src=images/Arch_Component_Clone.svg  style="width:32px;"> [Клонировать компонент](Arch_CloneComponent/ru.md):Создает клон выбранного Архитектурного компонента (не путать с [Draft Clone](Draft_Clone/ru.md))

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Разделить Сетку(Mesh)](Arch_SplitMesh/ru.md): Разделяет выбранную Сеть на отдельные компоненты
-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Сетка в Поверхность](Arch_MeshToShape/ru.md): Конвертирует сетку в поверхность, объединяя копланарные грани
-   <img alt="" src=images/Arch_SelectNonManifold.svg  style="width:32px;"> [Select non-solid meshes](Arch_SelectNonSolidMeshes/ru.md): Выделяет все не являющиеся телами сетки из текущего выделения или из документа
-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Remove Shape](Arch_RemoveShape/ru.md): Превращает кубический базирующийся на форме объект архитектурный в полностью параметрический
-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Close Holes](Arch_CloseHoles/ru.md): Закрывает отверстия в выбранном базирующемся на форме объекте
-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Merge Walls](Arch_MergeWalls/ru.md): Объединяет две или более стен
-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Check](Arch_Check/ru.md): Проверяет, являются ли выделенные объекты твёрдыми телами и не содержат дефектов
-   <img alt="" src=images/IFC.svg  style="width:32px;"> [Ifc Explorer](Arch_IfcExplorer/ru.md): Просмотр содержимого файла [IFC](Arch_IFC/ru.md)
-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Toggle IFC Brep flag](Arch_ToggleIfcBrepFlag/ru.md): Заставляет выделенные объекты экспортироваться как [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).
-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [3 Views from mesh](Arch_3Views/ru.md): Создаёт виды сверху, спереди, и с тыла из [mesh](Mesh_Workbench/ru.md).
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Create IFC spreadsheet\...](Arch_IfcSpreadsheet/ru.md): Создаёт электронную таблицу для сохранения параметров [IFC](Arch_IFC/ru.md) объекта
-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Toggle Subcomponents](Arch_ToggleSubs.md): Показывает или скрывает субкомпоненты объекта Arch.


</div>

### Настройки

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [Настройки](Arch_Preferences/ru.md): предпочтения для стен, структур, арматуры, окон, лестниц, панелей, труб, сеток и осей.

### Форматы файлов 

-   [IFC](Arch_IFC/ru.md) : Классы строительной индустрии
-   [DAE](Arch_DAE/ru.md) : Формат сеток Collada
-   [OBJ](Arch_OBJ/ru.md) : Формат сеток Obj (только экспорт)
-   [JSON](Arch_JSON/ru.md) : Формат JavaScript Object Notation (только экспорт)
-   [3DS](Arch_3DS/ru.md) : Формат 3DS (только импорт)
-   [SHP](Arch_SHP/ru.md): GIS Shapefiles (только импорт)

## Программный интерфейс 


<div class="mw-translate-fuzzy">

В архитектурном модуле можно использовать скрипты [Python](Python.md) и [макросы](macros/ru.md), используя функции [Arch Python API](http://www.freecadweb.org/api/Arch.html).


</div>

## Учебники

-   [Архитектурный рабочий процесс](http://yorik.uncreated.net/guestblog.php?tag=freecad): Пример начального использования FreeCAD в архитектурном процессе.
-   [Учебник по архитектурному модулю](Arch_tutorial/ru.md) (v. 0.14)
-   [Быстрый архитектурный обзор в блоге Yorik\'а](http://yorik.uncreated.net/guestblog.php?2012=180) (v. 0.13)
-   [Видеопрезентация верстака Arch](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Учебник по архитектурным панелям](Arch_panel_tutorial/ru.md) (v. 0.15)
-   [Глава моделирования BIM из руководства FreeCAD](Manual:BIM_modeling/ru.md)
-   [Импорт из STL или OBJ](Import_from_STL_or_OBJ/ru.md)
-   [Экспорт в STL или OBJ](Export_to_STL_or_OBJ/ru.md)





 

[<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md)

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Arch Workbench/ru
