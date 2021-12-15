# Interface creation/de
{{TOCright}}

## Einführung

Intensivnutzer haben die Möglichkeit, [Oberflächen erstellen](Interface_creation/de.md) um sie bei der Erstellung komplexer Werkzeuge für ihre benutzerdefinierten [Erweiterungen](Addon/de.md) zu unterstützen, wie z.B. [Makros](Macros/de.md) oder vollständige [Arbeitsbereiche](Workbenches/de.md).

Benutzeroberflächen werden mit [PySide](PySide/de.md) erstellt, einer Bibliothek zur Verwendung von Qt mit [Python](Python/de.md).

<img alt="" src=images/FreeCAD_creating_interfaces.svg  style="width:600px;"> 
*Zwei allgemeine Methoden zur Erstellung von Schnittstellen, durch Einfügen der Schnittstelle in die Python Datei oder durch die Verwendung von `.ui* Dateien.`

## Beschreibung

Es gibt typischerweise zwei Möglichkeiten, Benutzeroberflächen mit PySide zu erstellen.

### Oberfläche in einer .ui Datei 

In this method the interface is defined in a `.ui` file (an XML document that defines the structure of the interface), which is then imported into [Python](Python.md) code that uses it. This is the recommended approach.

-   It allows the programmer to work with the graphical interface separately from the logic that will use it.
-   It allows anybody to look at the interface alone, that is, the `.ui` file, without having to run Python code.
-   The `.ui` file may be designed by anybody without programming knowledge.
-   The `.ui` interface can be used in a standalone window (modal), or in an embedded window (non-modal); therefore, this method is ideal to create custom [task panels](Task_panel.md).
-   Since the `.ui` file just describes the \"appearance\" of the interface, it does not need to be tied to a particular programming language; it may be used both in [Python](Python.md) and C++ code.

### Oberfläche vollständig in Python Code 

In this method the entire interface is defined by several Python calls.

-   This is an older way of working with interfaces.
-   This method produces very verbose code because many details of the interface need to be specified by hand.
-   It is not simple to separate the interface from the logic that uses that code, meaning that a user would need to run the [Python](Python.md) file in the correct context in order to see how the interface would look.
-   This method has the advantage that several interfaces may be contained within a single document, at the expense of making the file very large.
-   This method is recommended only for small interfaces that don\'t define more than a few widgets, for example in [macros](Macros.md).

Beispiele für diese Methode findest Du unter [Dialogerstellung](Dialog_creation/de.md).





{{Powerdocnavi

}}

_ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Interface creation/de
