---
- GuiCommand:
   Name:Std TreeSelection
   MenuLocation:View → TreeView actions → Go to selection
   Workbenches:All
   Shortcut:**T** **G**
   Version:0.19
---

# Std TreeSelection/en

## Description

The **Std TreeSelection** command scrolls the [Tree view](Tree_view.md) to the first created object in a [3D view](3D_view.md) selection.

If the Tree view [SyncSelection](Std_TreeSyncSelection.md) mode is off, the Tree view is scrolled to the first created object in the selection whose parent was already expanded in the Tree view. If none of the objects\' parents are expanded the command will have no effect in that mode.

## Usage

1.  Select one or more objects in a 3D view.
2.  There are several ways to invoke the command:
    -   Click on the black down arrow to the right of the **<img src="images/Std_TreeSyncView.svg" width=16px>** button and select the **<img src="images/Std_TreeSelection.svg" width=16px> Go to selection** option from the flyout. Note: the button image will change depending on the selected option.
    -   Select the **View → TreeView actions → <img src="images/Std_TreeSelection.svg" width=16px> Go to selection** option from the menu.
    -   Select the **<img src="images/Std_TreeSelection.svg" width=16px> Go to selection** option from the 3D view context menu.
    -   Use the keyboard shortcut: **T** then **G**.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std TreeSelection/en
