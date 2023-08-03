---
 GuiCommand:
   Name: FCGear CrownGear
   Name/de: FCGear Kronenrad
   MenuLocation: Gear , Crown Gear
   Workbenches: FCGear_Workbench/de
   Shortcut: None
   Version: v0.16
   SeeAlso: FCGear_InvoluteGear/de
---

# FCGear CrownGear/de



## Beschreibung

Das Kronenerad ähnelt einer ringförmig gebogenen Zahnstange. Der Eingriffswinkel verringert sich kontinuierlich vom äußeren bis zum inneren Durchmesser. Damit wird die variable Umfangsgeschwindigkeit am Kronenrad zur konstanten Umfangsgeschwindigkeit des Ritzels ausgeglichen. Die spitzen Zahnaußenseiten und die steilen Zahnflanken am Innendurchmesser begrenzen die nutzbare Zahnbreite. Kronenräder sind ähnlich leistungsfähig wie Stirnräder. Ein Kronenrad kann mehrere Ritzel antreiben.

Bekannte Anwendungsgebiete von Kronenrädern:

-   Rear axle drives for cars and motorcycles
-   Swivel mechanism for operating tables
-   Angular milling heads
-   Powered tool systems with multiple pinions and a crown gear

![](images/Crown-Gear_example.png ) 
*Oben: Kronenrad*



## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/de.md) wechseln.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/FCGear_CrownGear.svg style="width:16px"> [Crown Gear](FCGear_CrownGear/de.md)** drücken.
    -   Den Menüeintrag **Gear → [<img src=images/FCGear_CrownGear.svg style="width:16px"> Crown Gear** auswählen.
3.  Das Kronenrad wird standardmäßig ohne Zähne dargestellt. ({{Version/de|0.21}})
4.  Die Einstellungen den geforderten Randbedingungen entsprechend ändern (siehe [Eigenschaften](#Eigenschaften.md)).
5.  Die {{PropertyData/de|preview_mode}} auf {{false}} setzen, um die Zähne darzustellen(see [Hinweise](#Hinweise.md)).



## Eigenschaften

Ein FCGear-CrownGear-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title|accuracy}}

-    **num_profiles|Integer**: Default is {{Value|4}}. Number of profiles used for loft.

-    **preview_mode|Bool**: Default is {{True}}.


{{Properties_Title|base}}

-    **height|Length**: Default is {{Value|2 mm}}. Value for the tooth width.

-    **module|Length**: Default is {{Value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).

-    **other_teeth|Integer**: Default is {{Value|15}}. Number of teeth of the construction gear (pinion) (see [Notes](#Notes.md)).

-    **teeth|Integer**: Default is {{Value|15}}. Number of teeth.

-    **thickness|Length**: Default is {{Value|5 mm}}. Height from the tip of tooth to the lower side of the crown wheel.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Default is {{Value|20 °}} (see [Notes](#Notes.md)).


{{Properties_Title|version}}

-    {{PropertyData/de|version|String}}:



## Hinweise

-   The **preview_mode** property is set to {{true}} by default and when the gear is created you\'ll find this message in the report view:

    :   *Gear module: Crown gear created, preview_mode = true for improved performance. Set preview_mode property to false when ready to cut teeth.*

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

-    **other_teeth**: Several pinions with the same number of teeth only can be used on one crown wheel.

-    **pressure_parameter**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

-   The geometry of the crown gear is primarily determined by the spur pinion geometry (**other_teeth**).

-   Create spur gear with [Involute gear](FCGear_InvoluteGear.md). The number of teeth must be identical to the parameter **other_teeth** of the crown gear.

-   Adjustments for optimal running characteristics can be made with the parameters of involute gear.



## Kronenrad-Stirnrad-Paarung im Überblick 

![](images/Crown-spur-gear-set_example.png )

-   \(1\) Stirnrad
-   \(2\) Kronenrad
-   \(3\) Zahnbreite
-   \(4\) Innendurchmesser
-   \(5\) Außendurchmesser



## Nützliche Formeln 

-   **Inner diameter (4)**
    -   
        **inner diamter**
        
        = **module (spur gear)** \* **teeth (crown gear)** \* **cos pressure_paramter (pinion)** : **cos pressure_parameter (crown gear)**

-   **Outer diameter (5)**
    -   
        **outer diamter**
        
        = **inner diameter** + **2x height (tooth width crown gear)**



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear CrownGear/de
