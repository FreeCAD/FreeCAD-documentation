---
- GuiCommand:/it
   Name:Path_Job
   Name/it:Lavorazione
   Workbenches:[Path](Path_Workbench/it.md)
   MenuLocation:Path → Lavorazione
   Shortcut:**P** **F**
   SeeAlso:
---

# Path Job/it


</div>

## Descrizione

Lo strumento Lavorazione (Job) crea un nuovo oggetto Lavorazione nel documento attivo. Esso contiene le seguenti informazioni:

1.  Un elenco di definizioni dei parametri degli utensili (Tool-Controller), che specifica la geometria, i movimenti e le velocità degli utensili per le Operazioni Path.
2.  Un elenco sequenziale del flusso di lavoro delle Operazioni Path.
3.  Un corpo base: un clone utilizzato per l\'offset.
4.  Un Pezzo (Stock), che rappresenta la materia prima che verrà fresata nell\'ambiente Path.
5.  Un foglio di lavorazione (SetupSheet), contenente gli input utilizzati dalle operazioni percorso, inclusi valori statici e le formule.
6.  I parametri di configurazione che specificano il percorso di destinazione, il nome e l\'estensione del file G-Code prodotto dalla lavorazione, nonché il Postprocessore utilizzato per generare il dialetto appropriato per il controller CNC di destinazione e i parametri per personalizzare Unità, Cambi di utensile, Soste, ecc.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Richiamare il comando Lavorazione utilizzando uno dei seguenti metodi:
    -   Premere il pulsante **<img src="images/Path_Job.svg" width=16px> [Lavorazione](Path_Job/it.md)** nella barra degli strumenti.
    -   Utilizzare la scorciatoia da tastiera **P** quindi **F**.
    -   Usare la voce **Path → Lavorazione** del menu principale.


</div>

La finestra di dialogo della GUI della lavorazione ha cinque schede allineate orizzontalmente: **General**, **Output**, **Setup**, **Tools**, e **Workplan**. L\'utente può in qualsiasi momento utilizzare le opzioni **OK** o **Annulla** nella finestra di dialogo.

## General

![](images/Job_1.jpg )

-   **Label**: L\'etichetta della lavorazione come visualizzata nella vista ad albero.
-   **Model**: L\'oggetto base che tramite la sua forma definisce i percorsi della lavorazione. Se si tratta di un oggetto Part Design, solitamente è il corpo che si seleziona qui. Se nell\'albero c\'è un elemento selezionato prima di fare clic sull\'icona \"Aggiungi lavorazione\" quell\'elemento è già stato inserito qui. È possibile cambiarlo selezionando un elemento diverso dal menu a discesa.
-   **Description**: Qui è possibile aggiungere alcune note alla lavorazione. Le note sono solo informative e non hanno alcun effetto sul percorso.

## Output

![](images/Job_2.jpg )

-   **Output File**: Imposta il nome, l\'estensione e il percorso del file dell\'output di G-Code. È possibile utilizzare i seguenti segnaposto:
    -   **%D** directory del documento attivo
    -   **%d** nome del documento attivo (senza estensione)
    -   **%M** directory macro utente
    -   **%j** nome della lavorazione

-   **Processor**: Selezionare il postprocessore per la propria macchina.
-   **Arguments**: Aggiungere gli argomenti di cui il postprocessore ha bisogno.

## Setup

![](images/Job_3.jpg )

-   **Stock**: imposta la dimensione e la forma del pezzo grezzo.
-   **Orientation**: il bordo o la faccia selezionati vengono usati per orientare di conseguenza la base o il pezzo grezzo.
-   **Alignment**: selezionare un vertice per impostare l\'origine o spostare la base o il pezzo grezzo.

## Utensili

![](images/Job_4.jpg )


<div class="mw-translate-fuzzy">

Aggiunge gli utensili necessari per le operazioni di questa lavorazione dalla [Tabella utensili](Path_ToolLibraryEdit/it.md).


</div>

Dopo aver aggiunto uno strumento, è possibile impostare o modificare l\'avanzamento e la velocità del mandrino se in questa lavorazione è necessario un avanzamento diverso. Le modifiche apportate qui non modificano i parametri memorizzati nella tabella.

Lo strumento predefinito può essere eliminato se è stato aggiunto un proprio strumento.

## Flusso di lavoro 

![](images/Job_5.jpg )

Se si dispone di una lavorazione composta da più operazioni percorso, è possibile determinare in quale ordine eseguire le operazioni. Per riordinare, selezionare un\'operazione e premere il pulsante su o giù.


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path Job/it
