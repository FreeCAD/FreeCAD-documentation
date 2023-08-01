---
- GuiCommand:
   Name: Std Quit
   Name/de: Std Beenden
   MenuLocation: Datei - Beenden
   Workbenches: All
   Shortcut: **Alt**+**F4**
   SeeAlso: [Std Schließen](Std_CloseActiveWindow/de.md)
---

# Std Quit/de

## Beschreibung

Der Befehl **Std Beenden** schließt das Programm FreeCAD und speichert bei Bedarf ungespeicherte Dokumente.

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Menüeintrag **Datei → <img src="images/Std_Quit.svg" width=16px> Exit** auswählen.
    -   Das Tastaturkürzel **Alt**+**F4**.
2.  Wenn ungesicherte Dokumente vorhanden sind erscheint ein Dialogfeld mit der Aufforderung sie zu speichern:
    -   Die Schaltfläche **Speichern** drücken, um das aktive Dokument zu speichern. Wenn nötig, vorher einen Dateinamen eingeben.
    -   Die Schaltfläche **Nicht speichern** drücken, um das aktive Dokument zu schließen und alle Änderungen zu verlieren.

## Optionen

-   Wenn noch mehrere ungespeicherte Dokumente vorhanden sind: Haken bei der Checkbox


{{CheckBox|TRUE|Apply answer to all}}

setzen, um Nachfragen zu jeder einzelnen Datei zu vermeiden.

-   Wenn noch ungespeicherte Dokumente vorhanden sind: **Esc** oder die Schaltfläche **Abbrechen** drücken, um den Befehl abzubrechen.

## Einstellungen

-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp (BasisAnwendung) → Preferences (Einstellungen) → General (Allgemein) → FileOpenSavePath**.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Quit/de
