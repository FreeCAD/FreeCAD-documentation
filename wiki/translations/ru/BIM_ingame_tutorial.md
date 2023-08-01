# <img alt="" src=images/BIM_tutorial_screenshot.png  style="width:1024px;"> BIM ingame tutorial/ru


{{BIMTutorialAction
|descr=Это внутреннее руководство по [верстаку BIM](BIM_Workbench/ru.md). Он не предназначен для чтения здесь, в вики, а скорее для запуска из FreeCAD, в рабочей среде BIM, в меню '''Справка -> Обучение BIM'''. Он включает в себя ряд шагов, которые должен выполнить пользователь. Каждый шаг завершается экземпляром шаблона [<nowiki>{{BIMTutorialAction|descr|goal1|test1|goal2|test2}}</nowiki>](Template_BIMTutorialAction.md), который информирует появлении необходимых условий. Изображения должны быть 300 пикселей в ширину. На этой странице нельзя использовать изображения SVG, так как они не поддерживаются виджетом QTextBrowser.}}



### Добро пожаловать в верстак BIM! 

<img alt="" src=images/BIM_Tutorial_title.jpg  style="width:300px;">

Это руководство познакомит вас с различными функциями [верстака BIM](BIM_Workbench/ru.md) и поможет вам встать на путь, моделируя очень простое здание павильона. Это займет от одного до двух часов, в зависимости от вашего предыдущего опыта работы с 3D-приложениями.

Вы можете прервать его в любое время и возобновить его позже, выбрав меню **Справка -\> Экран приветствия BIM** и снова щелкнув элемент **Обучение BIM**.

Некоторые шаги этого руководства требуют от вас действий. Они будут указаны под этим текстовым полем со значком, показывающим, была ли задача выполнена или нет. Но поскольку мы здесь, в FreeCAD, хорошие люди, необязательно выполнять действия для продвижения по этим страницам. Вы можете просто просмотреть руководство и пропустить действия по своему усмотрению.



#### О версиях FreeCAD 

Это руководство написано для [самой последней доступной разрабатываемой версии FreeCAD](Download/ru.md) (в настоящее время 0.19). Однако инструментальные средства BIM совместимы с любой версией FreeCAD. Если вы используете более старую версию FreeCAD, чем указанная здесь, некоторые инструменты BIM могут выглядеть иначе, работать по-другому или даже быть недоступными. Обратитесь к [документации](BIM_Workbench/ru.md), чтобы узнать больше в случае сомнений.



#### Примечания

Это руководство все еще находится в стадии написания и поэтому является **неполным**! Если у вас есть предложения или что-то непонятно, почему бы не помочь нам улучшить его на [форуме FreeCAD](https://forum.freecadweb.org/viewforum.php?f=23)!


{{BIMTutorialAction|descr=На этом шаге нет действий}}

### Set FreeCAD up 

FreeCAD имеет обширную систему настроек с множеством опций для установки, расположенную в меню **Правка-\> Настройки**. Каждая дополнительная рабочая среда может добавлять дополнительные страницы настроек, что делает ее очень сложной.

Инструментальные средства BIM предоставляют [упрощенный экран настройки](BIM_Setup/ru.md), который позволяет быстро установить некоторые из наиболее полезных настроек для работы с BIM. Экран настроек BIM находится в меню **Manage -\> Настройка BIM** (вы также можете нажать соответствующую кнопку на панели инструментов):

<img alt="" src=images/BIM_Tutorial_01.jpg  style="width:300px;">

Откройте теперь упрощенный экран настроек BIM и установите различные параметры по своему вкусу.

В случае необходимости наведите указатель мыши на любой параметр или параметр, чтобы увидеть описание того, для чего он используется:

<img alt="" src=images/BIM_Tutorial_02.jpg  style="width:300px;">


<div class="mw-translate-fuzzy">

В этом уроке мы будем работать в сантиметрах. Поэтому мы предлагаем вам установить предпочтительные единицы измерения как «сантиметры», а размер квадрата сетки по умолчанию - «10 см». Эти настройки можно изменить в любое время с помощью кнопки рабочей плоскости, расположенной на основных панелях инструментов, и индикатора единиц, расположенного в строке состояния (справа внизу):


</div>

<img alt="" src=images/BIM_tutorial_14.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Открыть экран настройки BIM|test1=True if hasattr(FreeCADGui,"BIMSetupDialog") else False|goal2=Установить единицы измерения в сантиметры, а размер сетки - 10 см.|test2=True if ((FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema",0) == 4) and (FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft").GetFloat("gridSpacing",10) == 100)) else False}}



### Создать новый документ 

Если вы только что установили FreeCAD, вы, вероятно, сейчас просматриваете **Стартовую страницу FreeCAD**:

<img alt="" src=images/BIM_tutorial_13.jpg  style="width:300px;">

На начальной странице перечислены последние документы, с которыми вы работали, а на разных вкладках объясняется, как получить помощь. Но для того, чтобы начать работу, нам нужно создать новый пустой **документ**. Если вы еще этого не сделали, создайте новый документ, используя элемент «Создать новый \...» на начальной странице или перейдя в меню **Файл -\> Создать**:

<img alt="" src=images/BIM_tutorial_09.jpg  style="width:300px;">

После этого вы окажетесь в трехмерном пространстве FreeCAD и будете готовы к работе:

<img alt="" src=images/BIM_tutorial_10.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Создать новый документ|test1=True if FreeCAD.ActiveDocument else False}}



### Навигация в окне трёхмерного просмотра 


<div class="mw-translate-fuzzy">

В FreeCAD есть несколько способов взаимодействия с мышью. Они называются [стили навигации](Mouse_Model/ru.md). Вы можете изменить текущий стиль навигации в любое время, нажав кнопку стиля навигации в строке состояния. Если навести указатель мыши на эту кнопку, вы также увидите, что делает каждая кнопка мыши. Некоторые из них созданы для соответствия другим хорошо известным приложениям. Выберите тот, который вам удобен.


</div>

<img alt="" src=images/BIM_Tutorial_03.jpg  style="width:300px;">

Управлять точкой зрения на вашу модель в 3D-виде можно несколькими способами: с помощью **мыши** (в зависимости от выбранного вами стиля навигации), **клавиатуры** (изучите содержимое меню **Вид**, чтобы узнать больше), или [Куба навигации](Navigation_Cube/ru.md) (щелкайте разные стрелки и грани куба, чтобы выровнять вид).

<img alt="" src=images/BIM_Tutorial_04.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Выбрать стиль навигации|test1=True|goal2=Установить вид сверху|test2=True if FreeCADGui.ActiveDocument.ActiveView.getViewDirection().getAngle(FreeCAD.Vector(0,0,-1)) < 0.01 else False}}



### Реорганизовать интерфейс 

Все панели и панели инструментов FreeCAD можно перемещать и реорганизовывать. Панели большего размера также можно соединить, перетащив их на другую. Если ваш экран слишком мал для отображения всех панелей инструментов и их содержимого (усеченные панели инструментов будут отображаться со знаком \>\>), было бы неплохо переместить их в лучшее положение.

<img alt="" src=images/BIM_Tutorial_05.jpg  style="width:300px;">

Панели инструментов и панели также можно включать и выключать из меню **Вид**.

Инструментальные средства BIM также имеют кнопки переключения в строке состояния, которые включают и выключают дополнительные панели, такие как представление выбора, представление отчета и консоль Python. Эти панели часто полезны при работе с FreeCAD, но они занимают драгоценное место на экране. Обычно вы можете выключить все, пока они вам не понадобятся. Помните, что сообщения об ошибках печатаются в окне отчета, поэтому, если что-то пойдет не так, обязательно загляните туда.

<img alt="" src=images/BIM_tutorial_17.jpg  style="width:300px;">


{{BIMTutorialAction|descr=На этом шаге нет действий}}



### Инструменты верстака BIM 

[Верстак BIM](BIM_Workbench/ru.md) содержит инструменты, заимствованные из других инструментальных средств, таких как [Arch](Arch_Workbench/ru.md), [Draft](Draft_Workbench/ru.md) или [Part](Part_Workbench/ru.md), а также несколько собственных инструментов. Они разделены на несколько категорий. У каждой категории есть меню и панель инструментов. Найдите минутку, чтобы изучить содержание меню, описанного ниже.



#### Двумерное черчение 

Эти инструменты позволяют рисовать плоские объекты, такие как линии, полилинии, прямоугольники, дуги и т.д., которые станут основой ваших объектов BIM. Например, вы можете использовать полилинию, чтобы определить базовую линию стены, или прямоугольник как профиль балки. Все двумерные объекты создаются в текущей [рабочей плоскости](Draft_SelectPlane/ru.md).

<img alt="" src=images/BIM_Tutorial_35.jpg  style="width:300px;">



#### Трёхмерное моделирование и BIM 

Эта категория содержит инструменты для создания объектов BIM, таких как [стены](Arch_Wall/ru.md) или [окна](Arch_Window/ru.md), а также общие, не-BIM трёхмерные объекты, такие как [кубы](BIM_Box/ru.md), которые можно превратить в объекты BIM позже. Результат будет другим, используете ли Вы инструмент с выбранным объектом или нет. Если нет, Вам будет представлен интерфейс создания. Если вы выбрали объект перед запуском инструмента, объект соответствующего типа будет создан с использованием выбранного объекта в качестве основы.

<img alt="" src=images/BIM_Tutorial_33.jpg  style="width:300px;">

Типичный пример - нажатие кнопки [стена](Arch_Wall/ru.md) с выбранной [линей](Draft_Line/ru.md) или [полилиния](Draft_Wire/ru.md). Стена будет создана автоматически с использованием линии или полилинии в качестве базовой линии.

Объекты, не относящиеся к BIM, включая объекты, созданные в других инструментальных средствах, всегда можно превратить в объекты BIM, выбрав их и нажав любую из кнопок инструментов BIM.



#### Аннотации

Эти инструменты создают объекты аннотации, такие как размеры, текст, метки или сетки, используемые не для моделирования, а для аннотирования ваших моделей и создания понятных чертежей.

<img alt="" src=images/BIM_Tutorial_34.jpg  style="width:300px;">



#### Привязки

Эти инструменты включают/выключают [привязку](Draft_Snap/ru.md) к позиции. Как и в большинстве приложений BIM, каждая дополнительная позиция привязки увеличивает время расчета при рисовании, поэтому лучше оставить включенными только те, которые вам нужны.



#### Модификация

Эти инструменты изменяют существующие объекты. Они содержат обычные инструменты преобразования, такие как «Перемещение» или «Поворот», а также ряд других, которые работают только для определенных типов объектов.



#### Управление

Эта категория содержит общие инструменты управления. Большинство из них позволяют редактировать BIM-свойства большой группы объектов одновременно, без необходимости их выбора.

У каждого инструмента, содержащегося в этих меню, есть собственная страница документации, на которой подробно описано, как он работает и какие параметры доступны. Они перечислены на странице [Документация по верстаку BIM](BIM_Workbench.md), которая также доступна из меню **Справка** или через меню **Справка -\> Что это?** и нажатие любой кнопки на панели инструментов.


{{BIMTutorialAction|descr=На этом шаге нет действий}}



### Подготовка рабочего места 

В FreeCAD есть много способов создавать объекты BIM. Вы можете использовать [инструменты верстака BIM](BIM_Workbench/ru.md) или любой другой инструмент FreeCAD из другого [верстака](Workbenches/ru.md). Все инструменты верстака BIM, как двумерного рисования, так и трёхмерные, в отличие от других верстаков, таких как Part Design, широко используют **рабочие плоскости** и **привязку**.


<div class="mw-translate-fuzzy">

[Рабочая плоскость](Draft_SelectPlane/ru.md) - это место, где будут созданы ваши следующие объекты. Вы можете установить его на одну из основных ортогональных плоскостей (земля, фронт, бок) или использовать любую выбранную грань для определения текущей рабочей плоскости. Вы также можете использовать [Прокси рабочей плоскости](Draft_SetWorkingPlaneProxy/ru.md) из меню **Утилиты**, чтобы сохранить определенное положение рабочей плоскости внутри вашей модели. [Строительные детали](Arch_BuildingPart/ru.md) также содержат неявное положение рабочей плоскости. Изменение текущей рабочей плоскости выполняется нажатием кнопки рабочей плоскости на панели инструментов BIM. **Сетка** всегда показывает, где находится рабочая плоскость.


</div>

Как вы заметили, угол обзора и рабочая плоскость не связаны друг с другом. Вы можете работать на своей рабочей плоскости под любым углом обзора.

Теперь установите рабочую плоскость в режим «Сверху»:

<img alt="" src=images/BIM_Tutorial_06.jpg  style="width:300px;">

[Инструменты привязки](Draft_Snap/ru.md) позволяют размещать новые объекты и точки точно в соответствии с существующей геометрией. Однако включение многих мест привязки может замедлить операции рисования, поэтому разумно включать только те инструменты привязки, которые вы собираетесь использовать. Найдите минутку, чтобы просмотреть, что делает каждый из них, чтобы при необходимости вы знали, какие из них можно отключить.

<img alt="" src=images/BIM_Tutorial_07.jpg  style="width:300px;">

Обратите особое внимание на последний инструмент, инструмент «Привязка рабочей плоскости», так как он заставляет точки привязки ложиться на плоскость обработки, таким образом предотвращая привязку над или под плоскостью обработки. Вам часто придется включать или выключать его, в зависимости от выполняемой операции.


{{BIMTutorialAction|goal1=Установите рабочую плоскость в режим «Сверху» (XY).|test1=True if ((FreeCAD.DraftWorkingPlane.axis.getAngle(FreeCAD.Vector(0,0,1)) < 0.01) and (FreeCAD.DraftWorkingPlane.weak == False)) else False|goal2=Обзор различных инструментов привязки|test2=True}}



### Проведём первую стену 


<div class="mw-translate-fuzzy">

Начнем строить павильон со стен. Стены можно нарисовать либо напрямую с помощью инструмента [стена](Arch_Wall/ru.md), либо сначала нарисовав 2D-объекты, такие как [линии](Draft_Line/ru.md), [полилинии](Draft_Wire/ru.md) или \[\[Sketcher_NewSketch/ru\|эскизы\] \], которые будут определять базовую линию наших стен. Когда у вас выбран такой базовый объект, нажатие инструмента «Стена» автоматически преобразует его в стену.


</div>

Сначала масштабируйте, пока не будет видна большая часть или вся сетка. Так будет легче видеть, что мы делаем:

<img alt="" src=images/BIM_tutorial_15.jpg  style="width:300px;">

Затем нажмите на панели инструментов кнопку <img alt="" src=images/Arch_Wall.png  style="width:16px;"> **Стена** (или выберите пункт меню **3D/BIM -\> Стена**). Щелкните две точки на сетке, выровненные по вертикали, на расстоянии 300 см друг от друга. Нажатие SHIFT после нажатия первой точки поможет вам сохранить стену в горизонтальном или вертикальном положении. Боковая панель сообщит вам длину стены во время рисования.

<img alt="" src=images/BIM_tutorial_16.jpg  style="width:300px;">

Если вы создали не ту стену, не беспокойтесь! Просто удалите или отмените его (меню **Правка -\> Отменить**) и повторите попытку.


{{BIMTutorialAction|goal1=Создать стену|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList]) == 1)}}



### Проведём вторую стену 

Сделайте вторую горизонтальную стену длиной 4 метра (или 400 сантиметров). Снова выберите инструмент <img alt="" src=images/Arch_Wall.png  style="width:16px;"> **Стена**, панорамируйте и масштабируйте, пока не увидите нужную область сетки, и выберите две точки из сетки, чтобы определить начало и конечные точки новой стены:

<img alt="" src=images/BIM_tutorial_11.jpg  style="width:300px;">

After they are created, select both walls by pressing CTRL and clicking them both in the 3D view or in the [tree view](Document_structure.md), and adjust their **height** property to 2.5 meters and their **width** to 20 centimeters (or any other measurement you are comfortable with, if working in another unit), so they look like this (Use the mouse to rotate the view, according to the navigation style you choose):

<img alt="" src=images/BIM_tutorial_08.jpg  style="width:300px;">

You can always correct or change properties after a wall or any other BIM object has been created. By expanding the wall object in the tree view, then double-clicking the baseline of the wall, you can also modify its base 2D object. Most BIM objects in FreeCAD are based on another object, such as a baseline or a profile.

<img alt="" src=images/BIM_tutorial_12.jpg  style="width:300px;">

#### Important note 

You will notice that some property changes, in FreeCAD, don\'t reflect immediately on the object in the 3D view. Instead, the object is marked with a \"to be recomputed\" blue mark in the tree:

<img alt="" src=images/BIM_Tutorial_20.jpg  style="width:300px;">

The reason for this is that a FreeCAD document can be a very complex chain of inter-dependent objects. Updating one can trigger an update on many others, and therefore take a long time. To avoid this, some operations simply mark the object to be recomputed, and you trigger the recomputation yourself by using menu **Edit -\> Refresh** or pressing **Ctrl+R**.


{{BIMTutorialAction|goal1=Create two orthogonal wall objects|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList]) == 2)|goal2=Set their height to 2.50 meters and width to 20 centimeters|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList and o.Height.Value == 2500 and o.Width.Value == 200]) == 2)}}

### Don\'t forget to save the file regularly! 

Like any other computer application, FreeCAD is subject to failing or crashing, specially when we have little experience with it. Saving your file often is a very good habit to take in these early moments. FreeCAD also has an auto-saving mechanism, that you can set up under menu **Edit -\> Preferences -\> General -\> Document**.

Save your file now by using menu **File -\> Save**.


{{BIMTutorialAction|goal1=Save your file|test1=bool(FreeCAD.ActiveDocument.FileName)}}

### Draw a roof slab 

We will now place a roof slab on top of our walls. Instead of drawing the slab directly, like we did with the walls, we will here first draw a rectangle, then turn the rectangle into a slab. We will now explore two methods to do so, both are useful to know, so we suggest you to try one first, then undo it (or reload the file), and try the other method.

#### Method 1: Draw the slab on the ground, then move it into position 

It is often convenient to consider the top XY plane (the ground plane) as a kind of \"drawing board\", where we will be building our objects, and move then next to their correct position. There is an additional advantage here, our working plane is already in \"Top\" mode, so we don\'t need to change it.

Set yourself in top view, zoom out a bit until you see both walls, and draw a rectangle encompassing them both. Press the <img alt="" src=images/Draft_Rectangle.png  style="width:16px;"> **Rectangle** button from the toolbar (or choose menu item **2D Drafting -\> Rectangle**):

<img alt="" src=images/BIM_Tutorial_18.jpg  style="width:300px;">

Rotate your view to inspect the results. By default, the rectangle is filled with a face. This can be changed by changing the **Make Face** property of our rectangle to False. For the slab we are going to build, this has no impact, for other types of objects, however, the base object being a polyline or a face can make a difference.

<img alt="" src=images/BIM_Tutorial_19.jpg  style="width:300px;">

The next step is to build a slab by *extruding* it with our rectangle as its base *profile*. In FreeCAD, structural objects such as columns, beams or slabs are all made with a same object, called **Structure**. After a structural object is created, setting is **IFC Type** property to the desired type (column, slab, etc\...) is all that is needed to change its type.

Make sure our rectangle is selected, then press the <img alt="" src=images/BIM_Slab.png  style="width:16px;"> **Slab** button from the toolbar (or choose menu item **3D/BIM -\> Slab**). As stated above, this can also be done with the Column or Beam tools, as they all produce the same type of object. After our object is created, we need to make the following changes to its properties:

-   Set its **Height** to **20 cm**
-   Verify its **IFC Type** is set to **Slab**

Now we need to move our new roof slab to its correct position, that is, above the walls. So we need to move it upwards, in the Z direction, by a distance of 250 cm, which is the height of our walls. We can simply edit the **Placement** property of our slab, expand its **Position** attribute, and set the value of **z** to 250 cm. Our slab is now well in place:

<img alt="" src=images/BIM_Tutorial_21.jpg  style="width:300px;">

Another way to move our slab to its correct position, is to use the <img alt="" src=images/Draft_Move.png  style="width:16px;"> **Move** tool from the **Modify** menu. For that, we need to set our working plane in a vertical plane first, by pressing the <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> **working plane** button (make sure you don\'t have any face selected), and setting it to **XZ (Front)**. By setting ourselves in front view (press key **1**), we can now select the slab, press the <img alt="" src=images/Draft_Move.png  style="width:16px;"> **Move** button, and move our slab by clicking one of its base points, and, with **Shift** pressed to restrict the movement vertically, click one point on top of the walls:

<img alt="" src=images/BIM_Tutorial_23.jpg  style="width:300px;">

#### Method 2: Draw the slab directly in the correct plane 

Another useful method is directly working on the intended plane. We can easily set the working plane to the top surface of the walls, which is where we want our slab. Selecting a face and pressing the <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> **working plane** button sets the working plane to coincide with the selected face. Select the top face of the wall and set it as the current working plane. The placement of the grid moves to show the current working plane.

<img alt="" src=images/BIM_Tutorial_22.jpg  style="width:300px;">

Everything we draw from now on will happen in that plane. If you like, you can now set yourself in top view, but this is not necessary. Once your working plane is set, and if **working plane snapping** is enabled, you can draw directly in any type of 3D view.

Once our rectangular *profile* is drawn, we can follow the same method as in method one to create a slab (select it, press the **Structure** button, adjust its properties).


{{BIMTutorialAction|goal1=Create a rectangle|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Rectangle" in o.Name]) == 1)|goal2=Create a 20cm thick slab|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "IfcType" in o.PropertiesList and o.IfcType == "Slab" and o.Height.Value == 200]) == 1)}}

### Create a metallic column 

Let\'s add a metallic column to give better support to our slab. Make sure the working plane is in Top mode, let\'s start by putting ourselves in top view (press key **2**), and turn the slab off, so we see better what\'s underneath. Select the slab, and press the **Space** key to turn its display off.

In FreeCAD, it is very easy to turn objects or groups on and off, and the tree shows you clearly what is shown and what is hidden. Be sure to use that often!

The **Column** tool (as well as the Beam tool) has some built-in profiles that we will use now. Make sure nothing is selected, then press the Column button. In the **Structure options**, select **CHS** (for \"Circular Hollow Section\"; RHS is \"Rectangular Hollow Section\", HEA, HEB, etc. are various \"H\" sections, etc.):

<img alt="" src=images/BIM_Tutorial_24.jpg  style="width:300px;">

And click a point to place your column, more or less at this position. Make sure the new column has an IFC Type of \"Column\" and give it a Height of 250cm to make it the same height as our walls.

<img alt="" src=images/BIM_Tutorial_25.jpg  style="width:300px;">

Unfortunately, the CHS preset has only one diameter option of 42mm, which is very thin to support our concrete roof slab. Fortunately, as everything is parametric, it is easy to change the diameter. Expand the new structural object in the tree view, and you will find its profile object, named CHS423. Change its diameter to 12cm and its thickness to 8mm. Now we have a strong enough column. Notice that you can specify units on the fly and switch between 0,8cm and 8mm without issue. FreeCAD will take care of conversion.

#### Add a support plate 

We need a way to attach our metal column to the concrete slab. So let\'s add a plate to its top, which can be bolted to the concrete slab. This will illustrate how you can easily modify BIM objects and create the very precise ones you need.

Let\'s start by changing the height of our column from 250cm to 249cm, to give it a space for a 1cm-thick plate. Then draw a 20cm x 20cm rectangle, either on the ground plane or by setting the top of the column as the current working plane, as we learned in the previous step. Use the **Move** tool, with midpoint and center snaps turned on, if needed, to center the rectangle over the column center.

Using the Slab tool again, create a structural object from the rectangle, give it a height of 1cm, and move it to a height of 249cm:

<img alt="" src=images/BIM_Tutorial_26.jpg  style="width:300px;">

Now let\'s add our plate to the column. BIM objects in FreeCAD have two properties named **Additions** and **Subtractions** that can receive objects that need to be unioned or subtracted to/from them. To add the plate to our column, select the plate, then, with **Ctrl** pressed, select the column and use the <img alt="" src=images/Arch_Add.png  style="width:16px;"> **Add** tool from the **Modify** menu. Our plate is now part of the column:

<img alt="" src=images/BIM_Tutorial_27.jpg  style="width:300px;">

By starting from simple shapes as *profiles*, and adding or subtracting objects, we can quickly create very complex BIM objects. Note that the Additions and Subtractions of a given BIM object can easily be changed by double-clicking them in the tree view and using the Add and Remove buttons there. Also, a same object can be used as an addition or subtraction to multiple other objects.

<img alt="" src=images/BIM_Tutorial_28.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Create a CTH tubular column|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "CTH" in o.Label]) == 1)|goal2=Add a 20cm x 20cm plate to the column|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Shape" in o.PropertiesList and (abs(o.Shape.Volume - 7409000) < 10000)]) == 1)}}

### Add a door 

Like columns and beams, doors and windows are created with a same [Window](Arch_Window.md) object in FreeCAD. Only their IFC type changes. They can be independent or, if an object is selected when running the tool, inserted in another BIM object, in which case they will automatically create a hole through it.

Let\'s insert a 80cm x 210cm glass door in one of our walls. Start by placing the working plane on a face of a wall, which will make it easier to precisely place our window:

<img alt="" src=images/BIM_Tutorial_29.jpg  style="width:300px;">

Then, with the wall selected, select **Door** from the **BIM** menu. Select the **Glass door** preset, and set the **Width** to 80cm and **Height** to 210cm. You can set the other values as you like:

<img alt="" src=images/BIM_Tutorial_30.jpg  style="width:300px;">

Click a point on the base of the wall where you wish to place the window. This can be difficult, as the grid lines don\'t necessarily correspond to the wall edges. Press the **Q** key while you have an active snap at a grid intersection, and press it again with an active snap on the bottom of the wall. FreeCAD will create a new snap point where their horizontal/vertical axis intersect. Use this to find a suitable point:

<img alt="" src=images/BIM_Tutorial_31.jpg  style="width:300px;">

If your door didn\'t get placed correctly, try the **Move** tool to move it to its correct position. Otherwise use undo or delete it from the model tree and try again.

When everything is done, you should obtain a door properly inserted into its wall:

<img alt="" src=images/BIM_Tutorial_32.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Create a glass door|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Window" in o.Name]) == 1)}}

### Organizing our model 

We now have in our model a growing collection of BIM objects. It is time to tidy things up. Creating well organized models, easily understandable by others, is a very important part of building quality BIM models.

A first very simple and very good habit to take is to give proper and meaningful names to our objects, so we can easily identify them in the tree view later on. To rename an object, right-click it in the tree view and choose **Rename**. A model where components are easily identifiable by others is a huge part of what makes a good BIM model.

Another interesting operation to do is **grouping**. Groups allow you to organize your objects in the tree view, like files and folders. An object can only belong to one group. Groups are created by right-clicking the document root or any other group in the tree view, and selecting **Create group**. You can then drag objects in and out of groups in the tree view.

A third way to organize things is by using layers. Layers are independent of groups, you can use both systems at the same time if you wish. Like groups, layers allow you to easily turn on/off a series of objects, but unlike groups, they cannot be stacked inside one another. They also allow you to override visual settings such as the color and line width of their child objects. Layers are created and managed using the Layers manager tool found under menu **Manage -\> Layers manager**. Objects are added or removed by dragging them in and out of layers in the tree view.

The **Layer selector** on the main toolbar allows you to set a current layer. After doing so, any new 2D or BIM object will automatically be placed in that layer.

Finally, BIM applications usually allow you to group objects into **levels** (or storeys) and **buildings**. FreeCAD offers these tools as well under the **3D/BIM modeling** menu. Like beams and columns, levels and buildings use a same object type called [Building Part](Arch_BuildingPart.md) with a different IFC type. They work the same way as groups, once created, you can drag and drop any object in and out of it. Building Parts are compatible with groups, so you can place groups inside them.

<img alt="" src=images/BIM_Tutorial_36.jpg  style="width:300px;">

Building Parts have many other uses, refer to their [documentation](Arch_BuildingPart.md) to know more.

Create a Building Part now by selecting **Level** from the **3D/BIM Modeling** menu. Make sure its IFC type is set to **Building Storey**, and drag all our other root BIM objects (no need to do so with included objects like the door or the plate of the column) into it, that is, our two walls, the roof slab and the metal column.

Note that, as Building Parts are generic building components, you are not forced to organize your model by levels in FreeCAD. You can choose to group your elements differently. But the IFC format expects things to be grouped by level, so if you plan to use that format, it is best to consider your Building Parts as levels.


{{BIMTutorialAction|goal1=Create a level|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "BuildingPart" in o.Name]) == 1)|goal2=Add the four other root BIM objects to it|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "BuildingPart" in o.Name and (len(o.Group) == 4)]) == 1)}}

### Adding section planes 

One of the most commonly operations done with a BIM model is to extract 2D drawings from it, such as plans or elevations. There are several ways to do that in FreeCAD, depending on the result you wish to obtain. Basically, you can choose between producing the 2D result inside the 3D space, which is useful if you wish to rework it there, build further on it or better control how it is exported to formats like [DXF](Draft_DXF.md) or [DWG](FreeCAD_and_DWG_Import.md), or on a [TechDraw sheet](TechDraw_Workbench.md) that is better suited for impression or export to PDF. In both cases, it starts with placing a [Section Plane](Arch_SectionPlane.md) in your model:

<img alt="" src=images/BIM_Tutorial_37.jpg  style="width:300px;">

1.  Select the Level object that contains your objects, that we created in the last step
2.  Add a Section Plane from menu **Annotations-\>Section Plane**

Section planes don\'t cut through the whole model, but only through objects in their **Objects** property. You can select the Section Plane to check and change the contents of this property anytime.

By default, the new section plane will be placed in the middle of the selected object or its contents, and will look downwards, as to create a floor plan view. But the section plane is an object like any other and can be moved and rotated to do what you need. Place it horizontally to create a plan view, vertically inside your model to create a section, or outside the model to create an elevation.


{{BIMTutorialAction|goal1=Select the main Building Part|test1=bool(len([o for o in FreeCADGui.Selection.getSelection() if "BuildingPart" in o.Name]) == 1)|goal2=Create a section plane|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Section" in o.Name and (len(o.Objects) == 1) and ("BuildingPart" in o.Objects[0].Name)]) == 1)}}

### Extracting 2D views as geometry 

Once your section plane is in place, we can now create 2D geometry from what it sees using the [Shape2DView](Draft_Shape2DView.md) tool:

<img alt="" src=images/BIM_Tutorial_38.jpg  style="width:300px;">

1.  Select the section plane
2.  Create a Shape 2D View using **Modify-\>Shape 2D View**
3.  Our view object is hidden under the walls. Turn the display of the level and the section plane off by selecting them both in the tree view and pressing the **Space** key, so we can view our result better

<img alt="" src=images/BIM_Tutorial_39.jpg  style="width:300px;">

The 2D view we created is a all-in-one 2D object and will be located on the (0,0) ground plane in the model. It can be moved around, and will be recalculated if the model changes.

To create thicker lines for cut areas, you can create another Shape 2D view, and set its **Projection Mode** property to \"Cutlines\" or \"Cutfaces\", and its **In Place** property to \"False\". You will then have two objects, one for viewed lines and one for cut lines, for which you can give different line thicknesses.


{{BIMTutorialAction|goal1=Select the section plane|test1=bool(len([o for o in FreeCADGui.Selection.getSelection() if "Section" in o.Name]) == 1)|goal2=Create a Shape 2D View|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Shape2DView" in o.Name]) == 1)}}

### Annotating and exporting to 2D CAD formats 

You can place [Texts](Draft_Text.md), [Labels](Draft_Label.md) (text with line and arrow), [Dimensions](Draft_Dimension.md) on anything in the model space: Either directly on the 3D model, or on the 2D view that we created in the step above. The choice is yours, depending on what you wish to achieve. If you leave the 2D view exactly under the 3D model, you might also want to do both in one go.

![](images/BIM_Tutorial_34.jpg )

Annotations (texts, labels, dimensions) will be placed on the current **Working Plane**. Be sure to place your working plane where you want your annotations. You can this way place annotations in any plane of the 3D space: Horizontally or vertically. You can also move or rotate them after creation.

Let\'s place a horizontal dimension between the extremities of our two walls:

![](images/BIM_Tutorial_40.jpg )

1.  Set the **working plane** to **Top** position
2.  Orient your view to be able to view the base of both walls
3.  Choose menu **Annotations -\>** <img alt="" src=images/Draft_Dimension.png  style="width:16px;"> [Dimension](Draft_Dimension.md)
4.  Click a first point at the extremity of the left wall
5.  Press **SHIFT** to constrain the dimension vertically or horizontally
6.  Click a second point at the extremity of the right wall
7.  Click a third point to indicate where to place the dimension line

[Dimensions](Draft_Dimension.md) have a lot of settings to tweak their aspect and the size and type of the text and arrow. You can set your preferred defaults under menu **Edit-\>Preferences-\>Draft-\>Text and Dimensions**.

Now let\'s add a text:

![](images/BIM_Tutorial_41.jpg )

1.  Choose menu **Annotations -\>** <img alt="" src=images/Draft_Text.png  style="width:16px;"> [Text](Draft_Text.md)
2.  Click a location in the 3D view to place the text
3.  Write the text you wish, for example **Pavilion**, then click the **Create Text** button or press Enter twice.

A good idea is to create **Groups** for the different sets of annotations (plan, section, different scales, etc\...):

1.  Create a group by right-clicking the document root and select **Create group**, rename it to \"Annotations\"
2.  Select the annotations we created above in the tree and drag and drop them into the group

#### Exporting to DXF 

2D objects such as lines or circles or 2D views as we created above or annotations are very suited to export to traditional 2D CAD formats such as [DXF or DWG](Draft_DXF.md). The DWG format requires an additional piece of software to be installed on your system, check the [instructions](Draft_DXF.md) to do that if needed.

Let\'s try to export our 2D work to DXF:

1.  Select the 2D view, the dimension and the text
2.  Select menu **File-\>Export**, choose the **Autodesk DXF**format, a file name, and press **Export**

If you don\'t use any 2D CAD program, there are several free and open-source applications that can open DXF files (apart from FreeCAD itself, of course!) such as [LibreCAD](https://librecad.org/) and [QCAD CE](https://qcad.org/).

![](images/BIM_Tutorial_42.jpg )


{{BIMTutorialAction|goal1=Create a dimension|test1=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Dimension" in obj.Name]))|goal2=Create a text|test2=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Text" in obj.Name]))}}

### Creating 2D geometry on a printable sheet 

Printable sheets are created and managed with the [TechDraw Workbench](TechDraw_Workbench.md). Let\'s create a new sheet and place a view of our model on it:

1.  Switch to the **TechDraw Workbench**
2.  Create a new empty sheet using the default template from menu **TechDraw -\> Insert default page**
3.  Select the section plane and create a view on the page using **TechDraw -\> Insert Arch Workbench Object**
4.  Change the **Scale** property of your Arch View and recalculate the model (F5) to see your changes.

\... To be continued


{{BIMTutorialAction|descr=No action to perform for this step}}

### Exporting an IFC file 

The [IFC, or Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes), is a protocol and file format aimed at interchanging BIM model between applications. By saving your model as an IFC file, you will be able to open it in most or all other open-source or proprietary BIM applications out there.

IFC import/export operations in FreeCAD are performed by an external piece of software called [IfcOpenShell](http://www.ifcopenshell.org/). Read the [Arch IFC](Arch_IFC.md) page to learn further about how to install it.

Once IfcOpenShell is installed, exporting your model as an IFC file is as simple as selecting the objects you wish to export, or just the top container (group or Building Part) that contains all other objects you wish to export, and use menu **File-\>Export** and choose the IFC file format.

Finally, once you have exported an IFC file, it is always a good idea to inspect it before sending it to other people, to make sure the model looks good and no object is missing. There are many free IFC viewer applications available on the internet for many platforms. A good, open-source viewer that works on all platforms is [IFC++](http://ifcquery.com/). If you want to use the IFC file for further editing [Blender BIM Add-on](https://blenderbim.org/) might be useful.

To test the structure and validity of your model for IFC export run the **Manage-\>IFC Preflight** tool. This will be discussed in the next section.


{{BIMTutorialAction|goal1=Open the BIM preflight tool and run all the tests|test1=True if (hasattr(FreeCADGui,"BIMPreflightDone") and (FreeCADGui.BIMPreflightDone == True)) else False}}

### Managing BIM properties 

A huge part of what makes a good BIM model are the non-geometry properties that you can give to your objects, such as type, material, or properties specific to a certain type. For example, a wall can be marked as load-bearing or not. Or as exterior or interior. The [IFC format](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) is very rich in that regard. The amount of specifications and properties you want to give your objects depends mostly on your needs and how you work with others and what they expect your BIM model to contain.

One thing is important to keep in mind: all BIM/Arch objects in FreeCAD support the full set of IFC properties. Other FreeCAD objects, such as those modeled with other workbenches, will also be exported to IFC but you cannot change any of their IFC properties. You can however convert any FreeCAD object to a BIM object by selecting the object and using **3D/BIM -\> Create Component**.

The main pieces of information you can give your objects are:

#### Name and description 

This seems obvious, but the simplest way to make your model more understandable to others is to properly name each of your objects, and, if relevant, add a description. This is done simply by selecting an object, and pressing **F2**, or change its **Label** property to rename it. The Description will be found among the object properties.

#### The BIM/IFC type 

This is the most fundamental piece of information. In FreeCAD, an object created with the wall tool will have its IFC type set to \"Wall\" by default. But you can change this anytime. So you can use the wall tool to model a beam for example. You only need to change its IFC type after creating it. To change the IFC type of an object, select it, find its **IFC Type** in its properties, and change to another type from the drop-down list.

You can also bulk-manage names, types and materials of several objects at a time using the IFC elements manager found under menu **Manage-\>IFC elements**.

#### Materials

Each object of a construction has a material. So it makes sense to give each object of your model a proper material, such as concrete or wood. To attribute a material to an object, select the object, and use the [materials manager](Arch_SetMaterial.md) from menu **Manage-\>Materials**.

#### Properties

Each BIM object can also receive additional properties, for example to indicate that a wall is load-bearing or not. IFC allows you to add custom properties to just anything, but most types such as Wall or Beam also have special, predefined sets of properties, usually named Pset_WallCommon or Pset_BeamCommon. You can choose to add these sets to your objects, modify the value of the properties contained in the set, or add your custom properties. Managing the IFC properties for a selected object or bulk edit the properties of several objects at a time is done using the properties manager under menu **Manage-\>IFC properties**.

#### Quantities

Quantities such as length or width or height of a wall can also be specifically written to an IFC file. They are not linked to the geometry of the object, so when meeting such quantities in an IFC file there is no guarantee that they reflect the actual object geometry. However, these quantities allow applications that are not able to process the geometry, such as spreadsheet applications, to know the principal dimensions of objects. You can check which quantities will be exported to IFC using the quantities manager found under menu **Manage-\>IFC quantities**.

The IFC format has many particularities and sometimes the application you will be opening your IFC file with or the person who will receive your IFC file will have further requirements. Becoming a fluent BIM modeller often means to get familiar with all these particularities and what needs to be added or specified to your BIM model. The BIM workbench of FreeCAD provides a [BIM Preflight](BIM_Preflight.md) tool that allows you to check your model for several of these particularities and most common requirements, and help you decide what to include in your model or not.


{{BIMTutorialAction|descr=No action to perform for this step}}

### Explore other BIM tools and other workbenches 

Take a moment to explore the other available BIM tools. Remeber that some are still not finished, and might not do everything you expect from them. Use the \"What\'s this?\" button found in menu **Help** to open the help page of any tool. The [FreeCAD forum](https://forum.freecadweb.org) is also always a good place to search or ask when encountering a specific problem you cannot solve.

FreeCAD is a big family of workbenches, and tools from other workbenches often come in handy. As we saw above, almost any object created from other workbenches can be turned into a valid BIM object, simply using the **3D/BIM -\> Create component** tool and giving it the correct IFC type.

There are more tutorials about BIM and other workbenches in the [Tutorials](Tutorials.md) section of the [FreeCAD documentation](https://wiki.freecadweb.org), and a complete video series of [BIM tutorials](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU) on youtube.


{{BIMTutorialAction|descr=No action to perform for this step}}

### Help FreeCAD to become a better tool! 

FreeCAD is free software, developed by an enthusiast community of users, some of them developing code, and many others contributing in one form or another to make the software better, being writing documentation, finding and reporting bugs, submitting ideas, writing tutorials, and many other things. The more and more active we are, the faster the software gets developed further. Why not join us? A good place to start is the [BIM section on the FreeCAD forum](https://forum.freecadweb.org/viewforum.php?f=23). See you there!


{{BIMTutorialAction|descr=No action to perform for this step}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Tutorials](Category_Tutorials.md) > BIM ingame tutorial/ru
