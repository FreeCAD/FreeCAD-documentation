# <img alt="Логотип верстака PartDesign" src=images/Workbench_PartDesign.svg  style="width   *64px;"> PartDesign Workbench/ru


{{TOCright}}

## Введение

<img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;">[Верстак PartDesign](PartDesign_Workbench/ru.md) предоставляет расширенные инструменты для моделирования сложных твердотельных деталей. Он в основном ориентирован на создание механических деталей, которые можно изготовить и собрать в готовое изделие. Тем не менее, созданные твёрдые тела можно использовать повсеместно для любых других целей, таких как [архитектурное проектирование](Arch_Workbench/ru.md), [анализ методом конечных элементов](FEM_Workbench/ru.md) или [механическая обработка и 3D-печать](Path_Workbench/ru.md).

Верстак PartDesign неразрывно связан с [верстаком Sketcher](Sketcher_Workbench/ru.md). Пользователь обычно создаёт эскиз, затем использует инструмент [PartDesign выдавливание](PartDesign_Pad/ru.md) для создания простого твёрдого тела, которое в последующем модифицируется (изменяется).

В то время как <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Верстак Part](Part_Workbench/ru.md) основан на методологии [конструктивной сплошной геометрии](constructive_solid_geometry/ru.md) (CSG) для построения фигур, верстак PartDesign использует параметрическую методологию редактирования объектов, которая означает, что базовое твёрдое тело последовательно преобразуется путем добавления элементов от начала и до тех пор, пока не будет получена окончательная форма. Более полное объяснение данного процесса смотри на странице [особенности редактирования компонентов](feature_editing/ru.md). Более полное описание этого процесса смотри на странице [редактирования элементов](feature_editing/ru.md), а затем смотри [Создание простой детали с помощью PartDesign](Creating_a_simple_part_with_PartDesign/ru.md), чтобы приступить к созданию твёрдых тел.

Более подробное обсуждение различий между верстаками Part и Part Design можно найти на странице   * [Part и Part Design](Part_and_PartDesign/ru.md).

Тела, созданные с помощью верстака PartDesign, достаточно часто сталкиваются с [проблемой назначения имени элементам топологии](Topological_naming_problem/ru.md), которая приводит к переименованию внутренних объектов при изменении параметрических операций. Эту проблему можно свести к минимуму, следуя рекомендациям, указаным на странице [с описанием особенностей редактирования компонентов](feature_editing/ru.md), а так же используя опорные (datum) объекты в качестве поддержки эскизов и компонентов.

<img alt="" src=images/PartDesign_Example.png  style="width   *500px;">

## Инструменты

Все инструменты проектирования деталей находятся в меню **Part Design** и на панели инструментов Part Design, которая появляется при загрузке верстака Part Design.

### Инструменты структуры 

Эти инструменты на самом деле не являются частью верстака PartDesign. Они относятся к категории [Стандартных инструментов](Std_Base/ru.md). Они были разработаны в версии 0.17 с целью упорядочивания и создания [сборок](Assembly/ru.md); как таковые, они весьма полезны при работе с телами, созданными с помощью этого верстака.

-   <img alt="" src=images/Std_Part.svg  style="width   *32px;"> [Создать деталь](Std_Part/ru.md)   * создает новую Деталь в текущем документе и делает её активной.

-   <img alt="" src=images/Std_Group.svg  style="width   *32px;"> [Создать группу](Std_Group/ru.md)   * добавляет в текущий документ контейнер группы, который позволяет организовать объекты в [древовидном представлении](Tree_view.md).

### Вспомогательные инструменты Part Design 

-   <img alt="" src=images/PartDesign_Body.svg  style="width   *32px;"> [Создать тело](PartDesign_Body/ru.md)   * создаёт объект [Тело](Body/ru.md) и делает его активным.

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *32px;"> [Создать эскиз](PartDesign_NewSketch/ru.md)   * создаёт новый эскиз на выбранной грани или плоскости. Если во время выполнения этого инструмента не выбрана ни одна из граней, пользователю будет предложено выбрать плоскость на Панели задач. После чего интерфейс переключится на [верстак Sketcher](Sketcher_Workbench/ru.md) в режим редактирования.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width   *32px;"> [Редактировать эскиз](Sketcher_EditSketch/ru.md)   * редактировать выбранный эскиз.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width   *32px;"> [Разместить эскиз на грани](Sketcher_MapSketch/ru.md)   * сопоставляет эскиз с ранее выбранной плоскостью или гранью активного тела.

### Инструменты моделирования Part Design 

#### Инструменты создания опорных элементов 

-   <img alt="" src=images/PartDesign_Point.svg  style="width   *32px;"> [Создать опорную точку](PartDesign_Point/ru.md)   * создает опорную точку в активном теле.

-   <img alt="" src=images/PartDesign_Line.svg  style="width   *32px;"> [Создать опорный отрезок](PartDesign_Line/ru.md)   * создает опорный отрезок в активном теле.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width   *32px;"> [Создать опорную плоскость](PartDesign_Plane/ru.md)   * создает опорную плоскость в активном теле.

-   <img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width   *32px;"> [Создать локальную систему координат](PartDesign_CoordinateSystem/ru.md)   * создает локальную систему координат прикрепленную к опорной геометрии в активном теле.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width   *32px;"> [Создать связующую форму](PartDesign_ShapeBinder/ru.md)   * создаёт привязку формы, ссылающуюся на геометрию из одного родительского объекта.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width   *32px;"> [Создать новую под-объектную связующую форму](PartDesign_SubShapeBinder/ru.md)   * создаёт геометрию привязки формы из одного или нескольких родительских объектов. {{Version/ru|0.19}}

-   <img alt="" src=images/PartDesign_Clone.svg  style="width   *32px;"> [Создать клон](PartDesign_Clone/ru.md)   * клонирует выбранное тело.

#### Аддитивные инструменты 

Это инструменты для создания базовых конструктивных элементов или для добавления простых аддитивных геометрических форм к уже существующему твёрдому телу.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width   *32px;"> [Выдавливание](PartDesign_Pad/ru.md)   * выдавливает твёрдое тело из выбранного эскиза.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width   *32px;"> [Вращение](PartDesign_Revolution/ru.md)   * создаёт твёрдое тело, поворачивая эскиз вокруг оси. Контур эскиза должен быть замкнутым.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width   *32px;"> [Аддитивный профиль](PartDesign_AdditiveLoft/ru.md)   * создает переходную форму, между двумя и более переходными контурами.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width   *32px;"> [Аддитивный профиль по траектории](PartDesign_AdditivePipe/ru.md)   * создаёт твёрдое тело путем протягивания одного или нескольких эскизов вдоль открытой или замкнутой траектории.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width   *32px;"> [Аддитивная спираль](PartDesign_AdditiveHelix/ru.md)   * создает сплошное тело, перемещая эскиз по спирали. {{Version/ru|0.19}}

-   <img alt="" src=images/PartDesign_CompPrimitiveAdditive.png  style="width   *48px;"> [Создать аддитивный примитив](PartDesign_CompPrimitiveAdditive/ru.md)   * добавляет аддитивный примитив к активному телу.

   **<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width   *32px;"> [Аддитивный параллелепипед](PartDesign_AdditiveBox/ru.md)   * создаёт аддитивный параллелепипед.

   **<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width   *32px;"> [Аддитивный цилиндр](PartDesign_AdditiveCylinder/ru.md)   * создает аддитивный цилиндр.

   **<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width   *32px;"> [Аддитивная сфера](PartDesign_AdditiveSphere/ru.md)   * создает аддитивную сферу.

   **<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width   *32px;"> [Аддитивный конус](PartDesign_AdditiveCone/ru.md)   * создает аддитивный конус.

   **<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width   *32px;"> [Аддитивный эллипсоид](PartDesign_AdditiveEllipsoid/ru.md)   * создает аддитивный эллипсоид.

   **<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width   *32px;"> [Аддитивный тор](PartDesign_AdditiveTorus/ru.md)   * создает аддитивный тор.

   **<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width   *32px;"> [Аддитивная призма](PartDesign_AdditivePrism/ru.md)   * создает аддитивную призму.

   **<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width   *32px;"> [Аддитивный клин](PartDesign_AdditiveWedge/ru.md)   * создает аддитивный клин.

#### Инструменты вычитания (съёма) материала (Субтрактивные инструменты) 

Это инструменты для вычитания материала из существующего тела.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width   *32px;"> [Вырез](PartDesign_Pocket/ru.md)   * создает вырез на основе выбранного эскиза.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width   *32px;"> [Отверстие](PartDesign_Hole/ru.md)   * создает отверстия на основе выбранного эскиза. Эскиз должен содержать один или несколько кругов.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width   *32px;"> [Проточка](PartDesign_Groove/ru.md)   * создает проточку, путем вращения эскиза вокруг оси.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width   *32px;"> [Субтрактивный профиль](PartDesign_SubtractiveLoft/ru.md)   * создает твердое тело путем перехода между двумя или более эскизами и вычитает созданное тело из активного тела.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width   *32px;"> [Субтрактивный профиль по траектории](PartDesign_SubtractivePipe/ru.md)   * создает твердое тело, перемещая один или несколько эскизов по конечному или замкнутому контуру, и вычитает созданное тело из активного тела.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width   *32px;"> [Субтрактивная спираль](PartDesign_SubtractiveHelix/ru.md)   * создает сплошную форму, перемещая эскиз вдоль спирали и вычитает его из активного тела. {{Version/ru|0.19}}

-   <img alt="" src=images/PartDesign_CompPrimitiveSubtractive.png  style="width   *48px;"> [Создать субтрактивный примитив](PartDesign_CompPrimitiveSubtractive/ru.md)   * создает субтрактивный примитив и отнимает его от активного тела.

   **<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width   *32px;"> [Субтрактивный параллепипед](PartDesign_SubtractiveBox/ru.md)   * создает субтрактивный прямоугольный параллелепипед и отнимает его от активного тела.

   **<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width   *32px;"> [Субтрактивный цилиндр](PartDesign_SubtractiveCylinder/ru.md)   * создает субтрактивный цилиндр и отнимает его от активного тела.

   **<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width   *32px;"> [Субтрактивная сфера](PartDesign_SubtractiveSphere/ru.md)   * создает субтрактивную сферу и отнимает её от активного тела.

   **<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width   *32px;"> [Субтрактивный конус](PartDesign_SubtractiveCone/ru.md)   * создает субтрактивный конус и отнимает его от активного тела.

   **<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width   *32px;"> [Субтрактивный эллипсоид](PartDesign_SubtractiveEllipsoid/ru.md)   * создает субтрактивный эллипсоид и отнимает его от активного тела.

   **<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width   *32px;"> [Субтрактивный тор](PartDesign_SubtractiveTorus/ru.md)   * создает субтрактивный тор и отнимает его от активного тела.

   **<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width   *32px;"> [Субтрактивная призма](PartDesign_SubtractivePrism/ru.md)   * создает субтрактивную призму и отнимает её от активного тела.

   **<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width   *32px;"> ‎[Субтрактивный клин](PartDesign_SubtractiveWedge/ru.md)   * создает субтрактивный клин и отнимает его от активного тела.

#### Инструменты преобразования 

Это инструменты для преобразования существующих элементов.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width   *32px;"> [Симметрия](PartDesign_Mirrored/ru.md)   * зеркально отражает один или несколько элементов.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width   *32px;"> [Линейный массив](PartDesign_LinearPattern/ru.md)   * создаёт линейный массив из одного или нескольких элементов.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width   *32px;"> [Круговой массив](PartDesign_PolarPattern/ru.md)   * создаёт круговой массив из одного или нескольких элементов.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *32px;"> [Множественное преобразование](PartDesign_MultiTransform/ru.md)   * создаёт массив, комбинируя любое из вышеупомянутых преобразований, а также преобразование [Масштабирование](PartDesign_Scaled/ru.md).
    -   <img alt="" src=images/PartDesign_Scaled.svg  style="width   *32px;"> [Масштабирование](PartDesign_Scaled/ru.md)   * масштабирует один или несколько элементов. Этот инструмент недоступен как отдельный инструмент преобразования.

#### Инструменты обработки граней тела 

Данные инструменты предназначены для создания кромок и обработки граней.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width   *32px;"> [Скругление](PartDesign_Fillet/ru.md)   * скругление граней активного тела.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width   *32px;"> [Фаска](PartDesign_Chamfer/ru.md)   * снимает фаску с граней активного тела.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width   *32px;"> [Уклон](PartDesign_Draft/ru.md)   * создает уклон выбранных граней активного тела

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width   *32px;"> [Преобразовать в полое тело](PartDesign_Thickness/ru.md)   * создает толстостенную полую оболочку из активного твердого тела и убирая выбранные грани.

#### Логические операции 

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width   *32px;"> [Булева операция](PartDesign_Boolean/ru.md)   * импортирует одно или несколько тел или клонов PartDesign в активное тело и применяет логическую операцию.

#### Дополнительные

Некоторые дополнительные функции в меню \"Part Design\"   *

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width   *32px;"> [Миграция](PartDesign_Migrate/ru.md)   * переносит файлы, созданные с помощью более старых версий FreeCAD. Если файл полностью основан на функциях PartDesign, миграция должна пройти успешно. Если файл содержит смешанные объекты Part/Part Design/Draft объекты, преобразование, скорее всего, завершится неудачно.

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width   *32px;"> [Цепное колесо (звездочка)](PartDesign_Sprocket/ru.md)   * создает профиль цепного колеса (звездочки), который можно далее сделать объемным. {{Version/ru|0.19}}

-   <img alt="" src=images/PartDesign_InternalExternalGear.svg  style="width   *32px;"> [Шестерня с эвольвентным профилем](PartDesign_InvoluteGear/ru.md)   * создает внутренний или наружный эвольвентный профиль шестерни, который далее можно сделать объемным.

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width   *32px;"> [Мастер проектирования вала](PartDesign_WizardShaft/ru.md)   * Создает вал из таблицы значений и позволяет анализировать силы и моменты. Вал создается как фигура вращения из эскиза, который можно редактировать.

### Инструменты контекстного меню 

<img alt="" src=images/PartDesign_MoveTip.svg  style="width   *32px;"> [Установить конечную точку расчета](PartDesign_MoveTip/ru.md)   * переопределяет положение конечной точки расчета детали.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width   *32px;"> [Переместить объект в другое тело](PartDesign_MoveFeature/ru.md)   * перемещает выбранный эскиз, базовой геометрии или объект в другое тело.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width   *32px;"> [Переместить объект следом за другим объектом](PartDesign_MoveFeatureInTree/ru.md)   * позволяет изменить порядок операций в древе построения тела, с помощью перемещения выбранного эскиза, базовой геометрии или объекта в другое положение в списке операций.

#### Комманды, используемые совместно с верстаком Part 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width   *32px;"> [Внешний вид](Std_SetAppearance/ru.md)   * определяет внешний вид всей детали (прозрачность, цвет и т.д.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width   *32px;"> [Установить цвета](Part_FaceColors/ru.md)   * позволяет назначить цвета для граней детали.

## Настройки

-   <img alt="" src=images/Preferences-part_design.svg  style="width   *32px;"> [Настройки](PartDesign_Preferences/ru.md)   * настройки, доступные для инструментов проектирования деталей.
-   [Точная настройка](Fine-tuning/ru.md)   * некоторые дополнительные параметры для точной настройки при проектировании деталей.

## Учебники

-   [Использование FreeCAD](http   *//help-freecad-jpg87.fr/), вебсайт, описывающий рабочий процесс проектирования механики.
-   [Создание простейшей детали с помощью PartDesign](Creating_a_simple_part_with_PartDesign/ru.md)
-   [Базовый учебник Part Design](Basic_Part_Design_Tutorial/ru.md)
-   [Учебник PartDesign Bearingholder I](PartDesign_Bearingholder_Tutorial_I/ru.md) (требует обновления)
-   [Учебник PartDesign Bearingholder II](PartDesign_Bearingholder_Tutorial_II/ru.md) (требует обновления)





 {{PartDesign_Tools_navi}}

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > PartDesign Workbench/ru
