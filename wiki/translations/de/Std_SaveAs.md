---
- GuiCommand:
   Name:Std SaveAs
   Name/de:Std SpeichernUnter
   MenuLocation:Datei → Speichern unter...
   Workbenches:Alle
   SeeAlso:[Std KopieSpeichern](Std_SaveCopy/de.md), [Std Speichern](Std_Save/de.md)
---

# Std SaveAs/de

## Beschreibung

Der Befehl **Std SpeichernUnter** speichert das aktive Dokument unter einem neuen Dateinamen.

## Anwendung

1.  Menüeintrag **Datei → <img src="images/Std_SaveAs.svg" width=16px> Speichern unter...** auswählen.
2.  Einen Dateinamen im Dialogfeld eingeben.
3.  Schaltfläche **Speichern** drücken.

## Optionen

-    **Esc**oder Schaltfläche **Abbrechen** drücken, um den Befehl abzubrechen.

## Hinweise

-   Dieser Befehl kann auch zum Speichern von Abhängigkeitsgraphen verwendet werden. Siehe [Std Abhängigkeitsgraph](Std_DependencyGraph/de.md).

## Einstellungen

-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp (BasisAnwendung) → Preferences (Einstellungen) → General (Allgemein) → FileOpenSavePath**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um ein Dokument unter einem neuen Namen zu speichern, verwendet man die Methode `saveAs` des Document-Objekts. Für ein Beispielskript siehe [Std Neu](Std_New/de.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std SaveAs/de
