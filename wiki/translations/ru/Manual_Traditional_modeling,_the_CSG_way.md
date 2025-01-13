# Manual:Traditional modeling, the CSG way/ru
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}


<div class="mw-translate-fuzzy">

КБГ означает [Конструктивную блочную геометрию (Constructive Solid Geometry, CSG)](https://ru.wikipedia.org/wiki/Конструктивная_сплошная_геометрия), и описывает самый простой способ работы со сплошной трёхмерной геометрией: создание сложных объектов добавкой и удалением кусков в/из сплошных тел с помощью булевых операций, таких как объединение, вычитание или пересечение.


</div>


<div class="mw-translate-fuzzy">

Как мы уже видели в этом руководстве, FreeCAD может поддерживать множество типов геометрии, но предпочтительным и наиболее подходящим типом объёмных объектов, которые мы будем проектировать с помощью FreeCAD, это объекты реального мира, которые, разумеется, твердотельные, [граничной](https://ru.wikipedia.org/wiki/Граничное_представление) геометрией, которая в основном поддерживается [модулем Part](Part_Workbench/ru.md). В отличие от [полигональных сеток](https://ru.wikipedia.org/wiki/Полигональная_сетка), которые состоят из точек и треугольников, поверхности объектов BREP определяются математическими кривыми, обеспечивающими абсолютную точность вне зависимости от масштаба.


</div>


<div class="mw-translate-fuzzy">

![](images/Mesh_vs_brep.jpg )


</div>


<div class="mw-translate-fuzzy">

Различие между ними может сравниться с различием между растровыми и векторными изображениями. Как в растровых изображениях, полигональные сетки разбивают кривые поверхности на последовательность точек. При взгляде на них в приближении или печати в большом масштабе они будут видны не как кривые, а как гранёная поверхность. Как в векторных изображениях, так и в данных граничных представлений, позиция любой точки кривой не сохраняется в геометрии, а вычисляется на лету, с высокой точностью.


</div>


<div class="mw-translate-fuzzy">

Граничная геометрия в FreeCAD поддерживается сторонним приложением с открытыми источниками, [OpenCasCade](https://ru.wikipedia.org/wiki/Open_Cascade_Technology). Основным интерфейсом между FreeCAD и ядром OpenCasCade служит модуль Part. Большинство других верстаков строят свою функциональность поверх модуля Part.


</div>

While other workbenches in FreeCAD, such as the Part Design and Surface Workbenches, offer more advanced tools for building and manipulating geometry, they rely on the underlying Part Workbench. Understanding how Part objects work internally and being adept with the basic Part tools is beneficial. Often, these simpler tools can resolve issues that more complex tools may not handle effectively.

![](images/Mesh_vs_brep.jpg )

The difference between the two can be compared to the difference between bitmap and vector images. As with bitmap images, polygon meshes have their curved surfaces divided into a series of points. If you look at it closely or print it very large, you will see not a curved but a faceted surface. In both vector images and BREP data, the position of any point on a curve is not stored in the geometry but calculated on the fly, with exact precision.


<div class="mw-translate-fuzzy">

Для иллюстрации работы верстака Part мы будем моделировать этот стол, используя лишь операции CSG (за исключением винтов, для которых мы используем одно из расширений, и размерностей, которые мы рассмотрим в следующей главе):


</div>

![](images/Exercise_table_complete.jpg )


<div class="mw-translate-fuzzy">

Создадим новый документ (**Ctrl+N** или через меню Файл → Создать), для нашего проекта стола. Документ сначала будет зваться \"unnamed\" во вкладке модели и в панели комбинированного вида, но когда Вы сохраните документ (**Ctrl+Shift+S** или меню Файл → сохранить как) как новый документ FreeCAD \"table.FCStd\", документ будет переименован в \"table\", что точнее идентифицирует проект.

переключимся на верстак Part, и начнём с первой ножки:


</div>

Теперь можно переключиться на Part верстак и начать создавать нашу первую ножку стола.


<div class="mw-translate-fuzzy">

-   Нажмите <img alt="" src=images/Part_Box.svg  style="width:16px;"> кнопку 
**Cube**
-   Выделите появившийся объёкт Куб и установите следующие параметры на вкладке **Данные**:
    -   Length: 80mm (или 8cm, или 0.8m, FreeCAD работает с любыми единицами)
    -   Width: 80mm
    -   Height: 75cm
-   Продублируйте Cube нажатием **Ctrl+C**, затем **Ctrl+V** (или в меню Правка → Дубликат)(Никаких изменений не будет видно, так как второй объект перекрывает первый.)
-   Выделите новый созданный объект под названием Cube001 (Нажмите на Куб001 в левой части вкладки Модель)
-   Смените его позицию редактированием параметра Placement:
    -   Position x: 8mm
    -   Position y: 8mm


</div>

Вы получите два высоких параллелепипеда, один в 8 миллиметрах от другого:

![](images/Exercise_table_01.jpg )

-   Теперь мы можем вычесть один из другого: выделите **первый**, который должен **остаться**, затем, с помощью нажатой кнопки CTRL, выделите **другой**, который будет **вычтен** (порядок важен), и нажмите кнопку <img alt="" src=images/Part_Cut.svg  style="width:16px;"> **Обрезать**:

![](images/Exercise_table_02.jpg )

Заметим, что вновь созданный объект, называемый \"Cut\", по-прежнему содержит два куба, использованных в качестве операндов. На деле оба куба остались в документе, просто они были скрыты и сгруппированы в древе проекта как объект Cut. Их еще можно выбрать, раскрывая стрелку у объекта Cut, и при желании можно сделать их видимыми снова, щелкнув их правой кнопкой, или изменить их свойства.

You can use the Cut tool and other Boolean tools also through \"Combo view\" with <img alt="" src=images/Part_Boolean.svg  style="width:16px;"> [Boolean](Part_Boolean.md). It gives more explicit but longer way to do it.


<div class="mw-translate-fuzzy">

-   Теперь давайте создадим три других ножки, создав 6 дублей нашего базового куба. Поскольку он уже скопирован, можно просто вставить его (Ctrl+V) 6 раз. Изменим их позиции следующим образом:
    -   Куб002: x: 0, y: 80cm
    -   Куб003: x: 8mm, y: 79.2cm
    -   Куб004: x: 120cm, y: 0
    -   Куб005: x: 119.2cm, y: 8mm
    -   Куб006: x: 120cm, y: 80cm
    -   Куб007: x: 119.2cm, y: 79.2cm


</div>


<div class="mw-translate-fuzzy">

-   Теперь сделаем три остальных выреза, выбрав сначала \"базовый\" параллелепипед, затем вырезаемый. Теперь у нас три объекта Cut:


</div>

![](images/Exercise_table_03.jpg )


<div class="mw-translate-fuzzy">

Вы могли подумать, что вместо шестикратного дублирования базового куба нам следовало дублировать полную ножку три раза. Это правда, как всегда в FreeCAD, есть много путей получить тот же результат. Это важно запомнить, поскольку по мере продвижения к более сложным объектам некоторые операции не дадут нам правильный результат и нам часто понадобится искать другие пути.


</div>


<div class="mw-translate-fuzzy">

-   Теперь сделаем отверстия для винтов, используя тот же метод Cut. Поскольку нам нужно 8 отверстий, два на каждую ножку, нам нужно сделать 8 вычитаемых объектов. Вместо этого поищем другой путь и сделаем 4 трубки, которые могут использоваться двумя ножками. Создадим четыре трубки инструментом <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> **Цилиндр**. Можно опять сделать только один и дублировать взамен. Возьмём все цилиндры радиусом 6mm. Теперь нам надо повернуть их, что так же делается параметром **Placement** на вкладке Данные *(**Примечание:** измените свойство параметра Axis*перед*установкой Angle, или поворот не будет применён)*:
    -   Цилиндр: height: 130cm, angle: 90°, axis: x:0,y:1, position: x:-10mm, y:40mm, z:72cm
    -   Цилиндр001: height: 130cm, angle: 90°, axis: x:0,y:1, position: x:-10mm, y:84cm, z:72cm
    -   Цилиндр002: height: 90cm, angle: 90°, axis: x:-1,y:0, position: x:40mm, y:-10mm, z:70cm
    -   Цилиндр003: height: 90cm, angle: 90°, axis: x:-1,y:0, position: x:124cm, y:-10mm, z:70cm


</div>

![](images/Exercise_table_04.jpg )

Как видите, цилиндры чуть длиннее, чем надо. Это потому что во всех твердотельных приложениях FreeCAD булевы операции чувствительны к ситуациям с совпадающими поверхностями и могут ошибаться. Удлинив цилиндры, мы предохраняем себя.


<div class="mw-translate-fuzzy">

-   Теперь выполним вычитание. Выберем первую ножку, затем, нажимая

CTRL, выделим один из пересекающих его цилиндров и нажмём кнопку **Cut**. Возникает отверстие, а цилиндр скрывается. Находим его в древе проекта раскрытием высверленной ножки.

-   Выделим другую ножку, которую пересекает этот скрытый цилиндр, затем повторяем эту операцию, на этот раз нажимая Ctrl во время выделения цилиндра в древе проекта, поскольку он не виден в трёхмерном виде (можно так же сделать его видимым вновь и выделить в трёхмерном виде). Повторим это для других ножек, пока каждая из них не окажется высверлена в двух местах:


</div>

![](images/Exercise_table_05.jpg )

Как видите, каждая ножка содержит длинную серию операций. Всё это остаётся параметрическим, и Вы можете в любое время изменить любой параметр любой из прежних операций. В FreeCAD мы часто называем эту последовательность как \"историю моделирования\", поскольку фактически она содержит всю историю выполненных операций.

Другая особенность FreeCAD - что концепция трёхмерного объекта и трёхмерной операции склонны к смешиванию воедино. Например, Cut это одновременно и операция, и получаемый из этого объект. В FreeCAD это зовётся \"характеристика\", вместо объекта или операции.


<div class="mw-translate-fuzzy">

-   Теперь сделаем столешницу, это будет простой деревянный массив, сделаем его как ещё один **Куб** длиной 126cm, шириной 86cm и высотой 8cm, в положении x: 10mm, y: 10mm, z: 67cm. Во вкладке **Вид** можно получить красивый коричневый, похожий на дерево цвет, изменив параметр **Shape Color**:


</div>

Теперь, когда все пять частей готовы, пришло время дать им более подходящие имена, чем \"Cut015\". Правым кликом в древе проекта (или нажатием **F2**) можно переименовать их во что-то более значимое для вас или других, кто откроет смотреть ваш файл позднее. Говорят, что правильное название ваших объектов важнее того, как Вы их получили.

-   Теперь установим болты. Теперь существует очень полезное расширение, разработанное членом сообщества FreeCAD, который можно найти в репозитории [расширений FreeCAD](https://github.com/FreeCAD/FreeCAD-addons), называемое [Fasteners (крепежи)](https://github.com/shaise/FreeCAD_FastenersWB), делающее установку винтов очень простым. Установка дополнительных верстаков легка и описывается на [странице расширений](Std_AddonMgr.md).
-   Когда вы установите верстак Fasteners и перезагрузите FreeCAD, он появится в списке верстаков, и мы сможем переключиться на него. Добавление винта в одно из наших отверстий делается через первоначальное выделение круглой грани нашего отверстия:

![](images/FastenerWorkbench.png )


<div class="mw-translate-fuzzy">

-   Теперь мы можем нажать кнопку винтов на верстаке Fasteners, например, **EN 1665 Hexagon bolt with flanges, heavy series**. Винты могут быть установлены и центрованы по нашим отверстиям, и резьба будет выбрана автоматически по размеру отверстия. Иногда болты устанавливаются в противоположном направлении, что может быть скорректировано их параметром **invert**. Мы так же можем установить их смещение на 2 мм, по тому же правилу, которое мы использовали между столешницей и ножками:


</div>

![](images/FastenerWorkbench_sel.png )

-   Повторим это для всех отверстий, и наш стол готов!


<div class="mw-translate-fuzzy">

**Внутренняя структура объектов Part**


</div>


<div class="mw-translate-fuzzy">

Как мы видели выше, в FreeCAD можно выбрать не только целый объект, но и его части, такие как круглую границу отверстия под винт. Теперь бросим быстрый взгляд на внутренне устройство объектов Part. Каждый верстак, создающий геометрию Part, будет базироваться на этом:


</div>

![](images/Tabble_alternative_complete.png )

**The internal structure of Part objects**

As we saw above, it is possible in FreeCAD to select not only whole objects but parts of them, such as the circular border of our screw hole. This is a good time to have a quick look at how Part objects are constructed internally. Every workbench that produces Part geometry will be based on these:

-   **Vertices**: These are points (usually endpoints) on which all the rest is built. For example, a line has two vertices.
-   **Edges**: the edges are linear geometry like lines, arcs, ellipses or [NURBS](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline) curves. They usually have two vertices, but some special cases have only one (a closed circle for example).
-   **Wires**: A wire is a sequence of edges connected by their endpoints. It can contain edges of any type, and it can be closed or not.
-   **Faces**: Faces can be planar or curved, and can be formed by one closed wire, which forms the border of the face, or more than one, in case the face has holes.
-   **Shells**: Shells are simply a group of faces connected by their edges. It can be open or closed.
-   **Solids**: When a shell is tightly closed, that is, it has no \"leak\", it becomes a solid. Solids carry the notion of inside and outside. Many workbenches rely on this to make sure the objects they produce can be built in the real world.
-   **Compounds**: Compounds are simply aggregates of other shapes, no matter their type, into a single shape.

In the 3D view, you can select individual **vertices**, **edges** or **faces**. Selecting one of these also selects the whole object.

**Примечание о совместном проектировании**


<div class="mw-translate-fuzzy">

Глянув на спроектированный стол, Вы можете решить, что его дизайн плох. Крепление ножек, вероятно, слабовато. Вы можете добавить усиления, или у Вас появятся другие идеи для его улучшения. Здесь появляется интерес к совместному проектированию. Вы можете загрузить файл, созданный во время упражнения по ссылке ниже, и улучшить его. Затем, если Вы поделитесь улучшенным файлом, другие смогут сделать его ещё лучше, или использовать Ваш хорошо спроектированный стол в своих проектах. Ваш дизайн может дать идеи другим людям, и, возможно, Вы немного поможете сделать мир лучше\...


</div>

**Загрузки**

-   Файл, созданный в этом упражнении: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd>

**Читать далее**


<div class="mw-translate-fuzzy">

-   [Верстак Part](Part_Workbench/ru.md)
-   [Репозиторий расширений FreeCAD](https://github.com/FreeCAD/FreeCAD-addons)
-   [Верстак Fasteners (Крепления)](https://github.com/shaise/FreeCAD_FastenersWB)


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Traditional modeling, the CSG way/ru
