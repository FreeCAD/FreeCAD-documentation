




<img alt="Иконка верстак Part" src=images/Workbench_Part.svg  style="width:128px;">


{{TOCright}}

## Введение

Возможности твердотельного моделирования FreeCAD основаны на ядре [Технологии OpenCASCADE](OpenCASCADE/ru.md) (OCCT), профессиональной САПР-системы, которая обеспечивает создание 3D-геометрии и манипулирование ею с помощью **функций** (features). <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Верстак Part](Part_Workbench/ru.md) - это слой, расположенный поверх библиотек OCCT, который даёт пользователю доступ к геометрическим примитивам и функциям OCCT. По существу, все функции 2D и 3D проектирования в каждом верстаке (<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/ru.md), <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/ru.md), <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/ru.md) и т.д.), базируются на этих функциях, предоставляемых Верстаком Part. Поэтому Верстак Part считается центральным компонентом возможностей моделирования FreeCAD.

Более подробное обсуждение сравнения Верстака Part с Верстаком Part Design можно найти здесь: [Part и PartDesign](Part_and_PartDesign/ru.md)

Объекты, создаваемые верстаком Part относительно просты, они предназначены для использования в булевых операциях (объединения и вырезания) для построения более сложных фигур. **Эта парадигма моделирования известна как процесс [конструктивной блочной геометрии](Constructive_solid_geometry/ru.md) (CSG, КБГ), и это традиционная методология, используемая в ранних системах САПР.** С другой стороны, [верстак PartDesign](PartDesign_Workbench/ru.md) предлагает более современный процесс создания фигур: он использует параметрически заданные эскизы, которые выдавливаются для формирования базовых твёрдых тел, которые потом модифицируются параметрическими трансформациями ([функциями редактирования](feature_editing/ru.md)) до получения конечного объекта.

Объекты Part сложнее, чем сеточные объекты, создаваемые в [верстаке Mesh](Mesh_Workbench/ru.md), поскольку они дают более сложные операции вроде когерентных (взаимосвязанных) булевых операций, историю модификации и параметрическое поведение.

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">


*Верстак Part Workbench это базовый слой, предоставляющий чертёжные функции OCCT всем верстакам FreeCAD.*

## Инструменты

Инструменты модуля расположены в меню {{MenuCommand|Деталь}} или в меню {{MenuCommand|Measure}}.

### Примитивы

Эти инструменты создают примитивные объекты.

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Куб](Part_Box/ru.md): Создаёт твердотельный куб.

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Цилиндр](Part_Cylinder/ru.md): Создаёт твердотельный цилиндр.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Сфера](Part_Sphere/ru.md): Создаёт твердотельную сферу.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Конус](Part_Cone/ru.md): Создаёт твердотельный конус.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Тор](Part_Torus/ru.md): Создаёт твердотельный тор (кольцо).

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Труба](Part_Tube/ru.md): Создаёт твердотельную трубу. {{Version/ru|0.19}}

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Примитивы](Part_Primitives/ru.md): Инструмент для создания одного из следующих примитивов:
    -   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Плоскость](Part_Plane/ru.md): Создаёт плоскость.
    -   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> [Куб](Part_Box/ru.md): Создаёт куб (параллепипед). Этот объект также может быть создан с помощью инструмента <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Куб](Part_Box/ru.md).
    -   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> [Цилиндр](Part_Cylinder/ru.md): Создаёт цилиндр. Этот объект также может быть создан с помощью инструмента <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Цилиндр](Part_Cylinder/ru.md).
    -   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> [Конус](Part_Cone/ru.md): Создаёт конус. Этот объект также может быть создан с помощью инструмента <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Конус](Part_Cone/ru.md).
    -   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> [Сфера](Part_Sphere/ru.md): Создаёт сферу. Этот объект также может быть создан с помощью инструмента <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Сфера](Part_Sphere/ru.md).
    -   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Эллипсоид](Part_Ellipsoid/ru.md): Создаёт эллипсоид.
    -   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> [Тор](Part_Torus/ru.md): Создаёт тор. Этот объект также может быть создан с помощью инструмента <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Тор](Part_Torus/ru.md).
    -   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Призма](Part_Prism/ru.md): Создаёт призму.
    -   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Клин](Part_Wedge/ru.md): Создаёт клин.
    -   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Спираль винтовая](Part_Helix/ru.md): Создаёт винтовую спираль.
    -   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Спираль плоская](Part_Spiral/ru.md): Создаёт плоскую спираль.
    -   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Окружность](Part_Circle/ru.md): Создаёт круглое ребро.
    -   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Эллипс](Part_Ellipse/ru.md): Создаёт эллиптическое ребро.
    -   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Точка](Part_Point/ru.md): Создаёт точку (вершину).
    -   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Линия](Part_Line/ru.md): Создаёт линию (ребро).
    -   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Правильный Многоугольник](Part_RegularPolygon/ru.md): Создаёт правильный многоугольник.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Построитель](Part_Builder/ru.md): Создаёт формы из разнообразных примитивов.

### Создание и изменение {#создание_и_изменение}

Эти инструменты служат для создания новых и изменения существующих объектов.

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Выдавить](Part_Extrude/ru.md): Выдавливает (вытягивает) плоские грани.

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Вращать](Part_Revolve/ru.md):Создаёт твёрдое тело, вращая объект (не твёрдое тело) вокруг оси.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Зеркальное отражение](Part_Mirror/ru.md): Отражает выбранный объект относительно зеркальной плоскости.

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Скругление](Part_Fillet/ru.md): Закругляет края объекта.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Фаска](Part_Chamfer/ru.md): Делает фаску на рёбрах объекта.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Создать грань из ломанных](Part_MakeFace/ru.md): Создаёт грань из набора ломанных (рёбер или контуров). Доступно из меню {{MenuCommand|Деталь}} {{Version/ru|0.19}}.

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Линейчатая поверхность](Part_RuledSurface/ru.md): Создаёт линейчатую поверхность.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Лофт](Part_Loft/ru.md): Лофт (плавная трансформация) от одного профиля к другому.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Развёртка](Part_Sweep/ru.md): Переносит (проецирует) один или несколько профилей вдоль траектории.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Разделить](Part_Section/ru.md): Обрезает объект по поверхности пересечения секущего объекта.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Поперечные сечения\...](Part_CrossSections/ru.md): Создаёт одно или несколько поперечных сечений через весь объект.

-   <img alt="" src=images/Part_CompOffsetTools.png  style="width:48px;"> [Инструменты смещения](Part_CompOffsetTools/ru.md):
    -   <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [3D смещение](Part_Offset/ru.md): Строит поверхность, равноудалённую на заданном расстоянии, от поверхности оригинального объекта.
    -   <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D смещение](Part_Offset2D/ru.md): Строит контур, равноудалённый на заданное расстояние, от оригинала или увеличивает/сжимает плоскую грань.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Толщина](Part_Thickness/ru.md): Делает твёрдое тело пустотелым.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Проекция на поверхность](Part_ProjectionOnSurface/ru.md): Проецирует логотип, текст или любую поверхность, контур или ребро на поверхность. {{Version/ru|0.19}}

-   <img alt="" src=images/Part_Attachment.svg  style="width:32px;"> [Attachment (Прикрепить)](Part_Attachment/ru.md): Прикрепляет расположение одного объекта относительно другого.

### Булевы операции {#булевы_операции}

Следующие инструменты выполняют логические (Булевы) операции.

-   <img alt="" src=images/Part_CompCompoundTools.png  style="width:48px;"> [Соединить](Part_CompCompoundTools/ru.md):
    -   <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Сделать соединение](Part_Compound/ru.md): Создаёт объект, соединяющий в себе выбранные объекты.
    -   <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Разъединить соединение](Part_ExplodeCompound/ru.md): Разъединяет ранее соединённые объекты.
    -   <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width:32px;"> [Фильтр соединений](Part_Compound‏‎Filter/ru.md): Извлекает отдельные части из соединений.

-   <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Булевы](Part_Boolean/ru.md): Производит булевы (логические) операции над объектами.

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Обрезать](Part_Cut/ru.md): Вырезает (вычитает) один объект из другого.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Объединить](Part_Fuse/ru.md): Объединяет (сплавляет) два объекта.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Пересечь](Part_Common/ru.md): Извлекает общую (пересекающуюся) часть двух объектов.

-   <img alt="" src=images/Part_CompJoinFeatures.png  style="width:48px;"> [Соединить тонкостенные объекты](Part_CompJoinFeatures/ru.md): Создаёт сложные сопряжения для объектов со стенками (например, труб).
    -   <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Connect (Соединить)](Part_JoinConnect/ru.md): Соединяет тонкостенные объекты по внутренней поверхности.
    -   <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Embed (Внедрить)](Part_JoinEmbed/ru.md): Внедряет один тонкостенный объект в другой тонкостенный объект.
    -   <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Cutout (Вырезать)](Part_JoinCutout/ru.md): Создаёт вырез в стенке тонкостенного объекта для другого тонкостенного объекта.

-   <img alt="" src=images/Part_CompSplittingTools.png  style="width:48px;"> [Инструменты разделения](Part_CompSplittingTools/ru.md):
    -   <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Логические(Булевы) фрагменты](Part_BooleanFragments/ru.md): Создаёт все фрагменты, которые могут быть получены булевыми операциями между объектами.
    -   <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Разрезать на части](Part_SliceApart/ru.md): Разрезает и разбивает объект, путём его пересечения с другими объектами.
    -   <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Обрезать](Part_Slice/ru.md): Обрезает объект, пересекая его с другими объектами образуя объединение.
    -   <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [Булева XOR](Part_XOR/ru.md): Удаляет пространство, общее для пересекаемых объектов (обратная версия [Обрезать](Part_Cut/ru.md)).

### Измерение

<img alt="" src=images/Part_Measure_Menu.png  style="width:64px;"> [Measure](Part_Measure_Menu/ru.md): Инструменты для линейных и угловых измерений.

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Measure Linear (Линейные измерения)](Part_Measure_Linear/ru.md) Делает линейные изменения.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Measure Angular (Угловые измерения)](Part_Measure_Angular/ru.md): Делает угловые измерения.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Measure Refresh (Обновить измерения)](Part_Measure_Refresh/ru.md): Обновляет все измерения.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Clear All(Удалить всё)](Part_Measure_Clear_All/ru.md): Удаляет все измерения.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Toggle All (Переключить всё)](Part_Measure_Toggle_All/ru.md): Показать или скрыть все измерения.

-   <img alt="" src=images/Part_Measure_Toggle_3d.svg  style="width:32px;"> [Toggle 3D (Переключить 3D)](Part_Measure_Toggle_3d/ru.md): Показать или скрыть трёхмерные измерения.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Toggle Delta (Переключить координаты)](Part_Measure_Toggle_Delta/ru.md): Показывает или скрывает измерения в ортогональной системе.

### Прочие инструменты {#прочие_инструменты}

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Импорт CAD\...](Part_Import/ru.md): Импорт в текущий документ файлов типа \*.IGES, \*.STEP или \*.BREP.

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Экспорт в CAD\...](Part_Export/ru.md): Экспортирует деталь в формат \*.IGES, \*.STEP или \*.BREP.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Выделить область](Part_BoxSelection/ru.md): Позволяет выбирать грани прямоугольной областью.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Создание фигуры из полигональной сетки](Part_ShapeFromMesh/ru.md): Создаёт форму из сетки.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Points from mesh](Part_PointsFromMesh/ru.md): Создаёт фигуру из точек сетки плигонального объекта.{{Version/ru|0.19}}

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Преобразовать в твёрдое](Part_MakeSolid/ru.md): Преобразует форму в твёрдое тело.

-   <img alt="" src=images/Part_ReverseShapes.svg  style="width:32px;"> [Reverse shapes (Обратная фигура)](Part_ReverseShapes/ru.md): Переворачивает нормали всех поверхностей выбранного объекта.

-   создать копию:
-   <img alt="" src=images/Part_SimpleCopy‎.svg  style="width:32px;"> [Create simple copy (Создать простую копию)](Part_SimpleCopy/ru.md): Создаёт простую копию выбранного объекта.
    -   <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Create transformed copy (Создать преобразованную копию)](Part_TransformedCopy/ru.md): Создаёт преобразованную копию выбранных объектов. {{Version/ru|0.19}}
    -   <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Create shape element copy (Создать копию формы)](Part_ElementCopy/ru.md): Создаёт копию только элементов, выбранного объекта (вершины, рёбра, грани) . {{Version/ru|0.19}}
-   <img alt="" src=images/Part_RefineShape.png  style="width:32px;"> [Уточнить форму](Part_RefineShape/ru.md): Очищает поверхности и удаляет ненужные линии (так называемые \"артефакты\").

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Проверка геометрии](Part_CheckGeometry/ru.md): Проверяет геометрию выбранных объектов на ошибки.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Удаление элемента](Part_Defeaturing/ru.md): Удаляет применённые функции (features) построения из объекта.

### Элементы контекстного меню {#элементы_контекстного_меню}

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Внешний вид\...](Std_SetAppearance/ru.md): Определяет внешний вид всего объекта (цвет, прозрачность и т.д.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Set colors (Установить цвета)](Part_FaceColors/ru.md): Задаёт цвет отдельным граням объекта.

## Настройки

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferences](PartDesign_Preferences/ru.md): Настройки, доступные для Инструментов Part (верстака Part) также используются в настройках PartDesign.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Preferences](Import_Export_Preferences/ru.md): Настройки, доступные для импорта и экспорта в различные форматы файлов.
-   [Fine-tuning](Fine-tuning/ru.md): Некоторые дополнительные параметры для тонкой настройки поведения модуля Part.

## Написание сценариев {#написание_сценариев}

Смотри [Создание сценариев (скриптов) модуля Part](Part_scripting/ru.md)

## Учебники

-   [Импорт из STL или OBJ](Import_from_STL_or_OBJ/ru.md) : Как импортировать файлы STL/OBJ в FreeCAD
-   [Экспорт в STL или OBJ](Export_to_STL_or_OBJ/ru.md) : Как экспортировать в FreeCAD файлы STL/OBJ
-   [Whiffle Ball (Шарик вдохновения) руководство](Whiffle_Ball_tutorial/ru.md) : Как использовать модуль Part





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
