---
- GuiCommand:/de
   Name:Std TreeSingleDocument
   Name/de:Std TreeSingleDocument
   MenuLocation:Ansicht → Baumansicht-Aktionen → Einzeldokument
   Workbenches:Alle
   Version:0.19
   SeeAlso:[Std BaumMehrfachdokument](Std_TreeMultiDocument/de.md), [Std BaumReduzieren](Std_TreeCollapseDocument/de.md)
---

# Std TreeSingleDocument/de



## Beschreibung

Der Befehl **Std BaumEinzeldokument** ändert den Dokument-Modus der [Baumansicht](Tree_view/de.md) auf Einzeldokument. In diesem Modus ist nur ein einziges Dokument in der Baumansicht sichtbar. Die anderen Modi sind [BaumMehrfachdokument](Std_TreeMultiDocument/de.md) und [BaumDokumentReduzieren](Std_TreeCollapseDocument/de.md).

Im Modus Einzeldokument kann man zu einem anderen Dokument wechseln, indem man die 3D-Ansicht aktiviert, die zu diesem Dokument gehört. Dies kann im [Hauptansichtsbereich](Main_view_area/de.md) erfolgen oder über das Menü **Fenster**.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den nach unten weisenden Pfeil rechts neben der Schaltfläche **<img src="images/Std_TreeSyncView.svg" width=16px>** anklicken und den Eintrag **Einzeldokument** in der angezeigten Liste auswählen. Hinweis: Das Bild der Schaltfläche ändert sich entsprechend der Auswahl.
    -   Den Menüeintrag **Ansicht → Baumansicht-Aktionen → <img src="images/Std_TreeSingleDocument.svg" width=16px> Einzeldokument** auswählen.



## Einstellungen

Die Einstellung Dokument-Modus der Baumansicht wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → TreeView → DocumentMode** (Parametereditor). Es ist ein ganzzahliger Wert. Die möglichen Werte sind `0` (Einzeldokument), `1` (Mehrfachdokument) oder `2` (DokumentReduzieren). Standardwert ist `2`.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std TreeSingleDocument/de
