# Third Party Libraries/it
## Panoramica

Si tratta di librerie che FreeCAD utilizza come dipendenze di terze parti durante la compilazione. Di solito sono [librerie collegate dinamicamente](https://en.wikipedia.org/wiki/Dynamic_loading) e hanno un\'estensione `.so` in Linux/MacOS e `.dll` in Windows, e sono accompagnate dai loro file di intestazione `.h` o `.hpp` o simili. Se è necessaria una libreria modificata o una classe wrapper, il codice della libreria modificata, o wrapper, deve diventare parte del codice sorgente di FreeCAD e compilato insieme ad esso.

Le dipendenze devono essere installate nel sistema prima di procedere con la compilazione; vedi [Compilazione in Linux](Compile_on_Linux/it.md), [Compilazione in Windows](Compile_on_Windows/it.md) e [Compilazione in MacOS](Compile_on_MacOS/it.md) per maggiori informazioni.

Se stai compilando usando Windows, prendi in considerazione l\'utilizzo di [LibPack](#LibPack.md) invece di provare a installare le librerie singolarmente.



## Collegamenti

++++
| Nome della libreria | Versione necessaria     | Link per ottenerla                                                            |
+=====================+=========================+===============================================================================+
| Python              | \>= 3.6                 | <http://www.python.org/>                                                      |
++++
| Boost               | \>= 1.33                | <http://www.boost.org/>                                                       |
++++
| OpenCASCADE         | \>= 7.3                 | <http://www.opencascade.org>                                                  |
++++
| Qt                  | \>= 5.4                 | <https://www.qt.io/>                                                          |
++++
| Shiboken2           |          | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **same as Qt** |                                                                               |
|                     |                      |                                                                               |
++++
| PySide2             |          | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **same as Qt** |                                                                               |
|                     |                      |                                                                               |
++++
| Coin3D              | \>= 3.x                 | <https://github.com/coin3d/coin>                                              |
++++
| SoQt (deprecated)   | \>= 1.2                 | <https://github.com/coin3d/soqt>                                              |
++++
| Quarter             | \>= 1.0                 | <https://github.com/coin3d/quarter>                                           |
++++
| Pivy                | \>= 0.6.5               | <https://github.com/coin3d/pivy/>                                             |
++++
| FreeType            | \>= XXX                 | XXX                                                                           |
++++
| PyCXX               | \>= XXX                 | XXX                                                                           |
++++
| KDL                 | \>= XXX                 | <https://orocos.org/wiki/orocos/kdl-wiki.html>                                |
++++
| Point Cloud Library | \>= XXX                 | XXX                                                                           |
++++
| Salome SMESH        | \>= XXX                 | XXX                                                                           |
++++
| VTK                 | \>= 6.0                 | XXX                                                                           |
++++
| Ply                 | \>= 3.11                | <https://www.dabeaz.com/ply/>                                                 |
++++
| Xerces-C++          | \>= 3.0                 | <https://xerces.apache.org/xerces-c/>                                         |
++++
| Eigen3              | \>= 3.0                 | <http://eigen.tuxfamily.org/index.php?title=Main_Page>                        |
++++
| Zipios++            | \>= 0.1.5               | <https://snapwebsites.org/project/zipios>, <https://github.com/Zipios/Zipios> |
++++
| Zlib                | \>= 1.0                 | <http://www.zlib.net/>, <https://github.com/madler/zlib>                      |
++++
| libarea             | \>= 0.0.20140514-1      | <https://github.com/danielfalck/libarea>                                      |
++++
|                     |                         |                                                                               |
++++



## Dettagli

### Python

**Versione:** 3.3 o superiore

**Licenza:** licenza Python 3.3


**Python 2 è diventato obsoleto nel 2019. L'ulteriore sviluppo di FreeCAD utilizzerà esclusivamente Python 3; la compatibilità con Python 2 non verrà testata, quindi i vecchi ambienti di lavoro e le macro che utilizzano questa versione dovranno essere aggiornati o potrebbero smettere di funzionare. Si prega di avvisare sul [https://forum.freecadweb.org/ forum di FreeCAD] se si riscontrano problemi con Python 3.**

Python è un popolare linguaggio di scripting per tutti gli usi ampiamente utilizzato in Linux e nel software open source. In FreeCAD, Python viene utilizzato durante la compilazione e anche in fase di esecuzione in diversi modi. È utilizzato

-   per scrivere script di test per testare condizioni diverse, come perdite di memoria, per garantire la funzionalità del software dopo le modifiche, per controlli post-compilazione e test di copertura dei test,
-   per scrivere [macro](Macros/it.md) e registrazione di macro,
-   per implementare la logica dell\'applicazione per i pacchetti standard,
-   per implementare strumenti ausiliari come [Addon Manager](Std_AddonMgr/it.md),
-   per implementare interi ambienti di lavoro come [Draft](Draft_Workbench/it.md) e [Arch](Arch_Workbench/it.md),
-   per caricare dinamicamente i pacchetti,
-   per implementare regole per la progettazione (ingegneria della conoscenza)
-   per creare interazioni fantasiose su Internet come gruppi di lavoro e PDM

Su Linux, Python è solitamente già installato nella propria distribuzione. Per Windows è possibile ottenere un binario precompilato da [Python.org](http://www.python.org/) o usare [ActiveState Python](http://www.activestate.com/), anche se è più difficile ottenere le librerie di debug da quest\'ultimo.

Python è stato scelto come linguaggio di scripting per FreeCAD per diversi motivi:

-   È più orientato agli oggetti rispetto a Perl e Tcl.
-   Il codice è più leggibile di Perl e Visual Basic.
-   È più facile da incorporare in un\'altra applicazione, a differenza, ad esempio, di Java.

In sintesi, Python è ben documentato ed è facile da incorporare ed estendere in un\'applicazione C++. È anche ben testato e gode di un forte sostegno da parte della comunità open source. Letture ulteriori su Python sfogliando la documentazione ufficiale su [Python.org](http://www.python.org).

### Boost

**Versione:** 1.33 o superiore

**Licenza:** Boost Software License - Versione 1.0

Le librerie Boost C++ sono raccolte di librerie open source sottoposte a revisione paritaria che estendono le funzionalità di C++. Sono pensate per essere ampiamente utili in un ampio spettro di applicazioni e per funzionare bene con la libreria standard C++. La licenza Boost è progettata per incoraggiarne l\'uso in progetti open source e closed source.

A causa della loro popolarità e stabilità, molte librerie Boost sono state accettate per l\'incorporazione nello standard C++11 e altre sono pianificate per l\'inclusione nei successivi standard C++.

Al fine di garantire efficienza e flessibilità, Boost fà ampio uso di modelli. Boost è stata una fonte di intenso lavoro e di ricerca nella programmazione generica e nella meta-programmazione in C++. Maggiori informazioni su Boost visitando la [home page di Boost](http://www.boost.org/).

### OpenCASCADE Technology 

**Versione:** 6.7 o superiore

**Licenza:** la versione 6.7.0 e successive sono regolate dalla [GNU Lesser General Public License (LGPL) versione 2.1 con eccezioni aggiuntive](https://www.opencascade.com/content/licensing). Le versioni precedenti utilizzano la [Open CASCADE Technology Public License](https://www.opencascade.com/content/occt-public-license).

OpenCASCADE Technology (OCCT) è un kernel CAD completo e di livello professionale. È stato sviluppato nel 1993 e originariamente chiamato CAS.CADE, da Matra Datavision in Francia per le applicazioni Strim (Styler) ed Euclid Quantum. Nel 1999 è stato rilasciato come software open source e da allora si chiama OpenCASCADE.

OCCT è un insieme ampio e complesso di librerie C++ che forniscono le funzionalità richieste da un\'applicazione CAD:

-   Un kernel geometrico completo conforme a STEP.
-   Un modello di dati topologici e le funzioni necessarie per lavorare con le forme (taglio, fusione, estrusione e molte altre).
-   Processori d\'importazione ed esportazione standard per file come STEP, IGES, VRML.
-   Un visualizzatore 2D e 3D con supporto alla selezione.
-   Una struttura di dati di documenti e progetti con supporto per salvataggio e ripristino, collegamento esterno di documenti, ricalcolo della cronologia di progettazione (modellazione parametrica) e una funzione per caricare dinamicamente nuovi tipi di dati come pacchetto di estensione.

Esistono due versioni principali di OpenCASCADE esistenti in diverse distribuzioni Linux. Una è distribuita dagli sviluppatori originali; è noto come OCCT ed è impacchettato con i nomi `occ` o `occt`. L\'altra versione è la \"community edition\", abbreviata OCE, e si trova normalmente con il nome `oce`. FreeCAD può compilare con entrambe le versioni, tuttavia, dal 2016 FreeCAD consiglia di compilare con le librerie OCCT ufficiali piuttosto che con quelle OCE. Il motivo è che l\'edizione della comunità mancano importanti correzioni di bug e funzioni che rendono migliore l\'utilizzo di FreeCAD.

Per ulteriori informazioni, visitare il [sito web di OpenCASCADE](http://www.opencascade.org).

### Qt

**Versione:** 4.1 o superiore

**Licenza:** GPL v2.0/v3.0 o commerciale; dalla versione 4.5 in poi anche LPGL v2.1.

Qt è uno dei toolkit di interfaccia utente grafica (GUI) più popolari disponibili nel mondo open source. FreeCAD utilizza questo toolkit per disegnare l\'interfaccia del programma. Per questo, l\'applicazione Qt Designer è molto utile in quanto consente agli sviluppatori di disegnare rapidamente finestre di dialogo e finestre, esportarle come file di risorse XML e quindi caricare queste interfacce in fase di esecuzione.

Ulteriori informazioni sulle librerie Qt e la relativa documentazione di programmazione sono disponibili nella [Documentazione di Qt](https://doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).

#### Shiboken2 e Pyside2 

Shiboken è il generatore di binding Python che Python Qt utilizza per creare il modulo PySide, in altre parole, è il sistema utilizzato per esporre l\'API Qt C++ al linguaggio Python.

I pacchetti originali Shiboken e PySide dovevano essere usati con Python 2 e Qt4; poiché queste due versioni sono considerate obsolete dal 2019, utilizzare Shiboken2 e PySide2, che funzionano con Python 3 e Qt5. Il nuovo sviluppo di FreeCAD è fatto con Python 3 e Qt5, quindi la compatibilità con Python 2 e Qt4 non è garantita dopo FreeCAD 0.18.

Maggiori informazioni su Shiboken e Pyside su [Qt per Python](https://wiki.qt.io/Qt_for_Python/Shiboken).

### Coin3D

**Versione:** 3.0 o superiore

**Licenza:** BSD 3-clause license

Coin3D è una libreria di grafica 3D di alto livello con una interfaccia di programmazione delle applicazioni (Application Programming Interface) in C++. Per \"renderizzare\" i grafici in tempo reale utilizza la struttura di dati scenegraph (grafo di scena) adatta alla maggior parte delle applicazioni di visualizzazione scientifica e ingegneristica.

Coin3D è costruito secondo lo standard del settore OpenGL delle librerie di modalità di renderizzazione immediata, e aggiunge astrazioni per primitive di livello superiore, fornisce interattività 3D e contiene molte funzioni di ottimizzazione complesse per il rendering veloce che sono trasparenti per il programmatore di applicazioni.

Coin3D è compatibile con l\'API Open Inventor 2.1 di SGI. Questa API è diventata l\'interfaccia grafica standard de facto per la visualizzazione 3D nella comunità scientifica e ingegneristica. Ha dimostrato il suo valore sin dal 2000 come componente principale in migliaia di applicazioni ingegneristiche in tutto il mondo.

Coin3D (Open Inventor) viene utilizzato come visualizzatore 3D in FreeCAD perché il visualizzatore OpenCASCADE (AIS e Graphics3D) presenta limitazioni e colli di bottiglia nelle prestazioni, in particolare con il rendering ingegneristico su larga scala; altre cose come texture o rendering volumetrico non sono interamente supportate dal visualizzatore OpenCASCADE.

Coin3D è portatile su un\'ampia gamma di piattaforme: sistemi operativi UNIX, Linux, BSD, macOS e Microsoft Windows. Per saperne di più su questa libreria, visita la [homepage di Coin3D](https://github.com/coin3d/coin).



#### SoQt (deprecato) 

**Versione:** 1.2.0 o superiore

**Licenza:** BSD 3-clause license

SoQt è il binding di Coin3D (Open Inventor) al toolkit GUI Qt.

SoQt non è più utilizzato in FreeCAD, è stato sostituito da Quarter che è un binding a Qt più recente.

#### Quarter

**Versione:** 1.0 or higher

**Licenza:** BSD 3-clause license

Quarter è un binding a Coin3D più recente rispetto al toolkit Qt. Una sua versione è inclusa nel codice sorgente di FreeCAD, quindi viene compilata insieme ad esso.

#### Pivy

**Versione:** 0.6.3 o successiva

**Licenza:** BSD 3-clause license

[Pivy](Pivy/it.md) è una libreria che avvolge la libreria Coin3d per l\'uso in [Python](Python/it.md). Non è necessaria per compilare FreeCAD o per avviarla, ma è necessaria come dipendenza di runtime dall\'[Ambiente Draft](Draft_Workbench/it.md) e da altri ambienti che la utilizzano internamente, come [Arch](Arch_Workbench/it.md) e [BIM](BIM_Workbench/it.md).

Se non si utilizzano questi ambienti di lavoro, non ci sarà bisogno di Pivy.

### Ply

**Versione:** 3.11 o successiva

**Licenza:** BSD 3-clause license

Ply è il parser Python-Lex-Yacc. Viene utilizzato come dipendenza di runtime dall\'[Ambiente OpenSCAD](OpenSCAD_Workbench/it.md). Se non si utilizza questo workbench, si potrebbe non aver bisogno di questo pacchetto.

Per ulteriori informazioni, vedere la [home page di Ply](https://www.dabeaz.com/ply/)

### Xerces-C++ 

**Versione:** 3.0 o successiva

**Licenza:** Apache Software License Versión 2.0

Xerces-C++ è un analizzatore (parser) di convalida XML scritto in un sottoinsieme portatile di C++. Xerces-C++ rende più facile fornire alla propria applicazione la capacità di leggere e scrivere dati XML. Per l\'analisi, la generazione, la manipolazione, e la convalida di documenti XML è prevista una libreria condivisa.

Xerces-C++ è un analizzatore XML di convalida scritto in un sottoinsieme portabile di C++. Xerces-C++ rende facile dare alla tua applicazione la capacità di leggere e scrivere dati XML. Viene fornita una libreria condivisa per l\'analisi, la generazione, la manipolazione e la convalida di documenti XML. Xerces-C++ è fedele alla raccomandazione XML 1.0 e agli standard associati.

L\'analizzatore viene utilizzato per salvare e ripristinare i parametri in FreeCAD. Per ulteriori informazioni, vedere la [homepage di Xerces-C++](https://xerces.apache.org/xerces-c/).

### Eigen3

**Versione:** 3.0 o successiva

**Licenza:** A partire dalla versione 3.1.1, è concesso in licenza con la [Mozilla Public License 2.0](http://www.mozilla.org/MPL/2.0). Le versioni precedenti erano concesse in licenza in base alla [GNU Lesser General Public License 3](https://www.gnu.org/licenses/lgpl-3.0.en.html).

Eigen è una libreria di template C++ per l\'algebra lineare: matrici, vettori, solutori numerici e algoritmi correlati.

Se vuoi solo usare Eigen, puoi usare subito i file di header. Non esiste alcuna libreria binaria a cui collegarsi e nessun file di intestazione configurato. Eigen è una libreria di modelli pura definita negli header.

Eigen è utilizzato in FreeCAD per molte operazioni vettoriali nello spazio 3D. Per saperne di più, visita la [homepage di Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page).

### Zipios++

**Versione:** 0.1.5 o successiva

**Licenza:** GNU Lesser General Public License 2.1

Zipios++ è una libreria C++ per leggere e scrivere file `.zip`. L\'accesso alle singole voci viene fornito tramite iostream C++ standard. Viene inoltre fornito un semplice file system virtuale di sola lettura che monta directory regolari e file `.zip`. La struttura e l\'interfaccia pubblica di Zipios++ sono vagamente basate sul pacchetto `java.util.zip` di Java.

Il formato di file nativo di FreeCAD `.FCstd` è in realtà un file `.zip` che memorizza e comprime altri tipi di dati al suo interno, come i file BREP e XML. Pertanto, Zipios++ viene utilizzato per salvare e aprire archivi compressi, inclusi i file FreeCAD.

Una copia di Zipios++ è inclusa nel codice sorgente di FreeCAD quindi viene compilata insieme ad esso. Se desideri utilizzare una libreria Zipios++ esterna, fornita dal tuo sistema operativo, si può impostare -DFREECAD_USE_EXTERNAL_ZIPIOS=ON con `cmake`.

Zipios++ utilizza la libreria Zlib per eseguire l\'effettiva decompressione dei file.

#### Zlib

**Versione:** 1.0 o successiva

**Licenza:** licenza zlib

Zlib è progettato per essere una libreria di compressione dei dati gratuita, generica e senza perdite da utilizzare su qualsiasi hardware e sistema operativo. Implementa l\'algoritmo di compressione `DEFLATE` comunemente usato nei file `.zip` e `.gzip`.

Una copia di questa libreria è inclusa nel codice sorgente di FreeCAD, quindi viene compilata insieme ad esso.

### libarea

**Versione:** 0.0.20140514-1 o successiva

**Licenza:** BSD 3-clause license

Libarea è una libreria software per calcolare le operazioni di profili e tasche utilizzate nel software di produzione assistita da computer (CAM). È stata creata da Dan Heeks per il suo progetto HeeksCNC.

Una copia della libreria è inclusa nel codice sorgente dell\'[Ambiente Path](Path_Workbench/it.md), quindi viene compilata insieme ad esso.

### LibPack

LibPack è un pacchetto utile con le dipendenze di compilazione di FreeCAD raccolte insieme. È necessario solo se si sta compilando FreeCAD su Windows con Visual Studio 2015 o versioni successive. È possibile trovare l\'ultimo LibPack nella [releases page](https://github.com/FreeCAD/FreeCAD/releases).

Se si sta lavorando sotto Linux, non c\'è bisogno del LibPack, poiché si può ottenere le dipendenze dai repository della tua distribuzione come menzionato nella pagina [Compilazione in Linux](Compile_on_Linux/it.md).

### FreeCAD 12.1.2 

Vedere l\'annuncio nel forum: [Nuovi libpack per Windows con Qt5.12, OCC7.3 e Python 3.6 di apeltauer](https://forum.freecadweb.org/viewtopic.php?f=4&t=35789)

Include tra le altre cose: Boost 1.67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technology 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salome SMESH, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2 .11



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Third Party Libraries/it
