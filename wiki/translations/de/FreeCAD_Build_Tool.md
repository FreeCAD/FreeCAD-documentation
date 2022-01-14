# FreeCAD Build Tool/de
{{TOCright}}

## Übersicht

Das **FreeCAD Bau Werkzeug** oder **fcbt** ist ein Pythonskript zu finden unter 
```python
trunc/src/Tools/fcbt.py
``` Es kann verwendet werden, um einige häufige Aufgaben zu vereinfachen für Aufbau, Verteilung und Erweiterung von FreeCAD.

## Anwendung

Mit korrekt installiertem [Python](http://de.wikipedia.org/wiki/Python_%28Programmiersprache%29), kann *fcbt* durch den Befehl ausgeführt werden 
```python
python fbct.py
``` Es zeigt ein Menü an, in dem du die Aufgabe für den Einsatz auswählen kannst, die du auswählen willst für: 
```python
FreeCAD Build Tool
 Usage:
    fcbt <command name> [command parameter]
 possible commands are:
  - DistSrc         (DS)   Build a source Distr. of the current source tree
  - DistBin         (DB)   Build a binary Distr. of the current source tree
  - DistSetup       (DI)   Build a Setup Distr. of the current source tree
  - DistSetup       (DUI)  Build a User Setup Distr. of the current source tree
  - DistAll         (DA)   Run all three above modules
  - NextBuildNumber (NBN)  Increase the Build Number of this Version
  - CreateModule    (CM)   Insert a new FreeCAD Module (Workbench) in the module directory
 
 For help on the modules type:
   fcbt <command name> ?
``` An der Eingabeaufforderung gib den abgekürzten Befehl den du anrufen möchtest ein. Gib z. B. \"CM\" für [Erstellung von Arbeitsbereichen](Workbench_creation/de.md) ein.

### DistSrc

Der Befehl \"DS\" **erzeugt eine Quellcode Verteilung** des aktuellen Quellcode Baums.

### DistBin

Der Befehl \"DB\" **erzeugt eine Binärverteilung** des aktuellen Quellcodebaums.

### DistEinstellung

Der Befehl \"DI\" **erstellt eine Einrichtungsverteilung** des aktuellen Quellcodebaums.

### DistEinstellung 

Der Befehl \"DUI\" **erstellt eine Benutzer Einstellverteilung** des aktuellen Quellcodebaums.

### DistAlles

Der Befehl \"DA\" führt \"DS\", \"DB\" und \"DI\" ALLE der Reihe nach aus.

### NächsteBauNummer

Der \"NBN\" Befehl **erhöht die Bau Nummer**, um eine neue Freigabestand Version von FreeCAD zu erstellen.

### ErstelleModul

Der \"CM\" Befehl [erzeugt ein neues Anwendungsmodul (Arbeitsbereich)](Workbench_creation/de.md).





 

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > FreeCAD Build Tool/de
