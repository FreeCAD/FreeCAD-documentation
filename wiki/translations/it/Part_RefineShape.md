# Part RefineShape/it
---
- GuiCommand:   Name:Part_RefineShape   Name/it:Affina forma   MenuLocation:Parte - Crea una copia - Affina forma   Workbenches:[SeeAlso:[[Part_SimpleCopy/it|Copia semplice](Part_Workbench/it___Parte]].md), [Copia trasformata](Part_TransformedCopy/it.md), [Copia elemento](Part_ElementCopy/it.md), [Affina forma di OpenSCAD](OpenSCAD_RefineShapeFeature/it.md)---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Part_RefineShape.svg  style="width:16px;"> [Affina forma](Part_RefineShape/it.md) produce una copia non parametrica affinata, cioè con i bordi e le facce ripuliti.


</div>


<div class="mw-translate-fuzzy">

Dopo alcune operazioni booleane, come una [Unione](Part_Union/it.md), rimangono visibili alcune linee delle forme precedenti. Questo strumento produce una copia del risultato booleano e ripulita dalle linee superflue.


</div>

In alternativa, per produrre altre copie non parametriche degli oggetti utilizzare <img alt="" src=images/Part_SimpleCopy.svg  style="width:16px;"> [Crea una copia semplice](Part_SimpleCopy/it.md), <img alt="" src=images/Part_TransformedCopy.svg  style="width:16px;"> [Crea una copia trasformata](Part_TransformedCopy/it.md), o <img alt="" src=images/Part_ElementCopy.svg  style="width:16px;"> [Copia elemento](Part_ElementCopy/it.md).

![](images/PartRefineShape_it.png )


<div class="mw-translate-fuzzy">



*Risultato booleano originale (a sinistra) e copia della forma affinata (a destra).*


</div>



## Utilizzo

1.  Selezionare un oggetto che si desidera pulire e copiare.
2.  Andare nel menu **Part → Crea una copia → <img src="images/Part_RefineShape.svg" width=16px> Affina forma**.
3.  Viene creata una copia pulita e indipendente dell\'oggetto originale; l\'oggetto originale è nascosto.

A partire da FreeCAD 0.19, il risultato viene automaticamente impostato su una copia parametrica (collegata).


<div class="mw-translate-fuzzy">

Questo comportamento può essere modificato nell\'[editor dei parametri](Std_DlgParameter/it.md).

1.  Andare al sottogruppo `BaseApp/Preferences/Mod/Part`
2.  Cambiare `ParametricRefine` di tipo `Boolean` in `False` per ottenere il vecchio comportamento (copia indipendente).


</div>

Vedi altri parametri in [Ottimizzare l\'installazione](Fine-tuning/it.md).




<div class="mw-translate-fuzzy">

### Note


</div>


<div class="mw-translate-fuzzy">

-   Questa funzione può essere utilizzata come ultimo passo nel lavoro di modellazione per ripulire le forme in un flusso di lavoro tradizionale di [geometria solida costruttiva](constructive_solid_geometry/it.md).
-   Questa funzione può aiutare a ripulire il modello prima di applicare un\'altra funzione, ad esempio un [raccordo](Part_Fillet/it.md).
-   Questa pulizia potrebbe impedire alle stampanti 3D di stampare bordi indesiderati una volta esportato il modello solido in un formato mesh.
-   Questa funzione può essere utilizzata anche dopo aver convertito una mesh in una forma con ([Forma da mesh](Part_ShapeFromMesh/it.md)) per pulire i bordi residui su facce piane.


</div>




<div class="mw-translate-fuzzy">

### Limitazioni


</div>

-   L\'algoritmo di affinamento funziona solo sui gusci. Quindi itera sui gusci della forma di ingresso e poi per ogni guscio (shell) ne crea uno nuovo con le facce unite, dove è possibile. Questo significa che se la forma di ingresso è solo una faccia, contorno, bordo o vertice l\'algoritmo non fa nulla.
-   \* A differenza del comando <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:24px;"> [Affina forma](OpenSCAD_RefineShapeFeature/it.md) di OpenSCAD, <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Affina forma](Part_RefineShape/it.md) di Parte non si aggiorna quando vengono modificate le forme precedenti.




<div class="mw-translate-fuzzy">

## Script

Il comando Pyhton per ripulire una forma è il seguente:


</div>

The Python command for refining a shape is the following:


```python
shape.removeSplitter()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/it
