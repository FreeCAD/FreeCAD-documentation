# <img alt="Логотип верстака Sketcher" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/ru


{{TOCright}}

## Введение

<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Верстак Sketcher](Sketcher_Workbench/ru.md) FreeCAD, используется для создания 2D геометрии, предназначенной для дальнейшего использования в верстаках: <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/ru.md), <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench/ru.md), и других. Плоский двухмерный эскиз является основой для построения большинства CAD моделей, поскольку 2D-эскиз можно «выдавливать» для создания объемных фигур; 2D-эскизы могут быть использованы для создания других элементов, таких как вырезы, выступы или \"надстройки\" поверх ранее построенных объемных фигур. Вместе с логическими операциями, перечисленными в <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [верстаке Part](Part_Workbench/ru.md), Sketcher формирует основу [конструктивной геометрии](constructive_solid_geometry/ru.md) (CSG) построения твердых тел. Более того, вместе с операциями <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [верстака PartDesign](PartDesign_Workbench/ru.md), Sketcher так же формирует основы методов [функционального редактирования](feature_editing/ru.md) при создании твердых тел.

Функции \"ограничения\" верстака Sketcher, позволяют задавать фигурам точные геометрические размеры определяя длины, углы и отношения (горизонтальность, вертикальность, перпендикулярность и т. д.). Решатель \"ограничений\" в интерактивном режиме обсчитывает ограничения степеней свободы геометрии эскиза.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*Так выглядит полностью ограниченный эскиз*

## О предназначении ограничений в эскизах 

Чтобы объяснить, как работает Sketcher, будет полезно сравнить его с \"традиционным\" способами черчения.

#### Традиционное черчение 

Системы Автоматизированного Проектирования (САПР) унаследовали традиционный способ черчения от старых [кульманов](https://ru.wikipedia.org/wiki/%D0%9A%D1%83%D0%BB%D1%8C%D0%BC%D0%B0%D0%BD_(%D1%87%D0%B5%D1%80%D1%82%D1%91%D0%B6%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82)). [Ортогональные (2D) проекции](http://en.wikipedia.org/wiki/Multiview_orthographic_projection) для создания технических чертежей (также известных как [\"синька\"](https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D0%BD%D1%8C%D0%BA%D0%B0_(%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F_%D1%87%D0%B5%D1%80%D1%82%D0%B5%D0%B6%D0%B0)) по англ. blueprints) чертились вручную. Объекты рисовались точно по предполагаемым размерам или габаритам. Если вы хотите нарисовать горизонтальную линию длиной 100 мм, начиная с координат (0,0), вы активируете инструмент линии, нажмите на экран или вводите координаты (0,0) для первой точки, затем нажимаете второй раз или вводите координаты второй точки (100,0). Или вы рисуете свою линию независимо от ее положения, а затем перемещаете ее. Когда вы закончите рисовать, вы добавляете размеры.

#### Эскизы построенные на ограничениях 

**Sketcher** исходит из логики, что объекты изначально не нужно рисовать абсолютно точно, потому что их размеры позже будут указаны с помощью ограничений. Изначально нарисованные Объекты не имеют ограичений, и, пока это так, они могут быть изменены. Иначе говоря, они находятся в \"свободном\" состоянии и их можно перемещать, растягивать, вращать, масштабировать и т. п. Это дает некоторую гибкость в процессе проектирования.

#### Что такое ограничения? 

Вместо размеров Ограничения используются для ограничения степеней свободы объекта. Например, линия без ограничений имеет 4 степени свободы (по англ. Degrees Of Freedom сокпащенно \"DOF\"): её можно перемещать по горизонтали или вертикали, можно растягивать и поворачивать.

Применение горизонтального или вертикального ограничения или углового ограничения (относительно другой линии или одной из осей) ограничит ее способность к вращению, оставляя таким образом 3 степени свободы. Блокировка одной из ее точек относительно начала координат устранит еще 2 степени свободы. А применение ограничения размером удалит последнюю степень свободы. Линия будет считаться **полностью ограниченной**.

Между собой могут быть ограничены и несколько объектов. Две линии могут быть объединены ограничением в их точке совпадения. Между ними может быть установлен угол или же они могут быть перпендикулярны. Линия может касаться дуги или круга и т.п. Сложный эскиз с несколькими объектами может иметь несколько различных решений, и его **полное ограничение** означает, что только одно из этих возможных решений было достигнуто на основе примененных ограничений.


<div class="mw-translate-fuzzy">

Существует два вида ограничений: геометрические и размерные. Они подробно описаны в разделе [Инструменты](#Инструменты.md) ниже.


</div>

### Для чего не стоит применять Sketcher 

Sketcher не предназначен для создания 2D чертежей. Когда эскизы используются для создания твердотельного элемента, они автоматически скрываются. Ограничения видны только в режиме редактирования эскиза.

Если вам нужны 2D виды только для печати, а не для создания 3D моделей, посмотрите на верстак [Draft](Draft_Workbench/ru.md). В отличии от элементов Sketcher-а (эскизы), объекты верстака Draft не используют ограничения; они являются простыми формами, определенными в момент создания. Как Draft так и Sketcher могут быть использованы для рисования 2D-геометрии и создания 3D-тел, хотя их предпочтительное использование отличается; Sketcher обычно используется совместно с верстаками [Part](Part_Workbench/ru.md) и [PartDesign](PartDesign_Workbench/ru.md) для создания твердых тел; Draft обычно используется для простых плоских рисунков поверх сетки, например при рисовании архитектурного плана этажа; в этих ситуациях Draft в основном используется вместе с [верстаком Arch](Arch_Workbench/ru.md). Инструмент [Draft2Sketch](Draft_Draft2Sketch/ru.md) преобразует объекты Draft-а в объекты Sketch-ра, и наоборот; многие инструменты, для которых требуется ввод 2D-элементов, работают с любыми типоми объектов, поскольку внутреннее преобразование выполняется автоматически.

## Процесс создания эскиза 

Эскиз всегда двумерный (2D). Чтобы создать твердое тело, создается двухмерный эскиз с одной замкнутой областью, а затем либо Выдавливается или Вращается, чтобы добавить 3-е измерение, создавая трехмерное тело из двухмерного эскиза.

Если в эскизе есть сегменты, которые пересекают друг друга, места, где точка не находится непосредственно на сегменте, или места, где есть промежутки между конечными точками смежных сегментов, Выдавливание или Вращение не будет создавать твердое тело. Иногда эскиз, содержащий линии, пересекающие друг друга, позволит сработать такой простой операции, как Выдавливание, но последующие операции, такие как Линейный Массив, не будут выполнены. Лучше избегать пересечения линий. Исключением для этих правил является Вспомогательная (синяя) геометрии, к которой они не применимы.

Внутри замкнутой области мы можем иметь меньшие непересекающиеся области. Они станут пустотами при создании 3D-тела.

Когда эскиз будет полностью ограничен, функции эскиза станут зелеными, а построительная геометрия останется синей. Обычно он «готов» и подходит для использования при создании трехмерного тела. Однако после закрытия диалогового окна «Эскиз» может оказаться целесообразным перейти к <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [верстаку Part](Part_Workbench/ru.md) и запустить команду **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Проверка геометрии](Part_CheckGeometry/ru.md)**, чтобы убедиться, что в Sketch нет элементов, которые могут вызвать дальнейшие проблемы.


<div class="mw-translate-fuzzy">

## Инструменты


</div>

Все инструменты верстака Sketcher находятся в меню Sketch, которое появляется при загрузке верстака Sketcher.

### Общее

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Создать эскиз](Sketcher_NewSketch/ru.md): Создать новый эскиз на выбранной грани или плоскости. Если во время использования этого инструмента грань не выбрана, пользователю, во всплывающем окне, предлагается выбрать плоскость.

-   <img alt="" src=images/Sketcher_EditSketch.svg‎‎  style="width:32px;"> [Редактировать эскиз](Sketcher_EditSketch/ru.md): Редактировать выбранный эскиз. Это откроет окно [Меню Sketcher](Sketcher_Dialog/ru.md)

-   <img alt="" src=images/Sketcher_LeaveSketch.svg‎‎  style="width:32px;"> [Покинуть эскиз](Sketcher_LeaveSketch/ru.md): Выйти из режима редактирования эскиза.

-   <img alt="" src=images/Sketcher_ViewSketch.svg‎‎  style="width:32px;"> [Обзор эскиза](Sketcher_ViewSketch/ru.md): Установить вид модели перпендикулярно плоскости эскиза.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Обзор сечения](Sketcher_ViewSection/ru.md): Создать плоскость сечения, которая временно скрывает любое содержимое перед плоскостью эскиза.

-   <img alt="" src=images/Sketcher_MapSketch.svg‎‎  style="width:32px;"> [Разместить эскиз на грани](Sketcher_MapSketch/ru.md): Сопоставить эскиз с ранее выбранной гранью или телом.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Переориентировать эскиз](Sketcher_ReorientSketch/ru.md): Позволяет прикрепить эскиз к одной из основных плоскостей.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Проверить эскиз](Sketcher_ValidateSketch/ru.md): Проверить отклонения различных точек и настроить их.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [Объединить эскизы](Sketcher_MergeSketches/ru.md): Объединить два или более эскиза.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [Отразить эскиз](Sketcher_MirrorSketch/ru.md): Зеркально отразить эскиз вдоль оси x, оси y или относительно нормали.

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Остановить операцию](Sketcher_StopOperation/ru.md): В режиме редактирования остановить текущую операцию, будь то рисование, установка ограничений и т. д.

### Геометрия эскиза 

Эти инструменты предназначенные для создания объектов.

-   <img alt="" src=images/Sketcher_CreatePoint.svg‎‎  style="width:32px;"> [Точка](Sketcher_CreatePoint/ru.md): Рисует точку.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Линия](Sketcher_CreateLine/ru.md): Рисует линию по двум точкам. Линии бесконечны относительно определенных ограничений.

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width:48px;"> [Создать дугу](Sketcher_CompCreateArc/ru.md): Данный элемент панели инструментов Sketcher, является меню и содержит следующие команды:

:\* <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Дуга](Sketcher_CreateArc/ru.md): Рисует сегмент дуги задав центр, радиус, начальный угол и конечный угол.

:\* <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Дуга по 3 точкам](Sketcher_Create3PointArc/ru.md): Рисует сегмент дуги по двум конечным точкам и точке на окружности.

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:48px;"> [Создать окружность](Sketcher_CompCreateCircle/ru.md): Данный элемент панели инструментов Sketcher, является меню и содержит следующие команды:

:\* <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Создать окружность](Sketcher_CreateCircle/ru.md): Рисует окружность от центра по величине радиуса.

:\* <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Создать окружность по трём точкам](Sketcher_Create3PointCircle/ru.md): Рисует окружность по 3-м точкам на грани окружности.

-   <img alt="" src=images/Sketcher_CompCreateConic.png  style="width:48px;"> [Создать коническое сечение](Sketcher_CompCreateConic/ru.md): Sketcher обеспечивает следующие конические сечения. В отличие от B-сплайнов они могут использоваться со всеми видами ограничений, такими как [касательные](Sketcher_ConstrainTangent/ru.md), [точки на объекте](Sketcher_ConstrainPointOnObject/ru.md) или [перпендикуляры](Sketcher_ConstrainPerpendicular/ru.md).
    -   <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Эллипс от центра](Sketcher_CreateEllipseByCenter/ru.md): Рисует эллипс по центральной точке, точке большого радиуса и точке малого радиуса.
    -   <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Эллипс по 3 точкам](Sketcher_CreateEllipseBy3Points/ru.md): Рисует эллипс по большому диаметру (2 точки) и малому радиусу.
    -   <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Дуга эллипса](Sketcher_CreateArcOfEllipse/ru.md): Рисует дугу эллипса от центральной точки, главной точки радиуса, начальной и конечной точкам.
    -   <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Дуга гиперболы](Sketcher_CreateArcOfHyperbola/ru.md): Рисует дугу гиперболы.
    -   <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Дуга параболы](Sketcher_CreateArcOfParabola/ru.md): Рисует дугу параболы.

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width:48px;"> [Нарисовать B-сплайн](Sketcher_CompCreateBSpline/ru.md): Данный элемент панели инструментов Sketcher, является меню и содержит следующие команды:
    -   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [Создать B-сплайн](Sketcher_CreateBSpline/ru.md): Рисует B-сплайн по его контрольным точкам.
    -   <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Создать периодический B-сплайн](Sketcher_CreatePeriodicBSpline/ru.md): Рисует периодическую (замкнутую) кривую B-сплайна по контрольным точкам.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Полилиния (линия состоящая из нескольких ребер)](Sketcher_CreatePolyline/ru.md): Рисует полилинию, состоящую из нескольких отрезков. Нажатие клавиши М во время рисования Полилинии переключает ее между различными режимами рисования.


</div>

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width:48px;"> [Создать прямоугольник](Sketcher_CompCreateRectangles/ru.md): Данный элемент панели инструментов Sketcher, является меню и содержит следующие команды: {{Version/ru|0.20}}

:\* <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Прямоугольник](Sketcher_CreateRectangle/ru.md): Рисует прямоугольник по 2-ум противоположным точкам.

:\* <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Создать прямоугольник](Sketcher_CreateRectangle_Center/ru.md): Рисует прямоугольник по центральной и крайней точкам. {{Version/ru|0.20}}

:\* <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Скругленный прямоугольник](Sketcher_CreateOblong/ru.md): Рисует cкругленный прямоугольник по двум точкам. {{Version/ru|0.20}}

-   <img alt="" src=images/Sketcher_CompCreateRegularPolygon.png  style="width:48px;"> [Создать правильный многоугольник](Sketcher_CompCreateRegularPolygon/ru.md): Данный элемент панели инструментов Sketcher, является меню и содержит следующие команды:

:\* <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Треугольник](Sketcher_CreateTriangle/ru.md): Рисует правильный треугольник, вписанный в круг вспомогательной геометрии.

:\* <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Квадрат](Sketcher_CreateSquare/ru.md): Рисует правильный квадрат, вписанный в круг вспомогательной геометрии.

:\* <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Пятиугольник](Sketcher_CreatePentagon/ru.md): Рисует правильный пятиугольник, вписанный в круг вспомогательной геометрии.

:\* <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Шестиугольник](Sketcher_CreateHexagon/ru.md): Рисует правильный шестиугольник, вписанный в круг вспомогательной геометрии.

:\* <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Семиугольник](Sketcher_CreateHeptagon/ru.md): Рисует правильный семиугольник, вписанный в круг вспомогательной геометрии.

:\* <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Восьмиугольник](Sketcher_CreateOctagon/ru.md): Рисует правильный восьмиугольник, вписанный в круг вспомогательной геометрии.

:\* <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Создать правильный многоугольник](Sketcher_CreateRegularPolygon/ru.md) : Рисует правильный многоугольник выбрав количество сторон и две точки: центральную и крайнюю.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Паз](Sketcher_CreateSlot/ru.md): Рисует овал, выбрав центр одного полукруга и конечную точку другого полукруга.

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Фаска](Sketcher_CreateFillet/ru.md): Создать фаску между двумя линиями, соединенными в одной точке. Выберите обе линии или нажмите на угловую точку, затем активируйте инструмент.

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Обрезать](Sketcher_Trimming/ru.md): Обрезать линию, окружность или дугу до точки пересечения.

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Продлить](Sketcher_Extend/ru.md): Продлить линию или дугу до линии границы, дуги, эллипса, эллиптической дуги или точки в пространстве.

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Разделить ребро](Sketcher_Split/ru.md): Разделяет линию или дугу на две части или преобразует окружность в две дуги, сохраняя при этом большинство ограничений. {{Version/ru|0.20}}

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Внешняя Геометрия](Sketcher_External/ru.md): Создать ребро, связанное с внешней геометрией.

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Структурная Копия](Sketcher_CarbonCopy/ru.md): Копировать геометрию из другого эскиза.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Вспомогательный режим](Sketcher_ToggleConstruction/ru.md): Переключить эскиз в режим вспомогательной геометрии. Вспомогательная геометрия показана синим цветом и скрывается вне режима редактирования эскиза.

### Ограничения Sketcher-а 

Ограничения используются для задания длин, задания правил взаимодействия между элементами эскиза, для блокировки эскиза по вертикальным и горизонтальным осям. Некоторые ограничения требуют использования [Вспомогательных ограничений](Sketcher_helper_constraint/ru.md).

#### Геометрические ограничения 

Эти ограничения не связаны с числовыми данными.

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Совпадение](Sketcher_ConstrainCoincident/ru.md): Прикрепляет точку к (Совпадает с) одной или нескольким другим точкам.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Точка на Объекте](Sketcher_ConstrainPointOnObject/ru.md): Прикрепляет точку к другому объекту, такому как линия, дуга или ось.

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Вертикаль](Sketcher_ConstrainVertical/ru.md): Ориентирует выбранные линии или полилинии вертикально и ограничить их. Перед применением этого ограничения можно выбрать более одного объекта.

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Горизонталь](Sketcher_ConstrainHorizontal/ru.md): Ориентирует выбранные линии или полилинии горизонтально и ограничить их. Перед применением этого ограничения можно выбрать более одного объекта.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Параллельность](Sketcher_ConstrainParallel/ru.md): Ограничивает две или более линии, параллельные друг другу.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Перпендикулярность](Sketcher_ConstrainPerpendicular/ru.md): Ограничивает две линии, перпендикулярные друг другу, или ограничить линию, перпендикулярную конечной точке дуги.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Касательная](Sketcher_ConstrainTangent/ru.md): Создает касательную и ограничение между двумя выбранными объектами, или коллинеарное ограничение между двумя линиями. Линия не обязательно должна лежать непосредственно на дуге или окружности, чтобы быть ограниченной касательной к этой дуге или окружности.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Равенство](Sketcher_ConstrainEqual/ru.md): Создает ограничение равенства двух выбранных объектов. При использовании на кругах или дугах их радиусы будут равны.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Симметричность](Sketcher_ConstrainSymmetric/ru.md): Создает симметрию и ограничение между двумя точками относительно линии или между двумя точками относительно третьей выбранной точки.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Заблокировать](Sketcher_ConstrainBlock/ru.md): Блокирует перемещение ребра, то есть предотвращает изменение текущего положения его вершин. Это может быть очень полезно для фиксации позиций В-сплайнов. Смотрите ветку форума [Block Constraint forum topic](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572).

#### Ограничения размерности 

Ограничения данного вида, имеют поля с числовыми значениями, для которых вы можете использовать [математические выражения](Expressions/ru.md). Данные также могут быть взяты из [электронных таблиц](Spreadsheet_Workbench/ru.md).

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Зафиксировать](Sketcher_ConstrainLock/ru.md): Ограничивает выбранный элемент, устанавливая вертикальные и горизонтальные расстояния относительно начала координат, тем самым фиксируя местоположение этого элемента. Позже эти ограничения расстояния могут быть отредактированы.

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Горизонтальное расстояние](Sketcher_ConstrainDistanceX/ru.md): Фиксирует горизонтальное расстояние между двумя точками или конечными точками линии. Если выбран только один элемент, то расстояние устанавливается относительно начала координат.

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Вертикальное расстояние](Sketcher_ConstrainDistanceY/ru.md): Фиксирует вертикальное расстояние между двумя точками или конечными точками линии. Если выбран только один элемент, то расстояние устанавливается относительно начала координат.

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Расстояние](Sketcher_ConstrainDistance/ru.md): Задает размер выбранной линии, ограничивая ее длину, или задает расстояние между двумя точками, ограничивая по расстоянию между ними.

-   <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Радиус](Sketcher_ConstrainRadius/ru.md): Задает радиус выбранной дуги или круга, ограничивая его.
-   <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Диаметр](Sketcher_ConstrainDiameter/ru.md): Задает диаметр выбранной дуги или окружности заданием ограничения радиуса.
-   <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Радиус/диаметр](Sketcher_ConstrainRadiam/ru.md): Автоматический задает радиус/диаметр выбранной дуги или окружности (вес для полюса B-сплайна, диаметр для полного круга, радиус для дуги) {{Version/ru|0.20}}
-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Внутренний угол](Sketcher_ConstrainAngle/ru.md): Задает внутренний угол между двумя выбранными линиями.

#### Особые ограничения 

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Закон Снелла](Sketcher_ConstrainSnellsLaw/ru.md): Ограничивает две линии подчиняя их закону преломления для имитации света, проходящего через поверхность.

-   <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:32px;"> [Привязать к внутренней геометрии](Sketcher_ConstrainInternalAlignment/ru.md): Выравнивает выбранные элементы в выбранной фигуре (например линия, которая должна стать главной осью эллипса).

#### Инструменты ограничений 

Для изменения степеней ограничений можно использовать следующие инструменты:

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Переключить ограничения в построительные/основные](Sketcher_ToggleDrivingConstraint/ru.md): Переключает панель инструментов или выбранные ограничения в/из вспомогательного режима.

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Вкл/Выкл ограничение](Sketcher_ToggleActiveConstraint/ru.md): Включить или отключить уже выставленное ограничение. {{Version/ru|0.19}}

### Инструменты эскизов 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Подсветить элементы со степенями свободы](Sketcher_SelectElementsWithDoFs/ru.md): Подсвечивает зеленую геометрию имеющую степени свободы, т.е. не полностью ограниченную.

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Завершить фигуру](Sketcher_CloseShape/ru.md): Создает замкнутую фигуру, применяя ограничение совпадения к конечным точкам.

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Соединить ребра](Sketcher_ConnectLines/ru.md): Соединяет элементы эскиза применяя ограничение совпадения к конечным точкам.

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Выбрать Ограничения](Sketcher_SelectConstraints/ru.md): Выбирает Ограничения элементов эскиза.

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Выбрать элементы, связанные с ограничениями](Sketcher_SelectElementsAssociatedWithConstraints/ru.md): Выбирает элементы эскиза, связанные с ограничениями.

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Выбрать Избыточные Ограничения](Sketcher_SelectRedundantConstraints/ru.md): Выбирает избыточные ограничения эскиза.

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Выбрать конфликтующие ограничения](Sketcher_SelectConflictingConstraints/ru.md): Выбирает конфликтующие ограничения эскиза.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Показать/Скрыть внутреннюю геометрию](Sketcher_RestoreInternalAlignmentGeometry/ru.md): Восстанавливает отсутствующую/удаленную внутреннюю геометрию выбранного эллипса, дуги эллипса/гиперболы/параболы или B-сплайна.

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Выбрать начало координат](Sketcher_SelectOrigin/ru.md): Выбирает начало координат эскиза.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Выбрать вертикальную ось](Sketcher_SelectVerticalAxis/ru.md): Выбирает вертикальную ось эскиза.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Выбрать горизонтальную ось](Sketcher_SelectHorizontalAxis/ru.md): Выбирает горизонтальную ось эскиза.

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Симметрия](Sketcher_Symmetry/ru.md): Копирует элемент эскиза симметрично выбранной линии.

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Клонировать](Sketcher_Clone/ru.md): Клонирует элемент эскиза.

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Копия](Sketcher_Copy/ru.md): Копирует элемент эскиза.

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Перемещение](Sketcher_Move/ru.md): Перемещает выбранную геометрию, используя в качестве ссылки последнюю выбранную точку.

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Прямоугольный массив](Sketcher_RectangularArray/ru.md): Создает массив из выбранных элементов эскиза.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Удалить выравнивание осей](Sketcher_RemoveAxesAlignment/ru.md): Удаляет выравнивание осей, пытаясь по возможности сохранить связь ограничения перпендикулярности и эквивалентности ребер. {{Version/ru|0.20}}

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Удалить всю геометрию](Sketcher_DeleteAllGeometry/ru.md): Удаляет всю геометрию из эскиза.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Удалить все Ограничения](Sketcher_DeleteAllConstraints/ru.md): Удаляет все ограничения из эскиза.

### Инструменты эскизов для B-сплайн-ов 

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Показать/Скрыть степень B-сплайна](Sketcher_BSplineDegree/ru.md)

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Показать/Скрыть полигон управления B-сплайном](Sketcher_BSplinePolygon/ru.md)

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Показать/Скрыть кривую B-сплайна](Sketcher_BSplineComb/ru.md)

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Показать/Скрыть узлы сопряжения B-сплайнов](Sketcher_BSplineKnotMultiplicity/ru.md)

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Показть/скрыть контрольную точку веса B-сплайна](Sketcher_BSplinePoleWeight/ru.md), {{Version/ru|0.19}}

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Преобразовать геометрию в B-сплайн](Sketcher_BSplineApproximate/ru.md)

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Увеличить степень B-сплайна](Sketcher_BSplineIncreaseDegree/ru.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Уменьшить степень B-сплайна](Sketcher_BSplineDecreaseDegree/ru.md), {{Version/ru|0.19}}

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Увеличить количество узлов сопряжения B-сплайна](Sketcher_BSplineIncreaseKnotMultiplicity/ru.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Уменьшить количество узлов сопряжения B-сплайна](Sketcher_BSplineDecreaseKnotMultiplicity/ru.md)

### Виртуальное пространство эскиза 

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Переключатель Виртуального Пространства](Sketcher_SwitchVirtualSpace/ru.md): Позволяет «скрыть» все ограничения эскиза и сделать их снова видимыми.


<div class="mw-translate-fuzzy">

### Настройки


</div>

-   <img alt="" src=images/Preferences-general.svg  style="width:32px;"> [Настройки](Sketcher_Preferences/ru.md): Настройки для верстака **Sketcher**.

## Лучшие Приемы Работы 

Каждый пользователь САПР со временем разрабатывает свой собственный способ работы, но есть несколько полезных общих принципов, которым нужно следовать.

-   Набором простых эскизов управлять легче, чем одним сложным. Например, первый эскиз может быть создан для применения 3D операции (такой как выдавливание или вращение), а второй может содержать отверстия или вырезы. Некоторые детали могут быть опущены, чтобы позднее быть реализованными 3D-операциями. Вы можете избегать скруглений в эскизе, если их слишком много, и добавить их позднее 3D-операцией.
-   Всегда создавайте закрытый контур, иначе из эскиза не получится твердое тело, а только набор открытых граней. Если вы не хотите, чтобы некоторые элементы были включены в создание твердого тела, включите их в состав вспомогательных элементов конструкции с помощью инструмента Вспомогательный режим.
-   Используйте функцию Авто Ограничения, чтобы уменьшить количество ограничений, которые вам нужно будет добавить вручную.
-   Как правило, сначала используются геометрические ограничения, затем размерные ограничения, последним и заблокировав эскиз. Но помните: правила созданы для того, чтобы их нарушать. Если вам трудно манипулировать эскизом, может быть полезно сначала ограничить несколько объектов, прежде чем закончить свой контур.
-   Если возможно, отцентрируйте эскиз по отношению к началу координат (0,0) с помощью фиксирующего ограничения. Если ваш эскиз не симметричный, расположите одну из его точек в начале координат или выберите хорошие круглые числа для фиксации расстояний. Начиная с версии v0.12 внешние ограничения (ограничивающие эскиз по отношению к существующей трехмерной геометрии, такой как ребра или другие эскизы) неприменимы. Это означает, что для размещения следующей геометрии эскиза по отношению к первому эскизу, вам необходимо вручную задать расстояния до первого эскиза. Фиксирующее ограничение (25,75) относительно начала координат легче запомнить, чем (23,47,73.02).
-   Если у вас есть возможность выбора между ограничением длины и ограничением горизонтального или вертикального расстояния, предпочтите последнее. Ограничения горизонтального и вертикального расстояния в вычислительном отношении дешевле.
-   В общем, лучшие ограничения для использования это: Горизонтальное и Вертикальное; Горизонтальное и Вертикальное ограничение длины; Совпадение Точка к Точке. Если возможно, ограничьте использование этих: Общее Ограничение Длинны (Расстояние); Совпадение Ребро к Ребру; Фиксация точки на Ограничении Линии; Ограничение Симметрии.
-   Если вы сомневаетесь в достоверности эскиза после его завершения (элементы становятся зелеными), закройте диалоговое окно Sketcher, переключитесь на верстак <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/ru.md) и запустите инструмент **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Проверка геометрии](Part_CheckGeometry/ru.md)**.

## Уроки

-   [Урок по Sketcher](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) от chrisb. Это большой 70-ти страничный PDF документ который служит подробным руководством по Sketcher. В нем объясняются основы использования Sketcher и подробно рассказывается о создании геометрических фигур и каждом из ограничений.
-   [Базовые уроки по Sketcher](Basic_Sketcher_Tutorial/ru.md) для начинающих
-   [Мини Урок по Sketcher - Ограничения на практике](Sketcher_Micro_Tutorial_-_Constraint_Practices/ru.md)
-   [Sketcher requirement for a sketch](Sketcher_requirement_for_a_sketch/ru.md) Минимальные требования для эскиза и полного определения эскиза.

## Программирование

Страница [программирование в Sketcher](Sketcher_scripting/ru.md) содержит в себе примеры создания различных ограничений через скрипты Python.





{{Sketcher Tools navi

}} 

[<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md)

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/ru
