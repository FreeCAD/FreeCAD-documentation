---
 GuiCommand:
   Name: Arch Building
   Name/de: Arch Gebäude
   MenuLocation: 3D/BIM , Gebäude
   Workbenches: BIM_Workbench/de
   Shortcut: **B** **U**
   SeeAlso: 
---

# Arch Building/de



## Beschreibung

Ein Gebäude ist ein spezielles FreeCAD-Gruppenobjekt, das sich besonders dafür eignet, eine ganze Gebäudeeinheit zu repräsentieren. Es wird durch enthaltene [Stockwerk](Arch_Floor/de.md)-Objekte zur Organisation des Modells eingesetzt.



## Anwendung

1.  Wahlweisel ein oder mehrere Objekte auswählen, die in das neues Gebäude aufgenommen werden sollen.
2.  Die Schaltfläche **<img src="images/Arch_Building.svg" width=16px> [Gebäude](Arch_Building.md)** drücken oder das Tastaturkürzel **B** dann **U**.



## Optionen

-   Seit FreeCAD Version 0.18 ist das Gebäudeobjekt tatsächlich ein [Gebäudeteil](Arch_BuildingPart/de.md), dessen {{PropertyData/de|IFC Type}} auf *Gebäude* gesetzt ist. Jedes Gebäudeteil kann in ein Gebäude umgewandelt werden, einfach durch Ändern seines IFC-Typs.
-   Nach dem erstellen eines Gebäudes, können ihm weitere Objekte durch Ziehen und Ablegen in der Baumansicht hinzugefügt werden oder durch verwenden des Werkzeugs **<img src="images/Arch_Add.svg" width=16px> [Arch hinzufügen](Arch_Add/de.md)**.
-   Objekte können aus einem Gebäude entfernt werden, durch Herausziehen und Ablegen in der Baumansicht oder durch Verwenden des Werkzeugs **<img src="images/Arch_Remove.svg" width=16px> [Arch Entfernen](Arch_Remove/de.md)**.



## Eigenschaften

-    {{PropertyData/de|Gebäude Typ}}: Der Typ des Gebäudes, wählbar aus einer Liste



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Gebäude Werkzeug kann sowohl in [Makros](macros/de.md) als auch aus der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden: 
```python
Building = makeBuilding(objectslist=None, baseobj=None, name="Building")
```

-   Erzeugt ein `Gebäude` Objekt aus der `Objekteliste`, die entweder eine Liste von Objekten oder oder ein `Basisobj`, das ein `Form` ist.

Beispiel:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall1, Wall2])

Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Building/de
