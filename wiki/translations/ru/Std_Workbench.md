---
- GuiCommand:
   Name: Std Workbench
   Name/ru: Std Workbench
   Empty: 1
   MenuLocation: {{StdMenu|[Вид](Std_View_Menu/ru.md)}} - Верстак
   Workbenches: [Верстаки](Workbenches/ru.md)
   SeeAlso: 
---

# Std Workbench/ru


</div>

## Описание

The **Std Workbench** command activates a selected [workbench](Workbenches.md) including its graphical user interface (GUI).

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:800px;"> 
*The Workbench dropdown list indicated by number 10 in the standard [interface](interface.md)*

## Применение

1.  There are several ways to invoke the command:
    -   Select a workbench from the **Workbench dropdown list** in the Workbench toolbar. This option is not available if the current workbench is `<none>` (no workbench).
    -   Select a workbench from the **View → Workbench** sub-menu.

## Примечания

-   Additional [External Workbenches](External_Workbenches.md) can be downloaded with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).

## Настройки

-   The start up workbench can be changed in the preferences: **Edit → Preferences... → General → General → Start up**. See [Preferences Editor](Preferences_Editor#General.md).

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change the worbench use the `activateWorkbench` method of the FreeCADGui module. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.activateWorkbench("PartDesignWorkbench")
```





{{Std Base navi

}}  {{Interface navi}}



---
⏵ [documentation index](../README.md) > Std Workbench/ru
