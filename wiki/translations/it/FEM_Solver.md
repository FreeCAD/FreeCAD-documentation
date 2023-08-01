# FEM Solver/it
{{TOCright}}

## Prefazione


<div class="mw-translate-fuzzy">

Questa pagina raccoglie le informazioni sui risolutori di elementi finiti utilizzati dall\'ambiente [FEM](FEM_Workbench.md). L\'interfaccia tra un solutore e FreeCAD in pre-elaborazione e post-elaborazione viene eseguita tramite file di testo. Ciò significa che in teoria qualsiasi solutore che può essere configurato e controllato tramite un file di testo è in grado di lavorare con FreeCAD; affinché questa comunicazione funzioni devono essere programmati un parser e uno scrittore appropriati dei file di input e di output.


</div>

Wikipedia [elenca molti pacchetti software ad elementi finiti](https://en.wikipedia.org/wiki/List_of_finite_element_software_packages) che potenzialmente potrebbero funzionare con FreeCAD in futuro. Un confronto è disponibile su [feacompare.com](https://feacompare.com/).

### Risolutori disponibili in varie distribuzioni Linux 


<div class="mw-translate-fuzzy">

Il repository [FreeCAD-dependencies](https://github.com/luzpaz/FreeCAD-dependencies) tiene traccia delle dipendenze di FreeCAD su molte distribuzioni Linux. La pagina [FEM.md](https://github.com/luzpaz/FreeCAD-dependencies/blob/master/FC-Workbenches/FEM.md) esamina i risolutori FEA open source che potrebbero essere utilizzati con [FEM](FEM_Workbench/it.md). La pagina mostra la versione di un particolare solutore nel repository di una particolare distribuzione Linux. Questa informazione è utile per sapere se un risolutore è aggiornato o non lo è e deve essere aggiornato.


</div>

Le informazioni sono anche discusse nel forum: [supported and not supported Solver](https://forum.freecadweb.org/viewtopic.php?f=18&t=26326&start=10#p270325).

## Solver con un\'interfaccia in FreeCAD 

Questi solutori sono ben integrati in FreeCAD, il che significa che è possibile impostare ed eseguire un progetto di simulazione dall\'interfaccia grafica e dai pulsanti nell\'ambiente FEM.

### CalculiX


<div class="mw-translate-fuzzy">

### CalculiX 

Questo è il primo solutore che è stato integrato per funzionare con FEM. CalculiX è progettato principalmente per analisi statiche, termomeccaniche e modali. Ulteriori informazioni su questo risolutore sono disponibili in [FEM CalculiX](FEM_CalculiX/it.md).


</div>

### Elmer


<div class="mw-translate-fuzzy">

Il solutore multifisico Elmer è stato integrato in FreeCAD come progetto di [Google Summer of Code 2017](Google_Summer_of_Code_2017.md): [main website](https://www.csc.fi/web/elmer), [community portal](http://www.elmerfem.org./), [code repository](https://github.com/ElmerCSC/elmerfem), [Elmer Integration (GSoC) - Activity Log](https://forum.freecadweb.org/viewtopic.php?f=18&t=22576) (discussione nel forum).


</div>

### Mystran

Mystran is a structural analysis program which uses Nastran input file format. It is released under MIT license. Which means it seems OpenSource. See [main website](https://www.mystran.com/), [code repository](https://github.com/dr-bill-c/MYSTRAN) and [Mystran-FreeCAD-forum (forum topic)](https://forum.freecadweb.org/viewtopic.php?t=46171).

### Z88


<div class="mw-translate-fuzzy">

Il solutore Z88 è progettato per simulazioni statiche lineari con particolare attenzione all\'insegnamento del metodo degli elementi finiti. È stato il secondo risolutore ad essere [integrato in FreeCAD](https://forum.freecadweb.org/viewtopic.php?f=18&t=15568). Successivamente, l\'integrazione è stata migliorata come progetto [Google Summer of Code 2017](Google_Summer_of_Code_2017.md).


</div>


<div class="mw-translate-fuzzy">

Vedere le informazioni:

-   [Main website](https://en.z88.de/z88os/), [download page](https://en.z88.de/download-z88os/), [source code repository](https://github.com/LSCAD/Z88OS) (e binari precompilati).
-   Note di rilascio: [Z88os V15 released 17.07.2017](https://forum.z88.de/viewtopic.php?f=18&t=885), [Z88os V13 released 20.05.2009](https://forum.z88.de/viewtopic.php?t=90) (version in Debian Jessie 8, Stretch 9, Buster 10).
-   [Come usare Z88 in FEM?](https://forum.freecadweb.org/viewtopic.php?t=23318) (forum thread).


</div>

Ci sono due versioni, Z88OS è l\'edizione open source, mentre Z88Aurora è freeware e include un\'interfaccia grafica e dei metodi di soluzione aggiuntivi.

## Solver implementati come ambienti esterni 


<div class="mw-translate-fuzzy">

Questi solutori non sono integrati nell\'ambiente [FEM](FEM_Workbench/it.md), il che significa che hanno bisogno di un\'interfaccia separata per impostare un progetto di simulazione. Ciò si ottiene attraverso le [macro](macros/it.md) o gli [ambienti esterni](external_workbenches/it.md).


</div>

### DualSPHysics

[DualSPHysics](https://dual.sphysics.org/) è un set di librerie C++, CUDA, e Java che usa il modello [idrodinamica a particelle levigate](https://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics) (SPH) denominato [SPHysics](https://wiki.manchester.ac.uk/sphysics/index.php/Main_Page) per studiare i fenomeni di flusso a superficie libera come le onde che si infrangono.


<div class="mw-translate-fuzzy">

DesignSPHysics è un ambiente esterno integrato in FreeCAD che fornisce un\'interfaccia utente grafica per DualSPHysics: [main website](https://design.sphysics.org/), [code repository](https://github.com/dualsphysics/DesignSPHysics), [Interesting project: DesignSPHysics fluid simulator](https://forum.freecadweb.org/viewtopic.php?f=18&t=20595) (discussione nel forum).


</div>


<div class="mw-translate-fuzzy">

DesignSPHysics può essere installato tramite [Addon manager](Std_AddonMgr/it.md).


</div>

### FastHenry e FasterCap 

FastHenry e FasterCap sono risolutori di campi di capacità e induttanza-resistenza sviluppati da FastFieldSolvers: [main website](https://www.fastfieldsolvers.com/default.asp), [download page](https://www.fastfieldsolvers.com/download.htm) (binary and source code), [forum](https://www.fastfieldsolvers.com/forum/).

[EM](EM_Workbench/it.md) è un ambiente di lavoro esterno che è stato creato per servire da front-end per questi risolutori elettromagnetici. FastHenry è completamente supportato per l\'analisi di impedenza magneto-quasistatica 3D, mentre FasterCap è accessibile attraverso alcune macro Python.


<div class="mw-translate-fuzzy">

Vedere: [ElectroMagnetic Workbench](https://forum.freecadweb.org/viewtopic.php?f=9&t=33372) (discussione principale), [Electromagnetic Workbench - again..](https://forum.freecadweb.org/viewtopic.php?f=18&t=31920), [FreeCAD for ElectroMagnetics](https://forum.freecadweb.org/viewtopic.php?f=18&t=5400), [repository del codice](https://github.com/ediloren/EM-Workbench-for-FreeCAD) per l\'ambiente.


</div>


<div class="mw-translate-fuzzy">

L\'ambiente EM può essere installato tramite [Addon manager](Std_AddonMgr/it.md).


</div>

### fcFEM

fcFEM è un risolutore di elementi finiti per studi strutturali e meccanici, implementato in Python e che può essere eseguito direttamente da FreeCAD senza chiamare solutori binari esterni. Pertanto, può essere considerato il risolutore interno di FreeCAD.

fcFEM è stato progettato per superare alcune limitazioni di altri solutori, come CalculiX, al fine di eseguire vari studi di ingegneria strutturale.


<div class="mw-translate-fuzzy">

Alcuni dei problemi che dovrebbero essere risolti da questo risolutore includono

-   Analisi di mesh miste (solidi-shell) per la gestione di colonne composite o componenti architettonici prefabbricati: [FEM object types](https://forum.freecadweb.org/viewtopic.php?f=18&t=21029&p=216682&hilit=sandwich#p216682).
-   Elementi travi e lastre migliorati, poiché gli elementi trave di CalculiX sembrano dare risultati errati: [CalculiX 3-node Beam Element](https://forum.freecadweb.org/viewtopic.php?f=18&t=27903&hilit=beam#p226038), [FEM object types](https://forum.freecadweb.org/viewtopic.php?f=18&t=21029&start=100), [Example for 1D analysis](https://forum.freecadweb.org/viewtopic.php?f=18&t=16044).
-   Controllo della lunghezza dell\'arco per superare i punti limite per l\'analisi del collasso elasto-plastico: [FEM - Tubular Connection with Shell Elements](https://forum.freecadweb.org/viewtopic.php?f=24&t=26921&hilit=riks#p215325).
-   Elementi di interfaccia a spessore zero per varie applicazioni, come il calcestruzzo post-tensionato con attrito: [pre-stressed pre/post-tensioned concrete bridge](https://forum.freecadweb.org/viewtopic.php?f=18&t=30286&hilit=classical&start=20#p259636).


</div>


<div class="mw-translate-fuzzy">

L\'autore considera FreeCAD una buona piattaforma di prototipazione per configurare, testare e visualizzare rapidamente diversi problemi strutturali, quindi avere un solutore integrato ma flessibile è molto utile. Vedere la discussione principale, [fcFEM - FEA from start to finish](https://forum.freecadweb.org/viewtopic.php?f=18&t=33974).


</div>


<div class="mw-translate-fuzzy">

fcFEM è impacchettato come una libreria python e una macro e può essere scaricato dal [github repository](https://github.com/HarryvL/fcFEM). Alla fine sarà disponibile dal [Addon manager](Std_AddonMgr/it.md), o sarà distribuito come parte di FreeCAD stesso.


</div>

### OpenFoam

[OpenFoam](https://openfoam.org/) è un potente framework per la simulazione [fluidodinamica computazionale](https://en.wikipedia.org/wiki/Computational_fluid_dynamics) (CFD), distribuito come una serie di librerie C++.

OpenFoam è disponibile in FreeCAD attraverso due ambienti esterni:

-   [Cfd](https://github.com/qingfengxia/Cfd), originario di Qingfeng Xia.
-   [CfdOF](https://github.com/jaheyns/CfdOF), una biforcazione di Cfd che è finalizzata alla facilità d\'uso.

Mentre Cfd è concepito come funzionalità completa per utenti avanzati, CfdOF è pensato per gli utenti che stanno iniziando con CFD e OpenFoam.


<div class="mw-translate-fuzzy">

Per Cfd: [update on FreeCAD + OpenFOAM fluid dynamic computation](https://forum.freecadweb.org/viewtopic.php?f=18&t=13699) (forum thread), [Progress of the general Computational Fluid Dynamics (CFD) workbench: CfdWorkbench](https://forum.freecadweb.org/viewtopic.php?f=37&t=22993) (old thread).


</div>


<div class="mw-translate-fuzzy">

Per CfdOF: [Computational Fluid Dynamics (CFD) workbench using OpenFOAM](https://forum.freecadweb.org/viewtopic.php?f=18&t=21576) (forum thread), [training material](http://opensim.co.za/training.html).


</div>


<div class="mw-translate-fuzzy">

Entrambi gli ambienti possono essere installati tramite [Addon manager](Std_AddonMgr/it.md), ed entrambi hanno un posto per la discussione nel subforum [CfdOF / CFD](https://forum.freecadweb.org/viewforum.php?f=37).


</div>


<div class="mw-translate-fuzzy">

## Implementazioni in corso 

### FEniCS


</div>

### FEniCS 

FEniCS è un framework di calcolo per la risoluzione di equazioni differenziali alle derivate parziali (PDE), con interfacce di programmazione di alto livello in Python e C++. Può essere usato per stabilire problemi scientifici nelle formulazioni di elementi finiti che possono essere risolti numericamente.


<div class="mw-translate-fuzzy">

Vedere: [main website](https://fenicsproject.org/), [Fenics as Solver](https://forum.freecadweb.org/viewtopic.php?f=18&t=4677) (forum thread).


</div>


<div class="mw-translate-fuzzy">

[FenicsSolver](https://github.com/qingfengxia/FenicsSolver) è una piattaforma di simulazione per affrontare problemi multi-corpo, multi-fisica (accoppiati) e multi-scala. Si spera di integrare il solutore FEniCS sia in [FEM](FEM_Workbench/it.md) che nell\'[ambiente esterno](external_workbenches/it.md) Cfd , quindi il sistema risultante funziona come un\'alternativa gratuita a Comsol o Moose. FenicsSolver è sviluppato dallo stesso autore di Cfd.


</div>

### OOFEM


<div class="mw-translate-fuzzy">

### OOFEM 

[OOFEM](http://www.oofem.org/) è un programma FEM orientato agli oggetti realizzato dall\'Università Tecnica Ceca, per risolvere problemi meccanici, di trasporto e di meccanica dei fluidi.


</div>


<div class="mw-translate-fuzzy">

È stato detto che presenta alcuni vantaggi rispetto a CalculiX, come gli elementi dell\'interfaccia ([pre-stressed pre/post-tensioned concrete bridge](https://forum.freecadweb.org/viewtopic.php?f=18&t=30286&start=20#p260275)), e controllo della lunghezza dell\'arco per l\'analisi del collasso elasto-plastico ([FEM - Tubular Connection with Shell Elements](https://forum.freecadweb.org/viewtopic.php?f=24&t=26921&hilit=Arc#p215325)).


</div>


<div class="mw-translate-fuzzy">

L\'integrazione preliminare in FEM è stata eseguita. Vedere: [OOFem](https://forum.freecadweb.org/viewtopic.php?f=18&t=31288) (main thread), [test request, multiple solvers](https://forum.freecadweb.org/viewtopic.php?t=15568&start=20#p126338).


</div>

Fino a quando l\'integrazione del solutore non viene completata e il nuovo codice non viene unito al repository principale di FreeCAD, i file necessari per l\'utilizzo del solutore in FEM possono essere scaricati da [forked FreeCAD branch](https://github.com/berndhahnebach/FreeCAD_bhb/tree/femoofem/src/Mod/Fem/). Per una panoramica dell\'implementazione, dai un\'occhiata alla cronologia dei commit <https://github.com/berndhahnebach/FreeCAD_bhb/commits/femoofem>

### MBDyn

-   OpenSource general purpose Multibody Dynamics analysis software
-   [MBDyn](https://www.mbdyn.org/)
-   [FreeCAD as pre-post processor for MBDyn (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=39165)

## Solutori non integrati 

I seguenti solutori non sono stati integrati in FreeCAD ma hanno suscitato un certo interesse da parte della comunità degli utenti. Se uno sviluppatore desidera creare un ponte di comunicazione per un determinato risolutore, deve fare riferimento al [subforum FEM](https://forum.freecadweb.org/viewforum.php?f=18) per consigli e assistenza.


<div class="mw-translate-fuzzy">

I seguenti articoli potrebbero essere obsoleti, ma le informazioni che contengono potrebbero comunque essere utili per capire come integrare i solutori in FreeCAD

-   [Estendere il modulo FEM](Extend_FEM_Module/it.md)
-   [Tutorial Aggiungere equazioni FEM](Add_FEM_Equation_Tutorial/it.md)
-   [Tutorial Aggiungere vincoli FEM](Add_FEM_Constraint_Tutorial/it.md)


</div>

### ADAPy

See [ADAPy](https://github.com/Krande/adapy/) and [ADA - Assembly for Design & Analysis (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=64929).

### Agros2D and Hermes 


<div class="mw-translate-fuzzy">

### Agros2D e Hermes 

[Agros2D](http://www.agros2d.org/) è un programma grafico multipiattaforma progettato per risolvere diversi problemi fisici. Internamente utilizza le librerie C++ [Hermes](http://www.hpfem.org/hermes/) per la soluzione di sistemi di equazioni alle derivate parziali non lineari (PDE) semplici e complessi dipendenti dal tempo che utilizzano una versione generale del metodo degli elementi finiti [(hp-FEM)](https://en.wikipedia.org/wiki/Hp-FEM). Codice principale [repository](https://github.com/hpfem/hermes), e [tutorials](https://github.com/hpfem/hermes-tutorial).


</div>

### Code-Aster and Code-Saturne 


<div class="mw-translate-fuzzy">

### Code-Aster e Code-Saturne 

[Code-Aster](https://www.code-aster.org/) è un solutore multiphysics open source; insieme al pre-processore Salomé-Meca formano una piattaforma di simulazione sviluppata da EDF-GDF, la più grande compagnia energetica francese. Era un primo pacchetto considerato per l\'inclusione in FreeCAD: [FreeCAD and Code-Aster/Salome-Meca](https://forum.freecadweb.org/viewtopic.php?t=2839) (discussione nel forum).


</div>

[Code-Saturne](https://www.code-saturne.org/cms/) è un software open source gratuito sviluppato e rilasciato da EDF per risolvere la fluidodinamica computazionale (CFD).

### FElt


<div class="mw-translate-fuzzy">

### FElt 

[FElt](http://felt.sourceforge.net/) è un pacchetto di elementi finiti per risolvere problemi di analisi strutturale lineare statica e dinamica. Il [codice originale](https://sourceforge.net/projects/felt/) è obsoleto, quindi è stato biforcato in un [nuovo repository](https://github.com/Sudhanshu-Dubey14/felt) per far rivivere il progetto e renderlo compilabile in un sistema moderno.


</div>


<div class="mw-translate-fuzzy">

Nei forum è stato suggerito di eseguire l\'analisi dei rinforzi del cemento armato (assemblaggi di travi e colonne) utilizzando elementi trave 1D: [Automation in Design](https://forum.freecadweb.org/viewtopic.php?f=18&t=17061&start=20#p268503), [Felt in FEM Workbench](https://forum.freecadweb.org/viewtopic.php?f=18&t=33463).


</div>

### Frame3DD


<div class="mw-translate-fuzzy">

[Frame3DD](http://frame3dd.sourceforge.net/) è un pacchetto software per l\'analisi strutturale statica e dinamica di strutture 2D e 3D, [repository principale](https://github.com/pslack/frame3dd). Un lettore preliminare per i file di input è stato annunciato nei forum: [Test read data from Frame3DD file.](https://forum.freecadweb.org/viewtopic.php?f=24&t=19428) Argomento generale del forum in FEM <https://forum.freecadweb.org/viewtopic.php?f=18&t=43389> .


</div>

### Impact FEM 


<div class="mw-translate-fuzzy">

### Impact FEM 

-   <http://www.impact-fem.org/> (broken link)


</div>

### libMesh


<div class="mw-translate-fuzzy">

### libMesh 

[libMesh](https://libmesh.github.io/) è una libreria di elementi finiti C++ per la soluzione numerica di equazioni alle derivate parziali, con l\'obiettivo principale di fornire supporto per calcoli di affinamento reticolare adattivo (AMR) in parallelo: [code repository](https://github.com/libMesh/libmesh).


</div>


<div class="mw-translate-fuzzy">

È stato suggerito di integrare questa libreria in FreeCAD come parte di un [progetto](https://forum.freecadweb.org/viewtopic.php?f=8&t=35493) [Google Summer of Code](Google_Summer_of_Code.md).


</div>

### Modelica


<div class="mw-translate-fuzzy">

### Modelica 

[Modelica](https://www.modelica.org/) è un linguaggio per modellare e ottimizzare sistemi fisici complessi e interconnessi, ad esempio meccanici, elettrici, termici, idraulici e altri. Il linguaggio stesso e le sue librerie standard sono open source. Alcuni ambienti di simulazione basati su Modelica, come Catia\'s Dymola, sono proprietari, ma ci sono anche implementazioni free come [OpenModelica](https://openmodelica.org/) and [JModelica](https://jmodelica.org/).


</div>

With FreeCAD, Modelica was suggested to help perform animations, but more broadly it could be used in mechanical and building engineering to solve equations and optimize a particular design: [Modelica (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=32556).

The [PyFMI](https://pypi.org/project/PyFMI/) package contains Python bindings to work with FMU models, which are standardized models in binary format produced by compliant Modelica environments, including Dymola, OpenModelica, and JModelica. It was suggested that this library could help FreeCAD connect to a [Modelica system](https://forum.freecadweb.org/viewtopic.php?f=18&t=32556#p272632) (forum topic).

### Mumps

[Mumps](http://mumps-solver.org/) is a generic solver for massive systems of equations, which generally deals with factorizing and operating on sparse matrices. It was mentioned in the forum: [Test request, multiple solvers (forum topic)](https://forum.freecadweb.org/viewtopic.php?t=15568&start=20#p126087).

It does not perform finite element analysis directly, but it may be used internally by other packages like Code-Aster.

### Nastran

Nastran is a structural analysis program developed by NASA in the 1970s. Modern versions of it are commercial products and closed source; however, older versions of it, [Nastran-93](https://github.com/nasa/NASTRAN-93) and [Nastran-95](https://github.com/nasa/NASTRAN-95) were released as open source in 2015. Forum post: [Nastran (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=12753).

There is no technical support for the open source code, and it is probably difficult to compile in a modern system.

### OpenSees

[OpenSees](https://opensees.berkeley.edu/) is a software framework for developing applications to simulate structural and geotechnical systems mainly in the field of earthquake engineering. [OpenSees, the Open System for Earthquake Engineering Simulation (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=20745) and [Relicensing of OpenSees (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31922).

### PolyFEM

[PolyFEM](https://polyfem.github.io/) is a simple C++ and Python finite element library. We provide a wide set of common partial differential equations including: Laplace, Helmholtz, Linear Elasticity, Saint-Venant Elasticity, Neo-Hookean Elasticity and Stokes. [PolyFEM (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=42857).

### Sparselizard

[Sparselizard](http://www.sparselizard.org/) is a fast, general, multiphysics, p-adaptive, open source C++ finite element library running on Linux, Mac and Windows. It is used to design next generation microdevices (ultrasound transducers, micromirrors, microvalves, comb drives,\...) and it is carefully validated against analytical solutions, third party software and measurements of the fabricated devices. It looks like it is developed by the team of gmsh mesh generator.

### SU2

[SU2](https://su2code.github.io/) is a collection of software tools developed in C++ and Python for the solution of [partial differential equations](https://en.wikipedia.org/wiki/Partial_differential_equation) (PDE) and PDE-constrained optimization problems on unstructured meshes. It is particularly used in the fields of aerodynamics and computational fluid dynamics (CFD).

### Technog

Technog Professional is a closed source program to perform geotechnical simulations such as landslides, driving piles, slope stability, and civil engineering calculations (masonry and earthquake response), [website](http://www.feat.nl/) (broken link).

Technog was successfully used in FreeCAD as a substitute of CalculiX, although the trial version is limited in the number of elements it can handle: [Integration of tochnog solver in FreeCAD FEM (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=26772).

### XC

[XC](http://www.xcengineering.xyz/) is a FEA program designed to solve structural problems in civil engineering like real beam shell analysis. Internally it uses the OpenSees libraries: [main repository](https://github.com/xcfem/xc), [XC, opensource structural engineering FEM code (forum topic)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31262).


{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Solver/it
