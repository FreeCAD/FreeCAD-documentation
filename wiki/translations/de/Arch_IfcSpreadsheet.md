---
 GuiCommand:
   Name: Arch IfcSpreadsheet
   Name/de: Arch_IfcTabellenblatt
   MenuLocation: Dienstprogramme , IFC-Kalkulationstabelle erstellen...
   Workbenches: BIM_Workbench/de
   Shortcut: **I** **P**
   SeeAlso: Arch_IFC
---

# Arch IfcSpreadsheet/de



## Beschreibung

Dieses Werkzeug erstellt eine Kalkulationstabelle, um [IFC](Arch_IFC/de.md)-Eigenschaften eines Objekts zu speichern.



## Anwendung

1.  Ein Objekt auswählen.
2.  Es gibt mehrere Mögkichkeiten, den Befehl aufzurufen:
    -   Den Menüeintrag **Dienstprogramme → <img src="images/Arch_IfcSpreadsheet.svg" width=16px> IFC-Kalkulationstabelle erstellen...** auswählen.
    -   Das Tastaturkürzel **I** dann **P**.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Dieses Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch folgende Funktion verwendet werden: 
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



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch IfcSpreadsheet/de
