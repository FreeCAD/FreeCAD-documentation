





{{TOCright}}

## Overview

The FreeCAD **mouse navigation** consists of the commands used to visually navigate the 3D space and interact with the objects displayed. FreeCAD supports multiple mouse navigation styles. The default navigation style is referred to as \"CAD Navigation,\" and is very simple and practical, but FreeCAD also provides alternative navigation styles which you can choose according to your preferences.

## Navigation

The mouse gestures used for object manipulation vary depending on the Navigation style selected; the currently selected style is used for all workbenches.

There are two ways to change the navigation style:

-   In the [Preferences Editor](Preferences_Editor#Navigation.md); menu {{MenuCommand|Edit → Preferences → Display → Navigation → 3D Navigation}}.
-   By right-clicking in empty space in the 3D view, then selecting {{MenuCommand|Navigation styles}} in the context menu.

### CAD Navigation {#cad_navigation}

This is the default navigation style. It allows the user a simple control of the view, and does not require the use of keyboard keys except to make multi-selections.


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

### OpenInventor Navigation {#openinventor_navigation}

OpenInventor navigation (formerly Inventor) was modeled after [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor). In order to select objects, you must hold down the **Ctrl** key.

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

### Blender Navigation {#blender_navigation}

The Blender navigation style was modeled after [Blender](https://www.blender.org). Previously there was no mouse-only panning; it always required holding the **Shift** key. This changed in 2016, now you can hold both left and right mouse buttons to pan. {{Blender Navigation
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

### Touchpad Navigation {#touchpad_navigation}

In Touchpad Navigation, panning, zooming, and rotating the view require a modifier key together with the touchpad. {{Touchpad Navigation
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

### Gesture Navigation {#gesture_navigation}

This style was introduced in version 0.16, and was tailored for use with a touchscreen and pen. Nevertheless, it can also be used with a mouse, and is recommended for use when using a Mac with a trackpad. {{Gesture Navigation
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
|Tilt_view_text=Hold both left and right mouse buttons, then move the pointer sideways. 
|Tilt_view_gesture_text=Rotate the imaginary line formed by two touch points.

On v0.18 this method is disabled by default. To enable, go to {{MenuCommand|Edit → Preferences → Display}}, and untick "Disable touchscreen tilt gesture" checkbox.
}}

### Maya-Gesture Navigation {#maya_gesture_navigation}

In Maya-Gesture Navigation, panning, zooming, and rotating the view require the **Alt** key together with a mouse button; therefore, a three-button mouse is required. It\'s also possible to use gestures as this mode was developed over the [Gesture Navigation](#Gesture_Navigation.md) mode. {{MayaGesture Navigation
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

### Revit Navigation {#revit_navigation}

This style was introduced in version 0.18.


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

This style was introduced in version 0.18.


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

## Selecting objects {#selecting_objects}

### Simple selection {#simple_selection}

Objects can be selected by a click with the left mouse button either by clicking on the object in the [3D view](3D_view.md) or by selecting it in the [tree view](tree_view.md).

### Preselection

There is also a *Preselection* mechanism that highlights objects and displays information before selection by just hovering the mouse over the objects. If you don\'t like this behaviour or you have a slow machine, you can switch preselection off in the preferences.

## Manipulating Objects {#manipulating_objects}

FreeCAD offers [*manipulators*](Manipulator.md) that are handles that can be used to modify an object\'s appearance, shape, or other parameters.

## Hardware support {#hardware_support}

FreeCAD also supports some [3D input devices](3D_input_devices.md).

## Mac OS X Issues {#mac_os_x_issues}

Recently we got reports [on the forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0) from Mac users that those mouse button and key combination do not work as expected. Unfortunately, none of the developers owns a Mac, neither do the other regular contributors. We need your help to determine which mouse buttons and key combination work so we can update this wiki.






