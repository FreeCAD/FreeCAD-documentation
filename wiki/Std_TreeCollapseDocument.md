---
- GuiCommand:
   Name:Std TreeCollapseDocument
   MenuLocation:View → TreeView actions → Collapse/Expand
   Workbenches:All
   Version:0.19
   SeeAlso:[Std TreeSingleDocument](Std_TreeSingleDocument.md), [Std TreeMultiDocument](Std_TreeMultiDocument.md)
---

## Description

The **Std TreeCollapseDocument** command switches the [Tree view](Tree_view.md) DocumentMode to CollapseDocument. In this mode activating a document's [3D view](3D_view.md) will automatically expand that document in the Tree view and collapse all other documents. The other modes are [SingleDocument](Std_TreeSingleDocument.md) and [MultiDocument](Std_TreeMultiDocument.md).

## Usage

1.  There are several ways to invoke the command:
    -   Click on the black down arrow to the right of the **<img src="images/Std_TreeSyncView.svg" width=16px>** button and select the **Collapse/Expand** option from the flyout. Note: the button image will change depending on the selected option.
    -   Select the **View → TreeView actions → <img src="images/Std_TreeCollapseDocument.svg" width=16px> Collapse/Expand** option from the menu.

## Preferences

The Tree view DocumentMode mode is stored: **Tools → Edit parameters... → BaseApp → Preferences → TreeView → DocumentMode**. It is an integer value. Possible values are `0` (SingleDocument), `1` (MultiDocument) or `2` (CollapseDocument). The default is `2`.




 {{Std Base navi}}  
