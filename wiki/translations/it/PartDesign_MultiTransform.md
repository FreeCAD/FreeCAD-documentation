---
- GuiCommand:/it
   Name:PartDesign_MultiTransform   Name/it:MultiTrasformazione
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:PartDesign → MultiTrasformazione
---


</div>

## Descrizione

Crea una combinazioni di trasformazioni - Lo strumento **![](images/)_Multitrasformazione**_utilizza_una_(o_una_serie_di)_funzioni_come_input_e_consente_all\'utente_di_applicare_progressivamente_più_trasformazioni_a_tale_funzione_(o_set_di_funzioni),_in_sequenza,_creando_una_trasformazione_combinata_o_composta.

Ad esempio, per produrre la flangia con una doppia fila di fori come mostrato di seguito:

1.  selezionare il foro come funzione (base) nella struttura del modello
2.  cliccare sull\'icona **![](images/) Multitrasformazione**
3.  aggiugere una serie lineare con due occorrenze nella direzione X.
4.  aggiungere una serie polare con otto occorrenze attorno all\'asse Y.

<img alt="" src=images/multitransform_example.png  style="width:600px;"> 
*Flangia con doppia fila di fori. Serie di fori creati con lo strumento 'Multitrasformazione'.*

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

Prima di iniziare uno dei metodi seguenti, assicurarsi che l\'oggetto **![](images/)_[Corpo](PartDesign_Body/it.md)** necessario sia [attivo](PartDesign_Body/it#Stato_attivo.md); in caso contrario, riceve un messaggio pop-up di errore che indica che è necessario un oggetto **![](images/)_[Corpo](PartDesign_Body/it.md)** attivo prima di usare lo strumento **![](images/)__Multitrasformazione**.


</div>

### Standard Method 


<div class="mw-translate-fuzzy">

### Metodo standard 

Questo metodo inizia senza funzioni di trasformazione esistenti e senza selezioni nella finestra o nella struttura del modello.
Quando questo metodo è completato l\'oggetto **<img src="images/PartDesign_MultiTransform.svg" width=16px> Multitrasformazione** dovrebbe diventare correttamente la \"Punta\" dell\'oggetto Body.


</div>


<div class="mw-translate-fuzzy">

1.  Cliccare sull\'icona **![](images/)  Multitrasformazione** per avviare l\'operazione
2.  Si apre la finestra per selezionare la funzione.
    Dall\'elenco, selezionare una funzione iniziale da utilizzare per le trasformazioni e fare clic su **OK** per procedere.
    È possibile aggiungere funzionià aggiuntive nel passaggio successivo.<img alt="" src=images/PartDesign-MultiTransform-Select_feature.png  style="width:300px;">
3.  Vengono visualizzate le finestre **Transformed features message** e **MultiTransform Parameters**.
    Si vede l\'etichetta della funzione selezionata nella vista Elenco funzioni, sotto i pulsanti ** Aggiungi funzione** e ** Rimuovi funzione**.<img alt="" src=images/PartDesign-MultiTransform-General.png  style="width:300px;">
    Se si desidera includere funzionalità aggiuntive per le trasformazioni, seguire queste istruzioni:
    1.  Cliccare su **Aggiungi funzione**
    2.  Passare alla vista ad albero del modello (fare clic sulla scheda **Modello**)
    3.  Selezionare la funzione che si desidera aggiungere e renderla visibile (barra spaziatrice, o clic con il pulsante destro del mouse e attiva la visibilità).
        **Nota:** Ciò nasconde la funzione precedentemente visibile.
    4.  Fare clic su qualsiasi cosa nella vista 3D.
    5.  Fare clic sulla scheda **Azioni** nella vista combinata per tornare alla finestra **Parametri MultiTransform**.
    6.  Si deve vedere l\'etichetta della funzione selezionata di recente nell\'elenco delle funzioni.
4.  Sotto la vista dell\'elenco delle caratteristiche è presente la vista dell\'elenco **Trasformazioni**. All\'interno si deve vedere il testo, \"Fare clic destro per aggiungere\".
5.  Aggiungere una trasformazione facendo clic con il pulsante destro del mouse nella vista elenco **Trasformazioni** per visualizzare l\'elenco delle opzioni.<img alt="" src=images/PartDesign-MultiTransform-Transformations_Right_Click.png  style="width:300px;">
    1.  Aggiungere la trasformazione desiderata selezionandola nell\'elenco delle opzioni.
    2.  La nuova voce di trasformazione viene visualizzata nell\'elenco **Trasformazioni** con le impostazioni corrispondenti visualizzate sotto l\'elenco.<img alt="" src=images/PartDesign-MultiTransform-Transformations-add_linear_pattern.png  style="width:300px;">
    3.  Regolare le impostazioni per la nuova trasformazione. (Si vede l\'anteprima nella finestra.)
    4.  Fare clic sul pulsante **OK** sotto queste impostazioni per salvare la nuova trasformazione.
6.  Continuare ad aggiungere trasformazioni nell\'ordine in cui si desidera applicarle utilizzando il passaggio 5 precedente.
7.  È inoltre possibile modificare, eliminare e spostare (modificare l\'ordine delle) trasformazioni secondo necessità facendo clic con il pulsante destro del mouse su una trasformazione nell\'elenco \"Trasformazioni\" e selezionando l\'opzione corrispondente.
8.  Quando si ha finito di aggiungere e modificare le trasformazioni, fare clic sul pulsante **OK** in alto per salvare la Multitrasformazione e uscire.


</div>

### Alternate Method 1 


<div class="mw-translate-fuzzy">

### Metodo alternativo 1 

Questo metodo inizia con una funzione di trasformazione esistente in oggetto **<img src="images/PartDesign_Body.svg" width=16px> [Corpo](PartDesign_Body/it.md)**.


</div>


<div class="mw-translate-fuzzy">

1.  Nella struttura del modello, all\'interno dell\'oggetto Body attivo, selezionare la trasformazione esistente da includere.
2.  Cliccare sull\'icona **![](images/)__Multitrasformazione**_per_avviare_l\'operazione.
3.  Nella vista Elenco funzioni, si vedono le etichette delle funzioni di trasformazione esistenti incluse.
    Per aggiungere altre funzioni, vedere al passaggio 3 del [Metodo standard](PartDesign_MultiTransform/it#Metodo_standard.md) above.
4.  Sotto la vista dell\'elenco delle funzioni è presente la vista dell\'elenco **Trasformazioni**. All\'interno si vede l\'etichetta della trasformazione esistente inclusa.
5.  Terminare usando passaggi 5-8 del [Metodo standard](PartDesign_MultiTransform/it#Metodo_standard.md) precedente.

Quando viene avviata e completata in questo modo, la **![](images/)_Multitrasformazione**_di_solito_non_riesce_a_diventare_la_\"Punta\"_dell\'oggetto_Corpo. Per correggere questo:

1.  Fare clic con il tasto destro del mouse sul nuovo oggetto **![](images/)_Multitrasformazione**.
2.  Scegliere \"Usa come entità finale\".


</div>

### Alternate Method 2 


<div class="mw-translate-fuzzy">

### Metodo alternativo 2 

Questo metodo inizia con più funzioni di trasformazioni indipendenti esistenti nell\'oggetto **![](images/)_[Corpo](PartDesign_Body/it.md)** - con l\'idea di combinarli. **NOTA:** per combinare delle trasformazioni esistenti, esse devono trovarsi all\'interno dello stesso oggetto Corpo e dovrebbero usare tutte la stessa funzione o set di funzioni.


</div>


<div class="mw-translate-fuzzy">

1.  Nell\'albero del modello, all\'interno dell\'oggetto Corpo attivo, selezionare una delle trasformazioni esistenti tra quelle che si desidera includere.
2.  Cliccre sull\'icona **![](images/)_Multitrasformazione**_per_avviare_l\'operazione.
3.  Cliccare sul pulsante **OK** per salvare e uscire.
4.  Nell\'albero degli oggetti selezionare il nuovo oggetto **![](images/)_Multitrasformazione**.
5.  Nella finestra Proprietà, individuare la proprietà \"Trasformazioni\" nella scheda \"Dati\".
6.  Modificare la proprietà **Trasformazioni** facendo clic sul suo valore, quindi fare clic sulla casella dell\'ellisse visualizzata per aprire la finestra **Collegamenti** per questa proprietà.
7.  Selezionare tutte le trasformazioni esistenti che devono essere incluse. Selezioni multiple sono consentite usando **Ctrl** + clic.
8.  Cliccare su **OK** per salvare e chiudere la finestra **Collegamenti**.
9.  Cliccare sul pulsante **![](images/)_[Aggiorna](Std_Refresh/it.md)** se è attivo.

Quando viene avviata e completata in questo modo, la **![](images/)_Multitrasformazione**_potrebbe_non_diventare_la_\"Punta\"_dell\'oggetto_Body. Se è necessario che sia la \"Punta\":

1.  Fare clic con il tasto destro del mouse sul nuovo oggetto **![](images/)_Multitrasformazione**.
2.  Scegliere \"Usa come entità finale\".


</div>

### Usage Notes 


<div class="mw-translate-fuzzy">

### Note d\'uso 

-   Trasformazioni di funzioni supportate sono: **<img src="images/PartDesign_Mirrored.svg" width=20px> [Specchiato](PartDesign_Mirrored/it.md)**, **<img src="images/PartDesign_LinearPattern.svg" width=20px> [Serie lineare](PartDesign_LinearPattern/it.md)**, **<img src="images/PartDesign_PolarPattern.svg" width=20px> [Serie polare](PartDesign_PolarPattern/it.md)**, e la Scalatura.
-   Ogni trasformazione legata alla **![](images/)_Multitrasformazione**_deve_utilizzare_la_stessa_funzione_o_set_di_funzioni_in_ciascuna_di_esse.


</div>

### Limitations


<div class="mw-translate-fuzzy">

### Limitazioni

-   Una trasformazione di scala non dovrebbe essere la prima della lista
-   La trasformazione di scala deve avere lo stesso numero di occorrenze della trasformazione immediatamente precedente nella lista
-   Vedere la funzione **<img src="images/PartDesign_LinearPattern.svg" width=20px> [Schiera lineare](PartDesign_LinearPattern/it.md)** per altre limitazioni





</div>

## Options


<div class="mw-translate-fuzzy">

## Opzioni

+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/Partdesign_Multitransfrom_parameters_it.png ) | Quando si crea una operazione di MultiTrasformazione, la finestra di dialogo **Parametri MultiTrasformazione** mostra due elenchi in campi diversi (Originali e Trasformazioni).                                                                                                                                                                                                                                                 |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | #### Selezionare gli originali                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | La finestra Vista combinata mostra la lista delle operazioni (oggetti) originali che devono essere trasformati. Fare clic su una operazione per aggiungerla alla lista.                                                                                                                                                                                                                                                          |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | #### Selezionare le trasformazioni                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | In questo elenco si possono inserire delle combinazioni di trasformazioni semplici quali [simmetria](PartDesign_Mirrored/it.md), [schiera lineare](PartDesign_LinearPattern/it.md), [schiera polare](PartDesign_PolarPattern/it.md) e [scalatura](PartDesign_Scaled/it.md). Le trasformazioni saranno applicate nell\'ordine una dopo l\'altra. Il menu di scelta rapida offre le seguenti voci: |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | #### Modifica                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | Permette di modificare i parametri di una trasformazione nella lista (un doppio clic produce lo stesso effetto)                                                                                                                                                                                                                                                                                                                  |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | #### Elimina                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | Rimuove una trasformazione dalla lista                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | #### Aggiungi trasformazione                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | Aggiunge una trasformazione alla lista                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | #### Sposta su o giù                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                | Permette di cambiare l\'ordine delle trasformazioni nella lista                                                                                                                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+





</div>

### Select originals 

The list view shows the \'originals\', the features that are to be patterned. Clicking on any feature will add it to the list.

### Select transformations 

This list can be filled with a combination of the simple transformations [mirrored](PartDesign_Mirrored.md), [linear pattern](PartDesign_LinearPattern.md), [polar pattern](PartDesign_PolarPattern.md) and [scaled](PartDesign_Scaled.md). The transformations will be applied one after the other. The context menu offers the following entries:

#### Edit

Allows editing the parameters of a transformation in the list (double-clicking will have the same effect)

#### Delete

Removes a transformation from the list

#### Add transformation 

Adds a transformation to the list

#### Move Up/Down 

Allows changing the order of transformations in the list \|}

## Examples


<div class="mw-translate-fuzzy">

## Esempi

![c\|800px](images/mt_example2.png )


*Il blocco più piccolo viene prima modellato tre volte in direzione X e poi scalato per un fattore due (in modo che alle tre occorrenze venga applicato il fattore di scala 1.0, 1.5 e 2.0). In seguito viene eseguita una schiera polare con 8 occorrenze.*

![c\|800px](images/mt_example3.png )


*Lo scavo viene prima riflesso sul piano YZ e poi si applicano due trasformazioni di schiera lineare per produrre una schiera rettangolare.*





</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}} 
