---
- GuiCommand:
   Name: Std TreeMultiDocument
   Name/de: Std BaumMehrfachdokument
   MenuLocation: Ansicht - Baumansicht-Aktionen - Mehrfachdokument
   Workbenches: Alle
   Version: 0.19
   SeeAlso: [Std BaumEinfachdokument](Std_TreeSingleDocument/de.md), [Std BaumDokumentReduzieren](Std_TreeCollapseDocument/de.md)
---

# Std TreeMultiDocument/de



## Beschreibung

Der Befehl **Std BaumMehrfachdokument** ändert den Dokument-Modus der [Baumansicht](Tree_view/de.md) auf Mehrfachdokument. In diesem Modus sind alle Dokumente in der Baumansicht sichtbar und können erweitert werden. Die anderen Modi sind [BaumEinzeldokument](Std_TreeMultiDocument/de.md) und [BaumDokumentReduzieren](Std_TreeCollapseDocument/de.md).



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den nach unten weisenden Pfeil rechts neben der Schaltfläche **<img src="images/Std_TreeSyncView.svg" width=16px>** anklicken und den Eintrag **Mehrfachdokument** in der angezeigten Liste auswählen. Hinweis: Das Bild der Schaltfläche ändert sich entsprechend der Auswahl.
    -   Den Menüeintrag **Ansicht → Baumansicht-Aktionen → <img src="images/_Std_TreeMultiDocument.svg" width=16px> Mehrfachdokument** auswählen.



## Einstellungen

Die Einstellung Dokument-Modus der Baumansicht wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → TreeView → DocumentMode** (Parametereditor). Es ist ein ganzzahliger Wert. Die möglichen Werte sind `0` (Einzeldokument), `1` (Mehrfachdokument) oder `2` (DokumentReduzieren). Standardwert ist `2`.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std TreeMultiDocument/de
