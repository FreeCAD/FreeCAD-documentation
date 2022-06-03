---
- GuiCommand   *
   Name   *Std TreeSyncPlacement
   MenuLocation   *View → TreeView actions → Sync placement
   Workbenches   *All
   Shortcut   ***T** **3**
   Version   *0.19
---

# Std TreeSyncPlacement/pl

## Description

The **Std TreeSyncPlacement** command toggles the [Tree view](Tree_view.md) SyncPlacement mode. If this mode is on, the **Placement** of objects is automatically adjusted when they are dragged and dropped from one container into another container with a different coordinate system, preserving their placement relative to the global coordinate system.

## Usage

1.  There are several ways to invoke the command   *
    -   Click on the black down arrow to the right of the **<img src="images/Std_TreeSyncView.svg" width=16px>** button and select the **Sync placement** option from the flyout. Note   * the button image will change depending on the selected option.
    -   Select the **View → TreeView actions → <img src="images/Std_TreeSyncPlacement.svg" width=16px> Sync placement** option from the menu.
    -   Use the keyboard shortcut   * **T** then **3**.

## Preferences

The Tree view SyncPlacement mode is stored   * **Tools → Edit parameters... → BaseApp → Preferences → TreeView → SyncPlacement**. It is a boolean value, the default is `False`.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std TreeSyncPlacement/pl
