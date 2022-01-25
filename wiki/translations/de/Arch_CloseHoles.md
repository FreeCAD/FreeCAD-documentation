---
- GuiCommand:/de
   Name:Arch CloseHoles
   Name/de:Arch SchließeLöcher
   MenuLocation:Arch → Dienstprogramme → Schließt Löcher
   Workbenches:[Arch](Arch_Workbench/de.md)
   SeeAlso:[Arch Überprüfung](Arch_Check/de.md)
---

# Arch CloseHoles/de

## Beschreibung

Dieses Werkzeug identifiziert Löcher (ringförmige Folge von offenen Kanten) in einem [Formteil](Part_Workbench/de.md)-Objekt und versucht, sie durch hinzufügen einer Fläche zu schließen, die aus der Folge von Kanten erstellt wird. Du musst dich aber noch selbst davon überzeugen, dass das Ergebnis ein Volumenkörper ist.

## Anwendung

1.  Wähle ein [Form](Part_Workbench/de.md)-Objekt.
2.  Drücke den **<img src="images/Arch_CloseHoles.svg" width=16px> [Löcher schließen](Arch_CloseHoles/de.md)**-Eintrag in {{MenuCommand/de|Arch → Dienstprogramme → Schließe Löcher}}.

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Dieses Werkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus mit der folgenden Funktion verwendet werden: 
```python
solid = closeHole(shape)
```

-   Schließt ein Loch in einer `Form`, welches ein `Part.Shape` ist und gibt das neue `solid` Objekt zurück.

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
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CloseHoles/de
