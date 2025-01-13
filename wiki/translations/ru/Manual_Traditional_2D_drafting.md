# Manual:Traditional 2D drafting/ru
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

Вы могли заинтересоваться FreeCAD, уже имея некоторый опыт технического черчения, например, с помощью программ вроде [AutoCAD](https://ru.wikipedia.org/wiki/AutoCAD). Или Вы уже знаете что-то о проектировании, либо Вы предпочитаете чертить вещи перед их изготовлением. В любом случае, FreeCAD предоставляет более традиционный верстак, чьи инструменты встречаются в большинстве двумерных САПР: [Верстак Draft](Draft_Workbench/ru.md).


</div>


<div class="mw-translate-fuzzy">

Верстак Draft, хотя и принимает методы работы из традиционного мира двумерных чертёжных САПР, вовсе не ограничен двумерной областью. Все его инструменты работают во всём трёхмерном пространстве и многие из инструментов Draft, например, <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Move](Draft_Move/ru.md) или <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Rotate](Draft_Rotate/ru.md) широко используются во всём FreeCAD, поскольку они зачастую более интуитивны, чем изменение параметров положения вручную.


</div>


<div class="mw-translate-fuzzy">

Среди инструментов, предоставляемых верстаком Draft, есть такие традиционные чертёжные инструменты как <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Line](Draft_Line/ru.md), <img alt="" src=images/Draft_Circle.svg  style="width:16px;"> [Circle](Draft_Circle/ru.md) или <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Wire](Draft_Wire/ru.md) (полилиния), инструменты редактирования вроде <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Move](Draft_Move/ru.md), <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Rotate](Draft_Rotate/ru.md) или <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Offset](Draft_Offset/ru.md), [система рабочих плоскостей с привязочными сетками](Draft_SelectPlane/ru.md), позволяющая Вам точно определить, в какой плоскости Вы работаете, и полная [система привязок](Draft_Snap/ru.md), сильно облегчающая черчение и позиционирование элементов в точных отношениях друг с другом.


</div>

The snapping system in FreeCAD's Draft Workbench is designed for precision. Whether working in 2D or 3D, you can snap to critical points like endpoints, midpoints, and centers of circles, making it easy to position elements relative to one another. Modes such as perpendicular, tangent, and intersection snapping further enhance precision. Combined with the working plane and grid system, these tools ensure the accurate alignment of objects and components.

FreeCAD's parametric nature enables constraints to be applied to drafted elements, ensuring geometric relationships stay intact. For example, you can make lines parallel or perpendicular and set fixed distances between elements. These constraints can be adjusted later, making design changes smooth and consistent across the project. The Draft Workbench also integrates seamlessly with other FreeCAD workbenches, such as Sketcher, which is designed for more constrained parametric 2D design, and TechDraw, which produces technical 2D drawings for documentation purposes.

Advanced features of the Draft Workbench include the ability to import and export files in formats like DXF and SVG, allowing you to work with or share designs with users of other CAD programs. Python scripting further enhances FreeCAD's capabilities, allowing you to automate tasks or create custom workflows. You can write scripts that generate draft objects based on specific geometric rules, streamlining repetitive tasks.

Для демонстрации работы и возможностей верстака Draft мы пройдём через простой пример, результатом которого будет этот простой чертёж, показывающий план маленького дома, содержащего лишь варочную плиту (немного абсурдно, но здесь мы можем делать что хотим, верно?):

![](images/Exercise_cabin_01.jpg )


<div class="mw-translate-fuzzy">

-   Переключаемся на **верстак Draft**
-   Как во всех приложениях технического черчения, разумнее правильно установить окружение, это съэкономит уйму времени. Сконфигурируйте по своему желанию [grid and working plane](Draft_SelectPlane/ru.md) и [Текст и размеры](Draft_Text/ru.md) в меню **Правка → Параметры → Draft**. В этом упражнении, тем не менее, мы будем действовать так, будто эти параметры сохранят значения по умолчанию.


</div>

![](images/FreeCAD_DraftPreferences.png )


<div class="mw-translate-fuzzy">

-   Верстак Draft так же содержит две специальные панели инструментов: одна с **визуальными установками**, где Вы можете изменить текущую рабочую плоскость, включить/отключить [конструктивный режим](Draft_ToggleConstructionMode.md), установить цвет линии, поверхности, толщину линии и размер текста для новых объектов, а другая для **привязок**. Здесь Вы можете включать/выключать сетку привязки, и устанавливать индивидуальные [положения привязки](Draft_Snap.md):


</div>

![](images/Draft_toolbars.png )

-   Turning on all the snap buttons is convenient, but also makes drawing slower, as more calculation needs to be done when you move the mouse cursor. It is often better to keep only the ones you will actually use.

-   Let\'s start by turning **construction mode** on, which will allow us to draw some guidelines on which we will draw our final geometry. You can do that by pressing on the <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md) command.
-   If you prefer, you can set the working plane to XY. This will lock the working plane, ensuring it remains on the XY plane regardless of how you change the view. If you choose not to do this, the working plane will automatically adapt to the current view, meaning you\'ll need to ensure you\'re in the top view whenever you want to draw on the XY (ground) plane to avoid unintended shifts in orientation.

Now we can switch to the Part Workbench and start to create our first table leg.


<div class="mw-translate-fuzzy">

-   Начнём с включённым **конструктивным режимом**, который позволит нам рисовать некоторые направляющие, по которым мы нарисуем финальную геометрию.
-   Если желаете, установите **рабочую плоскость** на **XY**. Если Вы сделаете это, рабочая плоскость не изменится при любом текущем виде. Если нет, рабочая плоскость будет меняться автоматически по текущему виду, и надо будет обращать внимание на том, чтобы был установлен вид сверху, когда Вы хотите рисовать на плоскости XY.
-   Затем выберите инструмент <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Rectangle](Draft_Rectangle/ru.md) и нарисуйте прямоугольник от точки (0,0,0) размером 2 метра на 2 метра (оставив Z равным нулю). Заметте, что большинство команд Draft могут быть выполнены с клавиатуры, не касаясь мыши, используя их двубуквенные сокращения. Наш первый прямоугольник 2x2 метра может быть выполнен так: re 0 **Enter** 0 **Enter** 0 **Enter** 2m **Enter** 2m **Enter** 0 **Enter**.
-   Сделайте дубль прямоугольника 15 см внутрь, используя инструмент <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Offset](Draft_Offset/ru.md), включив его команду Copy, и задав расстояние в 15 см:


</div>

-   Duplicate that rectangle by 15cm inside, using the <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Offset](Draft_Offset.md) tool, turning its Copy mode on, and giving it a distance of 15cm:

![](images/Exercise_cabin_02.png )


<div class="mw-translate-fuzzy">

-   Далее мы можем начертить пару вертикальных линий, чтобы определить, где будут помещены наши окна и двери, используя инструмент <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Линия](Draft_Line/ru.md). Пересечение этих линий с нашими двумя прямоугольниками даст нам полезное пересечение для привязки наших стен. Начертим первую линию от точки (15 см, 1 м, 0) к точке (15 см, 3 м, 0).
-   Создадим 5 дубликатов этих линий, используя инструмент <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Перемещение](Draft_Move/ru.md) с включённым копированием. Включим так же режим Relative, который позволит нам определить движение через смещение, что проще чем вычислять заданную абсолютную позицию каждой линии. Дадим каждой новой копии любую стартовую точку, оставив, например, (0,0,0), и следующие относительные конечные точки:
    -   line001: x: 10cm
    -   line002: x: 120cm
    -   line003: x: -55cm, y: -2m
    -   line004: x: 80cm
    -   line005: x: 15cm


</div>

![](images/Exercise_cabin_03.jpg )


<div class="mw-translate-fuzzy">

-   Это всё, что нам сейчас нужно, так что мы можем выключить конструкторский режим. Убедитесь, что вся конструкторская геометрия помещена в группу \"Construction\", с которой их скрыть разом или полностью потом удалить.
-   Теперь нарисуем наши два куска стены с использованием инструмента <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Wire](Draft_Wire/ru.md). Убедитесь, что включена <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:16px;"> [привязка по пересечению](Draft_Snap.md), поскольку нам нужно захватывать точки пересечения линий и прямоугольников. Рисуем две ломаные как показано ниже, кликнув все точки их контуров. Чтобы замкнуть их, кликните первую точку вновь или нажмите кнопку **Close**:


</div>

![](images/Exercise_cabin_04.jpg )


<div class="mw-translate-fuzzy">

-   Мы можем изменить серый цвет по умолчанию на красивую штриховку выбором обеих стен и установкой параметра **Pattern** в **Simple**, и его **Pattern size** по Вашему желанию, например, **0.005**.


</div>

![](images/Draft_Pattern.png )


<div class="mw-translate-fuzzy">

-   Теперь мы скроем конструктивную геометрию правым кликом на Construction group и выбором **Hide Selection**.
-   Нарисуем теперь окна и двери. Убедимся, что <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:16px;"> [привязка к средней точке](Draft_Snap/ru.md) включена, и нарисуем шесть линий как показано ниже:


</div>

![](images/Exercise_cabin_06.jpg )


<div class="mw-translate-fuzzy">

-   Теперь вставим линию двери, чтобы создать символ открытой двери. Начнём с вращения линии с помощью инструмента <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Rotate](Draft_Rotate/ru.md). Кликните конечную точку линии как центр вращения, задайте начальный угол **0**, и конечный угол **-90**.
-   Затем создайте открытую дугу инструментом <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [Arc](Draft_Arc/ru.md). Возьмите точку вращения предыдущего шага как центр дуги, кликните другую точку линии, чтобы получить радиус, затем кликните стартовую и конечную точку дуги как показано ниже:


</div>

![](images/Exercise_cabin_07.jpg )


<div class="mw-translate-fuzzy">

-   Теперь мы можем начать размещать мебель. Для начала поместим счётчик, нарисовав прямоугольник от верхнего левого внутреннего угла шириной 170 см и высотой -60 см. На рисунке выше, параметр **Transparency** прямоугольника установлен в 80%, чтобы получить красивый мебельный вид.
-   Затем добавим раковину и варочную поверхность. Рисование таких символов вручную может быть утомительным, и их обычно легко найти в интернете, например на <http://www.cad-blocks.net> . В нижеследующем разделе **Загрузки**, например, мы разделили раковину и плиту с этого сайта, и сохранили их как файлы DXF. Вы можете загрузить эти два файла по нижеследующим ссылкам, правым кликом и выбором на кнопке **Raw** и выбором **save as**.
-   Вставка файла DXF в открытый документ FreeCAD может производиться либо выбором в меню **Файл → Импортировать**, или перетаскиванием файла DXF из файлового менеджера в окно FreeCAD. Содержимое файлов DXF не может появиться прямо в центре Вашего текущего вида, в зависимости от того, где он был в файле DXF. Используйте меню **Вид → Стандартные виды → Уместить всё**, чтобы найти импортированные объекты. Вставьте два файла DXF, и поместите их на подходящем месте на столешнице:


</div>

![](images/Exercise_cabin_08.jpg )


<div class="mw-translate-fuzzy">

-   Теперь мы можем поместить пару размеров с помощью инструмента <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Dimension](Draft_Dimension/ru.md). Размеры рисуются указанием трёх точек: начальной, конечной точки, и точки размерной линии. Чтобы сделать горизонтальный или вертикальный размер, когда первые две точки не выровнены, нажмите кнопку **Shift** во время клика по следующей точке.
-   Можно изменить позицию размерного текста двойным кликом по размеру на древе проекта. Контрольная точка позволяет Вам перемещать текст графически. В нашем размере текст \"0.15\" был перемещён наружу для ясности чертежа.
-   Можно изменить содержимое размерного текста редактированием параметра **Override**. В нашем примере тексты размеров окон и дверей редактировались для показа их высоты:


</div>

![](images/Exercise_cabin_09.jpg )


<div class="mw-translate-fuzzy">

-   Добавим описание с помощью инструмента <img alt="" src=images/Draft_Text.svg  style="width:16px;"> [Text](Draft_Text/ru.md). Кликнем по точке позиционирования текста, затем введём текст, нажимая Enter после каждой его линии. Для завершения нажмём Enter дважды.
-   Линии-выноски, которые соединяют текст с описываемым элементом делаются просто инструментом Wire. Рисуем ломаные, начиная с позиции текста до описываемого объекта. Затем можно добавить точку или стрелку в конце, установив параметр **End Arrow** в **`True`**.


</div>

![](images/Exercise_cabin_10.jpg )


<div class="mw-translate-fuzzy">

-   Наш чертёж готов! Поскольку здесь получилось довольно много объектов, разумно сделать некоторую уборку и реструктурировать всё в логичные группы, чтобы файл было проще понять другому человеку:


</div>

![](images/Draft_Organised.png )


<div class="mw-translate-fuzzy">

-   Теперь мы можем напечатать нашу работу, поместив её на чертёжный лист, что мы покажем далее в этом руководстве, или экспортировать наш чертёж в другое приложение САПР, сохранив его в файл DXF. Просто выделите нашу группу \"Floor plan\", выберите в меню **Файл → Экспортировать**, и выберите формат Autodesk DXF. Файл может быть открыт в любой двумерной САПР вроде [LibreCAD](http://www.librecad.org). Вы можете отметить некоторые отличия, в зависимости от от конфигурации каждого приложения.


</div>

![](images/Exercise_cabin_12.jpg )


<div class="mw-translate-fuzzy">

-   Самое важное в верстаке Draft, тем не менее, что созданная геометрия может использоваться как базовая или легко выдавливаться в трёхмерные объекты, просто используя инструмент <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Выдавить](Part_Extrude/ru.md) из [верстака Part Workbench](Part_Workbench/ru.md), или, оставаясь в Draft, инструментом <img alt="" src=images/Draft_Trimex.svg  style="width:16px;"> [Trimex](Draft_Trimex/ru.md) (Обрезать/Удлинить/Выдавить), который внутри выполняет выдавливание из верстака Part, но делает их \"способом Draft\", то есть позволяет Вам отмечать и захватывать длину выдавливания графически. Экспериментальное выдавливание наших стен показано ниже.
-   Нажав после выделения грани объекта кнопку <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [Выбор плоскости](Draft_SelectPlane/ru.md), Вы так же можете поместить рабочую плоскость в любом месте, и рисовать объекты Draft в различных плоскостях, например, поверх стен. Затем они могут быть выдавлены в другие трёхмерные тела. Поэкспериментируйте установкой рабочих плоскостей поверх стен, затем нарисуйте прямоугольники прямо здесь.


</div>

![](images/Exercise_cabin_13.jpg )


<div class="mw-translate-fuzzy">

-   Все виды отверстий так же легко могут быть сделаны рисованием объектов Draft на поверхности стен, выдавливанием их и использованием булевых операций из верстака Part для вычитания их из других тел, как мы видели в предыдущей главе.


</div>


<div class="mw-translate-fuzzy">

По сути, то, что делает верстак Draft, это обеспечивает графический путь создания базовых операций Part. В то время как в верстаке Part Вы обычно располагаете объекты, устанавливая их параметры размещения, в верстаке Draft Вы можете делать это на экране. Иногда лучше это, иногда другое. Не забудьте, Вы можете создать [пользовательскую панель инструментов](Interface_Customization/ru.md) в одном из этих верстаков, добавить инструменты из другого, и получить максимум из обеих миров.


</div>

This difference is where the workbenches complement each other. The Draft Workbench is ideal for fast, interactive design, allowing you to draw and position objects without constantly entering precise numerical values. On the other hand, the Part Workbench offers more detailed, parametric control over object properties, making it better suited for highly accurate adjustments, especially in engineering or technical design projects.

The beauty of FreeCAD is that you don\'t need to choose between one or the other. You can create [custom toolbars](Interface_Customization.md) by combining tools from both the Draft and Part Workbenches, giving you the flexibility to switch between graphical and parametric methods as needed. This allows you to enjoy the best of both worlds---quick, on-screen adjustments from the Draft Workbench and the precision of the Part Workbench---depending on the needs of your project. Additionally, using keyboard shortcuts and custom toolbars can speed up your workflow, making it easy to transition between different operations without interrupting your design process.



## Загрузки


<div class="mw-translate-fuzzy">

-   Файл, созданный в ходе этого урока: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.FCStd>
-   Файл DXF раковины: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/sink.dxf>
-   Файл DXF варочной панели: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cooktop.dxf>
-   Финальный файл DXF, созданный во время этого упражнения: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.dxf>


</div>

## Related


<div class="mw-translate-fuzzy">

-   [Верстак Draft](Draft_Workbench/ru.md)
-   [Привязка](Draft_Snap/ru.md)
-   [Рабочая плоскость верстака Draft](Draft_SelectPlane/ru.md)


</div>



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Draft](Category_Draft.md) > Manual:Traditional 2D drafting/ru
