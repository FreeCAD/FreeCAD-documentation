---
 GuiCommand:
   Name: Arch RemoveShape
   Name/it: Rimuovi forma
   MenuLocation: Arch , Utilità , Rimuovi forma
   Workbenches: Arch_Workbench/it
   SeeAlso: Arch_SplitMesh/it, Arch_MeshToShape/it
---

# Arch RemoveShape/it



## Descrizione

Questo strumento tenta di eliminare una forma cubica (un parallelepipedo) incorporata in un **<img src="images/Arch_Wall.svg" width=16px> [Muro](Arch_Wall/it.md)** o in una **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** e di regolare le sue proprietà per rendere l\'oggetto rimanente totalmente parametrico. Questo strumento funziona solo se la forma da eliminare è cubica (con 6 facce e tutti gli angoli retti).



## Utilizzo

1.  Selezionare un **<img src="images/Arch_Wall.svg" width=16px> [Muro](Arch_Wall/it.md)** o una **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)**.
2.  Premere il pulsante **<img src="images/Arch_RemoveShape.svg" width=16px>** o usare **Arch** → **Utilità** → **<img src="images/Arch_RemoveShape.svg" width=16px> [Rimuovi forma](Arch_RemoveShape/it.md)** dal menu in alto.



## Script


**Vedere anche:**

[API di Arch](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Questo strumento può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
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



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch RemoveShape/it
