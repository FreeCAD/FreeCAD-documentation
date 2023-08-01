---
- GuiCommand:
   Name: Std TreeSyncPlacement
   Name/de: Std BaumSyncPosition
   MenuLocation: Ansicht - Baumansicht-Aktionen - Sync-Platzierung
   Workbenches: Alle
   Shortcut: **T** **3**
   Version: 0.19
---

# Std TreeSyncPlacement/de



## Beschreibung

Der Befehl **Std BaumSyncPosition** schaltet den Sync-Position-Modus der [Baumansicht](Tree_view/de.md) ein bzw. aus. Ist dieser Modus aktiv ist, wird die {{PropertyData/de|Placement}} von Objekten automatisch angepasst, wenn sie von einem Container in einen anderen Container mit einem anderen Koordinatensystem gezogen und abgelegt werden, wobei ihre Positionierungen relativ zum globalen Koordinatensystem erhalten bleiben.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den nach unten weisenden Pfeil rechts neben der Schaltfläche **<img src="images/Std_TreeSyncView.svg" width=16px>** anklicken und den Eintrag **Sync-Platzierung** in der angezeigten Liste auswählen. Hinweis: Das Bild der Schaltfläche ändert sich entsprechend der Auswahl.
    -   Den Menüeintrag **Ansicht → Baumansicht-Aktionen → <img src="images/Std_TreeSyncPlacement.svg" width=16px> Sync-Platzierung** auswählen.
    -   Das Tastaturkürzel **T** dann **3**.



## Einstellungen

Die Einstellung Sync-Position der Baumansicht wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → TreeView → SyncPlacement** (Parametereditor). Es ist ein boolescher Wert, die Vorgabe ist `False`.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std TreeSyncPlacement/de
