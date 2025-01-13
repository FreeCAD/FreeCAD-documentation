# Manual:Generating 2D drawings/ru
{{Manual:TOC}}


<div class="mw-translate-fuzzy">


**Этот урок использует последние возможности разрабатываемой версии FreeCAD 0.19.**

Если Ваша модель не может быть напечатана или выфрезерована машиной напрямую, например, слишком велика (строение) или требует ручной сборки из готовых частей, Вам нужен способ показать, как это делается, человеку. В технических кругах (архитектура, инженерное дело и т.д.) это делается чертежами. Чертежи передаются человеку, ответственному за конечную сборку продукта, которые показывают ему, как это сделать.


</div>

Типичным примером могут служить инструкции сборки Ikea, [архитектурные чертежи](https://ru.wikipedia.org/wiki/Архитектурная_графика) или [синьки](https://ru.wikipedia.org/wiki/Синька_(копия_чертежа)). Эти чертежи обычно содержат не только рисунки, но и аннотации, такие как комментарии, размеры, выноски, символы, которые помогают понять, что и как должно быть сделано.

В FreeCAD рабочим столом для создания таких чертежей является <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [верстак TechDraw](TechDraw_Workbench/ru.md).

Верстак TechDraw позволяет создать листы, пустые или содержащие предварительно сделанные [шаблоны](TechDraw_Templates/ru.md), уже содержащие рамки и основную надпись. На этих листах можно поместить [виды](Drawing_View/ru.md) ранее смоделированных Вами трёхмерных объектов, и сконфигурировать, как эти виды будут выглядеть на листе. Вы так же можете поместить на Ваш лист все виды аннотаций, такие как размерности, тексты, и прочие обычные символы, обычно используемые в техническом черчении.

Готовые чертёжные листы могут быть напечатаны или экспортированы в файлы форматов [SVG](https://ru.wikipedia.org/wiki/SVG), PDF или [DXF](https://ru.wikipedia.org/wiki/DXF).


<div class="mw-translate-fuzzy">

В следующем примере мы посмотрим как создать простой чертёж модели стула, находящейся в [библиотеке FreeCAD](https://github.com/FreeCAD/FreeCAD-library) (Furniture → Chairs → IkeaLikeChair). Библиотека FreeCAD может быть легко добавлена к Вашей установке FreeCAD (смотрите главу [установка](Manual:Installing/ru.md) данного руководства), или Вы можете просто загрузить модель с веб-страницы библиотеки, или через прямую ссылку внизу этой главы.


</div>

![](images/Exercise_TechDraw_01.png )


<div class="mw-translate-fuzzy">

-   Загрузите из библиотеки файл IkeaLikeChair. Можно выбрать между версией [.FCStd](File_Format_FCStd/ru.md) с полной историей моделирования, или версией [.step](STEP/ru.md), создающей лишь объект, без истории. Поскольку нам больше не нужно модерировать стул, лучше взять версию .step, котороу легче манипулировать.


</div>

![](images/Parts_library.jpg )


<div class="mw-translate-fuzzy">

-   Переключимся на <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [верстак TechDraw](TechDraw_Workbench/ru.md)
-   Нажмём на кнопку <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:16px;"> [Вставить новую страницу с помощью шаблона](TechDraw_PageTemplate/ru.md).
-   Выберем шаблон **A4_Portrait_ISO7200TD**. В окне FreeCAD откроется новая вкладка, показывающая новый лист.
-   В [древе проекта](tree_view/ru.md) (или вкладке модели) выделим модель стула. Она скорее всего будет названа как-то вроде \"Open CASCADE STEP translator.\"
-   Нажмём кнопку <img alt="" src=images/TechDraw_View.svg  style="width:16px;"> [Вставить вид на страницу](TechDraw_View/ru.md).
-   На нашей странице будет создан объект View. Выделите объект view в древе проекта и зададите ему следующие [параметры](TechDraw_View#Properties/ru.md) на вкладке Данные комбинированного вида:
    -   Под категорией Основание:
        -   X: 70 mm
        -   Y: 120 mm
        -   Rotation: 0
        -   Scale: 0.1
    -   Под категорией Projection (нажмите стрелку вниз для модификации компонент x, y, и z этих параметров отдельно):
        -   Direction: \[0 0 1\]
        -   XDirection: \[0 -1 0\] (Change the y field first, then the x field)
-   Теперь у нас есть прекрасный вид нашего стула сверху. Нажмите кнопку <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> [TechDraw ToggleFrame](TechDraw_ToggleFrame/ru.md) для выключения View frames, labels, и vertices:

![](images/Exercise_drawing_02.jpg )


</div>

![](images/Exercise_drawing_02.jpg )


<div class="mw-translate-fuzzy">

-   Повторим нашу операцию дважды, чтобы сделать ещё два вида. Установим значения X и Y, показывающие позиции наших видов на странице, чтобы показать их в стороне от вида сверху, и их направления, чтобы показать их с разных сторон. Придадим видам следующие параметры:
    -   View001 (вид спереди): X: 70, Y: 220, Scale: 0.1, Rotation: 0, Direction: (-1,0,0), XDirection: (0,-1,0)
    -   View002 (вид сбоку): X: 150, Y: 220, Scale: 0.1, Rotation: 0, Direction: (0,-1,0), XDirection: (1,0,0)
-   После этого у нас получится следующая страница:

![](images/Exercise_TechDraw_04.png )


</div>

![](images/Exercise_TechDraw_04.png )


<div class="mw-translate-fuzzy">

-   При желании мы можем настроить наши виды. Мы можем просто [повернуть](Manual:Navigating_in_the_3D_view/ru.md) трёхмерный вид вашей модели, и когда получите вид, который вы хотите, выберите модель в древе проекта и нажмите <img alt="" src=images/TechDraw_View.svg  style="width:16px;"> вставку нового вида на страницу. Это автоматически вставит вид с желаемыми свойствами поворота и направления. Можно так же использовать инструмент <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:16px;"> [Projection Group](TechDraw_ProjectionGroup/ru.md).


</div>

-   We can tweak the aspect of our views if we want, for example, we can change their **Line Width** property (under the View tab in the Combo View) to 0.5.


<div class="mw-translate-fuzzy">

Теперь поместим на нашем чертеже размеры и выноски. Есть два пути для указания в модели размерностей: одно - указание размерностей внутри модели, используя инструмент <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Размер](Draft_Dimension/ru.md) из [верстака Draft](Draft_Workbench/ru.md), и поместить вид этих размеров на нашем листе с помощью инструмента <img alt="" src=images/TechDraw_DraftView.svg  style="width:16px;"> [TechDraw DraftView](TechDraw_DraftView.md). По-другому мы можем делать это напрямую на чертёжном листе. Мы используем последний метод.


</div>


<div class="mw-translate-fuzzy">

-   Нажмём на переключаемую кнопку <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> для включения вершин.
-   Используем Ctrl + Клик левой кнопкой мыши для выбора двух вершин, между которыми Вы хотите измерить дистанцию.
-   Нажмём на кнопку <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Dimension Length](TechDraw_LengthDimension/ru.md).


</div>

![](images/Exercise_TechDraw_05.png )


<div class="mw-translate-fuzzy">

-   Повторяйте операцию, пока все размеры, которые вы хотите указать, не будут размещены. Используйте инструменты <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Вертикальный размер](TechDraw_VerticalDimension/ru.md) и <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Горизонтальный размер](TechDraw_HorizontalDimension/ru.md), если нужно.
-   Найдите минутку, чтобы взглянуть на [параметры](TechDraw_LengthDimension/ru#Properties.md) объекта Dimension в комбинированном представлении.
-   Обратите внимание, что если вы измеряете [аксонометрический вид](https://en.wikipedia.org/wiki/Axonometric_projection) (например, изометрический) вместо прямой проекции (например, вида спереди), как мы сделали здесь, вам следует использовать инструмент <img alt="" src=images/_TechDraw_LinkDimension.svg  style="width:16px;"> [Dimension Link](TechDraw_LinkDimension/ru.md), чтобы получить правильное измерение.


</div>

![](images/Exercise_TechDraw_07.png )

-   We will now place the two callouts shown in the image above, using the <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [TechDraw Balloon](TechDraw_Balloon.md) tool.

![](images/Exercise_TechDraw_06.png )

1.  Looking at the Page in the [3D view](3D_view.md) window, select the View to which the Balloon will be attached, as shown in the image above.
2.  Press the <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> Balloon button.
3.  The cursor is now displayed as a balloon icon. Click on the page to place the balloon origin at the desired position.
4.  The balloon bubble may be dragged to the desired position.
5.  Change the balloon properties by double-clicking the balloon label or the balloon object in the [tree view](Tree_view.md). This will open the Balloon Task dialog. Set the Value field to the desired text and change the Symbol drop-down menu selection to **None**
6.  Press **OK**
7.  Repeat the operation for the second callout.

-   We will now fill in the sheet title block.
    -   Make sure that the View frames, labels, and vertices are visible. If not, hit the <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> Toggle button.
    -   Edit the text in each section of the sheet title block by clicking on the small green square on the left side of the text.


<div class="mw-translate-fuzzy">

Теперь наша страница может быть экспортирована в SVG для дальнейшей работы в графических приложениях вроде [inkscape](http://www.inkscape.org), или в DXF. Выберите страницу в [древовидном представлении](tree_view/ru.md), а затем выберите меню **Файл → Экспортировать**. Формат DXF может быть импортирован практически во все существующие двумерные приложения САПР. Страницы TechDraw так же могут быть распечатаны или экспортированы в PDF.


</div>

**Загрузки**


<div class="mw-translate-fuzzy">

-   Модель стула: <https://github.com/FreeCAD/FreeCAD-library/blob/master/Furniture/Chairs/IkeaLikeChair.step>
-   Файл, созданный в ходе данного упражнения: <https://github.com/JoshuaCall/FreeCAD-manual/blob/master/files/drawing.FCStd>
-   Лист SVG, полученный из этого файла: <https://github.com/JoshuaCall/FreeCAD-manual/blob/master/files/drawing.svg>


</div>

**Читать далее**

-   [Верстак TechDraw](TechDraw_Workbench/ru.md)
-   [Создание собственных шаблонов](TechDraw_TemplateHowTo/ru.md)
-   [Другой учебник TechDraw](Basic_TechDraw_Tutorial/ru.md)
-   [Библиотека FreeCAD](https://github.com/FreeCAD/FreeCAD-library)
-   [Inkscape](http://www.inkscape.org)

**Watch tutorials**

-   [Sliptonic\'s TechDraw playlist](https://www.youtube.com/watch?v=7LbOmSGW9F0&list=PLEuOia-QxyFKQnmM1U9yVo7eNrK_Mcln8)
-   [Symbols and Views](https://www.youtube.com/watch?v=cggBR1Ghq7k)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Generating 2D drawings/ru
