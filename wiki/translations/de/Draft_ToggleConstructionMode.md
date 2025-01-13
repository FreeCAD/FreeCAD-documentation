---
 GuiCommand:
   Name: Draft ToggleConstructionMode
   Name/de: Draft KonstruktionsmodusUmschalten
   MenuLocation: Dienstprogramme , Konstruktionsmodus umschalten
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: Draft: **C** **M**
   SeeAlso: Draft AddConstruction/de
---

# Draft ToggleConstructionMode/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> **Draft KonstruktionsmodusUmschalten** schaltet den Draft Konstruktionsmodus ein oder aus. Falls der Konstruktionsmodus eingeschaltet ist, werden neue [Draft](Draft_Workbench/de.md)-Objekte einer bestimmen Gruppe zugeordnet und erhalten eine vordefinierte Farbe. Diese Möglichkeit ist für - oftmals temporäre - Hilfsgeometrie gedacht, um für die Erzeugung weiterer Objekte neue [Einrastpunkte](Draft_Snap/de.md) bereitzustellen. Wenn die Hilfsgeometrie nicht länger benötigt wird, kann die Konstruktionsgruppe einfach [ausgeblendet](Std_HideSelection/de.md) oder [gelöscht](Std_Delete/de.md) werden.

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;"> 
*Hilfsgeometrie, in blau, hilft bei der Festlegung von Mittelpunkt und Radius eines Kreises*



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche ![](images/Draft_tray_button_construction.png ) in der [Draft Ablage](Draft_Tray/de.md). Diese Schaltfläche ist heruntergedrückt, wenn der Konstruktionsmodus gerade eingeschaltet ist.
    -   [Draft](Draft_Workbench.md): Den Menüeintrag **Dienstprogramme → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Konstruktionsmodus umschalten** auswählen oder die Menüoption im Kontextmenü der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Draft: Das Tastaturkürzel **C** dann **M**.
2.  Die Schaltfläche in der [Draft Ablage](Draft_Tray/de.md) wird aktualisiert.



## Hinweise

-   Falls der Draft Konstruktionsmodus eingeschaltet ist, wird die aktive [Ebene](Draft_Layer/de.md) ignoriert.



## Einstellungen

-   Zur Änderung der Bezeichnung der Hilfsgeometriegruppe: **Bearbeiten → Einstellungen... → Draft → Allgemein →  Benennung der Hilfsgeometriegruppen**.
-   Zur Änderung der zu verwendenden Farbe: **Bearbeiten → Einstellungen... → Draft → Allgemein → Farbe der Hilfsgeometrie**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleConstructionMode/de
