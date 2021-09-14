# FEM CalculiX Cantilever 3D/it




<div class="mw-translate-fuzzy">


{{TutorialInfo/it
|Topic= Analisi Elementi Finiti
|Level= Base
|Time= 10 minuti
|Author=[http://www.freecadweb.org/wiki/index.php?title=User:Berndhahnebach Bernd]
|FCVersion=0.16.6377 o superiore
|Files=
}}


</div>

## Introduction


<div class="mw-translate-fuzzy">

## Introduzione

Questo esempio ha lo scopo di mostrare come appare una semplice analisi degli elementi finiti (FEA) e in che modo i risultati possono essere visualizzati nel [modulo FEM](FEM_Workbench/it.md) di FreeCAD. Viene mostrato come attivare una FEA e come modificare il valore e la direzione del carico. Inoltre, poiché il file di esempio è fornito con tutte le installazioni di FreeCAD, è facile verificare se il modulo FEM è impostato correttamente.


</div>

<img alt="" src=images/FEM_example01_pic00.jpg  style="width:700px;">

## Requirements


<div class="mw-translate-fuzzy">

## Requisiti

-   Una versione di FreeCAD compatibile con quella utilizzata per il tutorial.
-   La versione installata può essere verificata nel menu **Aiuto → Informazioni su FreeCAD**.
-   Per caricare il file di esempio non è necessario nessun altro software esterno, e neppure per visualizzare la mesh o la geometria, o per visualizzare i risultati.
-   Per poter rieseguire l\'analisi FEA è necessario che il software risolutore Calculix sia installato. Probabilmente il risolutore è già stato installato con FreeCAD. Se non è installato vedere la pagina [Installare FEM](FEM_Install/it.md).


</div>

## Impostare il file di esempio 

### Load Start Workbench 


<div class="mw-translate-fuzzy">

### Caricare l\'ambiente Start 

-   Avviare FreeCAD
-   L\'ambiente Start dovrebbe essere caricato


</div>

### Load the example file 


<div class="mw-translate-fuzzy">

### Caricare il file di esempio 

-   Andare ai progetti di esempio e fare clic su \"Carica un esempio di analisi FEM\"
-   Se con le operazioni successive succede di rovinare o eliminare alcune geometrie, vincoli, o risultati, basta ripetere semplicemente i passaggi precedenti.


</div>

<img alt="" src=images/FEM_example01_pic01.jpg  style="width:700px;">

### Activate the analysis container 


<div class="mw-translate-fuzzy">

### Attivare il contenitore delle analisi 

-   Per lavorare con una analisi, prima si deve attivarla.
-   Nella vista ad albero fare clic destro su <img alt="" src=images/Fem_Analysis.png  style="width:32px;"> Analisi meccanica → Attiva analisi


</div>

<img alt="" src=images/FEM_example01_pic02.jpg  style="width:700px;">

### Analysis container and its objects 


<div class="mw-translate-fuzzy">

### Il contenitore Analisi e suoi oggetti 

-   Se viene attivata l\'analisi FreeCAD cambia l\'ambiente corrente in FEM.
-   Per eseguire un\'analisi meccanica statica sono necessari almeno 5 oggetti.
-   <img alt="" src=images/Fem_Analysis.png  style="width:32px;"> contenitore dell\'analisi

1.  <img alt="" src=images/FEM_Solver.png  style="width:32px;"> un solutore
2.  <img alt="" src=images/FEM_Material.png  style="width:32px;"> un materiale
3.  <img alt="" src=images/Fem_ConstraintFixed.png  style="width:32px;"> un vincolo fissaggio
4.  <img alt="" src=images/Fem_ConstraintForce.png  style="width:32px;"> un vincolo forza
5.  <img alt="" src=images/FEM_Create.png  style="width:32px;"> un oggetto mesh FEM

-   In questo esempio sono inclusi anche i risultati quindi c\'è un sesto oggetto, cioè i risultati <img alt="" src=images/FEM_ShowResult.png  style="width:16px;">.


</div>

### Visualizing Results 


<div class="mw-translate-fuzzy">

### Visualizzare i risultati 

-   Assicurarsi che l\'analisi sia attivata.
-   Assicurarsi che l\'analisi contenga ancora l\'oggetto risultato, altrimenti basta ricaricare il file di esempio.
-   Nella barra degli strumenti fare clic sull\'icona <img alt="" src=images/FEM_ShowResult.png  style="width:16px;"> [Mostra risultati](FEM_ResultShow/it.md)
-   Nella scheda Azioni scegliere z-Displacement. Mostra -88.443 mm nella direzione z negativo.
-   Questo ha senso dal momento che anche la forza è in direzione Z negativo.
-   Attivare la casella di controllo \"Mostra\", a fianco del cursore in basso per visualizzare lo spostamento.
-   Il cursore può essere utilizzato per modificare la mesh e visualizzare la deformazione in modo semplificato.
-   Scegliere tra i diversi tipi di risultati per vedere nella GUI tutti i tipi di risultati disponibili.


</div>

<img alt="" src=images/FEM_example01_pic03.jpg  style="width:400px;">

### Purging Results 


<div class="mw-translate-fuzzy">

### Eliminare i risultati 

-   Assicurarsi che l\'analisi sia attivata.
-   Per rimuovere i risultati selezionare nella barra l\'icona <img alt="" src=images/FEM_PurgeResults.png  style="width:32px;"> [Elimina risultati](FEM_ResultsPurge/it.md)


</div>

### Running the FEA 


<div class="mw-translate-fuzzy">

### Eseguire la FEA 

-   Nella vista ad albero fare doppio click sull\'oggetto solver <img alt="" src=images/FEM_Solver.png  style="width:32px;">.
-   Nella finestra Azioni dell\'oggetto risolutore accertarsi che sia selezionata l\'analisi statica.
-   Nella stessa scheda, cliccare su \"Scrivi il file .inp\". Attendere che nella finestra del rapporto compaia la scritta \"write completed\".
-   Cliccare su **Esegui CalculiX**. Poiché questa è una breve analisi dovrebbe essere eseguita in meno di un secondo.
-   Nella finestra di testo dovrebbe essere stampato a caratteri verdi \"CalculiX done!\" e nella riga successiva \"loading result sets \...\"
-   Se non ci sono dei messaggi di errore si è conclusa la prima FEA in FreeCAD.
-   Cliccare su **Chiudi** nella scheda Azioni.
-   Questo dovrebbe aver creato un nuovo oggetto risultato. Abbiamo già visto come visualizzare i risultati.
-   Se si riceve un messaggio di errore \"no solver binary\" o simile quando si avvia l\'analisi consultare la pagina [FEM Install](FEM_Install/it.md).


</div>

<img alt="" src=images/FEM_example01_pic04.jpg  style="width:400px;">

### Running the FEA the fast Way 


<div class="mw-translate-fuzzy">

### Eseguire velocemente la FEA 

-   Nella vista ad albero selezionare l\'oggetto risolutore <img alt="" src=images/FEM_Solver.png  style="width:32px;"> dell\'analisi <img alt="" src=images/FEM_Analysis.png  style="width:32px;">.
-   Nella barra degli strumenti cliccare sull\'icona <img alt="" src=images/FEM_RunCalculiXccx.png  style="width:32px;"> [Analisi rapida](FEM_SolverRun/it.md).
-   Viene scritto il file Calculix di input, viene attivato Calculix e viene creato l\'oggetto risultato.


</div>

### Changing Load Direction and Load Value 


<div class="mw-translate-fuzzy">

### Modificare la Direzione e il Valore del carico 

-   Nella vista ad albero selezionare l\'oggetto mesh FEM <img alt="" src=images/FEM_Create.png  style="width:32px;"> e premere il tasto spazio.
    -   **Risultato:** L\'oggetto mesh FEM viene nascosto, e rimane visibile solo il modello geometrico.
-   Nella vista ad albero fare doppio click sull\'oggetto \"Vincolo forza\" per aprire la sua finestra Azioni.
-   Nella finestra Azioni cambiare il valore del carico 500000000 N = 500 MN (nella finestra Azioni l\'unità di misura della forza deve essere in N)
-   Cliccare sul pulsante **Direzione**.
-   Sul modello geometrico Cliccare su uno dei bordi lunghi in direzione x.
    -   **Risultato:** Le frecce rosse della forza cambiano direzione e si orientano in direzione x. Esse mostrano la direzione fissata.
-   Dato che la tensione deve essere applicata nel verso opposto bisogna attivare il controllo \"Reverse direction\".
-   Le frecce rosse della forza cambiano il loro verso.
-   Fare clic su **OK** nella finestra delle Azioni.

<img alt="" src=images/FEM_example01_pic05.jpg  style="width:700px;">

-   Attivare la visibilità della mesh FEM <img alt="" src=images/FEM_Create.png  style="width:32px;"> selezionandola nella vista ad albero e premendo il tasto spazio.
-   Abbiamo già visto come attivare un\'analisi e come visualizzare i risultati.
-   La deformazione in direzione x dovrebbe essere di 19.05 mm.


</div>

<img alt="" src=images/FEM_example01_pic05.jpg  style="width:700px;">

-   Toggle the [visibility](Std_ToggleVisibility.md) of the FEM mesh <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> \'On\' by selecting it in tree view and pressing the **Space** key.
-   You know how to trigger an analysis and how to visualize results already.
-   The deformation in x-direction should be 19.05 mm.

<img alt="" src=images/FEM_example01_pic06.jpg  style="width:400px;">

## What next? 


<div class="mw-translate-fuzzy">

## Cos\'altro ?

-   Il flusso di lavoro di base per l\'ambiente [FEM](FEM_Workbench/it.md) è finito.
-   Ora si è pronti per eseguire il secondo [Tutorial di FEM](FEM_tutorial/it.md).
-   Creeremo da soli un Calculix di una trave a sbalzo e confronteremo i risultati con la teoria delle travi.


</div>


{{Tutorials navi

}} {{FEM Tools navi}} 
