---
- GuiCommand:
   Name: Path ToolBitDock
   MenuLocation: Path -> ToolBit Dock
   Workbenches: Path_Workbench
   Shortcut: **P** **T**
   Version: 0.19
   SeeAlso: Path_ToolBitLibraryOpen, Path_Tools, Path_ToolBit
---

# Path ToolBitDock/en

## Description

![](images/Toolbit_Dock.png )

The <img alt="" src=images/Path_ToolBitDock.svg  style="width:16px;"> [ToolBit Dock](Path_ToolBitDock.md) is easily accessible from the main toolbar in the Path workbench. Pressing the button will toggle the state of the dock. The dock is displayed in the right position by default but may be moved by the user. The dock can also be toggled with the Accelerator sequence (p,t).

The purpose of the dock is to display the currently selected library and allow the user to quickly add tool controllers to the Path Job(s).

Double-clicking on a toolbit will create a single tool controller for the toolbit. Multi-selecting toolbits and pressing the \'Add to Job\' button will create tool controllers for all toolbits in the library.

The user may also select multiple tools and use the \'add\...\' button at the bottom to add tool controllers for the selection.

The top of the panel shows the name of the current library **(1)**. All tool libraries from that location are scanned and shown in the dock. The dock will remember the last selection between uses.

A manager button at the top right **(4)** allows the user to launch the library manager. The library manager can be used to maintain the toolbits and to select a different library.

## Usage

### Create Tool Controllers 

1.  There are several ways to open the Toolbit Dock:
    -   Press the **<img src="images/Path_ToolBitDock.svg" width=16px> [Path ToolBitDock](Path_ToolBitDock.md)** button.
    -   Select the **Path → <img src="images/Path_ToolBitDock.svg" width=16px> ToolBit Dock** option from the menu.
    -   Use the keyboard shortcut: **P** then **T**.
2.  Use the dock to add tool controllers to a Path Job
    -   Doubleclick on a toolbit node **(2)** to create a toolcontroller for that toolbit.
    -   select one or more toolbits and press the \'add to Job..**\'(3)** button

## Options





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolBitDock/en
