---
- GuiCommand:/de
   Name:FCGear BevelGear
   Name/de:FCGetriebe KegelradGetriebe
   MenuLocation:FCGetriebe → Erstelle ein KegelradGetriebe
   Workbenches:[FCGetriebe](FCGear_Workbench/de.md)
   Version:v0.16
---

# FCGear BevelGear/de

## Beschreibung

Unter anderem wegen der Geräuschentwicklung werden Kegelzahnräder nicht so häufig eingesetzt wie andere Getriebearten. Sie werden aber immer noch in bestimmten Bereichen eingesetzt, z. B. bei Nahrungsmittelverpackung und Lebensmittelkonserven, Grünflächen- und Gartengeräten, Maschinen wie Bohrmaschinen und Fräsen, Verdichtersysteme für den Gas- und Ölmarkt und Durchflußregelventilen.

Spiralförmige Kegelräder haben gekrümmte Zähne, die im Vergleich zu geraden Kegelrädern einen weicheren Eingriff und einen größeren Zahn zu Zahn Kontakt ermöglichen. Dadurch werden Vibrationen und Geräusche reduziert. Sie können bei hohen Geschwindigkeiten eingesetzt werden und werden normalerweise in Motorrad- und Fahrradgetrieben verwendet.

![](images/Bevel-Gear_example.png )


<div class="mw-translate-fuzzy">


:   ![](images/Bevel-Gear_example.png )
:   
    
*Von links nach rechts: Geradverzahnung, Spiralverzahnung*
    


</div>

## Anwendung

1.  Wechsle zur <img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [FCZahnrad Arbeitsbereich](FCGear_Workbench/de.md).
2.  Rufe den Befehl auf verschiedene Weise auf:
    -   Drücke die <img alt="" src=images/FCGear_BevelGear.svg  style="width:22px;"> [Erstellen eines Kegelzahnrads](FCGear_BevelGear/de.md) in der Werkzeugleiste.
    -   Mit dem **Menü → Kegelradgetriebe**.
3.  Ändere die Zahnradparameter auf die gewünschten Bedingungen (siehe **Eigenschaften → Daten** unten).

## Eigenschaften

### Daten


{{Properties_Title|Basis}}

-    **Placement**: [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**: User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|gear_parameter}}

-    **beta**: With the angle β a helical bevel gear is created (positive value → rotation direction right, negative value → rotation direction left).


{{Properties_Title|gear_parameter}}

-    **backslash**: Default is 0,00. Backlash, also called lash or play, is the distance between the teeths at a gear pair.

-    **clearance**: Default is 0,10 (see also the information in **Note**).

-    **height**: Value for the bevel gear width.

-    **m**: Module is the ratio of the reference diameter of the gear divided by the number of teeth (see also the information in **Note**).

-    **numpoints**: Default is 6, change of the involute profile. Changing the value can lead to unexpected results.

-    **reset_origin**: If the value is **True**, the center of the axis is at the center of the bottom of the gear (see also the information in **Note**).

-    **teeth**: Number of teeth.


{{Properties_Title|involute_parameter}}

-    **pitch_angle**: Angle of taper.

-    **pressure_parameter**: Default is 20 (see also the information in **Note**).

### Ansicht

The parameter descriptions of the **View** tab will be found in [Property editor](Property_editor.md), further below at **Example of the properties of a PartDesign object**.

## Hinweise

-    **clearance**: At a gear pair, clearance is the distance between the tooth tip of the first gear and the tooth root of the second gear.

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

-    **reset_origin**: It can be advantageous for mounting purposes if the parameter is set to **false**. The origin of the body is then at the tip of the pitch cone.

-    **pressure_parameter**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

## Hilfreiche Formeln 

-    **Teilkreisdurchmesser**= **Modul** \* **Zähne**

-    **Kopfkreisdurchmesser**= **Teilkreisdurchmesser** + 2 \* **Modul** \* **cos Bezugskonuswinkel**

-    **Kopfwinkel 1**= **(Zähne 1 + 2)** \* **(cos Referenzkegelwinkel 1)** : **(Zähne 2 - 2)** \* **(sin Referenzkegelwinkel 1)**

-    **Kopfwinkel 2**= **(Zähne 2 + 2)** \* **(cos Referenzkegelwinkel 2)** : **(Zähne 1 - 2)** \* **(sin Referenzkegelwinkel 2)**

-    **Referenz-Kegelwinkel 1**= **(Zähne 1)** : **(Zähne 2)**

-    **Referenz-Kegelwinkel 2**= **(Zähne 2)** : **(Zähne 1)**

-    **Achswinkel gesamt**= **Referenz-Kegelwinkel 1** + **Referenz-Kegelwinkel 2**


<div class="mw-translate-fuzzy">

Substantiv Referenz Kegelwinkel \[TECH.\]


</div>


<div class="mw-translate-fuzzy">





</div>

_ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > FCGear BevelGear/de
