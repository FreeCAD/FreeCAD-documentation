# <img alt="Symbol des externen Arbeitsbereichs FCGear" src=images/FCGear_workbench_icon.svg  style="width:64px;"> FCGear Workbench/de


{{TOCright}}

## Einleitung

Der Arbeitsbereich **FCGear** ist ein [externer Arbeitsbereich](External_workbenches/de.md) zur Herstellung verschiedener Arten von Zahnrädern und Schneckenwellen in FreeCAD. Durch die parametrische Modellierung können die erforderlichen Geometrien jederzeit geändert werden. Durch Ändern einiger Parameter wird das Evolventenzahnrad beispielsweise entweder zu einem geradverzahnten, einem schrägverzahnten oder einem doppelschrägverzahnten Zahnrad.
(Eine Doppelschrägverzahnung besitzt eine Nut zwischen den beiden Schrägverzahnungen, ohne Nut wird sie Pfeilverzahnung genannt)

Damit die Ergebnisse von FCGear verwendet werden können, ist ein gewisses Grundwissen über die verschiedenen Arten von Verzahnungen erforderlich. Modul, Teilkreisdurchmesser oder Fußkreisdurchmesser sind gängige Begriffe und sollten daher bekannt sein.

In Verbindung mit dem 3D-Druck haben Heimanwender nun die Möglichkeit, Zahnräder und Schneckenwellen nach ihren eigenen Vorstellungen zu konstruieren, herzustellen und gegebenenfalls an die konstruktiven Gegebenheiten anzupassen.

Der Arbeitsbereich FCGear kann mit dem <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr.md) installiert werden. Zur manuellen Installation siehe [Weitere Arbeitsbereiche installieren](Installing_more_workbenches/de.md).

Nach der Installation stehen die Werkzeuge in der Symbolleiste Gear und dem Menü Gear zur Verfügung.

## Werkzeuge

-   <img alt="" src=images/FCGear_InvoluteGear.svg  style="width:32px;"> [Evolventenzahnrad](FCGear_InvoluteGear/de.md): Erstellt ein Stirnrad mit Evolventenverzahnung.

-   <img alt="" src=images/FCGear_InternalInvoluteGear.svg  style="width:32px;"> [InnenverzahntesEvolventenzahnrad](FCGear_InternalInvoluteGear/de.md): Erstellt ein innenverzahntes Evolventenverzahnrad (Hohlrad).

-   <img alt="" src=images/FCGear_InvoluteRack.svg  style="width:32px;"> [Evolventenzahnstange](FCGear_InvoluteRack/de.md): Erstellt eine Zahnstange (für Stirnräder) mit Evolventenverzahnung.

-   <img alt="" src=images/FCGear_CycloidGear.svg  style="width:32px;"> [Zykloidenzahnrad](FCGear_CycloidGear/de.md): Erstellt ein Stirnrad mit Zykloidenverzahnung.

-   <img alt="" src=images/FCGear_CycloidRack.svg  style="width:32px;"> [Zykloidenzahnstange](FCGear_CycloidRack/de.md): Erstellt eine Zahnstange (für Stirnräder) mit Zykloidenverzahnung.

-   <img alt="" src=images/FCGear_BevelGear.svg  style="width:32px;"> [Kegelrad](FCGear_BevelGear/de.md): Erstellt ein Kegelrad.

-   <img alt="" src=images/FCGear_CrownGear.svg  style="width:32px;"> [Kronenrad](FCGear_CrownGear/de.md): Erstellt ein Kronenrad.

-   <img alt="" src=images/FCGear_WormGear.svg  style="width:32px;"> [Schneckenwelle](FCGear_WormGear/de.md): Erstellt eine Schneckenwelle.

-   <img alt="" src=images/FCGear_TimingGear.svg  style="width:32px;"> [Zahnriemenscheibe](FCGear_TimingGear/de.md): Erstellt eine Zahnriemenscheibe.

-   <img alt="" src=images/FCGear_LanternGear.svg  style="width:32px;"> [Triebstockrad](FCGear_LanternGear/de.md): Erstellt ein Triebstockrad.

-   <img alt="" src=images/FCGear_HypoCycloidGear.svg  style="width:32px;"> [Hypozykloidenrad](FCGear_HypoCycloidGear/de.md): Erstellt eine Scheibe mit Hypozykloid-Kontur und die dazugehörigen Rollen (Zapfen).

-   <img alt="" src=images/FCGear_GearConnector.svg  style="width:32px;"> [Zahnradpaarung](FCGear_GearConnector/de.md): Stellt Paare aus zwei verzahnten Elementen zusammen.

## Zahnradarten

### Evolventenzahnrad

<img alt="" src=images/Involute-Gear_example.png  style="width:200px;"> 
*Von links nach rechts: Geradverzahnung, Schrägverzahnung, Doppelschrägverzahnung (siehe [FCGear Evolventenzahnrad](FCGear_InvoluteGear/de.md))*

### Innenverzahntes Evolventenzahnrad 

<img alt="" src=images/FCGear_InternalInvoluteGear-01.png  style="width:200px;"> 
*Von links nach rechts: Geradverzahnung, Schrägverzahnung, Doppelschrägverzahnung (siehe [FCGear InnenverzahntesEvolventenzahnrad](FCGear_InternalInvoluteGear/de.md))*

### Evolventenzahnstange

<img alt="" src=images/Involute-Rack_example.png  style="width:" height="200px;"> 
*Von links nach rechts: Geradverzahnung, Schrägverzahnung, Doppelschrägverzahnung (siehe [FCGear Evolventenzahnstange](FCGear_InvoluteRack/de.md))*

### Zykloidenzahnrad

<img alt="" src=images/Cycloid-Gear_example_1.png  style="width:200px;"> 
*Von links nach rechts: Geradverzahnung, Schrägverzahnung, Doppelschrägverzahnung (siehe [FCGear Zykloidenzahnrad](FCGear_CycloidGear/de.md))*

### Zykloidenzahnstange

<img alt="" src=images/FCGear_CycloidRack-01.png  style="width:" height="200px;"> 
*Von links nach rechts: Geradverzahnung, Schrägverzahnung, Doppelschrägverzahnung (siehe [FCGear Zykloidenzahnstange](FCGear_CycloidRack/de.md))*

### Kegelrad

<img alt="" src=images/Bevel-Gear_example.png  style="width:150px;"> 
*Von links nach rechts: Geradverzahnung, Spiralverzahnung (siehe [FCGear Kegelrad](FCGear_BevelGear/de.md))*

### Kronenrad

<img alt="" src=images/Crown-Gear_example.png  style="width:150px;"> 
*Kronenrad (siehe [FCGear Kronenrad](FCGear_CrownGear/de.md))*

### Schneckenwelle

<img alt="" src=images/Worm-Gear_example.png  style="width:150px;"> 
*Schneckenwelle (siehe [FCGear Schneckenwelle](FCGear_WormGear/de.md))*

### Zahnriemenscheibe

<img alt="" src=images/Timing-Gear_example.png  style="width:150px;"> 
*Zahnriemenscheibe (siehe [FCGear Zahnriemenscheibe](FCGear_TimingGear/de.md))*

### Triebstockrad

<img alt="" src=images/Lantern-Gear_example.png  style="width:150px;"> 
*Triebstockrad (siehe [FCGear Triebstockrad](FCGear_LanternGear/de.md))*

### Hypozykloidenrad

<img alt="" src=images/FCGear_FCGear_HypoCycloidGear-05.png  style="width:120px;"> 
*Hypozykloidenrad (siehe [FCGear Hypozykloidenrad](FCGear_HypoCycloidGear/de.md))*

## Referenzen

-   Autor: looooo
-   Heimseite: <https://github.com/looooo/FCGear>
-   Quellcode auf github: <https://github.com/looooo/FCGear>

## Verweise zum Arbeitsbereich FCGear 

-   FreeCAD-Wiki: [Macro_FCGear](Macro_FCGear/de.md)
-   FreeCAD-Forum: [Bevel gear](http://forum.freecadweb.org/viewtopic.php?f=3&t=12878) und [FCGear](http://forum.freecadweb.org/viewtopic.php?f=21&t=12968)
-   Tutorien:
-   Videos:
-   Dateien:
-   Fehler melden: Bitte melde Fehler unter <https://github.com/looooo/FCGear/issues>

## Andere nützliche Verweise 

-   <img alt="PartDesign_InvoluteGear" src=images/PartDesign_InvoluteGear.svg  style="width:24px;"> [PartDesign Evolventenrad](PartDesign_InvoluteGear/de.md): Dieses Werkzeug ermöglicht die Erstellung eines 2D-Profils eines Evolventenzahnrades. Dieses 2D-Profil ist vollständig parametrisch und kann mit der Funktion [PartDesign Aufpolsterung](PartDesign_Pad/de.md) aufgefüllt werden.
-   [Externe Arbeitsbereiche](External_workbenches/de.md): Eine Liste aller aktuellen externen Arbeitsbereiche von FreeCAD
-   [Makrorezepte](Macros_recipes/de.md)
-   [Die Zykloidenverzahnung (deutsch)](https://vivat-geo.de/zykloidenverzahnung.html)
-   [Evolventenverzahnung (deutsch)](https://vivat-geo.de/evolventenverzahnung.html)



---
![](images/Button_right.svg) [documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > FCGear Workbench/de
