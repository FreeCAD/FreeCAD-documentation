---
- GuiCommand:/de
   Name:Arch Building   Name/de:Arch Gebäude
   MenuLocation:Architektur → Gebäude
   Workbenches:[Arch](Arch_Workbench/de.md)
   Shortcut:**B** **U**
   SeeAlso:[Arch Gebäudeteil](Arch_BuildingPart/de.md), [Arch Baugrund](Arch_Site/de.md)
---

# Arch Building/de

## Beschreibung

Ein Gebäude ist ein spezielles FreeCAD Gruppenobjekt, welches sich besonders dafür eignet, eine ganze Gebäudeeinheit zu repräsentieren. Ein Gebäude hilft so bei der Organisation des Modells, es enthält als Untereinheiten [Etagen](Arch_Floor/de.md) Objekte.

## Anwendung

1.  Wähle optional ein oder mehrere Objekte die in dein neues Gebäude aufgenommen werden sollen.
2.  Drücke den **<img src="images/Arch_Building.svg" width=16px> [Arch Gebäude](Arch_Building.md)** Knopf oder drücke die **B** dann **U** Tasten.

## Optionen

-   Seit FreeCAD Version 0.18 ist das Gebäudeobjekt tatsächlich ein [GebäudeTeil](Arch_BuildingPart/de.md), dessen {{PropertyData/de|IFC Typ}} Eigenschaft auf *Gebäude* gesetzt ist.

Du kannst jedes GebäudeTeil in ein Gebäude konvertieren, einfach durch ändern seines IFC Typs.

-   Nach dem erstellen eines Gebäudes, kannst du weitere Objekte durch Ziehen und loslassen in der Baumansicht oder durch verwenden des **<img src="images/Arch_Add.svg" width=16px> [Arch hinzufügen](Arch_Add/de.md)** Werkzeug ihm hinzufügen.
-   Du kannst Objekte aus einem Gebäude entfernen, durch Ziehen und loslassen aus seiner Baumansicht oder durch verwenden des **<img src="images/Arch_Remove.svg" width=16px> [Arch Entfernen](Arch_Remove/de.md)** Werkzeugs.

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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Building/de
