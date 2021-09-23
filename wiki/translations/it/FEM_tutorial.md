# FEM tutorial/it



<div class="mw-translate-fuzzy">


{{TutorialInfo/it
|Topic=Analisi agli elementi finiti
|Level=base
|Time=10 minuti più il tempo del solutore
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
|FCVersion=0.16.6700 o superiore
|Files=
}}


</div>

## Introduction


<div class="mw-translate-fuzzy">

## Introduzione

Questo tutorial ha lo scopo di introdurre il lettore al flusso di lavoro di base dell\'ambiente FEM, nonché alla maggior parte degli strumenti disponibili per eseguire un\'analisi statica.


</div>

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">

## Requirements


<div class="mw-translate-fuzzy">

## Requisiti

-   Versione 0.16.6700 o superiore di FreeCAD.
-   [Netgen](http://sourceforge.net/projects/netgen-mesher/) e/o [GMSH](http://geuz.org/gmsh/) installati nel sistema.
-   Nel caso si usi GMSH installare la [Macro GMSH](Macro_GMSH.md) da [Addon manager](AddonManager/it.md), sviluppata da [psicofil](https://github.com/psicofil/Macros_FreeCAD).
-   [Calculix](http://www.calculix.de/) installato nel sistema.
-   Il lettore abbia le conoscenze di base per utilizzare gli ambienti [Parte](Part_Workbench/it.md) e [PartDesign](PartDesign_Workbench/it.md)


</div>

## Procedura

### Modeling


<div class="mw-translate-fuzzy">

### Il modello 

In questo esempio viene utilizzato un cubo come oggetto di studio, ma al suo posto si posssono usare i modelli creati con Parte o PartDesign.


</div>


<div class="mw-translate-fuzzy">

1.  Creare un nuovo documento
2.  Attivare l\'ambiente Part
3.  Creare un cubo
4.  Modificare le sue **Dimensions** in questi valori:
    1.  Height: 1.000 mm
    2.  Length: 8.000 mm
    3.  Width: 1.000 mm


</div>

Ora abbiamo un modello con il quale lavorare.

### Creating the Analysis 

#### Netgen


<div class="mw-translate-fuzzy">

### Creare l\'analisi 

#### Netgen 

1.  Selezionare il modello
2.  Dal menu cliccare su <img alt="" src=images/FEM_Analysis.png  style="width:16px;"> [Nuova analisi](FEM_Analysis/it.md) per creare un\'analisi dall\'oggetto selezionato.
3.  Nella finestra di meshing, fare clic su **OK**


</div>


<div class="mw-translate-fuzzy">

È anche possibile trascinare e rilasciare in una Analisi meccanica un oggetto mesh che non dispone di un mesh all\'interno della struttura ad albero.


</div>

#### GMSH


<div class="mw-translate-fuzzy">

#### GMSH 

Si consiglia l\'utilizzo della macro di psicofil che viene utilizzata per questo esempio.

1.  Attivare la macro
2.  Selezionare l\'oggetto che si desidera utilizzare, in questo caso il cubo
3.  Attivare la casella **Create Mechanical Analysis from mesh**
4.  Cliccare su **OK**


</div>

Ora abbiamo reso mesh il nostro oggetto e siamo pronti ad aggiungere i vincoli e le forze.

### Constraints and Forces 


<div class="mw-translate-fuzzy">

### Vincoli e Forze 

1.  Nascondere la mesh dalla Vista ad albero.
2.  Visualizzare il modello originale
3.  Selezionare <img alt="" src=images/FEM_FixedConstraint.png  style="width:16px;"> [Vincolo fissaggio FEM](FEM_ConstraintFixed/it.md)
4.  Selezionare la faccia posteriore del cubo (la faccia sugli assi **YZ**) e fare clic su OK
5.  Selezionare <img alt="" src=images/FEM_ForceConstraint.png  style="width:16px;"> [Vincolo forza FEM](FEM_ConstraintForce/it.md)
6.  Selezionare la faccia frontale del cubo (la faccia parallela a quella posteriore) e impostare il **Carico dell\'area** al valore di 9000000.00
7.  Impostare la **Direzione** **-Z** selezionando uno dei bordi della faccia parallela a quella direzione.
8.  Cliccare su OK


</div>

Con questo abbiamo stabilito i vincoli e le forze per lo studio statico.

### Final preparations 


<div class="mw-translate-fuzzy">

### Ultimi preparativi 

1.  Selezionare <img alt="" src=images/FEM_Material.png  style="width:16px;"> [Materiale FEM per solidi](FEM_MaterialSolid/it.md) e scegliere Calculix
2.  Cliccare su **OK**


</div>

### Running the Solver 

#### Standard Procedure 


<div class="mw-translate-fuzzy">

### Avviare il Solver 

#### Procedura Standard 

1.  Selezionare l\'oggetto solver <img alt="" src=images/FEM_Solver.png  style="width:16px;"> contenuto in 
**Mechanical Analysis**
2.  Selezionare <img alt="" src=images/FEM_Calculation.png  style="width:16px;"> [Calcola](FEM_SolverControl/it.md) nel menu
3.  Selezionare **Write Calculix Input File**
4.  Selezionare **Run Calculix**
5.  Cliccare **Chiudi**


</div>

#### Quick Procedure 


<div class="mw-translate-fuzzy">

#### Procedura veloce 

1.  Selezionare l\'oggetto solver <img alt="" src=images/FEM_Solver.png  style="width:16px;"> contenuto in 
**Mechanical Analysis**
2.  Cliccare su <img alt="" src=images/FEM_RunCalculiXccx.png  style="width:16px;"> [Analisi veloce](FEM_SolverRun/it.md).


</div>

### Analyzing Results 


<div class="mw-translate-fuzzy">

### Risultati delle analisi 

1.  Selezionare l\'oggetto **Risultati** nell**\'albero degli oggetti**
2.  Selezionare <img alt="" src=images/FEM_ShowResult.png  style="width:16px;"> [Mostra risultati](FEM_ResultShow/it.md)
3.  Scegliete tra i diversi tipi di risultati quello che si desidera visualizzare
4.  Il cursore in basso può essere utilizzato per modificare la visualizzazione della mesh. Questo permette di visualizzare la deformazione subita dall\'oggetto, ricordare che si tratta di una approssimazione.
5.  Per azzerare i risultati selezionare <img alt="" src=images/FEM_PurgeResults.png  style="width:16px;"> [Purge results](FEM_ResultsPurge/it.md)


</div>


{{Note|Confronto con precedenti file di esempio|Se si seleziona come tipo di risultato '''Z displacement''', si può vedere che il valore ottenuto è quasi identico all'esempio di prova fornita da FreeCAD. Le differenze possono verificarsi a causa della qualità della mesh e del numero di nodi che possiede.}}


<div class="mw-translate-fuzzy">

A questo punto il flusso di lavoro di base per il [Modulo FEM](FEM_Workbench/it.md) è terminato.


</div>


{{Tutorials navi

}} {{FEM Tools navi}} 
