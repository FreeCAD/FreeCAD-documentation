---
 GuiCommand:
   Name: Draft ToggleConstructionMode
   Name/de: Draft KonstruktionsmodusUmschalten
   MenuLocation: Dienstprogramme , Konstruktionsmodus umschalten
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   SeeAlso: Draft AddConstruction/de
---

# Draft ToggleConstructionMode/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> **Draft KonstruktionsmodusUmschalten** schaltet den Draft Konstruktionsmodus ein oder aus. Falls der Konstruktionsmodus eingeschaltet ist, werden neue [Draft](Draft_Workbench/de.md)-Objekte, außer [Draft Punkten](Draft_Point/de.md) einer bestimmen Gruppe zugeordnet und erhalten eine vordefinierte Farbe. Diese Möglichkeit ist für - oftmals temporäre - Hilfsgeometrie gedacht, um für die Erzeugung weiterer Objekte neue [Einrastpunkte](Draft_Snap/de.md) bereitzustellen. Wenn die Hilfsgeometrie nicht länger benötigt wird, kann die Konstruktionsgruppe einfach [ausgeblendet](Std_HideSelection/de.md) oder [gelöscht](Std_Delete/de.md) werden.

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;"> 
*Hilfsgeometrie, in blau, hilft bei der Festlegung von Mittelpunkt und Radius eines Kreises*



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_ToggleConstructionMode.svg" width=16px> [Konstruktionsmodus umschalten](Draft_ToggleConstructionMode/de.md)** in der [Draft Ablage](Draft_Tray/de.md). Diese Schaltfläche ist heruntergedrückt, wenn der Konstruktionsmodus gerade eingeschaltet ist.
    -   Den Menüeintrag **Dienstprogramme → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Konstruktionsmodus umschalten** auswählen.
    -   Das Tastaturkürzel **C** dann **M**.
2.  Die Schaltfläche in der [Draft Ablage](Draft_Tray/de.md) wird aktualisiert.



## Hinweise

-   Falls der Draft Konstruktionsmodus eingeschaltet ist, wird die aktive [Ebene](Draft_Layer/de.md) ignoriert.



## Einstellungen

-   Zur Änderung der Bezeichnung der Hilfsgeometriegruppe: **Bearbeiten → Einstellungen... → Draft → Allgemein →  Benennung der Hilfsgeometriegruppen**.
-   Zur Änderung der zu verwendenden Farbe: **Bearbeiten → Einstellungen... → Draft → Allgemein → Farbe der Hilfsgeometrie**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleConstructionMode/de
