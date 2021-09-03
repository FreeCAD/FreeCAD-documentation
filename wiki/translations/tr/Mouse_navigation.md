





{{TOCright}}


<div class="mw-translate-fuzzy">

FreeCAD fare ile modelleme , 3D alanda görsel olarak gezinmek ve görüntülenen nesnelerle etkileşimde bulunmak için kullanılan komutlardan oluşur. FreeCAD, çoklu fare modeli gezinme stillerini destekler. Varsayılan gezinme stiline \"CAD Gezinme\" denir ve çok basit ve pratiktir, ancak FreeCAD ayrıca tercihlerinize göre seçebileceğiniz alternatif gezinme stilleri de sunar.


</div>

## Gezinme

Nesne işleme, tüm tezgahlarda ortaktır. Aşağıdaki fare hareketleri, nesnenin konumunu kontrol etmek ve seçilen Gezinme stiline göre görüntülemek için kullanılabilir.

Gezinme stilini değiştirmenin iki yolu vardır:

-   [Seçenekler penceresi](Preferences_Editor.md) içinde 3D Görünüm → 3D Navigasyon → Ekran → Düzen → Tercihler .
-   3D görünümünde boş alana sağ tıklayarak, ardından bağlam menüsünde \"Gezinme stili\" seçeneğini seçerek.

### CAD Gezinme (varsayılan) 

Bu, varsayılan gezinme stilidir. Kullanıcıya görünümün basit bir kontrolünü sağlar ve çoklu seçim yapmak dışında klavye tuşlarının kullanılmasını gerektirmez. {{CAD Navigation/tr}}


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

### OpenInventor Gezinme 

OpenInventor\'de (önceden Inventor) gezinme, [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) den sonra eklendi. (Bu mod Autodesk Inventor\'a dayalı değildir.) Fare tek başına yeterli değildir. Nesneleri seçmek için,**CTRL** tuşunu basılı tutmanız gerekir . {{Inventor Navigation/tr
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

### Blender Gezinme 

Blender Gezinme [Blender](http://www.blender.org)\'dan sonra eklendi. Daha önce tek başına fareyle taşıma yapılamıyordu,taşıma için**SHIFT** tuşu kullanılıyordu. 2016\'da bu özellik yenilendi. Hem fare sağ tuşu hem de fare sol tuşu birlikte basılı tutularak taşıma yapılabilir. {{Blender Navigation/tr}}

Alternatively, hold both left and right mouse buttons, and then move the pointer. \|Zoom\_text=Use the mouse wheel to zoom in and out. \|Rotate\_view\_text=Hold the middle mouse button, then move the pointer. }}

### Dokunmatik fare gezinme 

Dokunmatik fare gezinti de, Taşıma , zumlama ve döndürme işlemleri, yalnız fare kullanılarak (veya yalnız dokunmatik fare) yapılamaz. {{Touchepad Navigation/tr}}

### Gesture Gezinme (v0.16) 

Bu gezinme stili dokunmatik ekran ve kalemle kullanım için uyarlandı, ancak dokunmatik fare için de kullanılabilir. {{Gesture Navigation/tr}}

Alternatively, tap and hold, then drag. This simulates the pan with the right mouse button. \|Zoom\_text=Use the mouse wheel to zoom in and out. \|Zoom\_gesture\_text=Drag two fingers (pinch) closer or farther apart. \|Rotate\_view\_text=Hold the left mouse button, then move the pointer. In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

To set the camera\'s focus point for rotation, click a point with the middle mouse button. Alternatively, aim the cursor at a point and press **H** on the keyboard. \|Rotate\_view\_gesture\_text=Drag with one finger to rotate.

Hold **Alt** when in the [Sketcher](Sketcher_Workbench.md). \|Tilt\_view\_text=Hold both left and right mouse buttons, then move the pointer sideways. \|Tilt\_view\_gesture\_text=Rotate the imaginary line formed by two touch points.

On v0.18 this method is disabled by default. To enable, go to **Edit → Preferences → Display**, and untick \"Disable touchscreen tilt gesture\" checkbox. }}

### Maya-Gesture Gezinme 


<div class="mw-translate-fuzzy">

Maya-Gesture Gezinme,**ALT** tuşu ve bir fare düğmesine basarak tüm görünüm hareketleri etkinleştirilir , böylece bu gezinme modunu doğru kullanmak için 3 düğmeli bir fareye ihtiyaç duyulur. Alternatif olarak, bu mod, normal Gesture Gezinme modu üzerinde geliştirildiği için tüm Gestures hareketlerini kullanmak mümkündür. {{MayaGesture Navigation/tr}}


</div>

Alternatively, use the mouse wheel to zoom in and out. \|Rotate\_view\_text=Hold **Alt** and the left mouse button, then move the pointer. }}

### Revit Navigation 

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

## Nesneleri seçmek 

### Basit seçim 

Nesneler, 3D görünümdeki nesneyi tıklatarak veya ağaç görünümünde seçerek farenin sol tuşu ile tıklanarak seçilebilir.

### Ön Seçim 

Nesneleri vurgulayan ve seçimden önce fareyi nesnelerin üzerine getirerek bilgileri görüntüleyen bir \'Ön Seçim\' mekanizması da vardır. Bu davranışı sevmiyorsanız veya yavaş bir makineniz varsa, tercihlerde ön seçimi devre dışı bırakabilirsiniz.

## Nesne özelliklerini değiştirme 

FreeCAD, bir nesnenin görüntüsü, şekil veya diğer parametrelerini değiştirmek için kullanılabilecek [*manipulators*](Manipulator.md) sağlar.

## Donanım desteği 

FreeCAD, ayrıca bazı [ 3D giriş cihazlarını](3D_input_devices.md) destekler.

## Mac OS X Sorunları 

Son zamanlarda Mac kullanıcılarından [forum\'da](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0) bu fare tuş ve klavye tuş kombinasyonunun beklendiği gibi çalışmadığı bildirildi.Maalesef, geliştiricilerin hiçbiri Mac\'e sahip değil, diğer düzenli katkı yapanlar da yok. Hangi wiki düğmelerinin ve tuş kombinasyonunun işe yaradığını belirlemek için sizin yardımınıza ihtiyacımız var, böylece bu wiki\'yi güncelleyebiliriz.


{{docnav/tr|[Başlangıç](Getting_started/tr.md)|[Belge yapısı](Document_structure/tr.md)}}



