---
- GuiCommand:/zh-cn
   Name:Draft Arc
   Name/zh-cn:Draft Arc
   MenuLocation:Draft → Arc
   Workbenches:[Draft](Draft_Workbench/zh-cn.md), [Arch](Arch_Workbench/zh-cn.md)
   Shortcut:**A** **R**
   SeeAlso:[Draft Circle](Draft_Circle/zh-cn.md), [Draft Ellipse](Draft_Ellipse/zh-cn.md)
   Version:0.7
---


</div>

## 描述


<div class="mw-translate-fuzzy">

底图绘弧工具通过用户输入的4个点（圆的中心点、半径、第一个点与最后一个点），或通过拾取切线，或上述若干组合来在当前的[work plane上创建一个圆弧](Draft_SelectPlane/zh-cn.md)。它将根据[Draft Tray中的](Draft_Tray/zh-cn.md)[Draft Linestyle来创建圆弧](Draft_Linestyle/zh-cn.md)。


</div>

A Draft Arc is in fact a [Draft Circle](Draft_Circle.md) with a **First Angle** that is not the same as its **Last Angle**.

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


*通过中心点、半径、弧的初始点、弧的结束点这4点所定义的圆弧*


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## 如何使用

1.  按下**<img src="images/Draft_Arc.png" width=16px> [Draft Arc](Draft_Arc/zh-cn.md)**按钮，或先按**A**键再按**R**键。
2.  在3D视图中点击第一个点，或输入一个 [坐标并按](Draft_Coordinates/zh-cn.md)**<img src="images/Draft_AddPoint.svg" width=16px> [add point](Draft_AddPoin/zh-cnt.md)**按钮。
3.  在3D视图中点击第二个点，或输入一个半径值。
4.  在3D视图中点击第三个点，或输入一个起始角度。
5.  在3D视图中点击第四个点，或输入一个张角。


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## 选项

-   绘弧工具的主要用法就是通过拾取四个点：中点、一个圆周上的点，弧的起始及其终点。
    -   通过按**Alt**键，您能以一条切线而非拾取的点来定义弧所基于的圆。就此，您可以通过选择的一个、两个或三个切线来构建若干种不同的圆。
-   弧的方向取决于鼠标的移动操作。如果您在输入第三个点后，沿着顺时针移动鼠标，则所创的弧为顺时针。为了令其为逆时针方向，可令鼠标简单地向第三个点的另一侧移动，直到弧以另一个方向开始绘制。
-   为了手动输入坐标，可在简单地输入每一个X、Y、Z分量后，再按**Enter**键。当您需要在特定位置处插入点时，可以按**<img src="images/Draft_AddPoint.svg" width=16px> [add point](Draft_AddPoint.md)**按钮。
-   按**T**或点击*continue*多选框切换至连续模式。如果您开启了连续模式，则绘制完一条弧后，将立即重新开始绘制下一条弧，这可使您在绘制另一条弧时，无需再次按绘制弧工具按钮。
-   按住**Ctrl**可将您正在绘制的点强制[捕捉至最近的捕捉位置上](Draft_Snap.md)，这与距离无关。
-   按住**Shift**可将您正在绘制的点[约束在相对于中点的水平方向或垂直方向](Draft_Constrain.md)。
-   按**Esc**或**Close**按钮来终止当前命令。


</div>

## Notes


<div class="mw-translate-fuzzy">

通过双击树状视图（tree view）中的元素或点击**<img src="images/Draft_Edit.svg" width=16px> [Draft Edit](Draft_Edit/zh-cn.md)**按钮即可编辑对应弧。届时，您就可将中心点移动到预定的新位置。


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, radii and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties


<div class="mw-translate-fuzzy">

## 属性

弧对象享有[Draft Circle中的所有属性](Draft_Circle/zh-cn.md)，但是有些属性仅对圆形而言才有意义。


</div>

## Scripting


<div class="mw-translate-fuzzy">

## 脚本


**参见:**

[Draft API](Draft_API/zh-cn.md) 与 [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/zh-cn.md)。


</div>


<div class="mw-translate-fuzzy">

在[宏中与](macros.md)[Python控制台中可使用弧形工具](Python/zh-cn.md)，方法是使用绘制圆的函数，再辅以额外的参数。 参见[底图圆形工具中的有关信息](Draft_Circle/zh-cn.md)。


</div>

示例：


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

arc1 = Draft.make_circle(200, startangle=0, endangle=90)
arc2 = Draft.make_circle(500, startangle=20, endangle=160)
arc3 = Draft.make_circle(750, startangle=-30, endangle=-150)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
