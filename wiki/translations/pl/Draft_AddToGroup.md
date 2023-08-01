---
- GuiCommand:
   Name:Draft AddToGroup
   MenuLocation:Utilities - Move to group...
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   SeeAlso:[Std Group](Std_Group.md), [Draft AddNamedGroup](Draft_AddNamedGroup.md), [Draft AddConstruction](Draft_AddConstruction.md), [Draft AutoGroup](Draft_AutoGroup.md)
---

# Draft AddToGroup/pl

## Description

The <img alt="" src=images/Draft_AddToGroup.svg  style="width:24px;"> **Draft AddToGroup** command moves objects to a [Std Group](Std_Group.md). It can also ungroup objects.

In FreeCAD version 0.20 the command can also handle group-like [Arch](Arch_Workbench.md) objects.

## Usage

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_AddToGroup.svg" width=16px> [Draft AddToGroup](Draft_AddToGroup.md)** button.
    -   Select the **Utilities → <img src="images/Draft_AddToGroup.svg" width=16px> Move to group...** option from the menu.
    -   Select the **Utilities → <img src="images/Draft_AddToGroup.svg" width=16px> Move to group...** option from the [Tree view](Tree_view.md) or [3D view](3D_view.md) context menu.
3.  A menu is displayed near the cursor. Do one of the following:
    -   Select **Ungroup** to move the objects out of the group(s) they are in.
    -   Select the group you want to move the objects to.
    -   Select **+ Add new group** to move the objects to a new group: <small>(v0.20)</small> 
        1.  The **Add group** task panel opens.
        2.  Enter a **Group name**.
        3.  Press the **OK** button.

## Notes

-   Objects can also be moved to a group by drag and dropping them on the group in the [Tree view](Tree_view.md).
-   This command can be used to move objects to the [Draft construction group](Draft_ToggleConstructionMode.md), but, contrary to the [Draft AddConstruction](Draft_AddConstruction.md) command, it does not apply the [construction geometry color](Draft_ToggleConstructionMode#Preferences.md).
-   For more information about organizing your model see [Document structure](Document_structure.md) and [Arch tutorial](Arch_tutorial#Organizing_your_model.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AddToGroup/pl
