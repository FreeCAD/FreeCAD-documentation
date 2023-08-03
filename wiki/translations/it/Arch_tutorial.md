---
 TutorialInfo:t
   Topic: Modellazione
   Level: Intermedio
   Time: 
   Author: User:Yorik
   FCVersion: 0.14
   Files: 
---

# Arch tutorial/it




<div class="mw-translate-fuzzy">




</div>

![](images/Arch_tutorial_00.jpg )



## Introduzione


<div class="mw-translate-fuzzy">

Questo tutorial è una guida pratica che mira a fornire le basi per lavorare con l\'ambiente [Architettura](Arch_Workbench/it.md). Cercherò di renderla abbastanza semplice, in modo che non serva alcuna precedente esperienza con FreeCAD, ma è comunque utile avere almeno una discreta esperienza con il 3D o con le applicazioni [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling). In ogni caso, si deve essere disposti a cercare in proprio, nel [wiki della documentazione di FreeCAD](Main_Page.md), ulteriori informazioni su come funziona FreeCAD. Chi non ha mai provato FreeCAD deve prima leggere la pagina [Per iniziare](Getting_started/it.md). È utile consultare anche la nostra sezione dedicata ai [tutorial](tutorials/it.md) e ricordare che su [youtube](http://www.youtube.com/results?search_query=freecad) si trovano molte altre guide sull\'uso di FreeCAD.


</div>


<div class="mw-translate-fuzzy">

L\'ambiente [Arch](Arch_Workbench/it.md) ha lo scopo di offrire un flusso completo di lavoro [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) all\'interno di FreeCAD. Poiché è ancora in fase di sviluppo, non aspettatevi di trovare gli stessi strumenti e il grado di perfezionamento delle evolute alternative commerciali come [Revit](http://en.wikipedia.org/wiki/Revit) o [ArchiCAD](http://en.wikipedia.org/wiki/Archicad), ma d\'altra parte FreeCAD è fatto per essere utilizzato in un ambito molto più vasto di quanto lo siano queste applicazioni e l\'ambiente [Arch](Arch_Workbench/it.md) trae grossi benefici dalle altre discipline a cui FreeCAD si rivolge, inoltre offre alcune caratteristiche viste raramente nelle applicazioni BIM tradizionali.


</div>


<div class="mw-translate-fuzzy">

Ecco, come esempio, alcuni caratteristiche interessanti dell\'ambiente Arch di FreeCAD che è difficile trovare in altre applicazioni BIM:


</div>

-   Gli oggetti architettonici sono sempre dei solidi. Dal forte retroterra meccanico di FreeCAD abbiamo appreso l\'importanza di lavorare sempre con degli oggetti solidi. Questo assicura un flusso di lavoro con meno possibilità di errori, e le operazioni booleane sono molto affidabili. Dato che tagliare degli oggetti 3D con un piano 2D, per estrarre le sezioni, è anche un\'operazione booleana, è possibile intuire immediatamente l\'importanza di questo punto.

-   Gli oggetti architettonici possono sempre avere qualsiasi forma. Non c\'è nessuna restrizione. I muri non devono necessariamente essere verticali, le solette non hanno bisogno di apparire come solette. Qualsiasi oggetto solido può sempre diventare un oggetto architettonico. Cose molto complesse, di solito difficili da definire in altre applicazioni BIM, come una soletta curva che cresce diventando un muro (sì, è proprio di Zaha Hadid che stiamo parlando), in FreeCAD non presentano nessun problema particolare.


<div class="mw-translate-fuzzy">

-   Tutta la potenza di FreeCAD è a portata di mano. È possibile progettare gli oggetti architettonici con qualsiasi altro strumento di FreeCAD, ad esempio con quelli di [PartDesign](PartDesign_Workbench/it.md), e poi, quando sono pronti, convertirli in oggetti architettonici. Essi conservano sempre l\'intero storico della loro modellazione, e continuano ad essere completamente modificabili. L\'ambiente [Arch](Arch_Workbench/it.md) eredita anche gran parte delle funzionalità dell\'ambiente [Draft](Draft_Workbench/it.md), quali lo [snap](Draft_Snap/it.md) e i [piani di lavoro](Draft_SelectPlane/it.md).


</div>


<div class="mw-translate-fuzzy">

-   L\'ambiente [Arch](Arch_Workbench/it.md) è molto [mesh](Mesh_Workbench/it.md)-friendly. Si può facilmente progettare un modello architettonico con un\'applicazione basata su mesh, ad esempio [Blender](http://en.wikipedia.org/wiki/Blender_%28software%29) o [SketchUp](http://en.wikipedia.org/wiki/Sketchup), e poi importarlo in FreeCAD. Se la qualità del modello è stata curata e i suoi oggetti sono forme solide manifold, per trasformarlo in oggetto architettonico basta premere un tasto.


</div>


<div class="mw-translate-fuzzy">

In questo momento, però, l\'ambiente Arch, come il resto di FreeCAD, soffre di alcune limitazioni. Sulla maggior parte si sta lavorando e in futuro spariranno.


</div>


<div class="mw-translate-fuzzy">

-   FreeCAD non è una applicazione 2D. È pensato e sviluppato per il 3D. Mette a disposizione un discreto insieme di strumenti per il disegno e la modifica di oggetti 2D negli ambienti [Draft](Draft_Workbench/it.md) e [Sketcher](Sketcher_Workbench/it.md), ma non è fatto per gestire grandi (e talvolta mal disegnati) file di CAD 2D. Di solito è possibile importare correttamente i file 2D, ma se intendete continuare a lavorare su di loro in 2D non aspettatevi prestazioni elevate. Siete avvertiti.


</div>


<div class="mw-translate-fuzzy">

-   Per ora non c\'è ancora nessun supporto per i materiali. FreeCAD avrà presto un sistema completo di [Materiali](Material.md) in grado di definire dei materiali molto complessi, con tutte le preziosità che si possono desiderare (le proprietà personalizzate, le famiglie dei materiali, il rendering e le proprietà di aspetto, ecc) e ovviamente appena sarà pronto l\'ambiente Arch lo utilizzerà.


</div>

-   Supporto preliminare di [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes). È già possibile [importare i file IFC](Arch_IFC/it.md) in modo abbastanza affidabile, a condizione che [IfcOpenShell](http://ifcopenshell.org) sia installato sul sistema, ma l\'esportazione non è ancora supportata ufficialmente. Su questo stanno lavorando sia gli sviluppatori di FreeCAD che di IfcOpenShell, e ci si può aspettare che in futuro il supporto di IFC sarà completo.

-   La maggior parte degli strumenti di Arch sono ancora in sviluppo. Ciò significa che gli strumenti automatici \"wizard\", cioè quelli che creano automaticamente delle geometrie complesse, quali [Tetto](Arch_Roof/it.md) o [Scala](Arch_Stairs/it.md), possono produrre solo alcuni tipi di oggetti, e che altri strumenti che hanno delle impostazioni predefinite, quali [Struttura](Arch_Structure/it.md) o [Finestra](Arch_Window/it.md), per ora hanno solo poche preimpostazioni di base. Ovviamente cresceranno nel tempo.

-   In FreeCAD è già stato implementato il [Sistema di Unità](Units/it.md) di misura che permette di lavorare con qualsiasi unità desiderata (anche con le unità di misura imperiali, e chi proviene dagli Stati Uniti può essere eternamente grato di questo a Jürgen, il padrino e \"dittatore\" di FreeCAD). Al momento, però l\'attuazione non è completa, e l\'ambiente Arch non lo supporta ancora. Per ora Arch deve essere considerato \"unit-less\", cioè adimensionale.


<div class="mw-translate-fuzzy">


{{Note|È richiesta la versione 0.14 di FreeCAD|Questo tutorial è stato scritto utilizzando la [versione 0.14 di FreeCAD](Release_notes_0.14/it.md). Per seguirlo è necessario avere almeno questa versione. Con le precedenti versioni possono mancare degli strumenti necessari o delle opzioni che sono presentate qui.}}


</div>



## Flussi di lavoro tipici 


<div class="mw-translate-fuzzy">

L\'ambiente [Arch](Arch_Workbench/it.md) è fatto principalmente per due tipi di flussi di lavoro:


</div>

-   Costruire il modello con una applicazione più veloce, basata su mesh come [Blender](http://en.wikipedia.org/wiki/Blender_%28software%29) o [SketchUp](http://en.wikipedia.org/wiki/Sketchup), e importarlo in FreeCAD per estrarre i piani e le viste delle sezioni. FreeCAD è stato pensato per la modellazione di precisione ad un livello molto più elevato di quello che serve di solito per la modellazione architettonica, quindi costruire i modelli direttamente in FreeCAD può essere faticoso e lento. Per tale motivo, questo flusso di lavoro presenta dei grandi vantaggi. Nel mio blog ho descritto il procedimento in [questo articolo](http://yorik.uncreated.net/guestblog.php?2012=180). Se il modello è curato, corretto e preciso (pulito, solidi, mesh non-manifold), questo flusso di lavoro dà le stesse prestazioni e lo stesso livello di precisione dell\'altro.


<div class="mw-translate-fuzzy">

-   Costruire il modello direttamente in FreeCAD. Questo è il procedimento che voglio mostrare in questo tutorial. Useremo principalmente tre ambienti di lavoro: naturalmente [Arch](Arch_Workbench/it.md), ma anche [Draft](Draft_Workbench/it.md), i cui strumenti sono tutti inclusi in Arch e quindi non c\'è bisogno di cambiare ambiente, e [Sketcher](Sketcher_Workbench/it.md). Per comodità, come faccio di solito, si può creare una barra degli strumenti personalizzata per il proprio ambiente Arch, con Strumenti → Personalizza, e aggiungervi gli strumenti di Sketcher che si usano spesso. Questo è il mio ambiente Arch modificato \"su misura\":


</div>

![](images/Arch_tutorial_01.jpg )

In questo tutorial modelleremo la casa in 3D sulla base di disegni 2D scaricati dalla rete e poi estrarremo dal modello i documenti 2D, quali piante, prospetti e sezioni.



## Preparazione

Per modellare, invece di creare un progetto da zero, usiamo un progetto di esempio che ci farà risparmiare tempo. Ho scelto questa splendida casa del famoso architetto [Vilanova Artigas](http://en.wikipedia.org/wiki/Jo%C3%A3o_Batista_Vilanova_Artigas) (vedere una serie di [immagini](http://www.leonardofinotti.com/projects/architects-second-house/image/40409-130405-010d) di Leonardo Finotti) perché è vicina a dove vivo io, è semplice, è un meraviglioso esempio di splendida architettura moderna di São Paulo, e i disegni dwg sono [facilmente disponibili](http://www.bibliocad.com/library/second-house-vilanova-artigas_72926#).

Useremo i disegni 2D DWG ottenuti dal link indicato sopra come base per costruire il nostro modello (per scaricarli è necessario registrarsi, ma è gratis, oppure prelevare direttamente il dxf da [quì](http://yorik.uncreated.net/scripts/artigas.dxf)). Quindi la prima cosa da fare è prelevare il file DWG, scompattarlo e aprirlo all\'interno di un\'applicazione dwg quale [DraftSight](http://www.3ds.com/products-services/draftsight/overview/). In alternativa, è possibile convertirlo in DXF con una utility free come [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter). Se avete ODA converter installato (e il suo percorso è definito nelle impostazioni delle preferenze di Arch), FreeCAD è in grado di [importare direttamente i file DWG](Draft_DXF/it.md). Siccome questi file possono essere di cattiva qualità e molto pesanti, di solito è meglio aprirli prima con un\'applicazione CAD 2D e fare un po\' di pulizia.

In questo caso, ho rimosso tutti i disegni dei dettagli, tutti i cartigli e i layout di pagina, ho fatto \"pulizia\" (\"purga\" in gergo AutoCAD) di tutte le entità non utilizzate, riorganizzato le sezioni alla posizione logica rispetto alla vista in pianta, e spostato tutto al punto 0,0. Dopo queste operazioni il file può essere aperto pienamente efficiente in FreeCAD. Controllare le diverse opzioni disponibili in Modifica → Preferenze → Draft → Import/Export che possono influenzare il modo e la velocità di importazione dei file DXF/DWG.

Ecco come appare il file dopo essere stato aperto in FreeCAD. Con lo strumento [Scala](Draft_Scale/it.md) ho cambiato anche lo spessore delle pareti (i contenuti del gruppo \"muros\"), e girato un paio di porte che erano state importate con scala X sbagliata:

![](images/Arch_tutorial_02.jpg )

L\'[importatore DXF](Draft_DXF/it.md) (che si occupa anche dei file DWG, siccome quando si importano i file DWG, essi sono semplicemente convertiti prima in DXF ), raggruppa gli oggetti importati dai layer. In FreeCAD non ci sono i layer, ma ci sono i [gruppi](Std_Group/it.md). I gruppi offrono un modo simile per organizzare gli oggetti dei file, ma non hanno delle proprietà specifiche che applicano al loro contenuto, come fanno i layer di AutoCAD. I gruppi possono essere annidati all\'interno di altri gruppi, il che è molto comodo. La prima cosa che potremmo voler fare qui, è quella di creare un nuovo [gruppo](Std_Group/it.md) nella [vista albero](Document_structure/it.md), allora fare clic destro sull\'icona del documento, aggiungere un gruppo, fare clic destro su di esso, rinominarlo \"base 2D plans\" e poi trascinarvi dentro tutti gli altri oggetti.



## Costruire i muri 


<div class="mw-translate-fuzzy">

Come la maggior parte degli oggetti [Arch](Arch_Workbench/it.md), i [muri](Arch_Wall/it.md) possono essere costruiti su una grande varietà di altri oggetti: [linee](Draft_Line/it.md), [contorni](Draft_Wire/it.md) (polilinee), [schizzi](Sketcher_Workbench/it.md), facce o solidi (o anche su nulla, nel qual caso essi sono definiti da altezza, larghezza e lunghezza). La geometria della parete risultante dipende dalla geometria di base, e dalle proprietà definite, quali la larghezza e l\'altezza. Come si può immaginare, un muro basato su una linea usa questa linea come sua linea di allineamento, mentre un muro basato su una faccia usa tale faccia come sua impronta di base, e un muro basato su un solido adotta semplicemente la forma di tale solido. Questo permette a qualsiasi forma immaginabile di diventare un muro.


</div>


<div class="mw-translate-fuzzy">

In FreeCAD sono possibili diverse strategie per costruire un muro. Si potrebbe pensare di costruire un intero \"piano\" con [sketcher](Sketcher_Workbench/it.md), e poi costruire su di esso un solo, grande, oggetto muro. Questa tecnica funziona, ma a tutte le pareti del progetto sarebbe assegnato lo stesso spessore. In alternativa, è possibile costruire tutte le porzioni di muro basate su segmenti distinti. Oppure, come faremo qui, con un mix di entrambi. Costruiamo pertanto alcune [polilinee](Draft_Wire/it.md) sopra il piano importato, una per ogni tipo di muro:


</div>

![](images/Arch_tutorial_03.jpg )

Come potete vedere, ho disegnato in rosso le linee che diventeranno muri di cemento (una [ricerca di immagini](http://www.google.com/search?tbm=isch&q=casa+artigas+brooklin) della casa può aiutare a distinguere i diversi tipi di muro), mentre quelli verdi sono i muri di mattoni esterni e quelli blu diventeranno le pareti interne. Ho fatto passare le linee attraverso le porte, perché le porte saranno inserite nei muri più avanti e creeranno automaticamente le loro aperture. I muri possono essere allineati a sinistra, a destra o centralmente sulla loro base, quindi non importa da che parte si disegna la linea di base. Ho anche cercato di evitare le intersezioni per quanto ho potuto, perché in questo modo il nostro modello sarà più pulito. Delle intersezioni ci occuperemo più avanti.

Quando avete finito, se lo desiderate, potete mettete tutte le linee in un nuovo [gruppo](Std_Group/it.md), poi selezionatele tutte, una per una, e premete lo strumento [Muro](Arch_Wall/it.md) per costruire un muro da ciascuna linea. È anche possibile selezionare contemporaneamente più linee. Dopo aver fatto questo, e aver corretto gli spessori (i muri esterni sono di 25 centimetri e quelli interni sono di 15 centimetri) e alcuni allineamenti, i muri sono pronti:

![](images/Arch_tutorial_04.jpg )

Avremmo anche potuto costruire i muri partendo da zero. Se si preme il pulsante [Muro](Arch_Wall/it.md) con nessun oggetto selezionato, si possono scegliere due punti sullo schermo per disegnare un muro. Ma in realtà, lo strumento muro disegna comunque una linea e poi vi costruisce sopra un muro. Ho ritenuto il procedimento proposto più didattico per spiegare come funzionano le cose.

Avete notato che ho avuto grande cura di non incrociare i muri? Questo ci permetterà di evitare dei mal di testa in seguito, per esempio se esportiamo il nostro lavoro in altre applicazioni che potrebbero non gradire le intersezioni. Ho una sola intersezione, dove ero troppo pigro e invece di disegnare due piccoli segmenti ho disegnato una lunga polilinea che ne interseca un\'altra. Questo deve essere corretto. Fortunatamente, tutti gli oggetti Arch hanno una grande caratteristica: è ​​possibile aggiungerli uno all\'altro. Facendo questo si uniscono le loro geometrie, ma rimangono ancora modificabili in modo indipendente. Per aggiungere uno dei muri che si incrociano all\'altro muro, basta selezionare uno, CTRL + selezionare l\'altro, e premere lo strumento [Aggiungi](Arch_Add/it.md):

![](images/Arch_tutorial_05.jpg )

Sulla sinistra ci sono i due muri che si intersecano, sulla destra il risultato dopo aver aggiunto un muro all\'altro.


<div class="mw-translate-fuzzy">


{{Note|Una nota importante sugli oggetti parametrici|È già ora di fare delle considerazioni importanti. Come potete vedere, in FreeCAD, tutto è parametrico: Il nuovo muro "unito" è costituito da due muri, ciascuno basato su una linea. Quando lo si espande nella [vista ad albero](Document_structure/it.md), si può vedere tutta questa catena di dipendenze. Come potete immaginare, questo piccolo gioco può diventare rapidamente molto complesso. Inoltre, sapendo già come lavorare con [sketcher](Sketcher_Workbench/it.md), si potrebbe pensare di disegnare le linee di base con schizzi vincolati. Tutta questa complessità ha però un costo: si eleva in modo esponenziale il numero di calcoli che FreeCAD deve compiere per mantenere aggiornata tutta la geometria del modello. Quindi, pensateci, non aggiungete delle inutili complessità quando non servono. Mantenere un buon equilibrio tra oggetti semplici e complessi, e riservare questi ultimi per i casi in cui servono veramente.}}


</div>

Ad esempio, avrei potuto disegnare tutte le linee di base di cui sopra, senza preoccuparmi di cosa attraversavano e poi sistemarle con lo strumento [Aggiungi](Arch_Add/it.md). Ma avrei elevato molto la complessità del modello, senza nessun vantaggio. Meglio farle corrette fin dall\'inizio, e mantenerle come parti geometriche molto semplici.

Ora che i muri sono sistemati, dobbiamo incrementare la loro altezza fino a quando intersecano il tetto. Poi, dato che l\'oggetto muro ancora non può essere troncato automaticamente dalla copertura (questo però accadrà in futuro), costruiremo un oggetto \"fittizio\", che segue la forma del tetto, da sottrarre dai muri.

Guardando nei disegni 2D si può vedere che il punto più alto del tetto si trova a 5,6 m dal suolo. Quindi diamo a tutti i muri un\'altezza di 6 m, in modo da essere sicuri che saranno tagliati dal volume tetto \"fittizio\". Si può chiedere: perché 6 m e non 5.6 m? Beh, se avete già lavorato con le operazioni booleane (addizioni, sottrazioni, intersezioni), dovreste già sapere che queste operazioni di solito non gradiscono molto le situazioni \"faccia-contro-faccia\", ma preferiscono decisamente gli oggetti intersecati. Perciò, facendo in questo modo, continuiamo sul sicuro.

Per aumentare l\'altezza dei muri, basta selezionarli tutti nella vista ad albero, senza dimenticare quello che abbiamo aggiunto all\'altro, e modificare il valore della loro proprietà \"height\".

Prima di creare il tetto e di tagliare le pareti, costruiamo i rimanenti oggetti che dovranno essere tagliati: le pareti dello studio superiore, e le colonne. Le pareti dello studio si creano nello stesso modo di prima, sul piano superiore e sono alte 2,6 m. Poi assegniamo loro l\'altezza necessaria, non più 6m che è troppo, ma 3,4 m . Fatto questo, spostiamo in alto le pareti di 2,6 m: Selezionarle entrambe, mettersi in vista frontale (Visualizza → Viste Standard → Front), premere il pulsante [Sposta](Draft_Move/it.md) , selezionare il primo punto, poi immettere 0, 2.6, 0 come coordinate, e premere Invio. Ora gli oggetti sono spostati in alto di 2.6m:

![](images/Arch_tutorial_06.jpg )


<div class="mw-translate-fuzzy">


{{Note|A proposito di coordinate|Gli oggetti [Draft](Draft_Workbench/it.md), e anche molti oggetti  [Arch](Arch_Workbench/it.md), obbediscono ad un sistema Draft chiamato [piano di lavoro](Draft_SelectPlane/it.md). Questo sistema definisce il piano 2D dove avverranno le operazioni successive. Se non si specifica nessun piano, il piano di lavoro si adatta da solo alla visualizzazione corrente. Questo è il motivo per cui siamo passati alla vista frontale e poi abbiamo applicato uno spostamento di 0 in X e di 2.6 in Y . Con lo strumento piano di lavoro, potevamo anche costringere il piano di lavoro a rimanere al piano terra. Dopo, avremmo dovuto applicare uno spostamento di 0 in X, 0 in Y e 2.6 in Z.}}


</div>

Ora spostiamo i muri in orizzontale, nella loro posizione corretta. Dato che abbiamo dei punti di snap, questo è più facile: Selezionare entrambi i muri, premere lo strumento [Sposta](Draft_Move/it.md), e spostarli da un punto all\'altro:

![](images/Arch_tutorial_07.jpg )

Infine, ho cambiato il colore di alcuni muri in un colore simil-mattone (così è più facile differenziarli), e fatto una piccola correzione. Siccome alcuni muri non vanno fino al tetto, ma si fermano ad una altezza di 2.60m, ho corretto la loro altezza.



## Elevare la struttura 

Dato che dovremo tagliare i muri con un volume di sottrazione, vediamo se non ci sono altri oggetti che dovranno essere tagliati in quel modo. Ci sono, sono alcune delle colonne. Questa è una buona occasione per introdurre un secondo oggetto arch: la [Struttura](Arch_Structure/it.md). Gli oggetti Struttura si comportano più o meno come le pareti, ma non sono fatti per seguire una linea di base. Preferiscono lavorare su un profilo che viene estruso (lungo un contorno o anche no). Qualsiasi oggetto piatto può essere usato come profilo di una struttura, con un solo requisito: deve costituire una forma chiusa.

Per le colonne, useremo una strategia diversa da quella dei muri. Invece di \"disegnare\" sopra alle piante 2D, useremo direttamente i loro oggetti, cioè i cerchi che rappresentano le colonne nella vista in pianta. In teoria, potremmo semplicemente selezionarne uno e premere il tasto [Struttura](Arch_Structure/it.md). Però, se facciamo questo, produciamo un oggetto strutturale \"vuoto\". Questo succede perché non si può mai essere troppo sicuri di quanto gli oggetti siano stati disegnati bene nel file DWG, e spesso non sono forme chiuse. Quindi, prima di trasformarli in colonne reali, cerchiamo di trasformarli in facce, usando su di loro due volte lo strumento [Upgrade](Draft_Upgrade/it.md). La prima volta per convertirli in contorni chiusi (polilinee), la seconda volta per convertire i contorni in facce. Questo secondo passaggio non è obbligatorio, ma, se avete una faccia, siete sicuri al 100% che è chiusa, altrimenti la faccia non può essere creata.

Dopo aver convertito tutte le colonne in facce, possiamo utilizzare lo strumento [Struttura](Arch_Structure/it.md) sulle facce, e regolarne l\'altezza (alcune sono alte 6m, altre solo 2.25m ):

![](images/Arch_tutorial_08.jpg )

Nella immagine sopra, potete vedere due colonne che sono ancora come erano nel file DWG, due che sono state aggiornate a facce, e due che sono state trasformate in oggetti strutturali con altezza di 6m e 2.25m.

Notare che questi diversi oggetti Arch (muri, strutture, e tutti gli altri che scopriremo) condividono tutti un sacco di cose (per esempio tutti possono essere aggiunti uno all\'altro, come abbiamo già visto per i muri, e qualunque di loro può essere convertito in un altro). Quindi spesso è solo questione di gusti, potevamo anche costruire le colonne con lo strumento muro, e poi convertirle, se necessario. In effetti, alcuni dei nostri muri sono muri di cemento, e più avanti li convertiremo in strutture.



## Sottrazioni

Ora è tempo di costruire il volume di sottrazione. Il modo più semplice è quello di disegnare il suo profilo sopra la vista della sezione. Dopo, lo faremo ruotare e lo collocheremo nella sua posizione corretta. Ora capite perché ho ​​disposto le sezioni e i prospetti in questo modo prima di iniziare? Sarà molto utile per disegnare le cose lì e poi spostarle nella posizione corretta sul modello.

Ora disegniamo un volume più grande del tetto, che verrà sottratto dai muri. Per fare questo, ho disegnato due linee sulla parte superiore della base del tetto, poi le ho estese un po\' con lo strumento [Estendi](Draft_Trimex/it.md). Dopo, ho disegnato un [contorno](Draft_Wire/it.md), agganciato a queste linee, che và ben al di sopra dei 6 metri. Ho anche disegnato una linea blu al piano terra (0.00), che sarà l\'asse di rotazione.

<img alt="" src=images/Arch_tutorial_09.jpg  style="width:1024px;">

Ora viene la parte difficile. Useremo lo strumento [Ruota](Draft_Rotate/it.md) per ruotare il profilo di 90 gradi verso l\'alto, nella giusta posizione per essere estruso. Per fare questo, dobbiamo prima cambiare il [piano di lavoro](Draft_SelectPlane/it.md) con il piano YZ. Quando questo è fatto, la rotazione avverrà in detto piano. Ma se faremo come abbiamo fatto prima, e imposteremo la vista laterale, sarà difficile vedere e selezionare il profilo, e sapere dove si trova il punto base intorno a cui deve ruotare, giusto? Allora dobbiamo impostare manualmente il piano di lavoro: Premere il pulsante [Seleziona piano](Draft_SelectPlane/it.md) (è nella scheda \"Azioni\" della vista ad albero), e impostarlo su YZ (che è il piano \"laterale\"). Una volta impostato manualmente il piano di lavoro, come stiamo facendo, esso non cambierà secondo il punto di vista. Ora è possibile ruotare l\'immagine fino ad avere una buona visione di tutte le cose da selezionare. In seguito, per commutare il piano di lavoro nella modalità \"automatica\", premere di nuovo il tasto [Seleziona piano](Draft_SelectPlane/it.md) e impostarlo su \"Nessuno\".

Ora la rotazione sarà facile da fare: Selezionare il profilo, premere il pulsante [Ruota](Draft_Rotate/it.md), fare clic su un punto della linea blu, inserire 0 come angolo iniziale, e 90 come rotazione:

<img alt="" src=images/Arch_tutorial_10.jpg  style="width:1024px;">

Ora tutto quello che dobbiamo fare è spostare il profilo un po\' più vicino al modello (impostare il piano di lavoro XY se necessario), ed estruderlo. Questo può essere fatto con lo strumento [Estrudi](Part_Extrude/it.md), ma pure con [Estendi](Draft_Trimex/it.md) che ha anche lo speciale potere nascosto di estrudere le facce. Accertatevi che l\'estrusione sia più grande di tutti i muri da cui sarà sottratta, per evitare delle situazioni di faccia-contro-faccia:

<img alt="" src=images/Arch_tutorial_11.jpg  style="width:1024px;">

Ora, entra in azione il contrario dello strumento [Aggiungi](Arch_Add/it.md), che è [Rimuovi](Arch_Remove/it.md). Come si può immaginare, rende anche un oggetto figlio di un altro, ma invece di unire due oggetti, la sua forma è sottratta all\'oggetto ospite,. Così ora le cose sono semplici: Selezionare il volume da sottrarre nella vista ad albero (l\'ho rinominato come \"Roof volume to subtract\", quindi è facile da individuare), CTRL + selezionare un muro, e premere il tasto [Rimuovi](Arch_Remove/it.md). A sottrazione avvenuta, vedrete che il volume da sottrarre è scomparso sia nella vista 3D che nella vista ad albero. Questo perché il volume è stato contrassegnato come figlio del muro, e \"inghiottito\" da quel muro. Selezionare il muro, espanderlo nella vista ad albero, e vedrete che il volume è lì.

Ora, selezionare il volume nella vista ad albero, CTRL + selezionare il muro successivo, premere [Rimuovi](Arch_Remove/it.md). Ripetere l\'operazione per gli altri muri fino ad avere tutto correttamente tagliato:

<img alt="" src=images/Arch_tutorial_12.jpg  style="width:1024px;">

Ricordate che per [Aggiungi](Arch_Add/it.md) e [Rimuovi](Arch_Remove/it.md), l\'ordine in cui si selezionano gli oggetti è importante. Quello che ospita è sempre l\'ultimo, come in \"Rimuovi X da Y\" o \"Aggiungi X a Y\"


{{Note|Una nota sulle addizioni e sottrazioni|Gli oggetti Arch che supportano tali aggiunte e sottrazioni (tutti gli oggetti tranne gli aiuti "visivi" come gli assi) tengono traccia di tali oggetti tramite due proprietà, rispettivamente "Additions" e "Subtractions", che contengono un elenco di collegamenti agli altri oggetti da sottrarre o da aggiungere. Uno stesso oggetto può comparire in vari elenchi di diversi altri oggetti, come succede in questo caso per il volume di sottrazione. Ciascuno dei padri vorrebbe ingoiarlo nella vista ad albero, quindi di solito "vive" nell'ultimo. Per qualsiasi oggetto, si possono sempre modificare tali elenchi, facendo doppio clic su di esso nella vista ad albero, in modo che FreeCAD entri in modalità di modifica. Premendo il tasto ESC si esce dalla modalità di modifica.}}



## Creare i tetti 

Ora, per completare la struttura, rimangono da creare il tetto e le piccole solette interne. Ancora una volta, il modo più semplice è quello di disegnare i loro profili sulla parte superiore della sezione, con lo strumento [Polilinea](Draft_Wire/it.md). Qui ho disegnato tre profili su uno sopra l\'altro (nell\'immagine qui sotto li ho spostati in modo che si possano vedere meglio). Quello verde sarà utilizzato per i bordi laterali del solaio di copertura, poi quello blu per le parti laterali, e quelli rossi per la parte centrale, che si trova sopra il blocco bagno:

<img alt="" src=images/Arch_tutorial_13.jpg  style="width:1024px;">

Poi, dobbiamo ripetere l\'operazione di rotazione di cui sopra, per ruotare gli oggetti in una posizione verticale, quindi spostarli nelle loro posizioni corrette, e copiare alcuni di loro che dovranno essere estrusi due volte, con lo strumento [Sposta](Draft_Move/it.md), con il tasto ALT premuto, che crea delle copie invece di spostare l\'oggetto originale. Ho anche aggiunto altri due profili per le pareti laterali dell\'apertura del bagno.

<img alt="" src=images/Arch_tutorial_14.jpg  style="width:1024px;">

Quando tutti sono al loro posto, basta usare lo strumento [Estendi](Draft_Trimex/it.md) per estruderli, poi convertirli in oggetti [Struttura](Arch_Structure/it.md).

<img alt="" src=images/Arch_tutorial_15.jpg  style="width:1024px;">

Dopo questo, possiamo vedere che si presentano alcuni problemi: due delle colonne a destra sono troppo corte (dovrebbero arrivare fino al tetto), e c\'è un divario tra il solaio e le pareti dello studio in fondo a destra (nella vista in sezione il valore 2.60 della quota era ovviamente sbagliato). Grazie agli oggetti parametrici, tutto questo è molto facile da risolvere: per le colonne, basta cambiare la loro altezza in 6m, recuperare il tetto volume di sottrazione dalla visualizzazione ad albero, e sottrarlo alle colonne. Per le pareti, è ancora più facile: spostarle un po\' in basso. Poiché il volume di sottrazione copre anche quella zona, la geometria dei muri si adatta automaticamente.

Ora deve essere risolta un\'ultima cosa, c\'è una piccola soletta in bagno, che interseca alcuni muri. Risolviamo questo creando un nuovo volume sottrazione e sottraendolo poi a tali muri. Un\'altra caratteristica dello strumento [Estendi](Draft_Trimex/it.md) che usiamo per estrudere delle cose, è che si può anche estrudere una sola faccia di un oggetto esistente. Questo crea un nuovo oggetto separato, quindi non c\'è rischio di \"danneggiare\" l\'altro oggetto. Quindi possiamo selezionare la faccia di base della soletta piccola (si vede guardando il modello dal basso), poi premere il pulsante [Estendi](Draft_Trimex/it.md), ed estruderla ben oltre i tetti. Dopo, sottrarre il volume dalle due pareti interne del bagno con lo strumento [Rimuovi](Arch_Remove/it.md):

<img alt="" src=images/Arch_tutorial_16.jpg  style="width:1024px;">



## Pavimenti, scale e camino 

Ora, la struttura è completa, dobbiamo solo più costruire alcuni piccoli oggetti.



### Il camino 

Cominciamo con il camino. Ora sapete già come funziona, vero? Disegnare un paio di [contorni](Draft_Wire/it.md) chiusi, spostarli fino alla loro giusta altezza con lo strumento [Sposta](Draft_Move/it.md), estruderli con lo strumento [Estendi](Draft_Trimex/it.md), trasformare il più grande in una [struttura](Arch_Structure/it.md), e sottrarre quelli più piccoli. Notate come il tubo del camino non è stato disegnato sulla vista in pianta, ma ho trovato la sua posizione trascinando le linee blu dalle viste in sezione.

<img alt="" src=images/Arch_tutorial_17.jpg  style="width:1024px;">



### I pavimenti 

I pavimenti non sono ben rappresentati nei disegni di base. Se si esaminano le sezioni, non è possibile sapere dove sono e quanto sono spesso le solette. Quindi io suppongo che i muri sono situati sopra ai blocchi della fondazione, alla quota 0.00, e che anche le solette di 15 centimetri di spessore sono posate su quei blocchi. Quindi i pavimenti non passano sotto ai muri, ma intorno a loro. Potremmo farli creando prima una grande lastra rettangolare poi sottraendo le pareti, ma ricordate, le operazioni di sottrazione ci sono costate. Meglio farlo in pezzi più piccoli, sarà \"più conveniente\" in termini di calcolo, e se lo facciamo in modo intelligente, stanza per stanza, questo sarà anche utile dopo per calcolare le aree del pavimento:

<img alt="" src=images/Arch_tutorial_18.jpg  style="width:1024px;">

Una volta che i contorni sono disegnati, trasformarli semplicemente in [strutture](Arch_Structure/it.md), e dare loro una altezza di 0,15:

<img alt="" src=images/Arch_tutorial_19.jpg  style="width:1024px;">



### Le scale 

Ora le scale. Conosciamo un nuovo strumento Arch, lo strumento [Scala](Arch_Stairs/it.md). Questo strumento è ancora in una fase molto precoce di sviluppo, al momento in cui sto scrivendo, quindi non aspettatevi troppo da lui, ma è già molto utile per rendere semplici le scale dritte. è importante sapere che l\'utensile scala è pensato per costruire scale da un pavimento piano fino ad un muro. In altre parole, se visto dall\'alto, l\'oggetto scale occupa esattamente lo spazio che occupa nella vista in pianta, quindi l\'ultimo scalino non viene disegnato (ma è ovviamente tenuto in conto nel calcolo altezze).

In questo caso, ho preferito costruire la scale nella vista in sezione, perché avremo bisogno di molte misure che sono più facili da ottenere da questo punto di vista. Qui, ho disegnato un paio di linee guida rosse, poi due linee blu che saranno alla base delle due parti della scala e due contorni verdi chiusi, che formeranno le parti mancanti. Ora selezionare la prima linea blu, premere lo strumento [Scala](Arch_Stairs/it.md), impostare il numero di steps a 5, l\'altezza a 0,875, la larghezza a 1,30, il tipo di struttura a \"massive\", lo spessore struttura a 0,12. Ripetere l\'operazione per l\'altra parte.

Poi, estrudere i due contorni verdi di 1,30, ruotarli e spostarli nella giusta posizione:

<img alt="" src=images/Arch_tutorial_20.jpg  style="width:1024px;">

Nella vista in prospetto, disegnare (quindi ruotare) il contorno:

<img alt="" src=images/Arch_tutorial_21.jpg  style="width:1024px;">

Quindi spostare e posizionare tutto:

<img alt="" src=images/Arch_tutorial_22.jpg  style="width:1024px;">

Non dimenticate inoltre di tagliare la colonna che attraversa le scale, perché in BIM è sempre brutto avere oggetti che si intersecano. Ricordate che stiamo costruendo come nel mondo reale, dove gli oggetti solidi non possono intersecarsi. Qui, io non ho voluto sottrarre la colonna direttamente dalle scale (altrimenti, nella vista ad albero l\'oggetto colonna sarebbe stato inghiottito dall\'oggetto scale, e questo non mi piace), così ho preso la faccia su cui è stata costruita la colonna, e l\'ho estrusa di nuovo. Questa nuova estrusione è poi stata sottratta dalle scale.

Bene! Tutto il duro lavoro difficile ormai è fatto, andiamo avanti con il lavoro molto difficile!



## Porte e finestre 

Le [Finestre](Arch_Window/it.md) sono oggetti abbastanza complessi. Essi sono utilizzati per creare tutti i tipi di oggetti \"inseriti\", come finestre o porte. Sì, in FreeCAD, le porte sono solo un particolare tipo di finestra, e pensandoci bene, anche nella vita reale, o no? Lo strumento [Finestra](Arch_Window/it.md) attualmente può ancora essere un po\' difficile da usare, ma consideratelo un compromesso, siccome è stato costruito per la massima potenza. Con esso si può costruire quasi ogni tipo di finestra che riuscite ad immaginare. Ma appena lo strumento disporrà di ulteriori modelli predefiniti, la situazione migliorerà certamente.


<div class="mw-translate-fuzzy">

Gli oggetti [Finestra](Arch_Window/it.md) funzionano così: Si basano su un disegno 2D, qualsiasi oggetto 2D, ma preferibilmente uno [schizzo](Sketcher_Workbench/it.md), che contiene dei contorni chiusi, delle polilinee. Questi contorni definiscono le diverse parti della finestra: telai esterni, telai interni, pannelli di vetro, pannelli solidi, ecc. Gli oggetti finestra hanno quindi una struttura che memorizza cosa si deve fare con ciascuno di questi contorni: estruderli, posizionarli ad una certa distanza, ecc. Infine, una finestra può essere inserita in un oggetto ospite, come una parete o struttura, e crea automaticamente una apertura. Tale apertura è calcolata estrudendo il contorno più grande presente nel disegno 2D.


</div>

In FreeCAD, ci sono due modi per creare tali oggetti: utilizzando un modello predefinito, o creando da zero il disegno della finestra. Qui vedremo entrambi i metodi. Ma ricordate che il metodo del modello predefinito non fa altro che creare, per voi, il disegno dell\'oggetto e definire le estrusioni necessarie.



### Usare un modello predefinito 

Quando si preme lo strumento [Finestra](Arch_Window/it.md) con nessun oggetto selezionato, siete invitati a scegliere un disegno 2D, o ad utilizzare uno dei preset. Usiamo il preset \"Simple Door\" per posizionare la porta d\'ingresso principale del nostro modello. Dategli una larghezza di 1 m, una altezza di 2.45m, uno spessore W1 di 0,15 m, e lasciate gli altri parametri a 0.05m. Quindi fate clic nell\'angolo in basso a sinistra del muro, e vedrete che viene creata la nuova porta:

<img alt="" src=images/Arch_tutorial_23.jpg  style="width:1024px;">

Noterete che la nuova porta non appare nella vista ad albero. Questo perché, agganciandola ad un muro, abbiamo indicato che esso è il suo oggetto ospite. Di conseguenza, è stata \"inghiottita\" dal muro. Ma cliccando con il tasto destro sul muro → Vai alla selezione la troverete nell\'albero.

In questo caso, dato che la finestra non viene inserita in nessun muro (l\'apertura c\'era già), tanto vale svincolarla dal muro ospite. Questo viene fatto eseguendo un doppio clic sul muro ospite nella vista ad albero per entrare nella modalità di modifica. Lì si vede la finestra nel suo gruppo \"sottrazioni\". Basta selezionarla, premere il pulsante \"Rimuovi elemento\" e poi \"OK\". La nostra finestra è stato rimosso dal suo muro host, e si trova nella parte inferiore della struttura ad albero.

A sinistra abbiamo una seconda porta, esattamente come questa. Invece di creare una nuova porta da zero, abbiamo due modi per fare una copia della precedente: usando lo strumento [Sposta](Draft_Move/it.md), con il tasto ALT premuto, che, come già sapete, copia un oggetto anziché spostarlo, oppure, meglio ancora, possiamo usare lo strumento [Clona](Draft_Clone/it.md). Lo strumento clona produce un \"clone\" di un oggetto selezionato, che è possibile spostare, ma che mantiene la forma dell\'oggetto originale. Se l\'oggetto originale cambia, cambia anche il clone.

Quindi ora tutto quello che dobbiamo fare è selezionare la porta, premere il tasto [Clona](Draft_Clone/it.md), poi spostare il clone nella posizione corretta con lo strumento [Sposta](Draft_Move/it.md).



### Organizzare il modello 

<img alt="" src=images/Arch_tutorial_24.jpg  style="width:400px;">

Ora sarebbe un buon momento per fare un po\' di pulizia. Dato che abbiamo già due finestre, è bene fare un po\' di pulizia nella vista ad albero: creare un nuovo [gruppo](Std_Group/it.md), rinominarlo \"finestre\", e trascinare in esso le 2 finestre. Vi consiglio di separare in questo modo anche altri elementi, come i muri e le strutture. Dato che è anche possibile creare gruppi annidati, è possibile una ulteriore organizzazione, ad esempio inserendo tutti gli elementi che formano il tetto in un gruppo separato, in questo modo è facile attivarlo o disattivarlo (commutando un gruppo da visibile a invisibile, o viceversa, si applica la stessa azione a tutto il suo contenuto).


<div class="mw-translate-fuzzy">

L\'ambiente [Arch](Arch_Workbench/it.md) ha alcuni strumenti aggiuntivi per organizzare il modello: [Sito](Arch_Site/it.md), [Edificio](Arch_Building/it.md) e [Piano](Arch_Floor/it.md). Quei tre oggetti sono basati sul gruppo standard di FreeCAD , quindi si comportano esattamente come i gruppi, ma hanno alcune proprietà aggiuntive. Ad esempio, il [Piano](Arch_Floor/it.md) ha la capacità di impostare e gestire l\'altezza dei muri e delle strutture contenute, e quando viene spostato, vengono spostati anche tutti i contenuti.


</div>

Qui, dal momento che abbiamo solo un edificio con solo un piano (e mezzo), non vi è alcuna reale necessità di utilizzare tali oggetti, quindi ci bastano i gruppi semplici.




Ora, torniamo al lavoro. Nascondete il gruppo tetto, in modo da poter vedere meglio dentro, e cambiate la modalità di visualizzazione degli oggetti floor in Wireframe (o usate lo strumento [Aspetto](Draft_ToggleDisplayMode/it.md)) in modo da poterli ancora agganciare, ma si possa vedere il piano sottostante. Si può anche nascondere completamente i pavimenti, quindi posizionare le porte a livello 0, poi alzarle di 15 cm con lo strumento [Sposta](Draft_Move/it.md).

Posizioniamo le porte interne. Utilizzate nuovamente il \"Simple Door\" preset, create porte larghe 1.00m e 0.70m e alte 2,10 m , con dimensioni W1 di 0.1m. Accertatevi di agganciare correttamente il muro quando le inserite, in modo da creare automaticamente una apertura in quel muro. Se è difficile inserirle correttamente, è possibile posizionarle in un luogo più facile, in un angolo del muro, per esempio, e poi spostarle. L\'apertura si muove si muove insieme alla porta.

Se per sbaglio ospitate una finestra nel muro sbagliato, è facile da risolvere: rimuovete la finestra dal gruppo \"Subtraction\" del muro ospite in modalità di modifica, come abbiamo visto sopra, quindi aggiungetelo al gruppo \"Subtraction\" del muro giusto, con lo stesso metodo, o, semplicemente con lo strumento [Rimuovi](Arch_Remove/it.md).

Dopo un po\' di lavoro, ci sono tutte le porte:

<img alt="" src=images/Arch_tutorial_25.jpg  style="width:1024px;">

Dopo uno sguardo più attento alla vista in prospetto, ho rilevato un altro errore: la parte superiore delle pareti in mattoni non è a 2.60m, ma è più bassa di 17,5 cm, cioè a 2.425m. Fortunatamente, le finestre basate su un modello prestabilito hanno un vantaggio: è possibile modificare le loro dimensioni generali (larghezza e altezza) tramite le loro proprietà. Quindi cambiamo la loro altezza a 2,425-0,15, cioè, 2.275. La seconda finestra, siccome è un clone della prima, si adatterà anche lei. Questo è fondamentalmente un caso in cui si manifesta la vera magia della progettazione parametrica.

Ora possiamo guardare alle cose veramente interessanti: come progettare le finestre personalizzate.



### Creare delle finestre personalizzate 


<div class="mw-translate-fuzzy">

Come ho spiegato in precedenza, gli oggetti [Finestra](Arch_Window/it.md) sono creati da disegni 2D di elementi chiusi (contorni (polilinee), cerchi, rettangoli, nulla). Dal momento che gli oggetti [Draft](Draft_Workbench/it.md) non possono gestire più di uno di questi elementi, lo strumento preferito per disegnare le sagome delle finestre è [Sketcher](Sketcher_Workbench/it.md). Purtroppo, con l\'ambiente Sketcher, non è possibile lo snap agli oggetti esterni come si fa con nell\'ambiente Draft, cosa che qui sarebbe utile dato che i nostri prospetti sono già disegnati. Fortunatamente, esiste uno strumento per convertire gli oggetti Draft in uno schizzi: lo strumento [Converti Draft in Sketch](Draft_Draft2Sketch/it.md).


</div>

Cominciamo con la costruzione nostro primo disegno della finestra. L\'ho disegnato sul prospetto, utilizzando vari [rettangoli](Draft_Rectangle/it.md): uno per la sagoma esterna, e 4 per le sagome interne. Mi sono fermato davanti alla porta, perché, ricordate, la nostra porta ha già un telaio posizionato:

<img alt="" src=images/Arch_tutorial_26.jpg  style="width:1024px;">

Quindi, selezionare tutti i rettangoli, e premere il pulsante [Converti Draft in Sketch](Draft_Draft2Sketch/it.md) (ed eliminare i rettangoli, perché, per precauzione, questo strumento non elimina gli oggetti originali). Poi, con il nuovo schizzo selezionato, premere lo strumento [Finestra](Arch_Window/it.md):

<img alt="" src=images/Arch_tutorial_27.jpg  style="width:1024px;">

Lo strumento riconosce che il disegno ha un contorno esterno e diversi contorni interni, e propone automaticamente una configurazione predefinita: Una intelaiatura prodotta sottraendo i contorni interni da quello esterno e estrusi per 1m. Cambiamo queste impostazioni, entrando nella modalità di modifica della finestra, facendo doppio clic su di essa nella vista ad albero:

Vedete il componente \"Default\", che è stato creato automaticamente dallo strumento Finestra, che utilizza i 5 contorni (sempre sottraendo tutti gli altri dal più grande), e che ha un valore di estrusione di 1. Cambiamo il valore di estrusione a 0.1, per abbinarlo a quello che abbiamo usato per le porte.

Poi, andiamo ad aggiungere 4 nuovi pannelli di vetro, usando sempre lo stesso contorno, con una estrusione di 0,01, un offset di 0,05, e collocati al centro del telaio. Quando la finestra è finita, appare come questa:

<img alt="" src=images/Arch_tutorial_28.jpg  style="width:1024px;">

Suppongo che ora avete capito la potenza di questo sistema: è possibile qualsiasi combinazione di telai e pannelli di qualsiasi forma. Quello che è possibile disegnare in 2D, può esistere come un oggetto solido 3D valido.

Cerchiamo adesso di disegnare gli altri pezzi, poi sposteremo insieme ogni cosa al suo posto. Ma prima, bisogna fare alcune correzioni al disegno 2D di base, perché chiaramente dove le finestre si incontrano con le scale mancano alcune linee. Possiamo rimediare, scostando la linea della scala di 2,5 centimetri con lo strumento [Scosta](Draft_Offset/it.md), naturalmente con ALT premuto per copiare le linee invece di spostarle. Ora possiamo disegnare il nostro profilo, con [polilinea](Draft_Wire/it.md), poi convertirlo in uno schizzo, quindi da esso creare una finestra.

Ripetendo alcune volte queste operazioni (io l\'ho fatto in 4 parti separate, ma sta a voi decidere), completiamo la facciata:

<img alt="" src=images/Arch_tutorial_29.jpg  style="width:1024px;">

Ora, come prima, è solo più questione di ruotare i pezzi, e di posizionarli correttamente:

<img alt="" src=images/Arch_tutorial_30.jpg  style="width:1024px;">

L\'ultimo pezzo mancante è un segmento di muro che non appare nella vista in pianta e che deve essere aggiunto. Per questo, abbiamo diverse opzioni, io ho scelto di disegnare una linea sul piano terra, poi spostarla fino alla giusta altezza e quindi creare un muro su di essa. Dopo, bisogna anche recuperare il volume del tetto di sottrazione, che dovrebbe trovarsi contenuto nell\'oggetto ultima colonna, e sottrarlo dal muro. Ora questo lato dell\'edificio è pronto:

<img alt="" src=images/Arch_tutorial_31.jpg  style="width:1024px;">

Pronto? Non proprio. Guardate l\'immagine qui sopra, abbiamo creato le porte con un telaio di 5cm, che ricordate era il valore di default del preset. Le altre finestre, però, hanno uno spessore del telaio di 2,5 centimetri. Questo deve essere risolto.



### Modificare le finestre 

Abbiamo già visto come costruire e aggiornare i componenti della finestra, tramite la modalità di modifica della finestra, ma possiamo anche modificare il disegno a loro sottostante. Le finestre preimpostate non sono diverse da quelle personalizzate, ma semplicemente lo strumento [Finestra](Arch_Window/it.md) ha creato al nostro posto il disegno sottostante. Selezionare l\'oggetto door (l\'originale, non la copia, ricordiamoci che abbiamo fatto un clone), ed espanderlo nella vista ad albero. Ecco il nostro schizzo. Fare doppio clic su di esso per entrare in modalità di modifica.


<div class="mw-translate-fuzzy">

L\'ambiente [Schizzo](Sketcher_Workbench/it.md) è uno strumento estremamente potente. Non ha alcune delle comodità di [Draft](Draft_Workbench/it.md), come l\'ancoraggio o il piano di lavoro, ma ha molti altri vantaggi. In FreeCAD si utilizza di frequente uno o l\'altro a seconda delle necessità. La caratteristica più importante di Sketcher sono vincoli. I vincoli consentono di correggere automaticamente la posizione di alcuni elementi rispetto ad altri. Ad esempio, è possibile forzare un segmento a essere sempre in verticale, o a essere sempre ad una determinata distanza da un altro.


</div>

Quando noi modifichiamo il nostro schizzo porta, possiamo constatare che è prodotta da uno schizzo completamente vincolato:

<img alt="" src=images/Arch_tutorial_32.jpg  style="width:1024px;">

Ora basta modificare le distanze 5 cm tra la linea esterna e la linea interna, facendo doppio clic su di esse e cambiando il loro valore a 2,5 cm (Ricordate che al momento sto scrivendo questo, le unità non sono ancora pienamente funzionanti ). Appena clicchiamo sul pulsante \"OK\", la nostra porta (e il suo clone) vengono aggiornati.



## Lavorare senza il supporto 2D 

Fino ad ora il nostro lavoro è stato relativamente facile, perché avevamo i sottostanti disegni 2D su cui basare il nostro lavoro. Ma ora, dobbiamo costruire la facciata opposta e l\'atrio di vetro, e le cose diventano più complicate perché il disegno della facciata opposta ha un sacco di errori, non rappresenta l\'atrio, e noi non abbiamo il disegno per i muri interni dell\'atrio. Quindi dovremo inventare e crearci alcune cose da soli. Date uno sguardo a [reference pictures](http://www.pedrokok.com.br/2010/02/residencia-artigas-sao-paulo-sp/img_8265-533px/) per capire come sono fatte le cose. O fate come volete!

Una cosa che possiamo fare subito è duplicare la complicata finestra delle scale con lo strumento [Sposta](Draft_Move/it.md), perché è uguale su entrambi i lati:

<img alt="" src=images/Arch_tutorial_33.jpg  style="width:1024px;">

Notate che qui ho preferito duplicare con lo strumento [Sposta](Draft_Move/it.md) invece di utilizzare un [clone](Draft_Clone/it.md), perché attualmente il clone non supporta colori diversi all\'interno degli oggetti. La differenza è che il clone è una copia della forma finale dell\'oggetto originale, mentre se si copia un oggetto, si crea un nuovo oggetto con tutte le stesse proprietà di quello originale (e quindi, anche il suo schizzo di base e le sue definizioni dei componenti della finestra, che sono entrambi archiviati come proprietà).

Ora dobbiamo iniziare le parti che non sono disegnate in nessun posto. Cominciamo con la parete di vetro tra il salotto e l\'atrio. Sarà più facile disegnarle sulla vista in prospetto, perché avremo la giusta altezza del tetto. Quando siete in pianta, è possibile ruotare la vista dal menu Visualizza -\> Viste Standard -\> Ruota a sinistra o destra, fino ad ottenere una visualizzazione confortevole per lavorare, simile a questa:

<img alt="" src=images/Arch_tutorial_34.jpg  style="width:1024px;">

Notate come nell\'immagine qui sopra, ho fatto una linea dal modello alla sezione di sinistra, per ottenere l\'esatta larghezza della finestra. Poi, ho riprodotto tale larghezza nella vista di prospetto e l\'ho divisa in 4 parti. Dopo ho costruito il pezzo principale della finestra, più 4 finestre aggiuntive per le porte scorrevoli. Sketcher talvolta ha difficoltà con i contorni sovrapposti, quindi ho preferito tenerli separati in questo modo:

<img alt="" src=images/Arch_tutorial_35.jpg  style="width:1024px;">

Dopo le rotazioni necessarie, ogni cosa va perfettamente al proprio posto:

<img alt="" src=images/Arch_tutorial_36.jpg  style="width:1024px;">

Abbiamo ancora bisogno di alcuni pezzi nell\'angolo. Un piccolo trucco utile con lo strumento [piano di lavoro](Draft_SelectPlane/it.md), se avete una faccia selezionata quando premete il pulsante, il piano di lavoro corrisponde a questa faccia (almeno la sua posizione, e se la faccia è rettangolare, cerca anche di usare i suoi assi). Questo è utile per disegnare degli oggetti 2D direttamente sul modello, quindi, in questo caso, siamo in grado di disegnare direttamente nella sua posizione corretta un rettangolo da estrudere:

<img alt="" src=images/Arch_tutorial_37.jpg  style="width:1024px;">

Adesso facciamo i due pezzi rimanenti. Uno è facile, è una copia di quello che c\'è dall\'altra parte, quindi possiamo utilizzare semplicemente il disegno 2D:

<img alt="" src=images/Arch_tutorial_38.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

L\'altro è un po\' complicato, guardando le immagini, si vede che ha molte divisioni verticali, come le finestre delle scale. Casualmente (o perché Vilanova Artigas l\'ha progettata molto bene ), la larghezza della finestra, di 4.50m, è esattamente la stessa della finestra delle scale, quindi possiamo utilizzare la stessa divisione: 15 pezzi di 30 cm. Qui ho usato lo strumento [Schiera](Draft_Array/it.md) per copiare le due linee 15 volte, e vi ho disegnato sopra dei rettangoli:


</div>

<img alt="" src=images/Arch_tutorial_39.jpg  style="width:1024px;">

Fatto questo, possiamo creare la finestra con il metodo che conosciamo già. Nel caso che non lo abbiate ancora scoperto da soli, ecco un altro piccolo trucco utile: quando si modifica una finestra, se si modifica il nome di un componente, in realtà si crea un duplicato di essa. Quindi, per creare le 15 vetrate interne, invece di cliccare 15 volte il pulsante \"Aggiungi\" e compilare 15 volte i dati, si può modificarne uno solo, e cambiando il suo nome e contorno, si crea ogni volta una copia.

Dopo che la finestra viene ruotata e posizionata, l\'atrio è completo:

<img alt="" src=images/Arch_tutorial_40.jpg  style="width:1024px;">



## Modifiche e correzioni 

Ora, se guardiamo la nostra elevazione da dietro e lo confrontiamo con il piano, vediamo che ci sono alcune differenze che devono essere corrette. Vale a dire, le finestre delle camere sono più piccole di quanto sembravano all\'inizio e si deve allungare le pareti. Per correggere questo si deve tagliare i pavimenti:

<img alt="" src=images/Arch_tutorial_41.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

Naturalmente ci sono diversi modi per farlo, creando un volume sottrazione sarebbe un modo semplice, ma sarebbe aggiungere inutili complessità al modello. Meglio modificare il contorno di base di ogni pavimento. Qui è dove entra in azione la modalità [Modifica](Draft_Edit/it.md). Espandere i pavimenti nella vista ad albero, poi rendere visibile il loro contorno di base, quindi fare doppio clic su di essi per entrare nella modalità di modifica. Ora possiamo spostare i punti, oppure aggiungere o rimuovere dei punti. Con questo, modificare i nostri pavimenti diventa facile.


</div>

<img alt="" src=images/Arch_tutorial_42.jpg  style="width:1024px;">

Dopo un po\' di sudore (ovviamente, chi ha fatto questi disegni era ormai piuttosto pigro quando ha disegnato questa ultima elevazione e molte cose le ha disegnate sbagliate), finalmente abbiamo la nostra casa completa:

<img alt="" src=images/Arch_tutorial_43.jpg  style="width:1024px;">

Notare il tubo del camino, che è fatto da un cerchio che ho usato per fare un buco nel blocco della canna fumaria, che ho estruso, poi convertito in un tubo con lo strumento [Scosta](Part_Offset/it.md).


{{Note|Problemi negli oggetti|A volte un oggetto che si è creato può avere dei problemi. Ad esempio, l'oggetto si basava su qualcosa che è stato eliminato, e l'oggetto non può quindi ricalcolare la sua forma. Questi oggetti sono di solito mostrati con un piccolo segno rosso sulla loro icona, e/o un avviso nella finestra di output. Non esiste una ricetta generale per risolvere questi problemi, perché possono avere molte cause. Il modo più semplice per risolverli è spesso quello di eliminarli e poi, se non si eliminano i loro oggetti di base, ricreali.}}

## Output

Dopo tutto il duro lavoro che abbiamo fatto per costruire questo modello, arriva la ricompensa: cosa possiamo fare con esso? Fondamentalmente, questo è il grande vantaggio di lavorare con BIM, tutte le nostre esigenze architettoniche tradizionali, come disegni i 2D (piante, sezioni, ecc), rendering e calcoli (determinare le quantità, ecc) possono essere estratte dal modello. E, meglio ancora, possono essere rigenerate ogni volta che il modello cambia. Vi mostrerò qui come ottenere questi diversi documenti.



## Preparativi

Prima di iniziare ad esportare delle cose, è interessante fare una considerazione: come si è visto, il nostro modello sta diventando sempre più complesso, con un sacco di relazioni tra gli oggetti. Questo può rendere gravose le successive operazioni di calcolo, come, ad esempio, sezionare il modello. Un modo rapido per \"semplificare\" magicamente in modo drastico il modello è quello di rimuovere tutta questa complessità, esportandolo nel formato [STEP](http://en.wikipedia.org/wiki/ISO_10303-21). Tale formato conserva tutta la geometria, ma scarta tutte le relazioni e le costruzioni parametriche, salvaguardando solo la forma finale. Quando si reimporta il file STEP in FreeCAD, si ottiene un modello che non contiene alcuna relazione, e un file di dimensioni molto più piccole. Pensatelo come un file di \"output\", che è possibile rigenerare in qualsiasi momento dal file \"master\":

<img alt="" src=images/Arch_tutorial_44.jpg  style="width:1024px;">



### Esportazione in IFC e altre applicazioni 

<img alt="" src=images/Arch_tutorial_45.jpg  style="width:400px;">

Una delle cose veramente fondamentali che sono necessarie quando si lavora con BIM è quella di essere in grado di importare ed esportare i file[IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes). In FreeCAD, questo è ancora un work in progress. Il formato [IFC](Arch_IFC.md) è già supportato, e l\'importazione di file IFC è già abbastanza affidabile. L\'esportazione è ancora in fase sperimentale e attualmente ha molti limiti. Tuttavia, le cose stanno migliorando e speriamo di ottenere molto presto anche una corretta esportazione IFC.

[IFC export](Arch_IFC.md) richiede solo una minima configurazione dopo aver installato le librerie software necessarie. Semplicemente si deve ricreare la struttura dell\'edificio, che è necessaria in tutti i file IFC, aggiungendo al proprio file un [Edificio](Arch_Building/it.md) e poi un [Piano](Arch_Floor/it.md), quindi spostando in esso tutti i gruppi di oggetti che compongono il modello. Stare attenti a non inserire la geometria di costruzione (tutta la roba 2D che abbiamo disegnato) per evitare di appesantire inutilmente il file IFC.

Un\'altra cosa da impostare, è quello di verificare la proprietà \"Role\" degli elementi strutturali. Poiché IFC ha alcun elemento strutturale di tipo \"generic\"​​, come FreeCAD, bisogna assegnare loro dei ruoli (colonna, trave, ecc ..) in modo che l\'esportatore sappia quale elemento deve creare nel file IFC.

In questo caso, ci serve il nostro sistema architettonico complesso, in modo che l\'esportatore IFC possa sapere se un oggetto deve essere esportato come un muro o una colonna, quindi usiamo il nostro modello \"master\", e non il modello \"output\".

Fatto questo, è sufficiente selezionare l\'oggetto edificio, e scegliere il formato \"Industry Foundation Classes\". L\'esportazione in applicazioni non-BIM, come [Sketchup](http://www.sketchup.com/) è anche facile in quanto sono disponibili diversi formati di esportazione, come [Collada](Arch_DAE.md), STEP, IGES o OBJ.




### Rendering


<div class="mw-translate-fuzzy">

FreeCAD dispone anche di un modulo di rendering, che è il modulo [Raytracing](Raytracing_Workbench/it.md). Questo ambiente di lavoro attualmente supporta due motori di rendering, [PovRay](http://www.povray.org/) e [LuxRender](http://www.luxrender.net). Poiché FreeCAD non è progettato per il rendering delle immagini, le caratteristiche che l\'ambiente Raytracing vi offre sono un po\' limitate. La sequenza migliore di azioni quando si vuole fare rendering corretto, è quello di esportare il modello in un formato basato su maglia, come OBJ o STL, e aprirlo in un\'applicazione più adatta al rendering, come [blender](http://www.blender.org). L\'immagine sotto è stata prodotta con il motore di blender:


</div>

<img alt="" src=images/Arch_tutorial_47.jpg  style="width:1024px;">

Per un rendering veloce, l\'ambiente Raytracing può già fare un buon lavoro, con il vantaggio di essere molto facile da impostare, grazie al suo sistema di modelli. Questo è un rendering del nostro modello realizzato interamente all\'interno FreeCAD, con il motore Luxrender, utilizzando il modello \"indoor\".

<img alt="" src=images/Arch_tutorial_48.jpg  style="width:1024px;">

L\'ambiente Raytracing offre ancora un controllo molto limitato sui materiali, ma nei modelli sono definiti l\'illuminazione e gli ambienti che possono essere completamente personalizzati.



### Disegni 2D 

Certamente l\'uso più importante di BIM è quello per produrre automaticamente i disegni 2D . In FreeCAD questo viene fatto con lo strumento [Piano di sezione](Arch_SectionPlane/it.md). Questo strumento consente di posizionare nella vista 3D un oggetto \"piano di sezione\" orientabile per produrre piante, sezioni e prospetti. I piani di sezione devono sapere quali oggetti devono considerare, quindi dopo averne creato uno, è necessario aggiungergli degli oggetti ad essa con lo strumento [Aggiungi](Arch_Add/it.md). È possibile aggiungere singoli oggetti, o, più comodamente, un gruppo, un piano o un intero edificio. Questo permette di cambiare facilmente la portata di un certo piano di sezione, aggiungendo o rimuovendo gli oggetti a/da quel gruppo. Qualsiasi modifica a questi oggetti si riflette nelle viste prodotte dal piano di sezione.

Il piano di sezione produce automaticamente le viste in sezione degli oggetti che interseca. Per produrre viste, invece di sezioni, basta posizionare il piano di sezione al di fuori degli oggetti.

<img alt="" src=images/Arch_tutorial_49.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

I piani di sezione possono produrre due cose diverse: oggetti [shape](Part_Workbench/it.md), che convivono nello stesso documento come il modello 3D, oppure [viste](Drawing_Workbench/it.md) fatte per essere utilizzate in un foglio di disegno prodotto dall\'ambiente [Drawing](Drawing_Workbench/it.md). Ognuno di questi si comporta in modo diverso, e ha i suoi vantaggi.


</div>

**Viste Shape, Viste 2D**


<div class="mw-translate-fuzzy">

Questo output viene prodotto utilizzando lo strumento [Vista 2D](Draft_Shape2DView/it.md) con un piano di sezione selezionato. Si produce una vista 2D del modello direttamente nello spazio 3D, come nell\'immagine qui sopra. Il vantaggio principale è che si può lavorare su queste viste con gli strumenti di [Draft](Draft_Workbench/it.md) (o qualsiasi altro strumento standard di FreeCAD), in modo da poter aggiungere testi, dimensioni, simboli, ecc:


</div>

<img alt="" src=images/Arch_tutorial_50.jpg  style="width:1024px;">

Nella immagine qui sopra, sono stati prodotte due [Viste 2D](Draft_Shape2DView/it.md) per ogni sezione, una che mostra tutto, l\'altra che mostra solo le linee di taglio. Questo ci ha permesso di dare un diverso spessore di linea, e di aggiungere un tratteggio. Poi, sono state aggiunte le dimensioni, i testi, i simboli, e sono stati importati alcuni blocchi DXF per rappresentare i mobili. Queste viste sono anche facili da esportare in DXF o DWG, e da aprire nell\'applicazione di CAD 2D preferita, come ad esempio [LibreCAD](http://www.librecad.org) o [DraftSight](http://www.3ds.com/products-services/draftsight/overview/), dove è possibile lavorarle ulteriormente:

<img alt="" src=images/Arch_tutorial_51.jpg  style="width:1024px;">

Notare che alcune funzioni non sono ancora supportati dal [DXF/DWG exporter](Draft_DXF.md) quindi il risultato nella vostra applicazione 2D potrebbe essere un po\' diverso. Ad esempio, nell\'immagine sopra, ho dovuto rifare il tratteggio, e correggere la posizione di alcuni testi delle quote. Se in FreeCAD si posizionano gli oggetti in gruppi diversi, questi diventano i livelli, i layer, nella vostra applicazione di CAD 2D.

**ArchViews**

The other kind of output that can be produced from [section planes](Arch_SectionPlane.md) are [TechDraw ArchViews](TechDraw_ArchView.md). This method has one big limitation compared to the previous one: you have limited possibilities to edit the results, and at the moment, things like dimensioning or hatching are still not natively supported.

D\'altra parte, il risultato finale è più facile da manipolare, e dato che le possibilità grafiche del formato SVG sono enormi, questo sarà senza dubbio il metodo preferito in futuro. Al momento, però, si ottengono risultati migliori con il precedente.

<img alt="" src=images/Arch_tutorial_52.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

Nella immagine qui sopra, la geometria è l\'output diretto del piano di sezione, ma sono stati aggiunti alcuni altri oggetti di Draft, come le dimensioni e i poligoni tratteggiati, e da questi usando lo strumento [Drawing](Draft_Drawing/it.md) è stato prodotto un altro oggetto vista con la stessa scala e gli stessi valori di offset. In futuro, tali operazioni potranno essere effettuate direttamente sulla pagina di Drawing, lasciando il modello completamente pulito.


</div>



### Estrarre le quantità 


<div class="mw-translate-fuzzy">

Questo è un altro compito molto importante che deve essere eseguito sui modelli BIM. In FreeCAD, le cose si mettono bene fin dall\'inizio, dal momento che il kernel OpenCascade di FreeCAD si prende già cura di calcolare lunghezze, aree e volumi per tutte le forme che esso produce. Poiché tutti gli oggetti [Arch](Arch_Workbench/it.md) sono solidi, si è sempre sicuri di poter ottenere da loro un volume.


</div>

**Utilizzare i fogli di calcolo**

To populate a spreadsheet with values extracted from the model the Arch_Schedule tool can be used.

![](images/Arch_schedule_example03.jpg )

**La modalità di indagine**

Un altro modo per esaminare il modello e estrarre i valori, è quello di utilizzare la modalità [Ispeziona](Arch_Survey/it.md). In questa modalità è possibile fare clic sui punti, bordi, facce o fare doppio clic per selezionare gli oggetti interi, e si ottiene i valori di altezza, lunghezza, area o volume, indicati sul modello, stampati sulla finestra di output FreeCAD, e copiati negli appunti, in modo da poter facilmente selezionare, copiare e incollare i valori in un\'altra applicazione aperta contemporaneamente.

<img alt="" src=images/Arch_tutorial_54.jpg  style="width:1024px;">



## Conclusione


<div class="mw-translate-fuzzy">

Spero che questo offra una buona panoramica degli strumenti disponibili, per avere maggiori informazioni fate riferimento alla documentazione di [Arch](Arch_Workbench/it.md) e di [Draft](Draft_Workbench/it.md) (ci sono altri strumenti che non ho menzionato qui), e, più in generale, alle altre parti della [documentazione di FreeCAD](Main_Page/it.md). Pagare anche una visita al [forum](http://forum.freecadweb.org), molti problemi di solito possono essere risolti velocemente, e seguire il mio [blog](http://yorik.uncreated.net/guestblog.php?tag=freecad) per le novità sullo sviluppo dell\'ambiente Arch.


</div>

Il file creato durante questo tutorial è disponibile [qui](http://yorik.uncreated.net/archive/projects/casa_artigas.fcstd)



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch tutorial/it
