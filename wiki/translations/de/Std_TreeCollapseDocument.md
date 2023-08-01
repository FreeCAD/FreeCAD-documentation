---
- GuiCommand:/de
   Name:Std TreeCollapseDocument
   Name/de:Std BaumDokumentReduzieren
   MenuLocation:Ansicht → Baumansicht-Aktionen → Reduzieren/Erweitern
   Workbenches:Alle
   Version:0.19
   SeeAlso:[Std BaumEinzeldokument](Std_TreeSingleDocument/de.md), [Std BaumMehrfachdokument](Std_TreeMultiDocument/de.md)
---

# Std TreeCollapseDocument/de



## Beschreibung

Der Befehl **Std BaumDokumentReduzieren** wechselt den Dokument-Modus der [Baumansicht](Tree_view/de.md) auf Dokument reduzieren. In diesem Modus bewirkt das Aktivieren der [3D-Ansicht](3D_view/de.md) eines Dokuments automatisch ein Erweitern des Dokuments in der Baumansicht und das Reduzieren sämtlicher anderer Dokumente. Die anderen Modi sind [Einzeldokument](Std_TreeSingleDocument/de.md) and [Mehrfachdokument](Std_TreeMultiDocument/de.md).



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den nach unten weisenden Pfeil rechts neben der Schaltfläche **<img src="images/Std_TreeSyncView.svg" width=16px>** anklicken und den Eintrag **Reduzieren/Erweitern** in der angezeigten Liste auswählen. Hinweis: Das Bild der Schaltfläche ändert sich entsprechend der Auswahl.
    -   Den Menüeintrag **Ansicht → Baumansicht-Aktionen → <img src="images/Std_TreeCollapseDocument.svg" width=16px> Reduzieren/Erweitern** auswählen.



## Einstellungen

Die Einstellung Dokument-Modus der Baumansicht wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → TreeView → DocumentMode** (Parametereditor). Es ist ein ganzzahliger Wert. Die möglichen Werte sind `0` (Einzeldokument), `1` (Mehrfachdokument) oder `2` (DokumentReduzieren). Standardwert ist `2`.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std TreeCollapseDocument/de
