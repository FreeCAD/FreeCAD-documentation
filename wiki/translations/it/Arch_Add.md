---
- GuiCommand   */it
   Name   *Arch Add
   Name/it   *Aggiungi
   MenuLocation   *Arch → Aggiungi componente
   Workbenches   *[Architettura](Arch_Workbench/it.md)
   SeeAlso   *[Rimuovi](Arch_Remove/it.md)
---

# Arch Add/it

## Descrizione

Lo strumento Aggiungi permette di eseguire 4 diversi tipi di operazioni   *

-   Aggiungere a un componente di Architettura degli oggetti basati su [forme](Part_Workbench/it.md), ad esempio un **<img src="images/Arch_Wall.svg" width=16px> [muro](Arch_Wall/it.md)** o una **<img src="images/Arch_Structure.svg" width=16px> [struttura](Arch_Structure/it.md)**. Questi oggetti vengono inseriti nell\'elemento Architettura, ed è possibile modificare la loro forma, ma mantenendo le loro caratteristiche di base come la larghezza e l\'altezza.
-   Aggiungere componenti di Architettura, quali **<img src="images/Arch_Wall.svg" width=16px> [muri](Arch_Wall/it.md)** o **<img src="images/Arch_Structure.svg" width=16px> [Strutture](Arch_Structure/it.md)**, a un oggetto costituito da un gruppo base come il **<img src="images/Arch_Floor.svg" width=16px> [Piano](Arch_Floor/it.md)**.
-   Aggiungere dei **<img src="images/Arch_Axis.svg" width=16px> [sistemi di assi](Arch_Axis/it.md)** a oggetti **<img src="images/Arch_Structure.svg" width=16px> [struttura](Arch_Structure/it.md)**.
-   AAggiungere degli oggetti ai **<img src="images/Arch_SectionPlane.svg" width=16px> [piani di sezione](Arch_SectionPlane/it.md)**.

La controparte di questo strumento è lo strumento **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi componente](Arch_Remove/it.md)**.

<img alt="" src=images/Arch_Add_example.jpg  style="width   *640px;"> 
*Un box aggiunto a un muro come componente.*

## Utilizzo

1.  Selezionare gli oggetti da unire. L\'ultimo oggetto selezionato è l\'oggetto Arch ospite.
2.  Premere il pulsante **<img src="images/Arch_Add.svg" width=16px>**, o usare **Arch** → **<img src="images/Arch_Add.svg" width=16px> [Aggiungi componente](Arch_Add/it.md)** dal menu principale.

## Script


**Vedere anche   ***

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Aggiungi può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione   *

   *   
    
```python
    addComponents(objectsList, host)
    
```
    





   *   Il frammento di codice riportato sopra aggiunge gli oggetti dati in `objectsList` all\'oggetto `host` specificato.
   *   **Nota   *** `objectsList` può essere un singolo oggetto o un elenco di oggetti.

Esempio   *


```python
import FreeCAD, Arch, Draft, Part

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Arch.addComponents(Wall2, Wall)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Add/it
