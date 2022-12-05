# Addon/pl
{{TOCright}}

## Wprowadzenie

In FreeCAD and in this documentation, an [addon](addon.md) is any component that is not part of the base installation, but that can be added to the system by certain methods.

## Różne rodzaje 

There are three types of addons:

-   [Macros](Macros.md): short snippet of [Python](Python.md) code that provides a new tool or functionality in a single file ending with `.FCMacro`.
-   [Workbenches](External_workbenches.md): collections of Python files that provide related [Gui Commands](Gui_Command.md) (tools) centered around a particular topic, for example, tools to design cabinets, or tools to work with architecture, or tools to design boats, etc. These workbenches usually define new toolbars where [commands](Gui_Command.md) are placed as buttons.
-   [Preference Packs](Preference_Packs.md): distributable collections of user preferences. <small>(v0.20)</small> 

## Instalacja

The recommended way to install addons is with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).

But for macros and workbenches manual installation is also possible:

-   [How to install macros](How_to_install_macros.md)
-   [Installing more workbenches](Installing_more_workbenches.md)

## Informacja dla programistów 

If you have developed a macro or workbench, and want to see it included in the Addon manager, read how to do so on the repository pages: ([FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) and [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/)). If you add your macro to the [Macros recipes](Macros_recipes.md) page, there is nothing else to do, it will automatically be picked up by the Addon manager.

See also:

-   [Distribution of a Python workbench](Workbench_creation#Distribution.md)
-   [Distribution of a C++ workbench](Workbench_creation#Distribution_2.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/pl
