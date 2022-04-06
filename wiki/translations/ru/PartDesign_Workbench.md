# <img alt="Логотип верстака PartDesign" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/ru


{{TOCright}}

## Введение

<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;">[Верстак PartDesign](PartDesign_Workbench/ru.md) предоставляет расширенные инструменты для моделирования сложных твердых деталей. Предназначен в основном для создания механических деталей, которые можно изготовить и собрать в готовый продукт. Тем не менее, созданные тела могут быть использованы в целом для любых других целей, таких как [архитектурный дизайн](Arch_Workbench/ru.md), [анализ методом конечных элементов](FEM_Workbench/ru.md), или [механическая обработка и 3D-печать](Path_Workbench/ru.md).

PartDesign Workbench неразрывно связан с [верстаком Sketcher](Sketcher_Workbench/ru.md). Пользователь обычно создает эскиз, затем использует инструмент [PartDesign Pad](PartDesign_Pad/ru.md) для его выдавливания и создания простого объемного тела, далее это тело дополнительно модифицируется.

В то время как <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Верстак \"Part\"](Part_Workbench/ru.md) основан на методологии [конструктивной сплошной геометрии](constructive_solid_geometry/ru.md) (CSG) для построения фигур, верстак PartDesign использует параметрическую методологию редактирования объектов, которая означает, что базовое твердое тело последовательно преобразуется путем добавления элементов от начала и до тех пор, пока не будет получена окончательная форма. Более полное объяснение данного процесса см. на странице [особенности редактирования компонентов](feature_editing/ru.md). Страница: [создание простой детали с помощью PartDesign](Creating_a_simple_part_with_PartDesign/ru.md), так же описывает процесс создание твердых тел.

Более подробное обсуждение различий между верстаком Part и верстаком Part Design можно найти на странице: [Part и Part Design](Part_and_PartDesign/ru.md).

Тела, созданные с помощью верстака PartDesign, достаточно часто сталкиваются с [проблемой назначения имени элементам топологии](Topological_naming_problem/ru.md), которая приводит к переименованию внутренних объектов при изменении параметрических операций. Эту проблему можно свести к минимуму, следуя рекомендациям, указаным на странице [с описанием особенностей редактирования компонентов](feature_editing/ru.md), а так же используя базовые (datum) объекты в качестве поддержки эскизов и компонентов.

<img alt="" src=images/PartDesign_Example.png  style="width:500px;">

## Инструменты

Все инструменты проектирования деталей находятся в меню **Part Design** и на панели инструментов PartDesign, которая появляется при загрузке рабочей среды проектирования деталей.

### Инструменты упорядочивания 

Данные инструменты на самом деле не являются частью верстака PartDesign. Они относятся к категории [стандартных команд и инструментов (Std)](Std_Base/ru.md). Они были разработаны в версии 0.17 с целью упорядочивания и создания [сборок](Assembly/ru.md); как таковые, они достаточно полезны при работе с телами, созданными с помощью этого верстака.

-   <img alt="" src=images/Std_Part.svg  style="width:32px;"> [Создать деталь](Std_Part/ru.md): создает новую Деталь в текущем документе и делает её активной.

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Создать группу](Std_Group/ru.md): создает в текужем документе объединяющий контейнер группу, что позволяет упорядочить объекты в [дереве просмотра](Tree_view.md).

### Вспомогательные инструменты Part Design 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Создать тело](PartDesign_Body/ru.md): создает объект [тело](Body/ru.md) и делает активным его в текущем документе.

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Создать эскиз](PartDesign_NewSketch/ru.md): создает новый эскиз на выбранной грани или плоскости. Если во время выполнения этого инструмента не выбрана ни одна из граней, пользователю будет предложено выбрать плоскость на панели Задач. После чего интерфейс переключится на [верстак \"Sketcher\"](Sketcher_Workbench/ru.md) в режим редактирования.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Редактировать эскиз](Sketcher_EditSketch/ru.md): Переключает интерфейс в режим редакктирования эскиза.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Разместить эскиз на грани](Sketcher_MapSketch/ru.md): Позволяет разместить эскиз на выбранной плоскости или грани активного тела.


</div>

### Инструменты моделирования Part Design 

#### Инструменты создания опорных элементов 

-   <img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Создать опорную точку](PartDesign_Point/ru.md): создает опорную точку в активном теле.

-   <img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Создать опорную линию](PartDesign_Line/ru.md): создает опорную линию в активном теле.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Создать опорную плоскость](PartDesign_Plane/ru.md): создает опорную плоскость в активном теле.

-   <img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Создать локальную систему координат](PartDesign_CoordinateSystem/ru.md): создает локальную систему координат прикрепленную к опорной геометрии в активном теле.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Создать связующую форму](PartDesign_ShapeBinder/ru.md): создает связующую форму в активном теле.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Создать связующую форму к подэлементу](PartDesign_SubShapeBinder/ru.md): создает связующую форму к подэлементу, например к краю или грани другого тела, сохраняя при этом относительное положение этого элемента.{{Version/ru|0.19}}


</div>

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Создать нового клона](PartDesign_Clone/ru.md): клонирует выбранное тело.

#### Инструменты добавления (наращивания) материала (Additive tools) 

Это инструменты для создания базовых элементов или добавления материала к существующему твердому телу.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Выдавить эскиз](PartDesign_Pad/ru.md): выдавливает форму из выбранного эскиза.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Фигура вращения](PartDesign_Revolution/ru.md): создает фигуру вращения, \"выдавливая\" эскиз вокруг оси. Контур эскиза должен быть замкнутым.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [Аддитивный профиль](PartDesign_AdditiveLoft/ru.md): создает переходную форму, между двумя и более переходными контурами.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [Аддитивная трубный профиль](PartDesign_AdditivePipe/ru.md): создает сплошное тело, перемещая один или несколько эскизов по конечной или замкнутой траектории.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Аддитивная спираль](PartDesign_AdditiveHelix/ru.md): создает сплошное тело, перемещая эскиз по спирали. {{Version/ru|0.19}}

-   <img alt="" src=images/PartDesign_CompPrimitiveAdditive.png  style="width:48px;"> [Создать аддитивный примитив](PartDesign_CompPrimitiveAdditive/ru.md): добавляет аддитивный примитив к активному телу.

:\*<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:32px;"> [Аддитивный куб](PartDesign_AdditiveBox/ru.md): создает аддитивный куб.

:\*<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [Аддитивный цилиндр](PartDesign_AdditiveCylinder/ru.md): создает аддитивный цилиндр.

:\*<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [Аддитивная сфера](PartDesign_AdditiveSphere/ru.md): создает аддитивную сферу.

:\*<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width:32px;"> [Аддитивный конус](PartDesign_AdditiveCone/ru.md): создает аддитивный конус.

:\*<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [Аддитивный эллипсоид](PartDesign_AdditiveEllipsoid/ru.md): создает аддитивный эллипсоид.

:\*<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [Аддитивный тор](PartDesign_AdditiveTorus/ru.md): создает аддитивный тор.

:\*<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [Аддитивная призма](PartDesign_AdditivePrism/ru.md): создает аддитивную призму.

:\*<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Аддитивный клин](PartDesign_AdditiveWedge/ru.md): создает аддитивный клин.

#### Инструменты вычитания (съёма) материала (Subtractive tools) 

Это инструменты для вычитания материала из существующего тела.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Вырез](PartDesign_Pocket/ru.md): создает вырез на основе выбранного эскиза.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Отверстие](PartDesign_Hole/ru.md): создает отверстия на основе выбранного эскиза. Эскиз должен содержать один или несколько кругов.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Проточка](PartDesign_Groove/ru.md): создает проточку, путем вращения эскиза вокруг оси.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [Субтрактивный профиль](PartDesign_SubtractiveLoft/ru.md): создает твердое тело путем перехода между двумя или более эскизами и вычитает созданное тело из активного тела.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Субтрактивный трубный профиль](PartDesign_SubtractivePipe/ru.md): создает твердое тело, перемещая один или несколько эскизов по конечному или замкнутому контуру, и вычитает созданное тело из активного тела.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Субтрактивная спираль](PartDesign_SubtractiveHelix/ru.md): создает сплошную форму, перемещая эскиз вдоль спирали и вычитает его из активного тела. {{Version/ru|0.19}}

-   <img alt="" src=images/PartDesign_CompPrimitiveSubtractive.png  style="width:48px;"> [Создать субтрактивный примитив](PartDesign_CompPrimitiveSubtractive/ru.md): создает субтрактивный примитив и отнимает его от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [Субтрактивный параллепипед](PartDesign_SubtractiveBox/ru.md): создает субтрактивный прямоугольный параллелепипед и отнимает его от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Субтрактивный цилиндр](PartDesign_SubtractiveCylinder/ru.md): создает субтрактивный цилиндр и отнимает его от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [Субтрактивная сфера](PartDesign_SubtractiveSphere/ru.md): создает субтрактивную сферу и отнимает её от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [Субтрактивный конус](PartDesign_SubtractiveCone/ru.md): создает субтрактивный конус и отнимает его от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [Субтрактивный эллипсоид](PartDesign_SubtractiveEllipsoid/ru.md): создает субтрактивный эллипсоид и отнимает его от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Субтрактивный тор](PartDesign_SubtractiveTorus/ru.md): создает субтрактивный тор и отнимает его от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Субтрактивная призма](PartDesign_SubtractivePrism/ru.md): создает субтрактивную призму и отнимает её от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Субтрактивный клин](PartDesign_SubtractiveWedge/ru.md): создает субтрактивный клин и отнимает его от активного тела.

#### Инструменты преобразования форм 

Это инструменты для преобразования существующих форм. Они позволят выбрать способы преобразования форм.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Симметрия](PartDesign_Mirrored/ru.md): создает один или несколько симметричных элементов.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Линейный массив](PartDesign_LinearPattern/ru.md): создает линейный массив на основе одной или нескольких заготовок.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Круговой массив](PartDesign_PolarPattern/ru.md): создает круговой массив на базе одной или нескольких заготовок.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Множественное преобразование](PartDesign_MultiTransform/ru.md): создает массив на основе разнообразных комбинаций преобразований массивов перечисленных выше.

#### Инструменты обработки граней тела 

Данные инструменты предназначены для создания кромок и обработки граней.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Скругление](PartDesign_Fillet/ru.md): скругление граней активного тела.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Фаска](PartDesign_Chamfer/ru.md): снимает фаску с граней активного тела.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Уклон](PartDesign_Draft/ru.md): создает уклон выбранных граней активного тела

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Полость](PartDesign_Thickness/ru.md): создает толстостенную полую оболочку из активного твердого тела и убирая выбранные грани.

#### Логические операции 

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Логическая операция](PartDesign_Boolean/ru.md): импортирует одно или несколько тел или клонов PartDesign в активное тело и применяет логическую операцию.

#### Дополнительные

Некоторые дополнительные функции в меню \"Part Design\":

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Миграция](PartDesign_Migrate.md): переносит файлы, созданные с помощью более старых версий FreeCAD. Если файл полностью основан на функциях PartDesign, миграция должна пройти успешно. Если файл содержит смешанные объекты Part/Part Design/Draft объекты, преобразование, скорее всего, завершится неудачно.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Мастер проектирования цепного колеса (звездочки)](PartDesign_Sprocket/ru.md): cоздает профиль цепного колеса (звездчки), который можно далее сделать объемным. {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_InternalExternalGear.svg  style="width:32px;"> [Мастер проектирования шестерни с эвольвентным профилем](PartDesign_InvoluteGear/ru.md): создает внутренний или наружный эвольвентный профиль шестерни, который можно далее сделать объемным.


</div>

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [Мастер проектирования вала](PartDesign_WizardShaft/ru.md): Создает вал из таблицы значений и позволяет анализировать силы и моменты. Вал создается как фигура вращения из эскиза, который можно редактировать.

### Инструменты контекстного меню 

<img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Установить конечную точку расчета](PartDesign_MoveTip/ru.md): переопределяет положение конечной точки расчета детали.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Переместить объект в другое тело](PartDesign_MoveFeature/ru.md): перемещает выбранный эскиз, базовой геометрии или объект в другое тело.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Переместить объект следом за другим объектом](PartDesign_MoveFeatureInTree/ru.md): позволяет изменить порядок операций в древе построения тела, с помощью перемещения выбранного эскиза, базовой геометрии или объекта в другое положение в списке операций.

#### Комманды, используемые совместно с верстаком Part 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Внешний вид](Std_SetAppearance/ru.md): определяет внешний вид всей детали (прозрачность, цвет и т.д.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Установить цвета](Part_FaceColors/ru.md): позволяет назначить цвета для граней детали.


<div class="mw-translate-fuzzy">

### Настройки


</div>

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Настройки](PartDesign_Preferences/ru.md): настройки, доступные для инструментов проектирования деталей.
-   [Точная настройка](Fine-tuning/ru.md): некоторые дополнительные параметры для точной настройки при проектировании деталей.

## Учебники

-   [Использование FreeCAD](http://help-freecad-jpg87.fr/), вебсайт, описывающий рабочий процесс проектирования механики.
-   [Создание простейшей детали с помощью PartDesign](Creating_a_simple_part_with_PartDesign/ru.md)
-   [Базовый учебник Part Design](Basic_Part_Design_Tutorial/ru.md)
-   [Учебник PartDesign Bearingholder I](PartDesign_Bearingholder_Tutorial_I/ru.md) (требует обновления)
-   [Учебник PartDesign Bearingholder II](PartDesign_Bearingholder_Tutorial_II/ru.md) (требует обновления)





 {{PartDesign_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > PartDesign Workbench/ru
