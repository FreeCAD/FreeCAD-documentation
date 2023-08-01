---
- TutorialInfo:   Topic:Modeling
   Level:Experienced User
   Author:NormandC
   Time:
   FCVersion:0.19.23300 or higher
   Files:
---

# PartDesign Bearingholder Tutorial I/it





**This tutorial was originally written for a now deprecated development version of FreeCAD. This tutorial requires a complete rewrite to align with the PartDesign changes that will be in the upcoming v0.17 release.**





![Bearing Holder Tutorial - Supporto per cuscinetto finito(top)\|thumb\|right\|400px](images/HolderTop1-1.jpg )

## Seconda parte del tutorial 

[PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II/it.md)

Questa è la prima parte del tutorial. Usa il flusso di lavoro che può essere chiamato del \"corpo unico\", in questo esempio si utilizza solamente la parte superiore del supporto.

Ovviamente, per seguire questo tutorial è necessario attivare l\'ambiente PartDesign.

~~Potete trovare la versione di Jrheinlaender (l\'autore di questo articolo) della parte creata con questo tutorial a [http://ubuntuone.com/5gok0J4dye3Fo4BKWMGWVa questo link](http://ubuntuone.com/5gok0J4dye3Fo4BKWMGWVa_questo_link.md).~~ *Il file non è più disponibile, ne verrà fornito uno nuovo in un secondo momento*.

## Dati di progetto 

Il supporto deve essere in grado di contenere un cuscinetto di 90 mm di diametro con una larghezza fino a 33 mm (ad esempio, DIN 630 tipo 2308). Il cuscinetto richiede una spalla alta almeno 4,5 mm nel supporto (e sull\'albero). La parte superiore del supporto è imbullonata al fondo con due bulloni di 12 mm. A fianco del cuscinetto ci deve essere una scanalatura su entrambi i lati capace di contenere un anello di tenuta standard sull\'albero DIN 3760: 38x55x7 o 40x55x7 su un lato e 50x68x8 sull\'altro lato.

Il supporto sarà prodotto con un getto in sabbia con uno spessore minimo della parete di 5 mm, un angolo di sforno con di 2 gradi e un raggio di raccordo minimo di 3 mm .

## Impostazione della geometria di scheletro 

![Supporto per cuscinetto con i due più importanti piani dello scheletro\|thumb\|right\|text-top\|400px](images/HolderTop1-2.jpg )

La geometria scheletro serve per catturare le dimensioni su cui si basa la progettazione in una singola funzione di riferimento (ad esempio un piano o un asse). In questo modo, quando si vuole variare le dimensioni del progetto, tutto ciò che si deve fare è di cambiare le funzioni dello scheletro. Se il modello è ben costruito, allora tutte le sue funzioni sono ricalcolate e riflettono le modifiche apportate al progetto. Questo riduce il pericolo che in un modello complesso, in cui le dimensioni di base del progetto sono utilizzate in più posti, si dimentichi di cambiarle da qualche parte.

L\'alternativa alla geometria scheletro è quella di avere una tabella delle dimensioni di base del progetto che assegna un nome simbolico ad ogni dimensione e poi utilizzare il nome simbolico ovunque sono richieste le dimensioni per costruire il modello. FreeCAD non permette ancora questo approccio.

![Piani di base e tutti i piani di Riferimento\|thumb\|right\|text-top\|400px](images/HolderTop1-3.jpg )

Nel caso del supporto del cuscinetto, le due dimensioni di progettazione più importanti sono la distanza tra i bulloni (che limita la grandezza del cuscinetto che può essere utilizzato) e l\'altezza delle teste dei bulloni. Le dimensioni scelte sono

-   Distanza tra i bulloni: raggio del cuscinetto (45) + spessore parete (5) + raggio del foro per il bullone (7) = 57 mm, per cui il piano verticale sarà scostato (offset) di 57 mm dal piano YZ. Per creare questo piano di riferimento, selezionare il piano YZ e poi scegliere di creare un nuovo piano di riferimento. Inserire l\'offset nella finestra di dialogo che si apre quando si crea il piano
-   Altezza delle teste dei bulloni: questo piano è stato scelto con un offset di 28 mm dal piano XZ

Per comodità, possono essere creati due ulteriori piani di riferimento per riflettere la quantità di materiale che deve essere asportata dai fianchi del supporto del cuscinetto. Essi sono scostati di +22 e -22 dal piano XY.

Si consiglia di dare dei nomi esplicativi alle geometrie dello scheletro. Spesso si vuole disattivare la visibilità dei piani di riferimento perché ingombrano lo schermo, e se i piani hanno nomi auto-esplicativi si possono semplicemente selezionare nell\'albero tramite il nome invece che dallo schermo.

## La geometria del solido 

<img alt="Sketch del primo pad" src=images/HolderTop1-4.jpg  style="width:400px;"> Ora è il momento di iniziare a creare un po\' di geometria reale. Lo schizzo del primo pad (estrusione) è mostrato a destra. Esso è posizionato sul piano XY. Ci sono solo tre dimensioni: il raggio interno (22,5 mm), il sovrametallo alla base con un offset di 3 mm dal piano XZ e la distanza di 7 mm dal piano di riferimento che rappresenta l\'asse del bullone. In questo modo, se in seguito si sposta il piano di riferimento, il pad (l\'estrusione) setta automaticamente il proprio raggio esterno. Ricordare che prima di poter utilizzare il piano di riferimento per il dimensionamento, è necessario inserirlo nello schizzo come geometria esterna.

Probabilmente vi starete chiedendo perché vi è un piccolo segmento rettilineo in fondo a ciascun arco. Questo segmento garantisce che sarà possibile creare sugli archi uno sformo con un angolo di 2 gradi. Questo potrebbe sembrare un lavoro eccessivo per ottenere un vantaggio minimo, ma molti programmi CAD (e forse un giorno anche FreeCAD) dispongono di strumenti che evidenziono un modello solido in diversi colori e mostrano subito tutte le facce dove l\'angolo di sformo non è corretto. Certamente non si vuole che al proprio modello accada questo, soprattutto dopo avervi aggiunto un sacco di raccordi!

Dopo aver fatto il disegno (che è un po\' complicato a causa delle linee tangenziali per lo sformo di 2 gradi), basta estruderlo simmetricamente al piano dello schizzo con una lunghezza di 62 mm: 34 mm per il cuscinetto, 2x9 mm per gli anelli di tenuta, 2x5 mm per lo spessore della parete.
<img alt="Schizzo della parte da asportare dal fianco dell\'estrusione" src=images/HolderTop1-5.jpg  style="width:400px;"> Ora si vuole asportare sull\'esterno del materiale in corrispondenza degli anelli di tenuta in quanto il loro diametro esterno è molto inferiore a quello del cuscinetto. Il modo più semplice per creare i disegni necessari per questa operazione è quello di selezionare il disegno del pad e poi scegliere \"Duplica selezione\" dal menu \"Modifica\". Dopo è possibile rimappare il disegno su un fianco del pad, e modificarlo come indicato in figura.

Le uniche due dimensioni importanti di questo disegno sono i 3 mm di sovrametallo sul fondo e il diametro interno di 78 mm: 68 mm per il diametro esterno dell\'anello di tenuta + 2x5 mm spessore. Poiché l\'anello di tenuta sul lato opposto ha un diametro di 55 mm qui il diametro per l\'asportazione può essere di 65 mm.

Dopo aver creato il disegno, creare uno scavo fino al piano di riferimento che rappresenta il lato del cuscinetto più 5 mm per lo spessore. Volendo modificare il supporto in modo che sia in grado di contenere cuscinetti più larghi basta cambiare i dati di questi piani di riferimento e la profondità dello scavo si adatta di conseguenza.
<img alt="Sketch dello scavo interno al pad" src=images/HolderTop1-6.jpg  style="width:400px;"> Per ridurre il numero di lavorazioni meccaniche richieste, vogliamo anche asportare del materiale all\'interno del supporto. Anche in questo caso è conveniente duplicare lo schizzo del primo pad. Non ha neppure bisogno di essere rimappato. Anche in questo caso, le uniche dimensioni importanti sono il sovrametallo (3 mm) e il diametro esterno: 84 mm nel caso in cui il cuscinetto sia (90 mm - 2x sovrametallo), 49 mm per l\'anello di tenuta più piccolo (55 mm - 2x3 mm) e 62 mm per l\'anello di tenuta più grande.

Dopo aver creato gli schizzi, usarli per creare uno scavo: simmetricamente di 28 mm per creare lo spazio per il cuscinetto (34 mm - 2x sovrametallo) e di 23 mm su un solo lato per alloggiare gli anelli di tenuta: 34/2 mm per la metà della larghezza del cuscinetto + 9 mm per gli anelli di tenuta - 3 mm di sovrametallo.
<img alt="Geometria principale della parte superiore del supporto" src=images/HolderTop1-7.jpg  style="width:400px;"> La parte dovrebbe apparire come nell\'immagine a destra. Notare come i diversi scavi si combinano per produrre un spessore pressoché uniforme, cosa che renderà il getto più facile e meno suscettibile ad avere dei pori.
<img alt="Sketch con il disegno della parte per i bulloni" src=images/HolderTop1-8.jpg  style="width:400px;"> Ora non rimane che creare il materiale attraverso cui far passare i bulloni. Si potrebbe essere tentati di delinearlo con un cerchio e poi di estrude il cerchio, ma questo sarebbe causa di problemi quando in seguito si tentasse di basare lo sformo su di loro (suppongo che sia una debolezza di OpenCascade). Quindi, per aggirare i problemi, è meglio creare uno schizzo con l\'angolo di sformo incluso e poi ruotarlo di 360 gradi.

Anche qui piani scheletro tornano utili. Servono il piano dell\'asse del bullone e il piano della testa del bullone come geometrie esterne. Perciò, creare una linea retta per l\'asse di rotazione e assicurarsi che sia vincolata al piano di riferimento dell\'asse del bullone. Commutarla in geometria di costruzione. Poi, definire il resto del contorno. Le dimensioni importanti sono il sovrametallo in alto e in basso e il raggio di 12 mm: 7mm per il raggio del foro + 5 mm di spessore.
<img alt="Geometria finita della parte superiore del supporto (senza sformi e raccordi)" src=images/HolderTop1-9.jpg  style="width:400px;"> Creare una funzione di rivoluzione dal disegno e poi rifletterla sul piano YZ. Questa è tutta la geometria solida che si deve modellare. Il resto sono sformi e raccordi.

## Applicare uno sformo alla faccia laterale 

<img alt="Il piano neutro per creare gli sformi" src=images/HolderTop1-10.jpg  style="width:400px;"> Il passo successivo è quello di applicare gli sformi su tutte le facce. È importante considerare la posizione del piano neutro, cioè il piano intorno al quale la faccia è \"ruotata\". Se scegliamo come piano neutro il fondo del supporto avremo un problema con lo spessore della parete nella parte superiore del supporto. Quindi, creiamo un piano di riferimento con un offset di 40 mm dal piano XZ come compromesso tra la parte superiore del supporto che diventa più sottile e il fondo che diventa più spesso.
<img alt="Applicare uno sformo alla faccia laterale del supporto" src=images/HolderTop1-11.jpg  style="width:400px;"> Per applicare uno sformo su una faccia, selezionare la faccia e creare la funzione di sformo. È anche possibile selezionare più facce su cui applicare contemporaneamente lo sformo. Se si tratta una parte grande, è meglio applicare lo sformo solo su una faccia alla volta. Questo perchè se si modifica la geometria e uno sformo fallisce, fallisce solo questa funzione, mentre se si inseriscono tutte le facce in una unica funzione di sformo, può fallire l\'intera funzione a causa del fallimento di una sola faccia. Per una parte piccola come è il supporto del cuscinetto, è sufficiente creare due funzioni di sformo: una per le quattro facce esterne, e una per le facce interne.

La finestra di dialogo costringe a scegliere un piano neutro prima di completare l\'operazione. È possibile lasciare il campo della direzione di estrazione vuoto, in questo caso la direzione sarà normale al piano neutro. Non dimenticare di impostare l\'angolo di sformo pari a 2 gradi.

## Raccordare gli spigoli del supporto 

<img alt="Racccordo della parte che deve contenere i bulloni" src=images/HolderTop1-13.jpg  style="width:400px;"> Ora si possono raccordare gli spigoli della parte. L\'immagine mostra la prima serie di raccordi. Iniziare con i raccordi circolari piccoli e crearli con un raggio di 4 mm. Anche se secondo le specifiche 3 mm sono sufficienti, usando un raggio di 4 mm dopo la lavorazione rimane ancora 1 mm di raccordo e il bordo prodotto dalla lavorazione risulta meno tagliente. I raccordi grandi hanno un raggio di 6 mm per contribuire a distribuire la forza dai bulloni al resto della parte. Sarebbe bene usare un raggio ancora più grande, ma purtroppo OpenCascade non può ancora gestire i raccordi sovrapposti.

Come per lo sformo, in una parte complessa si dovrebbe eseguire il raccordo su un solo spigolo alla volta per evitare inutili errori quando viene modificata la geometria di base.
<img alt="Raccordare l\'esterno del supporto" src=images/HolderTop1-12.jpg  style="width:400px;"> Gli altri raccordi hanno semplicemente un raggio di 3 mm. Guardando l\'immagine a destra, i due raccordi evidenziati potrebbero effettivamente essere raccordati con 5 mm per ottenere uno spessore più uniforme per la fusione. Dopo la lavorazione, sarebbe comunque rispettato lo spessore minimo di 5 mm. Ma ancora una volta il fatto che OpenCascade non può gestire i raccordi sovrapposti impedisce di fare questo per il raccordo compreso tra i due raccordi evidenziati.
<img alt="Raccordare l\'interno del supporto - bordo problematico" src=images/HolderTop1-14.jpg  style="width:400px;"> Raccordare l\'interno della parte presenta delle difficoltà che non possono essere risolte con gli attuali strumenti dell\'ambiente PartDesign. Il bordo evidenziato non può essere raccordato, ancora una volta, perché gli arrotondamenti si sovrappongono. Questo potrebbe essere risolto creando una operazione di sweep al posto di un raccordo, ma sweep non è ancora implementato in PartDesign. Per il momento, siamo costretti a lasciare il bordo come è.
<img alt="La parte con i bordi arrotondati (tranne per il bordo impossibile)" src=images/HolderTop1-15.jpg  style="width:400px;"> L\'immagine a destra mostra il pezzo finito nello stato in cui si trova prima della lavorazione (ad eccezione di quello spigolo che è impossibile arrotondare). Notare che il bordo che gira intorno a tutta la base della parte è stato lasciato apposta non raccordato. Questo è il bordo dove il fondo e la parte superiore dello stampo si uniscono. Qui, non è possibile nessun raccordo (e comunque non è richiesto).

## Lavorazioni

<img alt="Lavorazione della parte superiore e inferiore del supporto" src=images/HolderTop1-16.jpg  style="width:400px;"> <img alt="Lavorazione della parte interna del supporto" src=images/HolderTop1-17.jpg  style="width:400px;"> Ora è possibile asportare il materiale che verrà tolto dalla parte in ghisa grezza durante la lavorazione. Questo è molto facile con la geometria definita scheletro. L\'idea è di creare tutte le caratteristiche della lavorazione (Tasche e Scanalature) utilizzando solo operazioni di riferimento. In questo modo esse saranno totalmente indipendenti dalla geometria solida del supporto per cuscinetto, cosa che ci dà alcuni grandi vantaggi:

-   Non importa come si cambia la geometria solida, le funzioni per la lavorazione non possono mai fallire.
-   È possibile creare la geometria di lavorazione prima di finalizzare il solido, e questo dà utili feedback visivi.
-   Se si spostano i piani scheletro di riferimento, allora sia la geometria solida che la lavorazione si adatteranno automaticamente.
-   Se si commette un errore nella geometria solida la lavorazione è ancora nella posizione corretta e molto probabilmente l\'errore diventa lampante (ad esempio lo spessore della parete che diventa di 2 mm invece che di 5 mm). Invece, se si riferisce la lavorazione alla geometria solida, ci si adatterà all\'errore del solido e, ad esempio si mantiene lo spessore di 5 mm, proprio nello stesso posto sbagliato, come è nel solido.

Prima di iniziare a lavorare sulla geometria di lavorazione, mi piace mettere un punto di riferimento nella struttura ad albero e dargli un nome simile a \"La_lavorazione_inizia_qui\". Questo è utile se si desidera passare dallo stato grezzo allo stato lavorato della parte perché si può vedere a colpo d\'occhio dove posizionarsi per essere nello stato grezzo.

Per lavorare il fondo del supporto, disegnare semplicemente un grande rettangolo nel piano XZ e con esso eseguire uno scavo. Per la parte superiore, disegnare un cerchio sul piano di riferimento che definisce la posizione della testa del bullone, con esso eseguire uno scavo e quindi rispecchiare lo scavo sul piano YZ. Nello stesso modo, creare uno scavo per il foro attraverso cui passerà il bullone e poi rifletterlo. Per la lavorazione all\'interno del supporto, creare uno schizzo sul piano YZ e con esso eseguire una scanalatura.
<img alt="La parte finita" src=images/HolderTop1-1.jpg  style="width:400px;"> Dopo aver concluso la lavorazione, si può ottenere un piacevole effetto visivo colorando tutte le superfici lavorate in modo che si possa vedere a colpo d\'occhio quali parti sono getto grezzo e quali sono lavorate dopo la fusione.

## Note finali 

Abbiamo modellato la parte superiore del supporto per cuscinetto con le dimensioni che avrà dopo la fusione. Per creare lo stampo di colata, è necessario applicare il ritiro alla propria parte, perché dopo la fusione, quando il metallo caldo si raffredda, esso si riduce di qualche punto percentuale (a seconda del materiale). Di solito è meglio lasciare l\'applicazione del ritiro alla fonderia che costruisce la parte perché essi hanno le conoscenze specifiche. Essi dovrebbero anche dirvi se la vostra parte ha aree problematiche, come ad esempio pareti molto spesse che improvvisamente si uniscono a sezioni molto sottili senza che tra di esse ci sia una sezione rastremata correttamente.

## Seconda parte del tutorial 

[PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II/it.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Bearingholder Tutorial I/it
