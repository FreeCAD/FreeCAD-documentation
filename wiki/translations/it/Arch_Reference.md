---
 GuiCommand:
   Name: Arch Reference
   Name/it: Riferimento
   MenuLocation: Arch , Riferimento
   Workbenches: Arch_Workbench/it
   SeeAlso: Arch_BuildingPart/it
---

# Arch Reference/it



## Descrizione

<img alt="" src=images/Arch_reference_screenshot.png  style="width:800px;">

Lo strumento Riferimento consente di posizionare nel documento corrente un oggetto che copia la sua forma e i suoi colori da un oggetto basato su [Part](Part_Workbench/it.md) (incluso [Parte di edificio](Arch_BuildingPart/it.md)) e memorizzato in un altro file di FreeCAD. Se il file di FreeCAD cambia, l\'oggetto di riferimento viene contrassegnato per essere ricaricato.



## Utilizzo

1.  Premere il pulsante **<img src="images/Arch_Reference.svg" width=16px> '''Riferimento'''**.
2.  Premere il pulsante \"Choose file\...\" e selezionare un file FreeCAD esistente.
3.  Selezionare uno degli oggetti Part-based inclusi dall\'elenco a discesa
4.  Premere **OK**.



## Opzioni

-   L\'oggetto di riferimento può essere spostato e ruotato, la posizione corrente verrà mantenuta dopo il ricaricamento dell\'oggetto.
-   Se l\'oggetto originale viene spostato nel file contenitore, questo movimento si riflette nell\'oggetto riferimento.
-   Facendo clic con il pulsante destro del mouse su un oggetto riferimento nella vista ad albero, si dispone delle opzioni per ricaricare l\'oggetto originale o aprire il file contenitore.
-   Per fare riferimento a più oggetti contemporaneamente, posizionali all\'interno di una [Parte di edificio](Arch_BuildingPart/it.md).
-   Quando si disattiva la proprietà vista **Update Colors** del Riferimento, non si ricaricano più i colori originali, quindi è possibile cambiarli in modo sicuro.



## Proprietà

-    **File**: il file base su cui è costruito questo componente

-    **Part**: la parte da utilizzare dal file di base

-    **Update Colors**: se è true, i colori del file collegato vengono aggiornati



## Script

Lo strumento Riferimento può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione: 
```python
makeReference ([file_path,object_name])
```

crea un oggetto Riferimento dall\'oggetto dato nel file specificato.

Esempio: 
```python
import Arch
Arch.makeReference("/path/to/some/file.FSCtd","myPart")
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Reference/it
