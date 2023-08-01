---
- GuiCommand:
   Name:Std Redo
   Name/de:Std Wiederherstellen
   MenuLocation:Bearbeiten - Wiederherstellen‎
   Workbenches:Alle
   Shortcut:**Strg**+**Y**
   SeeAlso:[Rückgängig](Std_Undo/de.md)
---

# Std Redo/de

## Beschreibung

Der Befehl **Std Rückgängig** nimmt die Aktion des Befehls [Wiederherstellen](Std_Undo/de.md) zurück.

## Anwendung

1.  Es gibt mehrere Wege, um den Befehl aufzurufen:
    -   Drücke die **<img src="images/Std_Redo.svg" width=16px> [Std Wiederherstellen](Std_Redo/de.md)**-Schaltfläche.
    -   Wähle die **Bearbeiten → <img src="images/Std_Redo.svg" width=16px> Wiederherstellen**-Option aus dem Menü.
    -   Benutze das Tastaturkürzel **Strg**+**Y**.

## Optionen

-   Um mehrere Aktionen wiederherzustellen, klicke auf den schwarzen Pfeil-nach-unten rechts neben der **<img src="images/Std_Redo.svg" width=16px> [Std Wiederherstellen](Std_Redo/de.md)**-Schaltfläche und wähle aus der Liste aus.

## Einstellungen

-   Die Rückgängig/Wiederherstellen-Funktionalität kann deaktiviert werden, indem **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Document → UsingUndo** auf `False` gesetzt wird, aber dies wird nicht empfohlen. Diese Einstellung kann auch im [Voreinstellungseditor](Preferences_Editor/de#Document.md) geändert werden.
-   Die maximale Anzahl von Rückgängig/Wiedererstellen-Schritten wird über **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Document → MaxUndoSize** definiert. Diese Einstellung kann auch im [Voreinstellungseditor](Preferences_Editor/de#Document.md) geändert werden.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Wiederherstellen einer Aktion, die gerade rückgängig gemacht wurde, benutze die `redo`-Methode des document-Objekts.


```python
import FreeCAD

FreeCAD.ActiveDocument.redo()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Redo/de
