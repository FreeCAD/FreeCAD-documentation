# PartDesign Bearingholder Tutorial II/it





{{TutorialInfo
|Topic=Modeling
|Level=Experienced User
|Author=NormandC
|Time=
|FCVersion=0.19.23300 or higher
|Files=
}}


{{VeryImportantMessage|Questo tutorial è stato originariamente scritto per una versione di sviluppo di FreeCAD ora deprecata. A partire da aprile 2016 queste funzionalità sono state integrate nella release di pre-sviluppo 0.17 disponibile [https://github.com/FreeCAD/FreeCAD/releases/tag/0.17_pre qui].
<br />
Si noti che questa versione di FreeCAD è ancora in una fase iniziale di sviluppo. Inoltre questo tutorial potrebbe richiedere un aggiornamento. Se si desidera partecipare alla sua revisione e aggiornamento, si prega di annunciarlo nella sezione Wiki del [http://forum.freecadweb.org forum].}}

![Bearing Holder Tutorial - Supporto per cuscinetto finito (top)\|thumb\|right\|400px](images/HolderTop2-19.jpg )


<div class="mw-translate-fuzzy">

Come indicato nell\'avviso a inizio pagina, questo **tutorial non funziona se non si compila un particolare ramo altamente sperimentale del codice sorgente di FreeCAD** ed è un tutorial introduttivo alla modellazione con l\'ambiente di lavoro PartDesign in FreeCAD **utilizzando i piani di Riferimento che sono una caratteristica che nella maggior parte delle versioni FreeCAD non esiste ancora**. Lo scopo di questo tutorial è quello di presentare due differenti flussi di lavoro per creare un pezzo di fusione, con sformi e raccordi. Secondo quali altri programmi CAD si sono utilizzati, uno o l\'altro metodo potrebbe esservi più familiare. Come esempio di lavoro viene modellato un semplice supporto per cuscinetto.


</div>

## Purpose in Brief 

The purpose of the tutorial is to introduce you to two different work flows for creating a cast part with drafts and fillets. Depending on what other CAD programs you have been using, one or the other might be familiar to you. As a working example we will be modeling a simple bearing holder.

Questa è la seconda parte del tutorial. In questo esempio si usa il flusso di lavoro che può essere chiamato del \"corpo multiplo\" e si utilizza solamente la parte superiore del supporto.

Ovviamente, per seguire questo tutorial è necessario attivare l\'ambiente PartDesign.

~~Potete trovare la versione di Jrheinlaender (l\'autore di questo articolo) della parte creata con questo tutorial a [http://ubuntuone.com/39PTZ3Y3LUnmZzpZQPcJT4 questo link](http://ubuntuone.com/39PTZ3Y3LUnmZzpZQPcJT4_questo_link.md)~~ *Il file non è più disponibile, ne verrà fornito uno nuovo in un secondo momento*.

## Dati di progetto 

Il supporto deve essere in grado di contenere un cuscinetto di 90 mm di diametro con una larghezza fino a 33 mm (ad esempio, DIN 630 tipo 2308). Il cuscinetto richiede una spalla alta almeno 4,5 mm nel supporto (e sull\'albero). La parte superiore del supporto è imbullonata al fondo con due bulloni di 12 mm. A fianco del cuscinetto ci deve essere una scanalatura su entrambi i lati capace di contenere un anello di tenuta standard sull\'albero DIN 3760: 38x55x7 o 40x55x7 su un lato e 50x68x8 sull\'altro lato.

Il supporto sarà prodotto con un getto in sabbia con uno spessore minimo della parete di 5 mm, un angolo di sforno con di 2 gradi e un raggio di raccordo minimo di 3 mm .

## Impostazione della geometria di scheletro 

![Sketch della geometria scheletro\|thumb\|right\|400px](images/HolderTop2-2.png ) Creare una nuova parte nell\'ambiente PartDesign. Rinominare il corpo da come viene creato per impostazione predefinita in \"Skeleton\". Questo corpo probabilmente è già attivato, cosa che si può vedere dallo sfondo blu nell\'albero delle proprietà. Creare un nuovo schizzo sul piano YZ contenente il contorno dell\'albero, i cuscinetti e gli anelli di tenuta. Dopo aver terminato lo schizzo, eseguire con esso una operazione di rivoluzione. Questa funzione \"Scheletro\" sarà utilizzata successivamente come riferimento per la geometria reale. In questo modo se si desidera modificare le dimensioni, basta regolare le dimensioni della funzione scheletro e il resto della parte viene aggiornato di conseguenza. ![La geometria scheletro\|thumb\|right\|400px](images/HolderTop2-2-1.jpg )

## Il corpo principale 

![Schizzo della prima estrusione\|thumb\|right\|400px](images/HolderTop2-3.jpg ) Creare un nuovo corpo e renderlo attivo. Lo schizzo della prima estrusione è mostrato a destra. Esso è posto su un piano di riferimento, con un offset di 5 mm (lo spessore della parete) dalla faccia che nello scheletro definisce un fianco (esterno) di uno degli anelli di tenuta del cuscinetto. Poiché tutte le dimensioni importanti sono prese dallo scheletro, ci sono solo tre dimensioni: l\'entità della lavorazione (3 mm) alla base come offset per il piano XY, lo spessore della parete 5 mm dal diametro esterno dello scheletro, e i 2 gradi dell\'angolo di sformo. Per creare la dimensione 5 mm, è necessario prima selezionare il cerchio esterno (raggio 45 mm) della geometria scheletro come \"geometria esterna\" dello schizzo, e poi aggiungere una linea di costruzione tangente e vincolata a questo cerchio con un angolo di due gradi.

Probabilmente vi starete chiedendo perché c\'è questo piccolo segmento dritto in fondo a ciascun arco. Questo segmento assicura che sarà possibile creare uno sformo con un angolo di 2 gradi sugli archi. Questo potrebbe sembrare un lavoro eccessivo per ottenere un vantaggio minimo, ma molti programmi CAD (e forse un giorno anche FreeCAD) dispongono di strumenti che evidenziono un modello solido in diversi colori e mostrano subito tutte le facce dove l\'angolo di sformo non è corretto. Certamente non si vuole che al proprio modello accada questo, soprattutto dopo avervi aggiunto un sacco di raccordi!
![La prima estrusione (Pad)\|thumb\|right\|400px](images/HolderTop2-4.jpg ) Dopo aver finito il disegno (che è un po\' complicato a causa delle linee tangenziali per lo sformo di 2 gradi), creare con questo schizzo una estrusione (Pad) che si estenda fino all\'altro fianco della geometria dello scheletro, di nuovo con un offset dal fianco di 5 mm. Questa volta non è necessario creare un piano di riferimento, la modalità \"fino alla faccia\" della finestra di dialogo dell\'estrusione permette di inserire un offset.
![Sketch per l\'estrusione con cui si asporta del materiale\|thumb\|right\|400px](images/HolderTop2-5.jpg ) Successivamente, si asporta un po\' di materiale su entrambe le estremità del Pad, perché per i pezzi di fusione l\'ideale è avere sempre uno spessore il più uniforme possibile. Creare uno schizzo su ciascuno dei lati frontali del Pad e dimensionarlo con 5 mm di offset dal cerchio che rappresenta l\'anello di tenuta del cuscinetto (raggio 27,5 mm su un lato e 34 mm sull\'altro). Per il segmento della linea di fondo del disegno, creare un\'altra geometria esterna al Pad e vincolarla a questa. In questo modo lo schizzo ha una sola dimensione, 5 mm dello spessore della parete (le dimensioni 150 mm e 75 mm non sono importanti, basta che siano abbastanza grandi in modo da garantire che tutto quello che non serve venga asportato).
![Il Pad con gli scavi per ottenere uno spessore uniforme della parete\|thumb\|right\|400px](images/HolderTop2-6.jpg ) Utilizzare il disegno è stato creato per eseguire uno scavo ed estenderlo alla faccia della geometria dello scheletro che rappresenta il cuscinetto, meno 5 mm di offset per lo spessore della parete. Per il secondo scavo, è possibile utilizzare l\'opzione \"Duplica oggetto selezionato\" dal menu Modifica per duplicare il disegno già fatto (scegliere di non duplicare gli oggetti dipendenti se viene posta la domanda). Quindi, selezionare la faccia su cui si desidera spostare questo schizzo, e dire a FreeCAD di mappare lo schizzo su questa faccia (questa è una voce del menu PartDesign). Dopo aver creato il secondo scavo, è possibile osservare il risultato dal basso per verificare se si dispone di una parete di spessore di 5 mm intorno al contorno della geometria dello scheletro.
![Piano neutro per applicare lo sformo\|thumb\|right\|400px](images/HolderTop2-7.jpg ) Ora è il momento di creare gli sformi e i raccordi. L\'operazione di sformo richiede un piano neutro, questo significa che la geometria che è tagliata da questo piano rimarrà al suo posto, mentre il resto della faccia viene inclinato secondo l\'angolo di sformo. Usare il piano della base del Pad come piano neutro non è una buona idea poiché lo spessore della parete nella parte superiore del supporto diventerebbe meno di 5 mm. Quindi per questa operazione creiamo un piano di Riferimento con un offset di circa 35 mm da XY. Attivare il corpo Scheletro e creare lì il piano, perché ne avremo ancora bisogno per applicare degli sformi ad altri corpi.
![Primo corpo con sformi e raccordi\|thumb\|right\|400px](images/HolderTop2-8.jpg ) L\'immagine a destra mostra il primo corpo finito con gli sformi e i raccordi applicati. Notare che i bordi esterni (concavo) hanno un raggio di raccordo maggiore di 5 mm, sempre con lo scopo di creare uno spessore della parete il più uniforme possibile (più di 5 mm non è possibile perché altrimenti dopo la lavorazione interna del supporto lo spessore della parete diventa inferiore a 5 mm).

## Aggiungere i corpi per i bulloni 

![Sketch con il disegno della parte per i bulloni\|thumb\|right\|400px](images/HolderTop2-13.jpg ) I bulloni hanno bisogno di due corpi cilindrici su entrambi i lati del corpo principale. E\' meglio inserire lo sformo di 2 gradi nel disegno. Ho provato a creare un cilindro con una rotazione e applicarvi successivamente uno sformo, ma dopo il mirroring sono successe delle strane cose e non ho potuto applicarvi i raccordi, perché la superficie era in qualche modo deformata.

Lo schizzo è dimensionato in modo che l\'asse di rotazione sia distante 12 mm dal diametro esterno del corpo scheletro, 7 mm per il raggio del foro più 5 mm per lo spessore della parete. Per il gusto di avere una parte completamente parametrica è una buona idea aggiungere un piano allo scheletro a circa 25 mm sopra il piano XY per contrassegnare la faccia superiore dei cilindri. Dato che questa faccia verrà lavorata, lo schizzo è dimensionato 3 mm al di sopra di essa.

![I corpi per i bulloni\|thumb\|right\|400px](images/HolderTop2-14.jpg ) Creare una rivoluzione dallo schizzo e applicare un raccordo di 4 mm al bordo superiore. In questo modo, dopo la lavorazione in cui si asportano 3 mm, rimane ancora un lieve raccordo che permette di evitare che il bordo sia tagliente e che qualcuno possa ferirsi durante il serraggio dei bulloni.
![Il corpo principale con i due corpi per i bulloni\|thumb\|right\|400px](images/HolderTop2-16.jpg ) Creare una funzione booleana per fondere il corpo principale con il corpo per il bullone. Quindi creare un nuovo corpo per l\'altro lato. Duplicare lo schizzo della rivoluzione, spostarlo in questo corpo e creare il secondo corpo per i bulloni (il mirroring di un corpo non è ancora supportato, quindi è necessario rifarlo per la maggior parte). Poi fondere anche questo secondo corpo nel corpo principale. Infine applicare un grande raccordo sul bordo creato con l\'operazione di fusione booleana, il bordo tra il corpo principale e il corpo per i bulloni. Il più grande che ho potuto ottenere è di 4 mm.

## Scavare il corpo principale 

![Il primo Pad del corpo dello scavo all\'interno del corpo principale\|thumb\|right\|300px](images/HolderTop2-9.jpg ) Passare ora a lavorare sulla parte interna del supporto e scavare per creare lo spazio per il cuscinetto e per gli anelli di tenuta. Nel fare questo, naturalmente, bisogna tenere a mente il sovrametallo di 3 mm. Dal momento che questo tutorial insegna il metodo \"multi-corpo\", prima si crea la geometria interna come un corpo separato e poi la si aporta dal corpo principale con una operazione booleana.

Creare un nuovo corpo e renderlo attivo. In primo luogo, serve un piano di riferimento con un offset di 3 mm all\'interno della faccia scheletro che rappresenta il lato del cuscinetto. Poi, duplicare il disegno del primo pad del corpo principale. Sarà aggiunto al corpo principale, quindi fare clic destro su di esso e scegliere di spostarlo sul corpo appena creato (se è attivo l\'ambiente PartDesign, questa opzione è disponibile solo nel menu di contesto). Mappare il disegno su piano di riferimento (se dopo la mappatura lo schizzo risulta capovolto, spostare il piano di riferimento sull\'altro lato del cuscinetto, accanto a cui si trova lo schizzo duplicato). Ora, modificare il disegno in modo che il diametro sia di 3 mm inferiore al diametro esterno della geometria scheletro che rappresenta il cuscinetto. Basta rimuovere la dimensione di 5 mm, trascinare il disegno all\'interno del cerchio di riferimento, e poi creare una nuova dimensione di 3 mm.
![Il corpo dello scavo interno al corpo scheletro\|thumb\|right\|400px](images/HolderTop2-10.jpg ) Ora servono altri due Pad per scavare lo spazio per gli anelli di tenuta. Duplicare il disegno del primo pad del \"Corpo per lo scavo\" e mapparlo al piano XZ. Modificare lo schizzo e sostituire il riferimento esterno con il diametro esterno dell\'anello di tenuta del cuscinetto. Estrudere questo schizzo con un offset di 3 mm dal fianco dell\'anello di tenuta. Ripetere l\'intero processo per l\'anello di tenuta del lato opposto.

Dopo di questo creare altri due rilievi all\'interno del supporto, come gli ultimi due per dare un gioco all\'albero (ad esempio 3 mm).
![Il corpo completo della parte da asportare (meno i raccordi impossibili)\|thumb\|right\|400px](images/HolderTop2-11.jpg ) Ora non rimane che applicare lo sformo alle facce piane laterali, utilizzando lo stesso piano neutro come si è fatto per il corpo principale, e i raccordi. Applicare un raccordo generale di 3 mm a tutti i bordi. Noterete che ci sono diversi spigoli che non possono essere raccordati \... questo è un difetto del kernel geometrico sottostante usato da FreeCAD.
![La parte grezza completata del supporto (senza le lavorazioni)\|thumb\|right\|400px](images/HolderTop2-15.jpg ) Siamo pronti per \"svuotare\" il corpo principale. Selezionarlo e scegliere di creare una nuova operazione booleana. Aggiungere il corpo della parte da asportare alla lista della finestra e impostare l\'operazione \"Differenza\". Mettere un raccordo di 3 mm sui due bordi derivanti dalla operazione di asportazione (rimangono di nuovo alcuni bordi che \"non sono raccordabili\"). Il risultato dovrebbe essere simile alla figura sulla destra.

Ora la parte grezza è completata. Questo è ciò a cui il supporto somiglierà prima della lavorazione. Si noti che, poiché lo stampo avrà una metà superiore e metà una inferiore, il bordo tra queste due parti può non essere raccordato. Inoltre, se si cede questo modello a una fonderia ricordarsi di sottolineare che esso ha le dimensioni che deve avere dopo il getto. La fonderia dovrà poi applicare una certa percentuale di restringimento al modello (rendendo il modello digitale utilizzato per fabbricare lo stampo più grande in modo che dopo la fusione, quando il metallo si raffredda e si contrae, abbia il giusto formato).

## Lavorazione

![Sketch per praticare il foro per le viti\|thumb\|right\|400px](images/HolderTop2-17.jpg ) Per togliere il materiale della lavorazione dall\'interno del supporto, si può usare molto convenientemente il Corpo Scheletro stesso. Se non si vuole fare questo perché dopo lo scheletro viene nascosto da qualche parte nell\'albero della struttura, è anche possibile duplicare lo schizzo della funzione di rivoluzione dello scheletro e ricreare la rivoluzione in un nuovo corpo. Questo, però, non è completamente parametrico, perché il disegno duplicato è indipendente da quello originale, in questo modo se si cambia una dimensione si deve poi lavorare su entrambi i disegni. Le funzioni duplicate dipendenti saranno supportate in futuro.

Per il resto della lavorazione, creare un nuovo corpo. La parte inferiore del supporto viene lavorato da un pad disegnato sul piano xy e esteso verso il basso. Successivamente, disegnare una rivoluzione per fare un foro per i bulloni. E\' necessario fare il disegno sul piano XZ e ruotarlo in modo da poter utilizzare il diametro esterno del corpo scheletro come riferimento esterno. La parte superiore del disegno servirà a lavorare una superficie piana per la testa del bullone. Esso è dimensionato per lasciare almeno 5 mm di spessore nella parete del supporto. Se questo non lascia abbastanza spazio per la testa del bullone allora si può spostare verso l\'alto il piano di Riferimento. Naturalmente, si potrebbe mettere questa logica nello scheletro, ma questo viene lasciato come esercizio per il lettore!
![Il corpo della lavorazione\|thumb\|right\|400px](images/HolderTop2-18.jpg ) È possibile eseguire il mirroring della rivoluzione sugli assi YZ. L\'immagine a destra mostra il \"Corpo lavorazione\". Naturalmente, la maggior parte delle dimensioni dei Pad e delle Rivoluzioni non sono importanti finché vi è abbondanza di sovrapposizione.
![Il supporto finito con le lavorazioni\|thumb\|right\|400px](images/HolderTop2-19.jpg ) Infine, creare una operazione booleana per asportare il Corpo lavorazione dal Corpo principale. Se si desidera un piacevole effetto visivo, è possibile colorare le superfici lavorate in modo diverso dal resto del pezzo. Questo costituisce anche un utile controllo visivo per individuare eventuali lavorazioni dimenticate.

## Parte Uno 

[PartDesign Bearingholder Tutorial I](PartDesign_Bearingholder_Tutorial_I/it.md)



[Category:Tutorials](Category:Tutorials.md)
