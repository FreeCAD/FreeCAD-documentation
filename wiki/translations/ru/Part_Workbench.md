# <img alt="Иконка верстака Part" src=images/Workbench_Part.svg  style="width:64px;"> Part Workbench/ru






## Введение


<div class="mw-translate-fuzzy">

Возможности твердотельного моделирования FreeCAD основаны на ядре [Технологии OpenCASCADE](OpenCASCADE/ru.md) (OCCT), CAD-системе профессионального уровня, в которой реализованы расширенные возможности создания и обработки трехмерной геометрии. <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Верстак Part](Part_Workbench/ru.md) - это слой, расположенный поверх библиотек OCCT, который даёт пользователю доступ к геометрическим примитивам и функциям OCCT. Практически все функции 2D- и 3D-проектирования в каждом верстаке (<img alt="" src=images/Workbench_Draft.svg  style="width:24px;">[Draft](Draft_Workbench/ru.md), <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/ru.md), <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/ru.md) и т.д.), основаны на этих функциях, предоставляемых Верстаком Part. Поэтому Верстак Part считается центральным компонентом возможностей моделирования FreeCAD.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The Part Workbench can also create objects that are not solids, such as faces, shells, and objects with only edges or vertices. It also provides a variety of general purpose tools for geometry manipulation, geometry validation, and making copies.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) uses an alternative workflow for creating solids. For a detailed discussion of the Part Workbench versus the Part Design Workbench see [Part and Part Design](Part_and_PartDesign.md).


</div>

![](images/Part_Workbench_Example.jpg )



## Инструменты


<div lang="en" dir="ltr" class="mw-content-ltr">

### Solids toolbar 


</div>

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Куб](Part_Box/ru.md): Создаёт твердотельный куб.

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Цилиндр](Part_Cylinder/ru.md): Создаёт твердотельный цилиндр.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Сфера](Part_Sphere/ru.md): Создаёт твердотельную сферу.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Конус](Part_Cone/ru.md): Создаёт твердотельный конус.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Тор](Part_Torus/ru.md): Создаёт твердотельный тор (кольцо).

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Полый цилиндр](Part_Tube/ru.md): Создаёт полый цилиндр.

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Примитивы](Part_Primitives/ru.md): Инструмент для создания одного из следующих примитивов:

  - <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Плоскость](Part_Plane/ru.md): Создаёт плоскость.

  - <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Куб](Part_Box/ru.md): Создаёт куб (параллепипед). Этот объект также может быть создан с помощью инструмента [Куб](Part_Box/ru.md).

  - <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Цилиндр](Part_Cylinder/ru.md): Создаёт цилиндр. Этот объект также может быть создан с помощью инструмента [Цилиндр](Part_Cylinder/ru.md).

  - <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Конус](Part_Cone/ru.md): Создаёт конус. Этот объект также может быть создан с помощью инструмента [Конус](Part_Cone/ru.md).

  - <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Сфера](Part_Sphere/ru.md): Создаёт сферу. Этот объект также может быть создан с помощью инструмента [Сфера](Part_Sphere/ru.md).

  - <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Эллипсоид](Part_Ellipsoid/ru.md): Создаёт эллипсоид.

  - <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Тор](Part_Torus/ru.md): Создаёт тор. Этот объект также может быть создан с помощью инструмента [Тор](Part_Torus/ru.md).

  - <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Призма](Part_Prism/ru.md): Создаёт призму.

  - <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Клин](Part_Wedge/ru.md): Создаёт клин.

  - <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Спираль винтовая](Part_Helix/ru.md): Создаёт винтовую спираль.

  - <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Спираль плоская](Part_Spiral/ru.md): Создаёт плоскую спираль.

  - <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Окружность](Part_Circle/ru.md): Создаёт круглое ребро.

  - <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Эллипс](Part_Ellipse/ru.md): Создаёт эллиптическое ребро.

  - <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Точка](Part_Point/ru.md): Создаёт точку (вершину).

  - <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Отрезок](Part_Line/ru.md): Создаёт отрезок (ребро).

  - <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Правильный Многоугольник](Part_RegularPolygon/ru.md): Создаёт правильный многоугольник.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Построитель](Part_Builder/ru.md): Создаёт формы из разнообразных примитивов.


<div lang="en" dir="ltr" class="mw-content-ltr">

### Part tools toolbar 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Create sketch](Sketcher_NewSketch.md): Creates a new sketch and opens the [Sketcher Dialog](Sketcher_Dialog.md) to edit it.


</div>

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Выдавить](Part_Extrude/ru.md): Выдавливает (вытягивает) плоские грани.

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Вращать](Part_Revolve/ru.md):Создаёт твёрдое тело, вращая объект (не твёрдое тело) вокруг оси.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Отразить зеркально](Part_Mirror/ru.md): Отражает выбранный объект относительно зеркальной плоскости.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Scale.svg  style="width:32px;"> [Scale](Part_Scale.md): Scales one or more shapes. <small>(v1.0)</small> 


</div>

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Скругление](Part_Fillet/ru.md): Закругляет края объекта.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Фаска](Part_Chamfer/ru.md): Делает фаску на рёбрах объекта.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Создать грань из ломанных](Part_MakeFace/ru.md): Создаёт грань из набора ломанных (рёбер или контуров).

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Линейчатая поверхность](Part_RuledSurface/ru.md): Создаёт линейчатую поверхность.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Лофт](Part_Loft/ru.md): Построение профиля методом перехода от одного эскиза к другому.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Развёртка](Part_Sweep/ru.md): Переносит (проецирует) один или несколько профилей вдоль траектории.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Разделить](Part_Section/ru.md): Обрезает объект по поверхности пересечения секущего объекта.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Поперечные сечения\...](Part_CrossSections/ru.md): Создаёт одно или несколько поперечных сечений через весь объект.

-   <img alt="" src=images/Part_Offset.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Offset:

  - <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [3D смещение](Part_Offset/ru.md): Строит поверхность, равноудалённую на заданном расстоянии, от поверхности оригинального объекта.

  - <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D смещение](Part_Offset2D/ru.md): Строит контур, равноудалённый на заданное расстояние, от оригинала или увеличивает/сжимает плоскую грань.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Толщина](Part_Thickness/ru.md): Делает твёрдое тело пустотелым.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Проекция на поверхность](Part_ProjectionOnSurface/ru.md): Проецирует логотип, текст или любую поверхность, контур или ребро на поверхность.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Установить цвета](Part_FaceColors/ru.md): Позволяет назначить цвета для граней детали.


</div>




<div class="mw-translate-fuzzy">

### Булевы операции 


</div>

-   <img alt="" src=images/Part_Compound.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Соединить:

  - <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Сделать соединение](Part_Compound/ru.md): Создаёт объект, соединяющий в себе выбранные объекты.


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Разъединить соединение](Part_ExplodeCompound/ru.md): Разъединяет ранее соединённые объекты.


</div>

  - <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width:32px;"> [Фильтр соединений](Part_Compound‏‎Filter/ru.md): Извлекает отдельные части из соединений.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Булевы](Part_Boolean/ru.md): Производит булевы (логические) операции над объектами.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Обрезать](Part_Cut/ru.md): Вырезает (вычитает) один объект из другого.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Объединить](Part_Fuse/ru.md): Объединяет (сплавляет) два объекта.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Пересечь](Part_Common/ru.md): Извлекает общую (пересекающуюся) часть двух объектов.


</div>

-   <img alt="" src=images/Part_JoinConnect.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Join:

  - <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Connect (Соединить)](Part_JoinConnect/ru.md): Соединяет полые объекты с усечением лишних внутренних поверхностей.

  - <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Embed (Внедрить)](Part_JoinEmbed/ru.md): Внедряет один полый объект в другой полый объект.

  - <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Cutout (Вырезать)](Part_JoinCutout/ru.md): Создаёт вырез в стенке полого объекта для другого полого объекта.

-   <img alt="" src=images/Part_BooleanFragments.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Split:

  - <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Логические(Булевы) фрагменты](Part_BooleanFragments/ru.md): Создаёт все фрагменты, которые могут быть получены булевыми операциями между объектами.

  - <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Разрезать на части](Part_SliceApart/ru.md): Разрезает и разбивает объект, путём его пересечения с другими объектами.

  - <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Обрезать](Part_Slice/ru.md): Обрезает объект, пересекая его с другими объектами образуя объединение.

  - <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [Булева XOR](Part_XOR/ru.md): Удаляет пространство, общее для пересекаемых объектов.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Проверка геометрии](Part_CheckGeometry/ru.md): Проверяет геометрию выбранных объектов на ошибки.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Удаление элемента](Part_Defeaturing/ru.md): Удаляет применённые функции (features) построения из объекта.



### Прочие инструменты 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Импорт CAD\...](Part_Import/ru.md): Импорт в текущий документ файлов типа \*.IGES, \*.STEP или \*.BREP.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Экспорт в CAD\...](Part_Export/ru.md): Экспортирует деталь в формат \*.IGES, \*.STEP или \*.BREP.


</div>

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Выделение прямоугольной область](Part_BoxSelection/ru.md): Позволяет выбирать грани прямоугольной областью.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Создание фигуры из полигональной сетки](Part_ShapeFromMesh/ru.md): Создаёт форму из сетки.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Points from mesh](Part_PointsFromMesh/ru.md): Создаёт фигуру из точек сетки плигонального объекта.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Преобразовать в твёрдое](Part_MakeSolid/ru.md): Преобразует форму в твёрдое тело.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_ReverseShape.svg  style="width:32px;"> [Reverse shapes (Обратная фигура)](Part_ReverseShape/ru.md): Переворачивает нормали всех поверхностей выбранного объекта.


</div>

-   Создать копию:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_SimpleCopy‎.svg  style="width:32px;"> [Создать простую копию](Part_SimpleCopy/ru.md): Создаёт простую копию выбранного объекта.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Создать преобразованную копию](Part_TransformedCopy/ru.md): Создаёт преобразованную копию выбранных объектов.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Создать копию элемента формы](Part_ElementCopy/ru.md): Создаёт копию только элементов, выбранного объекта (вершины, рёбра, грани).


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_RefineShape.png  style="width:32px;"> [Уточнить форму](Part_RefineShape/ru.md): Очищает поверхности детали и удаляет ненужные линии (так называемые \"артефакты\").


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Прикрепить (Attachment)](Part_EditAttachment/ru.md): Прикрепляет/фиксирует расположение одного объекта относительно другого.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Obsolete tools 


</div>



### Измерение


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Std_Measure.svg  style="width:32px;"> [Std Measure](Std_Measure.md) tool replaces the tools listed below. <small>(v1.0)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Измерить Длину](Part_Measure_Linear/ru.md) Создаёт линейное изменение.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Измерить Угол](Part_Measure_Angular/ru.md): Создаёт угловое измерение.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Обновить Измерение](Part_Measure_Refresh/ru.md): Обновляет все измерения.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Очистить Всё](Part_Measure_Clear_All/ru.md): Удаляет все измерения.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Переключить Всё](Part_Measure_Toggle_All/ru.md): Показать или скрыть все измерения.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width:32px;"> [Переключить 3D](Part_Measure_Toggle_3D/ru.md): Показать или скрыть трёхмерные измерения.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Переключить Дельту](Part_Measure_Toggle_Delta/ru.md): Показывает или скрывает результаты разностных измерений.


</div>



## Настройки


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferences](PartDesign_Preferences/ru.md): Настройки, доступные для Инструментов Part (верстака Part) также используются в настройках PartDesign.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Preferences](Import_Export_Preferences/ru.md): Настройки, доступные для импорта и экспорта в различные форматы файлов.
-   [Fine-tuning](Fine-tuning/ru.md): Некоторые дополнительные параметры для тонкой настройки поведения модуля Part.


</div>



## Программирование

Смотри [Создание сценариев (скриптов) модуля Part](Part_scripting/ru.md)



## Учебники

-   [Импорт из STL или OBJ](Import_from_STL_or_OBJ/ru.md) : Как импортировать файлы STL/OBJ в FreeCAD
-   [Экспорт в STL или OBJ](Export_to_STL_or_OBJ/ru.md) : Как экспортировать в FreeCAD файлы STL/OBJ
-   [Whiffle Ball (Шарик вдохновения) руководство](Whiffle_Ball_tutorial/ru.md) : Как использовать модуль Part



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Category_Part.md) > Part Workbench/ru
