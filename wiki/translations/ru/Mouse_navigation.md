# Mouse navigation/ru
{{TOCright}}

## Обзор


<div class="mw-translate-fuzzy">

Каждый стиль **управления мышью** определяет собой методы для навигации в трёхмерном пространстве, а так же методы взаимодействия с трехмерными объектами (перемещение, вращение и т.п.). FreeCAD поддерживает несколько стилей навигации с помощью мыши. По умолчанию установлен стиль навигации \"CAD Navigation\", он очень простой и практичный, но FreeCAD так же предлагает альтернативные стили навигации, которые Вы можете выбрать по своим предпочтениям.


</div>

For more information about selecting objects see [Selection methods](Selection_methods.md).

For more information about manipulating objects see [Std TransformManip](Std_TransformManip.md).


<div class="mw-translate-fuzzy">

## Навигация


</div>


<div class="mw-translate-fuzzy">

-   В [Настройках](Preferences_Editor/ru#Navigation.md), **Правка → Настройки → Отображение → Трёхмерный вид → Трёхмерная навигация**.
-   Правым кликом на пустом месте области пространственного вида и выбором **Стили навигации** контекстного меню.


</div>

## Available navigation styles 

### Навигация Blender 

The Blender navigation style was modeled after [Blender](https   *//www.blender.org).


<div class="mw-translate-fuzzy">

Стиль навигации Blender ориентируется на [Blender](https   *//www.blender.org). Ранее не было возможности сдвига только мышью, и требовалось нажимать кнопку **SHIFT** для сдвига вида. Это было изменено в 2016 году при добавке возможностей, теперь для сдвига можно нажать левую и правую кнопку мыши. {{Blender Navigation
|Select_name=Выбор
|Pan_name=Сдвиг
|Zoom_name=Масштаб
|Rotate_view_name=Вращать
|Shift=**Shift**
|Select_text=Нажмите левую кнопку мыши над выделяемым объектом.
|Pan_text=Удерживайте **Shift** и среднюю кнопку мыши и двигайте объект.
</div>

Либо удерживайте левую и правую кнопки и перемещайтесь.
|Zoom_text=Используйте колёсико мыши для приближения и отдаления.
|Rotate_view_text=Нажмите и тяните средней кнопкой мыши.
}}

### Навигация CAD 

Это стиль навигации по умолчанию и позволяет пользователю простейшее управление видом, не требуя использования клавиатуры, кроме как для множественного выделения.


{{CAD Navigation
|Select_name=Выбор
|Pan_name=Перемещение<br>в пространстве
|Zoom_name=Приблежение<br>отдаление
|Rotate_view_name=Вращение<br>обычное
|Rotate_view_alt_name=Вращение<br>альтернативным методом
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Нажмите левую кнопку мыши над объектом, который вы хотите выбрать.

<div class="mw-translate-fuzzy">
Нажатием **Ctrl** можно выбрать несколько объектов.
|Pan_text=Удерживая среднюю кнопку мыши, двигаем указатель.
|Pan_mode_text=Режим сдвига   * удерживая кнопку **Ctrl**, один раз нажимаем правую кнопку мыши, затем двигаем указатель. <small>(v0.17)</small> 
|Zoom_text=Используем колёсико мыши для приближения и отдаления.
</div>

<div class="mw-translate-fuzzy">
Кликом средней кнопкой вид центрируется по положению курсора.
|Zoom_mode_text=Режим приближения   * удерживая кнопки **Ctrl** и **Shift**, нажмите правую кнопку, и двигайте указатель. <small>(v0.17)</small> 
|Rotate_view_text=Удерживая среднюю кнопку мыши, нажмите и удерживайте левую кнопку мыши, затем двигайте указатель.
</div>

<div class="mw-translate-fuzzy">
Положение курсора во время нажатия средней кнопки мыши определяет центр вращения. Вращение работает как кручение шара вокруг своего центра. Если кнопки отпущены до остановки кнопки мыши, если так настроено, вид продолжает [крутиться](Spinning/ru.md).
</div>

<div class="mw-translate-fuzzy">
Двойной клик средней кнопкой мыши устанавливает новый центр вращения.
|Rotate_view_mode_text=Режим вращения   * удерживая кнопку **Shift**, нажмите правую кнопку, затем двигайте указатель. <small>(v0.17)</small> 
|Rotate_view_alt_text=Удерживая среднюю кнопку мыши, нажмите и удерживайте правую кнопку мыши, затем двигайте указатель.
</div>

При этом методе средняя кнопка мыши может быть отпущена после того как правая кнопка осталась нажатой.

Пользователи, использующие мышь правой рукой могут счесть этот метод проще исходного.
}}

### Навигация Gesture 

This style was tailored for use with a touchscreen and pen. Nevertheless, it can also be used with a mouse, and is recommended for use when using a Mac with a trackpad.


<div class="mw-translate-fuzzy">

Этот стиль навигации был предложен в версии 0.16, и скроен для использования с точскрином и пером, однако пригоден и для использования с мышью. {{Gesture Navigation
|Select_name=Выбор
|Pan_name=Сдвиг
|Zoom_name=Масштаб
|Rotate_view_name=Вращение
|Tilt_view_name=Tilt view
|Select_text=Нажмите левую кнопку мыши над объектом, который хотите выделить.
|Select_gesture_text=Щелкните для выбора.
|Pan_text=Удерживайте правую кнопку мыши и тяните курсор для сдвига вида.
|Pan_gesture_text=Тяните двумя пальцами.
</div>

Иначе, удерживайте щёлкните и удержите, потом тяните. Это симулирует сдвиг правой кнопкой мыши.
|Zoom_text=Используйте колёсико мыши для масштабирования.
|Zoom_gesture_text=Сдвиньте пальцы для масштабирования (т.е. потяните два пальца к/от друг друга).
|Rotate_view_text=Удерживайте левую кнопку мыши и тяните указатель.
В режиме [Sketcher](Sketcher_Workbench/ru.md) и некоторых других это действие заблокировано. Удерживайте **Alt** при нажатии кнопки мыши для перехода в режим вращения.

Чтобы установить точку фокуса камеры для вращения, кликните новую точку средней кнопкой мыши. Взамен, нацельте курсор в новую точку и нажмите кнопку **H** на клавиатуре.
|Rotate_view_gesture_text=Потяните одним пальцем для вращения.

Удерживайте вдобавок **Alt** в режиме [Sketcher](Sketcher_Workbench/ru.md).
|Tilt_view_text=Удерживайте левую и правую кнопку мыши и тяните указатель в сторону.
|Tilt_view_gesture_text=Вращайте воображаемую линию между двумя точками касания.

В версии v0.18 этот метод по умолчанию отключён. Для разрешения **Правка → Параметры → Отображение**, и снимите метку "Disable touchscreen tilt gesture".
}}

### Навигация MayaGesture 

In Maya-Gesture Navigation, panning, zooming, and rotating the view require the **Alt** key together with a mouse button; therefore, a three-button mouse is required. It\'s also possible to use gestures as this style was developed over the [Gesture navigation](#Gesture_navigation.md) style.


<div class="mw-translate-fuzzy">

При навигации типа MayaGesture, перемещения видов требуют нажатия **ALT** с кнопкой мыши, поэтому для него требуется трехкнопочная мышь. Взамен можно использовать жесты из режима [Gesture](Mouse_Model#Gesture_Navigation/ru.md). {{MayaGesture Navigation
|Select_name=Выбор
|Pan_name=Сдвиг
|Zoom_name=Масштаб
|Rotate_view_name=Вращать
|Alt=**Alt**
|Select_text=Нажмите левую кнопку мыши над выделяемым объектом.
|Pan_text=Удерживая **Alt** и среднюю кнопку мыши, двигайте указатель.
|Zoom_text=Удерживая **Alt** и правую кнопку мыши, двигайте указатель.
</div>

Иначе, используйте для приближения и отдаления колёсико мыши.
|Rotate_view_text=Удерживая **Alt** и левую кнопку мыши, двигайте указатель.
}}

#### Навигация OpenCascade 

The OpenCascade navigation style was modeled after [OpenCascade](https   *//www.opencascade.com/).


{{OpenCascade Navigation
|Select_name=Выбор
|Pan_name=Сдвиг
|Zoom_name=Масштаб
|Rotate_view_name=Вращать
|Ctrl=**Ctrl**
|Select_text=Нажать левую кнопку мыши над выделяемым объектом.
|Pan_text=Удерживайте среднюю кнопку мыши и двигайте указатель.
|Zoom_text=Используйте колёсико мыши для приближения и отдаления.

Иначе, удерживая **Ctrl** и левую кнопку мыши, двигайте указатель.
|Rotate_view_text=Удерживая **Ctrl** и правую кнопку мыши, двигайте указатель.
}}

### Навигация OpenInventor 


<div class="mw-translate-fuzzy">

При навигации в стиле [OpenInventor](http   *//en.wikipedia.org/wiki/Open_Inventor). Для выделения объектов надо нажать кнопку **CTRL**.


</div>


<div class="mw-translate-fuzzy">

Этот метод базируется на на Autodesk Inventor.


</div>


<div class="mw-translate-fuzzy">


{{OpenInventor Navigation
|Select_name=Выбор
|Pan_name=Сдвиг
|Zoom_name=Масштаб
|Rotate_view_name=Вращать
|Ctrl=**Ctrl**
|Select_text=Удерживая **Ctrl**, нажимаем левую кнопку мыши над объектом, который хотим выделить.
|Pan_text=Удерживая среднюю кнопку мыши, двигаем указатель.
|Zoom_text=Используем колёсико мыши для приближения и отдаления.
</div>

Hold down **Ctrl** instead to select multiple objects.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.

Иначе, удерживая среднюю кнопку мыши, нажимаем и удерживаем её левую кнопку, затем двигаем указатель. 
|Rotate_view_text=Удерживая левую кнопку мыши, двигаем указатель.
}}

### OpenSCAD navigation 

The OpenSCAD navigation style was modeled after [OpenSCAD](https   *//openscad.org/).


<small>(v0.20)</small> 


{{OpenSCAD_Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold the right mouse button, then move the pointer.
|Zoom_text=Hold the middle mouse button, then move the pointer.
Alternatively, hold **Shift** and the right mouse button, then move the pointer.
|Rotate_view_text=Hold the left mouse button, then move the pointer.
}}

### Навигация Revit 

The Revit navigation style was modeled after [Revit](https   *//en.wikipedia.org/wiki/Autodesk_Revit).


{{Revit Navigation
|Select_name=Выбор
|Pan_name=Сдвиг
|Zoom_name=Масштаб
|Rotate_view_name=Вращать
|Shift=**Shift**
|Select_text=Нажать левую кнопку мыши над выделяемым объектом.
|Pan_text=Удерживайте среднюю кнопку мыши и двигайте указатель.

Иначе, удерживая левую и правую кнопку мыши, двигайте указатель.

|Zoom_text=Используйте для приближения и отдаления колёсико мыши.
|Rotate_view_text=Удерживая **Shift** и среднюю кнопку мыши, двигайте указатель.

Иначе, удерживая среднюю кнопку мыши, нажмите и удерживайте правую кнопку, затем двигайте указатель.
}}

### TinkerCAD navigation 

The TinkerCAD navigation style was modeled after [TinkerCAD](https   *//en.wikipedia.org/wiki/Tinkercad).


<small>(v0.20)</small> 


{{TinkerCAD Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.
|Rotate_view_text=Press the right mouse button, then move the pointer.
}}

### Навигация Touchpad 

In Touchpad Navigation, panning, zooming, and rotating the view require a modifier key together with the touchpad.


<div class="mw-translate-fuzzy">

При включении навигации тачпадом, сдвиг, масштабирование и вращение вида требует вместе с тачпадом использования модифицирующих клавиш. {{Touchpad Navigation
|Select_name=Выбор
|Pan_name=Сдвиг
|Zoom_name=Масштаб
|Rotate_view_name=Вращение
|Shift=**Shift**
|Ctrl=**Ctrl**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=Нажмите левую кнопку над объектом, который хотите выбрать.
|Pan_text=Удерживайте **Shift** и двигайте объект.
|Zoom_text=Используйте **PageUp** и **PageDown** для приближения или отдаления.
|Zoom_alt_text=Иначе, удерживайте вместе **Shift** и **Ctrl**, нажмите левую кнопку мыши, и двигайте указатель.
|Rotate_view_text=Удерживайте **Alt** и двигайте указатель.
|Rotate_view_alt_text=Иначе, удерживайте клавиши **Shift** стрелку влево, затем двигайте указатель.
}}


</div>

## Поддержка оборудования 


<div class="mw-translate-fuzzy">

FreeCAD так же поддерживает несколько [3d мышей](3D_input_devices/ru.md).


</div>


<div class="mw-translate-fuzzy">

## Проблемы Mac OS X 


</div>


<div class="mw-translate-fuzzy">

В настоящее время имеется сообщение [на форуме](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0) от пользователей Mac, что кнопка мыши и сочетание клавиш работают не так, как ожидается. К сожалению, ни один из наших разработчиков не использует Mac. Нам требуется помощь, чтобы определить, какие сочетания кнопок мыши и комбинации клавиш работают, чтобы мы смогли обновить текст на wiki.


</div>

## Developing a custom navigation 

The tutorial [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) orients developers who want to develop a custom mouse navigation option. Familiarity with the C++ syntax is required.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Mouse navigation/ru
