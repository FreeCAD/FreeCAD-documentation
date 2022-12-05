---
- GuiCommand:/ru
   Name:Arch 3Views
   Name/ru:Arch: 3Views/3 D Просмотры
   MenuLocation:Архитектура → Утилиты → 3 Views from mesh
   Workbenches:[Arch](Arch_Workbench/ru.md)
   Shortcut:
   SeeAlso:[Arch SplitMesh](Arch_SplitMesh/ru.md), [Arch MeshToShape](Arch_MeshToShape/ru.md)
---

# Arch 3Views/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

**Эта команда в настоящее время не используется**. Она служит для создания плоских, базирующихся на форме видов из [полигональных](Mesh_Workbench/ru.md) объектов, для использования инструментами [Arch Equipment](Arch_Equipment/ru.md).


</div>

## Использование

1.  Select a Mesh object.
2.  Select the **<img src="images/Arch_3Views.svg" width=16px>** button, or **Arch** → **Utilities** → **<img src="images/Arch_3Views.svg" width=16px> [3Views](Arch_3Views.md)** from the top menu.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

This tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
shape = createMeshView(obj, direction=FreeCAD.Vector(0, 0, -1), outeronly=False, largestonly=False)
```

-   Creates a flat `shape` that is the projection of the given mesh object (`obj`) in the given `direction`.
-   If `outeronly` is `True` only the outer contour is taken into consideration, discarding the inner holes.
-   If `largestonly` is `True` only the largest segment of the given mesh will be used.

Use `Part.show()` to display the resulting flat shape.

Example: 
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


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch 3Views/ru
