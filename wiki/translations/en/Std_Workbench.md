---
- GuiCommand   *
   Name   *Std Workbench
   Empty   *1
   MenuLocation   *View → Workbench
   Workbenches   *[Workbenches](Workbenches.md)
---

# Std Workbench/en

## Description

The **Std Workbench** command activates a selected [workbench](Workbenches.md) including its graphical user interface (GUI).

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width   *800px;"> 
*The Workbench dropdown list indicated by number 10 in the standard [interface](interface.md)*

## Usage

1.  There are several ways to invoke the command   *
    -   Select a workbench from the **Workbench dropdown list** in the Workbench toolbar. This option is not available if the current workbench is `<none>` (no workbench).
    -   Select a workbench from the **View → Workbench** sub-menu.

## Notes

-   Additional [External Workbenches](External_Workbenches.md) can be downloaded with the <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr.md).

## Preferences

-   The start up workbench can be changed in the preferences   * **Edit → Preferences... → General → General → Start up**. See [Preferences Editor](Preferences_Editor#General.md).

## Scripting


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change the worbench use the `activateWorkbench` method of the FreeCADGui module. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.activateWorkbench("PartDesignWorkbench")
```





{{Std Base navi

}}  {{Interface navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Workbench/en
