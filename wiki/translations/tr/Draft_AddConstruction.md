---
- GuiCommand:/tr
   Name/tr:İnşa Ekle
   MenuLocation:Taslak → Araçlar → İnşa grubuna ekle
   Workbenches:[Taslak](Draft_Workbench.md), [Yapı](Arch_Workbench.md)
   SeeAlso:[İnşa moduna geç](Draft_ToggleConstructionMode/tr.md), [Gruba ekle](Draft_AddToGroup/tr.md)
   Version:0.17
---


</div>

## Tanım


<div class="mw-translate-fuzzy">

Bu araç seçilen nesne(ler)i [Taslak İnşa grubuna](Draft_ToggleConstructionMode/tr.md) katar.


</div>

## Bug in version 0.19 {#bug_in_version_0.19}

In FreeCAD version 0.19 this command and the [Draft ToggleConstructionMode](Draft_ToggleConstructionMode.md) command will typically use different groups. To avoid this change the {{MenuCommand|Construction group name}} in the preferences to {{Value|Draft_Construction}}: {{MenuCommand|Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name}}. In version 0.20 the {{MenuCommand|Construction group name}} is used for the label of the construction group, the name of the group is always {{Value|Draft_Construction}}.


<div class="mw-translate-fuzzy">

## Nasıl kullanılır {#nasıl_kullanılır}


</div>


<div class="mw-translate-fuzzy">

1.  Bir kaç nesne seçin.
2.  Menüden {{MenuCommand|Taslak → Araçlar → <img src="images/Draft_ToggleConstructionMode.png" width=16px> [İnşa grubuna ekle](Draft_AddConstruction/tr.md)}}yi seçin.


</div>

## Notes


<div class="mw-translate-fuzzy">

Nesneleri [Grup](Std_Group/tr.md) veya [Draft VisGroup](Draft_VisGroup.md) \'a eklemek için [Gruba ekle](Draft_AddToGroup/tr.md) komutunu kullanın.


</div>


<div class="mw-translate-fuzzy">





</div>


 
