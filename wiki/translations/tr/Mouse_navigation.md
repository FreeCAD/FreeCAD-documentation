# Mouse navigation/tr
## Overview


<div class="mw-translate-fuzzy">

FreeCAD fare ile modelleme , 3D alanda görsel olarak gezinmek ve görüntülenen nesnelerle etkileşimde bulunmak için kullanılan komutlardan oluşur. FreeCAD, çoklu fare modeli gezinme stillerini destekler. Varsayılan gezinme stiline \"CAD Gezinme\" denir ve çok basit ve pratiktir, ancak FreeCAD ayrıca tercihlerinize göre seçebileceğiniz alternatif gezinme stilleri de sunar.


</div>

For more information about selecting objects see [Selection methods](Selection_methods.md).

For more information about manipulating objects see [Std TransformManip](Std_TransformManip.md).

## Selecting a navigation style 


<div class="mw-translate-fuzzy">

-   [Seçenekler penceresi](Preferences_Editor.md) içinde 3D Görünüm → 3D Navigasyon → Ekran → Düzen → Tercihler .
-   3D görünümünde boş alana sağ tıklayarak, ardından bağlam menüsünde \"Gezinme stili\" seçeneğini seçerek.


</div>

## Available navigation styles 

With all navigation styles, unless selecting objects from a sketch in edit mode, you must hold **Ctrl** to select multiple objects.

The following keyboard options are available for all styles:

-    **Ctrl**\+ {{ASCII|43}} and **Ctrl** + {{ASCII|22}} or **PgUp** and **PgDn** to zoom in and out, respectively.

-   The arrow keys, {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, to pan the view left/right and up/down.

-    **Shift**\+ {{ASCII|17}} and **Shift** + {{ASCII|16}} to rotate the view by 90 degrees.




<div class="mw-translate-fuzzy">

### Blender Gezinme 


</div>

The Blender navigation style was modeled after [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">

Blender Gezinme [Blender](http://www.blender.org)\'dan sonra eklendi. Daha önce tek başına fareyle taşıma yapılamıyordu,taşıma için**SHIFT** tuşu kullanılıyordu. 2016\'da bu özellik yenilendi. Hem fare sağ tuşu hem de fare sol tuşu birlikte basılı tutularak taşıma yapılabilir. {{Blender Navigation/tr}}


</div>

\|Shift=**Shift**

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Use the mouse wheel to zoom in and out.

\|Rotate_view_text=Hold the middle mouse button, then move the pointer.

\|Pan_text=Hold **Shift** and the middle mouse button, then move the pointer.

Alternatively, hold both left and right mouse buttons, and then move the pointer. }}

### CAD navigation 


<div class="mw-translate-fuzzy">

### CAD Gezinme (varsayılan) 

Bu, varsayılan gezinme stilidir. Kullanıcıya görünümün basit bir kontrolünü sağlar ve çoklu seçim yapmak dışında klavye tuşlarının kullanılmasını gerektirmez. {{CAD Navigation/tr}}


</div>


{{CAD Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view<br>First method
|Rotate_view_alt_name=Rotate view<br>Alternate method
|Pan_name=Pan

|Ctrl=**Ctrl**
|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor.

|Rotate_view_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

If the buttons are released before you stop the mouse motion, the view continues spinning, if this is enabled.

A double click with the middle mouse button sets a new center of rotation.

|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

With this method the middle mouse button may be released after the right mouse button is held pressed.

Users who use the mouse with their right hand may find this method easier than the first method.

|Pan_text=Hold the middle mouse button, then move the pointer.

|Zoom_mode_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer.

|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer.

|Pan_mode_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer.
}}




<div class="mw-translate-fuzzy">

### Gesture Gezinme (v0.16) 


</div>

This style was tailored for use with a touchscreen and pen. Nevertheless, it can also be used with a mouse, and is recommended for use when using a Mac with a trackpad.


<div class="mw-translate-fuzzy">

Bu gezinme stili dokunmatik ekran ve kalemle kullanım için uyarlandı, ancak dokunmatik fare için de kullanılabilir. {{Gesture Navigation/tr}}


</div>

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Use the mouse wheel to zoom in and out.

\|Rotate_view_text=Hold the left mouse button, then move the pointer. In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

To set the camera\'s focus point for rotation, click a point with the middle mouse button. Alternatively, aim the cursor at a point and press **H** on the keyboard.

\|Pan_text=Hold the right mouse button, then move the pointer.

\|Tilt_view_text=Hold both left and right mouse buttons, then move the pointer sideways.

\|Select_gesture_text=Tap to select.

\|Zoom_gesture_text=Drag two fingers (pinch) closer or farther apart.

\|Rotate_view_gesture_text=Drag with one finger to rotate.

Hold **Alt** when in the [Sketcher](Sketcher_Workbench.md).

\|Pan_gesture_text=Drag with two fingers.

Alternatively, tap and hold, then drag. This simulates the pan with the right mouse button.

\|Tilt_view_gesture_text=Rotate the imaginary line formed by two touch points.

This method is disabled by default. To enable, go to **Edit → Preferences → Display → Navigation**, and uncheck the \"Disable touchscreen tilt gesture\" checkbox. }}




<div class="mw-translate-fuzzy">

### Maya-Gesture Gezinme 


</div>

In Maya-Gesture Navigation, panning, zooming, and rotating the view require the **Alt** key together with a mouse button; therefore, a three-button mouse is required. It\'s also possible to use gestures as this style was developed over the [Gesture navigation](#Gesture_navigation.md) style.


<div class="mw-translate-fuzzy">

Maya-Gesture Gezinme,**ALT** tuşu ve bir fare düğmesine basarak tüm görünüm hareketleri etkinleştirilir , böylece bu gezinme modunu doğru kullanmak için 3 düğmeli bir fareye ihtiyaç duyulur. Alternatif olarak, bu mod, normal Gesture Gezinme modu üzerinde geliştirildiği için tüm Gestures hareketlerini kullanmak mümkündür. {{MayaGesture Navigation/tr}}


</div>

\|Alt=**Alt**

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold **Alt** and the right mouse button, then move the pointer.

\|Rotate_view_text=Hold **Alt** and the left mouse button, then move the pointer.

\|Pan_text=Hold **Alt** and the middle mouse button, then move the pointer.

\|Tilt_view_text=Hold **Alt** and both left and right mouse buttons, and then move the pointer sideways. }}

### OpenCascade navigation 

The OpenCascade navigation style was modeled after [OpenCascade](https://www.opencascade.com/).


{{OpenCascade Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Pan_name=Pan

|Ctrl=**Ctrl**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold **Ctrl** and the left mouse button, then move the pointer.

|Rotate_view_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

Alternatively, hold **Ctrl** and the right mouse button, then move the pointer.

|Pan_text=Hold the middle mouse button, then move the pointer. It is possible to hold **Ctrl**.
}}

### OpenInventor navigation 


<div class="mw-translate-fuzzy">

### OpenInventor Gezinme 

OpenInventor\'de (önceden Inventor) gezinme, [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) den sonra eklendi. (Bu mod Autodesk Inventor\'a dayalı değildir.) Fare tek başına yeterli değildir. Nesneleri seçmek için,**CTRL** tuşunu basılı tutmanız gerekir . {{Inventor Navigation/tr
}}


</div>

This style is not based on Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Pan_name=Pan

|Shift=**Shift**

|Select_text=Hold **Shift**, then press the left mouse button over an object you want to select.

Hold **Ctrl** instead to select multiple objects.

|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

|Rotate_view_text=Hold the left mouse button, then move the pointer.

|Pan_text=Hold the middle mouse button, then move the pointer.
}}

### OpenSCAD navigation 

The OpenSCAD navigation style was modeled after [OpenSCAD](https://openscad.org/).


{{OpenSCAD_Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Pan_name=Pan

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

{{VersionMinus|0.21}} Hold **Ctrl** and **Shift** when pressing the mouse button to drag an object in a sketch in edit mode.

|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold the middle mouse button, then move the pointer.

Or hold **Shift** and the right mouse button, then move the pointer.

|Rotate_view_text=Hold the left mouse button, then move the pointer.

Alternatively, and when a sketch is in edit mode, hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

|Pan_text=Hold the right mouse button, then move the pointer.
}}

### Revit navigation 

The Revit navigation style was modeled after [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit).


{{Revit Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Pan_name=Pan

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Hold **Shift** and the middle mouse button, then move the pointer.

Alternatively, hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

|Pan_text=Hold the middle mouse button, then move the pointer.

Alternatively, hold both left and right mouse buttons, then move the pointer.
}}

### TinkerCAD navigation 

The TinkerCAD navigation style was modeled after [TinkerCAD](https://en.wikipedia.org/wiki/Tinkercad).


{{TinkerCAD Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Pan_name=Pan

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Press the right mouse button, then move the pointer.

|Pan_text=Hold the middle mouse button, then move the pointer.
}}




<div class="mw-translate-fuzzy">

### Dokunmatik fare gezinme 


</div>

With the Touchpad navigation style, panning, zooming, and rotating the view require a modifier key together with the touchpad. This style can also be used with a mouse.


<div class="mw-translate-fuzzy">

Dokunmatik fare gezinti de, Taşıma , zumlama ve döndürme işlemleri, yalnız fare kullanılarak (veya yalnız dokunmatik fare) yapılamaz. {{Touchepad Navigation/tr}}


</div>

\|Ctrl=**Ctrl** \|Shift=**Shift** \|Alt=**Alt**

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Hold **Ctrl** and **Shift**, then move the pointer.

\|Rotate_view_text=Hold **Alt**, then move the pointer.

Alternatively, hold **Shift** and the left button, then move the pointer.

\|Pan_text=Hold **Shift**, then move the pointer. }}



## Donanım desteği 


<div class="mw-translate-fuzzy">

FreeCAD, ayrıca bazı [ 3D giriş cihazlarını](3D_input_devices/tr.md) destekler.


</div>




<div class="mw-translate-fuzzy">

## Mac OS X Sorunları 


</div>


<div class="mw-translate-fuzzy">

Son zamanlarda Mac kullanıcılarından [forum\'da](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0) bu fare tuş ve klavye tuş kombinasyonunun beklendiği gibi çalışmadığı bildirildi.Maalesef, geliştiricilerin hiçbiri Mac\'e sahip değil, diğer düzenli katkı yapanlar da yok. Hangi wiki düğmelerinin ve tuş kombinasyonunun işe yaradığını belirlemek için sizin yardımınıza ihtiyacımız var, böylece bu wiki\'yi güncelleyebiliriz.


</div>


{{docnav/tr|[Başlangıç](Getting_started/tr.md)|[Belge yapısı](Document_structure/tr.md)}}



---
⏵ [documentation index](../README.md) > Mouse navigation/tr
