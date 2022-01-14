# PartDesign Chamfer/it
---
- GuiCommand:/it   Name:PartDesign Chamfer
   Name/it:Smusso
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:PartDesign → Smusso
   SeeAlso:[PartDesign Raccordo](PartDesign_Fillet/it.md),[Part Smusso](Part_Chamfer/it.md)---


</div>

## Descrizione

Questo strumento applica degli smussi ai bordi di un oggetto selezionato. All\'albero del Progetto viene aggiunto un nuovo elemento **Chamfer** (Smusso) (seguito da un numero sequenziale se non è il primo smusso creato nel documento).

## Utilizzo


<div class="mw-translate-fuzzy">

-   Selezionare uno spigolo, o una faccia su un oggetto, quindi avviare lo strumento facendo clic sul oulsante **[16px|PartDesign Chamfer](File:PartDesign_Chamfer.svg.md) [Smusso](PartDesign_Chamfer.md)** o usare **PartDesign** → **Smusso** dal menu principale. Nel caso in cui sia selezionata una faccia lo smusso viene applicato a tutti i suoi bordi.
-   Nei Parametri smusso del [pannello Azioni](Task_panel/it.md) si può definire lo smusso in 3 modi:
    -   **Stessa distanza**: I bordi degli smussi sono equidistanti dal bordo del corpo.
    -   **Due distanze**: Vengono specificate le distanze dal bordo dello smusso al bordo del corpo. È possibile invertire la direzione della distanza. {{Version/it|0.19}}
    -   **Distanza e angolo**: Viene specificata una distanza dal bordo dello smusso al bordo del corpo. Il secondo bordo dello smusso è definito dall\'angolo dello smusso. È possibile invertire la direzione della distanza. {{Version/it|0.19}}
-   Nei Parametri smusso del [pannello Azioni](Task_panel/it.md), impostare la dimensione dello smusso inserendo il valore o facendo clic sulle frecce su o giù. Lo smusso applicato è mostrato in tempo reale.
-   Se si desidera aggiungere altri bordi o facce fare prima clic sul pulsante **Aggiungi** e quindi selezionare il bordo o la faccia.
-   Se si desidera rimuovere bordi o facce,
    -   selezionare il bordo o la faccia nell\'elenco della finestra di dialogo e premere il tasto **Canc**. *Nota*: poiché deve esserci almeno un bordo per la funzione, l\'ultimo bordo o faccia rimanente nell\'elenco non può essere rimosso.
    -   oppure fare clic sul pulsante **Rimuovi**. Tutti i bordi e le facce precedentemente selezionate sono evidenziati in viola. Selezionare il bordo o la faccia da rimuovere.
-   Fare click su **OK** per convalidare.
-   Per una catena di spigoli tangenti tra loro, è possibile selezionare un singolo bordo; lo smusso si propaga lungo la catena.
-   Per modificare lo smusso dopo che la funzione è stata convalidata, fare doppio clic sull\'etichetta Smusso nella struttura del progetto, oppure fare clic con il pulsante destro del mouse su di essa e selezionare **Modifica smusso**.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Lo smusso di PartDesign e smusso di Parte 

**Lo smusso di PartDesign non deve essere confuso con lo [smusso di Part](Part_Chamfer/it.md)**. Anche se condividono la stessa icona, questi strumenti sono diversi e si utilizzano in modo diverso. La differenza principale è che lo smusso di PartDesign crea una voce smusso separata (seguita da un numero sequenziale se esistono già smussi) nella struttura del progetto per il corpo corrente. Lo smusso di Part diventa il genitore dell\'oggetto a cui è stato applicato.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Chamfer/it
