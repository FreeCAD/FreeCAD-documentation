# Manual:Installing/it
{{Manual:TOC}}

FreeCAD è concesso con la licenza [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), che consente di scaricarlo, installarlo, ridistribuirlo e utilizzarlo per qualsiasi scopo, commerciale o non commerciale, senza alcuna restrizione. Viene mantenuta la piena proprietà dei file creati.

FreeCAD funziona in modo coerente su Windows, macOS e Linux, sebbene il processo di installazione vari in base alla piattaforma. Per gli utenti Windows e Mac, la comunità di FreeCAD offre programmi di installazione precompilati pronti all\'uso. Su Linux, il codice sorgente viene fornito ai manutentori della distribuzione che confezionano il software per i loro sistemi specifici. In genere, gli utenti Linux possono installare FreeCAD direttamente tramite il software manager del proprio sistema.

La pagina di download ufficiale di FreeCAD può essere trovata visitando [Pagina di download di FreeCAD](https://www.freecad.org/downloads.php). Ulteriori informazioni sul processo di installazione possono essere trovate nel [download wiki](https://wiki.freecad.org/Download) dedicato.

**Versioni di FreeCAD**

Le versioni stabili ufficiali di FreeCAD sono disponibili nella pagina di download di riferimento e nel gestore del software della propria distribuzione. Tuttavia, il ritmo di sviluppo di FreeCAD è elevato, con nuove funzionalità e correzioni di bug incorporate quasi ogni giorno. A causa dei lunghi periodi tra i rilasci stabili, si potrebbe voler sperimentare versioni più attuali e all\'avanguardia di FreeCAD. Queste versioni di sviluppo, o pre-release, possono essere trovate nella stessa pagina di download. Per gli utenti su Ubuntu o Fedora, la comunità di FreeCAD fornisce anche [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (archivi dei pacchetti personali) e [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) \'daily builds\', che vengono regolarmente aggiornate con gli ultimi sviluppi.

Se si prevede di installare FreeCAD su una macchina virtuale, tenere presente che le sue prestazioni potrebbero essere significativamente ridotte e forse renderlo inutilizzabile, a causa del supporto OpenGL limitato in molte macchine virtuali.



### Installazione in Windows 

1.  Scaricare un programma di installazione (.exe) dalla pagina di download. I programmi di installazione di FreeCAD dovrebbero funzionare su qualsiasi versione di Windows a partire da Windows 7.
2.  Accettare i termini della licenza LGPL; questo sarà uno dei pochi casi in cui si potrà davvero fare clic in tutta sicurezza sul pulsante \"accetta\" senza leggere il testo. Nessuna clausola nascosta: ![](images/LicenseAgreement_0212.jpeg )
3.  Sarà possibile mantenere il percorso predefinito o modificarlo se lo si desidera: ![](images/Path0212.jpeg )
4.  Assicurarsi di controllare tutti i componenti da installare: ![](images/Components0212.jpeg )
5.  Questo è tutto. L\'installazione è ora completa e si può ora iniziare ad esplorare le funzionalità di FreeCAD.

**Installare una versione di sviluppo**

Creare FreeCAD e sviluppare un programma di installazione comporta un notevole investimento di tempo e fatica. Di conseguenza, le versioni di sviluppo (chiamate anche versioni pre-release) vengono generalmente fornite sotto forma di archivi .zip o .7z situati nella [pagina di download di FreeCAD](https://www.freecad.org/downloads.php) . Non è necessario un processo di installazione formale con questi file; è sufficiente estrarre il contenuto e avviare FreeCAD facendo doppio clic sul file FreeCAD.exe situato al suo interno. Questo approccio consente inoltre di mantenere sia la versione stabile che quella \"instabile\" sullo stesso computer. È come avere un\'affidabile auto quotidiana e un jet pack sperimentale nel proprio garage!



### Installazione in Linux 

Per gli utenti delle moderne distribuzioni Linux come Ubuntu, Fedora, openSUSE, Debian, Mint ed Elementary, installare FreeCAD è semplice come fare un solo clic. E\' possibile installarlo senza problemi tramite lo strumento di gestione del software fornito dalla propria distribuzione, sebbene l\'aspetto di questi strumenti possa differire da qualsiasi immagine illustrativa poiché ciascuna distribuzione utilizza la propria distinta applicazione.

1.  Aprire il software manager e cercare \"freecad\":
2.  Fare clic sul pulsante \"Installa\" e il gioco è fatto, FreeCAD viene installato. Non dimenticare di dare una valutazione in seguito!
    <img alt="" src=images/linuxInstallation.png  style="width:800px;">

**Metodi alternativi**

Uno dei grandi piaceri dell\'utilizzo di Linux è la vasta gamma di opzioni disponibili per personalizzare la propria esperienza software, quindi non ci si deve trattenere. Per gli utenti di Ubuntu e dei suoi derivati, FreeCAD può essere installato da un [PPA](https://launchpad.net/~freecad-maintainers) gestito dalla comunità di FreeCAD, che include sia la versione stabile che quella di sviluppo. Su Fedora, è possibile accedere alle ultime versioni di sviluppo di FreeCAD tramite [1](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/copr). Inoltre, poiché FreeCAD è open source, si ha anche la libertà di [compilare FreeCAD da soli](Compiling/it.md).



### Installazione in Mac OS 

Installare FreeCAD su Mac OSX oggi è facile come sulle altre piattaforme. Tuttavia, dal momento che ci sono meno persone della comunità che possiedono un Mac, i pacchetti disponibili spesso sono in ritardo di un paio di versioni rispetto alle altre piattaforme.

1.  Scaricare il pacchetto zip corrispondente alla propria versione.
2.  Aprire la cartella Download ed espandere il file zip scaricato: ![](images/Freecad-mac-01.jpg )
3.  Trascinare l\'applicazione FreeCAD dalla cartella zip alla cartella Applicazioni: ![](images/Freecad-mac-02.jpg )
4.  Questo è tutto, FreeCAD è installato! ![](images/Freecad-mac-03.jpg )
5.  Se il sistema impedisce l\'avvio di FreeCAD a causa delle restrizioni per le applicazioni non provenienti da App Store è necessario abilitarlo nelle impostazioni di sistema: ![](images/Freecad-mac-04.jpg )



### Disinstallazione

Idealmente, non ci si vorrà mai separare da FreeCAD, ma se mai si dovesse aver bisogno di disinstallarlo, il processo è semplice. Su Windows, utilizzare la familiare opzione \"rimuovi software\" dal pannello di controllo. Per gli utenti Linux, disinstallalo utilizzando lo stesso gestore software utilizzato per installarlo. Per gli utenti Mac la soluzione è più semplice: basta trascinare FreeCAD dalla cartella Applicazioni al cestino.



### Impostare le preferenze di base 

Dopo aver installato FreeCAD, probabilmente si vorrà personalizzarlo modificando alcune impostazioni. È possibile trovare le impostazioni delle preferenze in FreeCAD accedendo a **Modifica → Preferenze** nel menu. Di seguito sono riportate alcune impostazioni di base che si potrebbe considerare di modificare subito, ma si è liberi di esplorare le varie pagine delle preferenze per adattare ulteriormente il software alle proprie esigenze.



#### Categoria Generale, scheda Generale 

![](images/FreeCAD_022_GeneralGen.png )

1.  **Lingua**: Per impostazione predefinita, FreeCAD selezionerà la lingua del sistema operativo, ma è possibile modificarla. Grazie alla dedizione di molti contributori, FreeCAD è disponibile in un\'ampia gamma di lingue.
2.  **Unità**: Questa impostazione consente di scegliere il sistema di unità predefinito per i propri progetti.



#### Categoria Generale, scheda Documento 

![](images/FreeCAD_022_GeneralDoc.png )

1.  **Crea un nuovo documento all\'avvio**: FreeCAD aprirà automaticamente un nuovo documento ogni volta che si avvia il programma.
2.  **Opzioni di Archiviazione**: Configurare qui le impostazioni per aiutarsi a recuperare il proprio lavoro in caso di arresto anomalo.
3.  **\'Diritti d\'autore e licenza**\': In quest\'area è possibile definire le impostazioni per i nuovi file. Per facilitare la condivisione, valutare la possibilità di iniziare con una licenza più permissiva e con permesso d\'autore come Creative Commons.



#### Categoria Visualizzazione, scheda Navigazione 

![](images/FreeCAD_022_DisplayNav.png )

1.  **Ingrandimento al cursore**: Se abilitato, le azioni di zoom si concentrano sul cursore del mouse. Se disabilitato, lo zoom si concentra sul centro della vista.
2.  **Inverti lo zoom**: Questa opzione inverte la direzione dello zoom in relazione al movimento del mouse.



#### Scheda Ambienti di lavoro 

![](images/FreeCAD_022_WBMenu.png )

Sebbene FreeCAD in genere si apre alla pagina iniziale, questa impostazione consente di ignorarla. E\' possibile iniziare direttamente nel proprio ambiente di lavoro preferito. Inoltre, è possibile personalizzare quali ambienti di lavoro vengono visualizzati nel menu di selezione.



#### Scheda Importa/Esporta 

![](images/FreeCAD_022_ImportExport.png )

Qui vengono definiti i parametri di base per l\'importazione e l\'esportazione in vari formati.



### Installare contenuti aggiuntivi 

Man mano che la comunità di FreeCAD si espande e cresce la facilità di personalizzazione, numerosi contributi esterni e progetti collaterali da parte di membri della comunità e appassionati iniziano ad apparire su Internet. Molti di questi progetti assumono la forma di ambienti di lavoro o macro ed è possibile aggiungerli facilmente alla propria cassetta degli strumenti tramite l\'[Addon Manager](Std_AddonMgr/it.md), accessibile dal menu Strumenti. L\'Addon Manager apre un mondo di possibilità, permettendo di installare vari componenti interessanti, come:

![](images/FreeCAD_022_AddonsMenu.png )

1.  Una \[libreria di parti <https://github.com/FreeCAD/FreeCAD-library>\]. Questa libreria è un tesoro di modelli utili o frammenti di modelli realizzati dagli utenti di FreeCAD. Tutti gli elementi di questa libreria sono disponibili gratuitamente per l\'uso nei propri progetti ed è possibile accedervi direttamente all\'interno della configurazione di FreeCAD.
2.  [Ambienti di lavoro aggiuntivi](https://github.com/FreeCAD/FreeCAD-addons). Si tratta di estensioni specializzate che migliorano le funzionalità di FreeCAD per compiti specifici. Applicazioni di esempio includono l\'animazione di parti del modello o la gestione di processi di costruzione specifici come la piegatura della lamiera o il BIM (Building Information Modeling). Informazioni dettagliate su ciascun workbench, inclusa una panoramica degli strumenti in esso contenuti, sono fornite nella pagina di ciascun componente aggiuntivo, accessibile tramite il collegamento corrispondente dell\'Addon Manager.
3.  Una vasta gamma di [macro](https://github.com/FreeCAD/FreeCAD-macros) sono disponibili per il download. Queste possono semplificare in modo significativo il flusso di lavoro e la documentazione dettagliata su come utilizzarle può essere trovata nel [wiki di FreeCAD](Macros_recipes/it.md).

A partire da FreeCAD v0.17.9940, il metodo di installazione consigliato di uno qualsiasi degli strumenti di cui sopra è l\'Addon Manager integrato. Tuttavia, se per qualsiasi motivo questa opzione non fosse disponibile, l\'installazione manuale è sempre possibile. Maggiori informazioni possono essere trovate nella [FreeCAD addons page](https://github.com/FreeCAD/FreeCAD-addons)

**Approfondimenti**

-   [Altre opzioni di download](Download/it.md)
-   [PPA di FreeCAD per Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [PPA per gli addons di FreeCAD per Ubuntu](https://launchpad.net/freecad-extras)
-   [Compilare FreeCAD](Compiling/it.md)
-   [Tradurre FreeCAD](https://crowdin.com/project/freecad)
-   [La pagina di FreeCAD su github](https://github.com/FreeCAD)
-   [Il gestore degli addon di FreeCAD](Std_AddonMgr/it.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/it
