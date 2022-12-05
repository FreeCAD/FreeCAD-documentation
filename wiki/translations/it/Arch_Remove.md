---
- GuiCommand:/it
   Name:Arch Remove
   Name/it:Rimuovi
   Workbenches:[Architettura](Arch_Workbench/it.md)
   MenuLocation:Arch → Rimuovi
   SeeAlso:[Taglia con una linea](Arch_CutLine/it.md), [Taglia con un piano](Arch_CutPlane/it.md), [Aggiungi](Arch_Add/it.md)
---

# Arch Remove/it


</div>

# Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Rimuovi permette di eseguire 2 tipi di operazioni:

-   Rimuovere un sotto-componente di un oggetto Architettura, ad esempio rimuovere il cubo che è stato inserito in una parete per descrivere il comando <img alt="" src=images/Arch_Add.svg  style="width:16px;"> [Aggiungi](Arch_Add/it.md).
-   Rimuovere un oggetto basato su [forme](Part_Workbench/it.md), tipo un <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [muro](Arch_Wall/it.md) o una <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [struttura](Arch_Structure/it.md), da un oggetto Architettura


</div>


<div class="mw-translate-fuzzy">

La controparte di questo strumento è lo strumento <img alt="" src=images/Arch_Add.svg  style="width:16px;"> [Aggiungi](Arch_Add/it.md).


</div>

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;"> 
*Un parallelepipedo sottratto da un muro, lasciando un buco in esso.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un sotto-componente all\'interno di un oggetto Architettura.
2.  Premere il pulsante **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi](Arch_Remove/it.md)**.


</div>


<div class="mw-translate-fuzzy">

Oppure

1.  Selezionare gli oggetti da sottrarre, l\'ultimo oggetto selezionato deve l\'oggetto Arch dal quale verranno sottratti gli altri oggetti.
2.  Premere il pulsante **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi](Arch_Remove/it.md)**.


</div>


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Rimuovi può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


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


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Remove/it
