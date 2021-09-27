# Feature editing/it
{{TOCright}}

## Introduzione

Questa pagina spiega come utilizzare l\'ambiente <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign](PartDesign_Workbench/it.md) a partire da FreeCAD 0.17.

Mentre l\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md) e altri ambienti di FreeCAD costruiscono i modelli combinando insieme delle forme (vedere [Geometria solida costruttiva](Constructive_solid_geometry/it.md)), l\'ambiente <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> PartDesign usa le **funzioni (features)**. Una [feature](https://en.wikipedia.org/wiki/Feature_recognition) è un\'operazione che modifica la forma di un modello.

## Metodologia di editazione delle funzioni 

La prima funzione è chiamata comunemente **funzione di base**. Quando si aggiungono ulteriori funzioni al modello, ogni funzione prende la forma precedente e vi aggiunge o rimuove del materiale, creando delle dipendenze lineari tra una funzione e quella successiva. In effetti, questa metodologia simula un comune processo di produzione: un blocco viene tagliato su un lato, quindi su un altro lato, vengono aggiunti dei fori, poi dei raccordi, ecc.

Tutte le funzioni sono elencate in sequenza nell\'albero del modello e possono essere modificate in qualsiasi momento. L\'ultima funzione che è situata nella parte inferiore rappresenta la parte finale.

Le funzioni possono essere ordinate in diverse categorie:

-   **Basata su profili**: queste funzioni partono da un profilo per definire la forma dell materiale da aggiungere o rimuovere. Il profilo può essere costituito da uno schizzo, una faccia planare sulla geometria esistente (il profilo viene estratto dai suoi bordi), un oggetto Forma legata o un oggetto Draft che è stato incluso nel corpo attivo.

-   **Additiva**: aggiunge del materiale al modello esistente. Le funzioni additive vengono visualizzate con icone gialle.

-   **Sottrattiva**: rimuove la materia dal modello esistente. Le funzioni sottrattive vengono visualizzate con icone rosse e blu.

-   **Basata su primitive**: basata su primitive geometriche (cubo, cilindro, cono, toro \...). Possono essere additive o sottrattive.

-   **Funzioni di trasformazione**: applicano una trasformazione a delle funzioni esistenti (riflessione, schiera lineare, schiera polare, multitrasformazione).

-   **Abbellimento**: funzioni che applicano un trattamento ai bordi o alle facce, come raccordo, arrotondamento, smusso e sformo.

-   **Procedurale**: si può dire delle caratteristiche che non sono basate su schizzi, come le funzioni di trasformazione e di abbellimento.

### Corpo

Per lavorare in PartDesign è necessario creare innanzitutto un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[Corpo](PartDesign_Body/it.md)**. Un Corpo di PartDesign contiene una serie di schizzi, riferimenti (datum) e caratteristiche (feature) di PartDesign che formano un singolo solido contiguo.

![](images/PartDesign_Body_tree.png )

Un **unico solido contiguo** è un elemento simile a una fusione od a qualcosa di ricavato da un unico blocco di metallo. Se l\'elemento coinvolge chiodi, viti, colla o saldature, non è un unico solido contiguo. Come esempio pratico, PartDesign non dovrebbe essere utilizzato per modellare una sedia di legno, ma può essere utilizzato per modellare i suoi sotto-componenti (gambe, doghe, sedile, ecc).

In un documento di FreeCAD possono essere creati più corpi che possono poi anche essere combinati per formare un singolo solido contiguo.

In un documento può essere attivo un solo corpo. Il corpo attivo ottiene le nuove funzioni che vengono create. Un corpo può essere attivato o disattivato facendo doppio clic su di esso. Un corpo attivato è evidenziato in azzurro. Il colore di evidenziazione può essere impostato nelle preferenze in Visualizzazione / Colori / Contenitore attivo dalla versione 0.18.

Quando un modello richiede più corpi, come il precedente esempio della sedia di legno, si può usare una <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Parte](Std_Part/it.md) per raggrupparli e spostare il tutto in una unica unità.

### Gestione della visibilità del corpo 

Per impostazione predefinita, un corpo mostra solo la sua funzione più recente, cioè l\'ultima operazione eseguita. Di defualt, questa funzione è definita tip (cima o punta). Una buona analogia è l\'espressione \"la punta dell\'iceberg\": sopra l\'acqua è visibile solo la punta, la maggior parte della massa dell\'iceberg (le altre funzioni) è nascosta. Quando viene aggiunta una nuova funzione al corpo, la visibilità della funzione precedente viene disattivata e la nuova funzione diventa la punta del corpo.

Può essere visibile una sola funzione alla volta. È possibile [attivare la visibilità](Std_ToggleVisibility/it.md) di qualsiasi funzione nel corpo, selezionandola nell\'albero del modello e premendo la barra spaziatrice, tornando praticamente indietro nella cronologia del corpo.

### Origine del Corpo 

Il corpo ha un\'origine composta dai piani di riferimento (XY, XZ, YZ) e dagli assi (X, Y, Z) che possono essere utilizzati dagli schizzi e dalle funzioni. Gli schizzi possono essere collegati ai piani Origine e non è più necessario associarli a facce planari per le funzioni basate su di essi che si vuole aggiungere o sottrarre dal modello.

### Spostare e riordinare gli oggetti 

È possibile ridefinire temporaneamente la punta su una funzione intermedia dell\'albero del corpo per inserire nuovi oggetti (funzioni, schizzi o geometrie di riferimento). È anche possibile riordinare le funzioni all\'interno di un corpo o spostarle in un corpo diverso. Selezionare l\'oggetto e fare clic con il tasto destro del mouse per ottenere un menu contestuale che offre entrambe le opzioni. L\'operazione può essere impedita se l\'oggetto ha dipendenze nel corpo di origine, come essere collegato a una faccia. Per spostare uno schizzo su un altro corpo, esso non dovrebbe contenere dei collegamenti a geometrie esterne.

### Differenza con altri sistemi CAD 

Una differenza fondamentale tra FreeCAD e altri programmi, come Catia, è che FreeCAD non permette di avere più solidi disconnessi nello stesso <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Corpo](PartDesign_Body/it.md). Cioè, una nuova funzione dovrebbe sempre essere costruita sopra quella precedente. O detto in un modo diverso, la nuova funzione deve \"toccare\" la funzione precedente, in modo che entrambe le funzioni siano fuse insieme e diventino un singolo solido. Non si possono avere solidi \"fluttuanti\".

<img alt="" src=images/PartDesign_Body_non-contiguous.png  style="width:550px;">


*Differenza tra Catia e FreeCAD. A sinistra: Catia consente di scollegare i corpi dalle funzioni precedenti del corpo. In FreeCAD questo causa un errore; A destra:  la nuova funzione deve sempre toccare o intersecare la funzione precedente, in modo che sia fusa con essa e diventi un unico solido contiguo.*

## Geometrie di riferimento 

Le geometrie di riferimento consistono in piani, linee, punti o forme esterne collegate. Possono essere create per essere utilizzati come riferimento da schizzi e funzioni. C\'è una moltitudine di possibilità di associare gli oggetti riferimenti.

In alcuni sistemi CAD è possibile definire un piano di riferimento che è sfalsato rispetto al corpo precedente e creare un solido disconnesso. Pertanto, posizionare molti piani di riferimento e creare oggetti su di essi è corretto e non causa un errore. In genere, alla fine si regolano i piani nelle loro posizioni finali, in modo che i singoli oggetti siano fusi insieme.

In FreeCAD, come menzionato nella sezione precedente, i solidi scollegati **non** sono ammessi, quindi uno schizzo su un piano di riferimento che crea un solido non contiguo fallirà.

In FreeCAD, i piani di riferimento hanno senso se si posizionano gli schizzi (le estrusioni, le tasche, ecc.) in orientamenti non standard, cioè in piani sfalsati o ruotati intorno ai tre assi principali. Dato che gli schizzi possono essere posizionati anche in orientamenti non standard allo stesso modo dei piani di riferimento, spesso non c\'è bisogno di usare i piani di riferimento.

I piani di riferimento hanno senso se ci sarà più di uno schizzo con lo stesso orientamento non standard. In questo caso un piano di riferimento può essere usato e l\'orientamento deve essere regolato solo per il piano di riferimento al fine di modificare tutti gli schizzi associati e le caratteristiche create dagli schizzi.

Sia gli schizzi che i piani di riferimento dovrebbero essere attaccati ai piani di base. Il riferimento alla geometria generata (geometria che è il risultato di un\'operazione di creazione di un elemento, per esempio un estrusione o una tasca) dovrebbe essere evitato poiché le facce e gli spigoli vengono rinominati e rinumerati e i riferimenti non si riferiscono più alla stessa cosa. Questo si chiama instabilità topologica ed è dovuto al modo in cui FreeCAD utilizza alcune librerie geometriche esterne. Si spera che questo venga migliorato in futuro. (Vedi Consigli per creare modelli stabili qui sotto).

Anche se non sono utilizzati per il supporto di schizzi, gli oggetti di riferimento possono essere utili come indicatori visivi, per attirare l\'attenzione su delle caratteristiche o distanze importanti nel processo di modellazione. (Anche se, semplicemente aggiungendo la geometria a uno schizzo, si ottiene un feedback visivo simile).

<img alt="" src=images/PartDesign_Body_non-contiguous_slanted.png  style="width:550px;">


*Differenza tra Catia e FreeCAD. A sinistra: Catia consente di scollegare i corpi dalle funzioni precedenti del corpo. In FreeCAD questo causa un errore;  A destra: la nuova funzione dovrebbe sempre toccare o intersecare la funzione precedente, in modo che sia fusa con essa e diventi un solido contiguo. In questo esempio, il nuovo solido si basa su un piano di Riferimento ruotato attorno all'asse Y.*

## Riferimenti incrociati 

È possibile fare riferimento a elementi da un corpo all\'altro attraverso le geometrie di riferimento. Ad esempio, Forma legata può copiare come riferimento le facce di un corpo in un altro corpo. Questo dovrebbe rendere più facile modellare una scatola e il suo coperchio in due corpi separati. FreeCAD offre un aiuto per evitare collegamenti accidentali ad altri corpi chiedendoti una conferma del tue intenzioni.

## Associazione

L\'oggetto Associazione non è uno strumento specifico di PartDesign, ma piuttosto un\'utilità di Part introdotta in v0.17 che si può trovare nel menu Part. È molto utilizzato nell\'ambiente PartDesign per allegare schizzi e geometrie di riferimento ai piani e agli assi standard del corpo. Sono disponibili dei modi molto completi per creare punti di riferimento, linee e piani. I parametri opzionali di offset dell\'associazione rendono questo strumento molto versatile.

Per maggiori informazioni si può consultare la pagina [Associazione](Part_Attachment/it.md) e [Esercitazione di base sulle associazioni](Basic_Attachment_Tutorial/it.md).

## Consigli per creare dei modelli stabili 

L\'idea della modellazione parametrica implica che è possibile modificare i valori di alcuni parametri e che i passaggi successivi vengono modificati in base ai nuovi valori. Tuttavia, quando vengono apportate modifiche importanti, il modello può rovinarsi a causa del [problema della denominazione topologica](topological_naming_problem/it.md) che in FreeCAD non è ancora stato risolto. Il danno può essere ridotto al minimo rispettando i seguenti criteri di progettazione:

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

## Flusso di lavoro per la costruzione di un corpo 

Con [PartDesign](PartDesign_Workbench/it.md) sono possibili diversi flussi di lavoro. Quello che dovrebbe sempre essere rispettato è che tutte le funzioni create all\'interno di un [Corpo](PartDesign_Body/it.md) siano fuse insieme per ottenere l\'oggetto finale.

### Schizzi diversi 

Gli schizzi devono essere supportati da un piano. Questo piano può essere uno dei piani principali (XY, XZ o YZ) definiti dall\'origine del corpo. Uno schizzo può essere estruso in un solido positivo (additivo), con uno strumento come <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> _. Il primo aggiunge volume alla forma finale del corpo, mentre il secondo taglia il volume dalla forma finale. In questo modo è possibile creare qualsiasi numero di schizzi e parti solide parziali; la forma finale (tip) è il risultato della fusione di queste operazioni insieme. Naturalmente, il corpo non può consistere in sole operazioni sottrattive, poiché la forma finale dovrebbe essere un solido con un volume positivo diverso da zero.

<img alt="" src=images/PartDesign_workflow_1.svg  style="width:600px;">

### Funzioni sequenziali 

Gli schizzi possono essere supportati dalle facce delle precedenti operazioni solide. Questo può essere necessario per accedere a una faccia che è disponibile solo dopo aver creato una determinata funzione. Tuttavia, questo flusso di lavoro non è consigliato, poiché se la funzione originale viene modificata, le funzioni successive nella sequenza potrebbero interrompersi. Questo è il caso di un [problema di denominazione topologica](topological_naming_problem/it.md).

<img alt="" src=images/PartDesign_workflow_2.svg  style="width:600px;">

### Utilizzo di piani di riferimento per il supporto 

I piani di riferimento sono utili per supportare gli schizzi. Questi piani ausiliari dovrebbero essere collegati ai piani di base del corpo.

\'\'Nota: in molti casi, uno schizzo attaccato a un piano di base con offset di attacco può realizzare la stessa funzione. Le origini sono particolarmente utili quando più schizzi o altri costrutti useranno l\'origine. Ciò significa che tutte le modifiche all\'origine saranno applicate agli schizzi allegati, ecc. Aggiungere un singolo schizzo a un\'origine, piuttosto che usare gli offset di associazione nelle proprietà dello schizzo, è un passo in più ed è in fondo ridondante. \'\'

Come per gli schizzi, è possibile attaccare i piani di riferimento alla geometria generata (bordi, facce di solidi creati in precedenza), **\'\' ma questo non è raccomandato**\'\' poiché può causare il problema della denominazione topologica.

Inoltre, una <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:24px;"> [Forma legata](PartDesign_ShapeBinder/it.md) può essere usata per importare la geometria esterna nel corpo di riferimento; in seguito gli schizzi possono essere uniti a questo corpo ausiliario, usando o meno i piani di riferimento.

*Di nuovo, Forma legata dovrebbe essere basato sugli schizzi del corpo precedente, non sulla geometria generata.*

L\'uso degli oggetti datum è spesso il modo migliore per produrre modelli stabili, se usato con piani di base e offset di attacco, anche se richiede un po\' più di lavoro da parte dell\'utente. Per i dettagli sul collegamento di base, vedere: [Esercitazione di base sulle associazioni](Basic_Attachment_Tutorial/it.md) *Nota: mentre questo tutorial parla di schizzi, il collegamento dei dati è fatto in modo simile.*

## Tutorial

La pagina _.

-   [Creare una parte semplice con PartDesign](Creating_a_simple_part_with_PartDesign/it.md)
-   [Basi di Part Design](Basic_Part_Design_Tutorial/it.md)
-   [Esercitazione di base sulle associazioni](Basic_Attachment_Tutorial/it.md)

## Correlati

-   [Geometria solida costruttiva](Constructive_solid_geometry/it.md)

<img alt="" src=images/PartDesign_workflow_3.svg  style="width:600px;">


{{PartDesign Tools navi

}} 

_

---
[documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > Feature editing/it
