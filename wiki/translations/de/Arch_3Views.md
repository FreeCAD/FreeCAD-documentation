---
- GuiCommand:
   Name: Arch 3Views
   Name/de: Arch 3Ansichten
   MenuLocation: Arch - Dienstprogramme - 3 Ansichten aus Netz
   Workbenches: [Arch](Arch_Workbench/de.md)
   SeeAlso: [Arch NetzAufteilen](Arch_SplitMesh/de.md), [Arch NetzZuForm](Arch_MeshToShape/de.md)
---

# Arch 3Views/de



## Beschreibung


**Dieser Befehl wird zur Zeit nicht verwendet.**

Er dient dazu, flache, formbasierte Ansichten aus einem [Mesh](Mesh_Workbench/de.md) basierten Objekt zu erzeugen, die von der **<img src="images/Arch_Equipment.svg" width=24px> [Arch Ausrüstung](Arch_Equipment/de.md)** Werkzeug.



## Anwendung

1.  Wähle ein Netzobjekt aus.
2.  Wähle die **<img src="images/Arch_3Views.svg" width=16px>** Schaltfläche oder **Arch** → **Utilities** → **<img src="images/Arch_3Views.svg" width=16px> [3Ansichten](Arch_3Views.md)** aus dem oberen Menü.




<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Dieses Werkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus mit der folgenden Funktion verwendet werden:


</div>


```python
shape = createMeshView(obj, direction=FreeCAD.Vector(0, 0, -1), outeronly=False, largestonly=False)
```

-   Erzeugt eine flache `Form`, die die Projektion des gegebenen Netzobjekts (`obj`) in der gegebenen `Richtung` ist.
-   Wenn `nuraußen` `True` ist, wird nur die äußere Kontur berücksichtigt, wobei die inneren Löcher verworfen werden.
-   Wenn `nurgrößtes` `True` ist, wird nur das größte Segment des gegebenen Netzes verwendet.

Verwende `Part.show()`, um die resultierende flache Form anzuzeigen.

Beispiel: 
```python
import FreeCAD, Draft, Arch, Mesh, MeshPart

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

Shape = Wall.Shape.copy(False)
Shape.Placement = Wall.getGlobalPlacement()

mesh_obj = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
mesh_obj.Mesh = MeshPart.meshFromShape(Shape=Shape, MaxLength=520)
mesh_obj.ViewObject.DisplayMode = "Flat Lines"
FreeCAD.ActiveDocument.recompute()

XAxis = FreeCAD.Vector(1, 0, 0)
YAxis = FreeCAD.Vector(0, 1, 0)
ZAxis = FreeCAD.Vector(0, 0, -1)

s1 = Arch.createMeshView(mesh_obj, ZAxis)
s2 = Arch.createMeshView(mesh_obj, XAxis)
s3 = Arch.createMeshView(mesh_obj, YAxis)

Part.show(s1)
Part.show(s2)
Part.show(s3)

Wall.ViewObject.Visibility = False
mesh_obj.ViewObject.Visibility = False
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch 3Views/de
