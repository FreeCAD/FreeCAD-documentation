---
- GuiCommand   */de
   Name   *Arch Fence
   Name/de   *Arch Zaun
   MenuLocation   *Arch → Zaun
   Workbenches   *[Arch](Arch_Workbench/de.md)
   Version   *0.19
---

# Arch Fence/de

## Beschreibung

Der [Arch Zaun](Arch_Fence/de.md) ist ein Objekt, das einen Zaun durch die Wiederholung eines einzelnen Zaunpfostens und eines Abschnitts entlang eines bestimmten Pfades bildet.

<img alt="" src=images/Arch_Fence_description_example.png  style="width   *600px;">

## Anwendung

### Erzeugung von Grundauf 

1.  Verwende einen Arbeitsbereich deiner Wahl, um einen einzelnen Zaunpfosten und einen einzelnen Abschnitt zu erstellen.
2.  Erstelle den Pfad, dem der Zaun folgen soll, mit Hilfe des [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) oder [Entwurf Arbeitsbereich](Draft_Workbench/de.md).
3.  Wechsle zurück zum [Architektur Arbeitsbereich](Arch_Workbench/de.md).
4.  Wähle den Abschnitt, den Beitrag und den Pfad in genau dieser Reihenfolge aus.
5.  Drücke die **<img src="images/Arch_Fence.svg" width=16px> [Architektur Zaun](Arch_Fence/de.md)** Schaltfläche

## Optionen

Vorerst geht das Werkzeug von folgenden Voraussetzungen aus

1.  Der Pfad wird auf der XY Ebene gezeichnet
2.  Abschnitt und Pfosten sind am Ursprung so gezeichnet, dass sie in der Vorderansicht aufrecht stehen

## Eigenschaften

### Daten

-    {{PropertyData/de|Pfad}}   * Der Pfad, dem der Zaun folgen sollte

-    {{PropertyData/de|Pfahl}}   * Ein einziger Zaunpfahl zur Wiederholung

-    {{PropertyData/de|Abschnitt}}   * Ein einziger Abschnitt zum Wiederholen

-    {{PropertyData/de|Anzahl der Pfähle}}   * Die Gesamtzahl der Pfähle, die für den Bau des Zauns verwendet wurden. Diese wird automatisch berechnet.

-    {{PropertyData/de|Anzahl der Abschnitte}}   * Die Gesamtzahl der Abschnitte, die zum Bau des Zauns verwendet wurden. Diese wird automatisch berechnet.

### Ansicht

-    {{PropertyView/de|Ursprungsfarben verwenden}}}   * Wenn auf {`True` gesetzt, verwendet der Zaun die Farben aus dem Originalabschnitt und -pfahl. Andernfalls wird die FormFarbe des Zauns verwendet, um den Zaun einzufärben.

## Hinweise

-   Arch Zaun würde eingeführt mit FC v0.19 durch den Anwender furti.
-   [Forumsbeitrag](https   *//forum.freecadweb.org/viewtopic.php?t=36149) der die Arch Zaun Funktionalität diskutiert

## Skripten

Das Zaunwerkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole heraus durch Verwendung der folgenden Funktion verwendet werden   *


```python
Fence = buildFence(section, post, path)
```

Beispiel   *


```python
import FreeCAD
import Part
import Arch

parts = []

parts.append(Part.makeBox(2000, 50, 30, FreeCAD.Vector(0, 0, 1000 - 30)))
parts.append(Part.makeBox(2000, 50, 30))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(0, 15, 30)))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(1980, 15, 30)))

for i in range(8)   *
    parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector((2000 / 9 * (i + 1)) - 10, 15, 30)))

Part.show(Part.makeCompound(parts), "Fence_section")
fence_section = FreeCAD.ActiveDocument.Fence_section

sketch = FreeCAD.ActiveDocument.addObject("Sketcher   *   *SketchObject", "Path")
sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(20000, 0, 0)), False)
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(20000, 0, 0), FreeCAD.Vector(20000, 20000, 0)), False)

post = Part.makeBox(100, 100, 1000, FreeCAD.Vector(0, 0, 0))
Part.show(post, "Post")
post = FreeCAD.ActiveDocument.Post

Fence = Arch.buildFence(fence_section, post, sketch)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Fence/de
