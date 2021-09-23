---
- GuiCommand:/de
   Name:Std Undo
   Name/de:Std Rückgängig
   MenuLocation:Bearbeiten → Rückgängig
   Workbenches:Alle
   Shortcut:**Strg**+**Z**
   SeeAlso:[Wiederherstellen](Std_Redo/de.md)
---

# Std Undo/de

## Beschreibung

Der **Std Rückgängig**-Befehl macht die letzte Aktion rückgängig.

## Anwendung

1.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Std_Undo.svg" width=16px> [Std Rückgängig](Std_Undo/de.md)**-Schaltfläche.
2.  Wähle die **Bearbeiten → <img src="images/Std_Undo.svg" width=16px> Rückgängig**-Option aus dem Menü
    -   Benutze das Tastaturkürzel: **Strg**+**Z**.

## Optionen

-   Um mehrere Aktionen rückgängig zu machen, klicke auf den schwarzen Pfeil-nach-unten rechts neben der **<img src="images/Std_Undo.svg" width=16px> [Std Rückgängig](Std_ReUn/de.md)**-Schaltfläche und wähle aus der Liste aus.

## Einstellungen

-   Die Rückgängig/Wiederherstellen-Funktionalität kann deaktiviert werden, indem **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Document → UsingUndo** auf `False` gesetzt wird, aber dies wird nicht empfohlen. Diese Einstellung kann auch im [Voreinstellungseditor](Preferences_Editor/de#Document.md) geändert werden.
-   Die maximale Anzahl von Rückgängig/Wiedererstellen-Schritten wird über **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Document → MaxUndoSize** definiert. Diese Einstellung kann auch im [Voreinstellungseditor](Preferences_Editor/de#Document.md) geändert werden.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die letzte Aktion rückgängig zu machen, benutze die `undo`-Methode des document-Objekts.


```python
import FreeCAD

FreeCAD.ActiveDocument.undo()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std Undo/de
