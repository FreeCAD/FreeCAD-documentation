---
- GuiCommand:/it
   Name:Std_Refresh
   Name/it:Aggiorna
   MenuLocation:Modifica → Aggiorna
   Workbenches:Tutti
   Shortcut:**F5**
---

## Descrizione

Il comando **Aggiorna** ricalcola il documento attivo. Il comando è disabilitato se il documento non richiede un nuovo calcolo.

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_Refresh.svg" width=16px> Aggiorna**.
    -   Selezionare l\'opzione {{MenuCommand|Modifica → <img src="images/Std_Refresh.svg" width=16px> Aggiorna}} dal menu.
    -   Usare la scorciatoia da tastiera: **F5**.

## Opzioni


<div class="mw-translate-fuzzy">

-   Per forzare un ricalcolo selezionare il documento o uno o più oggetti nella [vista ad albero](Tree_view/it.md), selezionare l\'opzione {{MenuCommand|Segna da ricalcolare}} dal menu contestuale e richiamare il comando.
-   Per gli oggetti, ma non per i documenti, si può anche scegliere {{MenuCommand|Ricalcola l'oggetto}} dallo stesso menu contestuale ({{Version/it|0.19}}).


</div>

## Note

-   Per una macro che ricalcola il documento attivo, consultare: [Macro ForceRecompute](Macro_ForceRecompute/it.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per ricalcolare un documento, utilizzare il metodo `recompute` dell\'oggetto documento.


```python
import FreeCAD

doc = FreeCAD.newDocument()
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
