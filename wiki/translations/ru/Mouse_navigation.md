# Mouse navigation/ru
## Обзор

Каждый **стиль навигации** определяет собой методы для навигации в трёхмерном пространстве, а так же методы взаимодействия с трехмерными объектами (перемещение, вращение и т.п.). FreeCAD поддерживает несколько стилей навигации и управления. По умолчанию установлен [CAD стиль навигации](#Навигация_CAD.md), он очень простой и практичный, но FreeCAD так же предлагает альтернативные стили навигации, которые вы можете выбрать по своим предпочтениям. Назначенный пользователем стиль навигации будет использоваться для всех верстаков.

Дополнительные сведения о способах выбора объектов см. в разделе [Методы выбора объектов](Selection_methods/ru.md).

Дополнительные сведения о способах преобразования объектов см. на странице описания команды [Преобразование](Std_TransformManip/ru.md).



## Выбор стиля навигации 

1.  Выполните одно из следующих действий:
    -   Нажмите на кнопку **[<img src=images/NavigationCAD_dark.svg style="width:16px">** в [Строке состояния](Status_bar/ru.md).
    -   Щелкните правой кнопкой мыши в пустую область в [3D Виде](3D_view/ru.md), и выберите **Стили навигации** в контекстном меню.
    -   Откройте [Редактор настроек](Preferences_Editor/ru#Navigation.md) через пункт главного меню **Редактировать → Настройки...** В нем выберите раздел **Отображение →** вкладку **Навигация →** пункт **Трехмерная навигация**.
2.  Выберите стиль из списка.
3.  При необходимости укажите стиль **Ващения**: нажмите на кнопку **[<img src=images/NavigationCAD_dark.svg style="width:16px">** в [Строке состояния](Status_bar/ru.md) и выберите в контекстом меню пункт **Настройки → Вращение**. Подробности см. в описании [Редактора настроек](Preferences_Editor/ru#Navigation.md).
4.  При необходимости укажите **Режим вращения**. Подробности см. в описании [Редактора настроек](Preferences_Editor#Navigation.md).
5.  Если выбран стиль навигации **CAD**: при необходимости укажите параметр настроек **Включить анимацию**. Подробности см. в описании [Редактора настроек](Preferences_Editor#Navigation.md).



## Доступные стили навигации 

With all navigation styles, unless selecting objects from a sketch in edit mode, you must hold **Ctrl** to select multiple objects.

The following keyboard options are available for all styles:

-    **Ctrl**\+ {{ASCII|43}} and **Ctrl** + {{ASCII|22}} or **PgUp** and **PgDn** to zoom in and out, respectively.

-   The arrow keys, {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, to pan the view left/right and up/down.

-    **Shift**\+ {{ASCII|17}} and **Shift** + {{ASCII|16}} to rotate the view by 90 degrees.



### Навигация Blender 

Стиль навигации Blender основан на модели управления используемой в редакторе [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">


{{Blender Navigation
|Select_name=Выбор
|Pan_name=Перемещение
|Zoom_name=Масштабирование
|Rotate_view_name=Вращение
|Shift=**Shift**
|Select_text=Нажмите левую кнопку мыши над объектом, который хотите выбрать. 
|Pan_text=Удерживайте **Shift** и среднюю кнопку мыши для перемещения объекта.
</div>

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Hold the middle mouse button, then move the pointer.

|Pan_text=Hold **Shift** and the middle mouse button, then move the pointer.

Alternatively, hold both left and right mouse buttons, and then move the pointer.
}}



### Навигация CAD 

Это стиль навигации по умолчанию и позволяет пользователю простейшее управление видом, не требуя использования клавиатуры, кроме как для множественного выделения.


<div class="mw-translate-fuzzy">


{{CAD Navigation
|Select_name=Выбор
|Pan_name=Перемещение
|Zoom_name=Масштабирование
|Rotate_view_name=Вращение<br>обычное
|Rotate_view_alt_name=Вращение<br>альтернативным методом
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Нажмите левую кнопку мыши над объектом, который вы хотите выбрать.
</div>

|Ctrl=**Ctrl**
|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor.

|Rotate_view_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

Если кнопки будут отпущены до того, как вы остановите движение мыши, Вид продолжит вращение, в случае если включен [поворотный просмотр объекта](Spinning/ru.md).

<div class="mw-translate-fuzzy">
Двойное нажатие средней кнопкой мыши устанавливает новый центр вращения.
|Rotate_view_mode_text=Режим вращения: удерживая клавишу **Shift**, нажмите правую кнопку мыши, затем перемещайте указатель.
|Rotate_view_alt_text=Удерживая среднюю кнопку мыши, нажмите и удерживайте правую кнопку мыши, затем перемещайте указатель.
</div>

|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

При этом методе средняя кнопка мыши может быть отпущена после того как правая кнопка осталась нажатой.

<div class="mw-translate-fuzzy">
Пользователи, использующие мышь правой рукой могут счесть этот метод проще исходного.
}}


</div>

\|Pan_text=Hold the middle mouse button, then move the pointer.

\|Zoom_mode_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer.

\|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer.

\|Pan_mode_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer. }}



### Навигация Gesture (Жестами) 

Этот стиль был разработан специально для работы с сенсорным экраном с помощью стилуса или жестами. Тем не менее он также может применяться при управлении мышью, кроме того данный стиль управления рекомендуется использовать при управлении трекпадом в Mac.


<div class="mw-translate-fuzzy">


{{Gesture Navigation
|Select_name=Выбор
|Pan_name=Перемещение
|Zoom_name=Масштабирование
|Rotate_view_name=Вращение
|Tilt_view_name=Наклонить вид
|Select_text=Нажмите левую кнопку мыши над объектом, который хотите выбрать.
|Select_gesture_text=Коснитесь пальцем экрана для выбора.
|Pan_text=Удерживайте правую кнопку мыши и перемещайте указатель.
|Pan_gesture_text=Коснитесь экрана двумя пальцами и перемещайте их в нужном направлении.
</div>

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Hold the left mouse button, then move the pointer.
In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

<div class="mw-translate-fuzzy">
Чтобы установить точку фокуса камеры для вращения, кликните новую точку средней кнопкой мыши. Взамен, нацельте указатель в новую точку и нажмите кнопку **H** на клавиатуре.
|Rotate_view_gesture_text=Потяните одним пальцем для вращения.
</div>

|Pan_text=Hold the right mouse button, then move the pointer.

|Tilt_view_text=Hold both left and right mouse buttons, then move the pointer sideways.

|Select_gesture_text=Tap to select.

|Zoom_gesture_text=Drag two fingers (pinch) closer or farther apart.

|Rotate_view_gesture_text=Drag with one finger to rotate.

<div class="mw-translate-fuzzy">
Удерживайте вдобавок **Alt** в режиме [Sketcher](Sketcher_Workbench/ru.md).
|Tilt_view_text=Удерживайте левую и правую кнопку мыши и тяните указатель в сторону.
|Tilt_view_gesture_text=Вращайте воображаемую линию между двумя точками касания.
</div>

|Pan_gesture_text=Drag with two fingers.

<div class="mw-translate-fuzzy">
Или, коснитесь экрана одним пальцем, удерживайте его некоторое время, а потом перемещайте в нужном направлении. Это равносильно перемещению с помощью правой кнопки мыши.
|Zoom_text=Используйте колёсико мыши для масштабирования.
|Zoom_gesture_text=Сдвиньте пальцы для масштабирования (т.е. потяните два пальца к/от друг друга).
|Rotate_view_text=Удерживайте левую кнопку мыши и тяните указатель.
В режиме [Sketcher](Sketcher_Workbench/ru.md) и некоторых других это действие заблокировано. Удерживайте **Alt** при нажатии кнопки мыши для перехода в режим вращения.
</div>

|Tilt_view_gesture_text=Rotate the imaginary line formed by two touch points.

<div class="mw-translate-fuzzy">
Начиная с версии v0.18 этот метод по умолчанию отключён. Для разрешения **Правка → Настройки → Отображение**, и снимите метку "Отключить жест наклона для сенсорного экрана".
}}


</div>



### Навигация Maya-Gesture (Жестами в стиле Maya) 

В стиле навигации MayaGesture, перемещение, масштабирование и вращение Вида выполняется при зажатой клавише **ALT** и нажатии одной из трех кнопок мыши, поэтому этот стиль навигации полноценно можно использовать только с трехкнопочной мышью. В данном стиле также можно использовать жесты из [обычного стиля навигации жестами](Mouse_Model#Gesture_Navigation/ru.md), так как этот стиль был разработан на его основе.


<div class="mw-translate-fuzzy">


{{MayaGesture Navigation
|Select_name=Выбор
|Pan_name=Перемещение
|Zoom_name=Масштабирование
|Rotate_view_name=Вращение
|Alt=**Alt**
|Select_text=Нажмите левую кнопку мыши над объектом который вы хотите выбрать.
|Pan_text=Удерживая клавишу **Alt** и среднюю кнопку мыши, перемещайте указатель.
|Zoom_text=Удерживая клавишу **Alt** и правую кнопку мыши, перемещайте указатель.
</div>

|Alt=**Alt**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold **Alt** and the right mouse button, then move the pointer.

|Rotate_view_text=Hold **Alt** and the left mouse button, then move the pointer.

|Pan_text=Hold **Alt** and the middle mouse button, then move the pointer.

|Tilt_view_text=Hold **Alt** and both left and right mouse buttons, and then move the pointer sideways.
}}



### Навигация OpenCascade 

Стиль навигации OpenCascade основан на модели управления используемой в [OpenCascade](https://www.opencascade.com/).


<div class="mw-translate-fuzzy">


{{OpenCascade Navigation
|Select_name=Выбор
|Pan_name=Перемещение
|Zoom_name=Масштабирование
|Rotate_view_name=Вращение
|Ctrl=**Ctrl**
|Select_text=Нажмите левую кнопку мыши над объектом, который хотите выбрать. 
|Pan_text=Удерживая среднюю кнопку мыши, перемещайте указатель.
|Zoom_text=Используйте колёсико мыши для приближения и отдаления.
</div>

|Ctrl=**Ctrl**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

<div class="mw-translate-fuzzy">
Или, удерживая **Ctrl** и левую кнопку мыши, перемещайте указатель.
|Rotate_view_text=Удерживая **Ctrl** и правую кнопку мыши, перемещайте указатель.
}}


</div>

\|Rotate_view_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

Alternatively, hold **Ctrl** and the right mouse button, then move the pointer.

\|Pan_text=Hold the middle mouse button, then move the pointer. It is possible to hold **Ctrl**. }}



### Навигация OpenInventor 

Стиль навигации OpenInventor основан на модели управления используемой в редакторе [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor). Для выбора объектов, необходимо удерживать нажатой клавишу **Shift** или **Ctrl**.

Данный стиль управления отличен от того, что применен в Autodesk Inventor.


<div class="mw-translate-fuzzy">


{{OpenInventor Navigation
|Select_name=Выбор
|Pan_name=Перемещение
|Zoom_name=Масштабирование
|Rotate_view_name=Вращение
|Shift=**Shift**
|Select_text=Удерживая **Shift**, нажмите левую кнопку мыши над объектом, который хотите выбрать.
</div>

|Shift=**Shift**

|Select_text=Hold **Shift**, then press the left mouse button over an object you want to select.

<div class="mw-translate-fuzzy">
Вместо этого удерживайте нажатой клавишу **Ctrl**, чтобы выбрать несколько объектов.
|Pan_text=Удерживая среднюю кнопку мыши, перемещайте указатель.
|Zoom_text=Используем колёсико мыши для приближения и отдаления.
</div>

|Zoom_text=Use the mouse wheel to zoom in and out.

<div class="mw-translate-fuzzy">
Или, зажмите и удерживайте среднюю и левую кнопку мыши, затем перемещайте указатель. 
|Rotate_view_text=Удерживая левую кнопку мыши, перемещайте указатель.
}}


</div>

\|Rotate_view_text=Hold the left mouse button, then move the pointer.

\|Pan_text=Hold the middle mouse button, then move the pointer. }}



### Навигация OpenSCAD 

Стиль навигации OpenSCAD основан на модели управления используемой в редакторе [OpenSCAD](https://openscad.org/).


<div class="mw-translate-fuzzy">


{{OpenSCAD_Navigation
|Select_name=Выбор
|Pan_name=Перемещение
|Zoom_name=Масштабирование
|Rotate_view_name=Вращение
|Shift=**Shift**
|Select_text=Нажмите левую кнопку мыши над объектом, который хотите выбрать. 
|Pan_text=Удерживайте правую кнопку мыши и перемещайте указатель. 
|Zoom_text=Удерживая среднюю кнопку мыши, перемещайте указатель. 
Или, удерживая **Shift** и правую кнопку мыши, перемещайте указатель. 
|Rotate_view_text=Удерживайте левую кнопку мыши и перемещайте указатель.
}}


</div>

\|Shift=**Shift**

\|Select_text=Press the left mouse button over an object you want to select.


{{VersionMinus|0.21}}

Hold **Ctrl** and **Shift** when pressing the mouse button to drag an object in a sketch in edit mode.

\|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold the middle mouse button, then move the pointer.

Or hold **Shift** and the right mouse button, then move the pointer.

\|Rotate_view_text=Hold the left mouse button, then move the pointer.

Alternatively, and when a sketch is in edit mode, hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

\|Pan_text=Hold the right mouse button, then move the pointer. }}



### Навигация Revit 

Стиль навигации Revit основан на модели управления используемой в редакторе [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit).


<div class="mw-translate-fuzzy">


{{Revit Navigation
|Select_name=Выбор
|Pan_name=Перемещение
|Zoom_name=Масштабирование
|Rotate_view_name=Вращение
|Shift=**Shift**
|Select_text=Нажмите левую кнопку мыши над объектом, который хотите выбрать. 
|Pan_text=Удерживая среднюю кнопку мыши, перемещайте указатель.
</div>

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

<div class="mw-translate-fuzzy">
|Zoom_text=Используйте для приближения и отдаления колёсико мыши.
|Rotate_view_text=Удерживая **Shift** и среднюю кнопку мыши, перемещайте указатель.
</div>

|Rotate_view_text=Hold **Shift** and the middle mouse button, then move the pointer.

<div class="mw-translate-fuzzy">
Или, удерживая среднюю кнопку мыши, нажмите и удерживайте правую кнопку, затем перемещайте указатель.
}}


</div>

\|Pan_text=Hold the middle mouse button, then move the pointer.


<div class="mw-translate-fuzzy">

Или, удерживая левую и правую кнопку мыши, перемещайте указатель.


</div>



### Навигация TinkerCAD 

Стиль навигации TinkerCAD основан на модели управления используемой в редакторе [TinkerCAD](https://en.wikipedia.org/wiki/Tinkercad).


<div class="mw-translate-fuzzy">


{{TinkerCAD Navigation
|Select_name=Выбор
|Pan_name=Перемещение
|Zoom_name=Масштабирование
|Rotate_view_name=Вращение
|Select_text=Нажмите левую кнопку мыши над объектом, который хотите выбрать. 
|Pan_text=Удерживая среднюю кнопку мыши, перемещайте указатель.
|Zoom_text=Используйте колёсико мыши для приближения и отдаления.
|Rotate_view_text=Удерживая правую кнопку мыши, перемещайте указатель. 
}}


</div>

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Use the mouse wheel to zoom in and out.

\|Rotate_view_text=Press the right mouse button, then move the pointer.

\|Pan_text=Hold the middle mouse button, then move the pointer. }}



### Навигация Touchpad 


<div class="mw-translate-fuzzy">

В режиме навигации тачпадом, перемещение, масштабирование и вращение Вида требует использования вместе с тачпадом модифицирующих клавиш.


</div>


<div class="mw-translate-fuzzy">


{{Touchpad Navigation
|Select_name=Выбор
|Pan_name=Перемещение
|Zoom_name=Масштабирование
|Rotate_view_name=Вращение
|Ctrl=**Ctrl**
|Shift=**Shift**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=Нажмите левую кнопку над объектом, который хотите выбрать.
|Pan_text=Удерживайте **Shift** и двигайте объект.
|Zoom_text=Используйте **PageUp** и **PageDown** для приближения или отдаления.
|Zoom_alt_text=Или, зажмите **Ctrl** + **Shift** и нажмите левую кнопку мыши, после чего перемещайте указатель.
|Rotate_view_text=Удерживайте клавишу **Alt** и перемещайте указатель.
|Rotate_view_alt_text=Или, удерживайте клавиши **Shift** стрелку влево, после чего перемещайте указатель.
}}


</div>

\|Ctrl=**Ctrl** \|Shift=**Shift** \|Alt=**Alt**

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Hold **Ctrl** and **Shift**, then move the pointer.

\|Rotate_view_text=Hold **Alt**, then move the pointer.

Alternatively, hold **Shift** and the left button, then move the pointer.

\|Pan_text=Hold **Shift**, then move the pointer. }}



## Поддержка оборудования 

В FreeCAD так же поддерживает некоторые [устройства 3D ввода](3D_input_devices/ru.md).



## Рекомендуемый стиль управления для MacOS 

На MacBook с трекпадом навигация жестами работает хорошо, но жесты имеют особое значение:

-   Масштабирование: касание и перемещение двумя пальцами.
-   Вращение: касание и перемещение тремя пальцами.
-   Перемещение: **Ctrl** + касание и перемещение тремя пальцами.



---
⏵ [documentation index](../README.md) > Mouse navigation/ru
