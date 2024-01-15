# Frequently asked questions/it
In questa pagina sono riunite le domande più frequenti che sono state poste nel forum di FreeCAD. Probabilmente le soluzioni ai problemi e le risposte alle domande relative a FreeCAD si trovano già in questa pagina. Se non è così è possibile utilizzare il [forum di FreeCAD](http://forum.freecadweb.org/viewforum.php?f=3)!



## Installazione



### Il modo più facile per installare FreeCAD 

Se sei su Windows o macOS, il modo più semplice è andare al [ Download](Download.md), dove troverai diversi pacchetti pronti per l\'installazione. Se sei su Debian, Fedora o Ubuntu e alcune altre distribuzioni, FreeCAD è già incluso nei repository software standard e puoi semplicemente installarlo con il software manager. Su Ubuntu, il team di FreeCAD mantiene anche il proprio [repository PPA](Installing_on_Linux#Stable_PPA_version.md). Per ulteriori dettagli sull\'installazione, fare riferimento alla pagina di installazione del proprio sistema operativo ([Windows](Installing_on_Windows/it.md), [Linux](Installing_on_Linux/it.md) o [Mac](Installing_on_Mac/it.md)).



### Quali sono i prerequisiti per eseguire FreeCAD? 

Contrariamente alla maggior parte dei software di CAD 3D, FreeCAD può essere eseguito senza problemi anche su computer modesti - è noto che continua a funzionare anche su CPU Pentium IV e Intel Core2 Solo. Se nel computer è installato un sistema operativo corrente, è probabile che FreeCAD venga eseguito. L\'unico prerequisito è che la scheda grafica o il chipset supporti [OpenGL](https://it.wikipedia.org/wiki/OpenGL), preferibilmente non più vecchio della versione v2.0. In caso di problemi, consultare la sezione [Risoluzione dei problemi](Frequently_asked_questions/it#Risoluzione_dei_problemi.md) di queste FAQ.

#### Multithreading

Il kernel di modellazione geometrica sottostante a FreeCAD, la libreria di terze parti [OpenCASCADE Technology](https://it.wikipedia.org/wiki/Open_CASCADE_Technology) (OCCT), [ha solo un supporto multi-threading parziale in questo momento](https://forum.freecadweb.org/viewtopic.php?f=4&t=17501&p=173095&hilit=Multithread#p173095). Vedere la pagina [multithreading](multithreading.md) per maggiori dettagli.



#### Per gli utenti Mac 

È supportata solo l\'architettura MacIntel. Non sono disponibili build per l\'architettura PowerPC.



### E se voglio compilare FreeCAD? 

Il codice sorgente di FreeCAD è sempre disponibile nel repository del codice sorgente del progetto. La compilazione di FreeCAD in proprio consente di utilizzare le funzionalità più recenti in fase di sviluppo, ma richiede un po\' di conoscenza del computer, sebbene la procedura sia abbastanza semplice. L\'accesso al codice sorgente è spiegato [qui](Compile_on_Linux/it#Ottenere_il_codice_sorgente.md) e abbiamo istruzioni dettagliate per la compilazione su [Windows](Compile_on_Windows/it.md), [Linux](Compile_on_Linux/it.md) e [macOS](Compile_on_MacOS/it.md).



### FreeCAD segnala che mancano dei moduli o delle applicazioni 

FreeCAD dipende da molte cose per offrire tutte le sue funzionalità. Tutti i componenti principali richiesti sono solitamente raggruppati all\'interno dell\'installazione di FreeCAD o forniti dal gestore dei pacchetti, quindi normalmente non hai nulla di cui preoccuparti. Tuttavia se hai installato FreeCAD da fonti non ufficiali o hai compilato FreeCAD da solo, potrebbe mancare qualche pezzo, che non è fondamentale per FreeCAD stesso, ma potrebbe causare la non disponibilità di alcune funzionalità. Alcuni formati di file specifici come Collada o DWG richiedono anche componenti aggiuntivi, che non possono essere raggruppati in FreeCAD e devono essere installati separatamente.

Tutti questi componenti e il modo appropriato per installarli sono elencati nella pagina dedicata ai [ moduli Python aggiuntivi](Extra_python_modules/it.md).



## Risoluzione dei problemi 



### Problemi noti specifici del sistema operativo 

Trova i problemi noti specifici del sistema operativo in questa [discussione del forum](https://forum.freecad.org/viewtopic.php?t=30573)



### FreeCAD non si avvia affatto 

Potrebbero esserci molte ragioni per questo, la più probabile è che manchi qualche libreria. Prova ad avviare FreeCAD da un terminale (digitare {{SystemInput|freecad}} al prompt del terminale, {{SystemInput|FreeCAD}} su alcuni sistemi) per vedere se appare qualche messaggio di errore. Inoltre, leggi il resto di questa FAQ in quanto può darti più indizi per rilevare la causa del problema. Se nulla aiuta, parlane sul [forum](http://forum.freecadweb.org/), ci sarà sicuramente qualcuno che può aiutarti.

Su alcuni vecchi sistemi Windows XP potresti ricevere un messaggio di errore come questo: **The application can't start, because the side-by-side configuration is wrong. The reinstallation of the application may solve the problem.** Il motivo di questo problema è che sul tuo sistema mancano le librerie di runtime CRT o la versione installata è troppo vecchia perché FreeCAD era collegato a una versione più recente. In questo caso devi installare il **Microsoft Visual C++ Redistributable Package** che troverai in Microsoft. Vedi anche il corrispondente [messaggio sul forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=1298&p=9961).



### FreeCAD si avvia normalmente, ma non vengono visualizzate tutte le icone, alcune di esse sono sostituite da una \'X\' nera 

Alcune parti di FreeCAD dipendono da un modulo Python esterno chiamato Pivy. Su Windows, pivy è incluso nell\'installazione di FreeCAD. Sui sistemi Debian/Ubuntu, il pacchetto python-pivy fa parte dei repository software standard. Su altri sistemi, al momento, potresti dover compilare tu stesso pivy. Nota che sebbene alcuni strumenti non siano disponibili senza pivy, il resto di FreeCAD funziona normalmente.



### Ci sono dei problemi di visualizzazione, la vista 3D non si comporta correttamente, rimane dello sporco quando si muove o si ruota la vista, ecc. 

FreeCAD dipende da OpenGL per la visualizzazione di contenuti 3D e quindi richiede un ambiente OpenGL funzionante. Su alcuni sistemi, OpenGL non è attivato per impostazione predefinita e potrebbe essere necessario installare o aggiornare i driver grafici. Questo problema si verifica più spesso su sistemi Linux o su sistemi virtuali. Se utilizzi un sistema basato su Linux, prova i seguenti passaggi:

-   verifica che il tuo computer disponga di una scheda grafica compatibile con 3D
-   digita {{SystemInput|glxinfo}} in una finestra di terminale e controlla nell\'output che Direct Rendering sia impostato su \"yes\" e che il vendor/renderer/version di OpenGL corrisponda alla tua scheda grafica.



### FreeCAD si arresta all\'avvio 

Un arresto anomalo potrebbe indicare un bug più grave o qualche problema nella tua configurazione. La maggior parte degli arresti anomali all\'avvio si verifica a causa di uno dei due seguenti motivi:



#### I driver OpenGL non sono installati o non funzionano correttamente 

Questa è una causa molto comune del problema. I sintomi sono semplicemente che FreeCAD si arresta in modo anomalo all\'avvio o ogni volta che si apre una vista 3D (ad esempio creando un nuovo documento). Prova a scoprire qual è il tuo chip grafico, quindi scopri se supporta [OpenGL](https://it.wikipedia.org/wiki/OpenGL) (i chip più recenti lo fanno), quindi trova il driver corretto e installalo. Un buon modo per verificare se OpenGL è disponibile è provare a eseguire un\'altra applicazione OpenGL come [blender](http://www.blender.org).

E come suggerimento generale per ottenere qualche informazione in più sugli arresti anomali di FreeCAD, puoi avviarlo con il parametro del programma {{SystemInput|--write-log}}. Questo creerà il file **FreeCAD.log** in **$XDG_CONFIG_HOME/FreeCAD** ({{VersionPlus/it|0.20}}) o **$HOME/.FreeCAD** ({{VersionMinus/it|0.19}}) su Linux o **$HOME/Library/Preferences/FreeCAD** su macOS o **%APPDATA%/FreeCAD** su sistemi Windows.

In alcuni rari casi potresti avere un driver grafico installato, che non si adatta alla tua scheda grafica. Abbiamo avuto un caso in cui il laptop dell\'utente aveva una scheda grafica Intel integrata ma erano stati installati alcuni driver ATI. Fare riferimento al thread del forum in tedesco [FreeCAD startet nicht](http://forum.freecadweb.org/viewtopic.php?f=13&t=5160&start=10#p41042). Dopo aver rimosso i file e reinstallato il driver corretto, FreeCAD ha iniziato a funzionare.



#### Alcune librerie, necessarie a FreeCAD, non sono presenti nel sistema, o non vengono trovate da FreeCAD 

Ci possono essere due situazioni con questo problema: o manca semplicemente una libreria, quindi FreeCAD rifiuterà di avviarsi, oppure la libreria è presente, ma è una versione precedente a quella che FreeCAD si aspetta, quindi si verificherà un arresto anomalo quando FreeCAD tenterà di usare una funzione mancante da quella libreria. Un esempio comune è quando hai Qt3 e Qt4 installati sul tuo sistema, FreeCAD potrebbe rilevare Qt4 ma se l\'installazione di Qt non è configurata correttamente, alcuni pezzi di Qt3 potrebbero essere ancora utilizzati, provocando arresti anomali.

Si prega di rivedere la procedura di installazione ([Windows](Installing_on_Windows/it.md), [Linux](Installing_on_Linux/it.md) o [Mac](Installing_on_Mac/it.md)), assicurarsi di aver installato tutte le librerie richieste (sulla maggior parte dei sistemi Linux ciò avviene automaticamente), e controllare qual è il numero di versione minimo per ciascuno dei componenti.

Se tutto sembra corretto, descrivi il problema sul [forum](http://forum.freecadweb.org/) o [segnala un bug](Tracker/it.md). Se sei su un sistema Linux, è facile eseguire un backtrace di debug, che fornisce agli sviluppatori informazioni molto utili sul crash:

-   in un terminale, digita: {{SystemInput|gdb freecad}} (supponendo che il pacchetto gdb sia installato)
-   all\'interno di gdb, digita {{SystemInput|run}}
-   dopo il crash, digita {{SystemInput|bt}} per ottenere il backtrace, che puoi includere nella tua segnalazione di bug.



### FreeCAD si blocca dopo l\'avvio 

Quando si avvia FreeCAD la GUI appare quasi subito, ma rimane \"congelata\" e la CPU è impegnata circa al 99%. Questo può accadere sul desktop KDE quando si utilizza il tema Oxygen. Questo è un bug di Oxygen e utlizzando un tema diverso si dovrebbe risolvere il problema.



### FreeCAD si blocca quando si crea un nuovo documento o si apre un file 

Se FreeCAD si arresta in modo anomalo quando crea una nuova vista 3D, prova ad avviare FreeCAD da un terminale. Se viene visualizzato un messaggio di errore quando si verifica l\'arresto anomalo, menzionando {{SystemOutput|Assertion Failed}} e un nome componente che inizia con \"So\" ({{SystemOutput|SoBase}}, {{SystemOutput|SoFieldContainer}}, ecc.), le probabilità sono molto alte, specialmente se sei su Linux, che FreeCAD stia tentando di utilizzare due diverse versioni della libreria Coin, causando il crash. Per verificare se questo è effettivamente il problema, prova quanto segue:

-   Individua l\'eseguibile di FreeCAD (di solito in **/usr/lib/FreeCAD/bin**)
-   Esegui il comando {{SystemInput|ldd FreeCAD}} da un terminale
-   Prendere nota della versione della libreria **libCoin.so** utilizzata da FreeCAD (ad esempio **libCoin.so.60**)
-   Individua la libreria **libSoQt.so** (di solito in **/usr/lib**)
-   esegui {{SystemInput|ldd libSoQt.so}} e controlla se si collega alla stessa versione di Coin di FreeCAD

Se c\'è qualche differenza, è necessario ricompilare FreeCAD o SoQt (meglio ricompilare quello che utilizza la versione più vecchia di Coin). Il comportamento normale è cercare di contattare le persone responsabili del confezionamento di SoQt o FreeCAD e chiedere loro gentilmente di considerare la possibilità di ricompilare. Se vuoi intraprendere questo passaggio da solo e non è possibile ricompilare SoQt perché interrompe altre applicazioni sul tuo sistema, puoi forzare FreeCAD a compilare con la versione Coin richiesta con {{SystemInput|<nowiki>./configure - -with-coin=DIR</nowiki>}}. Ma devi assicurarti che sia installato il pacchetto di sviluppo corretto di questa versione di Coin.



### FreeCAD va in crash dopo Modifica -\> Allineamento 

Si verifica un errore di segmentazione in {{SystemOutput|vbo_save_playback_vertex_list()}}. Ciò significa che l\'implementazione di VBO nel driver grafico è pessima. Per evitare di memorizzare nella cache le chiamate OpenGL, puoi provare a impostare la variabile di ambiente {{SystemInput|<nowiki>IV_SEPARATOR_MAX_CACHES=0</nowiki>}} e riavviare FreeCAD.



### Ho problemi nell\'eseguire FreeCAD su macOS 

La piattaforma Mac è meno facile da supportare rispetto a Windows o Linux, poiché nessuno degli sviluppatori principali ne possiede una. I pacchetti macOS sono compilati da utenti FreeCAD volontari e a volte potrebbero non funzionare correttamente sulla tua macchina, a seconda del tuo sistema. La tua migliore possibilità è probabilmente quella di andare sui forum, cercare discussioni relative a macOS e discutere il tuo problema lì o vedere se qualcun altro ha trovato una soluzione.



### Non posso cambiare i valori numerici nei pannelli delle proprietà di FreeCAD 

<img alt="language options/it" src=images/Jj62l.png  style="width:480px;">

Molto probabilmente hai una cattiva configurazione delle impostazioni regionali di Windows. Controlla se hai lo stesso simbolo per il separatore decimale e il simbolo di raggruppamento delle cifre nelle impostazioni regionali. In tal caso, [adatta le tue impostazioni di sistema](http://forum.freecadweb.org/viewtopic.php?f=4&t=2655&p=20046#p20041) per utilizzare caratteri diversi per il simbolo di raggruppamento delle cifre e il separatore decimale. Si noti che non è obbligatorio avere il punto come separatore decimale. È obbligatorio utilizzare simboli diversi in queste due impostazioni. 



### FreeCAD stava funzionando normalmente, ma improvvisamente non si avvia più 

Ciò può accadere anche se hai installato una versione precedente di FreeCAD e hai eseguito l\'aggiornamento a una versione più recente. In quel processo, i file di configurazione di FreeCAD potrebbero essere stati danneggiati per qualche motivo, e di conseguenza FreeCAD non può più leggerli e non si avvia. La soluzione è semplicemente eliminare questi file di configurazione, così che FreeCAD li ricrei alla prima esecuzione.

-   Su Windows: apri Esplora file e scrivi **%APPDATA%\FreeCAD** come percorso del file. Una volta lì, elimina i file **user.cfg** e **system.cfg**
-   Su Linux: vai a **/home/USERNAME/.local/share/FreeCAD** ({{VersionPlus/it|0.20}}) o **/home/USERNAME/.FreeCAD** ({{VersionMinus/it|0.19}}) ed elimina i file **user.cfg** e **system.cfg**
-   Su Mac: vai a **/Users/USERNAME/Library/Preferences/FreeCAD** ed elimina i file **user.cfg** e **system.cfg**

FreeCAD dovrebbe riavviarsi normalmente con tutte le impostazioni ripristinate.

È disponibile una [Macro findConfigFiles](Macro_findConfigFiles/it.md) per aiutare a localizzare i file di configurazione. Può essere installata utilizzando Addon Manager nel menu Strumenti. **Strumenti → Addon Manager → Macro → findConfigFiles**. La macro troverà la cartella del file di configurazione, la copierà negli appunti e (tenterà di) aprire quella posizione con il browser di file predefinito. Non apporta modifiche ai file o alle impostazioni.



## Utilizzare FreeCAD 



### FreeCAD è veramente gratuito? Anche per uso commerciale? 

FreeCAD è [software open-source](http://en.wikipedia.org/wiki/Open-source_software) ed è gratuito non solo per l\'uso, per te stesso o per fare lavori commerciali, ma anche per distribuire, modificare o persino utilizzare in un\'applicazione closed-source. Per riassumere, sei libero di fare (quasi) tutto ciò che vuoi con esso. Vedere la pagina [Licenza](Licence/it.md) per maggiori dettagli.



### Come faccio a ruotare la vista 3D? 


<center>

Image:Style_of_navigation.png\|dal **bottone destro** del mouse Image:Style of navigation menu.png\|dal menu **Modifica → Preferenze →**


</center>




FreeCAD ha diverse [modalità di navigazione](Mouse_navigation/it.md) disponibili, che possono essere impostate nella finestra di dialogo delle impostazioni delle preferenze o modificate facendo clic con il pulsante destro del mouse nella vista 3D. Per tutti i dettagli sulle modalità, vedere la pagina [Navigare col mouse](Mouse_navigation/it.md).



### Cosa si può fare con FreeCAD? Da dove si inizia? 

Vai alla pagina [Guida introduttiva](Getting_started/it.md) per una rapida descrizione degli strumenti che puoi utilizzare. C\'è anche una nuova sezione [Tutorial](Tutorials/it.md) contenente alcune risorse. La sezione [User hub](User_hub/it.md) contiene informazioni più dettagliate sui diversi ambienti di lavoro di FreeCAD. Si noti che poiché FreeCAD è relativamente nuovo, la sua interfaccia utente è ancora molto spoglia e non dispone di molti strumenti. Ma funzionalità molto più avanzate sono già disponibili in [Python scripting](Power_users_hub/it.md).



### La documentazione per i nuovi utenti​​ è disponibile? Come imparare ad usare FreeCAD? 

C\'è molta documentazione sparsa in luoghi diversi, sia all\'interno che all\'esterno del sito Web di FreeCAD. Potresti voler iniziare con la pagina [Per iniziare](Getting_started/it.md). La sezione [Tutorial](Tutorials/it.md) contiene molte pagine di tutorial specializzate per aiutarti a iniziare con i diversi ambienti di lavoro. Il [Manuale:Introduzione](Manual:Introduction/it.md) è una guida generale e completa per l\'utente a FreeCAD. La sezione [User hub](User_hub/it.md) di questo wiki elenca tutte le pagine rivolte agli utenti finali. Su siti esterni come [Youtube](https://www.youtube.com/results?search_query=freecad), troverai anche un insieme di tutorial video creati dagli utenti. E, ultimo ma non meno importante, il [forum](https://forum.freecadweb.org) contiene molte risposte alle domande poste da altri nuovi arrivati.



### Voglio importare/esportare dati in formato XYZ in/da FreeCAD. Come lo faccio? 

Fare riferimento alla pagina [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md). Forse le tue domande lì hanno già una risposta.



### Dove posso trovare soluzioni alternative per funzionalità che FreeCAD attualmente non supporta? 

Fare riferimento alla pagina [Workarounds](Workarounds.md).



## Lavorare con le geometrie di Part 



### Come fare per estrudere i solidi. Non ottengo il risultato corretto 

La teoria è semplice: le linee (o polilinee), quando vengono estruse, formano delle facce. Le facce, quando vengono estruse, formano dei solidi.

Se estrudi qualcosa e il risultato non è un solido, allora quel qualcosa non era una faccia. Se hai delle linee e vuoi estrudere un solido da esse, devi prima selezionare le linee che formano un perimetro chiuso (selezionare diversi oggetti premendo **Ctrl**), unirli in una linea ([Draft Promuovi](Draft_Upgrade/it.md)), quindi creare una faccia da quella linea (<img alt="" src=images/Draft_Upgrade.svg  style="width:16px;"> [Draft Promuovi](Draft_Upgrade/it.md) di nuovo). Ecco qua, se tutto è andato bene ora puoi estruderlo in un solido.

Ora, ci possono essere molti piccoli colpi di scena che ti fanno ottenere il risultato sbagliato. Il modo migliore per essere sicuri è controllare cosa c\'è all\'interno dell\'oggetto che stai estrudendo. I contenuti degli oggetti possono essere facilmente esplorati con python. Supponendo ad esempio che tu abbia un oggetto chiamato \"Wire\", puoi digitarlo nella console Python:


{{code|code=
obj = FreeCAD.ActiveDocument.Wire
shp = obj.Shape
print shp.Faces
print shp.Wires
if shp.Wires:
    for w in shp.Wires:
        print w.isClosed()
}}

Il codice precedente recupera la forma da un oggetto, mostra le facce e le linee del tuo oggetto (se presenti) e, se ci sono linee, stampa se quelle linee sono chiuse. Se non hai una faccia, non otterrai un solido. Se non c\'è una linea chiusa, non diventerà una faccia. Se sei interessato, ci sono maggiori informazioni su cosa puoi controllare con Python nella pagina [Script di dati topologici](Topological_data_scripting/it.md). Se non è possibile unire più linee in un unica linea, la causa più probabile è che i loro punti finali non si incontrano, potrebbero esserci piccoli spazi tra di loro (o in alcuni di essi). In questo caso, temo, la mia esperienza mi dice che il modo più rapido sarebbe ridisegnare una linea sopra di loro.



### Le operazioni booleane non riescono, o danno strani risultati 

Il kernel di modellazione geometrica [Open CASCADE](https://it.wikipedia.org/wiki/Open_CASCADE_Technology) utilizzato in FreeCAD per la geometria delle parti, sebbene probabilmente il miglior kernel di geometria open source disponibile, ha i suoi difetti e limiti. Infatti le operazioni booleane (fusione, sottrazione, intersezione) non sono le sue caratteristiche migliori e spesso danno risultati strani. Questa è una limitazione attuale che non abbiamo modo di risolvere in breve, quindi il tuo percorso migliore è provare a ottenere il risultato desiderato modellando in un altro modo. Ad esempio, i problemi con le primitive come il cilindro possono essere spesso risolti utilizzando invece un cerchio estruso. Le superfici complanari tra le parti possono causare problemi, così come la tangenza della superficie. Come regola generale, se una forma non funziona, prova a rimodellarla in un modo diverso. Nel 99% dei casi alla fine riuscirai ad ottenere il risultato che desideri.



### Quando esporto (o visualizzo) il mio modello, i vuoti vengono riempiti 

Non utilizzare **Ctrl** + **A** (Seleziona tutto) per esportare tutto dall\'albero della gerarchia. Se il modello è di un singolo elemento, provare a selezionare solo l\'elemento più recente (di solito l\'ultimo) nell\'albero della gerarchia.

Quando creiamo un modello nell\'[Ambiente Part Design](PartDesign_Workbench/it.md), ogni funzione prende la forma dell\'ultima e aggiunge o rimuove qualcosa, creando dipendenze lineari da funzione a funzione durante la creazione del modello. Quindi una funzione \"Taglia\" non è solo il foro tagliato stesso, ma l\'intera parte con il taglio. Questo è il motivo per cui l\'utente di solito dovrebbe avere solo l\'elemento più recente (caratteristica) nell\'albero del modello visibile, perché altrimenti le fasi del modello si sovrappongono e i buchi vengono riempiti dalle funzioni del modello precedenti.

Per attivare o disattivare la visibilità di un oggetto, selezionalo nell\'albero della gerarchia e premi **barra spaziatrice** sulla tastiera. Di solito tutto tranne l\'ultimo elemento nell\'albero della gerarchia dovrebbe essere disattivato e quindi non visibile nella [Vista 3D](3D_view/it.md).



### I miei oggetti parametrici si rompono quando modifico i loro schizzi di base 

Hai incontrato il (famigerato) famoso problema della toponomastica. Questo è attualmente un problema importante in FreeCAD per i nuovi arrivati. È presente in tutto FreeCAD, ma è più evidente quando si usano gli [schizzi](Sketcher_Workbench/it.md). La spiegazione è semplice: quando si ricalcola uno schizzo, le entità geometriche (spigoli, facce\...) vengono ricostruite in un ordine diverso, a seconda della precedenza dei vincoli. Ricevono quindi un nome diverso (Edge1, Edge2, Face1, Face2\...). La maggior parte delle operazioni successive dipendono da questi nomi per identificare su quale sottocomponente si applicano. Pertanto, quando lo schizzo viene ricostruito, le funzioni basate su tali sottocomponenti potrebbero cambiare improvvisamente la loro geometria di base e fornire un risultato errato.

Questo è un problema molto difficile da superare (il [Topological Naming Project](Topological_Naming_Project/it.md) mira a risolverlo). Tuttavia, sono disponibili molte soluzioni alternative per mitigare il problema e gli utenti più avanzati generalmente riescono a evitarlo completamente. Un paio di strategie sono:

-   Sappi che gli schizzi sono altamente sensibili al problema. Fare riferimento a un bordo specifico di uno schizzo o a una faccia di un oggetto costruito su uno schizzo, come un [PartDesign Pad](PartDesign_Pad/it.md), è pericoloso, a meno che tu non sia abbastanza sicuro che questi schizzi non cambieranno nel tempo o lo schizzo è molto semplice. Un Pad costruito su un semplice schizzo rettangolare, ad esempio, sarà probabilmente sicuro in quanto genererà solo una faccia, quindi non ci sono problemi di ordine.
-   Preferisci altri tipi di oggetti come [Part](Part_Workbench/it.md) o [Draft](Draft_Workbench/it.md) quando possibile. Questi oggetti sono sempre costruiti allo stesso modo, e quindi le loro componenti geometriche di solito seguono lo stesso ordine ogni volta che vengono ricostruiti. Sono molto meno suscettibili ai problemi di toponomastica.
-   Per collegare altri oggetti alle facce della geometria basata su schizzo, utilizzare [Geometria di riferimento](PartDesign_Plane/it.md). Questi \"oggetti di supporto\" invisibili non dipendono dalla geometria dello schizzo e quindi rimangono stabili nel tempo.



## Contribuire a FreeCAD 



### FreeCAD è un grande programma! Come si può contribuire? 

Ci sono molti modi diversi per aiutare, anche se non sei un programmatore. Ecco un paio di cose che puoi fare:

-   Fornisci un feedback agli sviluppatori di FreeCAD: è sempre utile sapere cosa pensano le persone, cosa hanno trovato di buono, cosa gli manca, ecc. Scrivi una nota sul [forum](http://forum.freecadweb.org/) dando il tuo parere, esprimendo un\'opinione o facendo una richiesta sul nostro [issue tracker](https://tracker.freecadweb.org/main_page.php)!
-   Aiuta con la scrittura della documentazione: la documentazione che abbiamo su questo sito a volte è molto limitata. Se hai scoperto qualcosa che non è ben documentato, aggiungi lì le tue conoscenze!
-   Aiuta gli altri nuovi arrivati: resta nel forum e aiuta le nuove persone a risolvere domande di base, come installare, come aggiungere un cubo, ecc.
-   [Traduci la documentazione](Help_FreeCAD/it#Tradurre_la_documentazione.md) nella tua lingua
-   [Traduci FreeCAD](Help_FreeCAD/it#Tradurre_FreeCAD.md) nella tua lingua
-   Scrivi [Tutorial](Tutorial/it.md) o registra tutorial video: i tutorial sono un modo molto semplice per i principianti di imparare un nuovo software. Se hai fatto delle cose carine, perché non mostrare agli altri come si fa?
-   Contribuisci con risorse ed esempi: in FreeCAD mancano ancora dei buoni file di esempio. Se hai creato qualcosa di buono, condividilo con noi!
-   [Invia bug](Tracker/it.md): è molto importante che tutti i possibili bug siano corretti. Se ne trovi uno, segnalalo nel modo più chiaro possibile, così possiamo capire esattamente cosa sta succedendo.
-   Prova a fare un scrivere un po\' di codice Python: non hai mai programmato prima ma vuoi provare? Python è facile. Leggi la nostra [introduzione a Python](Introduction_to_Python/it.md), ma attenzione, potresti diventare dipendente rapidamente!
-   Consulta la pagina [Help FreeCAD](Help_FreeCAD/it.md) per maggiori dettagli su come contribuire.



### Come si può ottenere il permesso di modificare il wiki? 

Vedere il paragrafo della pagina [Migliorare la documentazione](Help_FreeCAD/it#Migliorare_la_documentazione.md) per maggiori dettagli su come contribuire.



### FreeCAD partecipa al Google Summer of Code? 

Sì. A partire dal 2016, FreeCAD partecipa a Google Summer of Code. Vedi [Google Summer of Code 2020](Google_Summer_of_Code_2020.md) per informazioni sulle edizioni passate e [Google Summer Of Code 2016](http://forum.freecadweb.org/viewtopic.php?f=8&t=13838) nel forum per l\'annuncio originale.



### Voglio iniziare a tradurre il wiki nella mia lingua. Cosa devo fare? 

Questo wiki ospita molti contenuti. Il materiale più aggiornato ed interessante viene raccolto nel [manuale](Online_Help_Toc/it.md).

Vedi il paragrafo della pagina [Tradurre la documentazione](Help_FreeCAD/it#Tradurre_la_documentazione.md) per maggiori dettagli su come tradurre il wiki.



### Posso comprare gadget? 

FreeCAD non offre gadget che si possono ordinare per sostenere il progetto. Ma è possibile crearne uno proprio. Per le istruzioni, consultare la pagina [Swag](Swag.md).



## Licenze, copia e riutilizzo 



### Si deve pagare qualcosa per usare FreeCAD? 

No. FreeCAD è totalmente gratuito da usare, scaricare, ridistribuire o modificare. Si tratta di [software open-source](https://en.wikipedia.org/wiki/Open_source), pubblicato secondo i termini della [GNU Lesser General Public License 2.1](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), che ti garantisce quelle libertà e, cosa ancora più importante, ti garantisce che queste libertà non ti saranno mai tolte.



### Posso riutilizzare qualsiasi parte della grafica di FreeCAD o parti del sito Web? 

Sicuro. Tutti gli artwork (icone, banner, ecc.) di FreeCAD sono concessi in licenza LGPL, come il codice FreeCAD. Aiutati nella pagina [Artwork](Artwork/it.md). Il sito Web è un sito MediaWiki standard, tutti gli elementi grafici possono essere riutilizzati liberamente e se sei curioso di sapere come modificare il software MediaWiki come abbiamo fatto noi, cerca le speciali pagine Common css e js.



### Si può riutilizzare parti di FreeCAD in un\'altra applicazione? 

Sì, puoi utilizzare le parti principali di FreeCAD in altre applicazioni purché rispetti i termini della LGPL. Le librerie di terze parti, gli [ambienti complementari](External_workbenches/it.md) e le [macro](Macros/it.md) possono essere soggette alle proprie condizioni di licenza, quindi consulta i loro autori. Maggiori dettagli nella pagina [Licenza](Licence/it.md).



---
⏵ [documentation index](../README.md) > [Documentation](Category_Documentation.md) > Frequently asked questions/it
