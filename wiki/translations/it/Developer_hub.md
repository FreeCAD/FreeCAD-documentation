

![150](images/Crystal_Clear_app_tutorials.png )

Questo è il posto giusto per contribuire allo sviluppo del software di FreeCAD.

Queste pagine sono in fase iniziale di sviluppo. Se non è possibile trovare le informazioni cercate, o se da altre parti si trovano informazioni utili non collegate, si prega di lasciare un commento nella pagina delle [discussioni nel forum](http://forum.freecadweb.org/index.php?sid=5f84150e79db8842e277b042077097ff) in modo che qualcuno se ne possa occupare (oppure, modificare direttamente questa pagina).

## Developer Documentation {#developer_documentation}


<div class="mw-translate-fuzzy">

## Documentazione per gli sviluppatori {#documentazione_per_gli_sviluppatori}

La documentazione per gli sviluppatori comprende le seguenti sezioni:


</div>

### Compiling FreeCAD {#compiling_freecad}


<div class="mw-translate-fuzzy">

### Fare da soli: Compilare FreeCAD {#fare_da_soli_compilare_freecad}

-   [Gestione del codice sorgente](Source_code_management/it.md)
-   [Trovare assistenza](Tracker/it.md) per quando si ha un problema o si pensa di aver trovato un bug
-   [Compilare in Windows](Compile_on_Windows/it.md)
-   [Compilare in Linux](Compile_on_Linux/it.md)
-   [Compilare in MacOS](Compile_on_MacOS/it.md)
-   [Licence details](Licence.md) - Dettagli sulle licenze FreeCAD
-   [Librerie di terze parti](Third_Party_Libraries/it.md)
-   [Strumenti di terze parti](Third_Party_Tools/it.md)
-   [Avvio e configurazione](Start_up_and_Configuration/it.md)
-   [Documentazione del codice sorgente](Source_documentation/it.md)


</div>

### Packaging

Il [Packaging](Packaging/it.md) consiste nel prendere i binari compilati e i file sorgente di Python di FreeCAD e distribuirli per l\'uso in un particolare sistema.

-   [Linux packaging](Linux_packaging.md)
    -   [Debian development](Debian_development.md)
    -   [Debian Unstable](Debian_Unstable.md)
    -   [Git buildpackage](Git_buildpackage.md)
-   [Windows packaging](Windows_packaging.md)
-   [MacOS packaging](MacOS_packaging.md)

### Build Support Tools {#build_support_tools}


<div class="mw-translate-fuzzy">

### Costruire strumenti di supporto {#costruire_strumenti_di_supporto}

-   [Strumenti per costruire FreeCAD](FreeCAD_Build_Tool/it.md)
    -   [Aggiungere un modulo applicativo](Module_Creation/it.md) a FreeCAD
-   [Mettere a punto](Debugging/it.md) FreeCAD
-   [Testare](Testing/it.md) FreeCAD
-   [Compilare FreeCAD in modo veloce](Compiling_(Speeding_up)/it.md)
-   [Integrazione continua](Continuous_Integration/it.md)


</div>

### Modifying FreeCAD {#modifying_freecad}


<div class="mw-translate-fuzzy">

#### Modificare FreeCAD {#modificare_freecad}

-   Comprendere il [Codice sorgente di FreeCAD](The_FreeCAD_source_code/it.md)
-   [Inviare patch](Tracker/it#Inviare_patch.md)
-   Aggiungere [Funzioni](Gui_Command/it.md) a FreeCAD o a un Ambiente di lavoro
-   [Marchiare e Personalizzare](Branding/it.md), oppure *come dare un aspetto uniforme a FreeCAD*
-   [Materiale grafico](Artwork/it.md) creato per FreeCAD, liberamente riutilizzabile
-   [Linee guida](Artwork_Guidelines/it.md) standard per le icone
-   [Tradurre FreeCAD](Localisation/it.md), le voci dell\'interfaccia grafica
-   [Moduli extra in Python](Extra_python_modules/it.md), o *come estendere le funzionalità di python all\'interno FreeCAD*
-   [Google Summer of Code](Google_Summer_of_Code.md) get involved via Google\'s student support program
-   [Fine-tuning](Fine-tuning/it.md) Mostra varie regolazioni e impostazioni che è possibile utilizzare per perfezionare l\'installazione di FreeCAD o per risolvere determinati problemi.


</div>

-   [Traduzione di un ambiente esterno](Translating_an_external_workbench/it.md)

### Module developer\'s guide {#module_developers_guide}


<div class="mw-translate-fuzzy">

### Guida per gli sviluppatori del modulo {#guida_per_gli_sviluppatori_del_modulo}

[FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide): Si tratta di un ebook in fase di scrittura su GitHub, si prega di creare una biforcazione e di inviare una richiesta di pull per contribuire.


</div>

Capitoli:

-   Overview and Software Architecture
-   Source code structure
-   Base and App module
-   Gui module
-   Python wrapping
-   Modular design
-   Fem module source analysis (mixed C++ and Python)
-   Development of CFD Module (pure Python)
-   Module testing and debugging
-   Contribute code with git

L\'ultima anteprima del pdf può essere scaricata dalla [cartella dei pdf](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide/tree/master/pdf) di questo repo git

### Moduli interni {#moduli_interni}

#### Documentazione di OpenCascade {#documentazione_di_opencascade}

OpenCascade è una piattaforma di sviluppo software per la modellazione 3D di superfici e solidi, lo scambio di dati CAD e la visualizzazione, principalmente sotto forma di librerie C++.

-   [Roman Lygin\'s tutorials](http://opencascade.wikidot.com/romansarticles)
-   [Full Online Documentation](https://dev.opencascade.org/doc/overview/html/index.html)
-   [Reference Manual](https://dev.opencascade.org/doc/refman/html/index.html)
-   [Il wiki di openCascade](http://opencascade.wikidot.com)

#### Formato dei file {#formato_dei_file}


<div class="mw-translate-fuzzy">

[Formato dei file FCStd](File_Format_FCStd/it.md). I file creati con FreeCAD sono file `.zip` che includono la geometria BREP, nonché i dati XML che descrivono il documento.


</div>

#### Solutore di Sketcher {#solutore_di_sketcher}

-   [Sketcher Solver Architecture Booklet](https://forum.freecadweb.org/viewtopic.php?f=10&t=36355) (forum thread), [source](https://github.com/abdullahtahiriyo/FreeCADBooks/tree/master/FreeCAD_Solver_Architecture) in GitHub.
-   [PlaneGCS solver](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/) in the FreeCAD source code; important files are [GCS.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/GCS.cpp) and [SubSystem.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/SubSystem.cpp).
-   [Recent Several Sketcher improvements](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192).

Il risolutore di sketcher non è perfetto, in quanto vi sono alcuni problemi con la precisione numerica quando si utilizzano valori elevati, vedere [Adventure of fixing sketcher solver for large sketches](https://forum.freecadweb.org/viewtopic.php?f=10&t=40502).

Lo sviluppo di una nuova architettura di risolutore potrebbe migliorare il modo in cui il risolutore viene utilizzato sia in [Sketcher](Sketcher_Workbench/it.md), sia per l\'assemblaggio di corpi 3D. Vedere [Reimplementing constraint solver](https://forum.freecadweb.org/viewtopic.php?f=20&t=40525).

## Roadmap


<div class="mw-translate-fuzzy">

## Mappa delle fasi di sviluppo {#mappa_delle_fasi_di_sviluppo}

Anche se già utilizzabile in diverse parti, FreeCAD è solo all\'inizio di un lungo cammino nell\'ambiente del CAD.

Serve ancora molto lavoro prima che possa competere con i software commerciali.


</div>

[0.20 Development Cycle](0.20_Development_Cycle.md)

## Community

-   [IRC channel](irc://chat.freenode.net/freecad) ,synchronized with [gitter channel](https://gitter.im/FreeCAD/FreeCAD)
-   [Development forum](https://forum.freecadweb.org/viewforum.php?f=6)

-   [Piano di sviluppo](Development_roadmap/it.md)

## Crediti

[ Collaboratori](Contributors/it.md)




[Category:Hubs{{\#translation:}}](Category:Hubs.md) [Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
