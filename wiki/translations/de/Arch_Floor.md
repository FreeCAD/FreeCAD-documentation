---
 GuiCommand:
   Name: Arch Floor
   Name/de: Arch Stockwerk
   MenuLocation: 3D/BIM , Stockwerk
   Workbenches: BIM_Workbench/de
   Shortcut: **L** **V**
   SeeAlso: 
---

# Arch Floor/de



## Beschreibung

Das Werkzeug [Arch Stockwerk](Arch_Floor/de.md) ist ein spezielles FreeCAD-Gruppenobjekt mit mehreren Zusatzeigenschaften, welche insbesondere zur Etagenkonstruktion geeignet sind. Insbesondere hält diese Gruppe eine Eigenschaft Höhe, die von allen Kindobjekten ([Wänden](Arch_Wall/de.md) und [Struktur](Arch_Structure/de.md)-Objekten) genutzt werden kann, um die Höhe automatisch anzupassen. Sie werden hauptsächlich zum Gliedern des Modells verwendet.

Für {{VersionPlus/de|0.18}} wird das Arch Stockwerk vollständig aus dem [Arch Gebäudeteil](Arch_BuildingPart/de.md)-Objekt abgeleitet, das ein allgemeiner Behälter zur Organisation eines Gebäudemodells ist, der nicht auf Stockwerke oder Etagen beschränkt ist. Ältere Stockwerk-Objekte können in den neuen Typ umgewandelt werden, indem sie mit der rechten Maustaste angeklickt werden und `Konvertieren zu Gebäudeteil` ausgewählt wird.



## Anwendung

1.  Wahlweise ein oder mehrere Objekte auswählen, die in dem neuen Stockwerk enthalten sein sollen.
2.  Den Befehl Arch Stockwerk mit einer der folgenden Möglichkeiten aufrufen:
    -   Die Schaltfläche **<img src="images/Arch_Floor.svg" width=16px> [Stockwerk](Arch_Floor/de.md)** drücken.
    -   Das Tastaturkürzel **L** dann **V**.
    -   Den Menüeintrag **3D/BIM → Stockwerk** auswählen.



## Optionen

-   Nach Erstellung eines Stockwerks können diesem mit Ziehen und Ablegen in der Baumansicht Objekte hinzugefügt werden oder mit dem Werkzeug **<img src="images/Arch_Add.svg" width=16px> [Hinzufügen](Arch_Add/de.md)**.
-   Objekte können durch Herausziehen und Ablegen in der Baumansicht aus dem Stockwerk entfernt werden oder mit dem Werkzeug **<img src="images/Arch_Remove.svg" width=16px> [Entfernen](Arch_Remove/de.md)**.



## Eigenschaften

Ein Arch-Stockwerk-Objekt besitzt alle Eigenschaften eines [Arch Gebäudeteils](Arch_BuildingPart/de.md), aber mit der {{PropertyData/de|Ifc Type}} auf `"Building Storey"` gesetzt.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Stockwerk kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden:


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
⏵ [documentation index](../README.md) > Arch Floor/de
