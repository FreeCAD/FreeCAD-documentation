---
 GuiCommand:
   Name: Std SaveAll
   Name/de: Std AllesSpeichern
   MenuLocation: Datei , Alles speichern
   Workbenches: Alle
   SeeAlso: Std_Save/de
---

# Std SaveAll/de

## Beschreibung

Der **Std AllesSpeichern**-Befehl speichert alle offenen Dokumente.

## Anwendung

1.  Wähle die **Datei → <img src="images/Std_SaveAll.svg" width=16px> Alles speichern**-Option aus dem Menü.
2.  Für neue Dokumente: gib einen Dateinamen in die Dialog-Box ein und drücke die **Speichern**-Schaltfläche.

## Optionen

-   Für neue Dokumente: Drücke **Esc** oder die **Abbrechen**-Schaltfläche, um den Befehl abzubrechen.

## Einstellungen

-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp (BasisAnwendung) → Preferences (Einstellungen) → General (Allgemein) → FileOpenSavePath**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um ein Dokument zu speichern, benutze die `save`-Methode des Dokument-Objekts. Ein neues Dokument muss zuerst mit der `saveAs`-Methode des Dokument-Objekts gespeichert werden. Für ein Skript-Beispiel siehe [Std Neu](Std_New/de.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std SaveAll/de
