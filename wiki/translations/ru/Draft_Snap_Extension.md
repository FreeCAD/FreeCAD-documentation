---
- GuiCommand:/ru
   Name:Draft Extension
   Name/ru:Draft Extension
   Workbenches:[Draft](Draft_Module/ru.md), [Arch](Arch_Module/ru.md)
   MenuLocation:Черчение → [Привязка](Draft_Snap/ru.md) → Продолжение
   Shortcut:
   SeeAlso:---


</div>

## Описание

Этот метод соответствует точке на воображаемой линии, которая простирается за пределы концов отрезков. <img alt="" src=images/Draft_Snap_Extension.png  style="width:400px;">


*Snapping the second point of a line to the extension of another line*

## Использование

1.  Убедитесь, что {{Button | <img src="images/_Snap_Lock.svg_" width= 16px> [ Draft ToggleSnap](Draft_ToggleSnap_.md)}} и {{Button | <img src="images/_Snap_Lock.svg_" width= 16px> [ Draft ToggleSnap](Draft_ToggleSnap_.md)}} активируется..
2.  Выберите инструмент рисования, чтобы нарисовать фигуру.
3.  Поместите курсор рядом с концами сегмента линии, который вы хотите расширить.
4.  Когда вы перемещаете указатель в сторону от сегмента линии, сохраняя тот же наклон, пунктирная линия указывает расширение исходной строки.
5.  Нажмите, чтобы добавить новую точку.










The <img alt="" src=images/Draft_Snap_Extension.svg  style="width:24px;"> **Draft Snap Extension** option snaps to an imaginary line that extends beyond the endpoints of straight edges. The edges can belong to [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) objects but also to objects created with other [workbenches](Workbenches.md).

Up to two edged can be referenced by this snap option and [Draft Snap Parallel](Draft_Snap_Parallel.md), making it possible to snap to virtual intersections. Both snap options can also be combined with other snap options.

![](images/Draft_Snap_Extension_example.png ) *Snapping the second point of a line to the extension of an edge*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
2.  If **Draft Snap Extension** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Extension.svg" width=16px>** button in the Draft Snap toolbar.
    -   Press the **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu select the **<img src="images/Draft_Snap_Extension.svg" width=16px> Snap Extension** option.
3.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
4.  Note that you can also change snap options while a command is active.
5.  Move the cursor over a straight edge.
6.  The edge is highlighted.
7.  If you now move the cursor beyond the endpoints of the edge, you will see a dashed line appear when the cursor is on the extended edge.
8.  The point is marked and the <img alt="" src=images/Draft_Snap_Extension.svg  style="width:16px;"> icon is displayed near the cursor.
9.  Click to confirm the point.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).





 