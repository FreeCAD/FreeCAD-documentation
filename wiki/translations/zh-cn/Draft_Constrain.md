





{{TOCright}}

## Description


<div class="mw-translate-fuzzy">

## 描述

在[底图工作台工具中](Draft_Workbench/zh-cn.md)，您可以通过指针单击3D视图来拾取图形中的点、距离、半径与角度。


</div>

Constraining is available with most [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md) commands.

![](images/Draft_Constrain_taskpanel_example.png ) *While the cursor is constrained the task panel locks the values that are not being modified*


<div class="mw-translate-fuzzy">

## 水平约束与垂直约束


</div>


<div class="mw-translate-fuzzy">

按住**Shift**键，即可在上一个输入点的水平（X）方向或垂直（Y）方向上绘制当前输入点。至于约束的是水平方向还是垂直方向，则取决于按下 **Shift**时鼠标指针的位置；如果按键时指针位于上一个点的东西两侧，则约束的是水平方向；如果按键时指针位于上一个点的南北两侧，则约束的是垂直方向。如果要改变约束方向，只需松开**Shift**键,并将指针移到另一个新位置，再重新按下**Shift**键即可。


</div>

## Usage X, Y and Z constraints 

1.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
2.  Pick a first point. A previous point is required.
3.  Press **X**, **Y** or **Z** to specify the direction.
4.  The cursor is now constrained.
5.  Pick the next point.
6.  If the command is still active optionally do one of the following:
    -   Press the same key to disable the constraint.
    -   Press one of the two other keys to constrain in a different direction.
7.  X, Y and Z constraints are automatically disabled when the command is finished.

## Notes

-   Constraining can be combined with [snapping](Draft_Snap.md).
-   The [Draft Offset](Draft_Offset.md) command and [Draft Trimex](Draft_Trimex.md) command use a different type of constraining, namely to restrict the operation to a certain segment.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The default **Constrain mod** key, **Shift**, can be changed: **Edit → Preferences... → Draft → Grid and snapping → Snapping → Constrain mod**.
-   The **X**, **Y** and **Z** shortcuts can be changed: **Edit → Preferences... → Draft → User interface settings → In-Command Shortcuts**.





  
