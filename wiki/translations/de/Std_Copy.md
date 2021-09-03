---
- GuiCommand:/de
   Name:Std Copy
   Name/de:Std Kopieren
   MenuLocation:Bearbeiten → Kopieren
   Shortcut:**Strg**+**C**
   Workbenches:Alle
   SeeAlso:[Std Ausschneiden](Std_Cut/de.md), [Std Einfügen](Std_Paste/de.md), [Std Auswahl duplizieren](Std_DuplicateSelection/de.md)---

## Beschreibung

Der **Std Kopieren**-Befehl kopiert Objekte in die Zwischenablage.

## Anwendung

1.  Wähle ein oder mehrere zu Objekte.
2.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Std_Copy.png" width=16px> [Kopieren](Std_Copy/de.md)**-Schaltfläche.
    -   Wähle die **Bearbeiten → <img src="images/Std_Copy.svg" width=16px> Kopieren**-Schaltfläche.
    -   Wähle die **Bearbeiten → <img src="images/Std_Copy.svg" width=16px> Kopieren**-Option auf dem Menü.
    -   Wähle die **Bearbeiten → <img src="images/Std_Copy.svg" width=16px> Kopieren**-Option auf dem [Baumansicht](Tree_view/de.md)-Kontextmenü.
    -   Benutze den Tastaturkurzbefehl **Strg** + **C**.
3.  Falls die Objekte Abhängigkeiten haben, die nicht ausgewählt wurden, öffnet sich eine Dialog-Box, um abzufragen, welche eingeschlossen werden sollen.

## Hinweise

-   Wenn du in einem FreeCAD-Textfenster, einem Eingabefenster oder einem Kalkulationsblatt arbeitest, wird der Standard-Tastaturkurzbefehl **Strg**+**C** - in fast allen Fällen - nicht den **Std Kopieren**-Befehl aufrufen, sondern stattdessen die Kopieren-Funktion des Betriebssystems benutzen.
-   Es ist nicht möglich, native Objekte zwischen FreeCad und anderen Anwendungen zu kopieren/einzufügen.

## Scripting

Der **Std Kopieren**-Befehl kann nach dem Auswählen von einem oder mehreren Objekt/en in der [Baumansicht](Tree_view/de.md) angewendet werden:


```python
FreeCADGui.runCommand('Std_Copy')
FreeCADGui.runCommand('Std_Paste')
```

Die Auswahl kann manuell (über die Maus) oder über die [Python-Konsole](Python_console.md) erfolgen. Über mehr über die programmatische Auswahl von Objekten zu erfahren, siehe [Auswahlmethoden](Selection_methods/de.md).





{{Std Base navi

}}  
