---
- GuiCommand:
   Name: FCGear InternalInvoluteGear
   Name/de: FCGear InnenverzahntesEvolventenzahnrad
   MenuLocation: Gear -> Internal Involute Gear
   Workbenches: FCGear_Workbench/de
   Shortcut: Kein
   Version: 1.0
   SeeAlso: FCGear_InvoluteGear/de
---

# FCGear InternalInvoluteGear/de

## Beschreibung

<img alt="" src=images/FCGear_InternalInvoluteGear-01.png  style="width:300px;">



*Von links nach rechts: Hohlräder mit Geradverzahnung, Schrägverzahnung, Pfeilverzahnung*

## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/de.md) wechseln.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/FCGear_InternalInvoluteGear.svg style="width:16px"> [Internal Involute Gear](FCGear_InternalInvoluteGear/de.md)** drücken.
    -   Den Menüeintrag **Gear → [<img src=images/FCGear_InternalInvoluteGear.svg style="width:16px"> Internal Involute Gear** auswählen.
3.  Die Einstellungen den geforderten Randbedingungen entsprechend ändern (siehe [Eigenschaften](#Eigenschaften.md)).

## Eigenschaften

Ein FCGear-InternalInvoluteGear-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title|accuracy}}

-    {{PropertyData/de|numpoints|Integer}}: Standardwert ist {{value|6}}. Ändert das Evolventenprofil. Das Ändern des Wertes kann zu unerwarteten Ergebnissen führen.


{{Properties_Title/de|Basis}}

-    **height|Length**: Default is {{value|5 mm}}. Value of the gear width.

-    **module|Length**: Default is {{value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **teeth|Integer**: Default is {{value|15}}. Number of teeth (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **thickness|Length**: Default is {{value|5 mm}}. Thickness of the uncut outer part of the gear.


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (read-only)

-    **da|Length**: (read-only) Inside diameter, measured at the addendum (the tip of the teeth).

-    **df|Length**: (read-only) Root diameter, measured at the foot of the teeth.

-    **dw|Length**: (read-only) Working pitch diameter.

-    **outside_diameter|Length**: (read-only) Outside diameter.

-    **transverse_pitch|Length**: (read-only) Pitch in the plane of rotation.


{{Properties_Title|fillets}}

-    **head_fillet|Float**: Default is {{value|0 mm}}.

-    **root_fillet|Float**: Default is {{value|0 mm}}.


{{Properties_Title|helical}}

-    **beta|Angle**: Default is {{value|0 °}}. With the helix angle β a helical gear is created -- positive value → rotation direction right, negative value → rotation direction left (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **double_helix|Bool**: Default is {{false}}, {{true}} creates a double helix gear (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **properties_from_tool|Bool**: Default is {{false}}. If {{true}} and **beta** is not zero, gear parameters are recomputed internally for the rotated gear.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Default is {{value|20 °}} (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **shift|Float**: Default is {{value|0}}. Generates a positive and negative profile shift (see [Notes](FCGear_InvoluteGear#Notes.md)).


{{Properties_Title|precision}}

-    **simple|Bool**: Standardwert ist {{false}}. {{true}} erzeugt eine vereinfachte Ansicht (ohne Zähne und mit nur einem Zylinder mit Teilkreisdurchmesser).


{{Properties_Title|tolerance}}

-    **backlash|Length**: Default is {{value|0 mm}}. Backlash, also called lash or play, is the distance between the teeth at a gear pair.

-    **clearance|Float**: Default is {{value|0.25}} (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **head|Float**: Default is {{value|-0.4 mm}}. This value is used to change the tooth height.

-    **reversed_backlash|Bool**: {{true}} backlash decrease or {{false}} (default) backlash increase (see [Notes](FCGear_InvoluteGear#Notes.md)).


{{Properties_Title|version}}

-    **version|String**:

## Hinweise

Siehe [FCGear Evolventenzahnrad](FCGear_InvoluteGear/de#Hinweise.md).

## Nützliche Formeln 

Siehe [FCGear Evolventenzahnrad](FCGear_InvoluteGear/de#Hilfreiche_Formeln.md).

## Skripten



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InternalInvoluteGear/de
