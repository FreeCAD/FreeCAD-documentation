---
- GuiCommand   */de
   Name   *Std Open
   Name/de   *Std Öffnen
   MenuLocation   *Datei → Öffnen...
   Workbenches   *Alle
   Shortcut   ***Strg**+**O**
   SeeAlso   *[Std Import](Std_Import/de.md), [Std Neu](Std_New/de.md)
---

# Std Open/de

## Beschreibung

Der Befehl **Std Öffnen** öffnet eine Datei. Wenn die Datei keine native FreeCAD-Datei (\*.FCStd) ist, wird die enthaltene Geometrie in ein neues Dokument importiert. Siehe [Std Import](Std_Import/de.md) für weitere Informationen.

## Anwendung

1.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen   *
    -   Die Schaltfläche **<img src="images/Std_Open.svg" width=16px> [Öffnen...](Std_Open/de.md)** drücken.
    -   Den Menüeintrag **Datei → <img src="images/Std_Open.svg" width=16px> Öffnen...** auswählen.
    -   Das Tastaturkürzel **Ctrl**+**O**.
2.  Optional kann das richtige Dateiformat im Dialogfeld ausgewählt werden.
3.  Eine Datei auswählen.
4.  Die Schaltfläche **Öffnen** drücken.

## Optionen

-    **Esc**oder Schaltfläche **Cancel** drücken, um den Befehl abzubrechen.

## Einstellungen

-   The last used file location is stored   * **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Skripten


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To open a document use the `open(filepath)` method or the `openDocument(filepath, [hidden<nowiki>=</nowiki>False])` method of the FreeCAD application.

These methods create and return a document and load a project file into it. The `filepath` argument must be a string pointing to an existing file. If the file doesn\'t exist or the file cannot be loaded an I/O exception is thrown. In this case the created document is kept, but will be empty. If `hidden<nowiki>=</nowiki>True` is used, the document won\'t be displayed in the GUI and no tab will appear for it. This allows performing automatic operations on a document and closing it without disrupting the user interface.

For a scripting example see [Std New](Std_New#Scripting.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Open/de
