---
- GuiCommand:
   Name:Std Save
   Name/de:Std Speichern
   MenuLocation:Datei - Speichern
   Workbenches:Alle
   Shortcut:**Ctrl**+**S**
   SeeAlso:[Std SpeichernUnter](Std_SaveAs/de.md), [Std KopieSpeichern](Std_SaveCopy/de.md), [Std AllesSpeichern](Std_SaveAll/de.md)
---

# Std Save/de

## Beschreibung

Der Befehl **Std Speichern** speichert das aktive Dokument.

## Anwendung

1.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_Save.svg" width=16px> [Speichern](Std_Save/de.md)** drücken.
    -   Den Menüeintrag **Datei → <img src="images/Std_Save.svg" width=16px> Speichern** auswählen.
    -   Das Tastaturkürzel **Ctrl**+**S**.
2.  Für neue Dokumente: Einen Dateinamen im Dialogfeld eintragen und die Schaltfläche **Speichern** drücken.

## Optionen

-   Für neue Dokumente: **Esc** oder Schaltfläche **Abbrechen** drücken, um den Befehl abzubrechen.

## Hinweise

-   This command can also be used to save dependency graphs. See [Std DependencyGraph](Std_DependencyGraph.md).

## Einstellungen

-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp (BasisAnwendung) → Preferences (Einstellungen) → General (Allgemein) → FileOpenSavePath**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

To save a document use the `save` method of the document object. A new document must first be saved with the `saveAs` method of the document object. For a scripting example see [Std New](Std_New.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Save/de
