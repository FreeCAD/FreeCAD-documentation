# Mouse navigation/zh
{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

Freecad的鼠标控制模式由用于三维空间可视化导航和与显示对象交互的命令组成.Freecad支持多个鼠标控制导航样模式。默认的导航样式被称为“CAD导航”，非常简单和实用，但FreeCad还提供了多种可选的导航样式，您可以根据自己的喜好进行选择。


</div>

For more information about selecting objects see [Selection methods](Selection_methods.md).

For more information about manipulating objects see [Std TransformManip](Std_TransformManip.md).

## Selecting a navigation style 


<div class="mw-translate-fuzzy">

-   在[首选项编辑器中](Preferences_Editor.md)，选择的 **编辑 → 首选项 → 显示 → 3D视图 → 3D导航**

在三维视图区域的空白处单击鼠标右键，然后在弹出菜单中选择**导航样式 →...**"。


</div>

## Available navigation styles 


<div class="mw-translate-fuzzy">

### Blender导航


</div>

The Blender navigation style was modeled after [Blender](https   *//www.blender.org).


<div class="mw-translate-fuzzy">

Blender导航样式参照[Blender](http   *//www.blender.org)的操作。以前一直需要按下**SHIFT**配合鼠标才能完成视图平移. 在2016年Blender增加了一个功能改变了这一情况。现在可以通过同时按下鼠标左键和右键进行视图平移。 {{Blender Navigation
|Select_name=选取
|Pan_name=平移
|Zoom_name=缩放
|Rotate_view_name=旋转视图
|Shift=**Shift**
|Select_text=在要选择的对象上按鼠标左键。
|Pan_text=按住**Shift** 并按住鼠标中键，然后移动鼠标。
</div>

或者，按住鼠标左键和右键，然后移动鼠标。 
|Zoom_text=使用鼠标滚轮放大和缩小。 
|Rotate_view_text=按住鼠标中键，然后移动鼠标。
}}

### CAD navigation 


<div class="mw-translate-fuzzy">

### CAD导航(默认)

这是默认的导航样式，其允许用户对视图进行简单的控制，并且不需要使用键盘键，除非进行多个选择。


</div>


{{CAD Navigation
|Select_name=选择
|Pan_name=平移
|Zoom_name=缩放
|Rotate_view_name=旋转视图<br>第一种方法
|Rotate_view_alt_name=旋转视图<br>替代方法
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=在要选择的对象上按鼠标左键。按住**Ctrl**可以选择多个对象。

<div class="mw-translate-fuzzy">
按住**Ctrl**可以选择多个对象。
|Pan_text=按住鼠标中键，然后移动鼠标。
|Pan_mode_text=平移模式：按住**Ctrl**键，按下鼠标右键一次，然后移动鼠标。
|Zoom_text=使用鼠标滚轮放大和缩小。单击鼠标中键可将视图重新置于光标位置的中心。 <small>(v0.17)</small> 
</div>

<div class="mw-translate-fuzzy">
单击鼠标中键可将视图重新置于光标位置的中心。 
|Zoom_mode_text=Zoom mode   * 按住键盘上的**Ctrl** 和**Shift**键不放, 点击鼠标右键一次后移动光标. <small>(v0.17)</small> 
|Rotate_view_text=按住鼠标中键不放, 然后按下鼠标左键不放, 然后移动光标.
</div>

<div class="mw-translate-fuzzy">
鼠标中键按下时光标的位置决定了旋转操作的旋转中心。旋转操作就像旋转一个围绕中心旋转的球。如果在停止鼠标移动之前释放按钮，视图将继续[旋转](spinning.md)(此选项启用时)。
</div>

<div class="mw-translate-fuzzy">
双击鼠标中键以设定一个新的旋转中心。
|Rotate_view_mode_text=Rotate mode   * 按住**Shift**键不放,点击鼠标右键一次后移动光标.  <small>(v0.17)</small> 
|Rotate_view_alt_text=按住鼠标中键不放, 然后按下鼠标右键不放, 然后移动光标.
</div>

该方法下鼠标中键可以在鼠标右键按下后放开。

习惯用右手的用户可能会觉得这种方法比第一种方法要容易些。}}


<div class="mw-translate-fuzzy">

### 手势导航


</div>

This style was tailored for use with a touchscreen and pen. Nevertheless, it can also be used with a mouse, and is recommended for use when using a Mac with a trackpad.


<div class="mw-translate-fuzzy">

这种导航风格是0.16版引入的为触摸屏和笔的可用性而量身定做的，但也可以配合鼠标使用。 {{Gesture Navigation
|Select_name=选择
|Pan_name=平移
|Zoom_name=缩放
|Rotate_view_name=旋转视图
|Tilt_view_name=倾斜视图
|Select_text=在要选择的对象上按鼠标左键。
|Select_gesture_text=点击选择。
|Pan_text=按住鼠标右键，然后移动鼠标。
|Pan_gesture_text=用两个手指拖拽。
</div>

或者，轻按并按住，然后拖动。这将使用鼠标右键模拟平移。
|Zoom_text=使用鼠标滚轮缩放。
|Zoom_gesture_text=将两个手指（捏）拉近或拉远。
|Rotate_view_text=按住鼠标左键，然后移动鼠标。
在[草图工作台](Sketcher_Workbench.md)和其他编辑模式下，此行为被禁用。按下鼠标按钮进入旋转模式的同时时按住键**Alt**。

要设置相机的旋转对焦点，请用鼠标中键单击一个点。 或者，将光标对准某个点，然后按键盘上的**H**。
|Rotate_view_gesture_text =用一根手指拖动以旋转。

在[草图工作台](Sketcher_Workbench.md)中按下**Alt** 。
|Tilt_view_text=按住鼠标左键和右键，然后将鼠标移到一边。 
|Tilt_view_gesture_text=旋转由两个触摸点组成的假想线。

在v0.18上，默认情况下禁用此方法。要启用，请转到**编辑→首选项→显示**，然后取消选中“禁用触摸屏倾斜手势”复选框。}}


<div class="mw-translate-fuzzy">

### Maya手势导航


</div>

In Maya-Gesture Navigation, panning, zooming, and rotating the view require the **Alt** key together with a mouse button; therefore, a three-button mouse is required. It\'s also possible to use gestures as this style was developed over the [Gesture navigation](#Gesture_navigation.md) style.


<div class="mw-translate-fuzzy">

在maya手势导航中，所有视图移动都是**ALT** 和鼠标按钮激活的，因此需要有一个3按钮鼠标才能正确使用此导航模式。另外，也可以使用手势，因为该模式是在常规手势导航模式基础上下开发的。 {{MayaGesture Navigation
|Select_name=选取
|Pan_name=平移
|Zoom_name=缩放
|Rotate_view_name=旋转视图
|Alt=**Alt**
|Select_text=在要选择的对象上按鼠标左键。
|Pan_text=按住 **Alt**并按住鼠标中键，然后移动鼠标。
|Zoom_text=按住**Alt** 并单击鼠标右键，然后移动鼠标。
</div>

或者，使用鼠标滚轮放大和缩小。 
|Rotate_view_text=按住**Alt**和鼠标左键，然后移动鼠标。 
}}


<div class="mw-translate-fuzzy">

### OpenCascade


</div>

The OpenCascade navigation style was modeled after [OpenCascade](https   *//www.opencascade.com/).


{{OpenCascade Navigation
|Select_name=选择
|Pan_name=平移
|Zoom_name=缩放
|Rotate_view_name=旋转视图
|Ctrl=**ctrl**
|Select_text=在要选择的对象上按鼠标左键。
|Pan_text=按住鼠标中键，然后移动鼠标。
|Zoom_text=使用鼠标滚轮放大和缩小。

或者，按住**Ctrl**和鼠标左键，然后移动指针。
|Rotate_view_text =按住**Ctrl**和鼠标右键，然后移动指针。
}}

### OpenInventor navigation 


<div class="mw-translate-fuzzy">

### openinventor导航

在Openinventor导航中，参照[Open Inventor](http   *//en.wikipedia.org/wiki/Open_Inventor)(不要与Autodesk的inventor混淆)的操作，不能仅靠鼠标进行选取操作。要选择对象，必须按住**Ctrl**键。


</div>


<div class="mw-translate-fuzzy">

该模式不基于Autodesk Inventor


</div>


<div class="mw-translate-fuzzy">


{{OpenInventor Navigation
|Select_name=选择
|Pan_name=平移
|Zoom_name=缩放
|Rotate_view_name=旋转视图
|Ctrl=**ctrl**
|Select_text=按住**ctrl**，然后在要选择的对象上按鼠标左键。
|Pan_text=按住鼠标中键，然后移动鼠标。
|Zoom_text=使用鼠标滚轮放大和缩小。
</div>

Hold down **Ctrl** instead to select multiple objects.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.

或者，按住鼠标中键，然后按住鼠标左键，然后移动指针。
|Rotate_view_text =按住鼠标左键，然后移动指针。
}}

### OpenSCAD navigation 

The OpenSCAD navigation style was modeled after [OpenSCAD](https   *//openscad.org/).


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

### Revit导航


</div>

The Revit navigation style was modeled after [Revit](https   *//en.wikipedia.org/wiki/Autodesk_Revit).

{{Revit Navigation \|Select_name =选择 \|Pan_name = Pan \|Zoom_name =缩放 \|Rotate_view_name =旋转视图 \|Shift = {**Shift**
|Select_text =在要选择的对象上按下鼠标左键。
|Pan_text =按住鼠标中键，然后移动指针。

或者，按住鼠标左键和右键，然后移动指针。

|Zoom_text =使用鼠标滚轮放大和缩小。
|Rotate_view_text =按住**Shift**和鼠标中键，然后移动指针。

或者，按住鼠标中键，然后按住鼠标右键，然后移动指针。
}}

=== TinkerCAD navigation ===

The TinkerCAD navigation style was modeled after [https   *//en.wikipedia.org/wiki/Tinkercad TinkerCAD].

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
===触控板导航===
</div>

In Touchpad Navigation, panning, zooming, and rotating the view require a modifier key together with the touchpad.

<div class="mw-translate-fuzzy">
触控板导航中,平移、缩放或视图旋转操作都需要一个辅助按键和触控板一起配合。
{{Touchpad Navigation
|Select_name=选取
|Pan_name=平移
|Zoom_name=缩放
|Rotate_view_name=旋转视图
|Shift=**Shift**
|Ctrl=**Ctrl**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=在要选择的对象上按鼠标左键。
|Pan_text=按住 **Shift**,然后移动鼠标.
|Zoom_text=使用 **PageUp**和**PageDown**进行缩放操作.
|Zoom_alt_text=或者按住**Shift**和**Ctrl**, 然后移动鼠标.
|Rotate_view_text=按住**Alt**,然后移动鼠标.
|Rotate_view_alt_text=或者，按住**Shift**和左键，然后移动鼠标。
}}
</div>

==硬件支持==

<div class="mw-translate-fuzzy">
FreeCAD 也支持一些[3D输入设备](3D_input_devices.md).
</div>

<div class="mw-translate-fuzzy">
== Mac OS X问题==
</div>

<div class="mw-translate-fuzzy">
最近我们[http   *//forum.freecadweb.org/viewtopic.php？f=3&t=3592&start=0 在论坛中]收到了来自Mac用户的报告称这些鼠标按钮和按键组合不能正常工作。不幸的是，没有一个开发人员拥有Mac，其他的常规志愿者也没有。我们需要您的帮助来确定哪些鼠标按钮和组合键有效，以便我们可以更新此wiki。
</div>

== Developing a custom navigation == 

The tutorial [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) orients developers who want to develop a custom mouse navigation option. Familiarity with the C++ syntax is required.


{{docnav
|[入门](Getting_started/zh.md)
|[导航立方体](Navigation_Cube/zh.md)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Mouse navigation/zh
