---
 GuiCommand:
   Name: Arch CloseHoles
   Name/de: Arch LöcherSchließen
   MenuLocation: Utils , Löcher schließen
   Workbenches: BIM_Workbench/de
   SeeAlso: Arch_Check/de
---

# Arch CloseHoles/de



## Beschreibung

Dieses Werkzeug identifiziert Löcher (ringförmige Folge von offenen Kanten) in einem [Part](Part_Workbench/de.md)-Objekt und versucht sie, durch hinzufügen einer Fläche, zu schließen, die aus der Folge von Kanten erstellt wird. Du musst dich aber noch selbst davon überzeugen, dass das Ergebnis ein Festkörper ist.



## Anwendung

1.  Eine [Form](Part_Workbench/de.md) (Shape-Objekt) auswählen.
2.  Den Menüeintrag **Utils → Löcher schließen** auswählen.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Dieses Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch folgende Funktion verwendet werden: 
```python
solid = closeHole(shape)
```

-   Schließt ein Loch in einer Form `shape`, die ein `Part.Shape` ist und gibt das neue Objekt `solid` zurück.

Beispiel: 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 900
Box.Width = 450
Box.Height = 2000
FreeCAD.ActiveDocument.recompute()

Draft.rotate(Box, 45)
Draft.move(Box, FreeCAD.Vector(1000, 700, 0))

Arch.removeComponents(Box, Wall)
FreeCAD.ActiveDocument.recompute() 

solid = Arch.closeHole(Wall.Shape)
```



---
⏵ [documentation index](../README.md) > Arch CloseHoles/de
