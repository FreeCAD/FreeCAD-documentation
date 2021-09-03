---
- GuiCommand:/de
   Name:Std TreeSelection
   Name/de:Std BaumAnsichtSelektion
   MenuLocation:View → BaumAnsicht-Aktionen → Gehe zu Selektion
   Workbenches:Alle
   Shortcut:**T** **G**
   Version:0.19
---

## Beschreibung

Der **Std BaumAnsichtSelektion**-Befehl verschiebt die [Baumansicht](Tree_view/de.md) auf das erste erstellte Objekt in einer [3D-Ansicht](3D_view/de.md)-Auswahl.

Falls der Baumansicht [Sync-Auswahl](Std_TreeSyncSelection/de.md)-Modus ausgeschaltet ist, wird die Baumansicht auf das erste erstellte Objekt in der Auswahl verschoben, dessen Eltern-Objekt bereits in der Baumansicht erweitert wurde. Falls keines der Eltern-Objekte dieses Objekts erweitert wurde, hat der Befehl keine Auswirkungen.

## Anwendung

1.  Wähle ein oder mehrere Objekte in einer 3D-Ansicht.
2.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Klicke auf den schwarzen Pfeil-nach-unten rechts neben der **<img src="images/Std_TreeSyncView.svg" width=16px>**-Schaltfläche und wähle die {{MenuCommand|<img src="images/Std_TreeSelection.svg" width=16px> Gehe zu Selektion}}-Option aus dem Flyout. Hinweis: Das Schaltflächensymbol ändert sich abhängig von der gewählten Option.
    -   Wähle die {{MenuCommand|Ansicht → BaumAnsicht-Aktionen → <img src="images/Std_TreeSelection.svg" width=16px> Gehe zu Selektion}}-Option aus dem Menü.
    -   Wähle die {{MenuCommand|<img src="images/Std_TreeSelection.svg" width=16px> Gehe zu Selektion}}-Option aus dem 3D-Ansicht-Kontext-Menü.
    -   Benutze den Tastaturkurzbefehl: **T**, dann **G**.





{{Std Base navi

}}  
