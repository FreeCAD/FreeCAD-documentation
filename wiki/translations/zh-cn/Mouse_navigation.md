# Mouse navigation/zh-cn
## Overview


<div class="mw-translate-fuzzy">

FreeCAD的 *\'鼠标模式* 由用于在3D空间视觉导航并与显示对象进行交互的命令组成。 FreeCAD支持多种鼠标型号导航。默认的导航风格被称为"CAD导航"，并且非常简单实用，但FreeCAD还提供了替代的导航样式，您可以根据自己的喜好进行选择。


</div>

For more information about selecting objects see [Selection methods](Selection_methods.md).

For more information about manipulating objects see [Std TransformManip](Std_TransformManip.md).

## Selecting a navigation style 


<div class="mw-translate-fuzzy">

-   在[首选项编辑器](Preferences_Editor/zh-cn.md)，显示部分，"3D视图"选项卡;
-   通过在3D视图区域的空白处右键单击，然后在上下文菜单中选择"导航样式"。


</div>

## Available navigation styles 

With all navigation styles, unless selecting objects from a sketch in edit mode, you must hold **Ctrl** to select multiple objects.




<div class="mw-translate-fuzzy">

### Blender 导航 


</div>

The Blender navigation style was modeled after [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">

在 Blender 导航中，以[Blender](http://www.blender.org)为模型，没有单独的鼠标平移方式。为了平移视图，您必须按住{{KEY | SHIFT}}键。2016年发生了改变，现在，您可以同时按住鼠标左右两键来移动视图。 {{Blender Navigation
|Select_name=选择对象
|Pan_name=移动视图
|Zoom_name=缩放视图
|Rotate_view_name=旋转视图
|Shift=**Shift**
|Select_text=在待选对象上点击鼠标左键。
|Pan_text=按住**Shift**键与鼠标中键，再移动鼠标指针。
</div>

或者按住鼠标左右两键，再移动鼠标指针。
|Zoom_text=用鼠标滚轮来进行缩放。
|Rotate_view_text=按住鼠标中键，再移动鼠标指针。
}}

### CAD navigation 


<div class="mw-translate-fuzzy">

### CAD导航（默认）

这是默认的导航样式，允许用户简单地控制视图，除了进行多选，不需要使用键盘键。


</div>


<div class="mw-translate-fuzzy">


{{CAD Navigation
|Select_name=选择对象
|Pan_name=移动视图
|Zoom_name=缩放视图
|Rotate_view_name=旋转视图<br>第一种方法
|Rotate_view_alt_name=旋转视图<br>另一种方法
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=在待选对象上点击鼠标左键。
</div>

<div class="mw-translate-fuzzy">
单击鼠标中键，以光标在视图中的位置进行重新定位(re-center)。
|Zoom_mode_text=缩放视图模式: 按住**Ctrl**与**Shift**键, 并按下鼠标右键一次, 再移动鼠标指针。<small>(v0.17)</small> 
|Rotate_view_text=按住鼠标中键，再按住鼠标左键，并移动鼠标指针。
</div>

<div class="mw-translate-fuzzy">
在按下鼠标中键时，指针所在位置确定了旋转中心。旋转操作如同令一个球绕其中心旋转。倘若开启了[[spinning]]，那么，如果在鼠标停止移动之前松开了按键，则视图会继续旋转。
</div>

<div class="mw-translate-fuzzy">
双击鼠标中键将设置一个新的旋转中心。
|Rotate_view_mode_text=旋转视图模式: 按住**Shift**键，按下鼠标右键一次，再移动鼠标指针。<small>(v0.17)</small> 
|Rotate_view_alt_text=按住鼠标中键，再按住鼠标右键，并移动鼠标指针。
</div>

若采用这种方法，则放开中键不放右键依然可以进行视图旋转。

若用户惯用右手，便会发现此法较第一种方法更易使用。
}}




<div class="mw-translate-fuzzy">

### 手势导航（v0.16）


</div>

This style was tailored for use with a touchscreen and pen. Nevertheless, it can also be used with a mouse, and is recommended for use when using a Mac with a trackpad.


<div class="mw-translate-fuzzy">

这种导航风格是针对触摸屏和笔的可用性量身定制的，但也可以与鼠标一起使用。 {{Gesture Navigation
|Select_name=选择对象
|Pan_name=移动视图
|Zoom_name=缩放视图
|Rotate_view_name=旋转视图
|Tilt_view_name=倾斜视图
|Select_text=在待选对象上点击鼠标左键。
|Select_gesture_text=通过点击来选择对象。
|Pan_text=按住鼠标右键，再移动鼠标指针。
|Pan_gesture_text=用二指拖动视图。
</div>

或者点击并按住，再进行拖拽。这模拟的是用鼠标右键来移动视图。
|Zoom_text=用鼠标滚轮来进行缩放。
|Zoom_gesture_text=二指合拢或张开拖动来进行缩放。
|Rotate_view_text=按住鼠标左键，再移动鼠标指针。
在[Sketcher](Sketcher_Workbench.md)和其他编辑模式下，禁用此动作：按住**Alt**键并按下鼠标左键进入旋转模式。

为了设置用于旋转的摄像机焦点，在预定点单击鼠标中键。或者令光标对准预定点，并按下键盘上的**H**键。
|Rotate_view_gesture_text=单指拖动进行旋转。

在[Sketcher](Sketcher_Workbench.md)中时，按住**Alt**键。
|Tilt_view_text=按住鼠标左右两键，再向一侧移动鼠标指针。
|Tilt_view_gesture_text=旋转两指间的假想线段。

<div class="mw-translate-fuzzy">
在v0.18版中，此方法默认禁用。若要开启，请依次选择**Edit → Preferences → Display**，并反选"Disable touchscreen tilt gesture" 复选框。
}}


</div>




<div class="mw-translate-fuzzy">

### Maya 手势导航 


</div>

In Maya-Gesture Navigation, panning, zooming, and rotating the view require the **Alt** key together with a mouse button; therefore, a three-button mouse is required. It\'s also possible to use gestures as this style was developed over the [Gesture navigation](#Gesture_navigation.md) style.


<div class="mw-translate-fuzzy">

在Maya手势导航中，按{{KEY | ALT}}和鼠标按钮激活所有视图动作，以便为了正确使用此导航模式，需要一个3按钮鼠标。或者，可以使用手势，因为这种模式是通过正常的手势导航模式开发的。 {{MayaGesture Navigation
|Select_name=选择对象
|Pan_name=移动视图
|Zoom_name=缩放视图
|Rotate_view_name=旋转视图
|Alt=**Alt**
|Select_text=在待选对象上点击鼠标左键。
|Pan_text=按住**Alt**与鼠标中键，再移动鼠标指针。
|Zoom_text=按下**Alt**与鼠标右键，再移动鼠标指针。
</div>

或者用鼠标滚轮来进行缩放。
|Rotate_view_text=按住**Alt**与鼠标左键，再移动鼠标指针。
}}

### OpenCascade navigation 

The OpenCascade navigation style was modeled after [OpenCascade](https://www.opencascade.com/).


{{OpenCascade Navigation
|Select_name=选择对象
|Pan_name=移动视图
|Zoom_name=缩放视图
|Rotate_view_name=旋转视图
|Ctrl=**Ctrl**
|Select_text=在待选对象上点击鼠标左键。
|Pan_text=按住鼠标中键，再移动鼠标指针。
|Zoom_text=用鼠标滚轮来进行缩放。

或者按住**Ctrl**与鼠标左键，再移动鼠标指针。
|Rotate_view_text=按住**Ctrl**与鼠标右键，再移动鼠标指针。
}}

### OpenInventor navigation 


<div class="mw-translate-fuzzy">

### Inventor 导航 

在[Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor)（不要与Autodesk Inventor混淆）建模后的 Inventor 导航中，没有鼠标选择。为了选择对象，您必须按住{{KEY | CTRL}}键。


</div>


<div class="mw-translate-fuzzy">

此模式并非基于Autodesk Inventor。


</div>


<div class="mw-translate-fuzzy">


{{OpenInventor Navigation
|Select_name=选择对象
|Pan_name=移动视图
|Zoom_name=缩放视图
|Rotate_view_name=旋转视图
|Ctrl=**Ctrl**
|Select_text=按住**Ctrl**，在待选对象上点击鼠标左键。
|Pan_text=按住鼠标中键，并移动鼠标指针。
|Zoom_text=用鼠标滚轮来进行缩放。
</div>

Hold **Ctrl** instead to select multiple objects.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.

或者按住鼠标中键，再按下鼠标左键，最后移动鼠标指针。
|Rotate_view_text=按住鼠标左键，再移动鼠标指针。
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

Hold **Ctrl** and **Shift** when pressing the mouse button to drag an object in a sketch in edit mode.
|Pan_text=Hold the right mouse button, then move the pointer.
|Zoom_text=Hold the middle mouse button, then move the pointer.
Alternatively, hold **Shift** and the right mouse button, then move the pointer.
|Rotate_view_text=Hold the left mouse button, then move the pointer.
}}




<div class="mw-translate-fuzzy">

### Revit 导航 


</div>

The Revit navigation style was modeled after [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit).


{{Revit Navigation
|Select_name=选择对象
|Pan_name=移动视图
|Zoom_name=缩放视图
|Rotate_view_name=旋转视图
|Shift=**Shift**
|Select_text=在待选对象上点击鼠标左键
|Pan_text=按住鼠标中间，再移动鼠标指针。

或者按下鼠标左右两键，再移动鼠标指针。

|Zoom_text=用鼠标滚轮来进行缩放。
|Rotate_view_text=按住**Shift**与鼠标中键，再移动鼠标指针。

或者按住鼠标中键，再按住鼠标右键，最后移动指针。
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

### 触摸板导航


</div>

With the Touchpad navigation style, panning, zooming, and rotating the view require a modifier key together with the touchpad. This style can also be used with a mouse.


<div class="mw-translate-fuzzy">

在触摸板导航中，既不是平移，也不是缩放，也不是旋转视图，仅限于鼠标（或仅限触摸板）操作。 {{Touchpad Navigation
|Select_name=选择对象
|Pan_name=移动视图
|Zoom_name=缩放视图
|Rotate_view_name=旋转视图
|Shift=**Shift**
|Ctrl=**Ctrl**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=在待选对象上点击鼠标左键。
|Pan_text=按住**Shift**键，再移动指针。
|Zoom_text=用**PageUp**与**PageDown**键来进行缩放。
|Zoom_alt_text=或者按住**Shift**与**Ctrl**键，再移动指针。
|Rotate_view_text=按住**Alt**键，再移动指针。
|Rotate_view_alt_text=或者按住**Shift**与鼠标左键，再移动指针。
}}


</div>



## 硬件支持


<div class="mw-translate-fuzzy">

FreeCAD 同样支持一些 [3D 输入设备](3D_input_devices/zh-cn.md).


</div>




<div class="mw-translate-fuzzy">

## Mac OS X 问题 


</div>


<div class="mw-translate-fuzzy">

最近我们从[论坛](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0)的Mac用户那里得到报告，那些鼠标按键和按键组合不能像预期的那样工作。不幸的是，没有一个开发者拥有Mac，也不是其他的常规贡献者。我们需要您的帮助来确定哪些鼠标按键和按键组合起作用，以便我们可以更新此维基。


</div>

## Developing a custom navigation 

The tutorial [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) orients developers who want to develop a custom mouse navigation option. Familiarity with the C++ syntax is required.


{{docnav|Getting started/zh-cn|Document structure/zh-cn}}



---
⏵ [documentation index](../README.md) > Mouse navigation/zh-cn
