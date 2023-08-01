# Path ExportTemplate/it
---
- GuiCommand:/it   Name:Path ExportTemplate   Name/it:Esporta modello   Workbenches:[MenuLocation:Path → Esporta modello   SeeAlso:[[Path_SetupSheet/it|Path SetupSheet](Path_Workbench/it___Path]].md) ---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

L\'esportazione dei modelli di lavorazione fornisce un comodo meccanismo per salvare le definizioni delle lavorazioni usate comunemente da una lavorazione esistente. Ciò facilita la configurazione delle lavorazioni future, che sono in gran parte simili, consentendo l\'importazione dei modelli di lavoro durante il processo di creazione della lavorazione.


</div>


<div class="mw-translate-fuzzy">

Nella tabella Modifica-\>Preferenze\...-\>Path-\>Job Preferences, Defaults-\>Template è impostato il modello predefinito.


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

Creare un modello

1.  Da qualsiasi lavorazione configurata, richiamare il comando <img alt="" src=images/Path-ExportTemplate.png  style="width:16px;"> [Esporta modello](Path_ExportTemplate/it.md) dal menu Path-\>, oppure facendo clic con il pulsante destro del mouse sul nodo Lavorazione (Job) nella Vista combinata.
2.  Selezionare gli elementi da includere nella finestra di dialogo di configurazione di Esporta modello.
3.  Fare clic su OK e salvare il modello. Il nome del modello deve seguire lo schema job\_.json Quando viene mostrato nella casella combinata di selezione, il prefisso job e l\'estensione non vengono mostrati. Affinché Path possa accedere ai modelli bisogna salvarli nella directory Macro o nella directory Path, secondo come configurato nelle Preferenze di Path.


</div>



## Opzioni

## Post Processing 


<div class="mw-translate-fuzzy">

## Post Processore 

-   Selezione del postprocessore
-   Argomenti del postprocessore
-   Nome del file di output


</div>

## Stock


<div class="mw-translate-fuzzy">

## Pezzo

-   Extent: dimensione del pezzo
-   Placement: posizione del pezzo


</div>

## Setup Sheet 


<div class="mw-translate-fuzzy">

## Impostazioni del foglio di lavorazione 

-   Profondità di lavorazione
-   Profondità di passata
-   Velocità di movimento rapido dello strumento


</div>

## Tool controllers 


<div class="mw-translate-fuzzy">

## Controller dell\'utensile 

-   Controller degli utensili selezionati.


</div>





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ExportTemplate/it
