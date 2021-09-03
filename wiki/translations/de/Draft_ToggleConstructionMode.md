---
- GuiCommand:/de
   Name:Draft ToggleConstructionMode
   MenuLocation:Draft → Hilfsmittel → Umschalten des Konstruktionsmodus
   Workbenches:[Draft](Draft_Module/de.md), [Arch](Arch_Module/de.md)
   SeeAlso:[[Draft AddConstruction]]
---


</div>

## Description


<div class="mw-translate-fuzzy">

## Beschreibung

== Der [Draft Arbeitsbereich](Draft_Arbeitsbereich.md) verfügt über einen Konstruktionsmodus, der es dem Benutzer ermöglicht, Formen in einer speziellen [Std Group/de](Std_Group/de.md) mit einer definierten Farbe zu zeichnen. Die Konstruktionsgeometrie besteht aus Linien, Punkten und anderen Formen, die als Referenzen oder Fangelemente dienen, die beim Erstellen Ihrer Hauptgeometrie hilfreich sind. Die Konstruktionsgeometrie kann ausgeblendet (**Visibility** `False`) oder gelöscht werden, nachdem sie nicht mehr benötigt wird.


</div>

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


*Konstruktionsgeometrie in blau hilft bei der Festlegung des Kreismittelpunktes*


</div>

## Bug in version 0.19 

In FreeCAD version 0.19 this command and the [Draft AddConstruction](Draft_AddConstruction.md) command will typically use different groups. To avoid this change the **Construction group name** in the preferences to {{Value|Draft_Construction}}: **Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name**. In version 0.20 the **Construction group name** is used for the label of the construction group, the name of the group is always {{Value|Draft_Construction}}.

## Usage


<div class="mw-translate-fuzzy">

## Anwendung

1.  Drücke die **<img src="images/Draft_ToggleConstructionMode.png" width=16px> [Toggle construction mode](Draft_ToggleConstructionMode.md)** Taste
2.  Zeichne einige Objekte.
3.  Drücke die **<img src="images/Draft_ToggleConstructionMode.png" width=16px> [Toggle construction mode](Draft_ToggleConstructionMode.md)** Taste erneut, um in den Normalmodus zurückzukehren.


</div>

## Notes

-   If Draft construction mode is switched on the active [layer](Draft_Layer.md) is ignored.

## Preferences

-   To change the label (<small>(v0.20)</small> ) of the construction group: **Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name**.
-   To change the color that is used: **Edit → Preferences... → Draft → General settings → Construction Geometry → Construction geometry color**.


<div class="mw-translate-fuzzy">





</div>


 
