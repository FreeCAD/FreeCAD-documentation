# Mouse navigation/id
{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

Penggunaan mouse di FreeCAD berisi perintah - perintah yang digunakan untuk navigasi pada tampilan 3D dan berinteraksi dengan objek yang di tampilkan. Ada tiga mode navigasi yang berbeda. Navigasi standar (default) mengarah pada \"CAD Navigation,\"yang sangat simpel dan praktis, tetapi FreeCAD juga memiliki 2 alternativ mode navigasi yaitu mode Inventor dan mode Blender.


</div>

For more information about selecting objects see [Selection methods](Selection_methods.md).

For more information about manipulating objects see [Std TransformManip](Std_TransformManip.md).

## Selecting a navigation style 


<div class="mw-translate-fuzzy">

-   Di menu Edit, [Preferences Editor](Preferences_Editor.md), pilih pada bagian Display, klik pada tab *3D View* ;
-   Dengan klik-kanan pada bagian tampilan 3d yang kosong, kemudian klik *Navigation style* dan pilih mode yang diinginkan.


</div>

## Available navigation styles 


<div class="mw-translate-fuzzy">

### Blender Navigation 


</div>

The Blender navigation style was modeled after [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">

Pada mode navigasi Blender, tidak ada perintah pan (menggeser layar 3D). Untuk melalukan penggeseran layar (pan) kamu harus menekan tombol **SHIFT**. {{Blender Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold **Shift** and the middle mouse button, then move the pointer.

Alternatively, hold both left and right mouse buttons, and then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.
|Rotate_view_text=Hold the middle mouse button, then move the pointer.
}}


</div>

Alternatively, hold both left and right mouse buttons, and then move the pointer. \|Zoom\_text=Use the mouse wheel to zoom in and out. \|Rotate\_view\_text=Hold the middle mouse button, then move the pointer. }}

### CAD navigation 


<div class="mw-translate-fuzzy">

### CAD Navigation (default) 

Mode ini adalah Nnavigasi standar bawaan dan memungkinkan pemakai mengendalikan tampilan dengan mudah, dan tidak memerlukan tombol keyboard kecuali untuk memilih multi objek.


{{CAD Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view<br>First method
|Rotate_view_alt_name=Rotate view<br>Alternate method
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.

Holding down **Ctrl** allows the selection of multiple objects.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Pan_mode_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Zoom_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor.
|Zoom_mode_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Rotate_view_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

The cursor location when the middle mouse button is pressed determines the center of rotation. Rotation works like spinning a ball which rotates around its center. If the buttons are released before you stop the mouse motion, the view continues [[spinning]], if this is enabled.

A double click with the middle mouse button sets a new center of rotation.
|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

With this method the middle mouse button may be released after the right mouse button is held pressed.

Users who use the mouse with their right hand may find this method easier than the first method.
}}


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

Holding down **Ctrl** allows the selection of multiple objects.
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

### Gesture Navigation (v0.16) 


</div>

This style was tailored for use with a touchscreen and pen. Nevertheless, it can also be used with a mouse, and is recommended for use when using a Mac with a trackpad.


<div class="mw-translate-fuzzy">

This navigation style was tailored for usability with touchscreen and pen, but is very usable with mouse too. {{Gesture Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Tilt_view_name=Tilt view
|Select_text=Press the left mouse button over an object you want to select.
|Select_gesture_text=Tap to select.
|Pan_text=Hold the right mouse button, then move the pointer.
|Pan_gesture_text=Drag with two fingers.

Alternatively, tap and hold, then drag. This simulates the pan with the right mouse button.
|Zoom_text=Use the mouse wheel to zoom in and out.
|Zoom_gesture_text=Drag two fingers (pinch) closer or farther apart.
|Rotate_view_text=Hold the left mouse button, then move the pointer.
In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

To set the camera's focus point for rotation, click a point with the middle mouse button. Alternatively, aim the cursor at a point and press **H** on the keyboard.
|Rotate_view_gesture_text=Drag with one finger to rotate.

Hold **Alt** when in the [Sketcher](Sketcher_Workbench.md).
|Tilt_view_text=Hold both left and right mouse buttons, and then move the pointer sideways. 
|Tilt_view_gesture_text=Rotate the imaginary line formed by two touch points.

On v0.18 this method is disabled by default. To enable, go to **Edit → Preferences → Display**, and untick "Disable touchscreen tilt gesture" checkbox.
}}


</div>

Alternatively, tap and hold, then drag. This simulates the pan with the right mouse button. \|Zoom\_text=Use the mouse wheel to zoom in and out. \|Zoom\_gesture\_text=Drag two fingers (pinch) closer or farther apart. \|Rotate\_view\_text=Hold the left mouse button, then move the pointer. In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

To set the camera\'s focus point for rotation, click a point with the middle mouse button. Alternatively, aim the cursor at a point and press **H** on the keyboard. \|Rotate\_view\_gesture\_text=Drag with one finger to rotate.

Hold **Alt** when in the [Sketcher](Sketcher_Workbench.md). \|Tilt\_view\_text=Hold both left and right mouse buttons, then move the pointer sideways. \|Tilt\_view\_gesture\_text=Rotate the imaginary line formed by two touch points.

On v0.18 this method is disabled by default. To enable, go to **Edit → Preferences → Display**, and untick \"Disable touchscreen tilt gesture\" checkbox. }}


<div class="mw-translate-fuzzy">

### Maya-Gesture Navigation 


</div>

In Maya-Gesture Navigation, panning, zooming, and rotating the view require the **Alt** key together with a mouse button; therefore, a three-button mouse is required. It\'s also possible to use gestures as this mode was developed over the [Gesture navigation](#Gesture_navigation.md) mode.


<div class="mw-translate-fuzzy">

In Maya-Gesture Navigation, all view movements are activated pressing **ALT** and a mouse button, so that it will be needed to have a 3 button mouse in order to correctly use this navigation mode. Alternately it\'s possible to use gestures as this mode was been developed over the normal Gesture Navigation mode. {{MayaGesture Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Alt=**Alt**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold **Alt** and the middle mouse button, then move the pointer.
|Zoom_text=Hold **Alt** and the right mouse button, then move the pointer.

Alternatively, use the mouse wheel to zoom in and out.
|Rotate_view_text=Hold **Alt** and the left mouse button, then move the pointer.
}}


</div>

Alternatively, use the mouse wheel to zoom in and out. \|Rotate\_view\_text=Hold **Alt** and the left mouse button, then move the pointer. }}

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

### Inventor Navigation 

Mode navigasi Inventor, tidak ada pemilihan objek pada mode ini. Untuk memilih objek kita harus menekan tombol **CTRL**. {{OpenInventor Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Ctrl=**Ctrl**
|Select_text=Hold **Ctrl**, then press the left mouse button over an object you want to select.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold the middle mouse button, then press and hold the left mouse button, then move the pointer. 
|Rotate_view_text=Hold the left mouse button, then move the pointer.
}}


</div>

This mode is not based on Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Ctrl=**Ctrl**
|Select_text=Hold **Ctrl**, then press the left mouse button over an object you want to select.
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

### Touchpad Navigation 


</div>

In Touchpad Navigation, panning, zooming, and rotating the view require a modifier key together with the touchpad.


<div class="mw-translate-fuzzy">

In Touchpad Navigation, neither panning, nor zooming, nor rotating the view, are mouse-only (or touchpad-only) operations. {{Touchpad Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Shift=**Shift**
|Ctrl=**Ctrl**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold **Shift**, then move the pointer.
|Zoom_text=Use **PageUp** and **PageDown** to zoom in and out.
|Zoom_alt_text=Alternatively, hold **Shift** and **Ctrl**, then move the pointer.
|Rotate_view_text=Hold **Alt**, then move the pointer.
|Rotate_view_alt_text=Alternatively, hold **Shift** and the left button, then move the pointer.
}}


</div>

## Hardware support 


<div class="mw-translate-fuzzy">

FreeCAD juga mendukung beberapa jenis dari [3D input devices](3D_input_devices.md).


</div>

## Recommended navigation for macOS 

On MacBooks with a trackpad the Gesture navigation works very well, but the gestures have a special meaning:

-   Zoom: drag with two fingers.
-   Rotate: drag with three fingers.
-   Pan: **Ctrl** + three fingers.

## Developing a custom navigation 

The tutorial [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) orients developers who want to develop a custom mouse navigation option. Familiarity with the C++ syntax is required.


{{docnav|Getting started|Document structure}}

---
[documentation index](../README.md) > Mouse navigation/id
