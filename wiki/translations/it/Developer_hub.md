# <img alt="" src=images/Crystal_Clear_app_tutorials.png  style="width:64px;"> Developer hub/it



Questo è il posto giusto per contribuire allo sviluppo del software di FreeCAD.

Queste pagine sono in fase iniziale di sviluppo. Se non è possibile trovare le informazioni cercate, o se da altre parti si trovano informazioni utili non collegate, si prega di lasciare un commento nella pagina delle [discussioni nel forum](http://forum.freecadweb.org/index.php?sid=5f84150e79db8842e277b042077097ff) in modo che qualcuno se ne possa occupare (oppure, modificare direttamente questa pagina).



## Documentazione per gli sviluppatori 

La documentazione per gli sviluppatori comprende le seguenti sezioni:



### Compilare FreeCAD 

-   [Github repo](https://github.com/FreeCAD/FreeCAD). Se sei nuovo su git, leggi [Gestione del codice sorgente](Source_code_management/it.md)
-   [Compilazione con Docker](Compile_on_Docker/it.md)
-   [Compilare in Windows](Compile_on_Windows/it.md)
-   [Compilare in Linux](Compile_on_Linux/it.md)
-   [Compilare in MacOS](Compile_on_MacOS/it.md)
-   [Licenze](License/it.md) - Dettagli sulle licenze FreeCAD
-   [Librerie di terze parti](Third_Party_Libraries/it.md)
-   [Strumenti di terze parti](Third_Party_Tools/it.md)
-   [Avvio e configurazione](Start_up_and_Configuration/it.md)
-   [Documentazione del codice sorgente](Source_documentation/it.md)
-   Usare il [bug Tracker](Tracker/it.md) quando quando si ha un problema o si pensa di aver trovato un bug

### Packaging

Il [Packaging](Packaging/it.md) consiste nel prendere i binari compilati e i file sorgente di Python di FreeCAD e distribuirli per l\'uso in un particolare sistema.

-   [Linux packaging](Linux_packaging.md)
    -   [Debian development](Debian_development.md)
    -   [Debian Unstable](Debian_Unstable.md)
    -   [Git buildpackage](Git_buildpackage.md)
-   [Windows packaging](Windows_packaging.md)
-   [MacOS packaging](MacOS_packaging.md)



### Costruire Strumenti di Supporto 

-   [Strumenti per costruire FreeCAD](FreeCAD_Build_Tool/it.md)
    -   [Creare un Ambiente di lavoro](Workbench_creation/it.md) a FreeCAD
-   [Mettere a punto](Debugging/it.md) FreeCAD
-   [Testare](Testing/it.md) FreeCAD
-   [Compilare FreeCAD in modo veloce](Compiling_(Speeding_up)/it.md)
-   [Integrazione continua](Continuous_Integration/it.md)



### Modificare FreeCAD 

-   Comprendere il [Codice sorgente di FreeCAD](The_FreeCAD_source_code/it.md)
-   [Inviare patch](Tracker/it#Inviare_patch.md)
-   Aggiungere [Funzioni](Gui_Command/it.md) a FreeCAD o a un Ambiente di lavoro
-   [Marchiare e Personalizzare](Branding/it.md), oppure *come dare un aspetto uniforme a FreeCAD*
-   [Materiale grafico](Artwork/it.md) creato per FreeCAD, liberamente riutilizzabile
-   [Linee guida](Artwork_Guidelines/it.md) standard per le icone
-   [Tradurre FreeCAD](Localisation/it.md), le voci dell\'interfaccia grafica
-   [Moduli extra in Python](Extra_python_modules/it.md), o *come estendere le funzionalità di python all\'interno FreeCAD*
-   [Google Summer of Code](Google_Summer_of_Code.md) get involved via Google\'s student support program
-   [Fine-tuning](Fine-tuning/it.md) Mostra varie regolazioni e impostazioni che è possibile utilizzare per perfezionare l\'installazione di FreeCAD o per risolvere determinati problemi
-   [Wrapping a C++ class in Python](Wrapping_a_Cplusplus_class_in_Python.md) mostra come creare il wrapper Python per una classe C++
-   [Lista di controllo per l\'aggiunta di una caratteristica ad un ambiente C++](NewFeatureCheckList_C++.md) fornisce un aiuto per i contributori.

-   [Traduzione di un ambiente esterno](Translating_an_external_workbench/it.md)



### Guida per gli sviluppatori del modulo 

[FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide): Si tratta di un ebook in fase di scrittura su GitHub, si prega di creare una biforcazione e di inviare una richiesta di pull per contribuire.

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



### Moduli interni 



#### Documentazione di OpenCascade 

OpenCascade è una piattaforma di sviluppo software per la modellazione 3D di superfici e solidi, lo scambio di dati CAD e la visualizzazione, principalmente sotto forma di librerie C++.

-   [Roman Lygin\'s tutorials](http://opencascade.wikidot.com/romansarticles)
-   [Full Online Documentation](https://dev.opencascade.org/doc/overview/html/index.html)
-   [Reference Manual](https://dev.opencascade.org/doc/refman/html/index.html)
-   [Il wiki di openCascade](http://opencascade.wikidot.com)



#### Formato dei file 

[Formato dei file FCStd](File_Format_FCStd/it.md). I file creati con FreeCAD sono file `.zip` che includono la geometria [BREP](https://en.wikipedia.org/wiki/Boundary_representation), nonché i dati XML che descrivono il documento.



#### Solutore di Sketcher 

-   [Sketcher Solver Architecture Booklet](https://forum.freecadweb.org/viewtopic.php?f=10&t=36355) (forum thread), [source](https://github.com/abdullahtahiriyo/FreeCADBooks/tree/master/FreeCAD_Solver_Architecture) in GitHub.
-   [PlaneGCS solver](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/) in the FreeCAD source code; important files are [GCS.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/GCS.cpp) and [SubSystem.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/SubSystem.cpp).
-   [Recent Several Sketcher improvements](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192).

Il risolutore di sketcher non è perfetto, in quanto vi sono alcuni problemi con la precisione numerica quando si utilizzano valori elevati, vedere [Adventure of fixing sketcher solver for large sketches](https://forum.freecadweb.org/viewtopic.php?f=10&t=40502).

Lo sviluppo di una nuova architettura di risolutore potrebbe migliorare il modo in cui il risolutore viene utilizzato sia in [Sketcher](Sketcher_Workbench/it.md), sia per l\'assemblaggio di corpi 3D. Vedere [Reimplementing constraint solver](https://forum.freecadweb.org/viewtopic.php?f=20&t=40525).



## Mappa delle fasi di sviluppo 

Anche se già utilizzabile in diverse parti, FreeCAD è solo all\'inizio di un lungo cammino nell\'ambiente del CAD.

Serve ancora molto lavoro prima che possa competere con i software commerciali.

[FreeCAD 1.0 Development Cycle](FreeCAD_1.0_Development_Cycle.md)

## Community

-   [IRC channel](ircs://irc.libera.chat:6697/freecad) ,synchronized with [gitter channel](https://gitter.im/FreeCAD/FreeCAD)
-   [Development forum](https://forum.freecad.org/viewforum.php?f=6)

-   [Piano di sviluppo](Development_roadmap/it.md)

## Crediti

[ Collaboratori](Contributors/it.md)



---
⏵ [documentation index](../README.md) > [Hubs](Category_Hubs.md) > [Developer Documentation](Category_Developer Documentation.md) > Developer hub/it
