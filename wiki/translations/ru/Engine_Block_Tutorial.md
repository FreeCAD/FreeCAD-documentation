---
- TutorialInfo   */ru
   Topic   * Part Workbench
   Level   * Beginner
   Time   *
   Author   *Andrewbuck40
   FCVersion   *0.14.3700
   Files   *
---

# Engine Block Tutorial/ru

 }


<div class="mw-translate-fuzzy">




</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Engine_Block_Tutorial_-_Finished_Engine_Block.png  style="width   *300px;">


</div>


<div class="mw-translate-fuzzy">

Это вводный урок моделирования в FreeCAD. Цель данного урока представить Вам первичные типы данных для параметризуемых объектов, двоичные операции, двумерное рисование и процесс преобразование двумерных набросков в трехмерные модели. В качестве рабочего примера мы будем моделировать простейший блок цилиндров и картер, показанный справа.


</div>


<div class="mw-translate-fuzzy">

## Начало

Чтобы начать, откройте FreeCAD, и выберите *Файл-\>Создать* для создания нового документа, затем *Файл-\>Сохранить* для сохранения его где-нибудь на Вашем компьютере. Я назвал свой проект \'Двигатель\'. Вы увидите, что \"древо проекта\" с левой стороны окна после его сохранения покажет имя проекта, над которым Вы работаете. У Вас может быть открыто более одного проекта одновременно и каждый проект будет показан в корне своего древа в окне древа проектов.


</div>


<div class="mw-translate-fuzzy">

## Эскизирование блока 

Теперь начнём работу над реальной моделью. Мы начнём добавлением Box в качестве контура блока цилиндров. Для этого нам надо добавить в модель *деталь*, чтобы выбрать [Part Workbench](Part_Workbench.md), перейдите на Вид-\>Верстак-\>Part. Вы увидите, что после выбора верстака Вы получите другой набор кнопок верхнего тулбара. Пройдите через несколько других верстаков для знакомства с системой верстаков, а затем вернитесь в модуль деталей.


</div>


<div class="mw-translate-fuzzy">

### Заготовка

В модуле деталей можно увидеть множество кнопок для первичных объектов вроде кубов, сфер, конусов и т.д. Нажмите кнопку Куб (<img alt="" src=images/Part_Box.png  style="width   *16px;">) для добавления куба. У каждого из перечисленных примитивов есть набор параметров, устанавливаемых при добавлении по умолчанию. Если хотите, можете добавить один из каждого вида примитивов, чтобы посмотреть, что они из себя представляют. Их можно удалить со сцены, выбрав их и нажав кнопку удаления. Есть два способа выбора объектов, Вы можете либо сделать клик левой кнопкой мыши в окне трёхмерного вида, либо сделать то же в древе проекта. И там, и там удержание кнопки CTRL позволяет выбрать несколько объектов. Вы можете приблизить трёхмерный вид прокручиванием колёсика мыши. Для сдвига вида нажмите среднюю кнопку и протащите. Для поворота вида нажмите и удерживайте среднюю кнопку и одновременно нажмите левую кнопку, тогда протаскивание мышью будет вращать вид. Можно так же кликнуть средней кнопкой где-нибудь на трёхмерном объекте, чтобы трёхмерный вид вращался вокруг этой точки. Кроме того, кнопки 1-6 и кнопка 0 на цифровой клавиатуре даст Вам различные виды этой сцены (сверху, слева, аксиометрический и так далее). Потратьте пару минут, чтобы освоиться с манипуляциями в трёхмерном окне.


</div>


<div class="mw-translate-fuzzy">


   *   *Читать далее   * [ Навигация в трёхмерном пространстве](Mouse_Model/ru.md)*


</div>


<div class="mw-translate-fuzzy">

Поставив куб и освоившись с работой с мышью, начнём устанавливать размеры модели. Выберите куб, кликнув по нему в древе проекта, затем кликните по вкладке \'Данные\' расположенного ниже *Просмотра свойств* (перейдите *Вид-\>Панели-\>Просмотр свойств*, если Вы закрыли его). На вкладке данных можно изменить свойства объекта, выделенного в древе проекта. Параметры, которые можно изменить, зависят от того, какой объект выделен. Для куба это три вектора, один для позиции в пространстве, другой для ориентации, а третий для определения размеров. Для сферы можно указать центральную точку и радиус, у конуса - радиус, высоту и позицию, и так далее. Мы создаём небольшой 2-цилиндровый блок, так что установите следующие размеры и позиции куба (убедитесь, что Вы установили XYZ для \'Position\', для \'Axis\' установили оси вращения и значения по умолчанию именно такие, как нужно)   *


</div>


<div class="mw-translate-fuzzy">


   *   {\| class=wikitable border=1

\|- \| X   * 0.0 mm \|\| Length   * 140.0 mm \|- \| Y   * -40.0 mm \|\| Width   * 80.0 mm \|- \| Z   * 0.0 mm \|\| Height   * 110.0 mm \|- \|}


</div>


<div class="mw-translate-fuzzy">

Теперь, когда наш блок цилиндров правильно образмерен, нам надо дать ему более понятное название. Выберите его в древе проекта и либо кликните правой кнопкой, либо нажмите на клавиатуре клавишу *F2*. Назовите эту деталь \'Заготовка\'.


</div>


<div class="mw-translate-fuzzy">

### Первый цилиндр 

Теперь мы вырежем первый цилиндр насквозь блока цилиндров. Для этого мы добавим цилиндр в модель с размером, который мы хотим просверлить и выполним двоичную операцию \"subtract\" вырезания материала из блока. Нажмите кнопку добавления цилиндра (<img alt="" src=images/Part_Cylinder.png  style="width   *16px;">) для его создания, выделите его в древе проекта и установите ему следующие параметры   *


</div>


   *   {\| class=wikitable border=1

\|- \| X   * 40.0 mm \|\| Height   * 110.0 mm \|- \| Y   * 0.0 mm \|\| Radius   * 25.0 mm \|- \| Z   * 0.0 mm \|\| \|- \|}


<div class="mw-translate-fuzzy">

После установки правильных параметров округлые концы цилиндра станут видны на верхней и нижней стороне блока цилиндров. Назовите это объект *Цилиндр 1*, выделив его в древе проекта.


</div>


<div class="mw-translate-fuzzy">

### Второй цилиндр 

Можно сделать второй цилиндр так же как первый, но куда проще скопировать уже сделанное для первого, поскольку единственное отличие между ними в координате X. Для этого выберите *Цилиндр 1* в древе проекта и перейдите на*Правка-\>Дубликат*. Вы увидите новый цилиндр в древе проекта (сразу названный *Цилиндр 2*), но его не видно в трехмерном виде, поскольку он находится там же, где и первый цилиндр. Выберите *Цилиндр 2* в древе проекта и поменяйте его координату X на 100 mm. Как только Вы измените число в поле данных, Вы увидите как цилиндр переместился в трехмерном пространстве. Когда второй цилиндр будет правильно помещён, можно будет поглядеть, как он выглядит, выбрав *Заготовку* в древе проекта и нажав на клавиатуре *Пробел* чтобы скрыть его (скрытые объекты становятся в древе проекта серыми). Скройте все три объекта один за другим и затем сделайте их видимыми вновь.


</div>

### Высверливание цилиндров 

<img alt="" src=images/_Engine_Block_Tutorial_-_Bored_Block.png  style="width   *300px;">


<div class="mw-translate-fuzzy">

Теперь оба цилиндра там, где они нужны для высверливания ими блока на нужные размеры. Чтобы это сделать, мы будем использовать *двоичные операции* над нашими тремя примитивами. Мы начнём с объединения двух цилиндров, чтобы мы могли вычесть их из блока как группу. Выберите *Цилиндр 1* в древе проекта, затем используйте *CTRL+LeftClick* для добавления *Цилиндра 2*. Теперь нажмите кнопку Объединения (<img alt="" src=images/Part_Fuse.png  style="width   *16px;">) для соединения объектов. В древе проектов появится новый объект под названием *Fusion*. Если Вы раскроете объект нажатием стрелки вниз возле него, Вы увидите два цилиндра, но они стали серыми. Переименуем *Fusion* в *Цилиндры*, чтобы их было легче найти потом. Теперь начнём высверливать цилиндры. Выделите *Заготовку* и *затем* выделите *Цилиндры*, потом нажмите кнопку Обрезать (<img alt="" src=images/Part_Cut.png  style="width   *16px;">). Два выбранных объекта опять объединятся, как это было с операцией объединения и единый результирующий объект будет назван *Cut* (который надо переименовать в *Высверленый блок*). Нажмите кнопку *2* на цифровой клавиатуре и Вы сможете увидеть прямо сквозь цилиндры на другую сторону блока цилиндров, затем покрутите с помощью *MiddleClick+LeftClick+Drag* для обзора блока цилиндров. Справа будет видно как выглядит конечный продукт, обратите внимание что я раскрыл вид древа проекта слева, чтобы показать отдельные примитивы и выделил *Цилиндр 2* для показа вкладки *Данные* окна *Просмотр свойств*.


</div>

### Ключевые преимущества параметрического моделирования 

Теперь, когда оба наших цилиндра высверлены, мы можем уделить минутку, чтобы поглядеть преимущества этой системы. Допустим, на каком-нибудь этапе проектирования окажется, что цилиндры надо сделать чуть больше. Поскольку выполненные операции объединения и обрезания были зафиксированы в древе проекта, мы можем изменить размер цилиндров и FreeCAD просто переделает объединение и обрезание и придёт к новому размеру двигателя. Поиграйте с радиусом и позицией цилиндра и вернитесь к предыдущим параметрам перед возвращения к уроку.

## Картер

### Заготовка и крышки подшипников 


<div class="mw-translate-fuzzy">

Далее мы будем работать над картером под блоком цилиндров. Добавьте новый блок, назвав его \"Заготовка Картера\'\', и установите следующие пропорции   *


</div>


   *   {\| class=wikitable border=1

\|- \| X   * 0.0 mm \|\| Length   * 140.0 mm \|- \| Y   * -50.0 mm \|\| Width   * 100.0 mm \|- \| Z   * -85.0 mm \|\| Height   * 85.0 mm \|- \|}


<div class="mw-translate-fuzzy">

Чтобы выделить картер от других деталей, придадим ему другой цвет. Цвет можно изменить правым кликом в древе проекта. Вы можете назначить цвет сами или дать объекту случайный цвет (выберите случайный цвет вновь, если этот цвет не понравился). Добавьте ещё один куб под названием *Выемка подшипников*, придайте им следующие параметры и вырежьте *Выемка подшипников* из *Заготовку Картера* (то есть выделив заготовку первой)   *


</div>

Add another box called **Bearing carve**, give it the following properties, and then cut the **Bearing carve** away from the **Crankcase Billet** (i.e. select the billet first)   *

   *   {\| class=wikitable border=1

\|- \| X   * 0.0 mm \|\| Length   * 140.0 mm \|- \| Y   * -40.0 mm \|\| Width   * 80.0 mm \|- \| Z   * -85.0 mm \|\| Height   * 30.0 mm \|- \|}


<div class="mw-translate-fuzzy">

Переименуем получившийся *Cut* в *Вырезанный картер*.


</div>


<div class="mw-translate-fuzzy">

### Вырезание шейки вала 

Далее мы вырежем полукруглое пространство для коленчатого вала для установки в картер и пространство для вращения вала в картере. Мы начнём с цилиндра, но ориентация цилиндра по умолчанию вертикальная, нам же нужна горизонтальная. Это значит, что нам надо понять способ вращения цилиндра для его правильной ориентации в двигателе. Глядя на направляющим осям в правом нижнем углу пространственного окна, можно заметить, что коленчатый вал лежит вдоль положительной оси X. Это значит, что его надо повернуть с начальной позиции на 90 градусов вокруг оси, параллельной к оси Y. Это показывает нам, какие параметры надо ввести для цилиндра. создайте цилиндр под названием *Выемка коленвала* и установите для него следующие параметры (обратите внимание, что нам теперь надо указать параметры направления, кроме размеров, которые мы указывали для сверления цилиндров)   *


</div>


   *   {\| class=wikitable border=1

\|- \| Axis X   * 0.0 mm \|\| Angle   * 90.0 degrees \|- \| Axis Y   * 1.0 mm \|\| \|- \| Axis Z   * 0.0 mm \|\| \|- \| Position X   * 0.0 mm \|\| Height   * 140.0 mm \|- \| Position Y   * 0.0 mm \|\| Radius   * 20.0 mm \|- \| Position Z   * -55.0 mm \|\| \|- \|}


<div class="mw-translate-fuzzy">

Вырежьте выемку коленчатого вала из *Вырезанного картера* и переименуйте итоговый объект в *Картер с шейкой вала*.


</div>

### Завершение картера 


<div class="mw-translate-fuzzy">

Под конец мы вырежем 2 финальные коробки, чтобы шатуны поршней могли проходить от картера в блок цилиндров двигателя. Сделайте два объекта под названием *Кубический вырез 1* и *Кубический вырез 2* с требуемыми размерами, объединение их в объект под названием *Кубические вырезы*, вырубить этот объект из *Картера с шейкой вала*, назвав результат *Картер*. Не забудьте, что вы можете скрыть *Высверленный блок*, выделив его и нажав пробел, чтобы видеть, что вы делаете; так же можно продублировать *Кубический вырез 1* и просто изменить координаты Х, чтобы получить второй вырез.


</div>


   *   {\| class=wikitable border=1

\|- \| X   * 15.0 mm \|\| Length   * 50.0 mm \|- \| Y   * -25.0 mm \|\| Width   * 50.0 mm \|- \| Z   * -55.0 mm \|\| Height   * 55.0 mm \|- \|}

   *   {\| class=wikitable border=1

\|- \| X   * 75.0 mm \|\| Length   * 50.0 mm \|- \| Y   * -25.0 mm \|\| Width   * 50.0 mm \|- \| Z   * -55.0 mm \|\| Height   * 55.0 mm \|- \|}

<img alt="" src=images/_Engine_Block_Tutorial_-_Crankcase.png  style="width   *300px;">

Справа можно видеть, на что похож итог. Древо проекта полностью раскрыто, так что видна вся иерархия двоичных операций создания устройства. Помните, что Вы можете пройти сквозь это древо и менять диаметр цилиндров, размер или позицию картера и так далее без переделывания всей модели с нуля. Мы можем продолжить вырезание картера, но пока этого достаточно. Далее мы посмотрим использование двумерного рисования для проектирования болтов и облегчения веса поршневого блока путём удаления лишнего металла из заготовки, который остался вокруг цилиндров.

## Двумерное черчение конструкции прокладки головки цилиндров 

For the head bolts and the shape of the engine block we will be using more boolean operations to \"carve\" away the parts of the block we don\'t want. However, if we stop to think about it, every head bolt is going to look the same, it will cut all the way down into the crankcase, the only thing different will be where on the top of the head it is located. This means we can simply \"draw\" the shape of the head gasket on the top of the engine, and then use that like a pattern to do the carving we want done.


<div class="mw-translate-fuzzy">

### Переход в режим двумерного черчения 

Для начала нам надо переключиться на верстак двумерного черчения, чтобы сделать это из режима детали, выберите *2D Drafting* из ниспадающего списка вверху, где теперь написано *Part*. Если не получается его обнаружить (не во всех верстаках он есть), можно выбрать верстак из меню *Вид-\>Верстак*. Хотя у нас двумерное черчение, мы выполняем его в трёхмерном пространстве, указывая FreeCAD, на какой плоскости должен проецироваться рисунок. После выбора верстака двумерного черчения прямо над верхним правым углом трёхмерного вида After you have selected the 2D Drafting workbench just above the top-right corner of the 3D view and click on the leftmost button which will say one of the following {none, top, front, size, or d(\..., \..., \...)}. Когда Вы его кликните, на левой стороне экрана появится текстовое поле для ввода смещения плоскости и 5 кнопок   * XY, XZ, YZ, Вид и None. Первые три означают стандартные верхний, фронтальный и боковой вид, при нажатии на *Вид* будет использована плоскость, перпендикулярная направлению взгляда камеры (плоскость обзора камеры), а последняя не проецирует на плоскость и позволяет полностью определять координаты XYZ для каждой рисуемой точки. Нам надо установить смещение плоскости на 110 (введите и нажмите Enter), затем нажмите кнопку XY для выбора плоскости XY, расположенной на 110 mm выше нуля по оси Z, что соответствует верху блока цилиндров. Когда мы указали FreeCAD плоскость для рисования, мы готовы начать проектирование прокладки головки блока цилиндров.


</div>

The last thing to do is set up the 3D view. Even though all the drawings we produce will be projected into our defined 2D plane, we can look at the plane we are drawing on from any angle (including the other side of the plane so we draw \"backwards\"). Since we have told it the plane is the one co-planar to the top of the engine block, we should probably have the 3D view looking at that, or at least roughly in that direction. Press the 2 key on the number pad to look at the top view (notice that on the num pad, adjacent keys are opposite views so 1 and 4 are front-rear, 2 and 5 are top-bottom, and 3 and 6 are right-left). Once you are looking at the engine from the top down, you can center it by dragging the middle mouse button to pan the view. Finally, the 2D drafting mode will allow us to snap parts of the drawing to the corners of the engine block, the center of the cylinders, etc, in order to make this work best we should hide the crankcase so the drawings snap only to the part we are working on (press spacebar to show/hide the selected object).

### Laying Out the Head Bolts 

Now that the proper plane projection and view is set up we add 2d drawing elements in the same way we added primitives. Click the *Add Circle* button (<img alt="" src=images/Draft_Circle.svg  style="width   *16px;">) and move your mouse around in the 3D view. You then need to tell FreeCAD the XY location for the center of the circle, and the radius, for both of these measurements you can either enter them with the mouse (following the instructions in the bottom left status bar), or you can type in the values in the text entry boxes that appear above the tree view. Go ahead and add a couple random circles on the top of the engine, as well as a few not on the engine, i.e. just out in the empty space surrounding your view of the engine. After you have done this, rotate the camera around the top of the engine block and look at the circles you drew, notice how they are \"flat\" in the plane we projected them into and this plane lines up with the top of the engine block; this will be important when we extrude the drawing to shape the engine. Now that you see how to add 2D elements you can delete the test circles you added and we will start entering the actual head layout. Note that if your circle disappears inside the engine block, your drawing projection plane is not properly set to XY mode, offset 110 mm.

Adding drafting elements with the mouse is fast and easy, but it is not very precise. For the actual bolt pattern we use the fact that moving the mouse will update the numbers in the text boxes just above the 3D view so we can see roughly the coordinates of where we want to place things. Once we have these rough coordinates we can type in the real values we want for precise positioning. Reset to the top view of the engine, click the *Add circle* button, and move your mouse around the top left corner of the engine block taking not of a good location for the head bolt. It looks like X=10, Y=30, would be a good place for the circle (note the Z coordinate should be grayed out, if it is not you need to set the plane properly like in the previous section, pressing escape will cancel drawing the circle).

Now that you see how to easily determine the coordinates of drawing elements you can easily design a bolt pattern or other 2 dimensional layout for a part such as fluid channels, circuit-board traces, etc. For our 3 head bolts let\'s on this side of the engine, let\'s use the following coordinates. Note that when you are typing in values to the boxes you can press enter to move on to the next box, and it is also a good idea to move your mouse out of the 3D view before you start typing in the coordinates as too much mouse movement will overwrite the numbers you have already entered in the text entry fields. Also, on my system I had trouble with the typed in circles having their Z coordinates set to 12.5 for some reason, if this is a problem for you, you can set the drawing projection plane to *None* and then manually enter the Z coordinates for the circles to be 110. Finally, when creating the circles, make sure to check the box labeled *Filled* otherwise when we extrude them later they will just create tubes like a toilet paper tube instead of a solid cylinder.

   *   {\| class=wikitable border=1

\|- \| X1   * 10 \|\| Y1   * 25 \|\| Radius   * 2.5 mm \|- \| X2   * 70 \|\| Y2   * 25 \|\| Radius   * 2.5 mm \|- \| X3   * 130 \|\| Y3   * 25 \|\| Radius   * 2.5 mm \|}


<div class="mw-translate-fuzzy">

Назовём эти круги *Болт 1* - *Болт 3*.


</div>


<div class="mw-translate-fuzzy">

### Другая сторона блока 

Теперь, когда первые три болта помещены на одной стороне двигателя, требуются ещё три болта с противоположной стороны, что можно сделать тремя способами   *

-   Можно продолжить добавление окружностей как мы это делали для первых трёх и просто инвертировать координату Y, чтобы поместить болты с противоположной стороны двигателя.
-   Можно выделить три уже добавленых, выбрать в меню *Правка -\> Дубликат* и инвертировать координаты Y трёх новых окружностей.
-   Использовать возможность зеркалирования из модуля Part.


</div>

Since you should already know how to do the first and second way, we will choose the third way for this example model. Each of the three methods has its own advantages and disadvantages, but a good operating rule is that simple models (like this one) probably should use the first or second methods, whereas models with lots of duplication and/or duplication of very complicated shapes/objects should probably use the third method.

So even though it is a bit of overkill we will mirror these bolts as a demonstration. Switch back to the part workbench (note that you can always switch to the *Complete* workbench to see all the tools at once if you would rather not switch back and forth (deprecated since v0.17)) by going to **View → Workbench**. Select the three bolt circles in the tree view, and then press the mirror button (<img alt="" src=images/Part_Mirror.svg  style="width   *16px;">). Once you press the mirror button you should notice a new display called the *Combo view* pop up on in the pane underneath the Tree view. Many of the tools need additional input before they can run and the Combo view lets you enter these parameters. You can make the Combo view larger by dragging the divider line separating it from the Property view up or down. Select **Bolt 1** from the list on the Combo view and set the *mirror plane* to XZ, then press OK (do the same for bolts 2 and 3).

At this point you should have a basic engine block with the cylinders bored out and the headbolt locations marked.

### Cutting Down the Excess Billet Material from the Block 

Now that we have holes marked out for headbolts (we could do the same thing for oil channels, water jackets, etc) we will want to \"trim\" the outside of the block billet down to a more suitable shape. This will make the engine lighter, allow it to cool more easily, mean less steel must be used to cast the block. Like the bolt pattern we will be laying out a 2 dimensional drawing outlining the shape we want on the finished product. We could draw the spline curve directly with the mouse, or use the hybrid approach like we used for the circles where we used the mouse to find approximate coordinates and then typed in the true values we wanted. A more interesting approach is to use the 2D drafting\'s *construction mode* to plot a few guide shapes to help us trace out a nice, symmetric, spline curve by snapping to our constructed guide shapes.

As a guide we will draw two regular polygons for each cylinder, with the polygons concentric with the cylinder. To begin, switch to the top view of the engine block, hide the crankcase, switch back to the 2D drafting workbench, select the reference plane offset to 110 mm and the XY plane mode (or the *None* mode if you prefer), and click the *Construction mode* button in the command bar (the construction mode button looks like a trowel and is located just above the top right corner of the 3D view). Construction mode works just like the normal mode except any 2D drawing objects created while in construction mode get drawn in a different color and are automatically put into a separate group in the Tree view, this allows you to hide you guide drawings and leave behind only the real things like bolt hole markings by hiding the construction group, or to delete all of the guide objects by just deleting the group.

   *   *Читать далее   * [ Режим конструирования](Draft_ToggleConstructionMode/ru.md)*

Now that your drawing plane is properly set up and you are in construction mode, click the *Regular Polygon* button (<img alt="" src=images/Draft_Polygon.svg  style="width   *16px;">) and move your mouse along the edge of the left cylinder while holding down the CTRL button. You should see that it is snapping a small black dot either to the edge of the cylinder, or to the center of the cylinder, depending on where your mouse is along the circumference. Move so that the black dot snaps to the center of the cylinder and click the left mouse button. This places the center of the polygon at the center of the cylinder, the program prompts us for the number of edges on the polygon and the radius it is inscribed in. Investigating with the mouse a little bit looks like a radius of 30 is good (so type that in) and enter 14 for the number of side, but leave the *Filled* box unchecked this time. If you can\'t get the snap to lock onto the center of the cylinder (I had trouble with mine) you can always enter the coordinates manually (X=40, Y=0, Z=110). Add a second polygon, also centered on the left cylinder but this one should have 22 side and 45 mm radius. Finally add the same two polygons over the right cylinder (centered at X=100, Y=0, Z=110). When you are finished you should have two \"figure-8\'s\" surrounding the cylinders and head bolts. (Note that currently the program does not actually prompt you for the number of edges so you will just have to set the center and radius and then change the number of faces in the Property view).

<img alt="" src=images/_Engine_Block_Tutorial_-_Spline.png  style="width   *300px;">

Now that we have our guide polygons in place we are ready to draw in the spline curve defining the outside shape of the engine block. Since this curve will be part of the final object you can turn off construction mode by clicking the same button you pressed to turn it on. Now click the *Add BSpline* button (<img alt="" src=images/Draft_BSpline.svg  style="width   *16px;">) and start drawing the BSpline by *CTRL+left clicking* on each place you want to add a control point for the spline curve. You will want your first control point to be on the leftmost point of the inner guide polygon for the left cylinder. Continue adding control points all along the spline curve until you click on the last point *before* the one you started drawing, then click the *Close* button up where you typed in the position and radius for the 2D circles we drew for the headbolts. Clicking this close button finished drawing control points for the spline curve and joins the ends together to form a closed loop. It is very important that you properly close loops like this if you plan to extrude them into solid objects like we will be with this one. For open spline curves you can just click the *Finish* button instead of the Close button when you are finished drawing. To the right you can see what you finished spline curve should look like just before you press the close button (notice I have drawn all but the last line segment and my mouse pointer is just about to click the *Close* button to finish the spline curve). Also notice that I have checked the *Filled* box so the resulting spline curve will form a solid sheet, rather than just an empty ring, this must be done to extrude it into a solid shape that is capped on the ends.

<img alt="" src=images/_Engine_Block_Tutorial_-_Spline_Edit_Mode.png  style="width   *300px;">

The control points are not shown in that picture so I have added a second screenshot showing the finished spline in edit mode (click the *Edit mode* button to turn editing on or off for the selected object, make sure to turn it off when you are done editing it or just skip over this step if you are satisfied with your engine block shape). Also, note that there is a discontinuity on the leftmost edge of the spline curve, even though it is closed properly, this is a bug in the program behavior and is currently being fixed, as a result your spline curve may look slightly different if you are running a newer version of the software than is available at this time.

### Выдавливание двумерного дизайна головок в объемную модель для завершения проекта 

Now we are closing in on the final design of the engine. Return to the Part workbench and click the *Extrude sketch* button (<img alt="" src=images/Part_Extrude.svg  style="width   *16px;">). In the combo box that pops up, use *CTRL+LeftClick* to select the 6 head bolts and the spline curve for extrusion. The default direction is the positive Z axis, we want the negative Z axis to extrude the head design \"down\" and into the engine block so set the direction to X=0, Y=0 and Z=-1, then type in 110 for the length (the height of the engine block). After you get all the values entered and click OK the circles for the bolts will be extruded downward to for cylinders and the spline will be extruded downward to produce a sort of cylinder with \"rippled\" edges. Select and hide the **Bored block** so you can see the extruded spline, then hide that object so you can see the 6 head bolt cylinders. You see that very sophisticated 3D shapes can be made by starting with a 2D drawing and extruding parts of it downward. We could even extrude different parts of the drawing by different amounts to do things like bore in bolt holes that just go part way through the block, but cut separate water jackets that go all the way through. At this point all your extruded objects are just named \"Extrude001\...\" so you will want to go through and name each of them so you can identify them in the next section (I will name mine *Head bolt bore 1* though *6* and name the spline **Extruded spline**, I suggest using the same names in your model as well). Now that you have your extruded shapes it is just a few boolean operations now to produce the final block design. Go through and show the major components (the *Bored block* and the *Crankcase*), and all your newly created extruded objects.

<img alt="" src=images/Engine_Block_Tutorial_-_Finished_Engine_Block.png  style="width   *300px;">

Now that we have 3D objects for the bore holes and the outer shape, we can use a few boolean operations to stitch the whole thing together. Select your 6 extruded head bolts in the tree view and join them into a union (name the resulting object **Head bolt boreholes**). Then select the **Bored block** and the **Head bolt boreholes** in that order and perform a cut (like you did when you bored out the cylinders), name the resulting *Cut* object **Block with headbolts**. Finally, select the **Block with headbolts** and the **Extruded spline** and press the *Make intersection* button (<img alt="" src=images/Part_Common.svg  style="width   *16px;">), and name the resulting object **Engine block**.

Your final object should look like the picture on the right.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Engine Block Tutorial/ru
