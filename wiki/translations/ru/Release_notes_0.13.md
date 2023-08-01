# Release notes 0.13/ru
Это обзор самых интересных изменений произошедших в последней версии FreeCAD. Смотри [полный список](http://www.freecadweb.org/tracker/changelog_page.php) для получения подробной информации об изменениях.


<div class="mw-translate-fuzzy">

Предыдущие версии: [0.12](Release_notes_0.12.md) - [0.11](Release_notes_0.11.md)


</div>

![800px](images/FreeCAD013.jpg)

*modeled in FreeCAD by psicofil*

## Основное

-   **Настройки цветов**: Вам надоели старые добрые серые формы с черными контурами установленные в FreeCAD по умолчанию? Теперь вы можете менять пользовательские предпочтения в настройках (Отобразить -\> Цвета), вместе с другими настройками цветов по умолчанию.

## Модуль создания проекций 

-   **Функция обрезки**: Новый инструмент [Обрезка изображения](Drawing_Clip.md) позволяет разместить проекции объектов внутри невидимого прямоугольника который обрежет границы изображения.
-   **Редактируемый штамп чертежа**: При проектировании [Чертежных Шаблонов](Drawing_templates.md), теперь можно отметить текст который будет редактируемым. Этот текст будет редактироваться напрямую в FreeCAD.
-   **Функция аннотации**: Новая функция [Аннотация](Drawing_Annotation.md) , простой инструмент для размещения блока текста на чертеже.

## Эскизный модуль 

**Улучшены Метки Данных и Отображение Ограничений:**

-   Каждая метка ограничения (включая стрелки) теперь корректно масштабируется по размеру сцены в 3D окне

-   Метки с текстовыми данными для Расстояние, Расстояние по X, Расстояние по Y и Радиус теперь можно вободно размещать.

-   Небольшие улучшения для иконок ограничения пересичения изаморозки.

-   Метка с текстовыми данными теперь переворачивается когда вид переориентируется на потивоположную сторону эскизав документ(трехмерная сцена а не лист чертежа). Вы можете указать направление вектора проекции.

Points can now be added and used as a feature within a sketch

-   **Sketch Origin**

![](images/Release-0.13-Origin.png )

User can now use the sketch\'s origin to define geometry as well as the sketch axes.

-   **Tangency and perpendicularity constraints for arcs and circles.**
-   **Constraints with respect to external (projected) geometry.**
-   **Improved counting of the sketch degrees of freedom.**
-   **Symmetry constraint with respect to a symmetry point** (midpoint constraint).

-   **Improved Datum Label and Constraint Visuals:**

![](images/Release-0.13-SketcherDimensions.png )

-   -   Each constraint label (including arrows) will correctly scale to the size of the scene automatically to the 3D viewport
    -   Datum label text for Distance, Distance X, Distance Y and Radius can be freely positioned now with greater control.
    -   Small improvements to overlapping constraint icons and fix freezes.
    -   Datum Label text will reverse when the view is orientated from the opposite side.

-   **Fully constrained Sketches are now highlighted:**

![The sketch color turns from white to green to indicate it is fully constrained. These default colors can be customized.](images/Release-0.13-SketcherFullyConstrained.png )

-   **Rubber band selection:**

![](images/Release-0.13-RubberBandSelection.png )

Geometry (Points, Lines and Curves) may be selected by dragging on the background to create a rectangular selection.

-   **Extended functionality of the polyline tool:** using the m key one can switch between arc and line mode and among free, tangent and perpendicular transitions from the previous segment.

-   **Map sketch to face** is a new tool to map (or remap) an existing sketch to the selected face on a solid. This allows the use of this sketch for features such as Pad and Pocket.

-   **Small Improvements:**
    -   When constructing geometry, tool tip with related information is shown next to cursor.
    -   **Sketch view** which sets the 3D view perpendicular to the sketch plane has now an icon in the Sketcher toolbar.

## Чертежный модуль 

-   **Режим задач**: Режим просмотра задач(Taskview) теперь по умолчанию установлен в Чертежном модуле. Не бойтесь, если вам больше нравится панель инструментовона по прежнему доступна в параметрах Чертежных настроек.
-   **Импорт из DXF**: Импортировщик из DXF теперь поддерживает точки (преобразуя их [Точки Чертежного модуля](Draft_Point.md)) и пунктир (преобразует в Ломаную Кривую)
-   **Совершенно новая система привязок**: [Система привязок](Draft_Snap.md) Чертежно модуля, полностью переписана с нуля. Теперь её гораздо проще расширять и использовать во внешних сценариях и модулях, также появились новые изображения обозначающие привязки , а также панель инструментов с ними, где вы можете вкл/выкл каждую привязку индивидуально или отключить всю систему привязок.

![800px](images/013-draft-snap.jpg)

-   **Улучшение ограничений**: Когда вы вводите точку в рехмерном пространстве, по мимо существующего ограничения при зажатой клавише Shift, теперь вы можете перемещаться только в X, Y или Z направлении нажав клавиши **X**, **Y** или **Z** соответственно. Повторное нажатие, отключит ограничение.
-   **Преобразование Чертеж \<-\> Эскиз**: Теперь Чертежный модуль обладает новым инструментом для конверсии [Draft2Sketch](Draft_Draft2Sketch.md) , он позволяет преобразовать выбранные Чертежные объекты (или любую плоскую форму) в Эскизы , а также это работает наоборот.
-   **Инструмент для создания клонов**: Создает копиии выбранного объекта с привязкой к оригиналу. Когда оригинал измениться, клоны обновяться автоматически. Объект клон можно переместить, повернуть, а также у него есть свойство масштаба, что позволяет вам менять размер копий.
-   **Импорт из SVG**: Теперь инструмент импорта из SVG лучше поддерживает кривые Безье.
-   **Скругленные углы**: Некоторые Чертежные объекты, как ([Ломаные](Draft_Wire.md), [Прямоугольник](Draft_Rectangle.md) и [Многоугольники](Draft_Polygon.md)) теперь обладают свойством **Радиус скругления** , скругляет их углы по указанному значению радиуса.

![800px](images/013-draft-fillet.jpg)

-   **Двумерная проекция**: Новый инструмент [Shape2DView](Draft_Shape2DView.md) позволяет быстро поместить проекцию выбранного объекта в трехмерную область документа(не пуать с модулем Проекций). Вы можете указать направление вектора проекции.

![800px](images/013-draft-shape2dview.jpg)

## Архитектурный модуль 

-   **Интеграция с Чертежным модулем**: Архитектурный и Чертежный модуль теперь тесно интегрированный друг с другом. Архитектурные инструменты используют [систему привязок Чертежного модуля](Draft_Snap.md) , а все чертежные инструменты представлены в Архитектурном модуле. На самом деле, если вы хотите вы можете теперь полностью скрыть Чертежный модуль (Настройки -\> Draft -\>Hide the Draft workbench)
-   **Новый инструмент для создания стен**: [Инструмент создания стен](Arch_Wall.md) был значительно усовершенствован, теперь появился режим рисования напрямую, он активируется , при нажатии на кнопку Стены, если не выбрано ни одного объекта, это позволяет вам рисовать стены, как будто вы рисуете простые линии. В дополнение к этому, теперь стены автоматически присоединяются если вы привязываетесь к существующей стене.

![800px](images/013-arch-wall.jpg)

!!FUZZY!!\* **Новый инструмент создания крыш**: Теперь в Архитектурном модуле доступен новый [инструмент создания крыш](Arch_Roof.md) , который позволяет вам быстро создать скатные крыши из выбранных граней.

-   **Новый инструмент создания окон**: Теперь [Окна](Arch_Window.md) создаются напрямую на поверхности плоской формы содержащий одну и более кломаных кривых(замкнутых), таких как прямоугольник или эскиз. Если эта форма была сразу нарисована на грани Стены, окно, автоматически вырезает отверстие в стене.
-   **Новая система сечений**: Теперь очень просто создать виды, разрезы и сечения из вашей модели: Поместите [Секущую плоскость](Arch_SectionPlane.md) , сориентируйте её, отредактируйте его чтобы включить только те объекты которые она должна видеть и \.... готово!
-   **Новая система отрисовки твердых тел**: В дополнение к основанном на OpenCasCADe каркасной 2D визуализации , которая сейчас используется [Модуле создания проекций](Drawing_Workbench.md), Архитектурный модуль тперь обладает новым двумерным визуализатором, который позволяет отрисовывать окрашенные грани в SVG Чертеж, создавая прекрасные 2D виды.

![800px](images/013-arch-vrm.jpg)

-   **Импорт из IFC с помощью [IfcOpenShell](http://www.ifcopenshell.org)**: Архитектурный модуль теперь может использовать [IfcOpenShell](http://www.ifcopenshell.org) если он установлен в вашей системе. Он предоставит вам , мощнейший импорт из IFC , все содержание IFC файла гарантировано будет импортировано.
-   **Новые объекты этаж и строение**: Строение и этажи это группы, вы можете добавлять и удалять из них с помощью простого перетаскивания в окне отображающем древовидную структуру пароекта.
-   **Новая система осей**: A new [axes system](Arch_Axis.md) feature has been added, that allows to quickly layout complex axes systems. These axes can then be added to [Structure](Arch_Structure.md) objects, so they spread automatically on the grid nodes.

![800px](images/013-arch-axes.jpg)

-   **Создание архитектурного объекта из полигионального**: Теперь, вы можете напрямую из полигиональных моделей создавать [стены](Arch_Wall.md) и [структуры](Arch_Structure.md), только если замкнуты а тела и ребра [многообразны](http://doc.spatial.com/index.php/Manifold_and_Non-manifold_Objects). Это позволяет быстро преобразовывать импортированную геометрию из других приложений, таких как [blender](http://www.blender.org) в объекты Архитектурного модуля.

## Part module 

-   **Refine shape** is a new utility that cleans up faces after a few operations on a shape. It can be set to run automatically after boolean operations in the Preferences.
-   **New Loft tool** can extrude a complex set of surfaces or a solid shape through a series of sketches or Draft objects.
-   **New Sweep tool** can extrude a complex set of surfaces or a solid shape through a series of sketches or Draft objects and a trajectory (sketch, edge or Draft object).
-   **New Offset tool** can offset a single surface or a shape.
-   **New Thickness tool** can hollow out a solid shape by setting a wall thickness and opening one or more faces.
-   **Shape Builder** and **Create primitives** are now in the Part toolbar for quick access.

## Part Design module 

-   **Pad** and **Pocket** are now more powerful thanks to more parameters, such as extrude to first/to last, up to face, 2 dimensions, symmetric to plane.
-   **Chamfer** and **Fillet** got an upgrade: selecting a face is now allowed, all the outer and inner edges of this face will be processed.
-   **Revolution**: a construction line can now be used as a revolution axis.
-   **New Groove tool**: cut matter from your solid by revolving a sketch.
-   **Linear pattern**, **Mirrored**, **Polar pattern** and **Multipattern** tools, that allow you to align and distribute pads and pockets on a feature.
-   A **Shaft Wizard** to help you design shaft objects

## Модуль проектирования кораблей 

-   Новый модуль для проектирования днищ кораблей

## 3D mice 

-   Support for 3D mice (Spaceball, Space Navigator) has been added to the Windows version.
-   A new **Spaceball Motion** tab in the Customize dialog allows for fine tuning your 3D mouse to the settings you want, directly from FreeCAD.

## OpenSCAD module 

-   This brand new (experimental) module brings OpenSCAD files import capability into FreeCAD. This file format is wildly popular in the RepRap community and on digital designs sharing site Thingiverse.
-   OpenSCAD script can be executed from within FreeCAD, by OpenSCAD (if installed on your computer), with the result appearing in your FreeCAD document.
-   For more information see the [OpenSCAD Workbench](OpenSCAD_Workbench.md) page on the FreeCAD wiki



---
![](images/Button_right.svg) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.13/ru
