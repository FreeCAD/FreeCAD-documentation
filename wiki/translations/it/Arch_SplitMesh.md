---
- GuiCommand:/it
   Name:Arch SplitMesh
   Name/it:Dividi mesh
   Workbenches:[Architetttura](Arch_Workbench/it.md)
   MenuLocation:Arch → Utilità → Dividi Mesh
   SeeAlso:[Seleziona mesh non solidi](Arch_SelectNonSolidMeshes/it.md), [Da Mesh a Forma](Arch_MeshToShape/it.md)
---

# Arch SplitMesh/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento suddivide un oggetto [Mesh](Mesh_Workbench/it.md) selezionato nei suoi singoli componenti


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto mesh.
2.  Premere il pulsante **<img src="images/Arch_SplitMesh.svg" width=16px> [Dividi Mesh](Arch_SplitMesh/it.md)** in **Arch → Utilità → Dividi Mesh**.


</div>


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>

Lo strumento Dividi Mesh può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


```python
new_list = splitMesh(obj, mark=True)
```

-   Divide l\'oggetto mesh dato (`obj`) in componenti separati.

-   Se `mark` è `True` [non-manifold](http://en.wikipedia.org/wiki/Manifold) i componenti diventano rossi.

-    `new_list`è un elenco di tutti i singoli componenti che creano la mesh.

Esempio:


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
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SplitMesh/it
