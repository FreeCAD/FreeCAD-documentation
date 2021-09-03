---
- GuiCommand:/it   Name:Part SimpleCopy‎‏‎   Name/it:Copia semplice   MenuLocation:Part → Crea una copia → Copia semplice   Workbenches:[SeeAlso:[[Draft_Clone/it   Clona](Part_Workbench/it___Part]].md), [Copia](Std_Copy/it.md), [Duplica Selezione](Std_DuplicateSelection/it.md), [Copia trasformata](Part_TransformedCopy/it.md), [Copia elemento](Part_ElementCopy/it.md), [Affina forma](Part_RefineShape/it.md)|Icon:Tree_Part.svg   Icon:Tree_Part.svg---


</div>

## Descrizione

[Crea una copia semplice‎](Part_SimpleCopy/it‎.md) elimina lo storico della parte in modo che i diversi passaggi per creare la parte non siano più accessibili / modificabili

In alternativa, per produrre altre copie non parametriche utilizzare <img alt="" src=images/Part_TransformedCopy.svg  style="width:16px;"> [Copia trasformata](Part_TransformedCopy/it.md), <img alt="" src=images/Part_ElementCopy.svg  style="width:16px;"> [Copia elemento](Part_ElementCopy/it.md), e <img alt="" src=images/Part_RefineShape.svg  style="width:16px;"> [Affina forma](Part_RefineShape/it.md).

## Utilizzo

1.  Selezionare un oggetto del quale si desidera effettuare una copia.
2.  Andare nel menu **Part → Crea una copia → <img src="images/Part_SimpleCopy.svg" width=16px> [Copia semplice](Part_SimpleCopy/it.md)**.

## Proprietà

### Dati

La copia ha una semplice proprietà **Placement** come qualsiasi altra [Part Feature](Part_Feature/it.md).

### Vista

La copia ha una semplice proprietà vista come qualsiasi altra [Part Feature](Part_Feature/it.md).

## Script

The **Part SimpleCopy**‎ command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Part_SimpleCopy')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).


<div class="mw-translate-fuzzy">





</div>


  
