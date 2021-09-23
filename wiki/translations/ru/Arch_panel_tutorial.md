# Arch panel tutorial/ru



{{TutorialInfo/ru
|Topic= Моделирование архитектурной панели
|Level= Начинающие
|Time= 60 минут
|Author= Yorik
|FCVersion=
|Files=
}}

Это кросс-пост [учебника](http://opensourceecology.org/wiki/FreeCAD_Architecture_Tutorial), изначально написанного для [Open-Source Ecology](http://opensourceecology.org).

## Представление FreeCAD 

<img alt="" src=images/Arch_panel_tutorial_01.jpg  style="width:800px;">

FreeCAD это программа параметрического трёхмерного моделирования. Параметрическое моделирование позволяет легко модифицировать Ваш проект изменением параметров назад по истории создания модели. FreeCAD это программа с открытыми исходными кодами (лицензия LGPL) и весьма модульная, позволяющая очень продвинутые расширения и настройки, особенно благодаря интенсивному использованию языка Python.

-   Веб-сайт FreeCAD: <http://www.freecadweb.org/>
-   Wiki-документация FreeCAD: <http://www.freecadweb.org/wiki/index.php?title=Main_Page/ru>
-   Верстаки FreeCAD: <http://www.freecadweb.org/wiki/index.php?title=Workbench_Concept/ru>
-   Форум FreeCAD: <http://forum.freecadweb.org/>
-   Приступая к работе с FreeCAD: <http://www.freecadweb.org/wiki/index.php?title=Getting_started/ru>
-   Архитектурный учебник FreeCAD: <http://www.freecadweb.org/wiki/index.php?title=Arch_tutorial/ru>

## Установка FreeCAD 

Вы можете выбрать установку последней стабильной версии (на сегодня, май 2015, это версия 0.15), или разрабатываемая версия (сейчас 0.16). Фактически, версия FreeCAD для разработчиков достаточно стабильна, и Вам рекомендуется попробовать проектируемую версию, если у Вас нет специфических причин не делать это. Поскольку разработка FreeCAD довольно быстрая, обязательно время от времени проверяйте последние версии и обновляйте программу, чтобы получить последние улучшения.

-   Для Windows: загрузите последнюю версию для Вашей версии Wibdiws (32 или 64 битной) с <https://github.com/FreeCAD/FreeCAD/releases>. Установите двойным кликом по файлу.
-   Для Mac OS: загрузите последнюю версию с <https://github.com/FreeCAD/FreeCAD/releases>. Установите двойным кликом по файлу.
-   Для Ubuntu: предлагаемая Ubuntu версия FreeCAD обычно устаревшая, так что советуем Вам взамен использовать PPA, поддерживаемый сообществом FreeCAD. Для установки, откройте приложение "Software Sources", и добавьте в число источников программ либо ppa:freecad-maintainers/freecad-stable для стабильной версии, или ppa:freecad-maintainers/freecad-daily для версии разработчика.
-   На других платформах: На большинстве поддерживаемых основных дистрибутивах Linux (Debian, Fedora, и т.д.) FreeCAD влючён в официальный репозиторий. Это вовсе не обязательно последняя версия. Если последняя версия, которая Вам нужна, не доступна, Выходом может быть самостоятельная компиляция FreeCAD (см. инструкции на сайте FreeCAD)

## Дополнительное опциональное содержимое 

-   Разрешение импорта,экспорта IFC: чтобы импортировать и экспортировать проект из/в файла формата IFC, FreeCAD использует IfcOpenShell importer, который Вы должны установить отдельно из <http://ifcopenshell.org/python.html>. Обязательно выберите версию на базе python2.7, поскольку именно эту версию использует FreeCAD.
-   Верстак образменивания Drawing dimensioning: дополнительный верстак для FreeCAD, который предлагает много удобных инструментов для добавления измерений и аннотация для двумерных чертежных листов FreeCAD: <https://github.com/hamish2014/FreeCAD_drawing_dimensioning> (инструкция установки находится на веб-странице)
-   Верстак Assembly2: дополнительный верстак для FreeCAD, который предлагает серию базовых инструментов для сборок: <https://github.com/hamish2014/FreeCAD_assembly2> (инструкция установки находится на веб-странице)

## Советы по быстрой установке 

Коллекция учебников, доступных на вики-страницах FreeCADа пока не густая. Однако многие члены сообщества FreeCAD используют youtube для размещения видеоуроков. Обязательно поищите контент по теме FreeCAD на youtube, это, вероятно, лучший источник для изучения.

FreeCAD это очень технически ориентированное приложение, и его кривая обучения может быть очень крутой. Полагайтесь на учебники, вики-документацию и не бойтесь спрашивать на форумах, если встретите специффическую проблему. Чётко сформулированные вопросы обычно получают очень быстрые и обширные ответы.

### Приблизительный список вещей, которые Вы должны знать 

-   Интерфейс FreeCAD разделён на верстаки. Верстаки это набор инструментов (кнопки на панелях и меню), которые сгруппированы для определённых задач. При переключении на другой верстак, интерфейс показывает Вам инструменты из этого верстака, но содержимое вашего трёхмерного документа не меняется. Вы продолжаете работать над тем же документом и теми же объектами.

-   FreeCAD всё еще в стадии разработке, имеет много ошибок, и приложение может периодически вылетать. Часто сохраняйтесь, и включите автосохранение в Правка → Параметры → Документ

-   Большинство объектов в FreeCAD параметрические. Это значит, что геометрия создаётся автоматически из набора параметров. Эти параметры всегда редактируемы в Properties View. Они делятся на параметры, относящиеся к геометрии (вкладка Data) и относящиеся к отображению объекта (вкладка View). Однако объекты, созданные в других приложениях и импортированные в FreeCAD обычно не определяются параметрами и потому не редактируются.

-   Several workbenches (PartDesign and Arch) are made to work only with solid objects, and will refuse to work on objects that are not solid. A good rule of thumb is always try to work with solid objects.

-   Although FreeCAD can import and work with mesh objects (Mesh workbench), it is primarily designed to work with a more advanced object type called brep, that is used by most of its workbenches (Part, PartDesign, Draft, Sketcher, Arch). When importing mesh-based files (.dae, .orb, .stl\...) you will usually need to convert these objects to brep before being able to do something interesting with them. Solid-based file formats however (.step, .iges), when imported into FreeCAD, directly produce brep objects. 2D formats (.dxf, .svg) also produce brep contents.

-   FreeCAD has different ways, or modes, to use the mouse buttons. These modes can be set in the preferences or changes on-the-fly by right-clicking on the 3D view background. They are described on <http://www.freecadweb.org/wiki/index.php?title=Mouse_Model>. The best suited modes for CAD work are CAD or Gestures.

## Упражнение: моделирование крышевой панели 

To showcase a typical workflow in FreeCAD, let\'s model a roof panel as described on <http://opensourceecology.org/wiki/MicroHouse_4_Roof_-_Module_-_Build_Instructions>. To do that,we will start from drawing the different pieces in a 2D constrained sketch, then we will take advantage of the special Arch Window object, which is able to build complex 3D objects from a 2D sketch containing the contours of several pieces. Finally, since what we need is not a window but a roof panel, we will simply convert our window object to another Arch type.

### 1. Open FreeCAD, then set your preferred units to "imperial" 

In menu Edit → Preferences → General → Units

### 2. Switch to the sketcher workbench and create a new sketch in the XY plane. 

![](images/Arch_panel_tutorial_02.jpg )

Usually, unless there is a specific reason not to do so,you\'ll always want to start drawing your 2D sketches on the ground plane, around the (0,0) origin point. Then, it is the 3D object generated from that, that will be moved/rotated into position.

### 3. Draw two rectangles. On each of them, place a vertical constraint of 16 ft and an horizontal constraint of 2 in. 

![](images/Arch_panel_tutorial_03.jpg )

Don\'t worry about the dimensions your pieces have when you draw them, the constraints will resize them accordingly. To add a dimension constraint (vertical or horizontal), you can either select a line, or two points (with CTRL pressed).

### 4. Once your two rectangles have the correct size, place a vertical constraint of 0 in between their corner points, and a horizontal constraint of 4 ft. 

![](images/Arch_panel_tutorial_04.jpg )

This ensures that our two rectangles are correctly positioned in relation to each other.

### 5. Add the two additional 2 in x 6 in pieces 

![](images/Arch_panel_tutorial_05.jpg )

Add two more rectangles and repeat the process. Note that in the example above, we didn\'t specify the length of these pieces, but rather placed a distance constraint between their extremities and the long vertical pieces, and we let a small gap of 0.05 inches between them. This is because if we make the rectangles touch each other, FreeCAD might deduce the loops wrongly, and we might get strange results with the Arch window tool. This little trick ensures that each rectangle will be recognized as an independent loop by the Arch window tool.

### 6. Add the corner reinforcement pieces 

![](images/Arch_panel_tutorial_06.jpg )

Same thing. Make them 6 inches wide, and separated them from other rectangles by 0.05 inches.

### 7. Draw 7 intermediary reinforcement pieces, set their width to 2 inches, and constrain their left and right endpoints at 0.05 inches of the vertical rectangles (or at 0 inch of the endpoints of the other horizontal rectangles) 

![](images/Arch_panel_tutorial_07.jpg )

Depending on your system, FreeCAD might begin to be slow to process new constraints. This is the disadvantage of using constrained objects, they quickly swallow up a lot of system resources. You must always consider if you absolutely need them. You can also delete constraints when they have done their job. These dimensions won\'t be fixed anymore, but unless you move the pieces around, they won\'t change. If needed, you can also always re-add constraints later.

### 8. Calculate the spacing between the 7 reinforcement pieces and set vertical constraints between them. 

In our case, our total length is 192 inches, minus the two end pieces (2 x 2 inches) and the two corner reinforcements (2 x 6 inches), = 192 -- (4 + 12) = 176. Removing the 7 reinforcement pieces ( 7 x 2 ) = 162. Dividing this by 8 gives us the space between each reinforcement: 20.25.

![](images/Arch_panel_tutorial_08.jpg )

### 9. Obtaining a fully constrained sketcher 

On the right panel (Tasks tab in the Combo View -\> Solver messages), you can see the message "\... 2 degrees of freedom". This means that our sketch is not fully constrained (it still has two "ways" of being deformed). This is because, although no piece of it can now move in relation to the others, the whole sketch can still move vertically and horizontally. To prevent this, we can simply take one of its corner points, select the origin point of the grid (where the green and red axes intersect) and press the Point Constraint button. This turns our sketch green, meaning it is fully constrained, no part of it can move anymore.

![](images/Arch_panel_tutorial_09.jpg )

This is actually not absolutely necessary. But it is always better to keep track of the exact position of objects (we are now certain that our corner is at the (0,0) point). In case something goes wrong later, or we need to figure out the position of an object built upon this sketch, this will be useful.

We can now press the "close" button and our base sketch is built:

![](images/Arch_panel_tutorial_10.jpg )

### 10. Switch to the Arch workbench and, with the sketch selected, press the "window" button 

Our sketch has now vanished and one of its rectangles has been extruded slightly into a solid piece:

![](images/Arch_panel_tutorial_11.jpg )

Although this seems wrong, it is simply because the Arch Window tool has created a default piece from the biggest loop it could find in the base sketch. We will fix that soon. Also, notice take note that the sketch has not disappeared, it has simply been turned off and "swallowed" by its new parent object. You can still find it in the tree view, by expanding the window object, and turn its display on/off by pressing the SPACE key.

### 11. Edit the window components by double-clicking it in the tree view 

![](images/Arch_panel_tutorial_12.jpg )

When double-clicking the window, its base sketch becomes visible again, and we get its edit interface: At the left, a list of the loops found in the base sketch, at the right the solid pieces built on it.

Begin with removing the "Default" piece.

Then, select the first loop (Wire0). It will highlight in the 3D view. Press the "Add" button to create a new piece from it. Give it a name, make sure the correct wire is set, and give it a 6 inches extrusion. The offset should stay 0 since we want it placed "on the ground".

The "Type" value will be used to attribute materials to the window (not implemented yet), so you can currently leave to "Frame".

![](images/Arch_panel_tutorial_13.jpg )

Then press the "Create component" button. Sometimes FreeCAD fails to guess correctly the direction of the extrusion, and you must therefore edit your component and change the 6 inches value by -6 inches.

Repeat this for all the needed pieces:

![](images/Arch_panel_tutorial_14.jpg )

When closing the edit panel we obtain the object above. Note that by default, window objects are represented semi-transparent. Since this will actually not be a window, we can just turn that off by setting its Transparency value to 0 in its View properties.

### 12. Add the cover panel 

We now have our panel frame, but not the base panel itself. To do that, the best way is to open our base sketch, and add a new rectangle. Remember though to not make any of the corners of that rectangle coincident to corners of other rectangles, in order not to confuse our window object, which might require us to redo the whole series of components if the order of the loops would change.

We can therefore constrain this new rectangle 0.05 inches inside the perimeter. This will require us to place 4 new constraints.

We can then edit our window again, and add new components. We can see that a new Wire has been found. This time, we will use it to add a 8mm polycarbonate panel (note that you can mix units without problems in FreeCAD, and write "8mm" as the thickness, even if you are working in inches). We will also give it an offset of 0.05 inches, so it is slightly offsetted from the frame, just for consistency, as all the parts of our object have that offest between them.

![](images/Arch_panel_tutorial_15.jpg )

We can now create another component based on the same Wire, in order to place another panel on top of our frame. This time, we will give it an offset of 6.05 inches. Our panel is finally complete:

![](images/Arch_panel_tutorial_16.jpg )

### 13. Turn the window into another type of Arch component 

This is not really necessary at the moment, but it might become important later when we export or work to other construction-oriented applications, for example via IFC, we don\'t want our panel to be identified as a window.

The Arch workbench of FreeCAD provides an easy way to handle that, which is that any object type can always become another, by being the base of another type. In this case, let\'s turn our window into a Panel object, simply by selecting the window and pressing the Panel tool.

![](images/Arch_panel_tutorial_17.jpg )

Notice that the color of the resulting panel has changed, that is because materials support in FreeCAD and the Arch module is still incomplete. When it is finished, this will be properly handled.

### 14. Duplicating the panel 

Our panel can then be duplicated and copied over in several ways, for example by using copy/paste. But a more interesting way is to use the Draft Clone tool (also present on the Arch workbench, like all other Draft tools). The Clone tool keeps the relationship between the base object and its clone, so any modification to the base object will reflect in all its clones.

![](images/Arch_panel_tutorial_18.jpg )

In the current development version of FreeCAD, clones of Arch objects are now Arch objects themselves too.

### 15. Rotating and positioning the panels. 

While the assembly workbench of FreeCAD is not ready yet, we need to position our pieces manually, either by manipulating their Placement property, or by using the Draft Move and Rotate tools, which are actually only visual ways to modify the Placement of objects.

Both Draft Rotate and Move tools make use of the Draft Snapping system. Different snapping positions (endpoints, midpoints, etc) are available, that can be switched on/off, allowing to perform very precise positionning and rotations.

![](images/Arch_panel_tutorial_19.jpg )

![](images/Arch_panel_tutorial_20.jpg )


{{Tutorials navi

}}   {{Sketcher Tools navi}} 
