---
 GuiCommand:
   Name: Draft AddToGroup
   MenuLocation: Utilities , Move to group...
   Workbenches: Draft_Workbench
   SeeAlso: Std_Group, Draft_AddNamedGroup, Draft_AddConstruction, Draft_AutoGroup
---

# Draft AddToGroup

## Description

The <img alt="" src=images/Draft_AddToGroup.svg  style="width:24px;"> **Draft AddToGroup** command moves objects to a [Std Group](Std_Group.md) or a group-like [BIM](BIM_Workbench.md) object. It can also ungroup objects.

## Usage

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_AddToGroup.svg" width=16px> [Move to group...](Draft_AddToGroup.md)** button.
    -   Select the **Utilities → <img src="images/Draft_AddToGroup.svg" width=16px> Move to group...** option from the menu, or from the [Tree view](Tree_view.md) or [3D view](3D_view.md) context menu.
3.  A menu is displayed near the cursor. Do one of the following:
    -   Select **Ungroup** to move the objects out of the group(s) they are in.
    -   Select the group you want to move the objects to.
    -   Select **+ Add new group** to move the objects to a new group:
        1.  The **Add group** task panel opens.
        2.  Enter a **Group name**.
        3.  Press the **OK** button.

## Notes

-   Objects can also be moved to a group by drag and dropping them on the group in the [Tree view](Tree_view.md).
-   This command can be used to move objects to the [Draft construction group](Draft_ToggleConstructionMode.md), but, contrary to the [Draft AddConstruction](Draft_AddConstruction.md) command, it does not apply the [construction geometry color](Draft_ToggleConstructionMode#Preferences.md).
-   For more information about organizing your model see [Document structure](Document_structure.md) and [Arch tutorial](Arch_tutorial#Organizing_your_model.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AddToGroup
