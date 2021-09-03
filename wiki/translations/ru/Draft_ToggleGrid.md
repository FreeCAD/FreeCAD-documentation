---
- GuiCommand:/ru
   Name:Draft ToggleGrid
   Name/ru:Показывать сетку
   MenuLocation:Черчение → Вспомогательные → Показывать сетку
   Workbenches:[Draft](Draft_Module/ru.md), [Arch](Arch_Module/ru.md)
   Shortcut:**G** **R**
   SeeAlso:[Draft Snap](Draft_Snap/ru.md), [Draft ToggleSnap](Draft_Snap_Lock/ru.md)
---


</div>

## Description


<div class="mw-translate-fuzzy">

Этот инструмент позволяет показывать и скрывать сетку, определённую в [Draft Preferences](Draft_Preferences/ru.md) или инструментом [Draft SelectPlane](Draft_SelectPlane/ru.md)


</div>

In FreeCAD version 0.19 and 0.20 the grid is always displayed when a command becomes active and toggling the grid while a command is active does not work.

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Optionally change the [working plane and/or the grid](Draft_SelectPlane.md).
2.  To invoke **Draft ToggleGrid** do one of the following:
    -   Press the **<img src="images/Draft_ToggleGrid.svg" width=16px>** button in the Draft Snap toolbar.
    -   Press the **<img src="images/Draft_ToggleGrid.svg" width=16px>** button in the [Draft snap widget](Draft_snap_widget.md).
    -   Use the keyboard shortcut: **G** then **R**. This shortcut cannot be used when a command is active.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).

-   To use the grid select: {{MenuCommand|Edit → Preferences... → Draft → Grid and snapping → Grid → Use grid}}. After changing this preference you must restart FreeCAD.
-   Several other grid preferences are also available: {{MenuCommand|Edit → Preferences... → Draft → Grid and snapping → Grid}}.


<div class="mw-translate-fuzzy">





</div>


 
