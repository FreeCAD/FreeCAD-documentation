---
- GuiCommand:/de
   Name:Std_CloseAllWindows
   Name/de:Std Alles schließen
   MenuLocation:Datei → Alles schließen
   Workbenches:Alle
   SeeAlso:[Schließen](Std_CloseActiceWindow/de.md)
---

# Std CloseAllWindows/de

## Beschreibung

Schließt alle geöffneten Dokumente.

Der **Std Alles schließen**-Befehl schließt alle Fenster und dadurch alle Dokumente.

## Anwendung

Wähle **Datei** → **Alles schließen** aus der Menüleiste.

1.  Wähle die **Datei → <img src="images/Std_CloseAllWindows.svg" width=16px> Alles Schließen**-Option aus dem Menü.
2.  Falls es nicht gesicherte Dokumente gibt, öffnet sich eine Dialog-Box, die zum Sichern auffordert:
    -   Drücke die **Speichern**-Schaltfläche zum Sichern des aktiven Dokuments. Falls erforderlich, gib zuerst den Dateinamen ein.
    -   Drücke die **Schließen ohne zu Speichern**-Schaltfläche, um das aktive Dokument zu verlassen und alle Änderungen zu verlieren.

## Optionen

-   Wenn die Dialog-Box angezeigt wird, drücke **Esc** oder die **Abbrechen**-Schaltfläche, um den Befehl abzubrechen.
-   Fall es mehrere nicht gesicherte Dokumente gibt: aktiviere das {{CheckBox|TRUE|Antwort auf alle anwenden}}-Kästchen, um zu vermeiden, für jedes ungesicherte Dokument separat aufgefordert zu werden.

## Hinweise

-   Ein Dokument kann auch geschlossen werden, indem es in der [Baumansicht](Tree_View/de.md) mit einem Rechtsklick ausgewählt und **Dokument schließen** aus dem Kontextmenü benutzt wird.

## Einstellungen

-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BasisAnwendung → Einstellungen → Allgemein → FileOpenSavePath**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um ein Dokument zu schließen, benutze die `closeDocument`-Methode der FreeCAD-Anwendung. Für ein Skripting-Beispiel siehe [Std Neu](Std_New/de.md).





{{Std Base navi

}}

---
[documentation index](../README.md) > Std CloseAllWindows/de
