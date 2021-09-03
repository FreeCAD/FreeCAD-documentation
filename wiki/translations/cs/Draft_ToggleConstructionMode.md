---
- GuiCommand:/cs   Name:Draft ToggleConstructionMode   Name/cs:DKreslení Přepnutí do konstrukčního módu   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení -> Utility -> Přepnutí do konstrukčního módu---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Kreslicí modul má konstrukční mód, který umožňuje kreslit určité objekty ve speciální skupině s definovoanou barvou, takže je snadné je odlišit od ostatních objektů a když tento mód nepotřebujeme lze jej vypnout nebo objekty smazat.


</div>

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;"> 
*Construction geometry, in blue, used to determine the center and radius of a circle*

## Bug in version 0.19 {#bug_in_version_0.19}

In FreeCAD version 0.19 this command and the [Draft AddConstruction](Draft_AddConstruction.md) command will typically use different groups. To avoid this change the {{MenuCommand|Construction group name}} in the preferences to {{Value|Draft_Construction}}: {{MenuCommand|Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name}}. In version 0.20 the {{MenuCommand|Construction group name}} is used for the label of the construction group, the name of the group is always {{Value|Draft_Construction}}.

## Usage


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_ToggleConstructionMode.png" width=16px> [Přepnutí konstrukčního módu](Draft_ToggleConstructionMode/cs.md)
**
2.  Nakreslete nějaké objekty
3.  Stiskněte ještě jednou tlačítko **<img src="images/Draft_ToggleConstructionMode.png" width=16px> [Přepnutí konstrukčního módu](Draft_ToggleConstructionMode/cs.md)** pro návrat do normálního módu


</div>

## Notes

-   If Draft construction mode is switched on the active [layer](Draft_Layer.md) is ignored.

## Preferences

-   To change the label (<small>(v0.20)</small> ) of the construction group: {{MenuCommand|Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name}}.
-   To change the color that is used: {{MenuCommand|Edit → Preferences... → Draft → General settings → Construction Geometry → Construction geometry color}}.





 
