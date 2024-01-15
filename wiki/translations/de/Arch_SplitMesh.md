---
 GuiCommand:
   Name: Arch SplitMesh
   Name/de: Arch NetzAufteilen
   MenuLocation: Arch , Dienstprogramme , Netz zerlegen
   Workbenches: Arch_Workbench/de
   SeeAlso: Arch_SelectNonSolidMeshes/de, Arch_MeshToShape/de
---

# Arch SplitMesh/de



## Beschreibung

Diese Werkzeug teilt ein ausgewähltes [Mesh](Mesh_Workbench/de.md)-Objekt in seine einzelnen Bestandteile.



## Anwendung

1.  Wähle ein Netzobjekt
2.  Drücke den **<img src="images/Arch_SplitMesh.svg" width=16px> [Netz aufteilen](Arch_SplitMesh/de.md)
** Eintrag in **Arch → Dienstprogramme → Netz aufteilen**



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug NetzAufteilen kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit der folgenden Funktion verwendet werden:


```python
new_list = splitMesh(obj, mark=True)
```

-   Teilt das gegebene Netzobjekt `obj` in einzelne Bestandteile auf.

-   Falls `mark` auf `True` gesetzt ist, werden [nicht-mannigfaltige](https://de.wikipedia.org/wiki/Mannigfaltigkeit) Komponenten rot dargestellt.

-    `new_list`ist eine Liste aller einzelnen Komponenten, aus denen das Netz besteht.

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



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SplitMesh/de
