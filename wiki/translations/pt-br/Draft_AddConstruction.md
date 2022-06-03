---
- GuiCommand   *
   Name   *Draft AddConstruction
   MenuLocation   *Utilities → Add to Construction group
   Workbenches   *[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Version   *0.17
   SeeAlso   *[Draft ToggleConstructionMode](Draft_ToggleConstructionMode.md), [Draft AddToGroup](Draft_AddToGroup.md)
---

# Draft AddConstruction/pt-br

## Descrição

The <img alt="" src=images/Draft_AddConstruction.svg  style="width   *24px;"> **Draft AddConstruction** command moves objects to the [Draft construction group](Draft_ToggleConstructionMode.md). It also applies the [construction geometry color](Draft_ToggleConstructionMode#Preferences.md) to the objects.

## Bug in version 0.19 

In FreeCAD version 0.19 this command and the [Draft ToggleConstructionMode](Draft_ToggleConstructionMode.md) command will typically use different groups. To avoid this change the **Construction group name** in the preferences to {{Value|Draft_Construction}}   * **Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name**. In version 0.20 the **Construction group name** is used for the label of the construction group, the name of the group is always {{Value|Draft_Construction}}.

## Utilização

1.  Select one or more objects.
2.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Draft_AddConstruction.svg" width=16px> [Draft AddConstruction](Draft_AddConstruction.md)** button.
    -   Select the **Utilities → <img src="images/Draft_AddConstruction.svg" width=16px> Add to Construction group** option from the menu.
3.  If it does not exist the construction group is created first.
4.  The objects are moved to the construction group and their color properties are changed.

## Notes

-   Objects can also be moved to the construction group by drag and dropping them on the group in the [Tree view](Tree_view.md), or by using the [Draft AddToGroup](Draft_AddToGroup.md) command. But in both cases the [construction geometry color](Draft_ToggleConstructionMode#Preferences.md) is not applied.
-   For more information about organizing your model see [Document structure](Document_structure.md) and [Arch tutorial](Arch_tutorial#Organizing_your_model.md).


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AddConstruction/pt-br
