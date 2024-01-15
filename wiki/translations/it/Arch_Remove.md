---
 GuiCommand:
   Name: Arch Remove
   Name/it: Rimuovi Componente
   MenuLocation: Arch , Rimuovi componente
   Workbenches: Arch_Workbench/it
   SeeAlso: Arch_CutLine/it, Arch_CutPlane/it, Arch_Add/it
---

# Arch Remove/it



# Descrizione

Lo strumento Rimuovi permette di eseguire 2 tipi di operazioni:

-   Rimuovere un sotto-componente di un oggetto Architettura, ad esempio rimuovere il cubo che è stato inserito in una parete per descrivere il comando <img alt="" src=images/Arch_Add.svg  style="width:16px;"> [Aggiungi componente](Arch_Add/it.md).
-   Rimuovere un oggetto basato su [forme](Part_Workbench/it.md), tipo un <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [muro](Arch_Wall/it.md) o una <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [struttura](Arch_Structure/it.md), da un oggetto di Arch.

La controparte di questo strumento è lo strumento **<img src="images/Arch_Add.svg" width=16px> [Aggiungi](Arch_Add/it.md)**.

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;"> 
*Un parallelepipedo sottratto da un muro, lasciando un buco in esso.*



## Utilizzo

1.  Selezionare un sotto-componente all\'interno di un oggetto di Arch.
2.  Premere il pulsante **<img src="images/Arch_Remove.svg" width=16px>**, o utilizzare **Arch** → **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi componente](Arch_Remove/it.md)** dal menù principale.

Oppure

1.  Selezionare gli oggetti da sottrarre, l\'ultimo oggetto selezionato deve essere l\'oggetto Arch dal quale verranno sottratti gli altri oggetti.
2.  Premere il pulsante **<img src="images/Arch_Remove.svg" width=16px>**, o utilizzare **Arch** → **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi componente](Arch_Remove/it.md)** dal menù principale.

## Script


**Vedere anche:**

[API di Arch](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Rimuovi può essere usato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione: 
```python
removeComponents(objectsList, host=None)
```

-   Rimuove dal genitore il componente o i componenti della lista `objectsList` fornita.
-   Se viene specificato un oggetto `host`, questa funzione prova invece ad aggiungere gli oggetti alla `objectsList`, come fori a `host`.

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
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Remove/it
