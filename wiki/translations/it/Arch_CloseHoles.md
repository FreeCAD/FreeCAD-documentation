---
 GuiCommand:
   Name: Arch CloseHoles
   Name/it: Chiudi fori
   MenuLocation: Arch , Utilità , Chiudi fori
   Workbenches: Arch_Workbench/it
   SeeAlso: Arch_Check/it
---

# Arch CloseHoles/it


</div>



## Descrizione

Questo strumento identifica i fori (sequenza circolare di bordi aperti) in un oggetto [Forma](Part_Workbench/it.md) e tenta di chiuderlo con l\'aggiunta di una nuova faccia costruita dalla sequenza dei bordi aperti. È però comunque necessario verificare se il risultato è un solido.



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una [Forma](Part_Workbench/it.md) (un oggetto Parte)
2.  Selezionare la voce **<img src="images/Arch_CloseHoles.svg" width=16px> [Chiudi fori](Arch_CloseHoles/it.md)** nel menu **Arch → Utilità → Chiudi fori**.


</div>



## Script


**Vedere anche:**

[API di Arch](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
```python
solid = closeHole(shape)
```

-   Chiude un foro in una `shape`, che è una `Part.Shape`, e restituisce il nuovo oggetto `solid`.

Esempio: 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 900
Box.Width = 450
Box.Height = 2000
FreeCAD.ActiveDocument.recompute()

Draft.rotate(Box, 45)
Draft.move(Box, FreeCAD.Vector(1000, 700, 0))

Arch.removeComponents(Box, Wall)
FreeCAD.ActiveDocument.recompute() 

solid = Arch.closeHole(Wall.Shape)
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch CloseHoles/it
