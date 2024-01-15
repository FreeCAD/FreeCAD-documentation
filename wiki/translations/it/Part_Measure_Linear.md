---
 GuiCommand:
   Name: Part Measure Linear
   Name/it: Misura Lineare
   MenuLocation: Misure , Misura Lineare
   Workbenches: Part_Workbench/it
   SeeAlso: Std_MeasureDistance/it, Draft_Dimension/it
---

# Part Measure Linear/it



## Descrizione

Questo strumento misura la distanza tra due elementi topologici selezionati (vertice, bordo, faccia) e visualizza le misurazioni nella [vista 3D](vista_3D/it.md). Vengono mostrate la distanza più breve tra i due elementi e le misurazioni delta (distanze parallele agli assi globali X, Y, Z).

L\'aspetto delle misurazioni può essere modificato nelle [preferenze](PartDesign_Preferences/it#Misura.md).

<img alt="" src=images/MeasureLinear3D1.png  style="width:400px;"> <img alt="" src=images/MeasureLinearDelta1.PNG  style="width:400px;">



## Utilizzo

1.  Selezionare una qualsiasi combinazione di due elementi: vertici, bordi, facce
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Part_Measure_Linear.svg" width=16px> [Misura Lineare](Part_Measure_Linear/it.md)**.
    -   Selezionare l\'opzione **Misura → <img src="images/Part_Measure_Linear.svg" width=16px> Misura lineare** dal menu.
3.  In alternativa, il comando può essere avviato senza preventiva selezione. Quindi si apre una finestra di selezione nella [scheda Azioni](Task_panel/it.md). Un widget di controllo fornisce anche i pulsanti per ripristinare la selezione, commutare la visualizzazione della misurazione nella [vista 3D](3D_view/it.md) e cancellare tutte le misurazioni.
4.  Le misurazioni vengono eliminate automaticamente quando si chiude il documento.



## Note

-   Non è possibile utilizzare gli strumenti dello snap di [Draft](Draft_Workbench/it.md) con questo comando.
-   Per aggiungere quote ai disegni utilizzare gli strumenti di quotatura dell\'[Ambiente TechDraw](TechDraw_Workbench/it.md).
-   Per strumenti di misurazione più completi, installare il <img alt="" src=images/Manipulator_workbench_icon.svg  style="width:24px;"> [Manipulator Workbench](Manipulator_Workbench/it.md) (un [ambiente di lavoro esterno](External_workbench/it.md)).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Measure Linear/it
