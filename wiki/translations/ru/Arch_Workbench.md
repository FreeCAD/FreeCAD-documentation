# Arch Workbench/ru
**In v1.0 the BIM, Native-IFC and Arch Workbenches have been merged into the integrated [BIM Workbench](BIM_Workbench.md).**

<img alt="Логотип верстака Arch" src=images/Workbench_Arch.svg  style="width:128px;">






## Введение

The <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Workbench](Arch_Workbench.md) provides a modern [**B**uilding **I**nformation **M**odelling](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM) workflow to FreeCAD, with support for features like fully parametric architectural entities such as walls, beams, roofs, windows, stairs, pipes, and furniture. It supports [**I**ndustry **F**oundation **C**lasses](Arch_IFC.md) (IFC) files, and production of 2D floor plans in combination with the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

Верстак Arch импортирует все инструменты из [верстака Draft](Draft_Workbench/ru.md), используя двумерные объекты для построения архитектурных объектов. В то же время Arch так же использует твердотельные объекты, созданные в других верстаках вроде [Part](Part_Workbench/ru.md) и [PartDesign](PartDesign_Workbench/ru.md).

Функциональность [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) во FreeCAD сейчас постепенно разделяется на описываемый верстак Arch, который содержит все архитектурные инструменты, и [верстак BIM](BIM_Workbench/ru.md), который можно установить через [Addon Manager](Std_AddonMgr/ru.md). Этот верстак добавит новые инструменты в интерфейсе программы поверх инструментов Архитектурного Модуля, с тем чтобы сделать рабочий процесс BIM в FreeCAD более интуитивно понятным и удобным для пользователя.

Разработчики Draft, Arch и BEAM также сотрудничают с крупным [OSArch сообществом](https://osarch.org), в целях улучшения проектирования зданий с помощью полностью бесплатного программного обеспечения.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">



## Инструменты

Данные инструменты используются для создания архитектурных объектов.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Стена](Arch_Wall/ru.md): создаёт стену с нуля или использует выбранный объект в качестве основы.

-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Структура](Arch_Structure/ru.md): создаёт структурный элемент с нуля или использует выбранный объект в качестве основы.

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Rebar tools](Arch_CompRebarStraight.md): These tools, except the last, are only available if the [Reinforcement Workbench](Reinforcement_Workbench.md) has been installed.


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Прямая арматура](Arch_Rebar_Straight/ru.md): Создает прямой арматурный стержень в выбранном структурном элементе.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [U-Образная арматура](Arch_Rebar_UShape/ru.md): Создает U-образный арматурный стержень в выбранном структурном элементе.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [L-Образная арматура](Arch_Rebar_LShape/ru.md): Создает L-образный арматурный стержень в выбранном структурном элементе.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Кольцевая арматура](Arch_Rebar_Stirrup/ru.md): Создает кольцевой арматурный стержень в выбранном структурном элементе.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Изогнутая арматура](Arch_Rebar_BentShape/ru.md): Создает изогнутый арматурный стержень в выбранном структурном элементе.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Спиральная арматура](Arch_Rebar_Helical/ru.md): Создает спиральный арматурный стержень в выбранном структурном элементе.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Армировать колонну](Arch_Rebar_ColumnReinforcement/ru.md): Добавляет арматуру внутрь указанной прямоугольной колонны.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [Армировать балку](Arch_Rebar_BeamReinforcement/ru.md): Добавляет арматуру внутрь указанной балки.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_Slab_Reinforcement.svg  style="width:32px;"> [Армировать плиту](Arch_Rebar_Slab_Reinforcement/ru.md): Добавляет арматуру внутрь указанной плиты.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width:32px;"> [Армировать фундамент](Arch_Rebar_Footing_Reinforcement/ru.md): Добавляет арматуру в указанный фундамент.


</div>

  - <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Арматура по эскизу](Arch_Rebar.md): Создает арматурный стержень в выбранном элементе конструкции по эскизу.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Светопрозрачный фасад](Arch_CurtainWall/ru.md): Создает светопрозрачный фасад с нуля или на основе выбранного объекта. {{Version/ru|0.19}}


</div>

-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Building Part](Arch_BuildingPart/ru.md): Создает часть здания, включающее выбранные объекты.

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Проект](Arch_Project/ru.md): Создает проект, включающий в себя выбранные объекты.

-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Местность](Arch_Site/ru.md): Создает участок, включающий в себя выбранные объекты.

-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Здание](Arch_Building/ru.md): Создает здание, включающее выбранные объекты.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Этаж](Arch_Floor/ru.md): Создает этаж, включающий выбранные объекты.

-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Reference](Arch_Reference/ru.md): Связывает объекты из другого файла FreeCAD с этим документом.

-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Окно](Arch_Window/ru.md): Создает окно используя выбранный объект в качестве основы.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Крыша](Arch_Roof/ru.md): Создает наклонную крышу от выбранной грани.

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Инструменты Осей](Arch_CompAxis/ru.md)

  - <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Оси](Arch_Axis/ru.md): Добавляет однонаправленный массив осей.

  - <img alt="" src=images/Arch_Axis_System.svg  style="width:32px;"> [Система осей](Arch_AxisSystem/ru.md): Добавляет в документ систему осей, состоящую из нескольких осей.

  - <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Сетка](Arch_Grid/ru.md): Добавляет в объект построенный по сетке из других объектов.

-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Сечение](Arch_SectionPlane/ru.md): Добавляет объект - секущую плоскость.

-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Пространство](Arch_Space/ru.md): Создаёт в объект - пространство.

-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Лестница](Arch_Stairs/ru.md): Создаёт в документе объект - лестницу.

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Инструменты панелирования](Arch_CompPanel/ru.md):

  - <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Панель](Arch_Panel/ru.md): Создает объект панель из выбранного 2D объекта.

  - <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Панельный контур](Arch_Panel_Cut/ru.md): Создает плоский контур из панели.

  - <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Панельный лист](Arch_Panel_Sheet/ru.md): Создает панельный лист для хранения панельных контуров и других плоских объектов.

  - <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Компоновка](Arch_Nest/ru.md): Позволяет оптимальным образом расположить несколько плоских объектов внутри определенной формы.

-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Оборудование](Arch_Equipment/ru.md): Создать объект техника (для комнаты) или мебель.

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Каркас](Arch_Frame/ru.md): Создает объект каркас из выбранного макета.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Ограждение](Arch_Fence/ru.md): Создаёт объект - ограждение из выбранных элементов и пути. {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Ферма](Arch_Truss/ru.md): Создает ферму по выбранному контуру или с нуля. {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profile](Arch_Profile/ru.md): Создает плоский параметрический профиль. {{Version/ru|0.19}}


</div>

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Инструменты материалов](Arch_CompSetMaterial/ru.md)

  - <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Material](Arch_SetMaterial.md): Creates a material and attributes it to selected objects, if any.

  - <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Multi-Material](Arch_MultiMaterial.md): Creates a multi-material and attributes it to selected objects, if any.

-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Schedule](Arch_Schedule.md): Creates different types of schedules.

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Инструменты для создания труб](Arch_CompPipe/ru.md)

  - <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Труба](Arch_Pipe/ru.md): Создает трубу.

  - <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Соединитель труб](Arch_PipeConnector/ru.md): Создает угловое или Т-образное соединение между двумя или тремя указанными трубами.



### Инструменты изменения 

Эти инструменты предназначены для изменения архитектурных объектов.

-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Обрезать плоскостью](Arch_CutPlane/ru.md): Обрезает объект по указанной плоскости.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Cut with line](Arch_CutLine.md): Cuts an object according to a line.

-   <img alt="" src=images/Arch_Add.png  style="width:32px;"> [Добавить компонент](Arch_Add/ru.md): Добавляет объекты к компоненту.

-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Удалить компонент](Arch_Remove/ru.md): Вычитает или удаляет объекты из компонента.

-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Анализ](Arch_Survey/ru.md): Переводит или выводит из режима анализа.



### Утилиты

Это дополнительные инструменты, которые помогут вам в решении конкретных задач.

-   <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Копмонент](Arch_Component/ru.md): Создает не параметрический архитектурный компонент из объекта верстака Part.

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Clone component](Arch_CloneComponent.md): Produces Arch Components that are clones of selected Arch objects (not to be confused with [Draft Clone](Draft_Clone.md)).

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Split Mesh](Arch_SplitMesh.md): Splits a selected mesh into separate components.

-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Mesh to Shape](Arch_MeshToShape.md): Converts a mesh into a shape, unifying coplanar faces.

-   <img alt="" src=images/Arch_SelectNonSolidMeshes.svg  style="width:32px;"> [Select non-manifold meshes](Arch_SelectNonSolidMeshes.md): Selects all non-manifold meshes from the current selection or from the document.

-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Remove Shape from Arch](Arch_RemoveShape.md): Turns cubic shape-based Arch object fully parametric.

-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Close holes](Arch_CloseHoles.md): Closes holes in a selected shape-based object.

-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Объединить стены](Arch_MergeWalls/ru.md): Объединить две и более стены.

-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Check](Arch_Check.md): Check if the selected objects are solids and don\'t contain defects.

-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Toggle IFC Brep flag](Arch_ToggleIfcBrepFlag.md): Forces a selected object to be exported as an [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [3 Views from mesh](Arch_3Views.md): Creates top, front and side views from a [mesh](Mesh_Workbench.md).

-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Create IFC spreadsheet\...](Arch_IfcSpreadsheet.md): Creates a spreadsheet to store [IFC](Arch_IFC.md) properties of an object.

-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Toggle subcomponents](Arch_ToggleSubs.md): Shows or hides the subcomponents of an Arch object.



### Настройки

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [Настройки](Arch_Preferences/ru.md): предпочтения для стен, структур, арматуры, окон, лестниц, панелей, труб, сеток и осей.



### Форматы файлов 


<div class="mw-translate-fuzzy">

-   [IFC](Arch_IFC/ru.md) : Формат классов строительной индустрии (Industry Foundation Classes)
-   [DAE](Arch_DAE/ru.md) : Формат 3D моделей Collada
-   [OBJ](Arch_OBJ/ru.md) : Формат 3D моделей Obj (поддерживается только экспорт)
-   [JSON](Arch_JSON/ru.md) : Формат JavaScript Object Notation (поддерживается только экспорт)
-   [3DS](Arch_3DS/ru.md) : Формат 3DS (поддерживается только импорт)
-   [SHP](Arch_SHP/ru.md): GIS Shapefiles (поддерживается только импорт)


</div>

## API

Архитектурный верстак может быть задействован в [Python](Python/ru.md)-скриптах и [макросах](Macros/ru.md), посредством [Arch Python API](Arch_API/ru.md).



## Учебники

-   [Переход в FreeCAD из Revit](Migrating_to_FreeCAD_from_Revit/ru.md)
-   [Архитектурный рабочий процесс](http://yorik.uncreated.net/guestblog.php?tag=freecad): Пример начального использования FreeCAD в архитектурном процессе.
-   [Руководство по архитектурному верстаку Arch](Arch_tutorial/ru.md) (v. 0.14)
-   [Быстрый архитектурный обзор в блоге Yorik\'а](http://yorik.uncreated.net/guestblog.php?2012=180) (v. 0.13)
-   [Видео презентация верстака Arch](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Руководство по архитектурным панелям](Arch_panel_tutorial/ru.md) (v. 0.15)
-   [Глава моделирования BIM из руководства FreeCAD](Manual:BIM_modeling/ru.md)
-   [Импорт из STL или OBJ](Import_from_STL_or_OBJ/ru.md)
-   [Экспорт в STL или OBJ](Export_to_STL_or_OBJ/ru.md)



---
⏵ [documentation index](../README.md) > [Obsolete_Workbenches](Category_Obsolete_Workbenches.md) > Arch Workbench/ru
