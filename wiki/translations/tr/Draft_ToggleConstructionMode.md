---
- GuiCommand:/tr
   Name:Draft ToggleConstructionMode
   Name/tr:İnşaat modunu değiştir
   MenuLocation:Draft → Utilities → Toggle construction mode
   Workbenches:[Draft](Draft_Workbench/tr.md), [Arch](Arch_Workbench/tr.md)
   Shortcut:**C** **M**
   SeeAlso:[Draft AddConstruction](Draft_AddConstruction.md), [Draft AutoGroup](Draft_AutoGroup.md)
---


</div>

## Description

The <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> **Draft ToggleConstructionMode** command switches Draft construction mode on or off. If construction mode is on new [Draft](Draft_Workbench.md) objects, except [Draft Points](Draft_Point.md), are placed in a dedicated group and given a predefined color. This feature is intended for, often temporary, construction geometry used to provide new [snap points](Draft_Snap.md) for creating other objects. When the construction geometry is no longer needed the construction group can easily be [hidden](Std_HideSelection.md) or [deleted](Std_Delete.md).

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;"> 
*Construction geometry, in blue, used to determine the center and radius of a circle*

## Bug in version 0.19 

In FreeCAD version 0.19 this command and the [Draft AddConstruction](Draft_AddConstruction.md) command will typically use different groups. To avoid this change the **Construction group name** in the preferences to {{Value|Draft_Construction}}: **Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name**. In version 0.20 the **Construction group name** is used for the label of the construction group, the name of the group is always {{Value|Draft_Construction}}.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_ToggleConstructionMode.svg" width=16px> [Draft ToggleConstructionMode](Draft_ToggleConstructionMode.md)** button in the [Draft Tray](Draft_Tray.md). This button is depressed if Draft construction mode is currently on.
    -   Select the **Utilities → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Toggle construction mode** option from the menu.
    -   Use the keyboard shortcut: **C** then **M**.
2.  The button in the [Draft Tray](Draft_Tray.md) is updated.

## Notes

-   If Draft construction mode is switched on the active [layer](Draft_Layer.md) is ignored.

## Preferences

-   To change the label (<small>(v0.20)</small> ) of the construction group: **Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name**.
-   To change the color that is used: **Edit → Preferences... → Draft → General settings → Construction Geometry → Construction geometry color**.





 
