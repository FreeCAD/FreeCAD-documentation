---
- GuiCommand:/de
   Name:Draft ToggleConstructionMode
   Name/de:Draft UmschaltenKonstruktionsmodus
   MenuLocation:Draft → Utilities → Konstruktionsmodus umschalten
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[Draft ZurKonstruktionsgruppeHinzufügen](Draft_AddConstruction/de.md)
---

## Beschreibung

Der <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> **Draft UmschaltenKonstruktionsmodus**-Befehl schaltet den Draft Konstruktionsmodus ein oder aus. Fall der Konstruktionsmodus eingeschaltet ist, werden neue [Draft](Draft_Workbench/de.md)-Objekte, außer [Draft Punkten](Draft_Point/de.md) in einer dedizierten Gruppe zugeordnet und erhalten eine vordefinierte Farbe. Diese Möglichkeit ist für - oftmals temporäre - Konstruktionsgeometrie gedacht, um für die Erzeugung weiterer Objekte neue [Einrastpunkte](Draft_Snap/de.md) bereitzustellen. Wenn die Konstruktionsgeometrie nicht länger benötigt wird, kann die Konstruktionsgruppe einfach [versteckt](Std_HideSelection/de.md) oder [gelöscht](Std_Delete/de.md) werden.

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;"> 
*Konstruktionsgeometrie, in blau, hilft bei der Festlegung des Mittelpunkts und Radius eines Kreises*

## Fehler in Version 0.19 

In FreeCAD Version 0.19 benutzen dieser und der [Draft ZurKonstruktionsgruppeHinzufügen](Draft_AddConstruction/de.md)-Befehl typischer Weise verschiedene Gruppen. Um dies zu vermeiden, ändere den **Konstruktionsgruppenname**n in den Einstellungen auf {{Value|Draft_Construction}}: **Bearbeiten → Einstellungen... → Draft → Allgemeine Einstellungen → Konstruktionsgeometrie → Konstruktionsgruppenname**. In Version 0.20 wird **Konstruktionsgruppenname** für die Bezeichnung der Konstruktionsgruppe verwendet, der Name der Gruppe ist immer {{Value|Draft_Construction}}.

## Anwendung

1.  Es gibt mehrere Wege, um den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_ToggleConstructionMode.svg" width=16px> [Draft UmschaltenKonstruktionsmodus](Draft_ToggleConstructionMode/de.md)**-Schaltfläche in der [Draft Ablage](Draft_Tray/de.md). Diese Schaltfläche ist heruntergedrückt, wenn der Konstruktionsmodus gerade eingeschaltet ist.
    -   Wähle die **Utilities → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Konstruktionsmodus umschalten**-Option aus dem Menü.
    -   Benutze das Tastaturkürzel: **C**, dann **M**.
2.  Die Schaltfläche in der [Draft Ablage](Draft_Tray/de.md) ist aktualisiert.

## Hinweise

-   Falls der Draft Konstruktionsmodus eingeschaltet ist, wird die aktive [Ebene](Draft_Layer/de.md) ignoriert.

## Einstellungen

-   Zur Änderung der Bezeichnung ({{Version/de|0.20}}) der Konstruktionsgruppe: **Bearbeiten → Einstellungen... → Draft → Allgemeine Einstellungen → Konstruktionsgeometrie → Konstruktionsgruppenname**.
-   Zur Änderung der zu verwendenden Farbe: **Bearbeiten → Einstellungen... → Draft → Allgemeine Einstellungen → Konstruktionsgeometrie → Hilfsgeometriefarbe**.





 
