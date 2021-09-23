# Mouse navigation/ro






{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

**Modelul mouse-ului** in FreeCAD este constituit din comenzi folosite la navigarea spațiului 3D și interacțiunea cu obiectele afișate. In versiunea actuală există trei moduri diferite de navigare. Modul implicit este numit \"Navigare CAD\" și este foarte simplu și practic, dar FreeCAD are două stiluri alternative modelate dupa navigarea în Inventor si Blender.


</div>

## Navigation


<div class="mw-translate-fuzzy">

## Navigarea

Modul de lucru cu obiecte este comun pentru toate paletele. Urmatoarele acțiuni cu mouse-ul pot fi folosite pentru controlul poziției si modului de vizualizare, în functie de stilul de navigare selectat.


</div>

Exista două moduri de a schimba stilul de navigare:

-   In dialogul pentru [preferinte](Preferences_Editor/ro.md), secțiunea Afișare, tab-ul *Vizualizare 3D*;
-   Click-dreapta în spațiul liber în zona de vizualizare 3D, selectând *Stil de navigare* în meniul contextual.

### CAD navigation 


<div class="mw-translate-fuzzy">

### Navigare CAD (implicita) 

Acesta este modul de navigare implicit și permite utilizatorului un control simplu al vizualizării; nu este nevoie de folosirea tastaturii decât pentru selecție multiplă. {{CAD Navigation/ro}}


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

### OpenInventor navigation 


<div class="mw-translate-fuzzy">

### Navigare Tip Inventor 

In acest tip de navigare modelată după [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) (a nu se confunda cu Autodesk Inventor) nu exista selectie cu mouse-ul. Pentru selectare trebuie apasată tasta **CTRL**. {{Inventor Navigation/ro}}


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


<div class="mw-translate-fuzzy">

### Navigare Tip Blender 


</div>

Blender Navigation a fost modelat după [Blender](http://www.blender.org). Anterior nu a existat o panoramare cu mouse-ul și a fost necesară utilizarea tastei {{KEY | SHIFT}} pentru a panorama vederea. Acest lucru s-a schimbat în 2016, cu o adăugare de caracteristici. Pentru a panorama vizualizarea, puteți apăsa acum butoanele mouse-ului stânga și dreapta și trageți în vizualizare. {{Blender Navigation
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


<div class="mw-translate-fuzzy">

### Navigarea cu Touchpad-ul 


</div>

În Navigatorul cu touchpad, nici panningul, nici zoom-ul, nici rotirea vizualizării nu sunt operații numai pentru mouse (sau doar touchpad). {{Touchpad Navigation
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


<div class="mw-translate-fuzzy">

### Navigarea prin Gesturi(v0.16) 


</div>

Acest stil de navigare a fost adaptat pentru utilizarea cu touchscreen și stiloul, dar este foarte ușor de utilizat cu mouse-ul. {{Gesture Navigation
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


<div class="mw-translate-fuzzy">

### Navigare tip Maya 


</div>


<div class="mw-translate-fuzzy">

În navigația Maya-Gesture, toate mișcările de vizualizare sunt activate prin apăsarea butonului {{KEY | ALT}} și a butonului mouse-ului, astfel încât să fie necesar un mouse cu 3 butoane pentru a utiliza corect acest mod de navigare. Alternativ, este posibil să utilizați gesturi, deoarece acest mod a fost dezvoltat în modul normal de navigare prin gesturi. {{MayaGesture Navigation
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

### Revit navigation 

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

### OpenCascade navigation 

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

## Selectarea Obiectelor 

### Simple selection 


<div class="mw-translate-fuzzy">

### Selecția Simplă 

Obiectele se selectează cu click-stânga în vizualizarea 3D sau selectare în vizualizarea arborescentă.


</div>

### Preselection


<div class="mw-translate-fuzzy">

### Preselecție

Există, de asemenea, și un mecanism de preselecție care evidențiază obiectele și prezintă informații despre ele înainte de a fi selectate, doar prin mișcarea mouse-ului deasupra lor. Dacă nu agreați acest comportament sau calculatorul este lent puteți să-l suprimați din dialogul pentru preferințe.


</div>

## Manipulating objects 


<div class="mw-translate-fuzzy">

## Manipularea Obiectelor 

FreeCAD oferă [manipulatori](manipulator/ro.md) ce pot fi folosiți pentru a schimba aparența sau proprietățile obiectului.


</div>

## Suport Hardware 


<div class="mw-translate-fuzzy">

FreeCAD suportă și un număr de [dispozitive 3D](3D_input_devices/ro.md).


</div>


<div class="mw-translate-fuzzy">

## Probleme la Mac OS X 


</div>


<div class="mw-translate-fuzzy">

Recent am primit rapoarte [pe forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0) de la utilizatorii de Mac la care acele combinații de taste și butoane de mouse nu funcționează conform așteptărilor. Din păcate, niciunul dintre dezvoltatori nu deține un Mac, nici ceilalți contributori obișnuiți. Avem nevoie de ajutorul tău pentru a determina ce butoane și combinații de taste ale mouse-ului funcționează astfel încât să putem actualiza acest


</div>

## Developing a custom navigation 

The tutorial [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) orients developers who want to develop a custom mouse navigation option. Familiarity with the C++ syntax is required.


{{docnav/ro|Getting started/ro|Document structure/ro}}



