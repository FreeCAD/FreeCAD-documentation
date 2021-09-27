# Addon/en
## Introduction

In FreeCAD and in this documentation, an [addon](addon.md) is any component that is not part of the base installation, but that can be added to the system by certain methods.

## Different types 

There are roughly three types of addons:

-   _ code that provides a new tool or functionality in a single file ending with `.FCMacro`.
-   Module: a single Python source file, or a collection of Python files, that extends the software in some way. Modules don\'t necessarily define a graphical \"workbench\" but may provide a supporting feature, for example, a library that performs conversion of formats, or code that modifies the graphical [interface](interface.md).
-   _ (tools) centered around a particular topic, for example, tools to design cabinets, or tools to work with architecture, or tools to design boats, etc. These workbenches usually define new toolbars where [commands](Gui_Command.md) are placed as buttons.

Macros as installed under the user\'s `Macro/` directory, while modules and workbenches are under the `Mod/` directory. {{Code|lang=bash|code=
$HOME/.FreeCAD/Macro/
$HOME/.FreeCAD/Mod/
}}

Macros usually start as a way to simplify or automate the task of drawing or editing a particular object. If many of these macros are collected inside a directory, and structure is provided to collect those tools, then the entire directory may be distributed as a workbench.

In other words, macros, modules, and workbenches are essentially the same thing, pieces of Python code that extend the base installation. Macros are usually short and focused on a single task, modules usually provide new functions or interfaces, and workbenches are collections of tools (buttons, menus) and graphical interfaces to perform related tasks.

If a workbench is sufficiently developed and is well documented, it may be included as one of the base [workbenches](workbenches.md) in FreeCAD.

## Installation

Starting from FreeCAD 0.17, the recommended way to install addons is with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).

However, manual installation is still possible.

-   [How to install macros](How_to_install_macros.md)
-   [Installing more workbenches](Installing_more_workbenches.md)




_

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/en
