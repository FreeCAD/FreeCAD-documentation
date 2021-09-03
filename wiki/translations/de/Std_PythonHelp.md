---
- GuiCommand:/de
   Name:Std PythonHelp
   Name/de:Std PythonHilfe
   MenuLocation:Hilfe → Automatische Dokumentation der Python Module
   Workbenches:Alle
   SeeAlso:[Std FreeCADHauptAnwenderZentrum](Std_FreeCADPowerUserHub/de.md)
---

## Beschreibung

Der Befehl **Std PythonHilfe** startet einen Webserver, der über einen lokalen Sockel mit dem Standard Internetbrowser des Systems kommuniziert. Der Webserver zeigt Informationen über die verfügbaren [Python](Python/de.md) Module, Klassen und Funktionen von FreeCAD an. Die benötigten Seiten werden automatisch generiert.

Der Webserver basiert auf dem Python Modul [pydoc](https://docs.python.org/3.8/library/pydoc.html#module-pydoc) und extrahiert daher die Dokumentationszeichenketten von Python Dateien (`.py`) sowie die textuelle Dokumentation, die in den Python Wrappern (`.xml`) definiert ist, die den zugrunde liegenden C++ Code offenlegen.

## Anwendung

1.  Wähle die **Hilfe → <img src="images/Std_PythonHelp.svg" width=16px> Automatische Python Module Dokumentation** aus dem Menü.
2.  Klicke auf einen der Verweise, um die Dokumentation einer bestimmten Klasse oder Funktion aufzurufen.





{{Std Base navi

}}  
