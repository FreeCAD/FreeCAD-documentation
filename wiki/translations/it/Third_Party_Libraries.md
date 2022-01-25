# Third Party Libraries/it
{{TOCright}}


<div class="mw-translate-fuzzy">

### Panoramica

Si tratta di librerie che nel progetto di FreeCAD non vengono modificate. Sono utilizzate sostanzialmente senza modifiche come librerie a collegamento dinamico (\*.so o \*.dll). Se è necessario modificarle o è necessaria una classe wrapper (classe involucro), allora il codice della wrapper o il codice della libreria modificata deve essere spostato nel pacchetto base di FreeCAD.


</div>

The dependencies need to be installed in the system before proceeding with compilation; see [compile on Linux](Compile_on_Linux.md), [compile on Windows](Compile_on_Windows.md), and [compile on MacOS](Compile_on_MacOS.md) for more information.


<div class="mw-translate-fuzzy">

Per l\'ambiente Windows, considerare la possibilità di usare [LibPack](#LibPack/it.md) invece di scaricare e installare tutto da soli.

Le librerie utilizzate sono:


</div>

## Link


<div class="mw-translate-fuzzy">

++++
| Nome della libreria | Versione necessaria     | Link per ottenerla                                                            |
+=====================+=========================+===============================================================================+
| Python              | \>= 3.4                 | <http://www.python.org/>                                                      |
++++
| Boost               | \>= 1.33                | <http://www.boost.org/>                                                       |
++++
| OpenCASCADE         | \>= 6.7                 | <http://www.opencascade.org>                                                  |
++++
| Qt                  | \>= 4.1                 | <https://www.qt.io/>                                                          |
++++
| Shiboken2           |          | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **same as Qt** |                                                                               |
|                     |                      |                                                                               |
++++
| PySide2             |          | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **same as Qt** |                                                                               |
|                     |                      |                                                                               |
++++
| Coin3D              | \>= 3.x                 | <https://bitbucket.org/Coin3D/coin/wiki/Home>                                 |
++++
| SoQt (deprecated)   | \>= 1.2                 | <https://bitbucket.org/Coin3D/soqt/src/default/>                              |
++++
| Quarter             | \>= 1.0                 | <https://bitbucket.org/Coin3D/quarter/src/default/>                           |
++++
| FreeType            | \>= XXX                 | XXX                                                                           |
++++
| PyCXX               | \>= XXX                 | XXX                                                                           |
++++
| KDL                 | \>= XXX                 | XXX                                                                           |
++++
| Point Cloud Library | \>= XXX                 | XXX                                                                           |
++++
| Salome SMESH        | \>= XXX                 | XXX                                                                           |
++++
| VTK                 | \>= 6.0                 | XXX                                                                           |
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


</div>

## Dettagli

### Python

**Versione:** 3.3 o superiore

**Licenza:** licenza Python 3.3


**Python 2 became obsolete in 2019. Further development of FreeCAD will use exclusively Python 3; compatibility with Python 2 won't be tested, so old workbenches and macros that use this version will have to be updated or they may stop working. Please post on the [https://forum.freecadweb.org/ FreeCAD forum] if you encounter problems with Python 3.**

Python is a popular all-purpose scripting language that is widely used in Linux and open source software. In FreeCAD, Python is used during compilation and also at runtime in different ways. It is used

-   to write test scripts to test for different conditions, such as memory leaks, to ensure functionality of the software after changes, for post build checks, and test coverage tests,
-   to write [macros](macros.md) and macro recording,
-   to implement application logic for standard packages,
-   to implement auxiliary tools such as the [Addon Manager](Std_AddonMgr.md),
-   to implement entire workbenches like [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md),
-   to dynamically load packages,
-   to implement rules for design (knowledge engineering),
-   to do fancy Internet interactions like work groups and PDM


<div class="mw-translate-fuzzy">

È possibile utilizzare il codice sorgente o i binari forniti da <http://www.python.org/> oppure, in alternativa, utilizzare ActiveState Python fornito da <http://www.activestate.com/> anche se è un po\' difficile ottenere le librerie di debug da ActiveState.


</div>

Python was chosen as the scripting language for FreeCAD for different reasons:

-   It is more object oriented than Perl and Tcl.
-   The code is more readable than Perl and Visual Basic.
-   It is easier to embed in another application, unlike, say, Java.

In summary, Python is well documented, and it\'s easy to embed and extend in a C++ application. It is also well tested and has strong support from the open source community. Read more about Python and browse the official documentation at [Python.org](http://www.python.org).

### Boost

**Versione:** 1.33 o superiore

**Licenza:** Boost Software License - Versione 1.0


<div class="mw-translate-fuzzy">

Le librerie Boost C++ sono un insieme di librerie open source sottoposte a revisione paritaria, librerie che estendono le funzionalità di C++. Le librerie sono rilasciate sotto Licenza Boost Software, progettate per consentire a Boost di essere utilizzato sia con progetti aperti che chiusi. Molti dei fondatori di Boost fanno parte della commissione C++ standard e diverse librerie di Boost sono state accettate per l\'incorporazione nel Technical Report 1 di C++0x.


</div>

Due to their popularity and stability, many Boost libraries have been accepted for incorporation into the C++11 standard, and more are planned for inclusion in subsequent C++ standards.


<div class="mw-translate-fuzzy">

Al fine di garantire efficienza e flessibilità, Boost fà ampio uso di modelli. Boost è stata una fonte di intenso lavoro e di ricerca nella programmazione generica e nella meta-programmazione in C++.


</div>


<div class="mw-translate-fuzzy">

#### OpenCasCade


</div>


<div class="mw-translate-fuzzy">

**Versione:** 5.2 o superiore


</div>


<div class="mw-translate-fuzzy">

**Licenza:** v6.7.0 and later are governed by GNU Lesser General Public License (LGPL) version 2.1 with additional exception. <https://www.opencascade.com/content/licensing> Earlier versions use a slightly different license: <https://www.opencascade.com/content/occt-public-license>


</div>


<div class="mw-translate-fuzzy">

OCC è un kernel di CAD completo. Originariamente, è stato sviluppato da Matra Datavision in Francia per le applicazioni Strim e Euclid Quantum e successivamente è stato reso Open Source. E\' una enorme libreria e sopratutto rende possibile un programma di CAD gratuito, mettendo a disposizione alcuni pacchetti che sarebbero difficili o impossibili da realizzare in un progetto Open Source:

-   Un kernel di geometria che supporta STEP
-   Un modello topologico di dati e tutte le funzioni necessarie per lavorare con essi (taglio, fusione, estrusione, ecc \...)
-   Processori standard di importazione / esportazione come STEP, IGES, VRML
-   Visualizzatore 3D e 2D con il supporto per la selezione
-   Un documento e una struttura di dati del progetto con il supporto per salvare e ripristinare, collegamenti esterni dei documenti, il ricalcolo della cronologia del progetto (modellazione parametrica) e un sistema per caricare nuovi tipi di dati in modo dinamico come un pacchetto di estensione.


</div>

OCCT is a big and complex set of C++ libraries that provide functionality required by a CAD application:

-   A complete STEP compliant geometry kernel.
-   A topological data model and needed functions to work with shapes (cut, fuse, extrude, and many others).
-   Standard import and export processors for files like STEP, IGES, VRML.
-   A 2D and 3D viewer with selection support.
-   A document and project data structure with support for save and restore, external linking of documents, recalculation of design history (parametric modeling) and a facility to load new data types as an extension package dynamically.

There are two main versions of OpenCASCADE in existence in different Linux distributions. One is distributed by the original developers; it is known as OCCT, and is packaged under the names `occ` or `occt`. The other version is the \"community edition\", abbreviated OCE, and is normally found with the `oce` name. FreeCAD can compile against either version, however, since 2016 FreeCAD recommends compiling against the official OCCT libraries rather than the OCE ones. The reason is that the community edition lacks important bug fixes and functions that make using FreeCAD better.


<div class="mw-translate-fuzzy">

Per saperne di più su OpenCascade visitare la pagina di OpenCascade o consultare <http://www.opencascade.org>.


</div>


<div class="mw-translate-fuzzy">

#### Qt


</div>


<div class="mw-translate-fuzzy">

**Versione:** 4.1.x o superiore


</div>


<div class="mw-translate-fuzzy">

**Licenza:** GPL v2.0/v3.0 o Commerciale (dalla versione 4.5 anche LPGL v2.1)


</div>


<div class="mw-translate-fuzzy">

Non credo sia necessario dire molto su Qt. E\' uno degli strumenti più utilizzati per i progetti di GUI (Interfacce grafiche) Open Source. Secondo me, i motivi principali per utilizzare Qt sono Qt Designer e la possibilità di caricare intere finestre di dialogo come risorse (XML) e di incorporarvi dei widget (componenti accessori) specializzati. In un\'applicazione CAX l\'interazione tra l\'utente e le finestre di dialogo costituiscono sicuramente la maggior parte del codice e disporre un buon disegnatore di dialoghi è molto importante per poter estendere facilmente FreeCAD con nuove funzionalità. Ulteriori informazioni e una buona documentazione online si trova in <http://www.qtsoftware.com>.


</div>

Further information about Qt libraries and their programming documentation are available at [Qt Documentation](https://doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).


<div class="mw-translate-fuzzy">

##### Shiboken e Pyside 

**Shiboken** (*Shi bō ken*, 死某剣) è il generatore di binding Python che Qt per Python usa per creare il modulo PySide, in altre parole, è il sistema che usiamo per esporre l\'API Qt C ++ a Python.


</div>

The original Shiboken and PySide packages were meant to be used with Python 2 and Qt4; since these two versions are considered obsolete in 2019, please use Shiboken2 and PySide2, which work with Python 3 and Qt5. New development of FreeCAD is done with Python 3 and Qt5, so compatibility with Python 2 and Qt4 is not guaranteed after FreeCAD 0.18.

Read more about Shiboken and Pyside on [Qt for Python](https://wiki.qt.io/Qt_for_Python/Shiboken).


<div class="mw-translate-fuzzy">

#### Coin3D


</div>


<div class="mw-translate-fuzzy">

**Versione:** 2.0 o superiore


</div>


<div class="mw-translate-fuzzy">

**Licenza:** GPL v2.0 o Commerciale


</div>


<div class="mw-translate-fuzzy">

Coin è una libreria di grafica 3D di alto livello con una interfaccia di programmazione delle applicazioni (Application Programming Interface) in C++. Per \"renderizzare\" i grafici in tempo reale Coin utilizza la struttura di dati scenegraph (grafo di scena) adatta alla maggior parte delle applicazioni di visualizzazione scientifica e ingegneristica.


</div>


<div class="mw-translate-fuzzy">

Coin è costruito secondo lo standard del settore OpenGL delle librerie di modalità di renderizzazione immediata, e aggiunge astrazioni per primitive di livello superiore, fornisce interattività 3D, aumenta enormemente la praticità e la produttività del programmatore, e contiene molte funzioni di ottimizzazione complesse per il rendering veloce che sono trasparenti per il programmatore di applicazioni.


</div>


<div class="mw-translate-fuzzy">

Coin si basa sul SGI (sistema di gestione integrato) della API (interfaccia di programmazione di applicazioni) di Open Inventor. Open Inventor, per coloro che non hanno familiarità con essa, è da tempo diventata di fatto la libreria standard per la visualizzazione grafica 3D e per i software di simulazione visiva nella comunità scientifica e di ingegneria. È stata sperimentata per un periodo di oltre 10 anni, la sua maturità contribuisce al suo successo. È utilizzata quale blocco di costruzione principale per migliaia di applicazioni di ingegneria in larga scala in tutto il mondo.


</div>


<div class="mw-translate-fuzzy">

In FreeCAD useremo OpenInventor come visualizzatore 3D perché il visualizzatore OpenCascade (AIS e Graphics3D) ha forti limitazione e costituisce una strozzatura delle prestazioni, soprattutto quando si tratta di grandi renderizzazioni di ingegneria. Altre cose quali texture o renderizzazione volumetrica non sono proprio supportate, ecc \....


</div>


<div class="mw-translate-fuzzy">

Coin è portabile su un\'ampia gamma di piattaforme: qualsiasi piattaforma UNIX / Linux / \* BSD, tutti i sistemi operativi Microsoft Windows, e Mac OS X.


</div>


<div class="mw-translate-fuzzy">

#### SoQt


</div>

**Versione:** 1.2.0 o superiore


<div class="mw-translate-fuzzy">

**Licenza:** GPL v2.0 o Commerciale


</div>


<div class="mw-translate-fuzzy">

SoQt è il collante tra il toolkit dei componenti GUI Qt e Inventor. Purtroppo, non è più LGPL quindi dobbiamo rimuoverlo dal codice base di FreeCAD e collegarlo come una libreria. Ha lo stesso modello di licenza di Coin. Deve essere compilato con la propria versione di Qt.


</div>

SoQt is no longer used in FreeCAD, it was replaced by Quarter which is a more recent Qt binding.

#### Quarter

**Version:** 1.0 or higher

**License:** BSD 3-clause license

Quarter is a newer Coin3D binding to the Qt toolkit. A version of it is included in the source code of FreeCAD so it is compiled together with it.

#### Pivy

**Version:** 0.6.3 or higher

**License:** BSD 3-clause license

[Pivy](Pivy.md) is a library that wraps the Coin3d library for use in [Python](Python.md). It is not needed to build FreeCAD or to start it, but it is needed as a runtime dependency by the [Draft Workbench](Draft_Workbench.md), and by other workbenches that use it internally, like [Arch](Arch_Workbench.md) and [BIM](BIM_Workbench.md).

If you are not going to use these workbenches, you won\'t need Pivy.

### Ply

**Version:** 3.11 or higher

**License:** BSD 3-clause license

Ply is the Python-Lex-Yacc parser. It is used as a runtime dependency by the [OpenSCAD Workbench](OpenSCAD_Workbench.md). If you don\'t use this workbench, you may not need this package.

For more information see [Ply homepage](https://www.dabeaz.com/ply/)


<div class="mw-translate-fuzzy">

#### Xerces-C++ 


</div>


<div class="mw-translate-fuzzy">

**Versione:** 2.7.0 o superiore


</div>

**Licenza:** Apache Software License Versión 2.0


<div class="mw-translate-fuzzy">

Xerces-C++ è un analizzatore (parser) di convalida XML scritto in un sottoinsieme portatile di C++. Xerces-C++ rende più facile fornire alla propria applicazione la capacità di leggere e scrivere dati XML. Per l\'analisi, la generazione, la manipolazione, e la convalida di documenti XML è prevista una libreria condivisa.


</div>


<div class="mw-translate-fuzzy">

In FreeCAD il parser è utilizzato per salvare e ripristinare i parametri.


</div>

### Eigen3

**Version:** 3.0 or higher

**License:** Starting from the 3.1.1 version, it is licensed under the [Mozilla Public License 2.0](http://www.mozilla.org/MPL/2.0). Earlier versions were licensed under the [GNU Lesser General Public License 3](https://www.gnu.org/licenses/lgpl-3.0.en.html).

Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.

If you just want to use Eigen, you can use the header files right away. There is no binary library to link to, and no configured header file. Eigen is a pure template library defined in the headers.

Eigen is used in FreeCAD for many vector operations in 3D space. To learn more, visit [Eigen homepage](http://eigen.tuxfamily.org/index.php?title=Main_Page).

### Zipios++

**Version:** 0.1.5 or higher

**License:** GNU Lesser General Public License 2.1

Zipios++ is a C++ library for reading and writing `.zip` files. Access to individual entries is provided through standard C++ iostreams. A simple read-only virtual file system that mounts regular directories and `.zip` files is also provided. The structure and public interface of Zipios++ are loosely based on the `java.util.zip` package of Java.

FreeCAD\'s native file format `.FCstd` is in reality a `.zip` file that stores and compresses other types of data within it, such as BREP and XML files. Therefore, Zipios++ is used to save and open compressed archives, including FreeCAD files.

A copy of Zipios++ is included in the source code of FreeCAD so it is compiled together with it. If you want to use an external Zipios++ library, provided by your operating system, you may set -DFREECAD_USE_EXTERNAL_ZIPIOS=ON with `cmake`.

Zipios++ uses the Zlib library to perform the actual decompression of files.


<div class="mw-translate-fuzzy">

#### Zlib


</div>


<div class="mw-translate-fuzzy">

**Versione:** 1.x.x


</div>


<div class="mw-translate-fuzzy">

**Licenza:** zlib


</div>


<div class="mw-translate-fuzzy">

zlib è una libreria di compressione usabile praticamente su qualsiasi hardware e sistema operativo senza perdita di dati. Di proposito generale, è progettata per essere libera, giuridicamente svincolata, cioè non coperta da alcun brevetto. Il formato dei dati zlib è di per sé portabile sulle varie piattaforme. A differenza del metodo di compressione LZW utilizzato nella compressione Unix e nel formato immagine GIF, il metodo di compressione attualmente utilizzato in zlib sostanzialmente non espande mai i dati. (LZW può raddoppiare o triplicare le dimensioni del file in casi estremi.) Inoltre, l\'utilizzo di memoria di Zlib è indipendente dai dati di input e, se necessario, può essere ridotta, ma con una perdita di efficienza di compressione.


</div>

A copy of this library is included in the source code of FreeCAD so it is compiled together with it.


<div class="mw-translate-fuzzy">

#### libarea


</div>


<div class="mw-translate-fuzzy">

**Versione:** N/A


</div>


<div class="mw-translate-fuzzy">

**Licenza:** New BSD (BSD 3-Clause)


</div>


<div class="mw-translate-fuzzy">

Area è una parte di software creato da Dan Heeks per HeeksCNC. Viene impiegato come una libreria per la generazione di operazioni CAM correlate all\'ambiente Path.


</div>

A copy of the library is included with the source code of the [Path Workbench](Path_Workbench.md), so it is compiled together with it.


<div class="mw-translate-fuzzy">

### LibPack

LibPack è un utile pacchetto che comprende tutte le librerie di cui sopra. È necessario solo sulla piattaforma Windows e lo si può trovare su <https://github.com/FreeCAD/FreeCAD-ports-cache/releases>. Lavorando sotto Linux non si ha bisogno di LibPack, si deve invece fare uso dei repository di pacchetti della propria distribuzione Linux.


</div>

If you\'re working under Linux, you don\'t need the LibPack, as you can get the dependencies from your distribution\'s repositories as mentioned in the [compile on Linux](Compile_on_Linux.md) page.

### FreeCAD 12.1.2 

See the announcement in the forum: [New libpacks for Windows with Qt5.12, OCC7.3 and Python 3.6 by apeltauer](https://forum.freecadweb.org/viewtopic.php?f=4&t=35789)

It includes among other things: Boost 1.67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technology 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salome SMESH, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2.11



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Third Party Libraries/it
