# Python console/de
**(Januar 2020) FreeCAD wurde ursprünglich für die Arbeit mit Python 2 entwickelt. Da Python 2 im Jahr 2020 das Ende seiner Lebensdauer erreicht hat, wird die zukünftige Entwicklung von FreeCAD ausschließlich mit Python 3 erfolgen und die Abwärtskompatibilität wird nicht unterstützt.**

## Einleitung


{{TOCright}}


<div class="mw-translate-fuzzy">

Die [Python Konsole](Python_console/de.md) ist ein Feld, das eine Instanz des [Python](Python/de.md) Interpreters ausführt, mit dem FreeCAD Prozesse gesteuert, Objekte und deren Eigenschaften erstellt und geändert werden können.


</div>

It can be made visible/hidden through the **View → Panels → Python console** drop-down menu.

Die Python-Konsole in FreeCAD verfügt über eine grundlegende Syntaxhervorhebung, die es ermöglicht, mit verschiedenen Stilen und Farben, Kommentaren, Zeichenketten, numerischen Werten, eingebauten Funktionen, gedruckter Textausgabe und Trennzeichen wie Klammern und Kommata zu unterscheiden. Diese Eigenschaften der Konsole können im [Voreinstellungseditor](Preferences_Editor/de.md) konfiguriert werden.

<img alt="" src=images/FreeCAD_Python_console.png  style="width   *800px;">



*Die Python Konsole zeigt Meldungen an, wenn FreeCAD gerade gestartet wurde.*

## Skripten


**Für absolute Anfänger, siehe   ***

[Einführung in Python](Introduction_to_Python/de.md), und [Python Tutorium Skripten](Python_scripting_tutorial/de.md).


**Siehe auch   ***

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md), und [Geskriptete Objekte](Scripted_objects/de.md).

Die Python Konsole kann grundlegende Code Vervollständigung durchführen, wenn ein Punkt nach einem Objekt steht; sie zeigt öffentliche Methoden und Attribute (Variablen) des aktuellen Objekts (Klasse), zum Beispiel `obj.`

Die Konsole ist auch in der Lage, den Dokumentationsstring einer bestimmten Funktion anzuzeigen, wenn die öffnende Klammer geschrieben wird, z.B. `function(`

<img alt="" src=images/FreeCAD_Python_console_example.png  style="width   *800px;">



*Beispiel Python Code, der Objekte in der 3D Ansicht erzeugt.*

Die FreeCAD Initialisierungsskripte laden automatisch einige Module und definieren einige Aliase. In der Python Konsole stehen diese daher zur Verfügung 
```python
App = FreeCAD
Gui = FreeCADGui
```

Daher sind diese gleichwertig


```python
App.newDocument()
FreeCAD.newDocument()
```


**Hinweis   ***

diese vorinstallierten Module und Aliase sind nur über die in das FreeCAD Programm eingebettete Python Konsole verfügbar. Wenn Du FreeCAD als Bibliothek in einem externen Programm verwendest, musst Du daran denken, die Module `FreeCAD` und `FreeCADGui` zu laden und die notwendigen Aliase zu definieren, wenn Du möchtest.

## Maßnahmen

Ein Rechtsklick auf die Python Konsole zeigt einige Befehle an   *

-    {{MenuCommand/de|Kopiere}}   * speichert den markierten Text in der Zwischenablage zum späteren Einfügen; er ist deaktiviert, wenn nichts markiert ist.

-    {{MenuCommand/de|Kopiere Befehl}}   * speichert den markierten Befehl in der Zwischenablage zum späteren Einfügen; er ist deaktiviert, wenn nichts markiert ist.

-    {{MenuCommand/de|Kopiere Historie}}   * die gesamte Historie der in dieser Sitzung eingegebenen Python-Befehle kopieren.

-    {{MenuCommand/de|Save history as}}   * die gesamte Historie der in dieser Sitzung eingegebenen Python Befehle in eine Textdatei speichern.

-    {{MenuCommand/de|Einfügen}}   * zuvor kopierten Text aus der Zwischenablage in die Python-Konsole einfügen.

-    {{MenuCommand/de|Alles Wählen}}   * wählt den gesamten Text in der Python-Konsole aus.

-    {{MenuCommand/de|Konsole löschen}}   * löscht alle in der Python Konsole eingegebenen Befehle. Dies ist nützlich, wenn die Python Konsole voll von Meldungen und zuvor eingegebenen Befehlen ist, die beim Testen einer neuen Funktion ablenken könnten. Dies ist nur ästhetisch, da dieser Befehl weder vorhandene Variablen löscht noch die importierten Module in der Sitzung löscht.

-    {{MenuCommand/de|Dateiname einfügen}}   * öffnet einen Dialog zum Suchen einer Datei im System, dann fügt es den vollständigen Pfad der Datei ein. Dies ist nützlich, um Funktionen zu testen, die eine Eingabedatei verarbeiten, ohne den gesamten Namen in die Konsole schreiben zu müssen, was fehleranfällig ist. Dieser Befehl führt die Datei nicht aus und importiert sie nicht als Python-Modul, sondern gibt nur den vollständigen Pfad der Datei zurück.

-    {{MenuCommand/de|Wort umbrechen}}   * sehr lange Zeilen umbrechen, die die horizontale Dimension der Python-Konsole überschreiten.

## Hinweise

-   One has the ability to scroll the API in the Python console. Example   *
    1.  In the console type   * `FreeCAD.`
    2.  A dialog box will display with optional classes/functions to choose from
    3.  Scroll through the list to read the description of each class/function
    4.  By choosing a function and following it with a `.` one can repeat steps 2 and 3 to traverse deeper in to the API
-   Tab/Word completion is supported using the **Ctrl**+**Space** shortcut


{{Interface navi

}} {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Python console/de
