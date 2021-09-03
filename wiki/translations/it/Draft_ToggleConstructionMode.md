---
- GuiCommand:/it
   Name:Draft ToggleConstructionMode
   Name/it:Costruzione
   MenuLocation:Draft → Utilità → Costruzione
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   Shortcut:**C** **M**
   SeeAlso:[Aggiungi al gruppo Costruzione](Draft_AddConstruction/it.md)
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

L\'[Ambiente Draft](Draft_Workbench/it.md) <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> presenta una modalità di costruzione, che consente all\'utente di disegnare forme in uno speciale [Gruppo](Std_Group/it.md), con un colore definito. La geometria di costruzione è composta da linee, punti e altre forme che fungono da riferimenti o [elementi di aggancio](Draft_Snap/it.md) che sono utili per costruire la geometria principale. La geometria della costruzione può essere nascosta (**Visibility** `False`) o cancellata dopo che non è più necessaria.


</div>

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


*Geometria di costruzione in blu che aiuta a impostare il centro del cerchio*


</div>

## Bug in version 0.19 {#bug_in_version_0.19}

In FreeCAD version 0.19 this command and the [Draft AddConstruction](Draft_AddConstruction.md) command will typically use different groups. To avoid this change the {{MenuCommand|Construction group name}} in the preferences to {{Value|Draft_Construction}}: {{MenuCommand|Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name}}. In version 0.20 the {{MenuCommand|Construction group name}} is used for the label of the construction group, the name of the group is always {{Value|Draft_Construction}}.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_ToggleConstructionMode.png" width=16px> [Attiva/disattiva modalità di costruzione](Draft_ToggleConstructionMode/it.md)**.
2.  Disegnare alcuni oggetti.
3.  Premere di nuovo il pulsante **<img src="images/Draft_ToggleConstructionMode.png" width=16px> [Attiva/disattiva modalità di costruzione](Draft_ToggleConstructionMode/it.md)** per tornare alla modalità normale.


</div>

## Notes

-   If Draft construction mode is switched on the active [layer](Draft_Layer.md) is ignored.

## Preferences

-   To change the label (<small>(v0.20)</small> ) of the construction group: {{MenuCommand|Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name}}.
-   To change the color that is used: {{MenuCommand|Edit → Preferences... → Draft → General settings → Construction Geometry → Construction geometry color}}.


<div class="mw-translate-fuzzy">





</div>


 
