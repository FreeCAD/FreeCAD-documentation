# Compile on Windows/it
Questa pagina spiega passo dopo passo **come compilare FreeCAD 0.19 o più recente su Windows** utilizzando il compilatore MSVC di Microsoft. Per informazioni sull\'utilizzo di MSYS2/MinGW, vedere [Compilare su MinGW](Compile_on_MinGW/it.md). Per altre piattaforme vedere [Compilare FreeCAD](Compiling/it.md).



## Prerequisiti

La compilazione di FreeCAD su Windows richiede diversi strumenti e librerie.



### Programmi richiesti 

-   Un compilatore. FreeCAD è testato con Visual Studio (MSVC): altri compilatori potrebbero funzionare, ma le istruzioni per l\'uso non sono incluse qui. Per maggiori dettagli, vedere la sezione [Compilatore](#Compilatore.md) di seguito.

-   [Git](http://git-scm.com/) (Sono disponibili anche frontend GUI per Git, vedere la sezione successiva.)

-   [CMake](https://cmake.org/download/) versione 3.11.x o successiva.  *Suggerimento:* Scegliendo l\'opzione *Add CMake to the system PATH for all users*, durante l\'installazione di CMake, si renderà CMake accessibile dal prompt dei comandi di Windows, il che può essere utile.

-   Il [LibPack](https://github.com/FreeCAD/FreeCAD-LibPack). Questo è un singolo pacchetto contenente tutte le librerie necessarie per compilare FreeCAD su Windows. Scaricare la versione del LibPack che corrisponde alla versione di FreeCAD che si desidera compilare. Per compilare FreeCAD 0.20 scaricare il [LibPack versione 2.6](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/2.6), per FreeCAD 0.19 scaricare il [LibPack versione 1.0](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/1.0). Estrarre il LibPack in una posizione facilmente accessibile. (Se il tuo computer non riconosce l\'estensione .7z, installare il programma [7-zip](https://www.7-zip.org).)  **Nota**: Si consiglia caldamente di compilare FreeCAD con la versione del compilatore per cui è progettato il LibPack. Ad esempio, si potrebbero riscontrare problemi durante la compilazione di FreeCAD 0.20 utilizzando MSVC 2017 perché il LibPack è progettato per essere compilato con MSVC 2019 o versioni successive.Per aggiornare il LibPack in un secondo momento, consultare la sezione [Aggiornamento del Libpack](#Aggiornamento_del_Libpack.md).



### Programmi opzionali 

-   Un frontend GUI per Git. Ci sono diversi frontend disponibili, vedere [questa lista](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs). Il vantaggio principale di un frontend è che non si devono imparare i comandi Git per scaricare il codice sorgente di FreeCAD o per inviare patch al repository GitHub di FreeCAD.

Di seguito descriviamo la gestione del codice sorgente usando il frontend [TortoiseGit](https://tortoisegit.org/). Questo frontend si integra direttamente in Windows con Esplora file e dispone di una grande comunità di utenti per ricevere assistenza in caso di problemi.

-   [NSIS](http://sourceforge.net/projects/nsis/) viene utilizzato per generare il programma di installazione di Windows di FreeCAD.



### Codice sorgente 

A questo punto si può scaricare il codice sorgente di FreeCAD:



#### Utilizzo di un frontend 

Quando si utilizza il [frontend di Git](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit:

1.  Creare una nuova cartella in cui verrà scaricato il codice sorgente.
2.  Fare clic con il tasto destro su questa cartella in Esplora file di Windows e selezionare nel menu contestuale **Git Clone**.
3.  Apparirà una finestra di dialogo. In esso, inserisci l\'URL per il repository Git di FreeCAD

*<https://github.com/FreeCAD/FreeCAD.git>*

e clicca **OK**.

L\'ultimo codice sorgente verrà scaricato dal repository Git di FreeCAD e la cartella verrà tracciata da Git.



#### Usando la riga di comando 

Per creare un ramo locale e scaricare il codice sorgente è necessario aprire un terminale (prompt dei comandi) e portarsi nella directory in cui si desidera creare il sorgente, quindi digitare:


```python
git clone https://github.com/FreeCAD/FreeCAD.git
```



### Compilatore

Il compilatore predefinito (consigliato) è MS Visual Studio (MSVC). Sebbene sia possibile utilizzare altri compilatori, ad esempio gcc tramite Cygwin o MinGW, questi non sono testati o esaminati qui.

È possibile ottenere una versione gratuita di MSVC (per uso individuale) scaricando la [versione *Community* di MS Visual Studio](https://visualstudio.microsoft.com/vs/community/).

Per chi vuole evitare l\'installazione completa dell\'ingombrante MSVC al solo scopo di avere un compilatore può vedere [Compilare in Windows - Occupare meno spazio](CompileOnWindows_-_Reducing_Disk_Footprint/it.md).

**Nota:** Sebbene l\'edizione *Community* di MSVC sia gratuita, per utilizzare l\'IDE per un periodo di prova superiore a 30 giorni è necessario creare un account Microsoft. Se compilerai solo utilizzando la riga di comando, non avrai bisogno dell\'IDE e quindi di nessun account Microsoft.

Come IDE alternativo gratuito e OpenSource puoi usare [KDevelop](https://www.kdevelop.org/download). Puoi usare KDevelop per modificare e scrivere codice C++, ma devi usare la riga di comando per compilare.



### Configurazione opzionale del percorso di sistema 

Facoltativamente è possibile includere i percorsi di alcune cartelle nella variabile PATH di sistema. Ciò è utile se si desidera accedere ai programmi in queste cartelle dalla riga di comando/powershell o se si desidera che il compilatore o CMake trovino programmi speciali. Oltre a questo, potrebbe essere necessario aggiungere cartelle al PATH se non si sono utilizzate le opzioni corrispondenti durante l\'installazione del programma.

-   Si può includere la cartella del tuo LibPack nella variabile PATH del tuo sistema. Ciò è utile se si prevede di creare più configurazioni / versioni di FreeCAD.
-   Se non si ha utilizzato l\'opzione per aggiungere CMake al PERCORSO durante l\'installazione, aggiungere la sua cartella di installazione

*C:\\Program Files\\CMake\\bin* to the PATH.

-   Se non si ha utilizzato l\'opzione per aggiungere TortoiseGit al PERCORSO durante l\'installazione, aggiungere la sua cartella d\'installazione

*C:\\Program Files\\TortoiseGit\\bin* to the PATH.

Per aggiungere percorsi di cartelle alla variabile PATH:

1.  Nel menu Start di Windows, fare clic con il pulsante destro del mouse su \"Computer\" e scegliere \"Proprietà\".
2.  Nella finestra di dialogo visualizzata, fare clic su \"Impostazioni di sistema avanzate\".
3.  Si aprirà un\'altra finestra di dialogo. Fare clic nella scheda *Avanzate* in **Variabili d\'ambiente**.
4.  Ancora una volta si aprirà un\'altra finestra di dialogo. Selezionare quindi la variabile *Percorso* e fare clic su **Modifica**.
5.  Si aprirà un\'altra finestra di dialogo. Fare clic su **Nuovo** e aggiungere al percorso la cartella di Git o LibPack.
6.  Infine cliccare **OK** e chiudere tutte le finestre di dialogo cliccando ancora **OK**.



## Configurazione

Una volta che hai tutti gli strumenti, le librerie e il codice sorgente di FreeCAD necessari, sei pronto per iniziare il processo di configurazione e compilazione. Questo processo procederà in cinque fasi:

1.  Eseguire CMake una prima volta per esaminare il tuo sistema e iniziare l\'avanzamento della configurazione (verrà segnalato che l\'operazione non è riuscita).
2.  Aggiustare le impostazioni CMake necessarie per configurare i percorsi del LibPack e abilitare Qt5.
3.  Rieseguire CMake per finalizzare la configurazione (questa volta dovrebbe riuscire).
4.  Utilizzare CMake per generare il sistema di compilazione di Visual Studio.
5.  Utilizzare Visual Studio per creare FreeCAD.

### CMake

Inizialmente configurare l\'ambiente di compilazione utilizzando CMake:

1.  Aprire la GUI di CMake
2.  Specificare la cartella di origine di FreeCAD.
3.  Specificare una cartella di compilazione. Questa può essere **build** nella cartella in cui è stato clonato il repository, perché questo percorso è ignorato da git. Non utilizzare la cartella di origine. CMake creerà questa cartella se non esiste.
4.  Fare clic su **Configura**.
5.  Nella finestra di dialogo, che appare, specificare il generatore, che si desidera utilizzare: nella maggior parte dei casi verranno utilizzate le impostazioni predefinite in questa finestra di dialogo. Per lo standard MS Visual Studio utilizzare *Visual Studio xx 2yyy* dove xx è la versione del compilatore e 2yyy l\'anno del suo rilascio. Si consiglia di utilizzare l\'opzione predefinita *Use default native compilers*.

**Nota:** È importante specificare la variante col numero di bit corretta. Se hai la variante a 64 bit di LibPack devi usare anche il compilatore x64.

Questo avvierà la configurazione e *fallirà* a causa delle impostazioni mancanti. Questo è normale: non hai ancora specificato la posizione del LibPack. Tuttavia, potrebbero verificarsi altri errori, che richiedono ulteriori azioni da parte tua.

Se non riesce, con il messaggio che Visual Studio non è stato trovato, il supporto CMake in MSVC non è ancora installato. Per farlo:

1.  Aprire l\'IDE MSVC
2.  Utilizzare il menu Strumenti → Ottieni strumenti e funzionalità
3.  Nella scheda *Workloads* abilita *Desktop development with C++*
4.  Sul lato destro ora si dovrebbe vedere il messaggio, che il componente *Visual C++ tools for CMake* verrà installato.
5.  Installarlo.

Se fallisce, con un messaggio relativamente alla versione Python errata o Python mancante, allora:

1.  Usare la casella \"Search:\" in CMake per cercare la stringa \"Python\"
2.  Se si ottiene un percorso come *C:/Program Files/Python38/python.exe*, CMake ha trovato, che Python è già installato sul tuo PC, ma che quella versione non è compatibile con il LibPack. Poiché il LibPack include una versione compatibile di Python, modificare le seguenti impostazioni Python nei percorsi di CMake (supponendo che il LibPack si trovi nella cartella *D:/FreeCAD-build/FreeCADLibs_2\_8_x64_VC2019*):

![](images/CMake_Python_settings.png )

Se non appaiono errori da Visual Studio o da Python, va tutto bene, ma CMake non ha ancora tutte le impostazioni necessarie. Pertanto successivamente:

1.  Cercare in CMake la variabile **FREECAD_LIBPACK_DIR** e specificare la posizione della cartella LibPack, che è stata scaricata in precedenza.
2.  (Se si sta compilando FreeCAD 0.19) Cercare la variabile **BUILD_QT5** e abilitare questa opzione.
3.  (*Se si sta pianificando di eseguire direttamente dalla cartella di compilazione, ad esempio per il debug*) Cercare e attivare le seguenti opzioni:
    -   **FREECAD_COPY_DEPEND_DIRS_TO_BUILD**
    -   **FREECAD_COPY_LIBPACK_BIN_TO_BUILD**
    -   **FREECAD_COPY_PLUGINS_BIN_TO_BUILD**
4.  Fare di nuovo clic su **Configure**.

Ora non dovrebbero apparire errori. Se si continua a riscontrare errori, che non si riesce a diagnosticare, visitare le pagine [Install/Compile forum](https://forum.freecadweb.org/viewforum.php?f=4) sul sito Web del forum di FreeCAD. Se CMake ha terminato correttamente, cliccare su **Generate**. Fatto ciò si può chiudere CMake e avviare la compilazione di FreeCAD utilizzando Visual Studio. Tuttavia, per la prima compilazione, tenerlo aperto nel caso in cui si desideri o sia necessario modificare alcune opzioni per il processo di compilazione.



### Opzioni per il processo di compilazione 

Il sistema di generazione CMake offre la flessibilità necessaria per il processo di creazione. Ciò significa che è possibile attivare e disattivare alcune funzionalità o moduli tramite le variabili di CMake.

Ecco una descrizione di alcune di queste variabili:

  Nome Variabile                      Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Valore di Default
    
  BUILD_XXX                           Fare il Build di FreeCAD con il componente XXX. Se non si vuole o non si ha bisogno di compilare ad es. l\'ambiente *OpenSCAD*, disabilitare la variabile *BUILD_OPENSCAD*. FreeCAD quindi non avrà questo ambiente di lavoro. **Nota:** Alcuni componenti sono necessari per altri componenti. Se per esempio deselezioni *BUILD_ROBOT* CMake ti informerà che il componente *Path* non può essere compilato correttamente. Pertanto controllare l\'output di CMake dopo aver modificato un\'opzione BUILD_XXX!                                                                                                                                                                                                                                                         dipende
  BUILD_ENABLE_CXX_STD                La versione standard del linguaggio C++. **C++14** è il più alto possibile per FreeCAD 0.19 mentre almeno **C++17** è richiesto per FreeCAD 0.20. Vedere anche la nota nella sezione [Compilazione con Visual Studio 15 (2017) e successive](#Compilazione_con_Visual_Studio_15_(2017)_e_successive.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                          dipende
  BUILD_DESIGNER_PLUGIN               Per creare il plug-in Qt Designer, consultare [questa sezione di seguito](#Plugin_di_Qt_Designer.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             OFF
  BUILD_FLAT_MESH                     Necessaria per avere una build che includa la [funzionalità CreateFlatMesh](MeshPart_CreateFlatMesh/it.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       OFF
  CMAKE_INSTALL_PREFIX                La cartella di output durante la creazione della destinazione *INSTALL*, vedere anche la sezione [Esecuzione e installazione di FreeCAD](#Esecuzione_e_installazione_di_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Cartella d\'installazione predefinita del programma in Windows
  FREECAD_COPY_DEPEND_DIRS_TO_BUILD   Copia le librerie dipendenti necessarie per eseguire FreeCAD.exe nella cartella di compilazione. Vedere anche la sezione [Esecuzione e installazione di FreeCAD](#Esecuzione_e_installazione_di_FreeCAD.md). **Nota:** le opzioni FREECAD_COPY_XXX appaiono solo se le librerie non sono già state copiate. Se si ha solo bisogno di aggiornare/passare a un\'altra versione di LibPack, consultare la sezione [Aggiornamento del LibPack](#Aggiornamento_del_Libpack.md). Se si desidera ripristinare le opzioni per qualche motivo, si devono eliminare tutte le cartelle nella cartella di compilazione, ad eccezione della cartella LibPack. In CMake cancellare la cache e avviare come se si dovesse compilare per la prima volta.   OFF
  FREECAD_COPY_LIBPACK_BIN_TO_BUILD   Copia i file binari LibPack necessari per eseguire FreeCAD.exe nella cartella di compilazione. Vedere anche la sezione [Esecuzione e installazione di FreeCAD](#Esecuzione_e_installazione_di_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       OFF
  FREECAD_COPY_PLUGINS_BIN_TO_BUILD   Copia i file del plugin di Qt necessari per eseguire FreeCAD.exe nella cartella di compilazione. Vedere anche la sezione [Esecuzione e installazione di FreeCAD](#Esecuzione_e_installazione_di_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     OFF
  FREECAD_LIBPACK_USE                 Attiva o disattiva l\'utilizzo di FreeCAD LibPack.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ON
  FREECAD_LIBPACK_DIR                 Directory in cui si trova il LibPack.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Cartella del codice sorgente di FreeCAD
  FREECAD_RELEASE_PDB                 Crea librerie di debug (\*.pdb) anche per build di rilascio. Non influisce sulla velocità (come farebbe una vera build di debug) e può essere molto utile per individuare arresti anomali nel codice di FreeCAD. Nel caso in cui FreeCAD si arresti in modo anomalo, verrà creato un file *crash.dmp* che può essere caricato con MSVC e se si dispone dei file PDB corrispondenti più il codice sorgente di quella versione è possibile eseguire il debug attraverso il codice. Senza i file PDB non è possibile eseguire il debug del codice e tutto ciò che il debugger mostra è il nome della DLL in cui si è verificato il crash.                                                                                                                                   ON
  FREECAD_USE_MP_COMPILE_FLAG         Aggiunge l\'opzione /MP (multiprocessore) ai progetti di Visual Studio, abilitando accelerazioni nelle CPU multi-core. Questo può accelerare notevolmente le build sui processori moderni.**Nota:** Se disattivi **FREECAD_USE_PCH**, la compilazione può sovraccaricare rapidamente lo spazio dell\'heap, anche se hai 16 GB di RAM.                                                                                                                                                                                                                                                                                                                                                                                                                      ON
  FREECAD_USE_PCH                     [Precompila the headers](https://en.wikipedia.org/wiki/Precompiled_header) per risparmiare tempo di compilazione.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ON
  FREECAD_USE_PYBIND11                Include la libreria [PyBind11](https://github.com/pybind/pybind11). Necessario avere una build che includa la [funzionalità CreateFlatMesh](MeshPart_CreateFlatMesh/it.md).**Nota:** dopo averla attivata si potrebbe ricevere un errore di configurazione. Basta configurare di nuovo e il problema dovrebbe scomparire.                                                                                                                                                                                                                                                                                                                                                                                                                          OFF



## Compilare FreeCAD 

A seconda del compilatore, il processo per la compilazione di FreeCAD sarà leggermente diverso. Nelle sezioni seguenti sono descritti i flussi di lavoro noti. Se stai costruendo con Qt Creator, passa a [Compilazione con Qt Creator (obsoleto)](#Compilazione_con_Qt_Creator_(obsoleto).md), altrimenti procedi direttamente:


<div class="mw-collapsible mw-collapsed toccolours">



### Compilazione con Visual Studio 15 (2017) e successive 


<div class="mw-collapsible-content">



#### Rilascio della Build 

1.  Avviare l\'IDE di Visual Studio. Questo si può fare cliccando sul pulsante *Apri progetto* nella GUI di CMake o facendo doppio clic sul file *FreeCAD.sln*, che si trova nella cartella di compilazione.
2.  Nella barra degli strumenti dell\'IDE MSVC assicurarsi di utilizzare per la prima compilazione *Release*.
3.  C\'è una finestra chiamata *Solution Explorer*. Elenca tutti i possibili target di compilazione. Per avviare una compilazione completa, fare clic con il pulsante destro del mouse sul target **ALL_BUILD** e quindi scegliere **Build**.

Ci vorrà molto tempo.

Per compilare un FreeCAD pronto all\'uso, compila la destinazione *INSTALLA*, vedere la sezione [Esecuzione e installazione di FreeCAD](#Esecuzione_e_installazione_di_FreeCAD.md).

Se non ricevi errori, hai finito. **Congratulazioni!** Puoi uscire da MSVC o tenerlo aperto.

**Importante:** A partire da Visual Studio 17.4 non è possibile utilizzare l\'ottimizzazione del codice attiva per impostazione predefinita per il target **SketcherGui**. In tal caso, i vincoli angolari verranno posizionati in modo errato negli schizzi. Per risolvere questo problema, fare clic con il pulsante destro del mouse su questo target in Esplora soluzioni MSVC e selezionare l\'ultima voce **Proprietà** nel menu contestuale. Nella finestra di dialogo che appare andare su C/C++ → Ottimizzazione e disabilitare l\'impostazione **Ottimizzazione**. Infine costruire di nuovo il target **ALL_BUILD**.



#### Compilazione di Debug 

Per una compilazione di debug è necessario utilizzare Python incluso nel LibPack. Per verificarlo:

1.  Cercare \"Python\" nella GUI di CMake
2.  Se si nota un percorso come *C:/Program Files/Python38/python.exe*, significa che CMake ha riconosciuto il Python, che è installato sul tuo PC, e non quello del LibPack. In questo caso adattare queste diverse impostazioni Python in CMake alle seguenti (assumendo che il LibPack si trovi nella cartella *D:\\FreeCAD-build\\FreeCADLibs_12.5.2_x64_VC17*): ![](images/CMake_Python_settings.png )

Come prerequisito per la build di debug, devi fare questo:

1.  Copiare il contenuto della cartella LibPack *bind* nella cartella *bin* della cartella build di FreeCAD (sovrascrivere i file esistenti).
2.  Copiare il contenuto della cartella LibPack *libd* nella cartella *lib* della cartella build di FreeCAD.

Adesso puoi compilare:

1.  Avviare l\'IDE di Visual Studio. Questo può essere fatto premendo il pulsante *Apri progetto* nella GUI di CMake o facendo doppio clic sul file *FreeCAD.sln*, che si trova nella cartella di build.
2.  Nella barra degli strumenti dell\'IDE MSVC assicurarsi di utilizzare per la prima compilazione *Debug*.
3.  C\'è una finestra chiamata *Solution Explorer*. Elenca tutti i possibili obiettivi di compilazione. Per avviare una compilazione completa, fare clic con il pulsante destro del mouse sul target **ALL_BUILD** e scegliere **Build** nel menu contestuale.

Richiederà molto tempo.

Se non ci sono stati errori di compilazione e se le opzioni **FREECAD_COPY\_\*** menzionate nella [Fase di configurazione di CMake](#CMake.md) sopra sono state abilitate, si può avviare la build di debug:

1.  Fare clic con il pulsante destro del mouse sull\'obiettivo **FreeCADMain** e scegliere **Set as Startup Project** nel menu contestuale.
2.  Infine fare clic sulla barra degli strumenti sul pulsante con il triangolo verde indicato **Local Windows Debugger**.

Questo avvierà la build di debug di FreeCAD ed è possibile utilizzare l\'IDE MSVC per eseguirne il debug.

#### Risorse video 

Un tutorial in lingua inglese che inizia con la configurazione in CMake Gui e continua con il comando \Build\ in Visual Studio 16 2019 è disponibile unlisted su YouTube all\'indirizzo [Tutorial: Build FreeCAD from source on Windows 10](https://youtu.be/s4pHvlDOSZQ) .


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Compilazione con Qt Creator (obsoleto) 


<div class="mw-collapsible-content">



#### Installazione e configurazione di Qt Creator 

-   Scaricare e installare [Qt Creator](https://www.qt.io/offline-installers)
-   Strumenti → Opzioni → Editor di testo → scheda Comportamento:
    -   Codifica dei file → Codifiche predefinite:
    -   Impostato su: **ISO-8859-1 /\...csISOLatin1** (Alcuni caratteri creano errori / avvertimenti con Qt Creator se lasciato impostato su UTF-8. Questo sembra risolverlo.)
-   Strumenti → Opzioni → Crea ed esegui:
    -   Scheda CMake
        -   Riempire la casella Eseguibile con il percorso di cmake.exe
    -   Scheda Kit
        -   Nome: MSVC 2008
        -   Compilatore: Microsoft Visual C++ Compiler 9.0 (x86)
        -   Debugger: rilevato automaticamente \...
        -   Versione Qt: Nessuna
    -   Scheda Generale
        -   Deselezionare: crea sempre un progetto prima di distribuirlo
        -   Deselezionare: distribuire sempre il progetto prima di eseguirlo



#### Importare e creare il progetto 

-   File → Apri file o progetto
-   Aprire **CMakeLists.txt** che si trova nel livello più alto della fonte
-   Questo avvierà CMake
-   Scegliere la cartella di costruzione e fare clic su Avanti
-   Impostare il generatore su **NMake Generator (MSVC 2008)**
-   Cliccare Esegui CMake. Seguire le istruzioni illustrate sopra per configurare CMake a tuo piacimento.

Ora è possibile creare FreeCAD

-   Build → Build All
-   Ci vorrà molto tempo \...

Una volta completato, può essere eseguito: Ci sono 2 triangoli verdi in basso a sinistra. Uno è il debug. L\'altro è l\'eseguibile. Scegliere quello che si desidera.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Compilazione dalla riga di comando 


<div class="mw-collapsible-content">

I passaggi su come compilare dalla riga di comando dipendono dal compilatore. Per MSVC 2017 i passaggi sono:

1.  Nel menu Start di Windows andare a **Visual Studio 2017 → Visual Studio Tools** e scegliere **Prompt dei comandi per sviluppatori per VS 2017**
2.  Passare alla tua cartella di build.
3.  Eseguire il comando


```pythonmsbuild ALL_BUILD.vcxproj /p:Configuration=Release```

o


```pythonmsbuild INSTALL.vcxproj /p:Configuration=Release```

Questi passaggi possono anche essere automatizzati. Ecco ad esempio una soluzione per MSVC 2017:

1.  Scaricare lo script [compile-FC.txt](https://forum.freecadweb.org/download/file.php?id=92135).
2.  Rinominarlo in *compile-FC.bat*
3.  In Esplora file di Windows fare Shift + Click con il tasto destro del mouse sulla cartella di build e utilizzare dal menu di scelta rapida \"Command prompt here\".
4.  Eseguire il comando


```pythoncompile-FC install```

Invece di chiamare **compile-FC** con l\'opzione *install* si può anche usare *debug* o *release*:

*debug*   - compila FreeCAD nella configurazione di debug

*release* - compila FreeCAD nella configurazione della versione

*install*    - compila FreeCAD nella configurazione di rilascio e crea una versione d\'installazione


</div>


</div>



## Esecuzione e installazione di FreeCAD 

Esistono 2 metodi per eseguire FreeCAD compilato:

*Metodo 1*: Eseguire FreeCAD.exe che si trova nella cartella di compilazione nella sottocartella *bin*

*Metodo 2*: compilare il target *INSTALL*

Il metodo 2 è quello più semplice, perché assicura automaticamente che tutte le librerie necessarie per eseguire FreeCAD.exe siano nella cartella corretta. FreeCAD.exe e le librerie verranno emessi nella cartella specificata nella variabile CMake *CMAKE_INSTALL_PREFIX*.

Per il Metodo 1 devi abilitare le opzioni **FREECAD_COPY\_\*** menzionate nella [Fase di configurazione di CMake](#CMake.md) sopra.



### Risoluzione dei problemi 

Durante l\'esecuzione di FreeCAD è possibile riscontrare DLL mancanti quando si utilizzano determinati ambienti di lavoro o funzionalità di ambienti di lavoro. Il messaggio di errore nella console di FreeCAD non ti dirà quale DLL manca. Per scoprirlo è necessario utilizzare uno strumento esterno:

-   Scaricare l\'ultima versione del programma **Dependencies**: <https://github.com/lucasg/Dependencies/releases> (scegliere il file *Dependencies_x64_Release.zip*)
-   Nella [console Python](console_Python.md) di FreeCAD eseguire questi comandi:

import os
os.system(r"~\DependenciesGui.exe")

**Nota**: invece di \~ si deve specificare il percorso completo di *DependenciesGui.exe* sul tuo sistema.

-   Ora trascinare il file \*.pyd del workbench con il quale si ottengono le DLL mancanti segnalate.



## Aggiornamento della compilazione 

FreeCAD è sviluppato molto attivamente. Pertanto il suo codice sorgente cambia quasi quotidianamente. Nuove funzionalità vengono aggiunte e i bug corretti. Per beneficiare di queste modifiche al codice sorgente, è necessario ricompilare FreeCAD. Questo avviene in due fasi:

1.  Aggiornamento del codice sorgente
2.  Ricompilazione



### Aggiornamento del codice sorgente 



#### Usando un frontend 

Quando si utilizza il [frontend di Git](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit:

1.  Fare clic con il tasto destro del mouse sulla cartella del codice sorgente di FreeCAD in Esplora file di Windows e selezionare nel menu di scelta rapida *\'Pull\'*.
2.  Apparirà una finestra di dialogo. Selezionare quale ramo di sviluppo vuoi utilizzare. **master** è il ramo principale. Pertanto utilizzare questo a meno che non si desideri compilare una nuova funzionalità speciale da un ramo che non è stato ancora unito a \"master\". (Per ulteriori informazioni sui rami Git, vedere [Processo di sviluppo Git](Source_code_management/it#Processo_di_sviluppo_Git.md)).

Finalmente cliccare su **OK**.



#### Utilizzando la riga di comando 

Aprire un terminale (prompt dei comandi) e passare alla cartella di origine. Quindi digitare:


```python
git pull https://github.com/FreeCAD/FreeCAD.git master
```

dove *master* è il nome del ramo di sviluppo principale. Se si vuole ottenere il codice da un altro ramo, usare il suo nome invece di *master*.



### Ricompilazione

1.  Aprire l\'IDE MSVC facendo doppio clic sul file *FreeCAD.sln* o sul file *ALL_BUILD.vcxproj* nella cartella di compilazione.
2.  Continuare con il passaggio 2 dalla sezione [Compilazione con Visual Studio 15 (2017) e successive](#Compilazione_con_Visual_Studio_15_(2017)_e_successive.md).



## Aggiornamento del Libpack 

Se viene rilasciata una nuova versione principale di una dipendenza di terze parti come Open Cascade o se una dipendenza di terze parti ha importanti correzioni di bug, viene rilasciato un nuovo LibPack. Si può trovare l\'ultima versione [qui](https://github.com/FreeCAD/FreeCAD-LibPack/releases/).

Per aggiornare il tuo LibPack, la seguente procedura è la pratica migliore:

1.  Eliminare la cartella *bin* nella tua cartella di compilazione.
2.  Passare alla tua cartella LibPack locale ed eliminare tutto il contenuto.
3.  Estrarre il contenuto del nuovo file ZIP LibPack nella cartella LibPack locale esistente, che ora è vuota.
4.  Aprire CMake e premere il pulsante **Configure** e poi il pulsante **Generate**. Questo ricrea la cartella *bin* appena eliminata e vi copia anche i nuovi file LibPack.
5.  In CMake fare clic sul pulsante **Open Project** e si aprirà l\'IDE MSVC.
6.  Nell\'IDE MSVC creare la destinazione *INSTALL*.



## Strumenti

Per partecipare allo sviluppo di FreeCAD è necessario compilare e installare i seguenti strumenti:



### Plugin di Qt Designer 

FreeCAD usa [Qt](https://en.wikipedia.org/wiki/Qt_(software)) come toolkit per la sua interfaccia utente. Tutte le finestre di dialogo sono impostate in file UI che possono essere modificati utilizzando il programma [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html) che fa parte di qualsiasi installazione di Qt ed è anche incluso nel LibPack. FreeCAD ha il proprio set di widget Qt per fornire funzionalità speciali come l\'aggiunta di un\'unità ai campi di input e per impostare le proprietà delle preferenze.



#### Compilazione

Il plugin non può essere caricato da Qt Designer se è stato compilato utilizzando una versione di Qt diversa da quella su cui si basa Qt Designer/Qt Creator. Pertanto il plugin deve essere compilato insieme a FreeCAD:

-   Nelle opzioni di CMake (vedere [questa sezione sopra](#Opzioni_per_il_processo_di_compilazione.md)) abilitare l\'opzione BUILD_DESIGNER_PLUGIN e riconfigurare.
-   aprire MSVC e creare il target **FreeCAD_widgets**

Come risultato si otterrà il file del plugin *\'FreeCAD_widgets.dll* nella cartella*\~\\src\\Tools\\plugins\\widget\\Release*



#### Installazione

Per installare il plugin, copia la DLL in

-   Se si usa il LibPack: nella cartella*\~\\FreeCADLibs_2\_8_x64_VC2019\\plugins\\designer*
-   Se si ha un\'installazione Qt completa: si può scegliere tra la cartella*C:\\Qt\\5.15.2\\msvc2019_64\\plugins\\designer*o*C: \\Qt\\5.15.2\\msvc2019_64\\bin\\designer* (si deve prima creare la sottocartella *designer*.)(adattare i percorsi alla propria installazione!).

Infine (ri)avviare Qt Designer e controllare il suo menu **Help → Plugins**. Se il plugin **FreeCAD_widgets.dll** è elencato come caricato, ora si può progettare e modificare i file .ui di FreeCAD. In caso contrario, si deve [compilare](#Compilare_FreeCAD.md) la DLL da se.

Se si preferisce usare [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator) invece di Qt Designer, il file del plugin deve essere posizionato in questa cartella:*C:\\Qt\\Qt5.15.2 \\Tools\\QtCreator\\bin\\plugins\\designer*Quindi (ri)avviare Qt Creator, passare alla modalità **Design** e controllare il menu **Tools → Form Editor → About Qt Designer Plugins**. Se il plugin **FreeCAD_widgets.dll** è elencato tra quelli caricati, si può progettare e modificare i file .ui di FreeCAD. In caso contrario, ci si deve [compilare](#Compilare_FreeCAD.md) la DLL.



### Creatore di miniature 

FreeCAD ha la funzionalità per fornire miniature di anteprima per i file \*.FCStd. Ciò significa, che nel file explorer di Windows i file \*.FCStd, sono mostrati con uno screenshot del modello che contiene. Per fornire questa funzionalità, FreeCAD deve avere il file **FCStdThumbnail.dll** installato in Windows.



#### Installazione 

La DLL viene installata in questo modo:

1.  Scaricare [questo file ZIP](https://forum.freecadweb.org/download/file.php?id=13404) ed estrarlo.
2.  Aprire un prompt dei comandi di Windows con privilegi di amministratore (questi privilegi sono un requisito).
3.  Passare alla cartella in cui si trova la DLL.
4.  Eseguire questo comando 
```pythonregsvr32 FCStdThumbnail.dll```

Quindi controllare se funziona, assicurarsi che in FreeCAD l\'opzione delle preferenze **[Salva la miniatura nel file di progetto al salvataggio del documento](Preferences_Editor/it#Documento.md)** sia abilitata e salvare il modello. Quindi visualizzare in Windows Explorer la cartella del modello salvato utilizzando una vista simboli. Ora si dovrebbe vedere uno screenshot del modello nella vista delle cartelle.



#### Compilazione 

Per compilare FCStdThumbnail.dll

1.  Passare alla cartella sorgente di FreeCAD*\~\\src\\Tools\\thumbs\\ThumbnailProvider*
2.  Aprire la GUI di CMake
3.  Specificare come cartella di origine quella in cui ci si trova attualmente.
4.  Usare la stessa cartella della cartella build.
5.  Fare clic su **Configure**
6.  Nella finestra di dialogo che appare, specificare il generatore in base a quello che si vuole usare. Per lo standard MS Visual Studio utilizzare *Visual Studio xx 2yyy* dove xx è la versione del compilatore e 2yyy l\'anno del suo rilascio. Si consiglia di utilizzare l\'opzione predefinita *Use default native compilers*.**Nota:** È importante specificare la variante col numero di bit corretta. Se si ha la variante a 64 bit di LibPack si deve usare anche il compilatore x64.
7.  Cliccare su **Generate**.
8.  Ora si dovrebbe avere il file **ALL_BUILD.vcxproj** nella cartella *\~\\src\\Tools\\thumbs\\ThumbnailProvider*. Fare doppio clic su di esso e si aprirà l\'IDE MSVC.
9.  Nella barra degli strumenti dell\'IDE MSVC assicurarsi di utilizzare l\'obiettivo di compilazione *Release*.
10. C\'è una finestra chiamata *Solution Explorer*. Fare clic destro su **ALL_BUILD** e poi sceglire **Build**.
11. Come risultato ora si dovrebbe avere un **FCStdThumbnail.dll** nella cartella *\~\\src\\Tools\\thumbs\\ThumbnailProvider\\release*, che si può installare come descritto sopra.



## Compilazione di Open Cascade 

Il LibPack viene fornito con una versione di [Open Cascade](https://en.wikipedia.org/wiki/Open_Cascade) adatta all\'uso generale. Tuttavia, in alcune circostanze potresti voler compilare con una versione alternativa di Open Cascade, come ad esempio una delle loro versioni ufficiali o un fork con patch.

Durante la compilazione di Open Cascade per FreeCAD, si tenga presente che non vi è alcuna garanzia che FreeCAD funzioni con tutte le versioni di Open Cascade. Si noti inoltre che quando si utilizza la libreria Netgen, è necessario utilizzare una versione NetGen approvata per la compilazione con la versione Open Cascade che si desidera compilare.

Compilare:

-   Per prima cosa si deve ottienere il codice sorgente di Open Cascade, direttamente dal [repository git di Open Cascade](https://github.com/Open-Cascade-SAS/OCCT) o clonando il fork di qualcun altro, come ad esempio il [fork \"blobfish\"](https://gitlab.com/blobfish/occt) gestito dal membro del forum di FreeCAD [tanderson69](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=208).

-   Quindi aprire la GUI di CMake per configurare il sistema di compilazione in modo simile alla creazione di FreeCAD. Queste opzioni di CMake devono essere impostate (o esplicitamente non impostate):

  Nome Variabile                     Descrizione                                                                                                                                                                                                                                                                                                                                      Valore di Default
    
  3RDPARTY_DIR                       Percorso verso i componenti di terze parti. Si consiglia di utilizzare la cartella come input in cui si trova il LibPack utilizzato. Lasciare esplicitamente vuoto questo campo.                                                                                                                                                                 vuoto
  3RDPARTY_DOXYGEN_EXECUTABLE        Percorso dell\'eseguibile del componente di terze parti [Doxygen](https://en.wikipedia.org/wiki/Doxygen). Si consiglia di installare Doxygen. Così CMake lo troverà automaticamente.                                                                                                                                                             vuoto
  3RDPARTY_FREETYPE_DIR              Percorso del componente di terze parti necessario [Freetype](https://en.wikipedia.org/wiki/FreeType). Si consiglia di utilizzare la cartella come input in cui si trova il LibPack utilizzato.                                                                                                                                                   vuoto
  3RDPARTY_RAPIDJSON_DIR             Disponibile solo se viene utilizzato **USE_RAPIDJSON**. Percorso del componente di terze parti [RapidJSON](https://rapidjson.org/). Si consiglia di NON utilizzare una cartella LibPack esistente come input. Si può usare la cartella RapidJSOn da un LibPack, ma copiata in una nuova cartella e poi usare questa nuova cartella come input.   vuoto
  3RDPARTY_TCL_DIR                   Percorso al componente di terze parti necessario [TCL](https://it.wikipedia.org/wiki/Tcl). Si consiglia di NON utilizzare una cartella LibPack esistente come input. Prendere ad esempio una di [queste versioni](https://github.com/teclab-at/tcltk/releases), estrarla e prenderla come cartella di input per CMake.                           vuoto
  3RDPARTY_TK_DIR                    Percorso del componente di terze parti necessario [TK](https://en.wikipedia.org/wiki/Tk_(software)). Si consiglia di NON utilizzare una cartella LibPack esistente come input. Prendere ad esempio una di [queste versioni](https://github.com/teclab-at/tcltk/releases), estrarla e prenderla come cartella di input per CMake.                 vuoto
  3RDPARTY_VTK_DIR                   Disponibile solo se viene utilizzato **USE_VTK**. Percorso del componente di terze parti necessario [VTK](https://en.wikipedia.org/wiki/VTK). Si consiglia di utilizzare la cartella come input in cui si trova il LibPack utilizzato. Se si utilizza un\'altra cartella, assicurarsi di non utilizzare VTK 9.x o versioni successive.           vuoto
  BUILD_RELEASE_DISABLE_EXCEPTIONS   Disabilita la gestione delle eccezioni per le build di rilascio. Per FreeCAD si deve impostarlo su **OFF**.                                                                                                                                                                                                                                      ON
  INSTALL_DIR                        Cartella di output durante la creazione della destinazione *INSTALL*. Se la compilazione è andata a buon fine, prendere i file da questa cartella per aggiornare il tuo LibPack.                                                                                                                                                                 Cartella d\'installazione predefinita del programma in Windows
  INSTALL_DIR_BIN                    Sottocartella di output per la DLL durante la creazione del target *INSTALL*. Si deve cambiarlo in **bin**.                                                                                                                                                                                                                                      win64/vc14/bin
  INSTALL_DIR_LIB                    Sottocartella di output per i file .lib durante la creazione della destinazione *INSTALL*. Si deve cambiarlo in **lib**.                                                                                                                                                                                                                         win64/vc14/lib
  USE_RAPIDJSON                      Per compilare Open Cascade con supporto per RapidJSON. L\'abilitazione è obbligatoria per ottenere supporto per il formato file [glTF](https://en.wikipedia.org/wiki/Gltf).                                                                                                                                                                      OFF
  USE_VTK                            Per compilare Open Cascade con supporto per VTK. Abilitare questo è ottimale. Si può usarlo per costruire il bridge VTK di Open Cascade.                                                                                                                                                                                                         OFF

-   Aprire il progetto in Visual Studio e per prima cosa creare i target ALL_BUILD e poi INSTALL in modalità **Release**.
-   Ripetere la creazione dei due target nella modalità **Debug**.

Per creare FreeCAD, utilizzando Open Cascade autocompilato, è necessario eseguire le seguenti operazioni:

-   Copiare tutte le cartelle da INSTALL_DIR nella tua cartella LibPack (sovrascrivere i file esistenti)
-   Passare alla cartella LibPack e andare lì alla sottocartella *cmake*
-   Aprire il file *OpenCASCADEDrawTargets.cmake* con un editor di testo
-   Cercare i percorsi assoluti della tua cartella LibPack e rimuoverli. Quindi ad es. il percorso assoluto*D:/FreeCADLibs_12.5.4_x64_VC17/lib/freetype.lib*diventerà solo *freetype.lib*
-   Fare lo stesso per il file *OpenCASCADEVisualizationTargets.cmake*



## Compilazione di Netgen 

Il LibPack viene fornito con una versione di [Netgen](https://ngsolve.org) che sarà stata testata per essere compilata con la versione Open Cascade del LibPack. Il problema è che ogni nuova versione di Netgen cambia l\'API. Anche ogni nuova versione di Open Cascade fa lo stesso. Pertanto non si può semplicemente cambiare in modo semplice la versione di Netgen.

Tuttavia, potresti comunque compliare Netgen. Questa è un\'attività semplice:

-   Per prima cosa scaricare il codice sorgente di Netgen, direttamente dal repository git di [Netgen](https://github.com/NGSolve/netgen).
-   Quindi aprire la GUI di CMake, per configurare il sistema di compilazione in modo simile alla creazione di FreeCAD. Devono essere impostate le seguenti opzioni di CMake :

  Nome Variabile         Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Valore di Default
    
  CMAKE_INSTALL_PREFIX   Cartella di output durante la creazione della destinazione *INSTALL*. Se la compilazione è andata a buon fine, prendere i file da questa cartella per aggiornare il tuo LibPack.                                                                                                                                                                                                                                                                                                                                                                                         C:/netgen
  OpenCasCade_DIR        Percorso dei file CMake di Open Cascade. Se si è compilato Open Cascade come descritto nella sezione [Compilazione di Open Cascade](#Compilazione_di_Open_Cascade.md) si può usare la sottocartella *cmake* della cartella usata come INSTALL_DIR. In caso contrario, usare la sottocartella *cmake* del tuo LibPack. Si noti che il LibPack deve già contenere una corretta build Open Cascade. Indipendentemente dalla cartella utilizzata, si deve creare anche una sottocartella *lib* e copiarvi i file *freetype.lib* e *freetyped.lib* dal tuo LibPack.   vuoto
  USE_GUI                Impostarlo a **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ON
  USE_NATIVE_ARCH        Impostarlo su **OFF**; questo è necessario solo per supportare le CPU più vecchie che non hanno il set di istruzioni [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions).                                                                                                                                                                                                                                                                                                                                                                                   ON
  USE_OCC                Impostarlo a **ON**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      OFF
  USE_PYTHON             Impostarlo a **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ON
  USE_SUPERBUILD         Impostarlo a **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ON
  ZLIB_INCLUDE_DIR       Percorso del componente di terze parti necessario [zlib](https://en.wikipedia.org/wiki/Zlib). Si consiglia di utilizzare la cartella come input in cui si trova il LibPack utilizzato.                                                                                                                                                                                                                                                                                                                                                                                   vuoto
  ZLIB_LIBRARY_DEBUG     Percorso del file ZLib *zlibd.lib*. Si trova nella sottocartella *lib* della cartella LibPack.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           vuoto
  ZLIB_LIBRARY_RELEASE   Il percorso del file ZLib *zlib.lib*. Si trova nella sottocartella *lib* della cartella LibPack.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         vuoto

-   Inoltre è necessario aggiungere una nuova voce CMake:

nome: *CMAKE_DEBUG_POSTFIX*, tipo: *stringa*, contenuto: **\_d** Ciò garantisce che i nomi dei file delle librerie di debug abbiano un nome diverso rispetto alle librerie di rilascio e non possano essere successivamente scambiati accidentalmente.

-   Premere il pulsante *Configura* in CMake per generare i file \*.cmake.
-   Necessario solo se devono essere supportate CPU precedenti che non dispongono del set di istruzioni AVX2:
    -   Cercare nella tua cartella di build Netgen il file *netgen-targets.cmake* e aprirlo con un editor di testo. Rimuovere l\'impostazione *;/arch:AVX2* nell\'opzione INTERFACE_COMPILE_OPTIONS.
    -   Premere di nuovo il pulsante \"Configure\" in CMake.
-   Premere il pulsante \"Generate\" in CMake.
-   Aprire il progetto in Visual Studio e creare prima i target ALL_BUILD e poi INSTALL in modalità **Release**.
-   Ripetere la creazione dei due obiettivi nella modalità **Debug**.

Per compilare FreeCAD, utilizzando Netgen autocompilato, è necessario eseguire le seguenti operazioni:

-   Copiare tutte le cartelle da CMAKE_INSTALL_PREFIX nella tua cartella LibPack (sovrascrivere i file esistenti)



## Riferimenti

Vedere anche

-   [Velocizzare la compilazione](Compiling_(Speeding_up)/it.md)



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Windows/it
