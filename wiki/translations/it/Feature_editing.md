# Feature editing/it
## Introduzione


<div class="mw-translate-fuzzy">

Questa pagina spiega come utilizzare l\'ambiente <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign](PartDesign_Workbench/it.md) a partire da FreeCAD 0.17.


</div>



### Corpo


<div class="mw-translate-fuzzy">

Per lavorare in PartDesign è necessario creare innanzitutto un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[Corpo](PartDesign_Body/it.md)**. Un Corpo di PartDesign contiene una serie di schizzi, riferimenti (datum) e caratteristiche (feature) di PartDesign che formano un singolo solido contiguo.


</div>

<img alt="" src=images/PartDesign_Feature_example.png  style="width:400px;">



*Feature editing in practice. From left to right:<br>
Body with a [box](PartDesign_AdditiveBox.md) feature.<br>
Body with a box and a [chamfer](PartDesign_Chamfer.md) feature.<br>
Body with a box, a chamfer and a [pocket](PartDesign_Pocket.md) feature.*


<div class="mw-translate-fuzzy">

In un documento può essere attivo un solo corpo. Il corpo attivo ottiene le nuove funzioni che vengono create. Un corpo può essere attivato o disattivato facendo doppio clic su di esso. Un corpo attivato è evidenziato in azzurro. Il colore di evidenziazione può essere impostato nelle preferenze in Visualizzazione / Colori / Contenitore attivo dalla versione 0.18.


</div>

![](images/PartDesign_Body_tree.png )

### What is a contiguous solid? 


<div class="mw-translate-fuzzy">

Un **unico solido contiguo** è un elemento simile a una fusione od a qualcosa di ricavato da un unico blocco di metallo. Se l\'elemento coinvolge chiodi, viti, colla o saldature, non è un unico solido contiguo. Come esempio pratico, PartDesign non dovrebbe essere utilizzato per modellare una sedia di legno, ma può essere utilizzato per modellare i suoi sotto-componenti (gambe, doghe, sedile, ecc).


</div>

In FreeCAD version 1.0 an experimental property was introduced that allows the Body to have non-contiguous solids. This can also be set in the [Preferences](PartDesign_Preferences#General.md) as default for newly created Bodies. This is not intended to be used to build, as in the example, a chair in one Body. It is meant to allow features that may produce disconnected solids that will be made contiguous by later features.


<div class="mw-translate-fuzzy">

Quando un modello richiede più corpi, come il precedente esempio della sedia di legno, si può usare una <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Parte](Std_Part/it.md) per raggrupparli e spostare il tutto in una unica unità.


</div>



### Gestione della visibilità del corpo 


<div class="mw-translate-fuzzy">

Per impostazione predefinita, un corpo mostra solo la sua funzione più recente, cioè l\'ultima operazione eseguita. Di defualt, questa funzione è definita tip (cima o punta). Una buona analogia è l\'espressione \"la punta dell\'iceberg\": sopra l\'acqua è visibile solo la punta, la maggior parte della massa dell\'iceberg (le altre funzioni) è nascosta. Quando viene aggiunta una nuova funzione al corpo, la visibilità della funzione precedente viene disattivata e la nuova funzione diventa la punta del corpo.


</div>


<div class="mw-translate-fuzzy">

Può essere visibile una sola funzione alla volta. È possibile [attivare la visibilità](Std_ToggleVisibility/it.md) di qualsiasi funzione nel corpo, selezionandola nell\'albero del modello e premendo la barra spaziatrice, tornando praticamente indietro nella cronologia del corpo.


</div>



### Spostare e riordinare gli oggetti 


<div class="mw-translate-fuzzy">

È possibile ridefinire temporaneamente la punta su una funzione intermedia dell\'albero del corpo per inserire nuovi oggetti (funzioni, schizzi o geometrie di riferimento). È anche possibile riordinare le funzioni all\'interno di un corpo o spostarle in un corpo diverso. Selezionare l\'oggetto e fare clic con il tasto destro del mouse per ottenere un menu contestuale che offre entrambe le opzioni. L\'operazione può essere impedita se l\'oggetto ha dipendenze nel corpo di origine, come essere collegato a una faccia. Per spostare uno schizzo su un altro corpo, esso non dovrebbe contenere dei collegamenti a geometrie esterne.


</div>

<img alt="" src=images/PartDesign_workflow.svg  style="width:400px;">



*Schematic representation of the PartDesign workflow.*



## Geometrie di riferimento 


<div class="mw-translate-fuzzy">

Le geometrie di riferimento consistono in piani, linee, punti o forme esterne collegate. Possono essere create per essere utilizzati come riferimento da schizzi e funzioni. C\'è una moltitudine di possibilità di associare gli oggetti riferimenti.


</div>


<div class="mw-translate-fuzzy">

In FreeCAD, i piani di riferimento hanno senso se si posizionano gli schizzi (le estrusioni, le tasche, ecc.) in orientamenti non standard, cioè in piani sfalsati o ruotati intorno ai tre assi principali. Dato che gli schizzi possono essere posizionati anche in orientamenti non standard allo stesso modo dei piani di riferimento, spesso non c\'è bisogno di usare i piani di riferimento.


</div>


<div class="mw-translate-fuzzy">

Sia gli schizzi che i piani di riferimento dovrebbero essere attaccati ai piani di base. Il riferimento alla geometria generata (geometria che è il risultato di un\'operazione di creazione di un elemento, per esempio un estrusione o una tasca) dovrebbe essere evitato poiché le facce e gli spigoli vengono rinominati e rinumerati e i riferimenti non si riferiscono più alla stessa cosa. Questo si chiama instabilità topologica ed è dovuto al modo in cui FreeCAD utilizza alcune librerie geometriche esterne. Si spera che questo venga migliorato in futuro. (Vedi Consigli per creare modelli stabili qui sotto).


</div>



## Consigli per creare dei modelli stabili 


<div class="mw-translate-fuzzy">

L\'idea della modellazione parametrica implica che è possibile modificare i valori di alcuni parametri e che i passaggi successivi vengono modificati in base ai nuovi valori. Tuttavia, quando vengono apportate modifiche importanti, il modello può rovinarsi a causa del [problema della denominazione topologica](Topological_naming_problem/it.md) che in FreeCAD non è ancora stato risolto. Il danno può essere ridotto al minimo rispettando i seguenti criteri di progettazione:


</div>


<div class="mw-translate-fuzzy">

-   Evitare di attaccare schizzi e oggetti di riferimento alla geometria generata del modello. (La geometria generata è qualsiasi faccia o bordo creato come risultato di una estrusione, una tasca, ecc.)
-   Posiziona i tuoi schizzi su piani di coordinate standard o su piani di riferimento personalizzati collegati a piani standard.
    -   Gli schizzi collegati a piani/assi di coordinate di base o a piani di riferimento collegati a piani/assi di coordinate, non verranno inaspettatamente ricollegati a un riferimento diverso.
-   Quando si crea la geometria di riferimento, non attaccarla alla geometria generata.
    -   Attaccalo ai piani/assi standard e/o agli schizzi o agli oggetti di riferimento che usano offset di attacco ai piani/assi standard.
-   Usare uno \"schizzo principale\". Poiché uno schizzo principale è fatto prima del modello, esso fa riferimento solo ai piani/assi delle coordinate.
    -   Uno schizzo principale dovrebbe essere il più semplice possibile e contenere gli elementi geometrici di base del tuo modello.
    -   Gli elementi dello schizzo principale possono essere referenziati quando si modellano le caratteristiche successive.
    -   Uno schizzo master può essere il primo schizzo del corpo, o completamente fuori dal corpo.
    -   Uno schizzo principale può essere referenziato come geometria esterna o tramite una [Forma legata](PartDesign_ShapeBinder/it.md).
-   Non creare [Forme legate](PartDesign_ShapeBinder/it.md) dalla geometria generata
-   Tenete a mente che le [Forme legate](PartDesign_ShapeBinder/it.md) possono essere un problema quando la geometria viene cancellata dallo schizzo su cui è basata.
-   Se dovete inevitabilmente fare riferimento a una caratteristica intermedia, per esempio il risultato di un\'operazione di spessore
    -   Usa il primo riferimento possibile nell\'elenco delle caratteristiche successive in cui si trova l\'elemento geometrico di riferimento.
    -   Se prendete una caratteristica iniziale come riferimento, tutte le modifiche ai passi intermedi non rovineranno il vostro modello.
    -   Cercate di fare riferimento a uno schizzo o alla geometria dello schizzo piuttosto che alla geometria generata.
-   Usare gli *abbellimenti*, come raccordi e smussi, il più tardi possibile nell\'albero delle caratteristiche
-   Si noti che l\'uso di fogli di calcolo, dati dinamici, schizzi master, ecc. generalmente produce modelli più parametrici e aiuta ad evitare il problema della denominazione topologica.


</div>



## Tutorial


<div class="mw-translate-fuzzy">

La pagina [Tutorial](Tutorials/it.md) fornisce alcuni esempi di utilizzo del metodo [Editazione delle funzioni](Feature_editing/it.md) di <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md).

-   [Creare una parte semplice con PartDesign](Creating_a_simple_part_with_PartDesign/it.md)
-   [Esercitazioni di base di Part Design 019](Basic_Part_Design_Tutorial_019/it.md)
-   [Esercitazione di base sulle associazioni](Basic_Attachment_Tutorial/it.md)


</div>



## Correlazioni

-   [Geometria solida costruttiva](Constructive_solid_geometry/it.md)


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [PartDesign](Category_PartDesign.md) > Feature editing/it
