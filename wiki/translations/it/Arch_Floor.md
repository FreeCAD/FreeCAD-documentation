---
- GuiCommand:/it
   Name:Arch Floor
   Name/it:Piano
   Workbenches:[Architettura](Arch_Workbench/it.md)
   MenuLocation:Arch → Piano
   Shortcut:**L** **V**
   SeeAlso:[Edificio](Arch_Building/it.md), [Sito](Arch_Site/it.md)
---

# Arch Floor/it


</div>

## Descrizione

Il [Piano](Arch_Floor/it.md) del modulo Arch è un gruppo speciale di oggetti di FreeCAD che possiede alcune proprietà aggiuntive particolarmente utili nella costruzione dei piani. In particolare, possiede la proprietà di altezza, che i suoi oggetti figli, i muri ([muri](Arch_Wall/it.md) e le [strutture](Arch_Structure/it.md)), possono utilizzare per impostare automaticamente la loro altezza. I piani sono prevalentemente utilizzati per organizzare il modello.

A partire da FreeCAD 0.18, il Piano è derivato interamente dall\'oggetto [Parte di edificio](Arch_BuildingPart/it.md), che è un contenitore generale per organizzare un modello di edificio non limitato a piani o pavimenti. Gli oggetti Piano creati con versioni precedenti di FreeCAD possono essere convertiti nel nuovo tipo facendo clic con il pulsante destro del mouse su di essi e scegliendo `Convert to BuildingPart`.

## Utilizzo

1.  Opzionalmente, selezionare uno o più oggetti da includere nel nuovo piano.
2.  Richiamare il comando Piano in uno di questi modi:
    -   Premere il pulsante **<img src="images/Arch_Floor.svg" width=16px> [Piano](Arch_Floor/it.md)** nella barra degli strumenti.
    -   Usare la scorciatoia **L** **V** da tastiera.
    -   Usare **Arch → Piano** dal menu principale.

## Opzioni

-   Dopo aver creato un piano, è possibile aggiungere ad esso altri oggetti con il drag-and-drop nella struttura ad albero o utilizzando lo strumento **<img src="images/Arch_Add.svg" width=16px> [Aggiungi](Arch_Add/it.md)**.
-   È possibile rimuovere gli oggetti da un piano trascinandoli fuori con il drag-and-drop nella vista ad albero o utilizzando lo strumento **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi](Arch_Remove/it.md)**.

## Proprietà


<div class="mw-translate-fuzzy">

Un oggetto Piano condivide tutte le proprietà di una [Parte di edificio](Arch_BuildingPart/it.md), con la proprietà**Ifc Role** impostata su `"Building Storey"`.


</div>

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Piano può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione: 
```python
Floor = makeFloor(objectslist=None, baseobj=None, name="Floor")
```

-   Crea un oggetto `Floor` da una `objectslist`, che è una lista di oggetti.

Esempio:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

Floor = Arch.makeFloor([Wall1, Wall2])

Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute() 
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Floor/it
