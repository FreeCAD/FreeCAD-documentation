---
- GuiCommand:/it
   Name:Part TransformedCopy
   Name/it:Crea una copia modificata
   MenuLocation:Part → Crea una copia → Crea una copia modificata
   Workbenches:[Part](Part_Workbench/it.md)
   Version:0.19
   SeeAlso:[Copia semplice](Part_SimpleCopy/it.md), [Copia di un elemento](Part_ElementCopy/it.md), [Affina forma](Part_RefineShape/it.md)
---


</div>

## Descrizione

[Copia modificata](Part_TransformedCopy/it.md) produce una copia non parametrica di un oggetto che è stato spostato dalla sua posizione originale.

Per produrre altre copie non parametriche utilizzare **<img src="images/Part_SimpleCopy.svg" width=16px> [Copia semplice](Part_SimpleCopy/it.md)**, **<img src="images/Part_ElementCopy.svg" width=16px>[Copia elemento](Part_ElementCopy/it.md)**, o **<img src="images/Part_RefineShape.svg" width=16px> [Affina forma](Part_RefineShape/it.md)**.

## Utilizzo

1.  Selezionare un oggetto del quale si desidera effettuare una copia.
2.  Andare nel menu **Part → Crea una copia → <img src=images/Part_TransformedCopy.svg style="width:16px"> [Copia modificata](Part_TransformedCopy/it.md)**.

## Proprietà

### Dati

La copia ha una semplice proprietà **Placement** come qualsiasi altra [Part Feature](Part_Feature/it.md).

### Vista

La copia ha una semplice proprietà vista come qualsiasi altra [Part Feature](Part_Feature/it.md).

## Scripting

The **Part TransformedCopy** command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Part_TransformedCopy')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).





 
