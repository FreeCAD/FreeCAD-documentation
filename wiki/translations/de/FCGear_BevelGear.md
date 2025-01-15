---
 GuiCommand:
   Name: FCGear BevelGear
   Name/de: FCGear Kegelrad
   MenuLocation: Gear , Bevel Gear
   Workbenches: FCGear_Workbench/de
   Version: v0.16
---

# FCGear BevelGear/de



## Beschreibung

The <img alt="" src=images/FCGear_BevelGear.svg  style="width:24px;"> [FCGear BevelGear](FCGear_BevelGear.md) tool creates a basic bevel gear, a solid object that needs to be trimmed to the correct final shape in following steps.

Unter anderem wegen der Geräuschentwicklung werden Kegelzahnräder nicht so häufig eingesetzt wie andere Getriebearten. Sie werden aber immer noch in bestimmten Bereichen eingesetzt, z. B. bei Nahrungsmittelverpackung und Lebensmittelkonserven, Grünflächen- und Gartengeräten, Maschinen wie Bohrmaschinen und Fräsen, Verdichtersysteme für den Gas- und Ölmarkt und Durchflußregelventilen.

Spiralförmige Kegelräder haben gekrümmte Zähne, die im Vergleich zu geraden Kegelrädern einen weicheren Eingriff und einen größeren Zahn zu Zahn Kontakt ermöglichen. Dadurch werden Vibrationen und Geräusche reduziert. Sie können bei hohen Geschwindigkeiten eingesetzt werden und werden normalerweise in Motorrad- und Fahrradgetrieben verwendet.

![](images/Bevel-Gear_example.png ) 
*Von links nach rechts: Geradverzahnung, Spiralverzahnung*



## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/de.md) wechseln.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/FCGear_BevelGear.svg style="width:16px"> [Bevel Gear](FCGear_BevelGear/de.md)** drücken.
    -   Den Menüeintrag **Gear → [<img src=images/FCGear_BevelGear.svg style="width:16px"> Bevel Gear** auswählen.
3.  Ein Kegelrad (BevelGear-Objekt) wird den Standardeinstellungen entsprechend erstellt.
4.  Die Einstellungen den geforderten Randbedingungen entsprechend ändern (siehe [Eigenschaften](#Eigenschaften.md)).



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein FCGear-BevelGear-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title|base}}

-    **height|Length**: Default is {{Value|5}}. Value of the bevel gear width, measured from the pitch circle.

-    **module|Length**: Default is {{Value|1}}. Module is the ratio of the pitch diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).

-    **reset_origin|Bool**: If {{True}} (default) the origin of the gear is at the center of the pitch circle (bottom of the gear) (see [Notes](#Notes.md)).

    :   If {{False}} the origin of the gear is at the tip of the pitch cone.

-    **teeth|Integer**: Default is {{Value|15}}. Number of teeth.


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (read-only)

-    **dw|Length**: (read-only) Working pitch diameter.


{{Properties_Title|helical}}

-    **beta|Angle**: Default is {{Value|0 °}}. With the helix angle β a helical bevel gear is created -- positive value → rotation direction right, negative value → rotation direction left.


{{Properties_Title|involute}}

-    **pitch_angle|Angle**: Default is {{Value|45 °}}. Taper angle of the pitch cone.


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

-   Bevel gears are quite complex, because their properties not only depend on the gear ratio but also on the angle between the gear axes. The default bevel gear is built for perpendicular axes and a 1:1 ratio.

-    **pitch angle**: The taper angle of the pitch cone is half the angle between gear axes for a 1:1 ratio, that is 45° for perpendicular axes. Pitch angles for other combinations of ratio and angles between axes can be determined geometrically within a [sketch](Sketcher_Workbench.md).

-    **clearance**: At a gear pair, clearance is the distance between the tooth tip of the first gear and the tooth root of the second gear.

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

-    **pressure_angle**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

-    **reset_origin**: It is recommended to set the parameter to **false** to have the origin of the gear at the tip of the pitch cone. This way we can extend the bevel gear beyond the pitch circle plane using the module property.

-   The weak point of this tool is that it builds the geometry from the pitch diameter towards the tip and ignores the fact that there is also geometry in the opposite direction. That is why we have to determine the cross-section of the gear at the pitch circle belonging to our chosen module to define cutting geometry and then use an extended (scaled from the tip) bevel gear to be cut. (see *reset origin* above)



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
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External%20Command%20Reference.md) > FCGear BevelGear/de
