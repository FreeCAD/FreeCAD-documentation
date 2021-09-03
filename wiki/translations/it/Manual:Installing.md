


<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC/it}}

FreeCAD usa la licenza [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), che permette di scaricare, installare, ridistribuire e utilizzare FreeCAD nel modo desiderato, a prescindere dal tipo di lavoro si farà con esso (commerciale o non commerciale). Non si è tenuti a rispettare nessuna clausola o restrizione, e i file prodotti sono di completa proprietà dell\'autore. In realtà, l\'unica cosa vietata dalla licenza è quella di affermare che avete programmato FreeCAD voi stessi!

FreeCAD funziona senza alcuna differenza su Windows, Mac OS e Linux. Tuttavia, i metodi per installarlo differiscono leggermente a seconda della piattaforma. Su Windows e Mac, la comunità di FreeCAD fornisce i pacchetti precompilati (installatori) pronti per il download, mentre su Linux, il codice sorgente è reso disponibile dai manutentori delle distribuzioni Linux, che sono quindi i responsabili dei pacchetti di FreeCAD per la loro specifica distribuzione. Di conseguenza, su Linux, di solito si può installare la giusta versione di FreeCAD dal gestore del software.

La pagina ufficiale per il download di FreeCAD per Windows e Mac OS è <https://github.com/FreeCAD/FreeCAD/releases>

**Versioni di FreeCAD**

I rilasci ufficiali di FreeCAD che si trovano sulla pagina di cui sopra e nel software manager della distribuzione sono delle versioni stabili. Tuttavia, lo sviluppo di FreeCAD è veloce! Quasi ogni giorno sono aggiunte delle nuove funzionalità e viene corretto qualche bug. Dato che a volte può passare molto tempo tra una versione stabile e la successiva, si può essere interessati a provare una versione più avanzata di FreeCAD. Queste versioni di sviluppo, o pre-release, vengono caricate periodicamente sulla [pagina di download](https://github.com/FreeCAD/FreeCAD/releases) menzionata sopra, o, se si utilizza Ubuntu o Fedora, la comunità di FreeCAD mantiene anche un [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Personal Package Archives) e [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) o \'daily builds\' che viene regolarmente aggiornato con le modifiche più recenti.

Se si sta installando FreeCAD su una macchina virtuale, bisogna essere consapevoli che le sue prestazioni potrebbero essere basse, e in alcuni casi essere inutilizzabile, a causa del limitato supporto di [OpenGL](https://en.wikipedia.org/wiki/OpenGL) sulla maggior parte delle macchine virtuali.

### Installazione in Windows {#installazione_in_windows}

1.  Scaricare il pacchetto di installazione (.exe) corrispondente alla propria versione di Windows (32bit o 64bit) da [download page](https://github.com/FreeCAD/FreeCAD/releases). Gli installatori FreeCAD dovrebbero funzionare su qualsiasi versione di Windows a partire da Windows 7.
2.  Fare doppio clic sul programma di installazione scaricato.
3.  Accettare i termini della licenza LGPL, questo è uno dei pochi casi in cui si può veramente, fare clic in modo sicuro sul pulsante \"Accetto\" senza leggere il testo. Non ci sono clausole nascoste: ![](images/Freecad-windows-install-01.jpg )
4.  È possibile lasciare il percorso predefinito, o cambiarlo a piacere: ![](images/Freecad-windows-install-02.jpg )
5.  Non è necessario impostare la variabile PYTHONPATH, a meno che non si abbia intenzione di fare un po di programmazione Python avanzata, nel qual caso probabilmente è già noto di cosa si tratta: ![](images/Freecad-windows-install-03.jpg )
6.  Durante l\'installazione, vengono anche installati un paio di componenti aggiuntivi, che sono impacchettati all\'interno del programma di installazione: ![](images/Freecad-windows-install-04.jpg )
7.  Questo è tutto, FreeCAD è installato. Lo trovate nel menu Start. ![](images/Freecad-windows-install-05.jpg )

**Installare una versione di sviluppo**

Impacchettare FreeCAD e creare di un programma di installazione richiede un po\' di tempo e di dedizione, così, di solito, le versioni di sviluppo (chiamate anche pre-release) sono fornite come archivi .zip oppure .7z. Queste versioni non hanno bisogno di essere installate, basta decomprimerle e lanciare FreeCAD facendo doppio clic sul file FreeCAD.exe che si trova al suo interno. Questo permette di avere contemporaneamente sullo stesso computer sia le versioni stabili che quelle \"instabili\".

### Installazione in Linux {#installazione_in_linux}


<div class="mw-translate-fuzzy">

Sulla maggior parte delle distribuzioni Linux moderne (Ubuntu, Fedora, openSUSE, Debian, Mint, Elementary, ecc), FreeCAD può essere installato con il clic di un pulsante, direttamente dall\'applicazione di gestione del software fornita dalla propria distribuzione (dato che ogni distribuzione utilizza un proprio strumento, il suo aspetto può differire dalle immagini sottostanti).


</div>

1.  Aprire il gestore del software e cercare \"freecad\":

<img alt="" src=images/Freecad-linux-install-01.jpg  style="width:800px;">

1.  Fare clic sul pulsante \"Installa\" e il gioco è fatto, FreeCAD viene installato. Dopo, non dimenticare di votarlo!
    <img alt="" src=images/Freecad-linux-install-02.jpg  style="width:800px;">

**Metodi alternativi**

Uno dei grandi piaceri di usare Linux è la moltitudine di possibilità di adattare il software, quindi non trattenetevi. Su Ubuntu e derivate, FreeCAD può anche essere installato da un [PPA](https://launchpad.net/~freecad-maintainers) mantenuto dalla comunità di FreeCAD (contiene entrambe le versioni, la stabile e quella di sviluppo). Su Fedora è possibile installare le versioni di sviluppo recenti di FreeCAD da [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) e siccome questo è un software open-source, può anche essere [compilato](Compiling/it.md) facilmente.

### Installazione in Mac OS {#installazione_in_mac_os}

Installare FreeCAD su Mac OSX oggi è facile come sulle altre piattaforme. Tuttavia, dal momento che ci sono meno persone della comunità che possiedono un Mac, i pacchetti disponibili spesso sono in ritardo di un paio di versioni rispetto alle altre piattaforme.

1.  Scaricare il pacchetto zip corrispondente alla propria versione da [download page](https://github.com/FreeCAD/FreeCAD/releases).
2.  Aprire la cartella Download ed espandere il file zip scaricato: ![](images/Freecad-mac-01.jpg )
3.  Trascinare l\'applicazione FreeCAD dalla cartella zip alla cartella Applicazioni: ![](images/Freecad-mac-02.jpg )
4.  Questo è tutto, FreeCAD è installato! ![](images/Freecad-mac-03.jpg )

5\. Se il sistema impedisce l\'avvio di FreeCAD a causa delle restrizioni per le applicazioni non provenienti da App Store è necessario abilitarlo nelle impostazioni di sistema: ![](images/Freecad-mac-04.jpg )

### Disinstallazione

Speriamo che non si voglia disinstallare FreeCAD, comunque è bene sapere come farlo. In Windows e Linux, la disinstallazione FreeCAD è molto semplice. In Windows utilizzare l\'opzione standard \"Disinstalla\" che si trova nel pannello di controllo su Windows, o rimuoverlo con lo stesso gestore del software utilizzato per installare FreeCAD. Su Linux rimuoverlo con lo stesso software manager usato per installarlo. Su Mac, basta rimuoverlo dalla cartella Applicazioni.

### Impostare le preferenze di base {#impostare_le_preferenze_di_base}

Dopo aver installato FreeCAD, forse si desidera aprirlo e modificare alcune preferenze. Le impostazioni delle preferenze in FreeCAD si trovano nel menu **Modifica → Preferenze**. Sotto sono elencate alcune impostazioni di base che magari si desidera modificare; sfogliare le pagine delle preferenze per vedere se c\'è qualcos\'altro che si vuole cambiare.

1.  **Language**: (categoria *Generale*, scheda *Generale*)
2.  **Lingua**: FreeCAD sceglie automaticamente la lingua del sistema operativo, ma si può cambiarla. FreeCAD è quasi completamente tradotto in cinque o sei lingue; altre attualmente sono tradotte solo parzialmente. Si può facilmente [contribuire a tradurre FreeCAD](https://crowdin.com/project/freecad). ![](images/Freecad-basic-options01.jpg )
3.  **Modulo da caricare automaticamente**: (categoria *Generale*, scheda *Generale*) Normalmente, FreeCAD si avvia visualizzando la pagina Start center. È possibile saltare questo e iniziare una sessione di FreeCAD direttamente nell\'ambiente di lavoro preferito, elencato sotto *Avvio*, *Modulo da caricare automaticamente*.. Gli [ambienti di lavoro](Workbenches/it.md) sono spiegati in dettaglio nel [prossimo capitolo](Manual:The_FreeCAD_Interface/it.md).
4.  **Crea un nuovo documento all\'avvio**: (categoria *Generale*, scheda *Documento*) In combinazione con l\'opzione *Modulo da caricare automaticamente*, avvia FreeCAD pronto per il lavoro. ![](images/Freecad-basic-options02.jpg )
5.  **Archiviazione**: (categoria *Generale*, scheda *Documento*) Come tutte le applicazioni complesse, FreeCAD potrebbe bloccarsi di tanto in tanto. Qui è possibile configurare alcune opzioni che aiutano a recuperare il lavoro in caso di incidente.
6.  **Diritti d\'autore e licenze**: (categoria *Generale*, scheda *Documento*) Qui è possibile stabilire le impostazioni predefinite che verranno utilizzate per i nuovi file. Considerare fin dall\'inizio di rendere i file condivisibili, utilizzando una licenza amichevole, [copyleft](https://en.wikipedia.org/wiki/Copyleft) come [Creative Commons](https://creativecommons.org/).
7.  **Reindirizza l\'output interno di python nel report**: (categoria *Generale*, scheda *Finestra di Output*) Conviene sempre attivare queste due opzioni, in quanto indirizzano dei messaggi dall\'interprete python interno che appaiono nella [vista Report](Manual:The_FreeCAD_Interface/it#Report_view.md) quando c\'è un problema nell\'esecuzione di uno script python. ![](images/Freecad-basic-options03.jpg )
8.  **Unità**: (categoria *Generale*, scheda *Unità*) Qui si può impostare il sistema di unità di misura di default che si desidera utilizzare. ![](images/Freecad-basic-options04.jpg )
9.  **Zoom al cursore**: (categoria *Visualizzazione*, scheda *Vista 3D*) Se selezionato, le operazioni di zoom sono focalizzate sul puntatore del mouse, altrimenti il fuoco dello zoom è il centro della vista corrente.
10. **Inverti lo zoom**: (categoria *Visualizzazione*, scheda *Vista 3D*) Inverte la direzione dello zoom rispetto al movimento del mouse. ![](images/FreeCAD-v0-18-Preferences-Display.png ).

### Installare dei contenuti aggiuntivi {#installare_dei_contenuti_aggiuntivi}

Dato che il progetto FreeCAD e la sua comunità crescono rapidamente, e anche perché è facile da estendere, i contributi esterni e i progetti paralleli realizzati dai membri della comunità e da altri appassionati cominciano ad apparire ovunque su internet. La maggior parte di questi progetti esterni sono degli ambienti di lavoro o macro e possono essere facilmente installati direttamente da FreeCAD tramite [Addons Manager](AddonManager/it.md) che si trova nel menu **Strumenti**. Il gestore dei componenti aggiuntivi consente di installare molti componenti interessanti, ad esempio:

1.  Una [Parts library](https://github.com/FreeCAD/FreeCAD-library), che contiene tutti i tipi di modelli utili, o pezzi di modelli, creati dagli utenti di FreeCAD che possono essere utilizzati liberamente nei vostri progetti. È possibile accedere e usare le libreria direttamente dall\'interno della propria installazione FreeCAD.
2.  [Ambienti aggiuntivi](https://github.com/FreeCAD/FreeCAD-addons) che estendono le funzionalità di FreeCAD per determinate attività, ad esempio animano le parti dei modelli, come piegatura della lamiera o BIM. Ulteriori spiegazioni su ogni ambiente e su quali strumenti contiene sono fornite nella pagina di ogni addon, che si può visitare facendo clic sul link corrispondente in Addon manager.
3.  Una [collezione di macro](https://github.com/FreeCAD/FreeCAD-macros), che sono disponibili anche nel [wiki di FreeCAD](Macros_recipes/it.md) insieme alla documentazione su come usarle.

<img alt="" src=images/FreeCAD-addon-manager01.jpg  style="width:800px;">

Se si utilizza il sistema operativo Ubuntu, alcuni degli addon indicati sopra sono disponibili anche come pacchetti sul [FreeCAD addons PPA](https://launchpad.net/freecad-extras)

**Approfondimenti**


<div class="mw-translate-fuzzy">

-   [Altre opzioni di download](Download/it.md)
-   [Istruzioni di installazione dettagliate](Installing/it.md)
-   [PPA di FreeCAD per Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [PPA per gli addons di FreeCAD per Ubuntu](https://launchpad.net/freecad-extras)
-   [Compilare FreeCAD](Compiling/it.md)
-   [Tradurre FreeCAD](https://crowdin.com/project/freecad)
-   [La pagina di FreeCAD su github](https://github.com/FreeCAD)
-   [Il gestore degli addon di FreeCAD](AddonManager/it.md)


</div>


<div class="mw-translate-fuzzy">





</div>

[Category:Poweruser Documentation{{\#translation:}}](Category:Poweruser_Documentation.md) [Category:Tutorials{{\#translation:}}](Category:Tutorials.md)
