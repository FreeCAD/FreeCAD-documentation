# DAG view/it


## Introduzione


{{TOCright}}

La [vista DAG](DAG_view/it.md) è un [grafico aciclico diretto](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG) che mostra le relazioni tra i diversi oggetti nel documento. Intende principalmente mostrare come determinati oggetti dipendono da altri in un modello complesso con molte funzioni e riferimenti, come quelli che possono essere creati con <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md).

La vista DAG assomiglia al grafico che può essere prodotto da un repository Git e dai suoi rami. Insieme allo [vista ad albero](tree_view/it.md) standard e al [grafico delle dipendenze](Std_DependencyGraph/it.md), la vista DAG è uno strumento per ispezionare la storia parametrica degli oggetti in un documento.

## Esempio

Un modello semplice verrà visto con diverse visualizzazioni.

![](images/FreeCAD_DAG_view_3D.png ) *Modello con forme 2D e 3D.*

<img alt="" src=images/FreeCAD_DAG_view_Tree_view.png ) ![](images/FreeCAD_DAG_view.png  style="width:" height="500px;">


*A sinistra: oggetti mostrati nella [vista ad albero](tree_view/it.md) standard. A destra: oggetti mostrati nella vista DAG.*

![](images/FreeCAD_DAG_view_Std_DependencyGraph.png )


*Relazioni tra gli oggetti mostrati nel [grafico delle dipendenze](Std_DependencyGraph/it.md).*

## Attivazione della vista DAG 

La vista DAG è stata introdotta nella versione 0.17 come funzionalità sperimentale per utenti esperti e sviluppatori, in modo che potessero risolvere i problemi di modelli complessi; pertanto, la vista DAG non è disponibile per impostazione predefinita.

Per disporre di questa vista usare l\'[editor dei parametri](Std_DlgParameter/it.md). Se non esiste creare il seguente sottogruppo

-    `BaseApp/Preferences/DockWindows/DAGView`
    

quindi aggiungere il parametro `Enabled` di tipo `Boolean`, e impostarlo su `True`.


<div class="mw-translate-fuzzy">

Quindi attivarlo, **{{StdMenu|[Visualizza](Std_View_Menu/it.md)** → Pannelli → Vista DAG}}.


</div>

Nell\'[editor dei parametri](Std_DlgParameter/it.md) si possono anche modificare alcune proprietà nei seguenti sottogruppi

-    `BaseApp/Preferences/DAGView`
    

-   FontPointSize - Imposta la dimensione del carattere del testo e può migliorare la leggibilità con display a alti DPI. Impostare su 0 per la dimensione del carattere predefinita.

-   SelectionMode
    -   0 - il singolo clic seleziona un elemento. Ctrl-clic per aggiungere elementi alla selezione.
    -   1 - ogni clic aggiunge / rimuove l\'elemento alla selezione.

-   Direction - l\'ordine in cui vengono visualizzati gli elementi.
    -   1 - figli in alto, genitore sotto di esso
    -   -1 - genitore in alto, figli sotto

## Link

-   [DAGView](https://forum.freecadweb.org/viewtopic.php?f=20&t=11276), thread del forum che presenta il nuovo strumento.
-   [easter egg of PartDesign Next: DAG View](https://forum.freecadweb.org/viewtopic.php?t=15375), includere la vista insieme all\'aggiornamento di PartDesign.


{{Interface navi

}} {{Std Base navi}} 
