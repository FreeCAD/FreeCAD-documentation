# <img alt="Symbol Externer Arbeitsbereich FCZahnrad" src=images/FCGear_workbench_icon.svg  style="width:64px;"> FCGear Workbench/de

## Einführung


{{TOCright}}

Die [FCZahnrad Arbeitsbereich](FCGear_Workbench/de.md) ist eine [externer Arbeitsbereich](external_workbenches/de.md) zur Herstellung verschiedener Arten von Zahnrädern und Schneckenrädern in FreeCAD. Durch die parametrische Modellierung können die erforderlichen Geometrien jederzeit geändert werden. Durch Ändern einiger Parameter wird das Evolventenzahnrad beispielsweise entweder zu einem Geradverzahnten, einem Schrägverzahnten- oder einem Pfeilverzahnten Zahnrad.

Damit die Ergebnisse von FC Zahnrad verwendet werden können, ist ein gewisses Grundwissen über die verschiedenen Arten von Verzahnungen erforderlich. Modul, Teilungsdurchmesser oder Fußdurchmesser sind gängige Begriffe und sollten daher bekannt sein.

In Verbindung mit dem 3D Druck haben Heimanwender nun die Möglichkeit, Zahnräder und Schneckenräder nach ihren eigenen Vorstellungen zu konstruieren, herzustellen und gegebenenfalls an die baulichen Gegebenheiten anzupassen.

Bevor [FCZahnrad Arbeitsbereich](FCGear_Workbench/de.md) gestartet werden kann, muss es installiert werden (wie es gemacht wird, siehe unten unter **Installation**). Nach der Installation stehen die Werkzeuge in der Werkzeugleiste zur Verfügung.

:   ![](images/FCGear_Drop-down-menu_example-en.png )
:   
    
*Das FCZahnrad Aufklappmenü*
    

## Zahnradarten

### Evolventenzahnrad

:   ![](images/Involute-Gear_example.png )
:   
    
*Von links nach rechts: Geradverzahnung, Schrägverzahnung, Pfeilverzahnung (siehe [FCZahnrad EvolventenZahnrad](FCGear_InvoluteGear/de.md))*
    

### Evolventen Zahnstange 

:   ![](images/Involute-Rack_example.png )
:   
    
*Von links nach rechts: Geradverzahnung, Schrägverzahnung, Pfeilverzahnung (siehe [FCZahnrad EvolventenZahnstange](FCGear_InvoluteRack/de.md))*
    

### Zykloidenzahnrad

:   ![](images/Cycloid-Gear_example_1.png )
:   
    
*von links nach rechts : Geradverzahnung, Schrägverzahnung, Pfeilverzahnung (siehe [FCZahnrad ZykloidenZahnrad](FCGear_CycloideGear/de.md))*
    

### Kegelzahnrad

:   ![](images/Bevel-Gear_example.png )
:   
    
*Von links nach rechts: Geradeverzahnung, Spiralverzahnung (siehe [FCGetriebe KegelZahnrad](FCGear_BevelGear/de.md))*
    

### Schneckenzahnrad

:   ![](images/Worm-Gear_example.png )
:   
    
*Oben: Schneckenzahnrad (siehe [FCGetriebe SchneckenZahnrad ](FCGear_WormGear/de.md))*
    

### Kronenzahnrad

:   ![](images/Crown-Gear_example.png )
:   
    
*Oben: Kronenzahnrad (siehe [FCGetriebe KronenZahnrad](FCGear_CrownGear/de.md))*
    

### Gleichlaufzahnrad und Triebstockzahnrad 

:   ![](images/Timing+Latern-gear_example.png )
:   
    
*Von links nach rechts: Gleichlaufverzahnung, Triebstockverzahnung (siehe [FCGetriebe GleichlaufZahnrad](FCGear_TimingGear/de.md) oder [FCGear TriebstockZahnrad](FCGear_LanternGear.md))*
    

## Referenzen

-   Autor: looooo
-   Heimseite: <https://github.com/looooo/FCGear>
-   Quellcode auf github: <https://github.com/looooo/FCGear>

## Werkzeuge

### Werkzeugleiste

-   <img alt="" src=images/FCGear_InvoluteGear.svg  style="width:32px;"> [FCZahnrad EvolventenZahnrad](FCGear_InvoluteGear/de.md) Erzeugt ein Evolventenzahnrad
-   <img alt="" src=images/FCGear_InvoluteRack.svg  style="width:32px;"> [FCZahnrad EvolventenZahnstange](FCGear_InvoluteRack/de.md) Erzeugt eine Evolventenzahnstange
-   <img alt="" src=images/FCGear_CycloideGear.svg  style="width:32px;"> [FCZahnrad ZykloidenZahnrad](FCGear_CycloideGear/de.md) Erzeugt ein Zykloidenzahnrad
-   <img alt="" src=images/FCGear_BevelGear.svg  style="width:32px;"> [FCZahnrad KegelZahnrad](FCGear_BevelGear/de.md) Erzeugt ein Kegelzahnrad
-   <img alt="" src=images/FCGear_WormGear.svg  style="width:32px;"> [FCZahnrad SchneckenZahnrad](FCGear_WormGear/de.md) Erzeugt ein Schneckenzahnrad
-   <img alt="" src=images/FCGear_CrownGear.svg  style="width:32px;"> [FCZahnrad KronenZahnrad](FCGear_CrownGear/de.md) Erzeugt ein Kronenzahnrad
-   <img alt="" src=images/FCGear_TimingGear.svg  style="width:32px;"> [FCZahnrad GleichlaufZahnrad](FCGear_TimingGear/de.md) Erzeugt ein Gleichlaufzahnrad
-   <img alt="" src=images/FCGear_LanternGear.svg  style="width:32px;"> [FCZahnrad TriebstockZahnrad](FCGear_LanternGear/de.md) Erzeugt ein Triebstockzahnrad

## Einrichtung

### Automatische Einrichtung 


<div class="mw-translate-fuzzy">

Die empfohlene Installationsmethode ab v0.17 ist über den <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Erweiterungsverwalter](Std_AddonMgr/de.md). Dieser befindet sich im 
**Werkzeuge → Erweiterungsverwalter**


</div>


<div class="mw-collapsible mw-collapsed toccolours" style="width:700px">

### Manuelle Einrichtung 

Sollte es notwendig sein, diesen Arbeitsbereich manuell zu installieren, sind die folgenden Anweisungen dafür vorgesehen:


<div class="mw-collapsible-content">

#### Linux

-    `git clone https://github.com/looooo/FCGear.git`
    

-   verknüpfe oder kopiere den Ordner zu {{FileName|/freecad/Mod}}

:   

    :   
        `sudo ln -s (Pfad_zu_FCGear) (Pfad_zu_Freecad)/Mod`
        

#### Windows

Getestet auf (7/8/8.1/10) (Von GitHub)

-   ZIP-Archiv herunterladen, durch klicken auf die Schaltfläche oben rechts
-   gehe zum FreeCAD-Makro-Ordner (in FreeCAD wähle \"Bearbeiten \> Einstellungen \> Allgemein \> Makro, um den Makro Pfad zu sehen)
-   Wenn du die Standardeinstellungen nicht geändert hast, sollte es \"C:\\Users\\Dein\_Windows\_Benutzername\\AppData\\Roaming\\FreeCAD\" sein
-   \\appdata ist ein HIDDEN Ordner, daher musst Du möglicherweise die Einstellungen des Datei Explorers ändern, um ihn zu sehen
-   Erstellen Sie einen Unterordner namens \"FCGear\".
-   stelle sicher, Dateien und Ordner GENAU wie oben gezeigt in den gerade erstellten Unterordner zu kopieren
-   Starte FreeCAD neu und der Arbeitsbereich sollte im Auswahlmenü erscheinen
-   In FreeCAD kannst Du \"Werkzeuge \> Anpassen \> Arbeitsbereiche\" wählen, um Arbeitsbereiche zu aktivieren/deaktivieren.

#### MacOSX

Siehe Anweisungen für Linux oben


</div>


</div>

## Verweise zum Arbeitsbereich Getriebe 

-   Arbeitsbereichs Wiki: <https://github.com/looooo/FCGear/wiki>
-   FreeCAD Wiki: [Macro\_FCGear](http://www.freecadweb.org/wiki/index.php?title=Macro_FCGear) und [Kegelzahnrad](http://forum.freecadweb.org/viewtopic.php?f=3&t=12878)
-   FreeCAD Forum: <http://forum.freecadweb.org/viewtopic.php?f=21&t=12968>
-   Tutorien:
-   Videos:
-   Dateien:
-   Fehler melden: Bitte melde Fehler unter <https://github.com/looooo/FCGear/issues>

## Andere nützliche Verweise 

-   <img alt="PartDesign\_InvoluteGear" src=images/PartDesign_InvoluteGear.svg  style="width:24px;"> _ aufgefüllt werden.
-   [Externe Arbeitsbereiche](External_workbenches/de.md): Eine Liste aller aktuellen externen Arbeitsbereiche von FreeCAD
-   [Makrorezepte](Macros_recipes/de.md)
-   [Die Zykloidenverzahnung (deutsch)](https://vivat-geo.de/zykloidenverzahnung.html)
-   [Evolventenverzahnung (deutsch)](https://vivat-geo.de/evolventenverzahnung.html)




_ _ _

---
[documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > FCGear Workbench/de
