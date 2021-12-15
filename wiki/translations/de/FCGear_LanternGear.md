---
- GuiCommand:/de
   Name:FCGear LanternGear
   Name/de:FCZahnrad TriebstockZahnrad
   MenuLocation:FCZahnrad → Erstelle ein Triebstock Zahnrad
   Workbenches:[FCZahnrad](FCGear_Workbench/de.md)
   Shortcut:Keine
   Version:v0.16
   SeeAlso:
---

# FCGear LanternGear/de

## Beschreibung

Die Triebstockverzahnung ist eine Sonderform der Zykloidenverzahnung, bei der Wälzkreis und Teilkreis gleich groß sind. Außerdem werden die Zähne des größeren Rades in einem Getriebe durch Zylinder ersetzt. Das kleine Rad erhält eine Zykloidenverzahnung. Daraus ergibt sich eine einseitige Punktverzahnung. Triebstockverzahnungen können nur gerade verzahnt sein.

Da sie sehr einfach aufgebaut sind, gehören sie zu den ältesten Formen von Getrieben. Triebstockgetriebe werden eingesetzt, wenn große Übersetzungsverhältnisse erforderlich sind, z. B. in Drehwerken von Mühlen oder Holzumschlagskränen.

Triebstockräder mit Rollenketten sind eine kostengünstige und robuste Alternative zu Zahnstangen- und Ritzelantrieben. Durch die tangentiale Führung der gespannten Triebstockkette entlang des Triebstocks wird eine lineare Bewegung der Kette in eine Drehbewegung des Rades umgesetzt. Umgekehrt kann eine lineare Bewegung der Kette auch durch die Drehbewegung des Triebstockrades (Motorrad/Fahrrad) erreicht werden.

![](images/Latern_Gear_example.png )


<div class="mw-translate-fuzzy">


:   ![](images/Latern_Gear_example.png )
:   
    
*Oben: Triebstockzahnrad*
    


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wechsle zur <img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [Arbeitsbereich FCZahnrad](FCGear_Workbench/de.md).
2.  Rufe den Befehl auf verschiedene Weise auf:
    -   Drücke die <img alt="" src=images/FCGear_LanternGear.svg  style="width:22px;"> [TriebstockZahnrad erstellen](FCGear_LanternGear/de.md) Schaltfläche in der Werkzeugleiste.
    -   Mit dem **Zahnradmenü → Triebstock Zahnrad**.
3.  Ändere die Zahnrad Parameter auf die gewünschten Bedingungen (siehe **Eigenschaften → Daten** unten).


</div>

## Eigenschaften

### Daten


{{Properties_Title|Base}}

-    **Placement**: [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**: User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|accuracy}}

-    **num_profiles**: Default is 10. The value normally does not need to be changed.


{{Properties_Title|gear_parameter}}

-    **bolt_radius**: Default is 1,00 mm. Diameter of the cylinder on the rotating disc which functions as a second \"gear wheel\".

-    **height**: Default is 5,00 mm. Value of the gear width.

-    **module**: Default is 1,00 mm. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see also the information in **Notes**.

-    **teeth**: Default is 15. Number of teeth.

### Ansicht

The parameter descriptions of the **View** tab will be found in [Property editor](Property_editor.md), further below at **Example of the properties of a PartDesign object**.

## Hinweise

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

## Begrenzungen

Begrenzungen sind noch nicht bekannt.

## Hilfreiche Formeln 

-    **addendum diameter**= **module** \* **(teeth +2)**

-    **ptch diameter**= **module** \* **teeth**

-    **axle base**= **pitch diameter (lantern gear 1 + 2)** : 2


<div class="mw-translate-fuzzy">





</div>

_ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > FCGear LanternGear/de
