# <img alt="PieMenu Workbench icon" src=images/PieMenuWorkbench.svg  style="width:64px;"> PieMenu Workbench

 

## Introduction

The <img alt="" src=images/PieMenuWorkbench.svg  style="width:32px;"> **PieMenu Workbench** is an [external workbench](External_workbenches.md) that brings a customizable menu providing quick access to FreeCAD tools via keyboard shortcuts. You can choose from multiple shapes, themes, customize tools and shortcuts, and much more.

 <img alt="" src=images/PieMenu_example.jpg  style="width:300px;"> 



*Example of a PieMenu containing 16 pies.*

In the example above, the first section corresponds to parametric workbenches, then workbenches for design and technical drawings, then workbenches for assemblies, then some workbenches for the author to make tests of new tools and finally a shortcut to the web tools.

## Installation

1.  Install the PieMenu Workbench via the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md). For manual installation, see [Installing more workbenches](Installing_more_workbenches.md).
2.  Restart FreeCAD.

## Definitions

-   A **PieMenu** is a set of tools grouped within a menu to create a shortcut bar accessible via a keyboard shortcut.
-   A **ToolBar** is a set of existing shortcuts in FreeCAD, containing a set of tools from a workbench.
-   **Context Mode**: A special activation mode that takes into account the geometry selected by the user to determine which PieMenu to activate based on the settings.
-   **Global shortcut**: General shortcut assigned to PieMenu to open the default PieMenu.
-   **Individual shortcut**: Shortcut assigned to a particular PieMenu.

## Usage

1.  Press the global global shortcut (default is **Tab** key) on the keyboard to invoke PieMenu.

### First launch 

-   It may be necessary to restart FreeCAD after installation and after the initial activation of PieMenu to ensure that the configuration is set up correctly.
-   By default, the global shortcut to activate PieMenu is the **Tab** key. However, if this does not work or if you wish to change it, you can access the Preferences via the **Accessories → Pie menu settings** menu, then **Global settings** tab, then **Global shortcut**.
-   You can assign a simple shortcut (e.g. a single key like **A**), a composite shortcut (e.g. **CTRL**+**Q**), or a multi-key shortcuts (e.g. **F**, **F**).

### Create/Modify a PieMenu 

In case of a fresh installation, PieMenu will create 3 PieMenus (**View**, **PartDesign**, and **Sketcher**) with some common tools. To create or modify other PieMenus, simply go to the Preferences (**QuickMenu → Preferences** or **Accessories Menu → PieMenu Preferences**).

 <img alt="" src=images/PieMenu_QuickMenu.png  style="width:300px;"> 



*QuickMenu*

The **QuickMenu** is the context menu displayed when clicking on the integrated button in the PieMenu, it allows to quickly adjusting certain settings. If the QuickMenu is not visible, it must be enabled in the **Preferences** by activating the **Show QuickMenu** option.

## PieMenu preferences 

The PieMenu preferences window contains 3 vertically stacked sections.

### Top section 

 <img alt="" src=images/PieMenu_top_section.png  style="width:400px;"> 

The top section contains a set of buttons that let you:

1.  Change the icon of your PieMenu.
2.  Switch between all your PieMenus.
3.  Add a new PieMenu.
4.  Remove a PieMenu.
5.  Rename a PieMenu.
6.  Copy a PieMenu.
7.  Create a new PieMenu from a existing toolbar.

### Middle section 

The middle section in turn is horizontally divided into 3 sections that can be resized or even hidden using the splitters placed between the sections. The first section has 4 tabs each containing several settings/tools.

#### PieMenu tab 

Create a new PieMenu by clicking on the **+** button, name it, and validate. It will now be visible in the dropdown list of PieMenus. Modify and adjust available settings (settings may vary depending on the PieMenu configuration):

 <img alt="" src=images/PieMenu_Tab_PieMenu.png  style="width:600px;"> 



*Window split into 3 sections showing PieMenu settings, a list of PieMenu actions and the current PieMenu preview.*

-   **Menu size**: Adjusts the size of the menu.
-   **Button size**: Adjusts the size of the buttons (Note: maximum size depends on the menu size).
-   **Shape**: Multiple shapes are available.
-   **Trigger Mode**: Choose the activation mode: \'On press\' or \'On hover\' of the mouse for this PieMenu.
-   **Set the hover activation delay**: To avoid triggering too quickly when passing over multiple commands, it is necessary to set a sufficient delay.
-   **Show command names**: Some shapes allow displaying command names.
-   **Number of rows and columns**: For shapes allowing a layout in rows and/or columns.
-   **Icon spacing**: Adjusts the space between buttons.

#### Tools tab 

 <img alt="" src=images/PieMenu_Tab_Tools.png  style="width:600px;"> 



*Window split on 2 sections containing available tools and current PieMenu preview.*

-   Check the desired tools to add them to your PieMenu tool list.
-   You can move or delete tools using the buttons located below the tools list.
-   **Tip**: You can search for tools by their name in the search bar.

#### Context tab 

 <img alt="" src=images/PieMenu_Tab_Context.png  style="width:600px;"> 



*Window split on 2 sections containing context settings and list of PieMenu actions.*

***(Attention, this feature is not fully functional, there may be bugs)***

Context allows activating a specific PieMenu based on the geometry selected by the user. For example, when the user selects a face in the 3D model, one might want a PieMenu for creating a \'New Sketch\' to open. This is possible with the Context mode.

##### How to use the context mode? 

In normal use, the default PieMenu opens when the global shortcut is pressed, but sometimes the user needs specific tools depending on the type of 3D object selected.

For example let\'s take the case *you want only the tools that are useful when a face of a 3D object is selected in PartDesign*. You can create a PieMenu containing these tools and set the display conditions for this PieMenu in the Context tab as follows:

-   If you select only one face (while in the PartDesign workbench) and press the global shortcut, this PieMenu is displayed, giving access only to the tools that the user has set in this PieMenu. If the box \'Immediate triggering when conditions are met\' is ticked this will trigger the immediate display of the PieMenu without the need to press the global shortcut.



:   <img alt="" src=images/PieMenu_Context_1.png  style="width:600px;">
-   The advantage is that you can create as many PieMenus as you need to cover your current needs. For example, you may need a PieMenu with only the tools that can be used in PartDesign with the edges:



:   <img alt="" src=images/PieMenu_Context_2.png  style="width:600px;">
-   Because of the inheritance of code from previous versions of PieMenu, for context mode to work it is necessary for \"Global Context\" mode to be activated either by the QuickMenu or by the general parameters.



:   <img alt="" src=images/PieMenu_Context_3.png  style="width:600px;">



#### Global settings tab 

 <img alt="" src=images/PieMenu_Tab_GlobalSettings.png  style="width:600px;"> 



*Window containing global settings that applies to all PieMenus.*

Here you can:

-   Select the theme style.
-   Enable or disable the QuickMenu.
-   Enable or disable the Context mode (also available in the QuickMenu).
-   Enable or disable the toggle mode for the global shortcut.
-   Enable long right click press to open PieMenu feature.
-   Import/Export settings.
-   Assign the global shortcut.

### Bottom section 

 <img alt="" src=images/PieMenu_bottom_section.png  style="width:400px;"> 

The bottom section contains a set of buttons that let you:

1.  Open the **About** page.
2.  Open the documentation using the FreeCAD [Help module](Help_Module.md) (check your setting on **Edit → Preferences → General → Help → Display**).
3.  Close the preferences window.

## References

-   Author: Grubuntu
-   Source code: <https://github.com/Grubuntu/PieMenu>
-   Bug reports and feature requests: <https://github.com/Grubuntu/PieMenu/issues>
-   Forum topic: <https://forum.freecad.org/viewtopic.php?t=84101>

## Links

-   [CHANGELOG](https://github.com/Grubuntu/PieMenu/blob/master/CHANGELOG.md)



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External%20Workbenches.md) > PieMenu Workbench
