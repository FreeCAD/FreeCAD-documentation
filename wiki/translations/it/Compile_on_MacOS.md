# Compile on MacOS/it
**Esiste un contenitore Docker FreeCAD sperimentale che viene testato per lo sviluppo di FreeCAD. Ulteriori informazioni su [[Compile on Docker]]**


{{TOCright}}



## Presentazione

Questa pagina descrive come compilare il codice sorgente di FreeCAD su MacOS. Per altre piattaforme, vedere la pagina [Compilare FreeCAD](Compiling/it.md).

Queste istruzioni sono state testate su macOS Catalina con XCode 11.6 standard. È noto che funzioni su macOS BigSur Beta con XCode 12.0 beta. Se si prevede di utilizzare XCode Beta, assicurarsi di scaricare il componente aggiuntivo degli strumenti della riga di comando tramite un pacchetto dmg, per risolvere alcuni problemi di dipendenza libz.

Questa pagina funge da punto di partenza rapido e non intende essere esaustiva per quanto riguarda la descrizione di tutte le opzioni di build disponibili.

Se si vuole solo valutare l\'ultima build pre-rilascio di FreeCAD, si possono scaricare i binari pre-compilati [da qui](https://github.com/FreeCAD/FreeCAD/releases).



## Installare i prerequisiti 

Il seguente software deve essere installato per supportare il processo di compilazione.

### Homebrew Package Manager 

Homebrew è un gestore di pacchetti basato sulla riga di comando per macOS. La [Homebrew main page](https://brew.sh/) fornisce una riga di comando per l\'installazione, che si deve semplicemente incollare in una finestra di terminale.

### CMake

CMake è uno strumento di compilazione che genera una configurazione di compilazione basata sulle variabili specificate. Quindi si esegue il comando \'make\' per creare effettivamente quella configurazione. La versione da riga di comando di CMake viene installata automaticamente come parte dell\'installazione Homebrew di cui sopra. Se si preferisce utilizzare una versione GUI di CMake, la si può scaricare da [qui](https://www.cmake.org/downloadDownload).



## Installare le dipendenze 

FreeCAD mantiene una \"cask\" Homebrew, che installa le formule e le dipendenze richieste. Immettere i seguenti comandi brew nel terminale.


```python
brew tap freecad/freecad
brew install eigen
brew install --only-dependencies freecad
```


{{Incode|brew install}}

potrebbe richiedere un po\' di tempo, quindi si può andare a prendere qualcosa da bere. :-).

In alternativa, si possono installare manualmente le singole dipendenze, installando i seguenti pacchetti, utilizzando {{Incode|brew install ...}}:

-    `cmake`
    

-    `swig`
    

-    `boost`
    

-    `boost-python3`
    

-    `eigen`
    

-    `gts`
    

-    `vtk`
    

-    `xerces-c`
    

-    `qt@5`\- Attualmente è supportato solo Qt5, il supporto per Qt6 è un work-in-progress

-    `opencascade`
    

-    `doxygen`
    

-    `pkgconfig`
    

-    `coin3d`\- Si noti che al momento della stesura di questo documento (novembre 2022) verrà installata una versione inutilizzabile di pyside@2 come dipendenza.

Ci sono diversi pacchetti che sono disponibili solo dopo aver toccato la cask di freecad: si deve fare (`brew tap freecad/freecad`). A causa di alcune soluzioni alternative a bug storici, al momento della stesura di questo articolo (novembre 2022) le versioni di PySide2 e Shiboken2 installate da Homebrew non sono utilizzabili, perché impongono l\'uso di Py_Limited_API, che FreeCAD non supporta. Si prevede che questa soluzione alternativa verrà rimossa nei prossimi mesi, ma nel frattempo è necessario utilizzare le versioni cask di FreeCAD di PySide e Shiboken. Usare `brew install ...`, installare i seguenti pacchetti:

-    `freecad/freecad/pyside2@5.15.5`
    

-    `freecad/freecad/shiboken2@5.15.5`
    

-    `freecad/freecad/med-file`
    

-    `freecad/freecad/netgen`
    

Si dovranno anche \"collegare\" PySide e Shiboken:


```python
brew link freecad/freecad/pyside2@5.15.5 freecad/freecad/shiboken2@5.15.5
```

In alcuni casi i pacchetti installati da Homebrew non utilizzano la stessa versione di Python: ad esempio, al momento in cui scriviamo PySide2 utilizza Python 3.10, ma boost-python3 utilizza Python 3.11. Sebbene sia possibile \"ripristinare\" la versione più avanzata (quindi in questo caso boost-python3 utilizza Python 3.10) si tratta di un\'operazione avanzata e in molti casi è meglio attendere un aggiornamento dell\'altro pacchetto. Se si vuole comunque seguire quel percorso, guardare il comando \"brew extract\", che si può usare per estrarre una formula in una nuova cask (tipicamente freecad/freecad). È quindi possibile modificare tale formula secondo necessità.

Si dovrà impostare il percorso su Qt: Qt5 è attualmente supportato, mentre il supporto per Qt6 è un work-in-progress. Impostare FREECAD_QT_VERSION su \"Auto\" o \"5\" per selezionare Qt5 (impostazione predefinita). Sulla riga di comando, usare qualcosa come:


```python
cmake \
  -DCMAKE_BUILD_TYPE="Release" \
  -DPYTHON_EXECUTABLE="/usr/local/bin/python3" \
  -DQt5_DIR="/usr/local/Cellar/qt@5/5.15.7/lib/cmake/Qt5" \
  -DPySide2_DIR="/usr/local/Cellar/pyside2@5.15.5/5.15.5/lib/cmake/PySide2-5.15.5" \
  -DShiboken2_DIR="/usr/local/Cellar/shiboken2@5.15.5/5.15.5_1/lib/cmake/Shiboken2-5.15.5" \
  ../freecad-source
```



## Ottenere il codice sorgente 

Nelle seguenti istruzioni, le cartelle di origine e di build vengono create fianco a fianco in


```python
/Users/username/FreeCAD
```

ma si può usare qualsiasi cartella si desideri.


```python
mkdir ~/FreeCAD
cd ~/FreeCAD
```

Il seguente comando clonerà il repository git di FreeCAD in una directory chiamata FreeCAD-git.


```python
git clone https://github.com/FreeCAD/FreeCAD FreeCAD-git
```

Creare la cartella di compilazione.


```python
mkdir ~/FreeCAD/build
```



## Eseguire CMake 

Successivamente, si eseguirà CMake per generare la configurazione della build. Devono essere passate a CMake diverse opzioni. La tabella seguente descrive queste opzioni e fornisce alcuni retroscena.



### Opzioni di CMake 

  Name                       Value                                    Notes
    
  CMAKE_BUILD_TYPE           Release (STRING)                         Release o Debug. Il debug viene generalmente utilizzato per i test a livello di sviluppatore, ma può essere richiesto anche per i test e la risoluzione dei problemi a livello di utente.
  CMAKE_PREFIX_PATH          \"/usr/local/opt/qt5152;\" \... (PATH)   Richiesto per compilare con Qt5. Vedere nota sotto. È inoltre necessario aggiungere il percorso alle librerie VTK e al file di configurazione cmake delle librerie NGLIB.
  FREECAD_CREATE_MAC_APP     1 (BOOL)                                 Crea un bundle FreeCAD.app nella posizione specificata in CMAKE_INSTALL_PREFIX, quando viene emesso il comando \'make install\'.
  CMAKE_INSTALL_PREFIX       \"./..\" (PATH)                          Percorso in cui si desidera generare il pacchetto FreeCAD.app.
  FREECAD_USE_EXTERNAL_KDL   1 (BOOL)                                 Richiesto.
  BUILD_FEM_NETGEN           1 (BOOL)                                 Richiesto se si sceglie di compilare gli strumenti FEM.

Note: linea di comando per generare CMAKE_PREFIX_PATH:

ls -d $(brew list -1 | grep qt | tail -1 | xargs brew --cellar)/*/lib/cmake



### GUI per CMake 

Aprire l\'app CMake e compilare i campi della cartella sorgente e di compilazione. In questo esempio, sarebbe **/Users/username/FreeCAD/FreeCAD-git** per l\'origine e **/Users/username/FreeCAD/build** per la cartella di compilazione.

Successivamente, fare clic sul pulsante **Configure** per popolare l\'elenco delle opzioni di configurazione. Verrà visualizzata una finestra di dialogo che chiede di specificare quale generatore utilizzare. Lasciarlo al valore predefinito **Unix Makefiles.** La configurazione fallirà la prima volta, perché ci sono alcune opzioni, che devono essere cambiate. Nota: sarà necessario selezionare la casella **Advanced** per ottenere tutte le opzioni.

Impostare le opzioni dalla tabella sopra, quindi fare nuovamente clic su **Configure** e quindi su **Generate**.



### CMake da riga di comando 

Immettere quanto segue nel terminale.


```python
export PREFIX_PATH="/usr/local/opt/qt5152;\
/usr/local/Cellar/nglib/v6.2.2007/Contents/Resources;\
/usr/local/Cellar/vtk@8.2/8.2.0_1/lib/cmake;"
```


```python
$cd ~/FreeCAD/build
$cmake \
  -DCMAKE_BUILD_TYPE="Release"   \
  -DBUILD_QT5=1                  \
  -DWITH_PYTHON3=1               \
  -DCMAKE_PREFIX_PATH="$PREFIX_PATH" \
  -DPYTHON_EXECUTABLE="/usr/local/bin/python3" \
  -DFREECAD_USE_EXTERNAL_KDL=1   \
  -DCMAKE_CXX_FLAGS='-std=c++14' \
  -DBUILD_FEM_NETGEN=1           \
  -DFREECAD_CREATE_MAC_APP=1     \
  -DCMAKE_INSTALL_PREFIX="./.."  \
  ../FreeCAD-git/

```



## Eseguire make 

Infine, da un terminale eseguire **make** per compilare e collegare FreeCAD e generare l\'app bundle.


```python
cd ~/FreeCAD/build
make -j5 install
```

L\'opzione -j specifica quanti processi make devono essere eseguiti contemporaneamente. Uno più il numero di core della CPU è solitamente un buon numero da utilizzare. Tuttavia, se la compilazione fallisce per qualche motivo, è utile eseguire nuovamente make senza l\'opzione -j, in modo da poter vedere esattamente dove si è verificato l\'errore.

Vedere anche [Velocizzare la compilazione](Compiling_(Speeding_up)/it.md).

Se make termina senza errori, si può avviare FreeCAD facendo doppio clic sull\'eseguibile nel Finder.



## Aggiornare da Github 

Lo sviluppo di FreeCAD avviene velocemente; ogni giorno circa ci sono correzioni di bug o nuove funzionalità. Per ottenere le modifiche più recenti, usare git per aggiornare la directory di origine (vedi [Source code management](Source_code_management.md)), quindi eseguire nuovamente CMake e seguire i passaggi precedenti. Di solito, in questo caso non è necessario iniziare con una directory di build pulita, e le successive compilazioni saranno generalmente molto più veloci della prima.



## Compilare con Qt4 e Python 2.7 

FreeCAD è passato da Qt 4 a Qt 5 così come homebrew. Qt 4 non è più disponibile come opzione per la nuova build su macOS dopo la transizione Qt 5. Python 2.7 è stato deprecato all\'interno dell\'homebrew e del prossimo macOS e non lo supportiamo più nemmeno per la build di macOS.



## Risoluzione dei problemi 



### Segfault all\'avvio di Qt5 

Se Qt4 è stato precedentemente installato tramite brew e quindi si compila con Qt5, è possibile che si verifichi un\'eccezione EXC_BAD_ACCESS (SEGSEGV) all\'avvio della nuova build Qt5. La soluzione per questo è disinstallare manualmente Qt4.


```python
brew uninstall --ignore-dependencies --force cartr/qt4/shiboken@1.2 cartr/qt4/pyside@1.2 cartr/qt4/pyside-tools@1.2 cartr/qt4/qt-legacy-formula
```

### Fortran

*\"No CMAKE_Fortran_COMPILER could be found.\"* durante la configurazione - Le versioni precedenti di FreeCAD richiedono l\'installazione di un compilatore fortran. Con Homebrew, lanciare \"brew install gcc\" e provare a configurare di nuovo, dando a cmake il percorso a Fortran ie -DCMAKE_Fortran_COMPILER=/opt/local/bin/gfortran-mp-4.9 . Oppure, preferibilmente usare una versione più aggiornata del sorgente di FreeCAD!

### FreeType

Quando si utilizzano versioni di CMake precedenti alla 3.1.0, è necessario impostare manualmente la variabile CMake FREETYPE_INCLUDE_DIR_freetype2, ad esempio /usr/local/include/freetype2



### Ulteriori istruzioni per la compilazione 

FreeCAD può essere compilato con l\'ultimo git master ospitato su github e avviato da una CLI utilizzando le librerie fornite dal tap homebrew-freecad. Per un elenco completo delle istruzioni di compilazione, vedere [qui](https://github.com/ipatch/homebrew-us-05/tree/dev/freecad#building-freecad-for-macos-by-macos).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on MacOS/it
