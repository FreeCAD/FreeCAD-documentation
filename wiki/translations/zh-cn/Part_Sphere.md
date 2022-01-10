---
- GuiCommand:
   Name:Part Sphere
   MenuLocation:Part → Primitives → Sphere
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Primitives](Part_Primitives.md)
---

# Part Sphere/zh-cn

## Description


<div class="mw-translate-fuzzy">

## 描述

利用位置、角度1、角度2、角度3与半径参数创建一个简单的参数化球体。


</div>

<img alt="" src=images/SimpleSphere.jpg  style="width:400px;">

## Usage


<div class="mw-translate-fuzzy">

## 如何使用

在[零件工作台中点击球体图标](Part_Workbench.md)<img alt="" src=images/Part_Sphere.png  style="width:32px;">。球体在创建时会被定位在原点(point 0,0,0)处。角度参数确定了所创的是局部球体，而非完整的球体（角度参数的默认设置值为360°）。


</div>

**Result:** The sphere will be positioned at origin (point 0,0,0) on creation. The angle parameters permit to make a portion of sphere instead of a full sphere (they are set to 360° by default).

The properties of the object can be edited, either in the [Property editor](Property_editor.md) or by double-clicking the object in the [Tree view](Tree_view.md).


<div class="mw-translate-fuzzy">

## 选项


</div>

### Data


{{TitleProperty|Sphere}}

-    **Radius:**Radius of the sphere

-    **Angle 1:**1nd angle to cut / define the sphere

-    **Angle 2:**2nd angle to cut / define the sphere

-    **Angle 3:**3rd angle to cut / define the sphere

由于很难描述angle 1、angle 2、angle 3这三个参数的意义，因此以下列图示来向您展示关于angle 1 = -45°, angle 2 = 45° 与 angle 3 = 90°时的效果，从而对此进行解释。

<img alt="" src=images/SphereCutThreeAngles.jpg  style="width:400px;">

## Scripting

A Part Sphere can be created using the following function:


```python
sphere = FreeCAD.ActiveDocument.addObject("Part::Sphere", "mySphere")
```

-   Where {{Incode|"mySphere"}} is the name for the object.
-   The function returns the newly created object.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sphere/zh-cn
