---
- GuiCommand:
   Name: Arch SplitMesh
   Name/de: Arch NetzAufteilen
   MenuLocation: Arch - Dienstprogramme - Netz zerlegen
   Workbenches: [Arch-Arbeitsbereich](Arch_Workbench/de.md)
   SeeAlso: [Arch SelectNonSolidMeshes](Arch_SelectNonSolidMeshes/de.md), [Arch NetzZuForm](Arch_MeshToShape/de.md)
---

# Arch SplitMesh/de



## Beschreibung

Diese Werkzeug teilt ein ausgewähltes [Mesh](Mesh_Workbench/de.md)-Objekt in seine einzelnen Bestandteile.



## Anwendung

1.  Wähle ein Netzobjekt
2.  Drücke den **<img src="images/Arch_SplitMesh.svg" width=16px> [Netz aufteilen](Arch_SplitMesh/de.md)
** Eintrag in **Arch → Dienstprogramme → Netz aufteilen**

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das NetzAufteilen Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole heraus durch folgende Funktion verwendet werden:


</div>


```python
new_list = splitMesh(obj, mark=True)
```


<div class="mw-translate-fuzzy">

-   Teilt das gegebene Netzobjekt `obj` in einzelne Bestandteile.

-   Falls `mark` auf `True` gesetzt ist, werden [nicht-mannigfaltige](https://de.wikipedia.org/wiki/Mannigfaltigkeit) Komponenten rot dargestellt.

-    `new_list`ist eine Liste aller einzelnen Komponenten, aus denen das Netz besteht.


</div>

Beispiel:


```python
import FreeCAD, Draft, Arch, Mesh, MeshPart

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

Shape = Wall.Shape.copy(False)
Shape.Placement = Wall.getGlobalPlacement()

mesh_obj = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
mesh_obj.Mesh = MeshPart.meshFromShape(Shape=Shape, MaxLength=520)
mesh_obj.ViewObject.DisplayMode = "Flat Lines"

new_list = Arch.splitMesh(mesh_obj)
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SplitMesh/de
