# Mouse navigation/es
## Overview


<div class="mw-translate-fuzzy">

## Vista general 

La **Navegación Ratón** de FreeCAD consiste en los comandos utilizados para navegar visualmente por el espacio tridimensional e interactuar con los objetos mostrados. Actualmente hay 3 esquemas diferentes de navegación con el ratón en FreeCAD. El estilo de navegación por defecto se denomina \"Navegación CAD\", y es muy simple y práctico, pero FreeCAD también tiene dos estilos de navegación alternativos modelados según la navegación de Inventor y Blender.


</div>

For more information about selecting objects see [Selection methods](Selection_methods.md).

For more information about manipulating objects see [Std TransformManip](Std_TransformManip.md).

## Selecting a navigation style 


<div class="mw-translate-fuzzy">

-   En el [Editor de Preferencias](Preferences_Editor/es.md), sección Display, pestaña *Vista 3D*;
-   Pulsando con el botón derecho en un área vacía de la vista 3D y seleccionando *Estilo de navegación* en el menú contextual.


</div>

## Available navigation styles 


<div class="mw-translate-fuzzy">

### Navegación de Blender 


</div>

The Blender navigation style was modeled after [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">

En la Navegación de Blender, no se puede hacer un encuadre sólo con el ratón. Para hacer un encuadre, debes mantener presionada la tecla **SHIFT**. {{Blender Navigation/es}}


{{Blender Navigation
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

Alternatively, hold both left and right mouse buttons, and then move the pointer. \|Zoom_text=Use the mouse wheel to zoom in and out. \|Rotate_view_text=Hold the middle mouse button, then move the pointer. }}

### CAD navigation 


<div class="mw-translate-fuzzy">

### Navegación CAD 

Este es el estilo de navegación por defecto y permite al usuario un control simple de la vista, y no requiere el uso del teclado con la excepción de la realización de selecciones múltiples.


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

Hold down **Ctrl** to select multiple objects.
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

### Navegación Gestual 


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

Alternatively, tap and hold, then drag. This simulates the pan with the right mouse button. \|Zoom_text=Use the mouse wheel to zoom in and out. \|Zoom_gesture_text=Drag two fingers (pinch) closer or farther apart. \|Rotate_view_text=Hold the left mouse button, then move the pointer. In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

To set the camera\'s focus point for rotation, click a point with the middle mouse button. Alternatively, aim the cursor at a point and press **H** on the keyboard. \|Rotate_view_gesture_text=Drag with one finger to rotate.

Hold **Alt** when in the [Sketcher](Sketcher_Workbench.md). \|Tilt_view_text=Hold both left and right mouse buttons, then move the pointer sideways. \|Tilt_view_gesture_text=Rotate the imaginary line formed by two touch points.

On v0.18 this method is disabled by default. To enable, go to **Edit → Preferences → Display**, and untick \"Disable touchscreen tilt gesture\" checkbox. }}


<div class="mw-translate-fuzzy">

### Navegación Maya-Gestual 


</div>

In Maya-Gesture Navigation, panning, zooming, and rotating the view require the **Alt** key together with a mouse button; therefore, a three-button mouse is required. It\'s also possible to use gestures as this style was developed over the [Gesture navigation](#Gesture_navigation.md) style.


<div class="mw-translate-fuzzy">


{{MayaGesture Navigation
|Select_name=Selección
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotar la vista
|Alt={KEY|Alt}}

\|Select_text=Presione el botón izquierdo del ratón sobre un objeto que desee seleccionar. \|Pan_text=Mantenga pulsados **Alt** y el botón central del ratón, luego mueva el puntero. \|Zoom_text=Mantenga pulsados **Alt** y el botón derecho del ratón, luego mueva el puntero.


</div>

Alternatively, use the mouse wheel to zoom in and out. \|Rotate_view_text=Hold **Alt** and the left mouse button, then move the pointer. }}


<div class="mw-translate-fuzzy">

### OpenCascade


</div>

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

### Navegación de Inventor 

La navegación de OpenInventor (antes Inventor) fue modelada según [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor). Para seleccionar los objetos, debe mantener pulsada la tecla **Ctrl**.


</div>


<div class="mw-translate-fuzzy">

Este modo no está basado en el Autodesk Inventor.


</div>


{{OpenInventor Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Shift=**Shift**
|Select_text=Hold **Shift**, then press the left mouse button over an object you want to select.

Hold down **Ctrl** instead to select multiple objects.
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


<div class="mw-translate-fuzzy">

### Navegación Revit 


</div>

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

### Navegación Touchpad 


</div>

In Touchpad Navigation, panning, zooming, and rotating the view require a modifier key together with the touchpad.


<div class="mw-translate-fuzzy">

En la Navegación Touchpad, ni el barrido, ni el acercamiento, ni la rotación de vista son operaciones exclusivas del ratón (o del touchpad). {{Touchpad Navigation/es}}


{{Touchpad Navigation
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

## Soporte de Hardware 


<div class="mw-translate-fuzzy">

FreeCAD también soporta algún [Dispositivo de entrada 3D](3D_input_devices/es.md).


</div>


<div class="mw-translate-fuzzy">

## Problemas en Mac OS X 


</div>


<div class="mw-translate-fuzzy">

Recientemente hemos recibido reportes [en el foro](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0) de usuarios Mac que esas combinaciones de ratón y tecla no funcionan como se espera. Desafortunadamente, ninguno de los desarrolladores posee una Mac, tampoco otros contribuidores regulares. Necesitamos de tu ayuda para determinar que combinaciones de ratón y tecla funcionan para poder actualizar este wiki.


</div>

## Developing a custom navigation 

The tutorial [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) orients developers who want to develop a custom mouse navigation option. Familiarity with the C++ syntax is required.



---
⏵ [documentation index](../README.md) > Mouse navigation/es
