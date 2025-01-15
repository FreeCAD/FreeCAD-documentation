---
 GuiCommand:
   Name: Arch Fence
   Name/de: Arch Zaun
   MenuLocation: 3D/BIM , Zaun
   Workbenches: BIM_Workbench/de
   Version: 0.19
---

# Arch Fence/de



## Beschreibung

Der [Arch Zaun](Arch_Fence/de.md) ist ein Objekt, das einen Zaun aufbaut durch die Wiederholung eines einzelnen Zaunpfostens und eines Zaunabschnitts entlang eines gegebenen Pfades.

<img alt="" src=images/Arch_Fence_description_example.png  style="width:600px;">



## Anwendung



### Erzeugung von Grundauf 

1.  Einen Arbeitsbereich nach Wahl verwenden, um einen einzelnen Zaunpfosten und einen einzelnen Zaunabschnitt zu erstellen.
2.  Den Pfad, dem der Zaun folgen soll, mit Hilfe des Arbeitsbereichs [Sketcher](Sketcher_Workbench/de.md) oder [Draft](Draft_Workbench/de.md).
3.  Zum Arbeitsbereich [BIM](BIM_Workbench/de.md) zurück wechseln.
4.  Den Zaunabschnitt, den Pfosten und den Pfad in genau dieser Reihenfolge auswählen.
5.  Die Schaltfläche **<img src="images/Arch_Fence.svg" width=16px> [Zaun](Arch_Fence/de.md)** drücken.



## Optionen

Vorerst geht das Werkzeug von folgenden Voraussetzungen aus:

1.  Der Pfad wird auf der XY-Ebene gezeichnet
2.  Zaunabschnitt und Pfosten sind am Ursprung so modelliert, dass sie in der Vorderansicht aufrecht stehen



## Eigenschaften



### Daten

-    {{PropertyData/de|Path}}: Der Pfad, dem der Zaun folgen soll.

-    {{PropertyData/de|Post}}: Ein einzelner Zaunpfosten, der wiederholt werden soll.

-    {{PropertyData/de|Section}}: Ein einzelner Zaunabschnitt, der wiederholt werden soll.

-    {{PropertyData/de|Number Of Posts}}: Die Gesamtanzahl der Pfosten, die für den Aufbau des Zauns verwendet werden. Diese wird automatisch berechnet.

-    {{PropertyData/de|Number Of Sections}}: Die Gesamtanzahl der Zaunabschnitte, die zum Aufbau des Zauns verwendet werden. Diese wird automatisch berechnet.



### Ansicht

-    {{PropertyView/de|Use Original Colors}}: Wenn auf `True` gesetzt, verwendet der Zaun die Farben des originalen Zaunabschnitts und des originalen Pfostens. Andernfalls wird die Formfarbe (ShapeColor) des Zauns verwendet, um den Zaun einzufärben.



## Hinweise

-   Arch Zaun wurde mit FC v0.19 durch den Anwender furti eingeführt.
-   [Forumsbeitrag](https://forum.freecadweb.org/viewtopic.php?t=36149) der die Funktionalität von Arch Zaun diskutiert.



## Skripten

Das Werkzeug Zaun kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch Verwendung der folgenden Funktion verwendet werden:


```python
Fence = buildFence(section, post, path)
```

Beispiel:


```python
import FreeCAD
import Part
import Arch

parts = []

parts.append(Part.makeBox(2000, 50, 30, FreeCAD.Vector(0, 0, 1000 - 30)))
parts.append(Part.makeBox(2000, 50, 30))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(0, 15, 30)))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(1980, 15, 30)))

for i in range(8):
    parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector((2000 / 9 * (i + 1)) - 10, 15, 30)))

Part.show(Part.makeCompound(parts), "Fence_section")
fence_section = FreeCAD.ActiveDocument.Fence_section

sketch = FreeCAD.ActiveDocument.addObject("Sketcher::SketchObject", "Path")
sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(20000, 0, 0)), False)
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(20000, 0, 0), FreeCAD.Vector(20000, 20000, 0)), False)

post = Part.makeBox(100, 100, 1000, FreeCAD.Vector(0, 0, 0))
Part.show(post, "Post")
post = FreeCAD.ActiveDocument.Post

Fence = Arch.buildFence(fence_section, post, sketch)
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Fence/de
