---
 GuiCommand:
   Name: Draft ToggleConstructionMode
   Name/ru: Draft ToggleConstructionMode
   MenuLocation: Черчение -> Утилиты -> Переключить режим конструирования
   Workbenches: Draft_Workbench/ru, Arch_Workbench/ru
---

# Draft ToggleConstructionMode/ru


</div>

## Description

The <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> **Draft ToggleConstructionMode** command switches Draft construction mode on or off. If construction mode is on new [Draft](Draft_Workbench.md) objects are placed in a dedicated group and given a predefined color. This feature is intended for, often temporary, construction geometry used to provide new [snap points](Draft_Snap.md) for creating other objects. When the construction geometry is no longer needed the construction group can easily be [hidden](Std_HideSelection.md) or [deleted](Std_Delete.md).

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;"> 
*Construction geometry, in blue, used to determine the center and radius of a circle*

## Usage

1.  There are several ways to invoke the command:
    -   Press the ![](images/Draft_tray_button_construction.png ) button in the [Draft Tray](Draft_Tray.md). This button is depressed if Draft construction mode is currently on.
    -   [Draft](Draft_Workbench.md): Select the **Utilities → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Toggle construction mode** option from the menu, or from the [Tree view](Tree_view.md) or [3D view](3D_view.md) context menu.
    -   Draft: Use the keyboard shortcut: **C** then **M**.
2.  The button in the [Draft Tray](Draft_Tray.md) is updated.

## Notes

-   If Draft construction mode is switched on the active [layer](Draft_Layer.md) is ignored.

## Preferences

-   To change the label of the construction group: **Edit → Preferences... → Draft → General → Construction group label**.
-   To change the color that is used: **Edit → Preferences... → Draft → General → Construction geometry color**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleConstructionMode/ru
