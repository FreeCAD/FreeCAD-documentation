# Compile on Linux/it
{{docnav/it|[Compilazione in Windows](Compile_on_Windows/it.md)|[Compilazione in MacOS](Compile_on_MacOS/it.md)}}


**Esiste un contenitore Docker FreeCAD sperimentale, che viene testato per lo sviluppo di FreeCAD. Leggi di più su [Compilazione con Docker](Compile_on_Docker/it.md)**






## Panoramica

Nelle distribuzioni Linux recenti FreeCAD si compila facilmente, dato che di solito tutte le dipendenze sono fornite dal gestore di pacchetti. Fondamentalmente si tratta di eseguire 3 passaggi:

1.  Ottenere il codice sorgente di FreeCAD
2.  Ottenere le dipendenze (i pacchetti da cui dipende FreeCAD)
3.  Configurare con `cmake` e compilare con `make`

Qui, di seguito, troverete le spiegazioni dettagliate di tutto il processo, delle particolarità che si possono incontrare e alcuni [script di compilazione automatica](#Script_di_compilazione_automatica.md). Se trovate qualcosa di sbagliato o di non aggiornato nel testo successivo (le distribuzioni Linux cambiano spesso), o se utilizzate una distribuzione che non è elencata, discutete il problema nel [forum](https://forum.freecadweb.org/index.php), e aiutateci a correggerlo.

<img alt="" src=images/FreeCAD_source_compilation_workflow.svg  style="width:800px;">



*Flusso di lavoro generale per compilare FreeCAD da sorgente. Le dipendenze di terzi devono essere nel sistema, così come il codice sorgente di FreeCAD. CMake configura il sistema in modo che con una singola istruzione make venga compilato l'intero progetto.*



## Ottenere il codice sorgente 

### Git

Il modo migliore per ottenere il codice è clonare il [repository Git](https://github.com/FreeCAD/FreeCAD). Per questo è necessario il programma `git` che può essere facilmente installato nella maggior parte delle distribuzioni Linux e può anche essere ottenuto dal [sito web ufficiale](http://git-scm.com/).

Git può essere installato tramite il seguente comando:


{{Code|lang=bash|code=
sudo apt install git
}}

Il seguente comando crea una copia locale della versione più recente del codice sorgente di FreeCAD in una nuova directory chiamata `freecad-source`.


{{Code|lang=bash|code=
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git freecad-source
}}

Per ulteriori informazioni sull\'uso di Git e sul contributo del codice al progetto, vedere [Gestione del codice sorgente](Source_code_management/it.md).



### Codice sorgente dall\'archivio 

In alternativa si può scaricare il sorgente dall\' [archivio](https://github.com/FreeCAD/FreeCAD/releases/latest), come file `.zip` o `.tar.gz`, e scompattarlo nella directory desiderata.



## Ottenere le dipendenze 

Per compilare FreeCAD si devono installare le dipendenze necessarie menzionate in [Librerie di terze parti](Third_Party_Libraries/it.md); i pacchetti che contengono queste dipendenze sono elencati di seguito per diverse distribuzioni Linux. Si noti che i nomi e la disponibilità delle librerie dipendono dalla propria particolare distribuzione; se la distribuzione è vecchia, alcuni pacchetti potrebbero non essere disponibili o avere un nome diverso. In questo caso, consultare la sezione [distribuzioni precedenti e non convenzionali](#Distribuzioni_precedenti_e_non_convenzionali.md) sottostante.

Dopo aver installato tutte le dipendenze, procedere con la [compilazione di FreeCAD](#Compilare_FreeCAD.md).

Notare che il codice sorgente di FreeCAD ha una dimensione di circa 500 MB; potrebbe essere tre volte più grande se clonate il repository Git con la sua intera cronologia delle modifiche. Ottenere tutte le dipendenze potrebbe richiedere il download di almeno 500 MB di nuovi file; quando questi file vengono decompressi potrebbero richiedere almeno 1500 MB di spazio. Attenzione anche che il processo di compilazione può generare fino a 1500 MB di file aggiuntivi mentre il sistema copia e modifica l\'intero codice sorgente. Pertanto, assicurarsi di disporre di spazio libero sufficiente sul disco rigido, almeno 4 GB, durante il tentativo di compilazione.


<div class="mw-collapsible mw-collapsed toccolours">



### Debian e Ubuntu 


<div class="mw-collapsible-content">

Sui sistemi basati su Debian (Debian, Ubuntu, Mint, ecc.) è abbastanza facile installare tutte le dipendenze necessarie. La maggior parte delle librerie sono disponibili tramite `apt` o il gestore di pacchetti Synaptic.

Se si ha già installato FreeCAD dai repository ufficiali, si possono installare le sue dipendenze di compilazione con questa singola riga di codice in un terminale:


```python
sudo apt build-dep freecad
```

Tuttavia, se la versione di FreeCAD nei repository è vecchia, le dipendenze potrebbero essere quelle sbagliate per compilare una versione recente di FreeCAD. Pertanto, verificare di aver installato i seguenti pacchetti.

Questi pacchetti sono essenziali per il successo di qualsiasi tipo di compilazione:

-    `build-essential`, installa i compilatori C e C++, le librerie di sviluppo C e il programma `make`.

-    `cmake`, strumento essenziale per configurare il sorgente di FreeCAD. Si potrebbe anche voler installare `cmake-gui` e `cmake-curses-gui` per un\'opzione grafica.

-    `libtool`, strumenti essenziali per produrre librerie condivise.

-    `lsb-release`, l\'utilità standard di reporting di base è normalmente già installata in un sistema Debian e consente di distinguere programmaticamente tra un\'installazione Debian pura o una variante, come Ubuntu o Linux Mint. Non rimuovere questo pacchetto, poiché molti altri pacchetti di sistema potrebbero dipendere da esso.

La compilazione di FreeCAD utilizza il linguaggio Python ed è utilizzato anche in fase di esecuzione come linguaggio di scripting. Se si sta usando una distribuzione basata su Debian, l\'interprete Python è normalmente già installato.

-    `python3`
    

-    `swig`, lo strumento che crea interfacce tra codice C++ e Python.

Verificare di aver installato Python 3. Python 2 è diventato obsoleto nel 2019, quindi il nuovo sviluppo in FreeCAD non viene testato con questa versione del linguaggio.

Le librerie Boost devono essere installate:

-    `libboost-dev`
    

-    `libboost-date-time-dev`
    

-    `libboost-filesystem-dev`
    

-    `libboost-graph-dev`
    

-    `libboost-iostreams-dev`
    

-    `libboost-program-options-dev`
    

-    `libboost-python-dev`
    

-    `libboost-regex-dev`
    

-    `libboost-serialization-dev`
    

-    `libboost-thread-dev`
    

Le librerie di Coin devono essere installate:

-    `libcoin80-dev`, per Debian Jessie, Stretch, Ubuntu da 16.04 a 18.10, oppure

-    `libcoin-dev`, per Debian Buster, Ubuntu 19.04 e successivi, così come per Ubuntu 18.04/18.10 con il [freecad-stable/freecad-daily PPA](Installing_on_Linux/it#Versione_ufficiale.md) aggiunto alle sorgenti software.

Diverse librerie, che si occupano di matematica, superfici triangolate, ordinamento, mesh, visione artificiale, proiezioni cartografiche, visualizzazione 3D, sistema X11 Window, parsing XML e lettura di file Zip:

-    `libeigen3-dev`
    

-    `libgts-bin`
    

-    `libgts-dev`
    

-    `libkdtree++-dev`
    

-    `libmedc-dev`
    

-    `libopencv-dev`or `libcv-dev`

-    `libproj-dev`
    

-    `libvtk7-dev`or `libvtk6-dev`

-    `libx11-dev`
    

-    `libxerces-c-dev`
    

-    `libyaml-cpp-dev`
    

-    `libzipios++-dev`
    


<div class="mw-collapsible mw-collapsed" style="background-color:#e0e0e0">



#### Python 2 e Qt4 

Non è raccomandato per le installazioni più recenti in quanto sia Python 2 che Qt4 sono obsoleti. A partire dalla versione 0.20, FreeCAD non li supporta più.


<div class="mw-collapsible-content">

Per compilare FreeCAD per Debian Jessie, Stretch, Ubuntu 16.04, utilizzando Python 2 e Qt4, installare le seguenti dipendenze.

-    `qt4-dev-tools`
    

-    `libqt4-dev`
    

-    `libqt4-opengl-dev`
    

-    `libqtwebkit-dev`
    

-    `libshiboken-dev`
    

-    `libpyside-dev`
    

-    `pyside-tools`
    

-    `python-dev`
    

-    `python-matplotlib`
    

-    `python-pivy`
    

-    `python-ply`
    

-    `python-pyside`
    


</div>


</div>



### Python 3 e Qt5 

Per compilare FreeCAD per Debian Buster, Ubuntu 19.04 e versioni successive, nonché Ubuntu 18.04/18.10 con il [freecad-stable/freecad-daily PPA](Installing_on_Linux/it#Versione_ufficiale.md) aggiunto alle sorgenti software, installare le seguenti dipendenze.

-    `qtbase5-dev`
    

-    `qttools5-dev`
    

-    `qt5-default`(if compiling 0.20 on a machine that still has Qt4)

-    `libqt5opengl5-dev`
    

-    `libqt5svg5-dev`
    

-    `qtwebengine5-dev`
    

-    `libqt5xmlpatterns5-dev`
    

-    `libqt5x11extras5-dev`
    

-    `libpyside2-dev`
    

-    `libshiboken2-dev`
    

-    `pyside2-tools`
    

-    `pyqt5-dev-tools`
    

-    `python3-dev`
    

-    `python3-matplotlib`
    

-    `python3-packaging`
    

-    `python3-pivy`
    

-    `python3-ply`
    

-    `python3-pyside2.qtcore`
    

-    `python3-pyside2.qtgui`
    

-    `python3-pyside2.qtsvg`
    

-    `python3-pyside2.qtwidgets`
    

-    `python3-pyside2.qtnetwork`
    

-    `python3-pyside2.qtwebengine`
    

-    `python3-pyside2.qtwebenginecore`
    

-    `python3-pyside2.qtwebenginewidgets`
    

-    `python3-pyside2.qtwebchannel`
    

-    `python3-pyside2uic`
    



#### Kernel OpenCascade 

Il kernel OpenCascade è la libreria grafica di base per creare forme 3D. Esiste in una versione ufficiale OCCT e in una versione comunitaria OCE. La versione community non è più consigliata perché obsoleta.

Per Debian Buster e Ubuntu 18.10 e successivi, così come Ubuntu 18.04 con [freecad-stable/freecad-daily PPA](Installing_on_Linux/it#Versione_ufficiale.md) aggiunto alle tue sorgenti software, installare i pacchetti ufficiali.

-    `libocct*-dev`-   
        `libocct-data-exchange-dev`
        

    -   
        `libocct-draw-dev`
        

    -   
        `libocct-foundation-dev`
        

    -   
        `libocct-modeling-algorithms-dev`
        

    -   
        `libocct-modeling-data-dev`
        

    -   
        `libocct-ocaf-dev`
        

    -   
        `libocct-visualization-dev`
        

-    `occt-draw`
    

Per Debian Jessie, Stretch, Ubuntu 16.04 e versioni successive, installare i pacchetti della community edition.

-    `liboce*-dev`-   
        `liboce-foundation-dev`
        

    -   
        `liboce-modeling-dev`
        

    -   
        `liboce-ocaf-dev`
        

    -   
        `liboce-ocaf-lite-dev`
        

    -   
        `liboce-visualization-dev`
        

-    `oce-draw`
    

È possibile installare le librerie singolarmente o utilizzando l\'espansione dell\'asterisco. Cambiare `occ` con `oce` se si vogliono installare le librerie della comunità.


```python
sudo apt install libocct*-dev
```



#### Pacchetti opzionali 

Opzionalmente si possono anche installare i seguenti pacchetti extra:

-    `libsimage-dev`, per fare in modo che Coin supporti formati di file immagine aggiuntivi.

-    `doxygen`e `libcoin-doc` (o `libcoin80-doc` per i sistemi precedenti), se si vuole generare la documentazione del codice sorgente.

-    `libspnav-dev`, per il supporto di [dispositivi di input 3D](3D_input_devices/it.md), come \"Space Navigator\" o \"Space Pilot\" di 3Dconnexion.

-    `checkinstall`, se si intende registrare i file installati nel gestore pacchetti del tuo sistema, in modo da poterlo disinstallare in seguito.



#### Comando Singolo per Python 3 e Qt5 

Richiede Pyside2 disponibile in Debian buster e nel [freecad-stable/freecad-daily PPA\|freecad-stable/freecad-daily PPA](Installing_on_Linux/it#Versione_ufficiale.md).


{{Code|lang=bash|code=
sudo apt install cmake cmake-gui libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside2-dev libqt5opengl5-dev libqt5svg5-dev qtwebengine5-dev libqt5x11extras5-dev libqt5xmlpatterns5-dev libshiboken2-dev libspnav-dev libvtk7-dev libx11-dev libxerces-c-dev libzipios++-dev occt-draw pyside2-tools python3-dev python3-matplotlib python3-packaging python3-pivy python3-ply python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtsvg python3-pyside2.qtwidgets python3-pyside2.qtnetwork python3-pyside2.qtwebengine python3-pyside2.qtwebenginecore python3-pyside2.qtwebenginewidgets python3-pyside2.qtwebchannel python3-markdown python3-git python3-pyside2uic qtbase5-dev qttools5-dev swig libyaml-cpp-dev
}}

NOTA: su alcune versioni di Ubuntu e alcune versioni di Qt, si riceverà un errore che python3-pyside2uic non può essere trovato - su quei sistemi puoi tranquillamente ometterlo. Su Ubuntu 20.04 si dovrà aggiungere `pyqt5-dev-tools`. Maggiori informazioni possono essere trovate in [questa discussione del forum](https://forum.freecadweb.org/viewtopic.php?t=51324).


<div class="mw-collapsible mw-collapsed" style="background-color:#e0e0e0">



#### Comando Singolo per Python 2 e Qt4 

Non raccomandato per le installazioni più recenti in quanto sia Python 2 che Qt4 sono obsoleti.


<div class="mw-collapsible-content">


{{Code|lang=bash|code=
sudo apt install cmake debhelper dh-exec dh-python libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin80-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside-dev libqt4-dev libqt4-opengl-dev libqtwebkit-dev libshiboken-dev libspnav-dev libvtk6-dev libx11-dev libxerces-c-dev libzipios++-dev lsb-release occt-draw pyside-tools python-dev python-matplotlib python-pivy python-ply swig
}}

Gli utenti di Ubuntu 16.04 possono consultare anche la discussione sulla compilazione nel forum: [Compilazione su Linux (Kubuntu): CMake non riesce a trovare VTK](http://forum.freecadweb.org/viewtopic.php?f=4&t=16292).


</div>


</div>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Raspberry Pi 


<div class="mw-collapsible-content">

Seguire gli stessi passaggi di Debian e Ubuntu.

Sono stati segnalati problemi durante il tentativo di compilazione in Raspberry PI OS a 32 bit con Python 3 e Qt5, ma la combinazione Python 3 e Qt4 sembra funzionare per le versioni precedenti di FreeCAD (con problemi minori).

Per le versioni più recenti di FreeCAD (\>= 0.20) la compilazione con Py3/Qt5 va a buon fine se il sistema operativo installato è Raspberry Pi OS 64-bit o Ubuntu 20.04.

A causa di diversi problemi con Qt, in Ubuntu 20.04 non verranno trovati i normali strumenti PySide. {{Code|lang=bash|code=
E: Unable to locate package python3-pyside2uic
}}

In questo caso, si possono installare i pacchetti da PyQt e creare collegamenti simbolici agli strumenti necessari. {{Code|lang=bash|code=
sudo apt-get install pyqt5-dev
sudo apt-get install pyqt5-dev-tools
cd /usr/bin/
ln -s pyrcc5 pyside2-rcc
ln -s pyuic5 pyside2-uic
}}

Ora la compilazione può procedere. {{Code|lang=bash|code=
cd freecad-build/
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DUSE_PYBIND11=ON
make -j2
}}

L\'opzione `-j` di `make` non dovrebbe essere maggiore di 3 perché il Raspberry Pi ha una memoria limitata. Ci vorranno diverse ore per compilare, quindi è meglio farlo durante la notte.

Per ulteriori informazioni, [FreeCAD e Raspberry Pi 4](https://forum.freecadweb.org/viewtopic.php?f=42&t=37458&start=160#p396652).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora


<div class="mw-collapsible-content">

C\'è un bug in cmake distribuito da Fedora 34/35 che fa sì che cmake non riesca a trovare le librerie opencascade. Questo può essere facilmente risolto apportando una piccola modifica al file cmake di livello superiore di opencascade installato su Fedora. Dettagli qui: <https://bugzilla.redhat.com/show_bug.cgi?id=2083568>.

Nella parte superiore del file **OpenCASCADEConfig.cmake**, modificare la seguente riga per utilizzare {{Incode|REAL_PATH()}}. Questa operazione corregge un bug introdotto dall\'uso di un collegamento simbolico da {{Incode|/lib}} a {{Incode|/usr/lib}} di Fedora, che causa l\'errore di cmake.

Questo file è solitamente installato in **/usr/lib64/cmake/opencascade/OpenCASCADEConfig.cmake**.


{{Code|lang=bash|code=
get_filename_component (OpenCASCADE_INSTALL_PREFIX "${OpenCASCADE_INSTALL_PREFIX}" PATH)
}}

cambiare in:


{{Code|lang=bash|code=
file (REAL_PATH ${OpenCASCADE_INSTALL_PREFIX} OpenCASCADE_INSTALL_PREFIX)
}}

Questa banale modifica deve essere apportata all\'interno della directory di build una volta che cmake è stato eseguito e ha avuto esito negativo. La riesecuzione di cmake rileverà quindi correttamente le librerie OCCT nel modo normale.

Sono necessari i seguenti pacchetti:

-    {{Incode|gcc-c++}}(or possibly another C++ compiler?)

-    {{Incode|cmake}}
    

-    {{Incode|doxygen}}
    

-    {{Incode|swig}}
    

-    {{Incode|gettext}}
    

-    {{Incode|dos2unix}}
    

-    {{Incode|desktop-file-utils}}
    

-    {{Incode|libXmu-devel}}
    

-    {{Incode|freeimage-devel}}
    

-    {{Incode|mesa-libGLU-devel}}
    

-    {{Incode|opencascade-devel}}
    

-    {{Incode|openmpi-devel}}
    

-    {{Incode|python3}}
    

-    {{Incode|python3-devel}}
    

-    {{Incode|python3-pyside2}}
    

-    {{Incode|python3-pyside2-devel}}
    

-    {{Incode|pyside2-tools}}
    

-    {{Incode|boost-devel}}
    

-    {{Incode|tbb-devel}}
    

-    {{Incode|eigen3-devel}}
    

-    {{Incode|qt-devel}}
    

-    {{Incode|qt5-qtwebengine-devel}}
    

-    {{Incode|qt5-qtxmlpatterns}}
    

-    {{Incode|qt5-qtxmlpatterns-devel}}
    

-    {{Incode|qt5-qtsvg-devel}}
    

-    {{Incode|qt5-qttools-static}}
    

-    {{Incode|ode-devel}}
    

-    {{Incode|xerces-c}}
    

-    {{Incode|xerces-c-devel}}
    

-    {{Incode|opencv-devel}}
    

-    {{Incode|smesh-devel}}
    

-    {{Incode|Coin3}}
    

-    {{Incode|Coin3-devel}}
    

-    {{Incode|yaml-cpp}}
    

(Aprile 2021, sono disponibili Coin4 e Coin4-devel) (se coin2 è l\'ultimo disponibile per la tua versione di Fedora, usare i packages di <http://www.zultron.com/rpm-repo/>)

-    {{Incode|SoQt-devel}}
    

-    {{Incode|freetype}}
    

-    {{Incode|freetype-devel}}
    

-    {{Incode|vtk}}
    

-    {{Incode|vtk-devel}}
    

-    {{Incode|med}}
    

-    {{Incode|med-devel}}
    

E facoltativamente:

-    {{Incode|libspnav-devel}}(per il supporto di dispositivi 3Dconnexion come Space Navigator o Space Pilot)

-    {{Incode|python3-pivy}}( <https://bugzilla.redhat.com/show_bug.cgi?id=458975> Pivy non è obbligatorio ma necessario per l\'ambiente Draft)

-   python3-markdown (affinché Addon Manager visualizzi il markdown nativo)

-    {{Incode|python3-GitPython}}(affinché Addon Manager utilizzi git per il checkout e l\'aggiornamento di workbench e macro)

Per installare tutte le dipendenze contemporaneamente (testato su fedora 36 e 37):


{{Code|lang=bash|code=
sudo dnf install gcc-c++ cmake doxygen swig gettext dos2unix desktop-file-utils libXmu-devel freeimage-devel mesa-libGLU-devel opencascade-devel openmpi-devel python3 python3-devel python3-pyside2 python3-pyside2-devel pyside2-tools boost-devel tbb-devel eigen3-devel qt-devel qt5-qtwebengine-devel qt5-qtxmlpatterns qt5-qtxmlpatterns-devel qt5-qtsvg-devel qt5-qttools-static ode-devel xerces-c xerces-c-devel opencv-devel smesh-devel Coin3 Coin3-devel SoQt-devel freetype freetype-devel vtk vtk-devel med med-devel libspnav-devel python3-pivy python3-markdown python3-GitPython yaml-cpp
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Gentoo


<div class="mw-collapsible-content">

Il modo più semplice per verificare quali pacchetti sono necessari per compilare FreeCAD è verificare tramite portage:

emerge -pv freecad

Questo dovrebbe fornire un bel elenco di pacchetti extra che devi installare sul tuo sistema.

Se FreeCAD non è disponibile su portage, è disponibile su [waebbl overlay](https://github.com/waebbl/waebbl-gentoo). Il tracker dei problemi sull\'overlay waebbl Github può aiutare a navigare attraverso alcuni problemi, che si potrebbero incontrare. L\'overlay fornisce freecad-9999, che si può scegliere di compilare o semplicemente usare per ottenere le dipendenze.

layman -a waebbl


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE


<div class="mw-collapsible-content">

#### Tumbleweed

I seguenti comandi installeranno i pacchetti richiesti per la creazione di FreeCAD con Qt5 e Python 3.


```python
zypper in --no-recommends -t pattern devel_C_C++ devel_qt5

zypper in libqt5-qtbase-devel libqt5-qtsvg-devel libqt5-qttools-devel boost-devel swig libboost_program_options-devel libboost_mpi_python3-devel libboost_system-devel libboost_program_options-devel libboost_regex-devel libboost_python3-devel libboost_thread-devel libboost_system-devel libboost_headers-devel libboost_graph-devel python3 python3-devel python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-pyside2-devel python3-pivy gcc gcc-fortran cmake occt-devel libXi-devel opencv-devel libxerces-c-devel Coin-devel SoQt-devel freetype2-devel eigen3-devel libode6 vtk-devel libmed-devel hdf5-openmpi-devel openmpi2-devel netgen-devel freeglut-devel libspnav-devel f2c doxygen dos2unix glew-devel yaml-cpp
```

Il seguente comando installerà Qt Creator e GNU Project Debugger.


```pythonzypper in libqt5-creator gdb```

Se mancano dei pacchetti, si può controllare il file Tumbleweed [\"FreeCAD.spec\"](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/FreeCAD.spec) su [Open Build Service](https://build.opensuse.org/package/show/openSUSE:Factory/FreeCAD).

Inoltre, controllare se ci sono patch che devono essere applicate (come [0001 -find-openmpi2-include-files.patch](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/0001-find-openmpi2-include-files.patch)).

#### Leap

Se c\'è una differenza tra i pacchetti disponibili su Tumbleweed e Leap, allora si può leggere il Leap [\"FreeCAD.spec \"](https://build.opensuse.org/package/view_file/openSUSE:Leap:15.0/FreeCAD/FreeCAD.spec) su [Open Build Service](https://build.opensuse.org/) per determinare i pacchetti richiesti.

Vedere la guida [piano_jonas unofficial \"Compile On openSUSE\"](https://forum.freecadweb.org/viewtopic.php?f=4&t=49726).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch Linux 


<div class="mw-collapsible-content">

Ci sarà bisogno delle seguenti librerie dai repository ufficiali:

-    `boost`
    

-    `cmake`
    

-    `coin`
    

-    `curl`
    

-    `desktop-file-utils`
    

-    `eigen`
    

-    `gcc-fortran`
    

-    `git`
    

-    `glew`
    

-    `hicolor-icon-theme`
    

-    `jsoncpp`
    

-    `libspnav`
    

-    `med`
    

-    `nlohmann-json`
    

-    `opencascade`
    

-    `pyside2-tools`
    

-    `pyside2`
    

-    `python-matplotlib`
    

-    `python-netcdf4`
    

-    `python-packaging`
    

-    `python-pivy`
    

-    `qt5-svg`
    

-    `qt5-tools`
    

-    `qt5-webengine`
    

-    `shared-mime-info`
    

-    `shiboken2`
    

-    `swig`
    

-    `utf8cpp`
    

-    `xerces-c`
    

-    `yaml-cpp`
    


```python
sudo pacman -S --needed boost cmake coin curl desktop-file-utils eigen gcc-fortran git glew hicolor-icon-theme jsoncpp libspnav med nlohmann-json opencascade pyside2-tools pyside2 python-matplotlib python-netcdf4 python-packaging python-pivy qt5-svg qt5-tools qt5-webengine shared-mime-info shiboken2 swig utf8cpp xerces-c yaml-cpp 
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Distribuzioni precedenti e non convenzionali 


<div class="mw-collapsible-content">

Su altre distribuzioni, abbiamo pochissimi feedback dagli utenti, quindi potrebbe essere più difficile trovare i pacchetti richiesti.

Inizialmente provare ad individuare le librerie richieste menzionate in [librerie di terze parti](Third_Party_Libraries/it.md) nel tuo gestore di pacchetti. Attenzione che alcuni di essi potrebbero avere un nome di pacchetto leggermente diverso; cerca `name`, ma anche `libname`, `name-dev`, `name-devel` e simili. Se ciò non fosse possibile, provare a compilare tu stesso quelle librerie.

FreeCAD richiede la versione del compilatore GNU g++ uguale o superiore alla 3.0.0, poiché FreeCAD è scritto principalmente in C++. Durante la compilazione vengono eseguiti alcuni script Python, quindi l\'interprete Python deve funzionare correttamente. Per evitare qualsiasi problema con il linker è anche una buona idea avere i percorsi della libreria nella variabile `LD_LIBRARY_PATH` o nel file `ld.so.conf`. Questo è già presente nelle moderne distribuzioni Linux, ma potrebbe essere necessario impostarlo in quelle più vecchie.


</div>


</div>

### Pivy

[Pivy](Pivy/it.md) (Python wrapper per Coin3d) non è necessario per compilare FreeCAD o per avviarlo, ma è necessario come dipendenza di runtime per [l\'ambiente Draft](Draft_Workbench/it.md). Se non si utilizzerà questo ambiente di lavoro, non ci sarà bisogno di Pivy. Tuttavia, si noti che Draft Workbench è utilizzato internamente da altri workbench, come [Arch](Arch_Workbench/it.md) e [BIM](BIM_Workbench/it.md), quindi Pivy deve essere installato anche per poter utilizzare questi workbench.

Entro novembre 2015 la versione obsoleta di Pivy inclusa nel codice sorgente di FreeCAD non verrà più compilata su molti sistemi. Questo non dovrebbe essere un grosso problema, poiché normalmente si dovrebbe ottenere Pivy dal gestore dei pacchetti della tua distribuzione; se non si riesce a trovare Pivy, si potrebbe doverlo compilare da solo, vedere [Istruzioni per la compilazione di Pivy](Extra_python_modules/it#Pivy.md).



### Simboli di Debug 

Per risolvere i problemi di crash in FreeCAD, è utile disporre dei simboli di debug di importanti librerie di dipendenze come Qt. A tal fine, si provi ad installare i pacchetti di dipendenza, che terminano con `-dbg`, `-dbgsym`, `-debuginfo` o simili, a seconda della propria distribuzione Linux.

Per Ubuntu, potrebbe essere necessario abilitare repository speciali per poter vedere e installare questi pacchetti di debug con il gestore pacchetti. Vedere [Pacchetti di simboli di debug](https://wiki.ubuntu.com/Debug_Symbol_Packages) per ulteriori informazioni.



## Compilare FreeCAD 


**La compilazione di FreeCAD 0.20 richiede almeno Python 3.6 e Qt 5.9.**

FreeCAD utilizza CMake come sistema di compilazione principale, poiché è disponibile su tutti i principali sistemi operativi. La compilazione con CMake è solitamente molto semplice e avviene in due passaggi.

1.  CMake verifica che tutti i programmi e le librerie necessari siano presenti sul tuo sistema e genera un `Makefile` configurato per il secondo passaggio. FreeCAD ha diverse opzioni di configurazione tra cui scegliere, ma viene fornito con impostazioni predefinite ragionevoli. Alcune alternative sono dettagliate di seguito.
2.  La compilazione stessa, che viene eseguita con il programma `make` e che genera gli eseguibili di FreeCAD.

Poiché FreeCAD è un\'applicazione di grandi dimensioni, la compilazione dell\'intero codice sorgente può richiedere da 10 minuti a un\'ora, a seconda della CPU e del numero di core della CPU utilizzati per la compilazione.



## Compilazione

Per compilare è sufficiente creare una directory di build, `build`. Quindi da questa directory di build puntare `cmake` alla cartella di origine corretta. Puoi usare `cmake-gui` o `ccmake` invece di `cmake` anche nelle istruzioni seguenti. Una volta che `cmake` ha finito di configurare l\'ambiente, usare `make` per avviare la compilazione vera e propria.


{{Code|lang=bash|code=
# from the base of your freecad source folder:
mkdir build
cd build
cmake ../
make -j$(nproc --ignore=2)
}}

L\'opzione `-j` di `make` controlla quanti lavori (file) vengono compilati in parallelo. Il programma `nproc` stampa il numero di core della CPU nel tuo sistema; utilizzandolo insieme all\'opzione `-j` si può scegliere di processare tanti file quanti sono i core, in modo da velocizzare la compilazione complessiva del programma. Nell\'esempio sopra, si utilizzeranno tutti i core del sistema tranne due; questo manterrà il tuo computer reattivo per altri usi mentre la compilazione procede in background. L\'eseguibile di FreeCAD apparirà infine nella directory `build/bin`. Vedere anche [Velocizzare la compilazione](Compiling_(Speeding_up)/it.md) per migliorare la velocità di compilazione.



### Risoluzione dei problemi di cmake 

Se si è già eseguita una build e si rimane bloccati su una dipendenza, che non viene riconosciuta o non sembra essere risolta, si provi quanto segue:

-   Eliminare il contenuto della directory di build prima di eseguire nuovamente cmake. FreeCAD è un obiettivo in rapido movimento, si potrebbe incappare su informazioni cmake memorizzate nella cache che puntano a una versione precedente rispetto a quella che il nuovo head del repository può utilizzare. Svuotare la cache può consentire a cmake di recuperare e riconoscere la versione effettivamente necessaria.

-   Se cmake segnala la mancanza di un file specifico, utilizzare uno strumento come \"apt-file search\", o il suo equivalente in altri sistemi di pacchetti, per scoprire a quale pacchetto appartiene quel file ed installarlo. Tenere presente, che probabilmente si avrà bisogno della versione -dev del pacchetto,che contiene i file di intestazione o di configurazione necessari a FreeCAD per utilizzare il pacchetto.



### Compilazione con GNU libc 2.34 e successivi 

GNU libc 2.34 introduce una modifica alla libreria che può causare il fallimento delle build su alcuni sistemi Linux con un errore come:


{{Code|lang=bash|code=
No rule to make target '/usr/lib/x86_64-linux-gnu/libdl.so
}}

Per risolvere questo problema, è necessario creare manualmente un collegamento simbolico dal libdl.so.\* installato nel sistema (ora vuoto) alla posizione indicata dal compilatore, che sta cercando il file. Ad esempio (se la copia effettivamente installata di libdl.so sul tuo sistema è /usr/lib/x86_64-linux-gnu/libdl.so.2):


{{Code|lang=bash|code=
sudo ln -s /usr/lib/x86_64-linux-gnu/libdl.so.2 /usr/lib/x86_64-linux-gnu/libdl.so
}}

Adattare il comando alla struttura del sistema cercando libdl.so\* e collegandolo alla posizione appropriata.



### Come riparare la directory del codice sorgente 

Se si è accidentalmente eseguita una compilazione all\'interno della directory del codice sorgente o si sono aggiunti strani file e si desidera ripristinare i contenuti solo nel codice sorgente originale, si possono eseguire i seguenti passaggi.


{{Code|lang=bash|code=
> .gitignore
git clean -df
git reset --hard HEAD
}}

La prima riga cancella il file `.gitignore`. Ciò garantisce che i seguenti comandi di pulizia e ripristino influiranno su tutto nella directory e non ignoreranno gli elementi che corrispondono alle espressioni in `.gitignore`. La seconda riga elimina tutti i file e le directory, che non sono tracciati dal repository git; quindi l\'ultimo comando ripristinerà qualsiasi modifica ai file tracciati, incluso il primo comando che ha cancellato il file `.gitignore`.

Se non si cancella la directory di origine, le successive esecuzioni di `cmake` potrebbero non acquisire nuove opzioni per il sistema se il codice cambia.



### Configurazione

Passando opzioni diverse a `cmake`, si può modificare il modo in cui FreeCAD viene compilato. La sintassi è la seguente.


```python
cmake -D <var>:<type>=<value> $SOURCE_DIR
```

Dove `$SOURCE_DIR` è la directory che contiene il codice sorgente. `<type>` può essere omesso nella maggior parte dei casi. Lo spazio dopo l\'opzione `-D` può anche essere omesso.

Ad esempio, per evitare di creare l\'[Ambiente FEM](FEM_Workbench/it.md)


{{Code|lang=bash|code=
cmake -D BUILD_FEM:BOOL=OFF ../freecad-source
cmake -DBUILD_FEM=OFF ../freecad-source
}}

Tutte le possibili variabili sono elencate nel file `InitializeFreeCADBuildOptions.cmake`, che si trova nella directory `cMake/FreeCAD_Helpers`. In questo file, cercare la parola `option` per arrivare alle variabili, che possono essere impostate e vedere i loro valori predefiniti.

    # ==============================================================================
    # =================   All the options for the build process    =================
    # ==============================================================================

    option(BUILD_FORCE_DIRECTORY "The build directory must be different to the source directory." OFF)
    option(BUILD_GUI "Build FreeCAD Gui. Otherwise you have only the command line and the Python import module." ON)
    option(FREECAD_USE_EXTERNAL_ZIPIOS "Use system installed zipios++ instead of the bundled." OFF)
    option(FREECAD_USE_EXTERNAL_SMESH "Use system installed smesh instead of the bundled." OFF)
    ...

Come alternativa, utilizzare il comando `cmake -LH` per elencare la configurazione corrente, e quindi tutte le variabili, che possono essere modificate. Si può anche installare ed utilizzare `cmake-gui` per avviare un\'interfaccia grafica, che mostra tutte le variabili che possono essere modificate. Nelle sezioni successive si elencano alcune delle opzioni più rilevanti, che si potrebbe voler utilizzare.



##### Per una compilazione di Debug 

Creare una build `Debug` per risolvere i problemi di crash in FreeCAD. Attenzione che con questa build l\'[Ambiente Sketcher](Sketcher_Workbench/it.md) diventa molto lento quando sono presenti schizzi complessi.


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Debug ../freecad-source
}}



#### Per una build di rilascio 

Creare una build `Release` per testare il codice, che non vada in crash. Una build `Release` verrà eseguita molto più velocemente di una build `Debug`.


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Release ../freecad-source
}}



#### Compilare per Python 3 e Qt5 

Il supporto per Python 2 e Qt4 è stato rimosso in FreeCAD 0.20 e non è necessario abilitare esplicitamente Qt5 e Python 3 se si compilano le versioni più recenti. Il supporto Qt6 è attualmente in fase di sviluppo, ma non funziona ancora. A meno che non si preveda di assistere nello sforzo di migrazione Qt6, FREECAD_QT_VERSION dovrebbe essere lasciato su \"Auto\" (impostazione predefinita) o impostato esplicitamente su \"5\".

Per la 0.20 e 0.21_dev: {{Code|lang=bash|code=
cmake ../freecad-source
}}

Si noti che quando si passa dalla build 0.20 a quella 0.21_dev, potrebbe essere necessario eliminare CMakeCache.txt prima di eseguire cmake.



#### Compilazione per una specifica versione di Python 

Se l\'eseguibile `python` predefinito nel tuo sistema è un collegamento simbolico a Python 2, `cmake` tenterà di configurare FreeCAD per questa versione. Si deve quindi scegliere un\'altra versione di Python dando il percorso a uno specifico eseguibile:


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

Se non dovesse funzionare, potrebbe essere necessario definire variabili aggiuntive, che puntano alle librerie Python desiderate e includere le directory:


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
    -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
    -DPYTHON_PACKAGES_PATH=/usr/lib/python3.6/site-packages/ \
    ../freecad-source
}}

È possibile avere diverse versioni indipendenti di Python nello stesso sistema, quindi le posizioni e i numeri di versione dei tuoi file Python dipenderanno dalla tua particolare distribuzione Linux. Usare `python3 -V` per visualizzare la versione di Python che si sta usando attualmente; sono necessari solo i primi due numeri; ad esempio, se il risultato è `Python 3.6.8`, è necessario specificare le directory relative alla versione 3.6. Se non si conoscono le directory giuste, provare a cercarle con il comando `locate`.


```python
locate python3.6
```

Si può usare `python3 -m site` in un terminale per determinare la directory `site-packages`, o `dist-packages` per i sistemi Debian.

Alcuni componenti di FreeCAD, come PySide, provano a rilevare automaticamente la versione più recente di Python installata sul tuo sistema, che potrebbe fallire se è diversa da quella che si è inserito sopra. L\'aggiunta della seguente opzione cMake potrebbe risolvere il problema:


{{Code|lang=bash|code=
-DPython3_FIND_STRATEGY=LOCATION
}}



#### Compilare con Qt Creator per Python 3 e Qt5 

1\. Avviare Qt Creator.

2\. Cliccare su **Apri progetto**.

3\. Passare alla directory in cui si trova il codice sorgente, `freecad-source/`, e scegliere il file `CMakeLists.txt` più in alto.

4\. Selezionando il file, si eseguirà automaticamente `cmake` su di esso, ma potrebbe fallire se le opzioni appropriate non sono impostate correttamente.

5\. Andare a **Projects → Build & Run → Imported Kit → Build → Build Settings → CMake**. Impostare la directory di compilazione appropriata, `build/`.

6\. Impostare le variabili appropriate nella finestra di dialogo Valore-chiave, di tipo `String` e `Bool`. 
```python
PYTHON_EXECUTABLE=/usr/bin/python3
```

7\. Se le variabili non caricano correttamente il progetto, potrebbe essere necessario andare su **Projects → Manage Kits → Kits → Default (or Imported Kit or similar) → CMake Configuration**. Quindi premere **Change** e aggiungere la configurazione appropriata come descritto sopra. Potrebbe essere necessario aggiungere più variabili sui percorsi Python, se il sistema Python non viene trovato. 
```python
PYTHON_EXECUTABLE:STRING=/usr/bin/python3.7
PYTHON_INCLUDE_DIR:STRING=/usr/include/python3.7m
PYTHON_LIBRARY:STRING=/usr/lib/x86_64-linux-gnu/libpython3.7m.so
PYTHON_PACKAGES_PATH:STRING=/usr/lib/python3.7/site-packages
```

7.1. Premere **Apply**, quindi **OK**.

7.2. Assicurarsi che il resto delle opzioni siano impostate correttamente, ad esempio, **Qt version** dovrebbe essere una versione presente installata nel sistema, come `Qt 5.9.5 in PATH (qt5)`.

Premere **Apply**, quindi **OK** per chiudere la configurazione.

Il programma `cmake` dovrebbe essere eseguito di nuovo automaticamente e dovrebbe riempire l\'intera finestra di dialogo Valore-chiave con tutte le variabili, che possono essere configurate.

8\. Andare su **Projects → Build & Run → Imported Kit → Run → Run Settings → Run → Run Configuration** e scegliere `FreeCADMain` per compilare la versione grafica di FreeCAD, o ` FreeCADMainCMD` per compilare solo la versione della riga di comando.

9\. Infine, andare al menu **Build → Crea progetto "FreeCAD"**. Se si tratta di una nuova compilazione, dovrebbero essere necessari diversi minuti, o addirittura ore, a seconda del numero di processori disponibili.



#### Plug-in Qt designer 

Se si desidera sviluppare codice Qt per FreeCAD, ci sarà bisogno del plug-in Qt Designer, che fornisce tutti i widget personalizzati di FreeCAD.

Andare in una directory ausiliaria del codice sorgente, eseguire `qmake` con il file di progetto indicato, per creare un `Makefile`; quindi esegui `make` per compilare il plugin.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
qmake plugin.pro
make
}}

Se si sta compilando per Qt5, assicurarsi che il binario `qmake` sia quello per questa versione, in modo che il risultante `Makefile` contenga le informazioni necessarie per Qt5.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
$QT_DIR/bin/qmake plugin.pro
make
}}

dove `$QT_DIR` è la directory, che memorizza le librerie binarie Qt, ad esempio `/usr/lib/x86_64-linux-gnu/qt5`.

La libreria creata è `libFreeCAD_widgets.so`, che deve essere copiata in `$QT_DIR/plugins/designer`.


{{Code|lang=bash|code=
sudo cp libFreeCAD_widgets.so $QT_DIR/plugins/designer
}}



#### Pivy esterno o interno 

In precedenza, era inclusa una versione di Pivy nel codice sorgente di FreeCAD (interno). Se si desiderava usare la copia del tuo sistema di Pivy (esterna), si doveva usare -DFREECAD_USE_EXTERNAL_PIVY=1.

L\'utilizzo di Pivy esterno è diventato l\'impostazione predefinita durante lo sviluppo di FreeCAD 0.16, pertanto questa opzione non deve più essere impostata manualmente.



#### Documentazione Doxygen 

Se si ha installato Doxygen si può compilare la documentazione del codice sorgente. Vedere la [documentazione del codice sorgente](source_documentation/it.md) per le istruzioni.



### Informazioni aggiuntive 

Il codice sorgente di FreeCAD è molto vasto e con CMake è possibile configurare molte opzioni. Imparare a utilizzare completamente CMake può essere utile per scegliere le opzioni giuste per le tue esigenze particolari.

-   [CMake Reference Documentation](https://cmake.org/documentation/) di Kitware.
-   [How to Build a CMake-Based Project](https://preshing.com/20170511/how-to-build-a-cmake-based-project/) (blog) di Preshing sulla programmazione.
-   [Learn CMake\'s Scripting Language in 15 Minutes](https://preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/) (blog) di Preshing sulla programmazione.



### Creazione di un pacchetto debian 

Se si ha intenzione di creare un pacchetto Debian dai sorgenti, si devono prima installare alcuni pacchetti:


{{Code|lang=bash|code=
sudo apt install dh-make devscripts lintian
}}

Andare nella directory di FreeCAD e chiamare


{{Code|lang=bash|code=
debuild
}}

Una volta compilato il pacchetto, si può usare `lintian` per controllare se il pacchetto contiene errori


{{Code|lang=bash|code=
lintian freecad-package.deb
}}



#### Pacchetto \*.deb con checkinstall 

Lo script Debian `checkinstall` permette di creare un pacchetto \*.deb che può essere installato e rimosso con i comandi standard `dpkg`. Potrebbe essere necessario installarlo prima (su Ubuntu usare `sudo apt install checkinstall`). È interattivo e richiede le informazioni richieste fornendo impostazioni predefinite utili. Durante il processo viene installato il pacchetto e vengono creati un file \*.deb e un archivio di backup.

È una buona idea definire un nome e una breve descrizione per il pacchetto. Il nome deve essere inserito per disinstallarlo nuovamente e la descrizione sarà elencata da `dpkg -l`. Il nome predefinito \"build\" non è molto informativo.

Esempio:


{{Code|lang=bash|code=
cd freecad-source/build
cmake ..
make
sudo checkinstall                                  # e.g. name=freecad-test1
}}

Il risultato è un file \*.deb nella cartella build. `checkinstall` installerà la build per impostazione predefinita. Ecco come installarlo o disinstallarlo:


{{Code|lang=bash|code=
cd freecad-source/build
ls <nowiki>|</nowiki> grep freecad
        freecad-test1_20220814-1_amd64.deb
sudo dpkg -i freecad-test1_20220814-1_amd64.deb   # install
dkpg -l <nowiki>|</nowiki> grep freecad                            # find by name
sudo dpkg -r freecad-test1                        # uninstall by name
}}



### Aggiornare il codice sorgente 

Il sistema CMake permette di aggiornare in modo intelligente il codice sorgente, e ricompilare solo ciò che è cambiato, rendendo più veloci le compilazioni successive.

Spostarsi nella posizione in cui è stato scaricato per la prima volta il codice sorgente di FreeCAD ed estrarre il nuovo codice:


{{Code|lang=bash|code=
cd freecad-source
git pull
}}

Quindi spostarsi nella directory di build in cui il codice è stato compilato inizialmente ed eseguire `cmake`, specificando la directory presente (indicata da un punto); quindi attivare la ricompilazione con `make`.


{{Code|lang=bash|code=
cd ../freecad-build
cmake .
make -j$(nproc --ignore=2)
}}



## Disinstallazione del codice sorgente 

Nel caso in cui il codice sorgente compilato sia stato installato con `sudo make install` (per Debian) i file sono stati copiati nella cartella **/usr/local** in diverse sottocartelle. Per la disinstallazione è possibile utilizzare il file **install_manifest.txt**. È stato creato nella cartella build durante la compilazione e contiene tutti i file installati. Finché esiste questo file, l\'installazione può essere disinstallata.


{{Code|lang=bash|code=
cd freecad-source/freecad-build
xargs sudo rm < install_manifest.txt
}}



## Risoluzione dei problemi 



### Per sistemi a 64 bit 

Quando si compila FreeCAD per 64 bit, esiste un problema noto con il pacchetto OpenCASCADE (OCCT) a 64 bit. Per far funzionare correttamente FreeCAD, potrebbe essere necessario eseguire lo script `configure` e impostare ulteriori `CXXFLAGS`:


{{Code|lang=bash|code=
./configure CXXFLAGS="-D_OCC64"
}}

Per i sistemi basati su Debian questa opzione non è necessaria quando si usano i pacchetti OpenCASCADE precompilati, perché questi impostano internamente il `CXXFLAGS` appropriato.



## Script di compilazione automatica 

Ecco tutto quello che serve per una compilazione completa di FreeCAD. Si tratta di uno script di approccio e funziona su una distro di recente installazione. I comandi richiedono la password di root per l\'installazione dei pacchetti e dei nuovi repository online. Questi script dovrebbero funzionare su versioni a 32 e 64 bit. Sono stati scritti per diverse versioni, e dovrebbero essere eseguibili anche su versioni successive, con o senza grandi cambiamenti.

Se si ha uno script di questo tipo per la propria distribuzione preferita, lo si discuta sul [forum di FreeCAD](https://forum.freecadweb.org/viewforum.php?f=21&sid=e3c22dca9da076fefb56b1d5c5fb3134) in modo che possa essere incorporato.


<div class="mw-collapsible mw-collapsed toccolours">

### Ubuntu


<div class="mw-collapsible-content">

Questi script forniscono un modo affidabile, per installare il set corretto di dipendenze necessarie per creare ed eseguire FreeCAD su Ubuntu. Fanno uso degli archivi dei pacchetti personali di Ubuntu (PPA) e dovrebbero funzionare su qualsiasi versione di Ubuntu considerata dal PPA. Il PPA [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) contempla le versioni recenti di Ubuntu, mentre il [+archive/ubuntu/freecad-stable freecad-stable](https://launchpad.net/~freecad-maintainers/) PPA si rivolge alle versioni ufficialmente supportate di Ubuntu.

Questo script installa l\'istantanea compilata quotidianamente di FreeCAD e le sue dipendenze. Aggiunge il repository giornaliero, ottiene le dipendenze per creare questa versione e installa i pacchetti richiesti. Successivamente procede a inserire il codice sorgente in una directory particolare, crea una directory di compilazione e vi si modifica, configura l\'ambiente di compilazione con `cmake` e infine compila l\'intero programma con `make`. Salvare lo script in un file, renderlo eseguibile ed eseguirlo, ma non usare `sudo`; i privilegi di superutente verranno richiesti solo per i comandi selezionati.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-daily && sudo apt-get update
sudo apt-get build-dep freecad-daily
sudo apt-get install freecad-daily

git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DFREECAD_USE_PYBIND11=ON ../freecad-source
make -j$(nproc --ignore=2)
}}

Se lo si desidera, si può disinstallare la versione precompilata di FreeCAD (`freecad-daily`) lasciando le dipendenze in posizione, tuttavia, lasciare questo pacchetto installato consentirà al gestore di pacchetti di mantenere aggiornate anche le sue dipendenze; questo è utile soprattutto se si intende seguire lo sviluppo di FreeCAD e aggiornare e compilare costantemente i sorgenti dal repository Git.

Lo script precedente presuppone, che si voglia compilare l\'ultima versione di FreeCAD, quindi che si stia usando il repository \"daily\", per ottenere le dipendenze. Tuttavia, si può invece ottenere le dipendenze di build della versione \"stabile\" per l\'attuale versione di Ubuntu. In tal caso, sostituire la parte superiore dello script precedente con le seguenti istruzioni. Per Ubuntu 12.04, omettere `--enable-source` dal comando.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-stable && sudo apt-get update
sudo apt-get build-dep freecad
sudo apt-get install libqt5xmlpatterns5-dev   # Needed for 0.20; should go away on next packaging update 
sudo apt-get install freecad
}}

Una volta installato il pacchetto `freecad` dal repository `freecad-stable`, questo sostituirà l\'eseguibile di FreeCAD disponibile dal repository Universe Ubuntu. L\'eseguibile sarà chiamato semplicemente `freecad`, e non `freecad-stable`.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE 


<div class="mw-collapsible-content">

Non sono necessari repository esterni per compilare FreeCAD. Tuttavia, esiste un\'incompatibilità con python3-devel, che deve essere rimossa. FreeCAD può essere compilato da GIT


{{Code|lang=bash|code=
# install needed packages for development
sudo zypper install gcc cmake OpenCASCADE-devel libXerces-c-devel \
python-devel libqt4-devel python-qt4 Coin-devel SoQt-devel boost-devel \
libode-devel libQtWebKit-devel libeigen3-devel gcc-fortran git swig
 
# create new dir, and go into it
mkdir FreeCAD-Compiled 
cd FreeCAD-Compiled
 
# get the source
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git free-cad
 
# Now you will have a subfolder in this location called free-cad. It contains the source
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build1
cd FreeCAD-Build1 
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}

Dato che si sta usando git, la prossima volta che si desidera compilare non è necessario clonare tutto, basta estrarre da git e ricompilare


{{Code|lang=bash|code=
# go into free-cad dir created earlier
cd free-cad
 
# pull
git pull
 
# get back to previous dir
cd ..
 
# Now repeat last few steps from before.
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build2
cd FreeCAD-Build2
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
# Note: to speed up build use all CPU cores: make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Debian Squeeze 


<div class="mw-collapsible-content">


{{Code|lang=bash|code=
# get the needed tools and libs
sudo apt-get install build-essential python libcoin60-dev libsoqt4-dev \
libxerces-c2-dev libboost-dev libboost-date-time-dev libboost-filesystem-dev \
libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev \
libboost-serialization-dev libboost-signals-dev libboost-regex-dev \
libqt4-dev qt4-dev-tools python2.5-dev \
libsimage-dev libopencascade-dev \
libsoqt4-dev libode-dev subversion cmake libeigen2-dev python-pivy \
libtool autotools-dev automake gfortran
 
# checkout the latest source
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git freecad
 
# go to source dir
cd freecad
 
# build configuration 
cmake .
 
# build FreeCAD
# Note: to speed up build use all CPU cores: make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora 27/28/29 


<div class="mw-collapsible-content">

Postato dall\'utente [http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666 PrzemoF](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666_PrzemoF.md) nel forum.


{{Code|lang=bash|code=
#!/bin/bash

ARCH=$(arch)

MAIN_DIR=FreeCAD
BUILD_DIR=build

#FEDORA_VERSION=27
#FEDORA_VERSION=28
FEDORA_VERSION=29

PACKAGES="gcc cmake gcc-c++ boost-devel zlib-devel swig eigen3 qt-devel \
shiboken shiboken-devel pyside-tools python-pyside python-pyside-devel xerces-c \
xerces-c-devel OCE-devel smesh graphviz python-pivy python-matplotlib tbb-devel \
 freeimage-devel Coin3 Coin3-devel med-devel vtk-devel"

FEDORA_29_PACKAGES="boost-python2 boost-python3 boost-python2-devel boost-python3-devel"

if [ "$FEDORA_VERSION" = "29" ]; then
    PACKAGES="$PACKAGES $FEDORA_29_PACKAGES"
fi

echo "Installing packages required to build FreeCAD"
sudo dnf -y install $PACKAGES
cd ~
mkdir $MAIN_DIR <nowiki>||</nowiki> { echo "~/$MAIN_DIR already exist. Quitting.."; exit; }
cd $MAIN_DIR
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git
mkdir $BUILD_DIR <nowiki>||</nowiki> { echo "~/$BUILD_DIR already exist. Quitting.."; exit; }
cd $BUILD_DIR
cmake ../FreeCAD 
make -j$(nproc)
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Arch usando AUR 


<div class="mw-collapsible-content">

[Arch User Repository (AUR)](https://aur.archlinux.org/) è una raccolta di ricette create dagli utenti per creare pacchetti, che non sono ufficialmente supportati dai manutentori della distribuzione/comunità. Di solito sono sicuri. Puoi vedere chi mantiene il pacchetto e per quanto tempo lo ha fatto. Si consiglia di controllare i file di compilazione. In quest\'area sono disponibili anche software non open source, anche se mantenuti dalla società proprietaria ufficiale.

Prerequisito: git

Passaggi:

1.  Aprire un terminale. Facoltativamente, creare una directory, ad es. {{incode | mkdir git}}. Opzionalmente cambiare directory es. `cd git`.
2.  Clonare il repository AUR: `git clone https://aur.archlinux.org/freecad-git.git`
3.  Inserire la cartella del repository AUR: `cd freecad-git`
4.  Compilare, usando [Arch makepkg](https://wiki.archlinux.org/index.php/Makepkg) : `makepkg -s`. Il flag -s o \--syncdeps installerà anche le dipendenze richieste.
5.  Installare il pacchetto creato: `makepkg --install` o fare doppio clic su pkgname-pkgver.pkg.tar.xz all\'interno del browser dei file.

Per aggiornare FreeCAD all\'ultima build basta ripetere dal passaggio 3. Aggiornare il repository AUR quando c\'è qualche modifica sostanziale nella ricetta o nuove funzionalità, usando `git checkout -f` all\'interno della cartella.


</div>


</div>


{{docnav/it|[Compilazione in Windows](Compile_on_Windows/it.md)|[Compilazione in MacOS](Compile_on_MacOS/it.md)}}



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Linux/it
