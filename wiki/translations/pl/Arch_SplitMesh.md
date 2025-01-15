---
 GuiCommand:
   Name: Arch SplitMesh
   Name/pl: BIM: Podziel siatkę
   MenuLocation: Narzędzia , Podziel siatkę
   Workbenches: BIM_Workbench/pl
   SeeAlso: Arch_SelectNonSolidMeshes/pl, Arch_MeshToShape/pl
---

# Arch SplitMesh/pl



## Opis

Narzędzie **Podziel siatkę** dzieli wybrany obiekt [Siatki](Mesh_Workbench/pl.md) na jego oddzielne komponenty.



## Użycie

1.  Wybierz obiekt siatki.
2.  Naciśnij przycisk w menu **Narzędzia → <img src="images/Arch_SplitMesh.svg" width=16px> Podziel siatkę**.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Podziel siatkę** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
new_list = splitMesh(obj, mark=True)
```

-   Dzieli podany obiekt siatki (`obj`) na oddzielne komponenty.

-   Jeśli `mark` ma wartość `True` komponenty [non-manifold](https://en.wikipedia.org/wiki/Manifold) zostaną pomalowane na czerwono.

-    `new_list`jest listą wszystkich pojedynczych komponentów tworzących siatkę.

Przykład:


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
⏵ [documentation index](../README.md) > Arch SplitMesh/pl
