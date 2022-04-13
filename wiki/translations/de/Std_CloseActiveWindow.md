---
- GuiCommand:/de
   Name:Std CloseActiveWindow
   Name/de:Std Schließen
   MenuLocation:Datei → Schließen
   Workbenches:Alle
   Shortcut:**Strg**+**F4**
   SeeAlso:[Std AllesSchließen](Std_CloseAllWindows/de.md)
---

# Std CloseActiveWindow/de

## Beschreibung

Der Befehl **Std Schließen** schließt das aktive Fenster. Um ein Dokument zu schließen, müssen alle seine Fenster geschlossen werden.

## Anwendung

1.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Wähle die **Datei → <img src="images/Std_CloseActiveWindow.svg" width=16px> Schließen**-Option aus dem Menü.
    -   Benutze den Tastaturkurzbefehl: **Ctrl**+**F4**.
2.  Um ein Dokument zu schließen: wiederhole dies für alle dazugehörigen Fenster..
3.  Beim Schließen des letzten Fensters eines nicht gesicherten Dokument öffnet sich eine Dialog-Box, die zum Sichern auffordert:
    -   Drücke die **Speichern**-Schaltfläche. Falls erforderlich, gib zuerst den Dateinamen ein.
    -   Drücke die **Schließen ohne zu Speichern**-Schaltfläche, um das Dokument zu verlassen und alle Änderungen zu verlieren.

## Optionen

-   Wenn die Dialog-Box angezeigt wird, drücke **Esc** oder die **Abbrechen**-Schaltfläche, um den Befehl abzubrechen.

## Hinweise

-   Der Befehl kann nur [docked](Std_ViewDockUndockFullscreen.md)-Fenster schließen.
-   \* Ein Dokument kann auch geschlossen werden, indem es in der [Baumansicht](Tree_view/de.md) mit einem Rechtsklick ausgewählt und **Dokument schließen** aus dem Kontextmenü benutzt wird.

## Einstellungen

-   Der zuletzt verwendete Dateispeicherort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BasisAnwendung → Einstellungen → Allgemein → FileOpenSavePath**.

## Scripting


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um ein Dokument zu schließen, benutze die `closeDocument`-Methode der FreeCAD-Anwendung. Für ein Skripting-Beispiel siehe [Std Neu](Std_New/de.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std CloseActiveWindow/de
