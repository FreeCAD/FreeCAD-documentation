---
 GuiCommand:
   Name: CAM ToolBitDock
   MenuLocation: CAM , ToolBit Dock
   Workbenches: CAM_Workbench
   Shortcut: **P** **T**
   Version: 0.19
   SeeAlso: CAM_ToolBitLibraryOpen, CAM_Tools, CAM_ToolBit
---

# CAM ToolBitDock/en

## Description

The <img alt="" src=images/CAM_ToolBitDock.svg  style="width:16px;"> [ToolBit Dock](CAM_ToolBitDock.md) is easily accessible from the main toolbar in the CAM workbench. Pressing the button will toggle the state of the dock. The dock is displayed in the right position by default but may be moved by the user.

The purpose of the dock is to display the currently selected library and allow the user to quickly add tool controllers to the CAM Job(s).

Double-clicking on a toolbit will create a single tool controller for the toolbit. Multi-selecting toolbits and pressing the \'Add to Job\' button will create tool controllers for all toolbits in the library.

The user may also select multiple tools and use the \'add\...\' button at the bottom to add tool controllers for the selection.

+++
| <img alt="" src=images/Toolbit_Dock.png  style="width:200px;"> | The top of the panel shows the name of the current library **(1)**. All tool libraries from that location are scanned and shown in the dock. The dock will remember the last selection between uses. A manager button at the top right **(4)** allows the user to launch the library manager. The library manager can be used to maintain the toolbits and to select a different library. |
+++

## Usage

### Create Tool Controllers 

1.  There are several ways to open the Toolbit Dock:
    -   Press the **<img src="images/CAM_ToolBitDock.svg" width=16px> [CAM ToolBitDock](CAM_ToolBitDock.md)** button.
    -   Select the **CAM → <img src="images/CAM_ToolBitDock.svg" width=16px> ToolBit Dock** option from the menu.
    -   Use the keyboard shortcut: **P** then **T**.
2.  Use the dock to add tool controllers to a CAM Job.
    -   Doubleclick on a toolbit node **(2)** to create a toolcontroller for that toolbit.
    -   select one or more toolbits and press the \'add to Job..\' **(3)** button.

## Options





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM ToolBitDock/en
