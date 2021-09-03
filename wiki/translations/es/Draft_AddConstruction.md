---
- GuiCommand:/es
   Name:Draft AddConstruction
   Name/es:Draft AddConstruction
   MenuLocation:Draft → Utilities → Add to construction group
   Workbenches:[Draft](Draft_Workbench/es.md), [Arch](Arch_Workbench/es.md)
   SeeAlso:[[Draft ToggleConstructionMode/es]],  [[Draft AddToGroup/es]]
   Version:0.17
---


</div>

## Descripción


<div class="mw-translate-fuzzy">

Este comando agrega los objetos seleccionados a la [Draft Construction group](Draft_ToggleConstructionMode.md).


</div>

## Bug in version 0.19 {#bug_in_version_0.19}

In FreeCAD version 0.19 this command and the [Draft ToggleConstructionMode](Draft_ToggleConstructionMode.md) command will typically use different groups. To avoid this change the {{MenuCommand|Construction group name}} in the preferences to {{Value|Draft_Construction}}: {{MenuCommand|Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name}}. In version 0.20 the {{MenuCommand|Construction group name}} is used for the label of the construction group, the name of the group is always {{Value|Draft_Construction}}.


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Seleccionar algunos objetos
2.  Haga clic en el menú Borrador → Utilidades → **<img src="images/Draft_ToggleConstructionMode.png" width=16px> [Add to construction group](Draft_AddConstruction.md)
**


</div>

## Notes

-   Objects can also be moved to the construction group by drag and dropping them on the group in the [Tree view](Tree_view.md), or by using the [Draft AddToGroup](Draft_AddToGroup.md) command. But in both cases the [construction geometry color](Draft_ToggleConstructionMode#Preferences.md) is not applied.
-   For more information about organizing your model see [Document structure](Document_structure.md) and [Arch tutorial](Arch_tutorial#Organizing_your_model.md).


<div class="mw-translate-fuzzy">





</div>


 
