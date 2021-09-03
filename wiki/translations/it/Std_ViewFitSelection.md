---
- GuiCommand:/it   Name:Std_ViewFitSelection   Name/it:Visualizza la selezione   MenuLocation:Visualizza → Viste standard → Visualizza la selezione   Workbenches:Tutti   Shortcut:**V** **S**   SeeAlso:[Visualizza tutto](Std_ViewFitAll/it.md)---

## Descrizione

Il comando **Visualizza la selezione** adatta la camera in modo che tutti gli oggetti selezionati siano visibili e si adattino all\'interno della [vista 3D](3D_view/it.md) attiva.

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_ViewFitSelection.svg" width=16px> Visualizza la selezione**.
    -   Selezionare l\'opzione **Visualizza → Viste standard →  <img src="images/Std_ViewFitSelection.svg" width=16px> Visualizza la selezione** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_ViewFitSelection.svg" width=16px> Visualizza la selezione** dal menu contestuale della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **V** e poi **S**.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per cambiare la vista in \'Visualizza la selezione\', è possibile usare il metodo `SendMsgToActiveView` dell\'oggetto FreeCADGui. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewSelection')
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
