---
 GuiCommand:
   Name: Arch 3Views,
   Name/pl: Architektura: Trzy widoki
   MenuLocation: Architektura , Narzędzia , Trzy widoki
   Workbenches: Arch_Workbench/pl
   SeeAlso: Arch_SplitMesh/pl, Arch_MeshToShape/pl
---

# Arch 3Views/pl



## Opis


**Polecenie to nie jest obecnie używane**

. Służy do generowania płaskich, opartych na kształtach widoków z obiektu opartego na [siatce](Mesh_Workbench/pl.md), do wykorzystania przez narzędzie **<img src="images/Arch_Equipment.svg" width=24px> [Wyposażenie](Arch_Equipment/pl.md)**.



## Użycie

1.  Wybierz obiekt siatki.
2.  Wybierz przycisk **<img src="images/Arch_3Views.svg" width=16px>** lub **Architektura → Narzędzia → <img src="images/Arch_3Views.svg" width=16px> Trzy widoki** z menu głównego.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Kształt z siatki** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji: 
```python
shape = createMeshView(obj, direction=FreeCAD.Vector(0, 0, -1), outeronly=False, largestonly=False)
```

-   Tworzy płaski `shape`, który jest rzutem danego obiektu siatki (`obj`) w danym `direction`.
-   Jeśli `outeronly` ma wartość `True`, tylko zewnętrzny kontur jest brany pod uwagę, odrzucając wewnętrzne otwory.
-   Jeśli `largestonly` ma wartość `True`, użyty zostanie tylko największy segment danej siatki.

Użyj `Part.show()`, aby wyświetlić wynikowy płaski kształt.

Przykład: 
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
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch 3Views/pl
