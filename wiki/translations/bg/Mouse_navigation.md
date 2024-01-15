# Mouse navigation/bg
## Overview


<div class="mw-translate-fuzzy">

Стилът на работа с мишката\" се състои от командите които се използват за навигация в 3D пространството и работа с обектите в него. FreeCAD подържа няколко стила на навигация с мишка. Стилът по-поразбиране се нарича \"CAD Навигация,\" и е доста прост и практичен. FreeCAD също предлага алтернативни стилове за навигация близки до интерфейсите на други програми.


</div>

For more information about selecting objects see [Selection methods](Selection_methods.md).

For more information about manipulating objects see [Std TransformManip](Std_TransformManip.md).

## Selecting a navigation style 


<div class="mw-translate-fuzzy">

-   В менюто [Preference Editor](Preferences_Editor/bg.md), скецията Display и в таба *3D View*;
-   Като натиснем десния бутон на мишката в празно място в 3D прозореца и изберем *Navigation style* от контекстното меню което се появява.


</div>

## Available navigation styles 

With all navigation styles, unless selecting objects from a sketch in edit mode, you must hold **Ctrl** to select multiple objects.




<div class="mw-translate-fuzzy">

### Стил навигация Blender 


</div>

The Blender navigation style was modeled after [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">

Този стил навигация е подобен на навигацията в програмата [Blender](http://www.blender.org). Не може да се движви обект в четерите посоки(pan) само с мишката. За да движите обект в четирите посоки трябва да задържите бутонът **SHIFT**. {{Blender Navigation/bg}}


</div>

Alternatively, hold both left and right mouse buttons, and then move the pointer. \|Zoom_text=Use the mouse wheel to zoom in and out. \|Rotate_view_text=Hold the middle mouse button, then move the pointer. }}

### CAD navigation 


<div class="mw-translate-fuzzy">

### Стил CAD Навигация (по-подразбиране) 

Това е стилът на навигация по-подразбиране който позволява лесен контрол на изгелда без да изисква използването на клавиатурата, с изключението на бутона **SHIFT** за избиране на няколко обекта едновременно. {{CAD Navigation/bg}}


</div>


{{CAD Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view<br>First method
|Rotate_view_alt_name=Rotate view<br>Alternate method
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Pan_mode_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor.
|Zoom_mode_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer.
|Rotate_view_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

If the buttons are released before you stop the mouse motion, the view continues spinning, if this is enabled.

A double click with the middle mouse button sets a new center of rotation.
|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer.
|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

With this method the middle mouse button may be released after the right mouse button is held pressed.

Users who use the mouse with their right hand may find this method easier than the first method.
}}




<div class="mw-translate-fuzzy">

### Навигация с жестове (v0.16) 


</div>

This style was tailored for use with a touchscreen and pen. Nevertheless, it can also be used with a mouse, and is recommended for use when using a Mac with a trackpad.


<div class="mw-translate-fuzzy">

Този стил на навигация е основно предназначен за работа с тъчскрийн или с електронна писалка/таблет. Може да се използва и само с мишка. {{Gesture Navigation/bg}}


</div>

Alternatively, tap and hold, then drag. This simulates the pan with the right mouse button. \|Zoom_text=Use the mouse wheel to zoom in and out. \|Zoom_gesture_text=Drag two fingers (pinch) closer or farther apart. \|Rotate_view_text=Hold the left mouse button, then move the pointer. In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

To set the camera\'s focus point for rotation, click a point with the middle mouse button. Alternatively, aim the cursor at a point and press **H** on the keyboard. \|Rotate_view_gesture_text=Drag with one finger to rotate.

Hold **Alt** when in the [Sketcher](Sketcher_Workbench.md). \|Tilt_view_text=Hold both left and right mouse buttons, then move the pointer sideways. \|Tilt_view_gesture_text=Rotate the imaginary line formed by two touch points.

This method is disabled by default. To enable, go to **Edit → Preferences → Display → Navigation**, and uncheck the \"Disable touchscreen tilt gesture\" checkbox. }}




<div class="mw-translate-fuzzy">

### Навигация с жестове стил Maya 


</div>

In Maya-Gesture Navigation, panning, zooming, and rotating the view require the **Alt** key together with a mouse button; therefore, a three-button mouse is required. It\'s also possible to use gestures as this style was developed over the [Gesture navigation](#Gesture_navigation.md) style.


<div class="mw-translate-fuzzy">

При навигация в стил Maya+жестове всички промени на изгледа се извършват като се задържи клавишът **ALT** и бутон на мишката. Поради това е нужна мишка с 3 бутона за използването на този стил. Ако нямате такава, е възможно и да се използват жестовете описани по-горе. {{MayaGesture Navigation/bg}}


</div>

Alternatively, use the mouse wheel to zoom in and out. \|Rotate_view_text=Hold **Alt** and the left mouse button, then move the pointer. }}

### OpenCascade navigation 

The OpenCascade navigation style was modeled after [OpenCascade](https://www.opencascade.com/).


{{OpenCascade Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Ctrl=**Ctrl**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold **Ctrl** and the left mouse button, then move the pointer.
|Rotate_view_text=Hold **Ctrl** and the right mouse button, then move the pointer.
}}

### OpenInventor navigation 


<div class="mw-translate-fuzzy">

### Стил на навгиация Inventor 

Този стил на навигация е наподобява програмата [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) (която не бива да се бърка с Autodesk Inventor). В този стил не можете да избирате обекти само с мишката. За да избирате обекти трябва да задържите натиснат бутонът **CTRL**. {{Inventor Navigation/bg}}


</div>

This style is not based on Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Shift=**Shift**
|Select_text=Hold **Shift**, then press the left mouse button over an object you want to select.

Hold **Ctrl** instead to select multiple objects.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold the middle mouse button, then press and hold the left mouse button, then move the pointer. 
|Rotate_view_text=Hold the left mouse button, then move the pointer.
}}

### OpenSCAD navigation 

The OpenSCAD navigation style was modeled after [OpenSCAD](https://openscad.org/).


<small>(v0.20)</small> 


{{OpenSCAD_Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.

Hold **Ctrl** and **Shift** when pressing the mouse button to drag an object in a sketch in edit mode.
|Pan_text=Hold the right mouse button, then move the pointer.
|Zoom_text=Hold the middle mouse button, then move the pointer.
Alternatively, hold **Shift** and the right mouse button, then move the pointer.
|Rotate_view_text=Hold the left mouse button, then move the pointer.
}}

### Revit navigation 

The Revit navigation style was modeled after [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit).


{{Revit Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold the middle mouse button, then move the pointer.

Alternatively, hold both left and right mouse buttons, then move the pointer.

|Zoom_text=Use the mouse wheel to zoom in and out.
|Rotate_view_text=Hold **Shift** and the middle mouse button, then move the pointer.

Alternatively, hold the middle mouse button, then press and hold the right mouse button, then move the pointer.
}}

### TinkerCAD navigation 

The TinkerCAD navigation style was modeled after [TinkerCAD](https://en.wikipedia.org/wiki/Tinkercad).


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




<div class="mw-translate-fuzzy">

### Навигация с тъчпад 


</div>

With the Touchpad navigation style, panning, zooming, and rotating the view require a modifier key together with the touchpad. This style can also be used with a mouse.


<div class="mw-translate-fuzzy">

В случай че разполагате само с тъчпад (например на лаптоп) може да използвате този стил. При навигацията с тъчпад за всяка операция (движение, ротация, промяна на мащаб) се използва и клавиатурата.


{{Touchpad Navigation/bg}}


</div>



## Поддържан хардуер 


<div class="mw-translate-fuzzy">

FreeCAD също поддържа някои [3D input devices](3D_input_devices.md).


</div>

## Recommended navigation for macOS 

On MacBooks with a trackpad the Gesture navigation works very well, but the gestures have a special meaning:

-   Zoom: drag with two fingers.
-   Rotate: drag with three fingers.
-   Pan: **Ctrl** + three fingers.

## Developing a custom navigation 

The tutorial [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) orients developers who want to develop a custom mouse navigation option. Familiarity with the C++ syntax is required.


{{docnav|Getting started/bg|Document structure/bg}}



---
⏵ [documentation index](../README.md) > Mouse navigation/bg
