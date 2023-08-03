---
 GuiCommand:
   Name: Arch Floor
   Name/de: Arch Geschoss
   MenuLocation: Architektur , Stockwerk
   Workbenches: Arch_Workbench/de
   Shortcut: **L** **V**
   SeeAlso: Arch_Building/de, Arch_BuildingPart/de, Arch_Site/de
---

# Arch Floor/de

## Beschreibung

Eine [Arch Etage](Arch_Floor/de.md) ist ein spezielles FreeCAD Gruppenobjekt mit mehreren Zusatzeigenschaften, welche insbesondere zur Etagenkonstruktion geeignet sind. Insbesondere hält diese Gruppe eine Höhen-Eigenschaft, welche von allen Kindobjekten ([Wände](Arch_Wall/de.md) und [Bauelemente](Arch_Structure/de.md)) genutzt werden kann, um die Höhe automatisch anzupassen. Im Wesentlichen dient das Etagenobjekt der Organisation des Konstruktionsmodells.

Beginnend mit <small>(v0.18)</small>  wird das Arch Geschoss komplett aus dem [Arch Gebäudeteil](Arch_BuildingPart/de.md) Objekt abgeleitet, das ein allgemeiner Behälter zur Organisation eines Gebäudemodells ist, der nicht auf Geschosse oder Etagen beschränkt ist. Ältere Geschoss Objekte können in den neuen Typ umgewandelt werden, indem sie mit Rechtsklick markiert werden und `Konvertieren zu GebäuseTeil` ausgewählt wird.

## Anwendung

1.  Wähle optional ein oder mehrere Objekte aus, die in deinem neuen Geschoss enthalten sein sollen.
2.  Rufe den Befehl Architektur Geschoss auf mehrere Arten auf:
    -   Drücken der **<img src="images/Arch_Floor.svg" width=16px> [Arch Geschoss](Arch_Floor/de.md)** Schaltfläche in der Werkzeugleiste.
    -   Verwendung der **L**, dann **V** Tastaturkürzel.
    -   Verwendung des **Architektur → Geschoss** Eintrags im oberen Menü.

## Optionen

-   Nach Erstellung der Etage können dieser per Drag and Drop in die Baumansicht Objekte hinzugefügt werden. Alternativ kann das **<img src="images/Arch_Add.svg" width=16px> [Hinzufügen](Arch_Add/de.md)**-Werkzeug verwendet werden.
-   Objekte können durch Herausziehen aus der Baumansicht oder mittels **<img src="images/Arch_Remove.svg" width=16px> [Entfernen](Arch_Remove/de.md)**-Werkzeug aus der Etage entfernt werden.

## Eigenschaften

Ein Arch Geschoss Objekt teilt alle Eigenschaften eines [Arch Gebäudeteils](Arch_BuildingPart/de.md), mit dem **Ifc Type** gesetzt auf `"Gebäude Stockwerk"`.

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Etagen-Werkzeug kann in [Makros](macros/de.md) ebenso wie aus der [Python](Python/de.md)-Konsole heraus durch folgende Funktion angesprochen werden: 
```python
Floor = makeFloor(objectslist=None, baseobj=None, name="Floor")
```

-   Erzeugt ein `Floor`-Objekt aus `objectslist`, einer Liste von Objekten.

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

Floor = Arch.makeFloor([Wall1, Wall2])

Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute() 
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Floor/de
