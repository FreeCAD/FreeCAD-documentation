# Path ToolLibraryEdit/it
---
- GuiCommand:/it   Name:Path ToolLibraryEdit   Name/it:Gestione utensili   Workbenches:[[Path Workbench/it   Path]]|MenuLocation:Path → Gestione utensili   Shortcut:P,T   SeeAlso:---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

L\'editor della tabella utensili permette di modificare i diversi strumenti della tabella utensili contenuta nell\'oggetto macchina di una [Lavorazione](Path_Job/it.md). Questa tabella utensili è utilizzata per le diverse operazioni contenute nel progetto per ottenere le informazioni necessarie sullo strumento corrente.


</div>

Serve per selezionare lo strumento che si desidera utilizzare nella lavorazione.

![](images/Path-Tooltable.png )


<div class="mw-translate-fuzzy">

La gestione è semplice:

-   Import\...: Importa una tabella utensili da un file XML. {{Note|Avviso | Attualmente questo è in parte rovinato e non funziona se non si è mai usato un file xml prima.}}
-   Export\...: Esporta la tabella degli utensili in un file XML.
-   New Tool: Apre una finestra di dialogo in cui si può inserire i parametri dell\'utensile. Vedere [Nuovo utensile](Path_NewTool/it.md)
-   Delete: cancella le linee attualmente selezionate. {{Note| Avvertenza | Gli strumenti vengono cancellati dalla tabella degli utensili anche se si annulla la finestra di dialogo}}
-   Move up: Non è possibile modificare il numero dello strumento, ma è possibile spostare la linea selezionata verso l\'alto per diminuirne il numero
-   Move down: È possibile spostare la linea selezionata verso il basso per aumentare il numero dell\'utensile


</div>

-   Create Tool Controller(s): Quando si seleziona una o più caselle di controllo a sinistra nell\'elenco degli strumenti, questo pulsante diventa attivo. Cliccando, gli strumenti selezionati vengono inseriti nella lavorazione corrente.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una [Lavorazione](Path_Job/it.md)
2.  Premere il pulsante **<img src="images/Path_ToolLibraryEdit.png" width=16px> [Gestione utensili](Path_EditToolsTable/it.md)
**
3.  Creare dei nuovi utensili o modificare le proprietà di quelli esistenti.
    Impostare almeno il diametro, FreeCAD ne ha bisogno per calcolare la compensazione del raggio. A partire dalla versione 0.17 questo è l\'unico valore utilizzato per creare il percorso. Tuttavia, se si desidera utilizzare lo strumento di simulazione in un secondo momento, aggiungere anche l\'angolo e l\'altezza del tagliente.
    ![](images/Path-ToolAdd.gif )


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   Gli utensili possono essere riordinati utilizzando i pulsanti sposta-in-alto/basso
-   Tabelle complete di utensili possono essere importate da file xml (FreeCAD ha un proprio formato tooltable) o da tooltables HeeksCAD


</div>





{{Path_Tools_navi

}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolLibraryEdit/it
