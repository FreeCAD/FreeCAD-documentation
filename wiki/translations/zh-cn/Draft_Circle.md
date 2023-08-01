---
- GuiCommand:
   Name:Draft Circle
   MenuLocation:Drafting → Circle
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**C** **I**
   Version:0.7
   SeeAlso:[Draft Arc](Draft_Arc.md), [Draft Arc 3Points](Draft_Arc_3Points.md)
---

# Draft Circle/zh-cn

## Description


<div class="mw-translate-fuzzy">

## 描述

底图圆形工具通过用户输入的两个点（中心点与半径），或通过拾取切线，或上述若干组合来在当前的[工作平面上创建一个圆形](Draft_SelectPlane.md)。它将根据[Draft Tray中的](Draft_Tray.md)[Draft Linestyle来创建圆形](Draft_Linestyle.md)。


</div>


<div class="mw-translate-fuzzy">

此工具与[Draft Arc工具的工作方式很相似](Draft_Arc.md)，区别在于前者创建的是一个完整的圆周。要绘制椭圆形请使用[Draft Ellipse工具](Draft_Ellipse.md)。


</div>

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*两点定一圆*


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## 如何使用

1.  点击**<img src="images/Draft_Circle.png" width=16px> [Draft Circle](Draft_Circle.md)**按钮，或先后按下**C**、**I**键。
2.  在3D视图中单击第一个点，或输入一个coordinate并按下**<img src="images/Draft_AddPoint.svg" width=16px> add point**按钮。
3.  在3D视图中单击第二个点，或输入一个半径值。


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## 选项

-   此工具绘制圆形的主要用法就是拾取两点，即圆形的中心点及其圆周上一点。
    -   通过按下**Alt**键，您就可以选取一条切线而非拾取一个点。You can therefore construct several types of circles by selecting one, two or three tangents.
-   为了手动输入坐标，您可以在输入X、Y或Z坐标值后，通过按下**Enter**键切换至下一个坐标分量。您可以在输入点的坐标值后按**<img src="images/Draft_AddPoint.svg" width=16px> add point**按钮来插入目标点。
-   按**T**键或单击continue多选框即可切换至*连续*模式。如果开启了连续模式，则圆形工具将在绘制完一个圆形后再次开启，并令您在不用按下圆形工具这一按钮的情况下，继续绘制下一个圆形。
-   按**L**键或单击filled复选框即可切换至*填充*模式。若开启填充模式，此工具创建的将是一个圆形的面(**Make Face** `True`)；否则创建的仅是一个圆形而非圆面(**Make Face** `False`)。
-   若希望将点强制绘至[捕捉到的最近位置](Draft_Snap.md)，请按住**Ctrl**键。
-   若希望令绘制的第二个点位于第一个的水平或垂直方向，请按住**Shift**键。
-   按**Esc**键或**Close**按钮来终止当前命令。


</div>

## Notes


<div class="mw-translate-fuzzy">

通过双击树状视图（tree view）中的元素或点击**<img src="images/Draft_Edit.svg" width=16px> [[Draft Edit]]**按钮即可编辑对应圆形。届时，您就可将中心点与半径点移动到预定的新位置。


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Circle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### 数据

-    **First Angle**: 指定圆形的起始角度；此值通常为0°.

-    **Last Angle**: 指定圆形的结束角度；此值通常为0°。

-    **Radius**: 指定圆形的半径。

-    **Make Face**: 指定此工具绘制的是圆面还是圆形。如果值为`True`则创建一个面，否则仅是创建一个圆周。只有绘制完整的圆形时，本属性才会生效。

:   对于完整的圆形而言，**First Angle** 与**Last Angle**应当有着相同的值；否则，显示的将是一个[弧线](Draft_Arc.md)。0°与 360°并非相同的值，因此若采用这两个值，则绘制的圆无法构成一个面。


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### 视图

-    **Pattern**: 指定[底图图案](Draft_Pattern.md)，用它来填充圆面。只有当**Make Face**为`True`且**Display Mode**为\"Flat Lines\"时本属性才能生效。

-    **Pattern Size**: 指定[底图图案的大小](Draft_Pattern.md)。


</div>

## Scripting


<div class="mw-translate-fuzzy">

## 脚本


**参见:**

[Draft API](Draft_API.md) 与 [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md)。


</div>


<div class="mw-translate-fuzzy">

通过下列函数就可以在[macros与](macros.md)[Python控制台中使用圆形工具](Python.md)：


</div>


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```


<div class="mw-translate-fuzzy">

-   利用指定的以毫米为单位的`radius`来创建一个`Circle`对象。
    -   可用`Part.Edge`来代替`radius`，但是其`Curve`属性必为`Part.Circle`.
-   如果给出了`placement`便采用此值为中心点；否则此圆形中心点位于原点。
-   如果`face`为`True`，则把圆形构造为一个面，即将它填充为实心圆片。
-   如果将`startangle`与`endangle`设置为不同的度数，便会启用此二参数，且目标对象表现为一个[Draft Arc](Draft_Arc.md)。


</div>

示例： 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Circle/zh-cn
