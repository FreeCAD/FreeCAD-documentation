---
 GuiCommand:
   Name: Std Undo
   Name/de: Std Rückgängig
   MenuLocation: Bearbeiten , Rückgängig
   Workbenches: Alle
   Shortcut: **Strg**+**Z**
   SeeAlso: Std Redo/de
---

# Std Undo/de



## Beschreibung

Der Befehl **Std Rückgängig** macht die letzte Aktion rückgängig.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_Undo.svg" width=16px> [Rückgängig](Std_Undo/de.md)** drücken.
    -   Den Menüeintrag **Bearbeiten → <img src="images/Std_Undo.svg" width=16px> Rückgängig** auswählen.
    -   Das Tastaturkürzel **Strg** + **Z**.



## Optionen

-   Um mehrere Aktionen rückgängig zu machen, auf den schwarzen Pfeil-nach-unten rechts neben der Schaltfläche **<img src="images/Std_Undo.svg" width=16px> [Rückgängig](Std_Undo/de.md)** klicken und aus der Liste auswählen.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md).

-   Die Rückgängig/Wiederherstellen-Funktionalität kann ausgeschaltet werden, indem **Bearbeiten → Einstellungen... → Allgemein → Dokument → Rückgängigmachen/Wiederholen in Dokumenten verwenden** deaktiviert wird. Aber dies wird nicht empfohlen.
-   Die maximale Anzahl von Rückgängig/Wiedererstellen-Schritten wird über **Bearbeiten → Einstellungen... → Allgemein → Dokument → Maximale Rückgängigmachen/Wiederholen-Schritte** festgelegt.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Um die letzte Aktion rückgängig zu machen, wird die Methode `undo` des document-Objekts verwendet. Das Gegenstück, die Methode `redo` steht auch zur Verfügung.


```python
import FreeCAD

FreeCAD.ActiveDocument.undo()
```

Wenn FreeCAD im reinen Konsolenmodus (CLI) läuft, ist der Undo/Redo-Mechanismus standardmäßig deaktiviert ist. Er muss für jedes Dokument separat aktiviert werden.


```python
import FreeCAD

FreeCAD.ActiveDocument.UndoMode = 1
```



---
⏵ [documentation index](../README.md) > Std Undo/de
