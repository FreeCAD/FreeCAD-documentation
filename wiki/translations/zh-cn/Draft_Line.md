---
- GuiCommand:
   Name:Draft Line
   MenuLocation:Draft → Line
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:L I
   SeeAlso:[Draft Wire](Draft_Wire.md), [[Draft Point]]
   Version:0.7
---

# Draft Line/zh-cn


</div>

## Description


<div class="mw-translate-fuzzy">

## 描述

线段工具用于创建两点定义的线段。它根据[Draft Tray中](Draft_Tray.md)[Draft Linestyle的设置来绘制线段](Draft_Linestyle.md)。此工具与[Draft Wire工具的行为基本相同](Draft_Wire.md)，唯独线段工具在绘制完一条两点的线段即停止工作。


</div>

A Draft Line is in fact a [Draft Wire](Draft_Wire.md) with only two points.

<img alt="" src=images/Draft_Line_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*根据两点创建一条线段*


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## 如何使用

1.  按下**<img src="images/Draft_Line.svg" width=16px> [[Draft Line]]**按钮, 或先按**L**再按**I**键。
2.  在3D视图中单击第一个点，或输入坐标并按下**<img src="images/Draft_AddPoint.svg" width=16px> add point**按钮。
3.  在3D视图中单击第二个点，或输入坐标并按下**<img src="images/Draft_AddPoint.svg" width=16px> add point**键。


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## 选项

-   设置好第一个点后，按**X**、**Y**或**Z**键来约束第二点的对应坐标。
-   为了手动输入坐标值，可以在每次输入X、Y与Z分量后按**Enter**键。
    -   您也通过指定\"Length（长度）\"与\"Angle（角度）\"的值来定义点的极坐标。点击\"Angle\"边上的复选框来约束线段所指向的角度。您还可以点击**<img src="images/Draft_AddPoint.svg" width=16px> add point**按钮来插入点。
-   按**R**键或点击relative复选框切换至*相对坐标*模式。如果开启了相对坐标模式，则第二个点的坐标将相对于第一个点而定（即以第一个点为基准）；否则两点采用绝对坐标定义，即基于原点(0,0,0)而定。
-   按**T**键或点击continue复选框切换至*连续*模式。如果开启了连续模式，则在指定某线段第二个端点后，线段绘制工具将自动重启并继续下条线段的绘制，而不必再次按线段工具按钮。
-   在将端点强制绘至最近[捕捉位置时](Draft_Snap.md)，按住**Ctrl**。
-   在绘制第二端点时，按住**Shift**键来[约束（constrain）它的位置位于第一个点的水平方向或垂直方向](Draft_Constrain.md)。
-   按**Ctrl**+**Z**键或点击{{button|<img src="images/Draft_UndoLine.png" width=12px> Undo}}按钮来撤销最近绘制的线段。
-   按**Esc**键或点击**Close**按钮来终止当前命令。


</div>

## Notes


<div class="mw-translate-fuzzy">

通过双击树状视图（tree view）中的元素或点击**<img src="images/Draft_Edit.svg" width=16px> [[Draft Edit]]**按钮即可编辑对应线段。届时，您就可将构成线段的点移动到预定的新位置。


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, lengths and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial focus of the task panel to the **Length** input box: **Edit → Preferences... → Draft → General settings → Draft tools options → Set focus on Length instead of X coordinate**. Note that you must move the pointer in the [3D view](3D_view.md) for the change to take effect.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Line](Part_Line.md) instead of a Draft Line.

## Properties


<div class="mw-translate-fuzzy">

## 属性

线段对象享有[Draft Wire的所有属性](Draft_Wire.md)，但是其中仅有部分属性适用于线段。


</div>

## Scripting


<div class="mw-translate-fuzzy">

## 脚本


**参见:**

[Draft API](Draft_API.md) 与 [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md)。


</div>


<div class="mw-translate-fuzzy">

借助下列函数即可在[宏与](macros.md)[Python控制台中使用线段绘制工具](Python.md)：


</div>


```python
line = make_line(p1, p2)
line = make_line(LineSegment)
line = make_line(Shape)
```

-   创建点`p1`与点`p2`间的一条 `Line`对象，每个点由其`FreeCAD.Vector`来定义，且以毫米为单位。
-   根据`Part.LineSegment`来创建一条`Line`对象。
-   从指定`Shape`的第一个顶点至最后一个顶点创建一条`Line`对象。

示例：


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 500, 0)
p3 = App.Vector(-250, -500, 0)
p4 = App.Vector(500, 1000, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p3, p4)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Line/zh-cn
