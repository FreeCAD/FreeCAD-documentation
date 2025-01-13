---
 GuiCommand:
   Name: Part ShapeFromMesh
   Name/it: ‏‎Part Crea forma da mesh
   MenuLocation: Parte , Crea forma da mesh...
   Workbenches: Part_Workbench/it
   SeeAlso: Part_MakeSolid/it, Part_RefineShape/it, Part_PointsFromMesh/it
---

# Part ShapeFromMesh/it



## Introduzione

Il comando <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:16px;"> **Crea forma da mesh** crea forme da [oggetti mesh](Mesh/it.md). In FreeCAD gli oggetti mesh hanno limitate capacità di editing, convertirli in [forme](Shape/it.md) permette di manipolarli con molti più comandi di modifica e booleani.

L\'operazione inversa è [Mesh da forma](Mesh_FromPartShape/it.md) dell\'<img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Ambiente Mesh](Mesh_Workbench/it.md).



## Utilizzo

1.  L\'analisi e la riparazione dell\'oggetto mesh, se necessario, devono essere eseguite prima di avviare questo comando. Strumenti appropriati per questa attività sono disponibili in <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Mesh](Mesh_Workbench/it.md).
2.  Selezionare uno o più oggetti mesh.
3.  Seleziona l\'opzione **Parte → [<img src=images/Part_ShapeFromMesh.svg style="width:16px"> Crea forma da mesh** dal menu.
4.  Si apre la finestra di dialogo **Forma da mesh**.
5.  Facoltativamente selezionare la casella di controllo **Cuci forma** e specificare una tolleranza:
    -   Questa opzione solitamente non è necessaria. È pensata per oggetti mesh che non sono impermeabili e presentano piccoli spazi tra i bordi.
    -   Se l\'opzione è selezionata, viene creato un composto di gusci, anziché un composto di facce.
    -   L\'operazione di cucitura potrebbe essere impegnativa dal punto di vista computazionale.
6.  Premere il pulsante **OK**.
7.  Per ogni oggetto mesh selezionato viene creata una [shape](Shape/it.md) come un nuovo oggetto separato.
8.  Facoltativamente utilizzare <img alt="" src=images/Part_RefineShape.svg  style="width:16px;"> [Part Affina forma](Part_RefineShape/it.md) su questi oggetti.
9.  Facoltativamente, trasformare gli oggetti finali in solidi con <img alt="" src=images/Part_MakeSolid.svg  style="width:16px;"> [Part Crea solido](Part_MakeSolid/it.md).



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Gli oggetti creati Part Forma da mesh sono oggetti [Part Feature](Part_Feature/it.md) senza proprietà aggiuntive.

## Scripting

La creazione di una [Forma](Shape/it.md) da una [Mesh](Mesh/it.md) può essere eseguita utilizzando il metodo `makeShapeFromMesh` da una [Part TopoShape](Part_TopoShape/it.md); è necessario specificare la mesh e la tolleranza di origine e assegnare il risultato a un nuovo oggetto [Part Feature](Part_Feature/it.md).

Si noti che la mesh deve essere ricalcolata prima di essere convertita in Shape, altrimenti non ci saranno informazioni sulla topologia e la conversione non avrà successo.


```python
import FreeCAD as App
import Part

doc = App.ActiveDocument
mesh = doc.addObject("Mesh::Cube", "Mesh")
mesh.recompute()

shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Mesh.Topology, 0.1)

solid = doc.addObject("Part::Feature", "Solid")
solid.Shape = Part.Solid(shape.removeSplitter())
solid.Placement.Base = App.Vector(15, 0, 0)
doc.recompute()
```

## Links

-   [Edit STL Files In FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) video by AllVisuals4U.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/it
