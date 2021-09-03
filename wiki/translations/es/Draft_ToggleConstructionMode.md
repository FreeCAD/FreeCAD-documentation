---
- GuiCommand:/es   Name:Draft ToggleConstructionMode   Workbenches:[Arquitectura](Draft_Module/es___Boceto]],_[[Arch_Module/es.md)|MenuLocation:Boceto → Utilidades → Alternar modo de construcción---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

El módulo de Boceto dispone de un modo de construcción, que permite dibujar ciertos objetos en un grupo especial, con un color definido, de modo que se pueda separar sencillamente de otros objetos y desactivarlos cuando no los necesites, o borrarlos después de que no los vuelvas a necesitar.


</div>

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;">


</div>

## Bug in version 0.19 {#bug_in_version_0.19}

In FreeCAD version 0.19 this command and the [Draft AddConstruction](Draft_AddConstruction.md) command will typically use different groups. To avoid this change the {{MenuCommand|Construction group name}} in the preferences to {{Value|Draft_Construction}}: {{MenuCommand|Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name}}. In version 0.20 the {{MenuCommand|Construction group name}} is used for the label of the construction group, the name of the group is always {{Value|Draft_Construction}}.

## Usage


<div class="mw-translate-fuzzy">

## Utilización

1.  Presiona el botón **<img src="images/Draft_ToggleConstructionMode.png" width=16px> [Alternar modo de construcción](Draft_ToggleConstructionMode/es.md)
**
2.  Dibuja algunos objetos
3.  Presiona el botón **<img src="images/Draft_ToggleConstructionMode.png" width=16px> [Alternar modo de construcción](Draft_ToggleConstructionMode/es.md)** de nuevo para volver al modo habitual


</div>

## Notes

-   If Draft construction mode is switched on the active [layer](Draft_Layer.md) is ignored.

## Preferences

-   To change the label (<small>(v0.20)</small> ) of the construction group: {{MenuCommand|Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name}}.
-   To change the color that is used: {{MenuCommand|Edit → Preferences... → Draft → General settings → Construction Geometry → Construction geometry color}}.





 
