# Manual:Generating 2D drawings/ru
{{Manual:TOC/ru}}


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

![](images/Exercise_TechDraw_01.svg )

-   Загрузите из библиотеки файл IkeaLikeChair. Можно выбрать между версией [.FCStd](File_Format_FCStd/ru.md) с полной историей моделирования, или версией [.step](STEP/ru.md), создающей лишь объект, без истории. Поскольку нам больше не нужно модерировать стул, лучше взять версию .step, котороу легче манипулировать.

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

-   Повторим нашу операцию дважды, чтобы сделать ещё два вида. Установим значения X и Y, показывающие позиции наших видов на странице, чтобы показать их в стороне от вида сверху, и их направления, чтобы показать их с разных сторон. Придадим видам следующие параметры:
    -   View001 (вид спереди): X: 70, Y: 220, Scale: 0.1, Rotation: 0, Direction: (-1,0,0), XDirection: (0,-1,0)
    -   View002 (вид сбоку): X: 150, Y: 220, Scale: 0.1, Rotation: 0, Direction: (0,-1,0), XDirection: (1,0,0)
-   После этого у нас получится следующая страница:

![](images/Exercise_TechDraw_04.png )


<div class="mw-translate-fuzzy">

-   При желании мы можем настроить наши виды. Мы можем просто [повернуть](Manual:Navigating_in_the_3D_view/ru.md) трёхмерный вид вашей модели, и когда получите вид, который вы хотите, выберите модель в древе проекта и нажмите <img alt="" src=images/TechDraw_View.svg  style="width:16px;"> вставку нового вида на страницу. Это автоматически вставит вид с желаемыми свойствами поворота и направления. Можно так же использовать инструмент <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:16px;"> [Projection Group](TechDraw_ProjectionGroup/ru.md).


</div>

-   We can tweak the aspect of our views if we want, for example we can change their **Line Width** property (under the View tab in the Combo View) to 0.5.


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


<div class="mw-translate-fuzzy">

![](images/Exercise_TechDraw_07.png )

-   Теперь мы разместим две выноски, показанные на изображении выше, используя инструмент <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [Balloon](TechDraw_Balloon/ru.md).

![](images/_Exercise_TechDraw_06.png )

1.  Глядя на страницу в окне [трёхмерного вида](3D_view/ru.md), выберите вид, к которому Balloon будет прикреплен, как показано на рисунке выше.
2.  Нажмите кнопку Balloon <img alt="" src=images/_TechDraw_Balloon.svg  style="width:16px;"> .
3.  Курсор теперь отображается в виде значка с изображением шарика. Нажмите на страницу, чтобы поместить исходную точку выноски в нужное место.
4.  Выноску можно перетащить в нужное положение.
5.  Измените свойства выноски, дважды щелкнув на значке его метки или объекте выноски в [древе проекта](tree_view/ru.md). Откроется диалоговое окно Balloon Task. Установите в поле «Значение» нужный текст и измените выделение раскрывающегося меню «Символ» на **None**
6.  Нажмите **OK**
7.  Повторите операцию для второго выносного элемента.

-   Теперь мы заполним блок заголовка листа.
    -   Убедитесь, что видимые рамки, метки и вершины видны. Если нет, нажмите кнопку <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;">.
    -   Отредактируйте текст в каждом разделе заголовка листа, щелкнув по маленькому зеленому квадрату в левой части текста.


</div>


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Generating 2D drawings/ru
