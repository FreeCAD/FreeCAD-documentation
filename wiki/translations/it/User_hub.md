# User hub/it
{{TOCright}} <img alt="" src=images/User_hub.png  style="width:64px;">



Questa è l\'area principale di aiuto per i nuovi utenti di FreeCAD.

FreeCAD è in continuo sviluppo, quindi potrebbero esserci informazioni mancanti o obsolete. Se non riuscite a trovare le informazioni di cui avete bisogno, non esitate a chiedere nel [forum di FreeCAD](https://forum.freecadweb.org).

Se vuoi contribuire a FreeCAD, per favore [dona](donate/it.md), e vedi la pagina [Aiuto FreeCAD](Help_FreeCAD/it.md) per contribuire in altro modo. Se vuoi modificare questo wiki, richiedi un account wiki con i permessi dell\'editor [nel forum](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830), e leggi le [WikiPages](WikiPages.md) per le linee guida generali che dovresti seguire.

Se volete sapere come anni fa è iniziato lo sviluppo di FreeCAD visitate la pagina [History](History/it.md).



## Utilizzare FreeCAD 



### Introduzione

-   [Panoramica sull\'applicazione](About_FreeCAD/it.md): Informazioni generali su FreeCAD
-   Come installare FreeCAD in [Windows](Install_on_Windows/it.md), [Linux](Install_on_Linux/it.md) e [Mac](Install_on_Mac/it.md)
-   [Installazione dei file della guida](Installing_Helpfile/it.md): come installare la documentazione offline basata su questo wiki.
-   [Installare componenti aggiuntivi](Installing_additional_components/it.md): come installare componenti aggiuntivi di terze parti che possono essere utilizzati con FreeCAD.
-   [Per iniziare](Getting_started/it.md): Una veloce panoramica degli strumenti disponibili
-   [FAQ](Frequently_asked_questions/it.md): Domande più frequenti
-   [Tutorial](Tutorials/it.md) che coprono diverse parti di FreeCAD



#### Migrare da altro software? 

-   [Workarounds](Workarounds.md)
-   [Migrare in FreeCAD da Fusion360](Migrating_to_FreeCAD_from_Fusion360/it.md)
-   [Migrare in FreeCAD da OnShape](Migrating_to_FreeCAD_from_OnShape/it.md)
-   [Migrare in FreeCAD da SolidWorks](Migrating_to_FreeCAD_from_SolidWorks.md)
-   [Migrare in FreeCAD da Revit](Migrating_to_FreeCAD_from_Revit.md)
-   [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [tabella di compatibilità delle applicazioni BIM](BIM_application_compatibility_table/it.md)



### Concetti base dell\'applicazione 

-   [Interfaccia](Interface/it.md): l\'interfaccia di FreeCAD è composta da vari elementi grafici sullo schermo, inclusi la [vista 3D](3D_view/it.md), l\'[albero della struttura](Tree_view/it.md), l\'[editor delle proprietà](Property_editor/it.md), il [pannello delle azioni](Task_panel/it.md), e la [console Python](Python_console/it.md).
-   [Navigazione con il mouse](Mouse_navigation/it.md): i diversi tipi di utilizzo del mouse o del trackpad per navigare nella vista 3D.
-   [Metodi di selezione](Selection_methods/it.md): i diversi metodi di selezione degli oggetti nel software.
-   [Denominazione degli oggetti](Object_name/it.md): gli oggetti FreeCAD hanno un nome `Name` di sola lettura che li identifica in modo univoco e una etichetta `Label` che è modificabile dall\'utente.
-   [Editor delle preferenze](Preferences_Editor/it.md): il sistema che consente di controllare molte proprietà del sistema di base e dei singoli ambienti di lavoro.
-   [Formati di file](Import_Export/it.md): i diversi formati di file che FreeCAD può leggere e scrivere.



### Ambienti di lavoro 

Gli [ambienti di lavoro](Workbenches/it.md) sono raccolte di strumenti che vengono utilizzate per specifiche attività. Questi sono gli ambienti di lavoro di base presenti fin da subito dopo ogni installazione di FreeCAD:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Standard tools](Std_Base.md). Questi comandi e strumenti sono presenti in tutti gli ambienti.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Ambiente Architettura](Arch_Workbench/it.md) per lavorare con elementi architettonici.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Ambiente Draft](Draft_Workbench/it.md) contiene strumenti 2D e operazioni CAD 2D e 3D di base.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [Ambiente FEM](FEM_Workbench/it.md) fornisce un flusso di lavoro di analisi agli elementi finiti (FEA).

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> [Ambiente Inspection](Inspection_Workbench/it.md) è realizzato per fornirti strumenti specifici per l\'esame delle forme. È ancora nelle prime fasi di sviluppo.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> [Ambiente Mesh](Mesh_Workbench/it.md) per lavorare con maglie triangolari.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> [Ambiente OpenSCAD](OpenSCAD_Workbench/it.md) per l\'interoperabilità con OpenSCAD e la riparazione della cronologia del modello della [geometria solida costruttiva](constructive_solid_geometry/it.md) (CSG).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Ambiente Part](Part_Workbench/it.md) per lavorare con primitive geometriche ed operazioni booleane.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [Ambiente Part Design](PartDesign_Workbench/it.md) per la costruzione di forme di parti da schizzi.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> [Ambiente Path](Path_Workbench/it.md) viene utilizzato per produrre istruzioni G-Code.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> [Ambiente Punti](Points_Workbench/it.md) per lavorare con nuvole di punti.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> [Ambiente Ingegneria inversa](Reverse_Engineering_Workbench/it.md) ha lo scopo di fornire strumenti specifici per convertire forme/solidi/mesh in forme parametriche compatibili con FreeCAD.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> [ Ambiente Robot](Robot_Workbench/it.md) per lo studio dei movimenti dei robot. Attualmente non mantenuto.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Ambiente Sketcher](Sketcher_Workbench/it.md) per lavorare con schizzi a geometria vincolata.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> [Ambiente Foglio di calcolo](Spreadsheet_Workbench/it.md) per la creazione e la manipolazione di dati in un foglio di calcolo.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> [Ambiente Start](Start_Workbench/it.md) consente di passare rapidamente agli ambienti di lavoro più comuni.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> [Ambiente Superficie](Surface_Workbench/it.md) fornisce strumenti per creare e modificare le superfici. È simile al [Part Builder](Part_Builder/it.md) con l\'opzione faccia dai bordi.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> [Ambiente TechDraw](TechDraw_Workbench/it.md) per la produzione di disegni tecnici da modelli 3D.

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> [Ambiente di Test](Testing/it.md) serve per il debug di FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> [Ambiente Web](Web_Workbench/it.md) fornisce una finestra del browser invece della [vista 3D](3D_view/it.md) all\'interno di FreeCAD.



### Macro

Le [macro](Macros/it.md) sono frammenti relativamente piccoli di codice [Python](Python/it.md) che eseguono un\'attività semplice o complessa che non è disponibile nel sistema FreeCAD di base.

Gli utenti esperti hanno anche scritto varie [macro](macros/it.md) per migliorare le capacità di FreeCAD.

Da FreeCAD 0.17 molte macro possono essere installate usando [Addon Manager](Std_AddonMgr/it.md). Per un elenco delle macro fare riferimento alla pagina [Raccolta di macro](Macros_recipes/it.md). Per installare manualmente le macro fare riferimento al tutorial [Come installare le macro](How_to_install_macros/it.md).



### Ambienti esterni 

Quando molte macro o funzioni vengono sviluppate insieme e organizzate in barre degli strumenti e menu, possono diventare un nuovo ambiente di lavoro.

Gli [ambienti esterni](External_workbenches/it.md) sono raccolte di funzioni che non fanno parte del sistema FreeCAD di base, generalmente sviluppate da utenti esperti e che si rivolgono a un\'esigenza particolare.

Da FreeCAD 0.17 molti ambienti possono essere installati usando [Addon Manager](Std_AddonMgr/it.md). Per l\'installazione manuale di questi ambienti fare riferimento al tutorial [Come installare ambienti aggiuntivi](How_to_install_additional_workbenches/it.md).



## Riferimenti

-   [Elenco dei comandi](List_of_Commands/it.md): Una lista completa dei comandi disponibili in FreeCAD.



## Aiuto in linea 

Questa è la guida ufficiale di FreeCAD online. Si prega di notare che l\'intero sistema della Guida in linea è attualmente in rilavorazione. Sarà usata per generare un file .CHM, che verrà distribuito con i pacchetti binari di FreeCAD. Al momento la guida in linea riassume alcune delle sezioni più complete di questo wiki.

-   [ Aiuto in linea - Indice dei contenuti](Online_Help_Toc/it.md)



## Altro

-   Il [Power users hub](Power_users_hub/it.md) è il riferimento per vedere un uso più avanzato di FreeCAD
-   Il [Portale della comunità](FreeCAD_Community_Portal/it.md) elenca i progetti realizzati dai membri della comunità di FreeCAD.
-   Non capite come viene usato un termine o una frase in FreeCAD? Provate a guardare la pagina [Glossario](Glossary/it.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/it
