---
- GuiCommand:
   Name:Draft ToggleGrid
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**G** **R**
   SeeAlso:[Draft Snap](Draft_Snap.md), [Draft Snap Grid](Draft_Snap_Grid.md), [Draft SelectPlane](Draft_SelectPlane.md)
---

# Draft ToggleGrid

## Description

The <img alt="" src=images/Draft_ToggleGrid.svg  style="width:24px;"> **Draft ToggleGrid** command switches the grid on or off. The grid can only be used if the **Use grid** preference is selected. See [Preferences](#Preferences.md).

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

-   To use the grid select: **Edit → Preferences... → Draft → Grid and snapping → Grid → Use grid**. After changing this preference you must restart FreeCAD.
-   Several other grid preferences are also available: **Edit → Preferences... → Draft → Grid and snapping → Grid**.

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleGrid
