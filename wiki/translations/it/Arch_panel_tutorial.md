---
 TutorialInfo:t
   Topic:  Modellare un pannello in Arch
   Level:  Base
   Time:  60 minuti
   Author:  Yorik
   FCVersion: 
   Files: 
---

# Arch panel tutorial/it





Questo è un cross-post (duplicato) del [tutorial](http://opensourceecology.org/wiki/FreeCAD_Architecture_Tutorial) originariamente scritto per [Open-Source Ecology](http://opensourceecology.org).



## Presentazione di FreeCAD 

<img alt="" src=images/Arch_panel_tutorial_01.jpg  style="width:800px;">

FreeCAD è un modellatore 3D parametrico. La modellazione parametrica consente di modificare facilmente il proprio progetto andando all\'indietro nello storico del modello e cambiando i suoi parametri. FreeCAD è open source (licenza LGPL) e molto modulare, permette estensioni molto avanzate e la personalizzazione, specialmente grazie al suo intenso uso del linguaggio Python.

-   Sito Web di FreeCAD: <http://www.freecad.org/?lang=it>
-   Wiki della documentazione di FreeCAD: <http://www.freecad.org/wiki/index.php?title=Main_Page/it>
-   Gli ambienti di lavoro di FreeCAD: <http://www.freecad.org/wiki/index.php?title=Workbench_Concept/it>
-   Forum di FreeCAD: <http://forum.freecad.org/>
-   Iniziare con FreeCAD: <http://www.freecad.org/wiki/index.php?title=Getting_started/it>
-   Tutorial di Architettura: <http://www.freecad.org/wiki/index.php?title=Arch_tutorial/it>



## Installare FreeCAD 

È possibile installare l\'ultima versione stabile (ad oggi, maggio 2015, la versione 0.15) o una versione di sviluppo (attualmente la 0.16). In realtà, le versioni di sviluppo di FreeCAD sono solitamente abbastanza stabili, e si è fortemente incoraggiati a provare una versione di sviluppo, se non c\'è uno specifico motivo per non farlo. Dato che lo sviluppo di FreeCAD è abbastanza veloce, e se viene scaricato manualmente, bisogna controllare di tanto in tanto e reinstallarlo o aggiornarlo per beneficiare di tutti i miglioramenti.

-   Su Windows: Scaricare la versione più recente per la propria versione di Windows (32 o 64 bit) da <https://github.com/FreeCAD/FreeCAD/releases>. Fare doppio clic sul file per installarlo.
-   Su Mac OS: Scaricare la versione più recente da <https://github.com/FreeCAD/FreeCAD/releases>. Fare doppio clic sul file per installarlo.
-   Su Ubuntu: In genere la versione di FreeCAD fornita da Ubuntu è superata, perciò si consiglia di utilizzare al suo posto il PPA mantenuto dalla comunità di FreeCAD. Per installarlo, aprire l\'applicazione "Software Sources" di Ubuntu, e aggiungere alle sorgenti del software i ppa:freecad-maintainers/freecad-stable per la versione stabile, o il ppa:freecad-maintainers/freecad-daily per la versione di sviluppo.
-   Su altre piattaforme: Sulla maggior parte delle distribuzioni principali di Linux (Debian, Fedora, ecc), FreeCAD è incluso nei repository software ufficiali. Potrebbe però non essere sempre la versione più aggiornata. Se la versione necessaria non è disponibile, l\'unica opzione è quella di compilare FreeCAD da soli (le istruzioni sono sul sito di FreeCAD)



## Contenuti opzionali aggiuntivi 

-   Abilitare l\'importazione e l\'esportazione IFC: Per importare ed esportare i progetti nel formato di file IFC, FreeCAD si basa sull\'importatore IfcOpenShell, che è necessario installare separatamente da <http://ifcopenshell.org/python.html>. Accertarsi di scegliere una versione basata su una versione di Python2.7 che sia la stessa versione di Python utilizzata da FreeCAD.
-   Ambiente Drawing dimensioning: Un ambiente di lavoro aggiuntivo per FreeCAD che offre molti strumenti utili per aggiungere le quote e le annotazioni ai fogli di disegno 2D di FreeCAD: <https://github.com/hamish2014/FreeCAD_drawing_dimensioning> (le istruzioni di installazione sono nella pagina web)
-   Ambiente Assembly2: Un ambiente di lavoro aggiuntivo per FreeCAD che offre una serie di strumenti di base per l\'assemblaggio: <https://github.com/hamish2014/FreeCAD_assembly2> (le istruzioni di installazione sono nella pagina web)



## Suggerimenti per un avvio rapido 

La raccolta di tutorial disponibili sul wiki di FreeCAD è ancora molto scarsa. Tuttavia, molti membri della comunità di FreeCAD utilizzano YouTube per pubblicare dei video tutorial. Ricercate i contenuti correlati a FreeCAD su youtube, che è certamente la migliore fonte di materiale didattico.

FreeCAD è un\'applicazione molto tecnica, e la sua curva di apprendimento può essere ripida. Fate affidamento sulle esercitazioni, sul wiki della documentazione e non esitate a porre delle domande sul forum se incontrate un problema specifico. Le domande che sono enunciate chiaramente di solito ricevono delle risposte molto veloci ed estese.



### Un elenco molto approssimativo di cose che si devono sapere 

-   L\'interfaccia di FreeCAD è divisa in ambienti di lavoro. Gli ambienti sono semplicemente delle raccolte di strumenti (i pulsanti della barra degli strumenti e i menu) che, di solito, sono raggruppati per svolgere un determinato compito. Quando si passa ad un nuovo ambiente di lavoro, l\'interfaccia mostra gli strumenti di questo nuovo ambiente, ma il contenuto del documento 3D non cambia. Si sta ancora lavorando sullo stesso documento, e sugli stessi oggetti.

-   FreeCAD è ancora in fase di sviluppo, ci sono ancora molti bug, ed a volte l\'applicazione potrebbe bloccarsi. Salvare spesso, e abilitare il backup dei file in Modifica → Preferenze → Documento

-   In FreeCAD la maggior parte degli oggetti sono parametrici. Significa che loro geometria viene creata automaticamente da una serie di parametri. Questi parametri sono sempre modificabili nella finestra delle proprietà. Sono sempre divisi tra i parametri che influenzano la sola geometria (scheda Dati) ed i parametri che interessano solo la visualizzazione dell\'oggetto (scheda Vista). Gli oggetti creati con altre applicazioni, e importati in FreeCAD, di solito non sono definiti da parametri, quindi non sono modificabili.

-   Diversi ambienti di lavoro (PartDesign e Arch) sono fatti per funzionare solo con oggetti solidi, e si rifiutano di lavorare su oggetti che non sono dei solidi. Come regola cercare quindi di lavorare sempre con oggetti solidi.

-   Anche se FreeCAD può importare e lavorare con gli oggetti mesh (ambiente Mesh), esso è sostanzialmente progettato per funzionare con un tipo più avanzato di oggetti chiamato BREP, che viene utilizzato dalla maggior parte dei suoi ambienti (Parte, PartDesign, Draft, Sketcher, Arch). Durante l\'importazione dei file basati su mesh (.dae, .orb, .stl \...) di solito è necessario convertire questi oggetti in BREP prima di poterli usare per fare qualcosa di interessante. Comunque i formati di file basati su solidi (.step, .iges), al momento dell\'importazione in FreeCAD, producono direttamente gli oggetti BREP. Anche i formati 2D (.dxf, svg) producono dei contenuti BREP.

-   FreeCAD ha diversi modi, o modalità, di utilizzare i tasti del mouse. Queste modalità possono essere impostate nelle preferenze e modificabili al volo con un clic destro sullo sfondo della vista 3D. Essi sono descritti in <https://wiki.freecad.org/Mouse_navigation/it>. I modi più adatti per il lavoro CAD sono CAD o Gestures.



## Esercizio: modellare un pannello del tetto 

Per mostrare un tipico flusso di lavoro in FreeCAD, cercheremo di modellare un pannello del tetto come descritto in <http://opensourceecology.org/wiki/MicroHouse_4_Roof_-_Module_-_Build_Instructions>. Per fare questo, inizieremo disegnando i vari pezzi in uno schizzo 2D vincolato, poi ci avvantaggeremo dello speciale oggetto Finestra di Arch, che è in grado di costruire oggetti 3D complessi da uno schizzo 2D contenente i contorni di vari pezzi. Infine, dato che quello che ci serve non è una finestra, ma un pannello del tetto, ci basterà semplicemente convertire il nostro oggetto Finestra in un altro tipo di oggetto Arch.



### 1. Aprire FreeCAD, quindi impostare le unità di misura preferite in \"imperial\" 

Nel menu Modifica → Preferenze → Generale → Unità



### 2. Passare in Sketcher e creare un nuovo schizzo nel piano XY. 

![](images/Arch_panel_tutorial_02.jpg )

Di solito, a meno che non ci sia un motivo specifico per non farlo, si preferisce iniziare disegnando gli schizzi 2D sul piano terra, attorno al punto di origine (0,0). Poi, è l\'oggetto 3D generato da tali schizzi, che viene spostato o ruotato in posizione.



### 3. Disegnare due rettangoli. Applicare su ciascuno di essi un vincolo verticale di 16 piedi e un vincolo orizzontale di 2 pollici. 

![](images/Arch_panel_tutorial_03.jpg )

Non preoccupatevi delle dimensioni che hanno pezzi quando li disegnate, i vincoli li ridimensionano di conseguenza. Per aggiungere un vincolo di dimensione (verticale o orizzontale), è possibile selezionare una linea, o due punti (con CTRL premuto).



### 4. Quando i due rettangoli hanno la dimensione corretta, posizionare un vincolo verticale di 0 tra i loro punti d\'angolo, e un vincolo orizzontale di 4 piedi. 

![](images/Arch_panel_tutorial_04.jpg )

Questo garantisce che i due rettangoli abbiano reciprocamente un corretto posizionamento.



### 5. Aggiungere altri due ulteriori pezzi di 2 x 6 pollici 

![](images/Arch_panel_tutorial_05.jpg )

Aggiungere altri due rettangoli e ripetere il processo. Notare che nell\'esempio precedente, non è stata specificata la lunghezza di questi pezzi, ma è stato messo un vincolo di distanza tra le loro estremità e le parti verticali, e tra di loro è stato lasciato un piccolo spazio di 0,05 pollici. Questo perché se si creano dei rettangoli che si toccano, FreeCAD potrebbe confondere i contorni, e si potrebbero ottenere risultati strani con lo strumento finestra di Arch. Questo piccolo trucco assicura che ogni rettangolo venga riconosciuto dallo strumenti finestra di Arch come un contorno indipendente.



### 6. Aggiungere i pezzi angolari di rinforzo 

![](images/Arch_panel_tutorial_06.jpg )

Stessa cosa. Renderli larghi 6 pollici, e separarli da altri rettangoli di 0,05 pollici.



### 7. Disegnare 7 pezzi di rinforzo intermedi, impostare la loro larghezza a 2 pollici, e vincolare i loro punti finali, sinistro e destro, a 0,05 pollici dai rettangoli verticali (oppure a 0 pollici dei punti finali degli altri rettangoli orizzontali) 

![](images/Arch_panel_tutorial_07.jpg )

A seconda del sistema, FreeCAD potrebbe cominciare a essere lento nell\'elaborare i nuovi vincoli. Questo è lo svantaggio conseguente all\'uso degli oggetti vincolati, essi assorbono subito un sacco di risorse del sistema. Si deve sempre valutare se è assolutamente necessario usarli. È anche possibile eliminare i vincoli dopo che essi hanno fatto il loro lavoro. Queste dimensioni non saranno più fissate, ma esse non cambieranno, a meno che se non si spostino i pezzi. Se in seguito è necessario, è anche sempre possibile aggiungere nuovamente i vincoli.



### 8. Calcolare la distanza tra i 7 pezzi di rinforzo e impostare i loro vincoli verticali. 

Nel nostro caso, la lunghezza totale è di 192 pollici, meno i due pezzi laterali (2 x 2 pollici) e i due rinforzi angolari (2 x 6 pollici), = 192 -- (4 + 12) = 176. Sottraendo i 7 pezzi di rinforzo ( 7 x 2 ) si ottiene = 162. Dividendo questo per 8 si ottiene lo spazio tra ogni rinforzo: 20.25.

![](images/Arch_panel_tutorial_08.jpg )



### 9. Ottenere uno schizzo completamente vincolato 

Sul pannello di destra (Scheda Azioni della Vista combinata -\> Messaggi del solutore), è possibile vedere il messaggio \"\...2 gradi di libertà\". Questo significa che il disegno non è completamente vincolato (che può ancora essere deformato in due \"modi\"). Anche se ora nessun pezzo può più muoversi rispetto agli altri, l\'intero disegno può ancora muoversi verticalmente ed orizzontalmente. Per evitare questo, basta prendere uno dei suoi punti d\'angolo, selezionare il punto di origine della griglia (dove gli assi verde e rosso si intersecano) e premere il tasto di Vincolo su punto. Questo trasforma in verde lo schizzo, il che significa che è completamente vincolato, nessuna parte di esso può più muoversi.

![](images/Arch_panel_tutorial_09.jpg )

Questo non è indispensabile in assoluto, ma è sempre meglio tenere traccia della esatta posizione degli oggetti (ora c\'è la certezza che l\'angolo è nel punto (0,0)). Questo può essere utile in seguito nel caso in cui qualcosa vada storto, o ci sia bisogno di capire la posizione di un oggetto costruito su questo disegno,.

Ora lo schizzo di base è costruito e si può premere il pulsante \"Chiudi\":

![](images/Arch_panel_tutorial_10.jpg )



### 10. Passare all\'ambiente Arch e, con il disegno selezionato, premere il tasto \"Finestra\" 

Il disegno scompare e uno dei suoi rettangoli viene estruso leggermente in un pezzo solido:

![](images/Arch_panel_tutorial_11.jpg )

Anche se questo sembra sbagliato, avviene semplicemente perché lo strumento Finestra di Arch crea un pezzo di default dal contorno più grande che trova nel disegno di base. Rimedieremo al più presto. Inoltre, notare e prendere atto che il disegno non è scomparso, è semplicemente stato nascosto e \"inghiottito\" dal suo nuovo oggetto padre. È ancora possibile trovarlo nella vista ad albero, basta espandere l\'oggetto finestra e riattivare la sua visualizzazione premendo il tasto SPAZIO.



### 11. Modificare i componenti della finestra con un doppio clic su di essi nella vista ad albero 

![](images/Arch_panel_tutorial_12.jpg )

Facendo doppio clic sulla finestra, il suo schizzo di base diventa di nuovo visibile, e si accede alla sua interfaccia di modifica: A sinistra c\'è un elenco dei contorni presenti nello schizzo di base, a destra ci sono i pezzi solidi costruiti su tali schizzi.

Iniziare la rimozione del pezzo di \"Default\".

Per fare ciò, selezionare il primo contorno (Wire0). Esso viene evidenziato nella vista 3D. Premere il pulsante \"Aggiungi\" per creare un nuovo pezzo da esso. Dargli un nome, assicurarsi che sia impostato il contorno corretto, e dargli una estrusione di 6 pollici. L\'offset dovrebbe rimanere a 0 poiché lo vogliamo posizionato \"per terra\".

Per attribuire i materiali alla finestra viene utilizzato il valore \"Type\" (non ancora implementato), quindi attualmente si può lasciare su \"Frame\".

![](images/Arch_panel_tutorial_13.jpg )

Quindi premere il pulsante \"Crea componente\". A volte FreeCAD non riesce a indovinare la direzione dell\'estrusione, e si deve quindi editare il componente e cambiare il valore di 6 pollici in -6 pollici.

Ripetere questa operazione per tutti i pezzi necessari:

![](images/Arch_panel_tutorial_14.jpg )

Chiudendo il pannello di modifica si ottiene l\'oggetto di cui sopra. Notare che, per impostazione predefinita, gli oggetti finestre sono rappresentati semi-trasparenti. Dato che questo oggetto non sarà effettivamente una finestra, si può semplicemente disattivare la trasparenza impostando il suo valore a 0, nelle proprietà Vista.



### 12. Aggiungere il pannello di copertura 

A questo punto abbiamo il telaio del pannello, ma non ancora il vero pannello base. Per farlo, il modo migliore è quello di riaprire lo schizzo di base, e aggiungere un nuovo rettangolo. Ricordare però di fare in modo che nessuno degli angoli del rettangolo coincida con angoli di altri rettangoli, per non confondere l\'oggetto finestra, e non rischiare di dover rifare tutta la serie di componenti, se l\'ordine dei contorni cambiasse.

Quindi si può vincolare questo nuovo rettangolo a 0,05 pollici all\'interno del perimetro. Questo richiede di inserire 4 nuovi vincoli.

Possiamo quindi modificare di nuovo la finestra, e aggiungere i nuovi componenti. Possiamo vedere che è stato trovato un nuovo contorno. Questa volta lo useremo per aggiungere un pannello in policarbonato di 8mm (notare che in FreeCAD si possono mescolare le unità senza problemi, e scrivere \"8mm\" come spessore, anche se si sta lavorando in pollici). Dargli anche uno scostamento di 0,05 pollici, in questo modo esso viene scostato leggermente dal telaio, solo per coerenza, dato che tutte le parti del nostro oggetto hanno un offest tra di loro.

![](images/Arch_panel_tutorial_15.jpg )

Ora si può creare un altro componente basato sullo stesso contorno, per aggiungere un altro pannello alla struttura. Questa volta, dare un offset di 6,05 pollici. Finalmente il pannello è completo:

![](images/Arch_panel_tutorial_16.jpg )



### 13. Commutare la finestra in un altro tipo di componente Arch 

Questo non è veramente necessario in questo momento, ma può diventare importante in seguito, quando si esporta o si lavora per altre applicazioni orientate alle costruzioni, per esempio attraverso IFC, e non si vuole che il pannello sia identificato come una finestra.

L\'ambiente Arch di FreeCAD fornisce un modo semplice per gestire questo. Qualsiasi tipo di oggetto può sempre diventare di un tipo diverso, diventando la base di un altro tipo. In questo caso, commutiamo la finestra in un oggetto Pannello, semplicemente selezionando la finestra e premendo lo strumento Pannello.

![](images/Arch_panel_tutorial_17.jpg )

Notare che il colore del pannello risultante è cambiato, è perché in FreeCAD il supporto dei materiali e il modulo Arch sono ancora incompleti. Quando saranno finiti, questo sarà gestito adeguatamente.



### 14. Duplicare il pannello 

Il pannello può essere duplicato e copiato in diversi modi, ad esempio utilizzando copia / incolla. Ma un modo più interessante è quello di utilizzare lo strumento Clona di Draft (presente anche in Arch, come tutti gli altri strumenti di Draft). Lo strumento Clona mantiene una relazione tra l\'oggetto di base e il suo clone, in modo che qualsiasi modifica all\'oggetto base si riflette su tutti i suoi cloni.

![](images/Arch_panel_tutorial_18.jpg )

Nella attuale versione sviluppo di FreeCAD, gli oggetti Cloni di Arch ora sono anche essi stessi oggetti Arch.



### 15. Rotazione e posizionamento dei pannelli. 

Fino a quando l\'ambiente di assemblaggio di FreeCAD non sarà pronto, bisogna posizionare i pezzi manualmente, manipolando le loro proprietà Placement, o utilizzando gli strumenti Ruota e Sposta di Draft, che in realtà sono solo i modi visivi per modificare il posizionamento degli oggetti.

Entrambi gli strumenti Ruota e Sposta di Draft usano il sistema di Aggancio di Draft. Sono disponibili diverse posizioni di aggancio (punti finali, punti medi, ecc), che possono essere attivati o disattivati, permettendo di effettuare il posizionamento e le rotazioni con precisione.

![](images/Arch_panel_tutorial_19.jpg )

![](images/Arch_panel_tutorial_20.jpg )


{{BIM_Tools_navi

}} {{Draft_Tools_navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Category_Sketcher.md) > Arch panel tutorial/it
