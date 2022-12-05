# Manual:All workbenches at a glance/ru
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC/ru}}

Главная сложность новых пользователей FreeCAD - узнать, в каком верстаке найти нужный инструмент. Расположенная ниже таблица даст Вам обзор наиболее важных верстаков и их инструментов. Более полный список [верстаков](Workbenches/ru.md) смотрите в документации FreeCAD.

Четыре верстака так же разработаны для работы в парах, и один из них полностью включён в другой: верстак Arch содержит все инструменты Draft, а PartDesign - все инструменты Sketcher. Тем не менее, они разделены ниже для ясности.

### Верстак Part 

Верстак Part предоставляет базовые инструменты для работы с твердотельными частями: примитивами, такими как кубы или сферы, и простыми геометрическими и булевыми операциями. Будучи основной точкой привязки к [OpenCasCade](https://ru.wikipedia.org/wiki/Open_Cascade_Technology), верстак Part обеспечивает основу геометрической системы FreeCAD, и почти все другие верстаки производят геометрию, базируемую на Part.


<div class="mw-translate-fuzzy">

  Инструмент                                                                                                        Описание                                                        Инструмент                                                                                                         Описание
     
  <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Box](Part_Box/ru.md)                                        Рисует параллелепипед                                           <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone/ru.md)                                     Рисует конус
  <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder/ru.md)                    Рисует цилиндр                                                  <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere/ru.md)                             Рисует сферу
  <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus/ru.md)                                Рисует тор (кольцо)                                             <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Create primitives](Part_Primitives/ru.md)      Создаёт различные параметрические примитивы по выбору
  <img alt="" src=images/Part_Shapebuilder.svg  style="width:32px;"> [Shape builder](Part_Builder/ru.md)        Создаёт сложные формы из примитивов                             <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Union](Part_Fuse/ru.md)                                    Объединяет два объекта
  <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Common](Part_Common/ru.md)                            Выделяет общую часть (пересечение) двух объектов                <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Cut](Part_Cut/ru.md)                                         Вычитает один объект из другого
  <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [JonConnect](Part_JoinConnect/ru.md)         Соединяет внутренности объектов со стенками                     <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [JoinEmbed](Part_JoinEmbed/ru.md)                 Внедряет один объект со стенками в другой аналогичный
  <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Join Cutout](Part_JoinCutout/ru.md)           Создаёт вырез в стене объекта для другого объекта со стенками   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrude](Part_Extrude/ru.md)                         Выдавливает планарные грани объекта
  <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Fillet](Part_Fillet/ru.md)                            Скругляет рёбра объекта                                         <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Revolve](Part_Revolve/ru.md)                         Создаёт твёрдое тело поворотом другого объекта (не твердотельного) вокруг оси
  <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Section](Part_Section/ru.md)                        Создаёт сечение объекта секущей плоскостью                      <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [SectionCross](Part_SectionCross/ru.md)   Создаёт несколько пересечений объекта
  <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chamfer](Part_Chamfer/ru.md)                        Создаёт скос (фаску) граней объекта                             <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Mirror](Part_Mirror/ru.md)                             Отражает выбранный объект заданной отражающей плоскостью
  <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Ruled Surface](Part_RuledSurface/ru.md)   Создаёт линейную поверхность между выбранными кривыми           <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Sweep](Part_Sweep/ru.md)                                 Протягивает один или несколько профилей вдоль трассы
  <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Part Loft](Part_Loft/ru.md)                               Создаёт объект через операцию лофтинга между двумя профилями    <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [Offset](Part_Offset/ru.md)                             Создаёт увеличенную копию оригинального объекта
  <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Thickness](Part_Thickness/ru.md)                Назначает толщину граням формы                                                                                                                                                     


</div>

### Верстак Draft 

Верстак Draft обеспечивает инструменты для базовых задач двумерных САПР: линии, окружности и так далее, и серия общеупотребительных инструментов вроде перемещения, вращения или масштабирования. Он так же обеспечивает несколько вспомогательных инструментов, вроде сетки и привязки. Это принципиально означает рисовать направляющие для архитектурных объектов, но так же служит \"швейцарским ножом\" для FreeCAD .


<div class="mw-translate-fuzzy">

  Инструмент                                                                                                             Описание                                                           Инструмент                                                                                                        Описание
     
  <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Line](Draft_Line/ru.md)                                      Рисует отрезок между двумя точками                                 <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Wire](Draft_Wire/ru.md)                                 Рисует линию, составленную из нескольких линейных сегментов (полилиния)
  <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Circle](Draft_Circle/ru.md)                              Рисует окружность по центру и радиусу                              <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arc](Draft_Arc/ru.md)                                     Рисует сегмент дуги по центру, радиусу, начальному и конечному углу
  <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;">[Ellipse](Draft_Ellipse/ru.md)                           Рисует эллипс по двум угловым точкам                               <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygon](Draft_Polygon/ru.md)                     Рисует правильный многоугольник по центру и радиусу
  <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectangle](Draft_Rectangle/ru.md)                  Рисует прямоугольник по двум противоположным точкам                <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text/ru.md)                                 Рисует многострочную текстовую аннотацию
  <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension/ru.md)                  Рисует размерные линии                                             <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [BSpline](Draft_BSpline/ru.md)                     Рисует B-сплайн из последовательности точек
  <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Point](Draft_Point/ru.md)                                  Вставляет одиночную точку                                          <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Shapestring](Draft_ShapeString/ru.md)     Вставляет сложную форму, представляющую собой текстовую строку в заданной точке текущего документа
  <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Facebinder](Draft_Facebinder/ru.md)              Создаёт новый объект из выбранных граней существующих объектов     <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Bezier Curve](Draft_BezCurve/ru.md)             Рисует кривую Безье по последовательности точке
  <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Move](Draft_Move/ru.md)                                      Перемещает или копирует объекты из одного места в другое           <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Rotate](Draft_Rotate/ru.md)                         Вращает объекты на определённый угол вокруг точки
  <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Offset](Draft_Offset/ru.md)                              Создаёт смещение объекта на некоторую дистанцию                    <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trimex](Draft_Trimex/ru.md)                         Обрезает, удлиняет или вытягивает объект
  <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade/ru.md)                          Превращает или соединяет объекты в объекты более высокого уровня   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade/ru.md)             Превращает или разделяет объекты в объекты более низкого уровня
  <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scale](Draft_Scale/ru.md)                                  Масштабирует объекты относительно точки                            <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D View](Draft_Shape2DView/ru.md)   Создаёт двумерный объект с плоским видом другого объекта
  <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch/ru.md)   Преобразует объект Draft в объект Sketch (эскиз) и наоборот        <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Array](Draft_Array/ru.md)                             Создаёт из объекта полярный или прямоугольный массив
  <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray/ru.md)                 Создаёт массив из объекта, помещая его вдоль трассы                <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone/ru.md)                             Создаёт связанные копии объектов
  <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Mirror](Draft_Mirror/ru.md)                              Отражает объекты вдоль линии                                                                                                                                                         


</div>

### Верстак Sketcher 

Верстак Sketcher содержит инструменты для создания и редактирования сложных двумерных объектов, называемых эскизами (sketch). Геометрия внутри этих эскизов может быть точно позиционирована и связана использованием ограничений. Это создано в первую очередь для создания блоков в геометрии PartDesign, но может быть полезно в любом месте FreeCAD.


<div class="mw-translate-fuzzy">

  Инструмент                                                                                                                                                     Описание                                                                                                                                                                     Инструмент                                                                                                                                               Описание
     
  <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Point](Sketcher_CreatePoint/ru.md)                                               Рисует точку                                                                                                                                                                 <img alt="" src=images/Sketcher_Line.svg  style="width:32px;"> [Line](Sketcher_CreateLine/ru.md)                                                         Рисует отрезок по двум точкам
  <img alt="" src=images/Sketcher_Arc.svg  style="width:32px;"> [Arc](Sketcher_CreateArc/ru.md)                                                                   Рисует отрезок дуги по центру, радиусу, начальному и конечному углу                                                                                                          <img alt="" src=images/Sketcher_CreateArc3Point.png  style="width:32px;"> [Arc 3 points](Sketcher_Create3PointArc/ru.md)                      Рисует отрезок дуги по двум конечным точкам и третьей точке на окружности
  <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [Circle](Sketcher_CreateCircle/ru.md)                                                       Рисует окружность по центру и радиусу                                                                                                                                        <img alt="" src=images/Sketcher_CreateCircle3Point.png  style="width:32px;"> [ Circle 3 points](Sketcher_Create3PointCircle/ru.md)         Рисует окружность по трём точкам на ней
  <img alt="" src=images/Sketcher_CreateEllipse.svg  style="width:32px;"> [Ellipse](Sketcher_CreateEllipseByCenter/ru.md)                               Рисует эллипс по центральной точке, и точкам большого и малого радиуса                                                                                                       <img alt="" src=images/Sketcher_CreateEllipse3Point.png  style="width:32px;"> [Ellipse 3 points](Sketcher_CreateEllipseBy3Points/ru.md)   Рисует эллипс по главному диаметру (две точки) и точке малого радиуса
  <img alt="" src=images/Sketcher_CreateArcOfEllipse.png  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse/ru.md)                 Рисует дугу эллипса по центральной точке, точке большого радиуса и начальной и конечной точке                                                                                <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polyline](Sketcher_CreatePolyline/ru.md)                             Рисует линию, состоящую из нескольких отрезков. Доступно несколько режимов рисования
  <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rectangle](Sketcher_CreateRectangle/ru.md)                               Рисует прямоугольник по двум противоположным точкам                                                                                                                          <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Triangle](Sketcher_CreateTriangle/ru.md)                             Рисует равносторонний треугольник, вписанный в круг конструктивной геометрии
  <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Square](Sketcher_CreateSquare/ru.md)                                           Рисует равносторонний прямоугольник, вписанный в круг конструктивной геометрии                                                                                               <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pentagon](Sketcher_CreatePentagon/ru.md)                             Рисует равносторонний пятиугольник, вписанный в круг конструктивной геометрии
  <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Hexagon](Sketcher_CreateHexagon/ru.md)                                       Рисует равносторонний шестиугольник, вписанный в круг конструктивной геометрии                                                                                               <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Heptagon](Sketcher_CreateHeptagon/ru.md)                             Рисует равносторонний семиугольник, вписанный в круг конструктивной геометрии
  <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Octagon](Sketcher_CreateOctagon/ru.md)                                       Рисует равносторонний восьмиугольник, вписанный в круг конструктивной геометрии                                                                                              <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Slot](Sketcher_CreateSlot/ru.md)                                             Рисует овал выбором центра одного из полукругов и конечной точки другого полукруга
  <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Fillet](Sketcher_CreateFillet/ru.md)                                           Создаёт фаску между двумя отрезками, соединёнными в одной точками                                                                                                            <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Trimming](Sketcher_Trimming/ru.md)                                               Обрезает линию, окружность или дугу относительно указанной точки
  <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [External geometry](Sketcher_External/ru.md)                                            Создаёт грань, соединённую с внешней геометрией                                                                                                                              <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Construction mode](Sketcher_ToggleConstruction/ru.md)        Переключает элемент в/из конструктивного режима. Конструктивный объект не может использоваться в трёхмерной геометрии и видим только при редактировании содержащего его Эскиза
  <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [Point on point](Sketcher_ConstrainCoincident/ru.md)                        Поставить точку на (совпадающую с) одной или более точек                                                                                                                     <img alt="" src=images/Constraint_PointOnObject.svg  style="width:32px;"> [Point on object](Sketcher_ConstrainPointOnObject/ru.md)            Поставить точку на другой объект, как линия, дуга, или ось
  <img alt="" src=images/Constraint_Vertical.svg  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical/ru.md)                                        Ограничивает выбранные линии или элементы полилинии только вертикальной ориентацией. Перед установкой ограничения может быть выделено несколько объектов.                    <img alt="" src=images/Constraint_Horizontal.svg  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal/ru.md)                          Ограничивает выбранные линии или элементы полилинии только горизонтальной ориентацией. Перед установкой ограничения может быть выделено несколько объектов.
  <img alt="" src=images/Constraint_Parallel.png  style="width:32px;"> [Parallel](Sketcher_ConstrainParallel/ru.md)                                        Ограничивает две или более линий параллельностью к другой                                                                                                                    <img alt="" src=images/Constraint_Perpendicular.png  style="width:32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular/ru.md)              Ограничивает две линии перпендикулярностью одна другой, или ограничивает линию перпендикулярностью конечной точке дуги
  <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> [Tangent](Sketcher_ConstrainTangent/ru.md)                                            Creates a tangent constraint between two selected entities, or a co-linear constraint between two line segments.                                                             <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> [Equal length](Sketcher_ConstrainEqual/ru.md)                           Ограничивает два выбранных элемента равенством длинны. При применении к окружностям или дугам их радиусы будут равными.
  <img alt="" src=images/Constraint_Symmetric.png  style="width:32px;"> [Symmetric](Sketcher_ConstrainSymmetric/ru.md)                                    Ограничивает две точки симметричностью относительно линии, или ограничивает первые две выбранные точки симметрией относительно третьей точки                                 <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Lock](Sketcher_ConstrainLock/ru.md)                                    Ограничивает выбранные элементы установкой вертикальной и горизонтальной дистанции от базы, фиксируя их положение
  <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:32px;"> [Horizontal distance](Sketcher_ConstrainDistanceX/ru.md)        Фиксирует горизонтальную дистанцию между двумя точками или конечными точками линии. Если выбран только один элемент, расстояние устанавливается относительно нулевой точки   <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:32px;"> [Vertical distance](Sketcher_ConstrainDistanceY/ru.md)        Фиксирует вертикальную дистанцию между двумя точками или концами отрезка. Если выбран один элемент, дистанция устанавливается относительно нулевой точки
  <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Distance](Sketcher_ConstrainDistance/ru.md)                                            Назначает расстояние от выбранной линии ограничением их длинны, или определяет расстояние между двумя точками ограничением расстояния между ними.                            <img alt="" src=images/Constraint_Radius.png  style="width:32px;"> [Radius](Sketcher_ConstrainRadius/ru.md)                                          Определяет радиус выбранной дуги или окружности установкой ограничением радиуса
  <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> [Internal anglr](Sketcher_ConstrainAngle/ru.md)                           Определяет внутренний угол между двумя выбранными линиями                                                                                                                    <img alt="" src=images/Constraint_SnellsLaw.png  style="width:32px;"> [Snell\'s law](Sketcher_ConstrainSnellsLaw/ru.md)                           Ограничивает две линии подчинением закону рефракции для симуляции света, идущего через интерфейс
  <img alt="" src=images/Constraint_InternalAlignment.png  style="width:32px;"> [Internal alignment](Sketcher_ConstrainInternalAlignment/ru.md)   Выравнивает выбранные элементы по выбранной форме (например, линии, чтобы стать главной осью эллипса)                                                                        <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Map sketch](Sketcher_MapSketch/ru.md)                                          Располагает эскиз на заранее выбранной плоскости тела
  <img alt="" src=images/Sketcher_MergeSketch.svg  style="width:32px;"> [Merge](Sketcher_MergeSketches/ru.md)                                             Соединяет два или более эскиза                                                                                                                                               <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [Mirror](Sketcher_MirrorSketch/ru.md)                                     Отражает выбранные элементы эскиза


</div>

### Верстак PartDesign 

Верстак Part Design содержит инструменты для построения твердотельных частей. Он так же содержит все инструменты по работе с эскизами. Поскольку он может создавать только твёрдые тела (правило номер один Part Design), это главный верстак для использования частей для производства или трёхмерной печати, поскольку Вы всегда получите пригодный к печати объект.


<div class="mw-translate-fuzzy">

  Инструмент                                                                                                                              Описание                                                                     Инструмент                                                                                                                                 Описание
     
  <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Pad](PartDesign_Pad/ru.md)                                            Выдавливает твердотельный объект из выбранного эскиза                        <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Pocket](PartDesign_Pocket/ru.md)                                   Создаёт выемку из выбранного эскиза. Эскиз должен быть привязан к грани существующего объекта
  <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Revolution](PartDesign_Revolution/ru.md)                Создаёт твёрдое тело вращением эскиза вокруг оси                             <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Groove](PartDesign_Groove/ru.md)                                   Создаёт канавку вращением эскиза вокруг оси
  <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Fillet](PartDesign_Fillet/ru.md)                                Скругляет переход между гранями объекта                                      <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Chamfer](PartDesign_Chamfer/ru.md)                               Создаёт фаску на рёбрах объекта
  <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Draft](PartDesign_Draft/ru.md)                                    Применяет угловую вытяжку на грани объекта                                   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Mirrored](PartDesign_Mirrored/ru.md)                           Отражает элементы на плоскость или грань
  <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Linear pattern](PartDesign_LinearPattern/ru.md)   Создаёт линейный массив элементов                                            <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Polar pattern](PartDesign_PolarPattern/ru.md)          Создаёт круговой массив элементов
  <img alt="" src=images/PartDesign_Scaled.png  style="width:32px;"> [Scaled](PartDesign_Scaled/ru.md)                                Масштабирует элемент к другому размеру                                       <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Multitransform](PartDesign_MultiTransform/ru.md)   Позволяет создание элемента с любой комбинацией трансформаций
  <img alt="" src=images/PartDesign_WizardShaft.png  style="width:32px;"> [Shaft wizard](PartDesign_WizardShaft/ru.md)           Формирует вал из таблицы значений и позволяет анализировать силы и моменты   <img alt="" src=images/PartDesign_InvoluteGear.png  style="width:32px;"> [Involute gear wizard](PartDesign_InvoluteGear/ru.md)   Позволяет создавать различные типы редукторов


</div>

### Верстак Arch 

Верстак Arch содержит инструменты для работы с проектами на основе [BIM](https://ru.wikipedia.org/wiki/BIM) (промышленно-гражданское строительство и архитектура). Он так же содержит все инструменты верстака Draft. Основное использование верстака Arch в создании объектов BIM или добавлении атрибутов BIM к объектам, созданным с помощью других верстаков, чтобы экспортировать их в [IFC](https://ru.wikipedia.org/wiki/Industry_Foundation_Classes).

  Инструмент                                                                                           Описание                                                                       Инструмент                                                                                                        Описание
     
  <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Wall](Arch_Wall/ru.md)                       Создаёт стену с нуля или с использованием выбранного объекта в качестве базы   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Structure](Arch_Structure/ru.md)                Создаёт структурный элемент с нуля или используя выбранный объект в качестве базы
  <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Rebar](Arch_Rebar/ru.md)                   Создаёт арматуру в выбранном структурном элементе                              <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Floor](Arch_Floor.md)                                   Создаёт пол, включающий выбранные объекты
  <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Building](Arch_Building/ru.md)       Создаёт здание, включающее выбранные объекты                                   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Site](Arch_Site/ru.md)                                    Создает стройплощадку, включающую выбранные объекты
  <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Window](Arch_Window/ru.md)               Создаёт окно с использованием выбранного объекта в качестве базы               <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Section plane](Arch_SectionPlane/ru.md)   Добавляет к документу секущую плоскость
  <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Axis](Arch_Axis/ru.md)                       Добавляет систему осей к документу                                             <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Roof](Arch_Roof/ru.md)                                    Создаёт покатую крышу из выбранной грани
  <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Space](Arch_Space/ru.md)                   Создаёт пространственный объект в документе                                    <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Stairs](Arch_Stairs/ru.md)                            Создаёт лестничный объект в документе
  <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panel](Arch_Panel/ru.md)                   Создаёт панель из выбранного плоского объекта                                  <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Frame](Arch_Frame/ru.md)                                Создаёт рамочный объект из выбранной раскладки
  <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Equipment](Arch_Equipment/ru.md)   Создаёт объект оборудования или мебели                                         <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Material](Arch_SetMaterial/ru.md)           Назначает материал к выбранному объекту
  <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Schedule](Arch_Schedule/ru.md)       Создаёт различные типы расписаний                                              <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Cut plane](Arch_CutPlane/ru.md)                   Обрезает объект в соответствии с планом
  <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Add](Arch_Add/ru.md)                           Добавляет объекты к компоненту                                                 <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Remove](Arch_Remove/ru.md)                            Вычитает или удаляет объекты из компонента
  <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Survey](Arch_Survey/ru.md)               Переходит в или покидает режим ревизии                                                                                                                                                           

### Верстак Drawing 


**Разработка [верстака Drawing](Drawing_Workbench/ru.md) остановлена в FreeCAD 0.16, а новый [верстак TechDraw](TechDraw_Workbench/ru.md), нацеленный на его замену, был представлен в v0.17. Верстак Drawing может быть удалён в будущих версиях. Вместо него используйте верстак TechDraw.**

Верстак Drawing поддерживает создание и обработку плоских чертёжных листов, используется для показа видов вашей трёхмерной работы на чертежах. Эти листы могут быть экспортированы в двумерные приложения в форматах SVG или DXF, в формат PDF, или распечатаны.


<div class="mw-translate-fuzzy">

  Инструмент                                                                                                             Описание                                                                       Инструмент                                                                                                         Описание
     
  <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [New sheet](Drawing_Landscape_A3/ru.md)   Создаёт новый чертёжный лист                                                   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [View](Drawing_View/ru.md)                            Вставляет вид выбранного объекта в активный чертёжный лист
  <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Annotation](Drawing_Annotation/ru.md)        Добавляет аннотацию к текущему чертёжному листу                                <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Clip](Drawing_Clip/ru.md)                            Добавляет разрез к текущему чертёжному листу
  <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Open browser](Drawing_Openbrowser/ru.md)   Открывает предпросмотр текущего листа в браузере                               <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Ortho views](Drawing_Orthoviews/ru.md)   Автоматически создаёт ортографическую проекцию объектов текущего чертёжного листа
  <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol/ru.md)                        Добавляет содержимое текущего файла SVG как символ в текущем чертёжном листе   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft view](Drawing_DraftView/ru.md)       Вставляет специальный вид Draft текущего объекта в текущий чертёжный лист
  <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save](Drawing_Save/ru.md)                                Сохраняет текущий лист в файл SVG                                                                                                                                                                 


</div>

### Прочие встроенные верстаки 

Хотя выше собраны наиболее важные инструменты FreeCAD, доступны многие другие верстаки, среди которых:


<div class="mw-translate-fuzzy">

-   [Верстак Mesh](Mesh_Workbench/ru.md) позволяет работать с [полигональными сетками](https://ru.wikipedia.org/wiki/Полигональная_сетка). Хотя сетки не лучший тип геометрии при работе с FreeCAD, из-за недостатка точности и поддержки кривых, сетки всё ещё полезны, и полностью поддерживаются в FreeCAD. Верстак Mesh так же предоставляет несколько инструментов трансляции деталей в сетки и обратно.
-   [Верстак Raytracing](Raytracing_Workbench/ru.md) предоставляет инструменты для взаимодействия с внешними визуализаторами, такими как povray или luxrender. Этот верстак позволяет создавать высококачественную отрисовку вашей модели прямо из FreeCAD.
-   [Верстак Spreadsheet](Spreadsheet_Workbench/ru.md) позволяет создавать и обрабатывать в электронных таблицах данные, которые могут быть выделены из моделей FreeCAD. Ячейки электронных таблиц могут ссылаться на многие области FreeCAD, позволяя использовать их как главные структуры данных.
-   [Верстак FEM](FEM_Workbench.md) работает с [анализом методом конечных элементов](https://ru.wikipedia.org/wiki/Метод_конечных_элементов), и позволяет выполнять предварительные и постпроцессорные вычисления для показа результатов графически.


</div>

### Внешние верстаки 

Существует несколько очень полезных верстаков, созданных членами сообщества FreeCAD. Хотя они и не включены в стандартную установку FreeCAD, их легко установить как плагины. Ссылки на них показаны в репозитории [дополнений FreeCAD](https://github.com/FreeCAD/FreeCAD-addons). Из наиболее завершённых в разработке:

-   [верстак Drawing Dimensioning](https://github.com/hamish2014/FreeCAD_drawing_dimensioning) предлагает много новых инструментов для работы прямо на чертёжных листах и позволяет добавлять размеры, аннотации и других технические символы с глубоким контролем над их аспектами. **Верстак Drawing Dimensioning больше не поддерживается.**
-   [Верстак Fasteners](https://github.com/shaise/FreeCAD_FastenersWB) обеспечивает широкий диапазон готовых к использованию крепёжных изделий вроде болтов, винтов, шпилек и болтов. Доступно множество опций и настроек.
-   Верстак [A2plus](https://github.com/kbwbe/A2plus) предлагает ряд инструментов для монтирования и работы со [сборками](https://ru.wikipedia.org/wiki/Сборочный_чертёж).

**Читать далее**


<div class="mw-translate-fuzzy">

-   [Полный список верстаков](Workbenches/ru.md)
-   [Верстак Part](Part_Workbench/ru.md)
-   [Верстак Draft](Draft_Workbench/ru.md)
-   [Верстак PartDesign и Sketcher](PartDesign_Workbench/ru.md)
-   [Верстак Arch](Arch_Workbench/ru.md)
-   [Верстак TechDraw](TechDraw_Workbench.md)
-   [Верстак FEM](FEM_Workbench/ru.md)
-   [Репозиторий расширений FreeCAD](https://github.com/FreeCAD/FreeCAD-addons)


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Manual:All workbenches at a glance/ru
