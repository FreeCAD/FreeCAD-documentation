---
 GuiCommand:
   Name: Draft AddConstruction
   MenuLocation: Utilities , Add to construction group<br>Utils , Add to construction group
   Workbenches: Draft_Workbench, BIM_Workbench
   Version: 0.17
   SeeAlso: Draft_ToggleConstructionMode, Draft_AddToGroup
---

# Draft AddConstruction/en

## Description

The <img alt="" src=images/Draft_AddConstruction.svg  style="width:24px;"> **Draft AddConstruction** command moves objects to the [Draft construction group](Draft_ToggleConstructionMode.md). It also applies the [construction geometry color](Draft_ToggleConstructionMode#Preferences.md) to the objects.

## Usage

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   [Draft](Draft_Workbench.md): Press the **<img src="images/Draft_AddConstruction.svg" width=16px> [Add to construction group](Draft_AddConstruction.md)** button.
    -   Draft: Select the **Utilities → <img src="images/Draft_AddConstruction.svg" width=16px> Add to construction group** option from the menu, or from the [Tree view](Tree_view.md) or [3D view](3D_view.md) context menu.
    -   [BIM](BIM_Workbench.md): Select the **Utils → <img src="images/Draft_AddConstruction.svg" width=16px> Add to construction group** option from the menu.
3.  If it does not exist the construction group is created first.
4.  The objects are moved to the construction group and their color properties are changed.

## Notes

-   Objects can also be moved to the construction group by drag and dropping them on the group in the [Tree view](Tree_view.md), or by using the [Draft AddToGroup](Draft_AddToGroup.md) command. But in both cases the [construction geometry color](Draft_ToggleConstructionMode#Preferences.md) is not applied.
-   For more information about organizing your model see [Document structure](Document_structure.md) and [Arch tutorial](Arch_tutorial#Organizing_your_model.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AddConstruction/en
