# FEM ElementFluid1D/it
---
 GuiCommand:   Name: FEM_ElementFluid1D   Name/it: Elemento Fluido 1D   MenuLocation: Modello , Sezione del fluido per il flusso 1D   ---



## Descrizione

Crea un elemento FEM di sezione del fluido per le reti pneumatiche e idrauliche



## Utilizzo

1.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/FEM_ElementFluid1D.svg" width=16px> [Sezione fluido per flusso 1D](FEM_ElementFluid1D/it.md)**.
    -   Seleziona l\'opzione **Model → Geometria dell'Elemento → <img src="images/FEM_ElementFluid1D.svg" width=16px> Sezione fluido per flusso 1D** dal menu.
2.  Selezionare il tipo di fluido: liquido, gas o canale aperto
3.  Selezionare il tipo di sezione: Pipe Manning (coefficiente di scabrezza), Pipe Inlet (tubo di aspirazione) ecc.
4.  Inserire i parametri del tipo di sezione.
5.  Selezionare e aggiungere un bordo.



## Limitazioni

1.  Funziona solo con un elemento di rete a 3 nodi. Le informazioni possono essere trovate in: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node54.html>



## Note

1.  Un esempio di impostazione di una rete idraulica è disponibile in: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node13.html>
2.  La scheda \*FLUID SECTION viene utilizzata per modellare elementi fluidi per il flusso 1D. Le informazioni sulla scheda sono disponibili in: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node205.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementFluid1D/it
