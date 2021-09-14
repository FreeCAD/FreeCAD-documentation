# Mouse navigation/es







{{TOCright}}

## Vista general 

La **Navegación Ratón** de FreeCAD consiste en los comandos utilizados para navegar visualmente por el espacio tridimensional e interactuar con los objetos mostrados. Actualmente hay 3 esquemas diferentes de navegación con el ratón en FreeCAD. El estilo de navegación por defecto se denomina \"Navegación CAD\", y es muy simple y práctico, pero FreeCAD también tiene dos estilos de navegación alternativos modelados según la navegación de Inventor y Blender.

## Navegación

Los gestos del ratón utilizados para la manipulación de objetos varían según el estilo de navegación seleccionado; el estilo seleccionado actualmente se utiliza para todos los ambientes de trabajo.

Hay dos formas de cambiar el estilo de navegación:

-   En el [Editor de Preferencias](Preferences_Editor/es.md), sección Display, pestaña *Vista 3D*;
-   Pulsando con el botón derecho en un área vacía de la vista 3D y seleccionando *Estilo de navegación* en el menú contextual.

### Navegación CAD 

Este es el estilo de navegación por defecto y permite al usuario un control simple de la vista, y no requiere el uso del teclado con la excepción de la realización de selecciones múltiples.


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

The cursor location when the middle mouse button is pressed determines the center of rotation. Rotation works like spinning a ball which rotates around its center. If the buttons are released before you stop the mouse motion, the view continues [spinning](spinning.md), if this is enabled.

A double click with the middle mouse button sets a new center of rotation.
|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

With this method the middle mouse button may be released after the right mouse button is held pressed.

Users who use the mouse with their right hand may find this method easier than the first method.
}}

### Navegación de Inventor 

La navegación de OpenInventor (antes Inventor) fue modelada según [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor). Para seleccionar los objetos, debe mantener pulsada la tecla **Ctrl**.

Este modo no está basado en el Autodesk Inventor.


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

### Navegación de Blender 

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

Alternatively, hold both left and right mouse buttons, and then move the pointer. \|Zoom\_text=Use the mouse wheel to zoom in and out. \|Rotate\_view\_text=Hold the middle mouse button, then move the pointer. }}

### Navegación Touchpad 

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

### Navegación Gestual 

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

Alternatively, tap and hold, then drag. This simulates the pan with the right mouse button. \|Zoom\_text=Use the mouse wheel to zoom in and out. \|Zoom\_gesture\_text=Drag two fingers (pinch) closer or farther apart. \|Rotate\_view\_text=Hold the left mouse button, then move the pointer. In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

To set the camera\'s focus point for rotation, click a point with the middle mouse button. Alternatively, aim the cursor at a point and press **H** on the keyboard. \|Rotate\_view\_gesture\_text=Drag with one finger to rotate.

Hold **Alt** when in the [Sketcher](Sketcher_Workbench.md). \|Tilt\_view\_text=Hold both left and right mouse buttons, then move the pointer sideways. \|Tilt\_view\_gesture\_text=Rotate the imaginary line formed by two touch points.

On v0.18 this method is disabled by default. To enable, go to **Edit → Preferences → Display**, and untick \"Disable touchscreen tilt gesture\" checkbox. }}

### Navegación Maya-Gestual 

En Navegación Maya-Gestual, la panorámica, el zoom y la rotación de la vista requieren la tecla **Alt** junto con un botón del ratón; por lo tanto, se requiere un ratón de tres botones. También es posible utilizar gestos, ya que este modo fue desarrollado sobre el modo [Navegación Gestual](#Navegación_Gestual.md). {{Navegación Maya-Gestual
|Select_name=Selección
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotar la vista
|Alt={KEY|Alt}} \|Select\_text=Presione el botón izquierdo del ratón sobre un objeto que desee seleccionar. \|Pan\_text=Mantenga pulsados **Alt** y el botón central del ratón, luego mueva el puntero. \|Zoom\_text=Mantenga pulsados **Alt** y el botón derecho del ratón, luego mueva el puntero.

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator

Alternatively, use the mouse wheel to zoom in and out. \|Rotate\_view\_text=Hold **Alt** and the left mouse button, then move the pointer. }}

### Navegación Revit 

Este estilo fue introducido en la versión 0.18.


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

### OpenCascade

Este estilo fue introducido en la versión 0.18.


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

## Seleccionando objetos 

### Selección simple 

Los objetos pueden seleccionarse mediante un clic con el botón izquierdo del ratón o bien pulsando sobre el objeto en [la vista 3D](3D_view/es.md) o seleccionándolo en la [vista en árbol](tree_view/es.md).

También hay un mecanismo de preselección que resalta los tobjetos y muestra información de ellos antes de seleccionarlos con sólo pasar el ratón sobre ellos. Si no te gusta ese comportamiento o si tienes una máquina lenta, puedes desactivar la opción de preselección en el menú de *preferencias*.

## Manipulación de Objetos 

FreeCAD ofrece [manipuladores](manipulator/es.md) que se pueden utilizar para modificar un objeto o su aspecto visual.

## Soporte de Hardware 

FreeCAD también soporta algún [Dispositivo de entrada 3D](3D_input_devices/es.md).

## Problemas en Mac OS X 

Recientemente hemos recibido reportes [en el foro](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0) de usuarios Mac que esas combinaciones de ratón y tecla no funcionan como se espera. Desafortunadamente, ninguno de los desarrolladores posee una Mac, tampoco otros contribuidores regulares. Necesitamos de tu ayuda para determinar que combinaciones de ratón y tecla funcionan para poder actualizar este wiki.






