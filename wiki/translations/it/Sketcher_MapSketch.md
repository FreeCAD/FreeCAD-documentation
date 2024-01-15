---
 GuiCommand:
   Name: Sketcher MapSketch
   Name/it: Mappa Schizzo
   MenuLocation: Part Design/Schizzo , Mappa schizzo su faccia...
   Workbenches: Sketcher_Workbench/it, PartDesign_Workbench/it
   SeeAlso: Sketcher_NewSketch/it
---

# Sketcher MapSketch/it



## Descrizione

Questo strumento mappa uno schizzo esistente sulla faccia di una forma. Le funzionalità di PartDesign create da questo schizzo verranno fuse con il solido sottostante per le funzionalità aggiuntive (Pad, Rivoluzione) o verranno sottratte dal solido sottostante in caso di funzionalità sottrattive (Tasca, Scanalatura).

Notare che questo strumento non serve per creare i nuovi disegni. Mappa o rimappa uno schizzo esistente alla faccia di un solido o di una funzione PartDesign. Casi d\'uso tipici sono:

-   Lo schizzo è stato creato su un piano standard (XY, XZ, YZ) e si desidera mapparlo sulla faccia di un solido al fine di costruire una funzione su di esso.
-   Lo schizzo è stato mappato su una faccia di un solido, ma è necessario associarlo ad una faccia diversa.
-   Riparazione di un modello rovinato.

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">



## Utilizzo

-   Selezionare la faccia di un oggetto PartDesign o di un solido.
-   Fare clic sull\'icona **<img src="images/Sketcher_MapSketch.svg" width=16px> [Mappa schizzo su faccia](Sketcher_MapSketch/it.md)** nella barra degli strumenti (o andare al menu PartDesign o Schizzo a seconda dell\'ambiente di lavoro attivo )
-   Nella finestra di dialogo **Seleziona schizzo** che si apre, selezionare dall\'elenco lo schizzo da mappare sulla faccia e fare clic su OK.
-   Lo schizzo viene aperto automaticamente in modalità di modifica.



## Uso per riparare un modello rovinato 

Mappa schizzo viene spesso utilizzato durante la riparazione di un modello danneggiato.

Un caso d\'uso comune è quando il grafico delle dipendenze è stato rovinato. (Si può visualizzare il grafico delle dipendenze da **Strumenti** → **[Grafico delle dipendenze](Std_DependencyGraph/it.md)**). Questo può accadere quando si elimina una funzione nel mezzo dell\'albero del modello. Nell\'esempio seguente interromperemo e ripareremo un modello.

Questo è il modello base. Ha un pad, una tasca e un pad all\'interno della tasca. Notare che il grafico delle dipendenze è lineare.

![](images/JschremppFCADEdit1.png )

Ora abbiamo eliminato la tasca e lo schizzo che ha creato la tasca (Pocket e Sketch001). Notare che ora il grafico delle dipendenze è interrotto. Per riparare questo modello, vogliamo attaccare Sketch002 alla faccia superiore del Pad. Nella vista del modello si può vedere che sarebbe facile selezionare la faccia sbagliata.

![](images/JschremppFCADEdit2.png )

Per riparare il modello, prima cambiamo la visibilità dei solidi. Nascondiamo Pad001 e rendiamo visibile Pad.

![](images/JschremppFCADEdit3.png )

Ora selezioniamo la faccia superiore di Pad e quindi selezioniamo lo strumento Mappa schizzo su faccia. Nella finestra di dialogo che appare selezioniamo Sketch002. Ora il nostro modello è riparato. Nell\'albero del modello rendiamo Pad001 visibile e nascondiamo Pad, quindi possiamo vedere il modello corretto.

![](images/JschremppFCADEdit4.png )





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher MapSketch/it
