---
- GuiCommand:/it   Name:Sketcher MapSketch   Name/it:Mappa Schizzo   Workbenches:[PartDesign](Sketcher_Workbench/it___Sketcher]],_[[PartDesign_Workbench/it.md)|MenuLocation:Part design → Mappa schizzo su faccia   SeeAlso:[Crea nuovo schizzo](Sketcher_NewSketch/it.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Mappa uno **Schizzo già esistente nel progetto** su una faccia planare selezionata in una forma. Permette di utilizzare uno schizzo realizzato in precedenza, di modificarlo e, inoltre, di riposizionarlo sul piano definito dalla faccia selezionata. Le funzioni PartDesign create da questo disegno saranno fuse con il solido di base per le funzionalità additive (PAD, Rivoluzione) o sottratte dal solido di base nel caso di funzioni sottrattive (Scavo, Scanalatura).


</div>

Notare che questo strumento non serve per creare i nuovi disegni. Mappa o rimappa uno schizzo esistente alla faccia di un solido o di una funzione PartDesign. Casi d\'uso tipici sono:

-   Lo schizzo è stato creato su un piano standard (XY, XZ, YZ) e si desidera mapparlo sulla faccia di un solido al fine di costruire una funzione su di esso.
-   Lo schizzo è stato mappato su una faccia di un solido, ma è necessario associarlo ad una faccia diversa.
-   Riparazione di un modello rovinato.

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare la faccia della forma su cui si vuole applicare lo schizzo
2.  Fare clic sul pulsante {{KEY/it|<img src="images/Sketcher_MapSketch.svg" width=16px> Mappa uno schizzo su una faccia}} per selezionare lo schizzo da utilizzare.
3.  Selezionare lo schizzo. Questa azione posiziona automaticamente lo schizzo selezionato sul piano della faccia attiva, anche se faccia e schizzo sono orientati diversamente, e avvia l\'ambiente Sketcher per consentire eventuali modifiche allo schizzo stesso.


</div>

## Uso per riparare un modello rovinato 

Mappa schizzo viene spesso utilizzato durante la riparazione di un modello danneggiato.


<div class="mw-translate-fuzzy">

Un caso d\'uso comune è quando il grafico delle dipendenze è stato rotto. Si può visualizzare il grafico delle dipendenze da **Strumenti** → **[Grafico delle dipendenze](Std_DependencyGraph/it.md)**. Questo può accadere quando si elimina una funzione nel mezzo dell\'albero del modello. Nell\'esempio seguente interromperemo e ripareremo un modello.


</div>

Questo è il modello base. Ha un pad, una tasca e un pad all\'interno della tasca. Notare che il grafico delle dipendenze è lineare.

![](images/JschremppFCADEdit1.png )

Ora abbiamo eliminato la tasca e lo schizzo che ha creato la tasca (Pocket e Sketch001). Notare che ora il grafico delle dipendenze è interrotto. Per riparare questo modello, vogliamo allegare Sketch002 alla faccia superiore del Pad. Nella vista del modello si può vedere che sarebbe facile selezionare la faccia sbagliata.

![](images/JschremppFCADEdit2.png )

Per riparare il modello, prima cambiamo la visibilità dei solidi. Nascondiamo Pad001 e rendiamo visibile Pad.

![](images/JschremppFCADEdit3.png )

Ora selezioniamo la faccia superiore di Pad e quindi selezioniamo lo strumento Mappa schizzo su faccia. Nella finestra di dialogo che appare selezioniamo Sketch002. Ora il nostro modello è riparato. Nell\'albero del modello rendiamo Pad001 visibile e nascondiamo Pad, quindi possiamo vedere il modello corretto.

![](images/JschremppFCADEdit4.png )


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}} 
