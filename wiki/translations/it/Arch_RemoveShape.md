---
- GuiCommand:/it
   Name:Arch RemoveShape
   Name/it:Rimuovi forma
   Workbenches:[Architettura](Arch_Workbench/it.md)
   MenuLocation:Arch → Utilità → Rimuovi forma
   SeeAlso:[Dividi mesh](Arch_SplitMesh/it.md), [Da Mesh a Forma](Arch_MeshToShape/it.md)
---

# Arch RemoveShape/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento tenta di eliminare una forma cubica (un parallelepipedo) incorporata in un <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Muro](Arch_Wall/it.md) o in una <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Struttura](Arch_Structure/it.md) e di regolare le sue proprietà per rendere l\'oggetto rimanente totalmente parametrico. Questo strumento funziona solo se la forma da eliminare è cubica (con 6 facce e tutti gli angoli retti).


</div>

## Utilizzo

1.  Selezionare un <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Muro](Arch_Wall/it.md) o una <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Struttura](Arch_Structure/it.md).
2.  Premere il pulsante **<img src="images/Arch_RemoveShape.svg" width=16px> [Rimuovi Forma](Arch_RemoveShape/it.md)** in **Arch → Utilità → Rimuovi Forma**.

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Questo strumento può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
```python
removeShape(objs, mark=True)
```

Prende una lista di oggetti Arch (`objs`) costruiti su una forma cubica, e rimuove la forma interna, conservando la sua lunghezza, larghezza e altezza come proprietà dell\'oggetto Arch.

-   -   
        `objs`
        
        è un singolo oggetto [Parete](Arch_Wall/it.md) o [Struttura](Arch_Structure/it.md), o un loro elenco.

-   Se `mark` è `True`, gli oggetti che non possono essere elaborati da questa funzione diventano rossi.


```python
import FreeCAD, Draft, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 2000
Box.Height = 1000
FreeCAD.ActiveDocument.recompute()

Structure = Arch.makeStructure(Box)
FreeCAD.ActiveDocument.recompute()

Arch.removeShape(Structure)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch RemoveShape/it
