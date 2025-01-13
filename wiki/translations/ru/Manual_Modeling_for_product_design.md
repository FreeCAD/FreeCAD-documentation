# Manual:Modeling for product design/ru
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}


<div class="mw-translate-fuzzy">

[Проектирование продукта](https://en.wikipedia.org/wiki/Product_design) изначально было коммерческим термином, но в мире 3D это обычно означает моделирование чего-то, что будет напечатано с помощью [3D-принтера](https://ru.wikipedia.org/wiki/3D_принтер), или, в более общем случае, произведено с помощью машины, будь это объёмный принтера или [станок с ЧПУ](https://ru.wikipedia.org/wiki/Числовое_программное_управление).


</div>


<div class="mw-translate-fuzzy">

Когда Вы печатаете объёмный объект, обязательно нужно, чтобы Ваш объект был **твёрдым телом**. Конечно, ничего не мешает ему быть пустым внутри. Но Вам всегда следует чётко знать, с какой стороны внутренний материал, а где внешняя сторона, поскольку принтер или ЧПУ должны чётко знать, что заполнено материалом, а что нет. Поэтому [верстак PartDesign](PartDesign_Workbench/ru.md) является лучшим инструментом в FreeCAD для построения таких частей, потому что он всегда следит за тем, чтобы объекты были твердотельны и изготовляемы.


</div>


<div class="mw-translate-fuzzy">

Для демонстрации работы верстака PartDesign, смоделируем эту хорошо известную деталь [Лего](https://ru.wikipedia.org/wiki/Лего):


</div>

![](images/FreeCAD_Exercise1_RedBrick.png )


<div class="mw-translate-fuzzy">

В элементах Лего хорошо то, что их размеры, как минимум для стандартных, легко узнать в Интернет. Их достаточно легко моделировать и печатать в объёме, и при некотором терпении (объёмная печать требует много настройки) Вы сможете сделать элементы, которые полностью совместимы и идеально присоединяются к оригинальным блокам Лего. В показанном ниже примере мы делаем элемент в 1,5 раз больше оригинала.


</div>


<div class="mw-translate-fuzzy">

Мы будем использовать только инструменты модулей [Sketcher](Sketcher_Workbench/ru.md) и [PartDesign](PartDesign_Workbench/ru.md). Поскольку все инструменты верстака Sketcher включены в верстак PartDesign, мы можем оставаться в PartDesign и не нуждаться в переключении между верстаками.


</div>

A sketch is considered fully constrained when every point is locked into position by the appropriate number of constraints, meaning no part of the sketch can be moved freely. Achieving a fully constrained sketch is ideal because it ensures the design is well-defined and stable, allowing for predictable changes later in the design process. On the other hand, if more constraints are added than necessary---referred to as an over-constrained sketch---this can cause conflicts in the geometry. FreeCAD will alert you to any redundant or conflicting constraints, as over-constraining can cause issues in further operations like extrusions or cuts.


<div class="mw-translate-fuzzy">

Объекты PartDesign полностью базируются на **Эскизах**. Эскизы это двумерные объекты, составленные из линейных сегментов (линий, дуг или эллипсов) и геометрических ограничений. Эти ограничения могут быть применены либо к линейным сегментам или их конечным точкам или центральным точкам, и заставляют геометрию следовать некоторым правилам. Например, Вы можете поместить вертикальные ограничения к сегменту линии, чтобы заставить его быть вертикальным, или установить для конечных точек ограничения позиции, чтобы запретить перемещение. Когда эскиз содержит такой набор ограничений, что никакие точки эскиза не могут быть сдвинуты, говорят о полностью ограниченном эскизе. Когда есть излишние ограничения, которые могут быть убраны без позволения изменений геометрии, он называется переограниченным. Этого следует избегать, и FreeCAD в этом случае сделает предупреждение.


</div>

Эскизы имеют режим редактирования, где их геометрия и ограничения могут быть изменены. Когда Вы завершили редактирование, эскизы ведут себя как остальные объекты FreeCAD, и могут использоваться как строительные блоки для всех инструментов PartDesign и для других верстаков, вроде [Part](Part_Workbench/ru.md) или [Arch](Arch_Workbench/ru.md). [Верстак Draft](Draft_Workbench/ru.md) так же содержит инструменты, которые преобразуют объекты Draft в объекты Sketch и наоборот.


<div class="mw-translate-fuzzy">

-   Начнём с моделирования палаллелепипеда, который станет базой для нашего кубика Lego. Далее мы вырежем внутренности, и добавим 8 точек сверху. Поэтому начнём с создания прямоугольного эскиза, который мы потом выдавим:
-   Переключимся на [верстак PartDesign](PartDesign_Workbench/ru.md)
-   Кликнем на кнопке <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Создать эскиз](Sketcher_NewSketch/ru.md). Появится диалог, спрашивающий, как расположить эскиз, выберем плоскость **XY**, плоскость \"вида сверху\". Эскиз будет создан и переключён в режим редактирования, а вид будет повёрнут так, чтобы видеть эскиз сверху.
-   Теперь нарисуем прямоугольник, выбрав инструмент <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> [Создать прямоугольник](Sketcher_CreateRectangle/ru.md) и кликнув две угловые точки. Можете поместить их где угодно, поскольку правильное положение будет установлено на следующем шаге.
-   Вы увидите, что прямоугольнику сразу будет добавлено множество геометрических ограничений: вертикальные сегменты получат вертикальные ограничения, горизонтальные - горизонтальные ограничения, а каждый угол - ограничение коинцидентности, соединяющее сегменты вместе. Вы можете на пробу подвигать прямоугольник, перетаскивая его линии мышью, и вся геометрия останется соответствующей ограничениям.


</div>

![](images/FreeCAD_Exercise1_re_UC.png )


<div class="mw-translate-fuzzy">

-   Теперь добавим ещё три ограничения:
    -   Выберите один из вертикальных сегментов и добавьте <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [Ограничение расстояния по вертикали](Sketcher_ConstrainDistanceY/ru.md). Установите размер 23,7 мм.
    -   Выберите один из горизонтальных сегментов и добавьте <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [Ограничение расстояния по горизонтали](Sketcher_ConstrainDistanceX/ru.md). Установите его в 47,7 мм.
    -   Затем выберите одну из угловых точек и начальную точку (это точка на пересечении красной и зелёной оси), и добавьте <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:16px;"> [Ограничение коинцидентности](Sketcher_ConstrainCoincident/ru.md). Прямоугольник переместится к начальной точке привязки, и эскиз станет зелёным, означая, что он он полностью ограничен. Попробуйте перемещать линии или точки, ничего больше не сдвинется.


</div>

![](images/FreeCAD_Exercise1_re.png )


<div class="mw-translate-fuzzy">

-   Наш базовый эскиз теперь готов, мы можем закончить редактирование нажатием кнопки **Закрыть** на панели задач, или просто нажатием кнопки **Escape**. Если нужно, в любое время можно вернуться в режим редактирования двойным кликом на эскизе в древе проекта.
-   Применим к эскизу инструмент <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Выдавливание](PartDesign_Pad/ru.md), и зададим расстояние 14,4 мм. Прочие опции можно оставить по умолчанию:


</div>

![](images/FreeCAD_Exercise1_padding.png )


<div class="mw-translate-fuzzy">

**Выдавливание** в PartDesign действует похоже на инструмент [Extrude](Part_Extrude/ru.md), который мы использовали в предыдущей главе, но есть много отличий. Главное из них, что это выдавливание не может быть передвинуто, оно навсегда привязано к эскизу. Если Вы хотите изменить положение выдавливания, Вам следует перемещать эскиз. В текущем контексте, где мы хотим гарантировать, что ничего не уйдет со своего места, это добавляет защиту.


</div>


<div class="mw-translate-fuzzy">

-   Мы будем теперь делать вырез внутри блока, используя инструмент <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [карман](PartDesign_Pocket/ru.md), версия инструмента [Обрезать](Part_Cut/ru.md). Чтобы сделать выемку, мы сделаем эскиз внизу нашего блока, который будет использовать для удаления части блока.
-   При выбранной нижней гранью нажмите кнопку <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Создать эскиз](Sketcher_NewSketch/ru.md).
-   Рисуем в этом эскизе прямоугольник


</div>

![](images/FreeCAD_Exercise1_TopFaceSketch.png )


<div class="mw-translate-fuzzy">

-   Теперь мы ограничим прямоугольник относительно нижней грани. Для этого нам нужно \"импортировать\" некоторые грани поверхности с помощью инструмента <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [External geometry](Sketcher_External/ru.md). Примените этот инструмент к двум вертикальным линиям на нижней поверхности:


</div>

![](images/FreeCAD_Exercise1_topCylPad.png )


<div class="mw-translate-fuzzy">

Вы заметите, что этим инструментом могут быть добавлены только рёбра с базовой поверхности. Когда Вы создаёте эскиз с выбранной поверхностью, создается связь между ними, которая важна для дальнейших операций. Вы всегда можете позднее пересоединить эскиз к другой поверхности инструментом <img alt="" src=images/Sketcher_MapSketch.svg  style="width:16px;"> [Разместить эскиз на грани](Sketcher_MapSketch/ru.md).


</div>


<div class="mw-translate-fuzzy">

-   Внешняя геометрия не \"реальна\", она пропадёт при выходе из режима редактирования. Но её можно использовать для наложения ограничений. Установите следующие 4 ограничения:
    -   Выделите верхнюю левую точку прямоугольника и верхнюю точку импортированной линии и добавьте <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [Ограничение расстояния по горизонтали](Sketcher_ConstrainDistanceX/ru.md) равным 1,8 мм
    -   Снова выделите верхнюю левую точку прямоугольника и верхнюю точку импортированной линии и добавьте <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [Ограничение расстояния по вертикали](Sketcher_ConstrainDistanceY/ru.md) равным 1,8 мм
    -   Выделите нижнюю правую точку прямоугольника и верхнюю точку импортированной линии и добавьте <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [Ограничение расстояния по горизонтали](Sketcher_ConstrainDistanceX/ru.md) равным 1,8 мм
    -   Снова выделите нижнюю правую точку прямоугольника и верхнюю точку импортированной линии и добавьте <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [Ограничение расстояния по вертикали](Sketcher_ConstrainDistanceY/ru.md) равным 1,8 мм


</div>

-   We will now carve the inside of the block, using the <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Pocket](PartDesign_Pocket.md) tool, which is the PartDesign version of [Part Cut](Part_Cut.md). To make a pocket, we will create a sketch on the bottom face of our block, which will be used to remove a part of the block.
-   With the bottom face selected, press the <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [New Sketch](PartDesign_NewSketch.md) button.
-   Draw a <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> [Rectangle](Sketcher_CreateRectangle.md) on the face.
-   Apply a <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [symmetry constraint](Sketcher_ConstrainSymmetric.md) by selecting the upper left corner point of the rectangle, then the origin point (the dot where the red and green axes intersect), and the lower right corner point.
-   By using the \[Image:Sketcher_External.svg\|16px\]\] [External geometry](Sketcher_External.md) choose the left edge of the bottom face. Notice again that it will be highlighted in red.
-   Set the horizontal and vertical distance of the rectangle in regards to the upper right point to 1.8 by using the <img alt="" src=images/Sketcher_Dimension.svg  style="width:16px;"> [ automatic dimension](Sketcher_Dimension.md) constraint.


<div class="mw-translate-fuzzy">

-   Покинув режим редактирования, мы теперь можем выполнить операцию создания кармана. С выделенным эскизом нажимаем кнопку <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Карман](PartDesign_Pocket/ru.md). Задаём длину 12,6 мм, что оставит толщину верхней поверхности нашей детали в 1,8 мм (вспоминаем, что общая высота нашей детали 14,4 мм).


</div>

-   Create three <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [circles](Sketcher_CreateCircle.md) by making sure their center is located on the X-axis (red line).
-   By choosing all three circles apply an <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [equal constraint](Sketcher_ConstrainEqual.md).
-   Set the diameter of one circle to 9.765mm.
-   Set the center distance of the left circle in regards to the bottom edge of the rectangle we created before to 10.2mm.
-   Set the distance between the left and middle circles to 12 mm. Repeat this step to set the same 12 mm distance between the middle and right circles


<div class="mw-translate-fuzzy">

-   Теперь мы займёмся 8 точками на верхней поверхности. Для этого, поскольку они имеют одну форму, мы используем удобный инструмент <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [Linear pattern](PartDesign_LinearPattern/ru.md) верстака PartDesign, который позволяет делать повторы один раз смоделированной формы.
-   Начните с выделения верхней поверхности нашего блока
-   Нажмите <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Создать эскиз](Sketcher_NewSketch/ru.md).
-   Создайте две <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [окружности](Sketcher_CreateCircle/ru.md).
-   Для каждой окружности выделите её и задайте им <img alt="" src=images/Constraint_Radius.svg  style="width:16px;"> [Ограничение радиуса](Sketcher_ConstrainRadius/ru.md) в 3,6 мм каждой
-   Импортируйте левое ребро базовой плоскости инструментом <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [Геометрия извне](Sketcher_External.md).
-   Поместите два вертикальных и два горизонтальных ограничения в 6 мм между центральными точками каждой окружности и угловых точек импортированного ребра, так чтобы центр каждой из окружности был в 6 мм от края верхней грани:


</div>

-   We are almost done.
-   Create three additional <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [circles](Sketcher_CreateCircle.md) , ensuring that each new circle is concentric with one of the previously drawn circles. Alternatively, you can place the new circles anywhere in the sketch and use the <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [coincident constraint](Sketcher_ConstrainCoincident.md) tool to align their centers with the centers of the existing circles.
-   By choosing all three circles apply an <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [equal constraint](Sketcher_ConstrainEqual.md).
-   Set the diameter of one circle to 7.2mm.
-   You can now exit the sketch.


<div class="mw-translate-fuzzy">

-   Заметьте снова, что когда Вы зафиксировали все позиции и размеры на Вашем эскизе, он становится полностью ограниченным. Это даёт вам гарантии. Вы можете изменить сейчас первый эскиз, но всё, что мы сделали после этого остаётся привязанным.
-   Покиньте режим редактирования, выделите этот новый эскиз, и создайте <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Выдавливание](PartDesign_Pad/ru.md) в 2,7 мм:


</div>

-   By choosing the completed sketch use the <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Pocket](PartDesign_Pocket.md) tool setting the length to 12 mm.

![](images/FreeCAD_Exercise1_BottomPad.png )

-   This is it. Our brick is ready. If you wish to change its color, you can do so by going to the **View tab**.

![](images/FreeCAD_Exercise1_redBrick2.png )


<div class="mw-translate-fuzzy">

Теперь мы видим, что наша история моделирования (которая видна в древе проекта) стала довольно длинной. Это прекрасно, поскольку каждый шаг нашей работы может быть потом изменён. Адаптация этой модели для другого вида кирпичиков, например, на 2x2 точки вместо 2x4, будет проще пареной репы, нам только надо будет изменить пару размеров и число шагов в линейных массивах. Мы сможем так же легко создать большие элементы, которых нет в оригинальной игре Lego.


</div>


<div class="mw-translate-fuzzy">

Но нам может понадобиться вычистить нашу историю, например, если мы собираемся смоделировать их этих кирпичиков замок, и нам не хочется, чтобы эта история повторялась в нашем файле сотни раз.


</div>


<div class="mw-translate-fuzzy">

Есть два простых способа отбросить историю, один это использовать инструмент [Create simple copy](Part_SimpleCopy/ru.md) из [верстака Part](Part_Workbench/ru.md), который создаст независимую от истории копию нашего элемента (потом можно будет её даже удалить), другой путь - это экспортировать элемент в файл STEP и снова импортировать его.


</div>

**Загрузки**

-   Созданная во время этого упражнения модель: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.FCStd>

**Читать далее**

-   [Эскизирование](Sketcher_Workbench.md)
-   [Верстак PartDesign](PartDesign_Workbench.md)
-   [Верстак Assembly2](https://github.com/hamish2014/FreeCAD_assembly2)


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Modeling for product design/ru
