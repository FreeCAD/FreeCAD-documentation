---
- GuiCommand:/de
   Name:Arch IfcSpreadsheet
   Name/de:Arch_ErstelleIfcTabellenblatt
   Workbenches:[Arch](Arch_Workbench/de.md)
   MenuLocation:Arch → Dienstprogramme → Erstelle IFC Tabellenblatt
   Shortcut:**I** **P**
   SeeAlso:[Arch IfcExplorer](Arch_IFC/de]],_[[Arch_IfcExplorer/de.md)
---

# Arch IfcSpreadsheet/de



## Beschreibung

Dieses Werkzeug erstellt eine Tabellenblatt, um [IFC](Arch_IFC/de.md) Eigenschaften eines Objekts zu speichern.



## Anwendung

1.  Wähle ein Objekt aus.
2.  Rufe den Befehl mit mehreren Methoden auf:
    -   Drücken der **<img src="images/Arch_IfcSpreadsheet.svg" width=16px> IFC Tabellenblatt erstellen** Schaltfläche in der Werkzeugleiste.
    -   Verwenden der **I** dann **P** Tastaturkürzel.
    -   Verwenden des **Arch → Dienstprogramme → <img src="images/Arch_IfcSpreadsheet.svg" width=16px> IFC Tabellenblatt erstellen** Eintrags aus dem oberen Menü.

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Dieses Werkzeug kann in [Makros](macros/de.md) ebenso wie aus der Python-Konsole heraus durch folgende Funktion angesprochen werden:


</div>


```python
spreadsheet = makeIfcSpreadsheet(archobj=None)
```

-   Erstellt ein `Tabellenblatt` Objekt. Optional kann ein `archobj` angegeben werden.

Beispiel: 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

spreadsheet = Arch.makeIfcSpreadsheet(Wall)
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch IfcSpreadsheet/de
