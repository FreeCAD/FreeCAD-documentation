---
- GuiCommand:
   Name:Draft ToggleConstructionMode
   Name/de:Draft UmschaltenKonstruktionsmodus
   MenuLocation:Draft - Utilities - Konstruktionsmodus umschalten
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[Draft ZurKonstruktionsgruppeHinzufügen](Draft_AddConstruction/de.md)
---

# Draft ToggleConstructionMode/de

## Beschreibung

Der <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> **Draft UmschaltenKonstruktionsmodus**-Befehl schaltet den Draft Konstruktionsmodus ein oder aus. Fall der Konstruktionsmodus eingeschaltet ist, werden neue [Draft](Draft_Workbench/de.md)-Objekte, außer [Draft Punkten](Draft_Point/de.md) in einer dedizierten Gruppe zugeordnet und erhalten eine vordefinierte Farbe. Diese Möglichkeit ist für - oftmals temporäre - Konstruktionsgeometrie gedacht, um für die Erzeugung weiterer Objekte neue [Einrastpunkte](Draft_Snap/de.md) bereitzustellen. Wenn die Konstruktionsgeometrie nicht länger benötigt wird, kann die Konstruktionsgruppe einfach [versteckt](Std_HideSelection/de.md) oder [gelöscht](Std_Delete/de.md) werden.

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;"> 
*Konstruktionsgeometrie, in blau, hilft bei der Festlegung des Mittelpunkts und Radius eines Kreises*

## Anwendung

1.  Es gibt mehrere Wege, um den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_ToggleConstructionMode.svg" width=16px> [Draft UmschaltenKonstruktionsmodus](Draft_ToggleConstructionMode/de.md)**-Schaltfläche in der [Draft Ablage](Draft_Tray/de.md). Diese Schaltfläche ist heruntergedrückt, wenn der Konstruktionsmodus gerade eingeschaltet ist.
    -   Wähle die **Utilities → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Konstruktionsmodus umschalten**-Option aus dem Menü.
    -   Benutze das Tastaturkürzel: **C**, dann **M**.
2.  Die Schaltfläche in der [Draft Ablage](Draft_Tray/de.md) ist aktualisiert.

## Hinweise

-   Falls der Draft Konstruktionsmodus eingeschaltet ist, wird die aktive [Ebene](Draft_Layer/de.md) ignoriert.

## Einstellungen


<div class="mw-translate-fuzzy">

-   Zur Änderung der Bezeichnung ({{Version/de|0.20}}) der Konstruktionsgruppe: **Bearbeiten → Einstellungen... → Draft → Allgemeine Einstellungen → Konstruktionsgeometrie → Konstruktionsgruppenname**.
-   Zur Änderung der zu verwendenden Farbe: **Bearbeiten → Einstellungen... → Draft → Allgemeine Einstellungen → Konstruktionsgeometrie → Hilfsgeometriefarbe**.


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleConstructionMode/de
