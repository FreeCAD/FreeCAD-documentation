# Addon
## Introduction

In FreeCAD and in this documentation, an [addon](addon.md) is any component that is not part of the base installation, but that can be added to the system by certain methods.

## Different types 

There are three types of addons   *

-   [Macros](Macros.md)   * short snippet of [Python](Python.md) code that provides a new tool or functionality in a single file ending with `.FCMacro`.
-   [Workbenches](External_workbenches.md)   * collections of Python files that provide related [Gui Commands](Gui_Command.md) (tools) centered around a particular topic, for example, tools to design cabinets, or tools to work with architecture, or tools to design boats, etc. These workbenches usually define new toolbars where [commands](Gui_Command.md) are placed as buttons.
-   [Preference Packs](Preference_Packs.md)   * distributable collections of user preferences. <small>(v0.20)</small> 

## Installation

The recommended way to install addons is with the <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr.md).

But for macros and workbenches manual installation is also possible   *

-   [How to install macros](How_to_install_macros.md)
-   [Installing more workbenches](Installing_more_workbenches.md)

## Information for developers 

If you have developed a macro or workbench, and want to see it included in the Addon manager, read how to do so on the repository pages   * ([FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) and [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/)). If you add your macro to the [Macros recipes](Macros_recipes.md) page, there is nothing else to do, it will automatically be picked up by the Addon manager.

### Python workbenches 

For Python workbenches, you don\'t need any specific approval to have your workbench added to the Addon Manager. In addition, because your Addon is outside the FreeCAD source code, you can choose the license you want. If you request for your workbench to be added to the Addon Manager\'s default list (we will not add any new workbench without a request from its authors), either by asking so on the forum or by opening an issue on the [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) repository, your code will stay on your own git repository, we will just add it as a submodule to the [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) repository. Of course, before adding your workbench, we will take a look at it and make sure there is nothing potentially problematic with it. For more details about structuring your Addon, including information about metadata used by the Addon Manager, see [Workbench creation](Workbench_creation.md).

### C++ workbenches 

If you develop a workbench in C++, it cannot be run directly by users and must be compiled first. You then have two options, either you provide precompiled versions of your workbench yourself, for the different operating systems, or you should request to have your code merged into the FreeCAD source code. For that, you should use the LGPL license (or a fully compatible license like MIT or BSD), and you must present your new tools to the community in the [FreeCAD forum](https   *//forum.freecadweb.org) for review. Once your code has been tested and approved, you should fork the FreeCAD repository, if not done yet, create a new branch, push your code to it, and open a pull request so that your branch is merged into the main repository.



## Adding a WorkBench to the AddOn Manager 

-   Activate AddOn Manager \"developer mode\"
    -   Go to **Edit \> Settings \> Preference \> AddOn Manager** at the bottom of the Preferences page, there is checklist.
    -   This will give you a new button in the Addon Manager that will help you to create your Addon\'s \*package.xml\* file.
-   Create package.xml file
    -   Hit the **+** and create a single workbench.
    -   Check the box to indicate it\'s the only item in the addon.
    -   Set the class name to the addon main class name.
    -   Set subdirectory to **\"./\"**.
    -   Everything else should be optional.

### Add it the .gitmodules file. 

-   Fork <https   *//github.com/FreeCAD/FreeCAD-addons/>.
-   Create a new branch
-   Edit **.gitmodules** file to include your new Addon, in alphabetical order.
-   Push that new branch to GitHub.
-   Submit a Pull Request to the FreeCAD-Addons repo with the new **.gitmodules** file.




[Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon
