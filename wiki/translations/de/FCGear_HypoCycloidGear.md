---
- GuiCommand:
   Name: FCGear HypoCycloidGear
   Name/de: FCGear Hypozykloidenrad
   MenuLocation: Gear -> HypoCycloid Gear
   Workbenches: FCGear_Workbench/de
   Shortcut: Kein
   Version: 1.0
   SeeAlso: 
---

# FCGear HypoCycloidGear/de

## Beschreibung

The <img alt="" src=images/FCGear_HypoCycloidGear.svg  style="width:16px;"> **FCGear HypoCycloid Gear** command creates two splined cam disks and a set of rollers that stay in touch with the disks\' outer surfaces while moving.

<img alt="" src=images/FCGear_FCGear_HypoCycloidGear-04.png  style="width:200px;"> <img alt="" src=images/FCGear_FCGear_HypoCycloidGear-05.png  style="width:200px;"> 
*Left: Hypocycloid gear. Right: Gear and transparently displayed also provided reversed gear and set of rollers*

Please provide a short description what can be achieved using such a gear train.

## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/de.md) wechseln.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/FCGear_HypoCycloidGear.svg style="width:16px"> [HypoCycloid Gear](FCGear_HypoCycloidGear.md)** drücken.
    -   Den Menüeintrag**Gear → [<img src=images/FCGear_HypoCycloidGear.svg style="width:16px"> HypoCycloid Gear** auswählen.
3.  Die Einstellungen den geforderten Randbedingungen entsprechend ändern (siehe [Eigenschaften](#Eigenschaften.md)).

## Eigenschaften

## Hinweise

The default gear(s) are displayed like this:

<img alt="" src=images/FCGear_FCGear_HypoCycloidGear-01.png  style="width:200px;">

To display the cam disks and the set of rollers (pins) in different colours, we need three identical HypocycloidGear objects. Their visibility can be toggled:

-    **show_disk0|Bool**for the main cam disk.

-    **show_disk1|Bool**for a reversed cam disk on top.

-    **show_pins|Bool**for the set of pins.

<img alt="" src=images/FCGear_FCGear_HypoCycloidGear-02.png  style="width:200px;"> <img alt="" src=images/FCGear_FCGear_HypoCycloidGear-03.png  style="width:200px;"> 
*Left: HypocycloidGear objects as created. Right: Objects repositioned to get a better view on each object*

## Skripten



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear HypoCycloidGear/de
