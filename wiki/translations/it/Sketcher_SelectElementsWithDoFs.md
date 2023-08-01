---
- GuiCommand:
   Name/it:Seleziona il Risolutore dei gradi di libertà
   Icon:Sketcher SelectElementsWithDoFs.svg
   MenuLocation:Sketch - Strumenti - Seleziona gli elementi con gradi di libertà
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   Version:0.18
---

# Sketcher SelectElementsWithDoFs/it


</div>



## Descrizione

Questo strumento ha lo scopo di aiutare a vincolare completamente uno schizzo evidenziando in verde gli elementi dello schizzo con residui gradi di libertà (DoF).



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Nella casella Messaggi del Risolutore situata nella parte superiore della scheda Azioni, dovrebbe essere visualizzato il seguente messaggio:
    > Schizzo sotto vincolato con X gradi di libertà

    dove \"X\" è il numero di gradi di libertà rimanenti nello schizzo; cliccare sul link blu, o usare il menu.
2.  Gli elementi che hanno dei gradi di libertà sono evidenziati in verde.
3.  Fare clic in qualsiasi punto dello schizzo per cancellare il colore di evidenziazione.


</div>

-   In case of an **under-constrainend** sketch:

> Under-constrained sketch with X degrees of freedom

where \"X\" is the number of degrees of freedom remaining in the sketch; you will receive more information if you click on the blue link, or if you use the menu.

1.  The elements which have degrees of freedom are now highlighted in green.
2.  Click anywhere in the sketch to clear the highlight color.

-   In case of a **fully-constrainend** sketch:

> Fully constrained sketch 


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/it
