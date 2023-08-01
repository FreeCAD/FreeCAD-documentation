---
- GuiCommand:/it
   Name:Part ShapeFromMesh
   Name/it:‏‎Crea forma da mesh
   MenuLocation:Part → Crea forma da mesh...
   Workbenches:[Part](Part_Workbench/it.md)
   SeeAlso:[Converti in solido](Part_MakeSolid/it.md), [Affina forma](Part_RefineShape/it.md), [Crea punti da mesh](Part_PointsFromMesh/it.md)
---

# Part ShapeFromMesh/it

## Introduzione

Il comando **<img src="images/Part_ShapeFromMesh.svg" width=16px> [Crea forma da mesh](Part_ShapeFromMesh/it.md)** crea una forma da un [oggetto mesh](Mesh/it.md). In FreeCAD gli oggetti mesh hanno limitate capacità di editing, convertendoli in [forme](Shape/it.md) permette di utilizzarli con molti più strumenti di modifica e booleani.

L\'operazione inversa è **[<img src=images/Mesh_FromPartShape.svg style="width:16px"> [Mesh da forma](Mesh_FromPartShape/it.md)** dal <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Ambiente Mesh](Mesh_Workbench/it.md).

## Utilizzo

1.  Selezionare un oggetto mesh nella [Vista ad albero](tree_view/it.md)\...
2.  Andare nel menu **Part → [<img src=images/Part_ShapeFromMesh.svg style="width:16px"> Crea forma da mesh**.
3.  Un menu pop-up chiede di definire la tolleranza per la chiusura; il valore di default è {{Value|0.1}}
4.  Dall\'oggetto mesh viene creato un nuovo oggetto [forma](Shape/it.md) indipendente.

L\'analisi e la riparazione della mesh, se necessario, devono essere eseguite manualmente prima di lanciare **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Crea forma da mesh](Part_ShapeFromMesh/it.md)**. Gli strumenti appropriati per questa attività sono disponibili in <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Ambiente Mesh](Mesh_Workbench/it.md).

Dopo la creazione di una [Forma](Shape/it.md), può essere utile utilizzare **[<img src=images/Part_MakeSolid.svg style="width:16px"> [Converti in solido](Part_MakeSolid/it.md)** (necessario per [operazioni booleane](Part_Boolean/it.md)) e **[<img src=images/Part_RefineShape.svg style="width:16px"> [Affina una forma](Part_RefineShape/it.md)**.

## Links

-   [Edit STL Files In FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) video by AllVisuals4U.

## Scripting

La creazione di una [Forma](Shape/it.md) da una [Mesh](Mesh/it.md) può essere eseguita utilizzando il metodo `makeShapeFromMesh` da una [Part TopoShape](Part_TopoShape/it.md); è necessario specificare la mesh e la tolleranza di origine e assegnare il risultato a un nuovo oggetto [Part Feature](Part_Feature/it.md).

Si noti che la mesh deve essere ricalcolata prima di essere convertita in Shape, altrimenti non ci saranno informazioni sulla topologia e la conversione non avrà successo.


```python
import FreeCAD as App
import Part

doc = App.newDocument()
mesh = doc.addObject("Mesh::Cube", "Mesh")
mesh.recompute()

solid = doc.addObject("Part::Feature", "Shape")
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Mesh.Topology, 0.1)

solid.Shape = shape
solid.Placement.Base = App.Vector(15, 0, 0)
solid.purgeTouched()
doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/it
