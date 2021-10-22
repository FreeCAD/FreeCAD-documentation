---
- GuiCommand:/it
   Name:Arch MeshToShape
   Name/it:Da Mesh a Forma
   Workbenches:[Architettura](Arch_Workbench/it.md)
   MenuLocation:Arch → Utilità → Da Mesh a Forma
   SeeAlso:[Dividi mesh](Arch_SplitMesh/it.md), [Rimuovi Forma](Arch_RemoveShape/it.md)
---

# Arch MeshToShape/it


</div>

## Descrizione

Da Mesh a Forma converte un oggetto [Mesh](Mesh/it.md) ([Mesh Feature](Mesh_Feature/it.md)) selezionato in un oggetto [Forma](Shape/it.md) ([Part Feature](Part_Feature/it.md)).


<div class="mw-translate-fuzzy">

Questo strumento è ottimizzato per oggetti con facce piane (senza curve). Lo strumento corrispondente **<img src=images/Part_ShapeFromMesh.svg style="width:16px"> _ potrebbe essere più adatto per oggetti che contengono superfici curve.


</div>

## Utilizzo

1.  Selezionare un oggetto mesh.
2.  Premere il pulsante **<img src="images/Arch_MeshToShape.svg" width=16px> [Da mesh a forma](Arch_MeshToShape/it.md)** in **Arch → Utilità → Da mesh a forma**.

## Proprietà

## Limitazioni

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Questo strumento può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
```python
new_obj = meshToShape(obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)
```

-   Il frammento di codice sopra riportato converte il dato `obj`, una mesh, in una forma, unendo le facce complanari.

-   Se `mark` è `True`, gli oggetti non solidi saranno contrassegnati in rosso.

-   Se `fast` è `True` usa un algoritmo più veloce costruendo una shell dalle faccette.

-    `tol`è la tolleranza utilizzata durante la conversione dei segmenti di mesh in contorni.

-   Se `flat` è `True` forza i contorni a essere perfettamente planari, per essere sicuri che possano essere convertiti in facce, ma ciò potrebbe lasciare degli spazi vuoti nella shell finale.

-   Se `cut` è `True` i fori nelle facce sono fatti per sottrazione.

Esempio: 
```python
import Arch, Mesh, BuildRegularGeoms

Box = FreeCAD.ActiveDocument.addObject("Mesh::Cube", "Cube")
Box.Length = 1000
Box.Width = 2000
Box.Height = 1000
FreeCAD.ActiveDocument.recompute()

new_obj = Arch.meshToShape(Box)
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MeshToShape/it
