# Std Export/de
---
- GuiCommand:/de
   Name:Std Export
   Name/de:Std Export
   MenuLocation:Datei → Exportieren...
   Workbenches:Alle
   Shortcut:**Strg**+**E**
   SeeAlso:[Std PrintPdf](Std_PrintPdf/de.md), [Export](Import_Export/de.md), [Import Export Einstellungen](Import_Export_Preferences/de.md)---

## Beschreibung

Der **Std Export**-Befehl exportiert ausgewählte Objekte in ein anderes Dateiformat. Viele Dateiformate werden unterstützt und für einige Formate existieren mehrere Exportoptionen. Siehe [Import/Export](Import_Export/de.md) für weitere Informationen.

## Anwendung

1.  Wähle ein oder mehrere Objekte. Um das Exportieren von unsichtbaren oder doppelten Objekten zu vermeiden:
    -   Sei vorsichtig, wenn du **Strg**+**A** zur Auswahl aller Objekte benutzt. Dies wird auch unsichtbare Objekte auswählen.
    -   Selektiere einen [PartDesign Körper](PartDesign_Body/de.md) durch Auswahl nur des Körpers selbst oder des letzten Features.
    -   Selektiere eine [Std Gruppe](Std_Group/de.md) oder ein [Std Teil](Std_Part/de.md) durch Auswahl nur des Eltern-Objekts selbst oder der darin verschachtelten Objekte.
    -   Benutze nicht den [Std Alles Auswählen](Std_SelectAll/de.md)-Befehl, weil er auch Unterelemente von PartDesign-Körpern auswählt.
    -   Aus dem gleichen Grund sollte der [Std Rechteckauswahl](Std_BoxSelection/de.md)-Befehl in FreeCAD-Version 0.18 und früher vermieden werden.
2.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Wähle die **Datei → <img src="images/Std_Export.svg" width=16px> Exportieren...**-Option aus dem Menü.
    -   Benutze das Tastaturkürzel: **Strg**+**E**.
3.  Wähle das richtige Dateiformat in der Dialogbox.
4.  Gib einen Dateinamen ein.
5.  Drücke die **Speichern**-Schaltfläche.

## Optionen

-   Drücke **Esc** oder die **Abbrechen**-Schaltfläche, um den Befehl abzubrechen.

## Hinweise

-   Um ein [Polygonnetz-Objekt](Mesh_Workbench/de.md) in ein stabiles Dateiformat zu exportieren, muss es zuerst konvertiert werden. Siehe das [Importieren von STL oder OBJ](Import_from_STL_or_OBJ/de.md)-Tutorium.
-   Einige Arbeitsbereiche haben zusätzliche Export-Befehle. Siehe: [Import/Export](Import_Export/de.md).

## Einstellungen

-   Siehe: [Import Export Einstellungen](Import_Export_Preferences/de.md).
-   Der zuletzt verwendete Dateiablageort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → General → FileOpenSavePath**.
-   Der zuletzt verwendete Exportfilter wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → General → FileExportFilter**.





{{Std Base navi

}}  

_

---
[documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Export/de
