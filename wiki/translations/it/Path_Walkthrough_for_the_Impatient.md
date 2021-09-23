# Path Walkthrough for the Impatient/it
<div class="mw-translate-fuzzy">


{{TutorialInfo/it
|Topic=Ambiente Path
|Level=
|Time=
|Author=Chrisb
|FCVersion=
|Files=
}}


</div>

## Aim


<div class="mw-translate-fuzzy">

Ecco una dimostrazione che mostra la creazione di una lavorazione del WB Path da un modello 3D, generando un codice G nel dialetto corretto per una macchina CNC di destinazione.


</div>

## Il modello 3D 


<div class="mw-translate-fuzzy">

Il progetto inizia con un semplice modello di FreeCAD: un cubo con una tasca rettangolare,


</div>


<div class="mw-translate-fuzzy">

![](images/Path-SquarePocketModel.png )


</div>


<div class="mw-translate-fuzzy">

creato nell\'ambiente [Part Design](PartDesign_Workbench/it.md) e formato da un corpo, un cubo con una tasca basata su uno schizzo orientato nel piano XY.


</div>


<div class="mw-translate-fuzzy">

Completato il Modello 3D, selezionare l\'ambiente Path.


</div>


<div class="mw-translate-fuzzy">

## La lavorazione 

Cliccare su <img alt="" src=images/Path-Job.png  style="width:32px;"> [Lavorazione](Path_Job/it.md) per crearne una.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-JobCreationDialog.png )


</div>


<div class="mw-translate-fuzzy">

Nella finestra di dialogo Crea lavorazione, fare clic su OK per accettare il Corpo come modello base, senza usare nessun modello.


</div>

### Impostazione della lavorazione 


<div class="mw-translate-fuzzy">

Nella tabella Azioni si apre la finestra Job Edit e la vista del modello mostra il pezzo grezzo incorniciato dalle linee di un cubo attorno al Corpo base. La scheda selezionata è quella delle Impostazione.


</div>

### Job Output 


<div class="mw-translate-fuzzy">

La scheda Output definisce il percorso del file di output, il suo nome e la sua estensione e definisce anche il Postprocessore. Per utenti esperti, è possibile definire gli argomenti dell\'algoritmo di post-elaborazione: posizionando il mouse sopra i campi appaiono i suggerimenti per gli argomenti più comuni.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-JobOutput.png )


</div>

### Job Tools 


<div class="mw-translate-fuzzy">

![](images/Path-JobTools.png )


</div>


<div class="mw-translate-fuzzy">

Modifichiamo lo strumento predefinito selezionandolo e facendo clic sul pulsante Modifica. Questo apre la finestra di modifica del Tool Controller.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-ToolConfig.gif )


</div>


<div class="mw-translate-fuzzy">

Il nome assegnato all\'utensile e il numero dell\'utensile corrispondono al numero dell\'utensile della macchina. Qui lo strumento è il Nr. 4. Il controller dell\'utensile è configurato per avanzamenti orizzontali e verticali di 2mm/s e una velocità del mandrino di 2000 rpm.


</div>


<div class="mw-translate-fuzzy">

Selezionare il pannello secondario Tool del controller dell\'utensile. Impostare il diametro e - se si desidera utilizzare lo strumento di simulazione in un secondo momento - aggiungere l\'angolo del tagliente e l\'altezza del tagliente.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-ToolAdd.gif )


</div>


<div class="mw-translate-fuzzy">

Confermare i valori con OK.


</div>


<div class="mw-translate-fuzzy">

Per un facile accesso, tutti gli utensili possono essere predefiniti e selezionati dal [Gestore degli utensili](Path_EditToolsTable/it.md).


</div>

### Job Workplan 


<div class="mw-translate-fuzzy">

La scheda Piano di lavoro inizia vuota e viene popolata dalla sequenza delle Operazioni della lavorazione, dai Comandi di percorso parziale e dai Dressup dei percorsi. La sequenza di queste voci iene ordinata in questa scheda.


</div>

Questo è albero che viene mostrato dopo la configurazione della lavorazione dopo che il percorso è stato aperto:


<div class="mw-translate-fuzzy">

![](images/Path-TreeWithJob.png )


</div>

## Le operazioni del percorso 


<div class="mw-translate-fuzzy">

Vengono ora aggiunte due operazioni per generare i percorsi di fresatura di questa lavorazione. L\'operazione [Contornatura](Path_Contour/it.md) crea un percorso attorno al cubo e l\'operazione [Tasca](Path_Pocket_Shape/it.md) crea un percorso per la tasca interna.


</div>


<div class="mw-translate-fuzzy">

Per ora facciamo una cosa semplice. Il pulsante <img alt="" src=images/Path_Profile.png  style="width:32px;"> [Contornatura](Path_Contour/it.md) apre il pannello Contour. Dopo aver confermato l\'uso dei valori predefiniti con OK, il percorso verde attorno all\'oggetto diventa visibile.


</div>


<div class="mw-translate-fuzzy">

Selezionare il fondo della tasca e poi il pulsante <img alt="" src=images/Path_Pocket.png  style="width:32px;"> [Tasca](Path_Pocket_Shape/it.md) per aprire la finestra Pocket Shape. Vengono utilizzati i valori predefiniti per Geometria di base, Profondità e Altezza e viene selezionato il pannello secondario Operazione e la percentuale di passata è impostata su 50.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-PocketOperation.gif )


</div>


<div class="mw-translate-fuzzy">

Cambiare Pattern in \"Offset\" e confermare con OK la Job Operation per la configurazione della tasca.


</div>

Il risultato è un modello con due percorsi:


<div class="mw-translate-fuzzy">

![](images/Path-WalkThroughResult.gif )


</div>

## Verificare i percorsi 

Esistono due modi per verificare i percorsi creati. Il codice G può essere ispezionato, inclusa l\'evidenziazione dei segmenti di percorso corrispondenti. Il processo di fresatura di Path Job può anche essere simulato per determinare i percorsi utensile ideali, richiesti dalle geometrie dell\'utensile per fresare il pezzo.


<div class="mw-translate-fuzzy">

Per ispezionare il codice G, utilizzare lo strumento <img alt="" src=images/Path_Inspect.png  style="width:32px;">. Selezionare le corrispondenti righe del codice G all\'interno della finestra di ispezione del codice G per evidenziare i singoli segmenti del percorso.

![](images/Path-InspectWindow.gif )


</div>


<div class="mw-translate-fuzzy">

Per iniziare la simulazione usare lo strumento <img alt="" src=images/Path_Simulator.png  style="width:32px;"> [Simulazione](Path_Simulator/it.md).


</div>


<div class="mw-translate-fuzzy">

Regolare la velocità e la precisione e avviare la simulazione con il pulsante di riproduzione.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-Simulation.gif )


</div>


<div class="mw-translate-fuzzy">

Se si desidera terminare la simulazione, fare clic sul pulsante Annulla per rimuovere lo pezzo creato per la simulazione. Cliccando su Ok questo oggetto viene conservato nella lavorazione.


</div>

## Postelaborare la lavorazione 

Il passaggio finale per generare il G-Code per la fresatura è di postelaborare il la lavorazione. Questo produce i codici G in un file che può essere caricato nel controllore macchina CNC di destinazione. Per richiamare il postprocessore:


<div class="mw-translate-fuzzy">

-   Selezionare l\'oggetto Job nell\'albero
-   Selezionare lo strumento Path Postprocessing <img alt="" src=images/Path_PostProcess.png  style="width:32px;"> per postelaborare il file. Si apre una finestra di codice G che consente l\'ispezione del file di output finale prima che venga salvato.


</div>


<div class="mw-translate-fuzzy">

![](images/Path-PostOutput.gif )


</div>


{{Tutorials navi

}} {{Path Tools navi}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path Walkthrough for the Impatient/it
