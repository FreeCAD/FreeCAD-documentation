





{{TOCright}}


<div class="mw-translate-fuzzy">

\"Model myši\" ve FreeCADu obsahuje příkazy používané k vizuální navigaci ve 3D prostoru a interakci se zobrazenými objekty. FreeCAD podporuje vícenásobný model navigačních stylů myši. Defaultní navigační styl je označován jako \"CAD navigace\" a je velmi jednoduchý a praktický, ale FreeCAD také poskytuje alternativní navigační styly, které si můžete vubrat podle Vašich požadavků.


</div>

## Navigace

Práce s objekty je společná pro všechny pracovní plochy. Následující gesta myši mohou být použita pro řízení pozice objektu a pohledu podle toho jaky styl je vybrán.

Jsou dva způsoby změny navigačního stylu:

-   V sekci Display (Zobrazení) [Editoru Předvoleb](Preferences_Editor/cs.md), záložka *3D Pohled*;
-   Kliknutím pravého tlačítka myši v prázdném prostoru v oblasti 3D pohledu a potom výběrem \"Navigačního stylu\" v kontextuálním menu.

### CAD Navigace (default) {#cad_navigace_default}

Je to defaultní navigační styl, který umožňuje uživateli jednoduchou kontrolu nad pohledem a nepožaduje používání klávesnice, kromě vícenásobného výběru. {{CAD Navigation/cs}} {{CAD Navigation
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

### Inventor Navigation (Tvůrčí navigace) {#inventor_navigation_tvůrčí_navigace}

Tvůrčí navigace, vytvářená podle [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) (nezaměňovat s Autodesk Inventor), kde se nepoužívá pouze výběr myší. Při vybírání objektů musíte držet stisknutou klávesu **CTRL**. {{Inventor Navigation/cs}} {{OpenInventor Navigation
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

V Blender Navigaci, vytvářené podle [Blenderu](http://www.blender.org), není snímání (kamerou) pouze myší. Při snímání pohledu kamerou musíte držet klávesu **SHIFT**. {{Blender Navigation/cs}} {{Blender Navigation
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

### Touchpad Navigation {#touchpad_navigation}

V Touchpad Navigaci, bez snímání, zoomování, a otáčení pohledu, jsou pouze operace s myší (nebo touchpadem). {{Touchpad Navigation/cs}} {{Touchpad Navigation
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

### Gesture Navigation (v0.16) {#gesture_navigation_v0.16}

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

On v0.18 this method is disabled by default. To enable, go to {{MenuCommand|Edit → Preferences → Display}}, and untick "Disable touchscreen tilt gesture" checkbox.
}}

Alternatively, tap and hold, then drag. This simulates the pan with the right mouse button. \|Zoom\_text=Use the mouse wheel to zoom in and out. \|Zoom\_gesture\_text=Drag two fingers (pinch) closer or farther apart. \|Rotate\_view\_text=Hold the left mouse button, then move the pointer. In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

To set the camera\'s focus point for rotation, click a point with the middle mouse button. Alternatively, aim the cursor at a point and press **H** on the keyboard. \|Rotate\_view\_gesture\_text=Drag with one finger to rotate.

Hold **Alt** when in the [Sketcher](Sketcher_Workbench.md). \|Tilt\_view\_text=Hold both left and right mouse buttons, then move the pointer sideways. \|Tilt\_view\_gesture\_text=Rotate the imaginary line formed by two touch points.

On v0.18 this method is disabled by default. To enable, go to {{MenuCommand|Edit → Preferences → Display}}, and untick \"Disable touchscreen tilt gesture\" checkbox. }}

### Maya-Gesture Navigation {#maya_gesture_navigation}


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

## Výběr objektu {#výběr_objektu}

### Jednoduchý výběr {#jednoduchý_výběr}

Objekty mohou být vybírány kliknutím levým tlačítkem myši na objekt ve 3D-pohledu nebo výběrem objektu ve stromu pohledu.

### Předvýběr

Je zde také možný mechanizmus*Předvýběru* který zvýrazňuje objekty a před výběrem zobrazuje informace o objektu při přechodu myší nad objektem. Pokud Vám takové chování nevyhovuje nebo pokud máte pomalý stroj, můžete v předvolbách přepnout Předvýběr na Off (Vypnuto).

## Manipulace s objekty {#manipulace_s_objekty}

FreeCAD nabízí [*manipulátory*](Manipulator.md) což jsou ovladače, které mohou být použity pro modifikace vzhledu objektu, jeho tvaru nebo jiných parametrů.

## Podpora hardwaru {#podpora_hardwaru}

FreeCAD také podporuje některé [3D vstupní zařízení](3D_input_devices/cs.md).

## Mac OS X problémy {#mac_os_x_problémy}

Nedávno jsme dostali oznámení [na fóru](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0) od uživatelů Mac, že uvedená tlačítka myši a kombinace kláves nefungují podle očekávání. Bohužel žádný z vývojářů nevlastní Mac a ani žádný zpravidelných spolupracovníků. Potřebujeme Vaši pomoc ke zjištění která tlačítka myši a klávesové kombinace mají uvedené problémy abychom mohli aktualizovat tuto stránku wiki.


{{docnav/cs|[Zacínáme](Getting_started/cs.md)|[Struktura dokumentu](Document_structure/cs.md)}}



