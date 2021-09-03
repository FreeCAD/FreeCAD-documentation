---
- GuiCommand:/it
   Name:Part ElementCopy
   Name/it:Part ElementCopy
   MenuLocation:Part → Crea una copia → Copia un elemento
   Workbenches:[Part](Part_Workbench/it.md)
   Version:0.19
   SeeAlso:[Copia semplice](Part_SimpleCopy/it.md), [Copia modificata](Part_TransformedCopy/it.md), [Affina forma](Part_RefineShape/it.md)
---


</div>

## Descrizione

[Copia un elemento](Part_ElementCopy/it.md) produce una copia non parametrica di un sottoelemento di un oggetto particolare, ovvero di un vertice, un bordo o una faccia.

Per produrre copie complete non parametriche degli oggetti utilizzare **<img src="images/Part_SimpleCopy.svg" width=16px> [Crea una copia semplice](Part_SimpleCopy/it.md)**, **<img src="images/Part_TransformedCopy.svg" width=16px>[Crea una copia trasformata](Part_TransformedCopy/it.md)**, or **<img src="images/Part_RefineShape.svg" width=16px> [Affina una forma](Part_RefineShape/it.md)**.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un vertice, un bordo o una faccia di un oggetto di cui si desidera fare una copia.
2.  Andare nel menu **Part → Crea una copia → <img src=images/Part_ElementCopy.svg style="width:16px"> [Copia un elemento](Part_ElementCopy/it.md)**.


</div>

## Proprietà

### Dati


<div class="mw-translate-fuzzy">

La copia ha una semplice proprietà **Placement** come qualsiasi altra [Part Feature](Part_Feature/it.md).


</div>

### Vista


<div class="mw-translate-fuzzy">

La copia ha una semplice proprietà vista come qualsiasi altra [Part Feature](Part_Feature/it.md).


</div>

## Scripting

The **Part ElementCopy** command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Part_ElementCopy')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).





 
