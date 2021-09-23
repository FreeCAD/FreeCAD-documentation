# Std ViewFitAll/it
---
- GuiCommand:/it   Name:Std_ViewFitAll   Name/it:Visualizza tutto   MenuLocation:Visualizza → Viste standard → Visualizza tutto   Workbenches:Tutti   Shortcut:**V** **F**   SeeAlso:[Visualizza la selezione](Std_ViewFitSelection/it.md)---

## Descrizione


<div class="mw-translate-fuzzy">

Il comando **Visualizza tutto** adatta la camera in modo che tutti gli oggetti siano visibili e si adattino all\'interno della [vista 3D](3D_view/it.md) attiva.


</div>

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_ViewFitAll.svg" width=16px> Visualizza tutto**.
    -   Selezionare l\'opzione **Visualizza → Viste standard → <img src="images/Std_ViewFitAll.svg" width=16px> Visualizza tutto** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_ViewFitAll.svg" width=16px> Visualizza tutto** dal menu contestuale della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **V** e poi **F**.

## Note


<div class="mw-translate-fuzzy">

-   È anche possibile \'visualizzare tutto\' tramite il menu Mini-cubo del [Cubo di navigazione](Navigation_Cube/it.md).


</div>

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per modificare la vista in \'visualizza tutto\', usare il metodo `fitAll` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.fitAll()
```

In alternativa, è possibile utilizzare il metodo `SendMsgToActiveView` dell\'oggetto FreeCADGui. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewFit')
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewFitAll/it
