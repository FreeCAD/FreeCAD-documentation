# Mouse navigation/tr
{{TOCright}}

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


<div class="mw-translate-fuzzy">

### Blender Gezinme 


</div>

The Blender navigation style was modeled after [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">

Blender Gezinme [Blender](http://www.blender.org)\'dan sonra eklendi. Daha önce tek başına fareyle taşıma yapılamıyordu,taşıma için**SHIFT** tuşu kullanılıyordu. 2016\'da bu özellik yenilendi. Hem fare sağ tuşu hem de fare sol tuşu birlikte basılı tutularak taşıma yapılabilir. {{Blender Navigation/tr}}


</div>

Alternatively, hold both left and right mouse buttons, and then move the pointer. \|Zoom_text=Use the mouse wheel to zoom in and out. \|Rotate_view_text=Hold the middle mouse button, then move the pointer. }}

### CAD navigation 


<div class="mw-translate-fuzzy">

### CAD Gezinme (varsayılan) 

Bu, varsayılan gezinme stilidir. Kullanıcıya görünümün basit bir kontrolünü sağlar ve çoklu seçim yapmak dışında klavye tuşlarının kullanılmasını gerektirmez. {{CAD Navigation/tr}}


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

### Gesture Gezinme (v0.16) 


</div>

This style was tailored for use with a touchscreen and pen. Nevertheless, it can also be used with a mouse, and is recommended for use when using a Mac with a trackpad.


<div class="mw-translate-fuzzy">

Bu gezinme stili dokunmatik ekran ve kalemle kullanım için uyarlandı, ancak dokunmatik fare için de kullanılabilir. {{Gesture Navigation/tr}}


</div>

Alternatively, tap and hold, then drag. This simulates the pan with the right mouse button. \|Zoom_text=Use the mouse wheel to zoom in and out. \|Zoom_gesture_text=Drag two fingers (pinch) closer or farther apart. \|Rotate_view_text=Hold the left mouse button, then move the pointer. In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

To set the camera\'s focus point for rotation, click a point with the middle mouse button. Alternatively, aim the cursor at a point and press **H** on the keyboard. \|Rotate_view_gesture_text=Drag with one finger to rotate.

Hold **Alt** when in the [Sketcher](Sketcher_Workbench.md). \|Tilt_view_text=Hold both left and right mouse buttons, then move the pointer sideways. \|Tilt_view_gesture_text=Rotate the imaginary line formed by two touch points.

On v0.18 this method is disabled by default. To enable, go to **Edit → Preferences → Display**, and untick \"Disable touchscreen tilt gesture\" checkbox. }}


<div class="mw-translate-fuzzy">

### Maya-Gesture Gezinme 


</div>

In Maya-Gesture Navigation, panning, zooming, and rotating the view require the **Alt** key together with a mouse button; therefore, a three-button mouse is required. It\'s also possible to use gestures as this style was developed over the [Gesture navigation](#Gesture_navigation.md) style.


<div class="mw-translate-fuzzy">

Maya-Gesture Gezinme,**ALT** tuşu ve bir fare düğmesine basarak tüm görünüm hareketleri etkinleştirilir , böylece bu gezinme modunu doğru kullanmak için 3 düğmeli bir fareye ihtiyaç duyulur. Alternatif olarak, bu mod, normal Gesture Gezinme modu üzerinde geliştirildiği için tüm Gestures hareketlerini kullanmak mümkündür. {{MayaGesture Navigation/tr}}


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

### OpenInventor Gezinme 

OpenInventor\'de (önceden Inventor) gezinme, [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) den sonra eklendi. (Bu mod Autodesk Inventor\'a dayalı değildir.) Fare tek başına yeterli değildir. Nesneleri seçmek için,**CTRL** tuşunu basılı tutmanız gerekir . {{Inventor Navigation/tr
}}


</div>

This style is not based on Autodesk Inventor.


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

### Dokunmatik fare gezinme 


</div>

In Touchpad Navigation, panning, zooming, and rotating the view require a modifier key together with the touchpad.


<div class="mw-translate-fuzzy">

Dokunmatik fare gezinti de, Taşıma , zumlama ve döndürme işlemleri, yalnız fare kullanılarak (veya yalnız dokunmatik fare) yapılamaz. {{Touchepad Navigation/tr}}


</div>

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

## Developing a custom navigation 

The tutorial [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) orients developers who want to develop a custom mouse navigation option. Familiarity with the C++ syntax is required.


{{docnav/tr|[Başlangıç](Getting_started/tr.md)|[Belge yapısı](Document_structure/tr.md)}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Mouse navigation/tr
