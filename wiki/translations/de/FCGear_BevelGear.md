---
- GuiCommand:
   Name:FCGear BevelGear
   Name/de:FCGear Kegelrad
   MenuLocation:Gear - Bevel Gear
   Workbenches:[FCGear](FCGear_Workbench/de.md)
   Version:v0.16
---

# FCGear BevelGear/de

## Beschreibung

Unter anderem wegen der Geräuschentwicklung werden Kegelzahnräder nicht so häufig eingesetzt wie andere Getriebearten. Sie werden aber immer noch in bestimmten Bereichen eingesetzt, z. B. bei Nahrungsmittelverpackung und Lebensmittelkonserven, Grünflächen- und Gartengeräten, Maschinen wie Bohrmaschinen und Fräsen, Verdichtersysteme für den Gas- und Ölmarkt und Durchflußregelventilen.

Spiralförmige Kegelräder haben gekrümmte Zähne, die im Vergleich zu geraden Kegelrädern einen weicheren Eingriff und einen größeren Zahn zu Zahn Kontakt ermöglichen. Dadurch werden Vibrationen und Geräusche reduziert. Sie können bei hohen Geschwindigkeiten eingesetzt werden und werden normalerweise in Motorrad- und Fahrradgetrieben verwendet.

![](images/Bevel-Gear_example.png ) 
*Von links nach rechts: Geradverzahnung, Spiralverzahnung*

## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/de.md) wechseln.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/FCGear_BevelGear.svg style="width:16px"> [Bevel Gear](FCGear_BevelGear/de.md)** drücken.
    -   Den Menüeintrag **Gear → [<img src=images/FCGear_BevelGear.svg style="width:16px"> Bevel Gear** auswählen.
3.  Die Einstellungen den geforderten Randbedingungen entsprechend ändern (siehe [Eigenschaften](#Eigenschaften.md)).

## Eigenschaften

Ein FCGear-BevelGear-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title|base}}

-    **height|Length**: Default is {{Value|5}}. Value for the bevel gear width.

-    **module|Length**: Default is {{Value|1}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).

-    **reset_origin|Bool**: If {{True}} (default) the center of the axis is at the center of the bottom of the gear (see [Notes](#Notes.md)).

-    **teeth|Integer**: Default is {{Value|15}}. Number of teeth.


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (read-only)

-    **dw|Length**: (read-only) Working pitch diameter.


{{Properties_Title|helical}}

-    **beta|Angle**: Default is {{Value|0 °}}. With the helix angle β a helical bevel gear is created -- positive value → rotation direction right, negative value → rotation direction left.


{{Properties_Title|involute}}

-    **pitch_angle|Angle**: Default is {{Value|45 °}}. Angle of taper.


{{Properties_Title|involute_parameter}}

-    **pressure_angle|Angle**: Default is {{Value|20 °}} (see [Notes](#Notes.md)).


{{Properties_Title|precision}}

-    **numpoints|Integer**: Default is {{Value|6}}. Change of the involute profile. Changing the value can lead to unexpected results.


{{Properties_Title|tolerance}}

-    **backlash|Length**: Default is {{Value|0}}. Backlash, also called lash or play, is the distance between the teeth at a gear pair.

-    **clearance|Float**: Default is {{Value|0.1}} (see [Notes](#Notes.md)).


{{Properties_Title|version}}

-    {{PropertyData/de|version|String}}:

## Hinweise

-    **clearance**: At a gear pair, clearance is the distance between the tooth tip of the first gear and the tooth root of the second gear.

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

-    **reset_origin**: It can be advantageous for mounting purposes if the parameter is set to **false**. The origin of the body is then at the tip of the pitch cone.

-    **pressure_parameter**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

## Nützliche Formeln 

-    **Teilkreisdurchmesser**= **Modul** \* **Zähne**

-    **Kopfkreisdurchmesser**= **Teilkreisdurchmesser** + 2 \* **Modul** \* **cos Bezugskonuswinkel**

-    **Kopfwinkel 1**= **(Zähne 1 + 2)** \* **(cos Referenzkegelwinkel 1)** : **(Zähne 2 - 2)** \* **(sin Referenzkegelwinkel 1)**

-    **Kopfwinkel 2**= **(Zähne 2 + 2)** \* **(cos Referenzkegelwinkel 2)** : **(Zähne 1 - 2)** \* **(sin Referenzkegelwinkel 2)**

-    **Referenz-Kegelwinkel 1**= **(Zähne 1)** : **(Zähne 2)**

-    **Referenz-Kegelwinkel 2**= **(Zähne 2)** : **(Zähne 1)**

-    **Achswinkel gesamt**= **Referenz-Kegelwinkel 1** + **Referenz-Kegelwinkel 2**

Substantiv Referenz-Kegelwinkel \[TECH.\]



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear BevelGear/de
