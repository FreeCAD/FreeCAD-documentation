# <img alt="L\'icona dell\'ambiente FEM" src=images/Workbench_FEM.svg  style="width:64px;"> FEM Workbench/it


{{TOCright}}

## Introduzione

L\'[Ambiente FEM](FEM_Workbench/it.md) offre a FreeCAD un moderno flusso di lavoro per [l\'analisi agli elementi finiti](https://it.wikipedia.org/wiki/Metodo_degli_elementi_finiti) (FEA). Questo significa che tutti gli strumenti per fare una analisi degli elementi finiti sono combinati in una GUI.

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">

## Flusso di lavoro 

I passaggi per effettuare un\'analisi ad elementi finiti sono:

1.  Preelaborazione: impostazione del problema di analisi.
    1.  Modellazione della geometria: creazione della geometria con FreeCAD o importazione da una diversa applicazione.
    2.  Creare una analisi.
        1.  Aggiungere i vincoli di simulazione quali i carichi e i supporti al modello da analizzare.
        2.  Aggiungere i materiali alle parti del modello geometrico.
        3.  Creare un elemento mesh finito per il modello geometrico o importarlo da una diversa applicazione.
2.  Risoluzione: eseguire usando un risolutore esterno dall\'interno di FreeCAD.
3.  Postelaborazione: visualizzare i risultati dell\'analisi dall\'interno di FreeCAD, o esportare i risultati in modo che possano essere postelaborati con un\'altra applicazione.

Il modulo FEM può essere usato su piattaforme Windows, Mac OSX e Linux. Dato che il modulo FEM utilizza un risolutore esterno, la quantità di interventi manuali dipende dal sistema operativo che si sta utilizzando. Consultare la pagina [Installare FEM](FEM_Install/it.md) per le istruzioni sulla configurazione degli strumenti esterni.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;">



*Flusso di lavoro del Workbench FEM; il workbench chiama due programmi esterni per eseguire il meshing di un oggetto solido e risolvere il problema degli elementi finiti*

## Menu Modello 

-   <img alt="" src=images/Fem_Analysis.svg  style="width:32px;"> [Contenitore analisi](FEM_Analysis/it.md): Crea un nuovo contenitore per una analisi meccanica statica. Se invece, prima di cliccare su questo strumento, viene selezionato un solido nella vista ad albero si apre la finestra di meshing.

### Materiali

-   <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;">[Materiale FEM per solidi](FEM_MaterialSolid/it.md): Consente di selezionare un materiale dal database.

-   <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Materiale FEM per fluidi](FEM_MaterialFluid/it.md): Consente di selezionare un materiale dal database.

-   <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Materiale non lineare](FEM_MaterialMechanicalNonlinear/it.md): Consente di selezionare un materiale dal database.

-   <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [ Materiale rinforzato (calcestruzzo)](FEM_MaterialReinforced/it.md): Consente di selezionare dal database i materiali rinforzati costituiti da una matrice e da un rinforzo.

-   <img alt="" src=images/FEM_MaterialEditor.svg  style="width:32px;"> [Editor dei materiali](FEM_MaterialEditor/it.md): Consente di aprire l\'editor dei materiali per modificare i materiali.

### Geometria dell\'elemento 

-   <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Sezione trasversale di trave](FEM_ElementGeometry1D/it.md): Utilizzato per definire le sezioni trasversali per gli elementi trave.

-   <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Rotazione di trave](FEM_ElementRotation1D/it.md): Utilizzato per ruotare le sezioni trasversali degli elementi trave.

-   <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Spessore di una lastra](FEM_ElementGeometry2D/it.md): Utilizzato per definire lo spessore dell\'elemento lastra.

-   <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Sezione del fluido per flusso 1D](FEM_ElementFluid1D/it.md): Utilizzato per creare un elemento sezione del fluido FEM per reti pneumatiche e idrauliche.

### Vincoli elettrostatici 

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Vincolo Potenziale elettrostatico](FEM_ConstraintElectrostaticPotential/it.md): Utilizzato per la definizione del potenziale elettrostatico.

### Vincoli dei fluidi 

-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Vincolo velocità iniziale del flusso](FEM_ConstraintInitialFlowVelocity/it.md): Utilizzato per definire una velocità di flusso iniziale per il corpo.

-   <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Vincolo pressione iniziale](FEM_ConstraintInitialPressure.md): Utilizzato per definire una pressione iniziale per il corpo. {{Version/it|1.0}}

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Vincolo velocità del flusso](FEM_ConstraintFlowVelocity/it.md): Utilizzato per definire una velocità del flusso come condizione di un contorno su un bordo (2D) o una faccia (3D).

### Vincoli geometrici 

-   <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Vincolo piano di rotazione](FEM_ConstraintPlaneRotation/it.md): Utilizzato per definire un vincolo piano di rotazione su una faccia piana.

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Stampa sezione dei vincoli](FEM_ConstraintSectionPrint/it.md): Utilizzato per stampare le variabili di output facciale predefinite (forze e momenti) nel file dat. {{Version/it|0.19}}

-   <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Vincolo trasforma](FEM_ConstraintTransform/it.md): Utilizzato per definire un vincolo di trasformazione su una faccia.

### Vincoli meccanici 

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Vincolo fissaggio](FEM_ConstraintFixed/it.md): Utilizzato per definire un vincolo di fissaggio su un punto, bordo o faccia (e).

-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [ Vincolo di dislocamento](FEM_ConstraintDisplacement/it.md): Utilizzato per definire un vincolo di dislocamento su un punto, bordo o faccia (e).

-   <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Vincolo contatto](FEM_ConstraintContact/it.md): Utilizzato per definire un vincolo contatto tra due facce.

-   <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Legame di vincolo](FEM_ConstraintTie/it.md): Utilizzato per definire un vincolo di collegamento (\"contatto vincolato\") tra due facce. {{Version/it|0.19}}

-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Vincolo molla](FEM_ConstraintSpring/it.md): utilizzato per definire una molla. {{Version/it|0.20}}

-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Vincolo forza](FEM_ConstraintForce/it.md): Utilizzato per definire una forza in N applicata uniformemente ad una faccia selezionabile, nella direzione definibile.

-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Vincolo pressione](FEM_ConstraintPressure/it.md): Utilizzato per definire un vincolo pressione.

-   <img alt="" src=images/FEM_ConstraintCentrif.svg  style="width:32px;"> [Vincolo centrifugo](FEM_ConstraintCentrif/it.md): Utilizzato per definire un vincolo di carico centrifugo sul corpo. {{Version/it|0.20}}

-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Vincolo peso proprio](FEM_ConstraintSelfWeight/it.md): Utilizzato per definire una accelerazione di gravità che agisce su un modello.

### Vincoli termici 

-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Vincolo temperatura iniziale](FEM_ConstraintInitialTemperature/it.md): Utilizzato per definire un vincolo di temperatura iniziale di un corpo.

-   <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Vincolo scambio termico](FEM_ConstraintHeatflux/it.md): Utilizzato per definire un vincolo di scambio termico su una faccia (e).

-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Vincolo temperatura](FEM_ConstraintTemperature/it.md): Utilizzato per definire un vincolo di temperatura limite su un punto, bordo o faccia (e).

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Vincolo fonte di calore del corpo](FEM_ConstraintBodyHeatSource/it.md): Utilizzato per definire un calore corporeo generato internamente.

### Vincoli senza solutore 

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Condizione limite del fluido](FEM_ConstraintFluidBoundary/it.md): Utilizzato per definire una condizione al contorno del fluido.

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Vincolo cuscinetto](FEM_ConstraintBearing/it.md): Utilizzato per definire un vincolo cuscinetto.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Vincolo ingranaggio](FEM_ConstraintGear/it.md): Utilizzato per definire un vincolo di ingranaggio.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Vincolo puleggia](FEM_ConstraintPulley/it.md): Utilizzato per definire un vincolo puleggia.

### Sovrascrivere le costanti 

-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Permittività del vuoto costante](FEM_ConstantVacuumPermittivity/it.md): Utilizzato per sovrascrivere la [costante dielettrica del vuoto](https://it.wikipedia.org/wiki/Costante_dielettrica_del_vuoto) con un valore personalizzato. {{Version/it|0.19}}

## Menu Mesh 

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [Mesh FEM da forma con Netgen](FEM_MeshNetgenFromShape/it.md): Genera una mesh a elementi finiti per un modello utilizzando Netgen.

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [Mesh FEM da forma con Gmsh](FEM_MeshGmshFromShape/it.md): Genera una mesh agli elementi finiti per un modello usando Gmsh.

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [Strato limite di mesh FEM](FEM_MeshBoundaryLayer/it.md): Crea mesh anisotrope per calcoli accurati vicino ai confini.

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [Regione di mesh FEM](FEM_MeshRegion/it.md): Crea una o più aree localizzate da meshare in modo da ottimizzare il tempo di analisi.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [Gruppo di mesh FEM](FEM_MeshGroup/it.md): Raggruppa ed etichetta insieme gli elementi di una mesh (vertice, bordo, superficie), utile per esportare la mesh a solutori esterni.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [ Imposta i nodi](FEM_CreateNodesSet/it.md): Crea o definisce un set di nodi da mesh FEM.

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [Converti mesh FEM in mesh](FEM_FemMesh2Mesh/it.md): Converte la superficie di una mesh FEM in una mesh.

## Menu Solutore 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solutore Calculix Standard](FEM_SolverCalculixCxxtools/it.md): Crea un nuovo solutore per questa analisi. Nella maggior parte dei casi viene creato il risolutore unitamente all\'analisi.

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Solutore CalculiX (nuovo framework)](FEM_SolverCalculiX/it.md):

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solutore Elmer](FEM_SolverElmer/it.md): Crea il controller del risolutore per Elmer. È indipendente da altri oggetti del risolutore.

-   <img alt="" src=images/_FEM_SolverMystran.svg  style="width:32px;"> [Solver Mystran](FEM_SolverMystran/it.md): {{Version/it|0.20}}

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Solutore Z88](FEM_SolverZ88/it.md): crea il controller del risolutore per Z88. È indipendente da altri oggetti risolutore.

-   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Equazione di elasticità](FEM_EquationElasticity/it.md): Equazione per il [Solver Elmer](FEM_SolverElmer.md) <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> per eseguire analisi meccaniche.

-   <img alt="" src=images/_FEM_EquationElectricforce.svg  style="width:32px;"> [Equazione Electricforce](FEM_EquationElectricforce/it.md): Equazione per il [Solver Elmer](FEM_SolverElmer.md) <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> per calcolare la forza elettrica sulle superfici. {{Version/it|0.19}}

-   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Equazione elettrostatica](FEM_EquationElectrostatic/it.md): Equazione per il [Solver Elmer](FEM_SolverElmer.md) <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> per eseguire analisi elettrostatiche.

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Equazione di flusso](FEM_EquationFlow/it.md): Equazione per il [Solver Elmer](FEM_SolverElmer.md) <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> per eseguire analisi di flusso.

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Equazione di flusso](FEM_EquationFlux/it.md): Equazione per il [Solver Elmer](FEM_SolverElmer.md) <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> per eseguire analisi di flusso.

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Equazione del calore](FEM_EquationHeat/it.md): Equazione per il [Solver Elmer](FEM_SolverElmer.md) <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> per eseguire analisi di trasferimento di calore.

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Controlli del solutore](FEM_SolverControl/it.md): Apre il menu per regolare e avviare il risolutore selezionato.

-   <img alt="" src=images/Fem-run-solver.svg  style="width:32px;"> [Avvia il solutore](FEM_SolverRun/it.md): Avvia il risolutore selezionato per l\'analisi attiva.

## Menu Risultati 

-   <img alt="" src=images/Fem-purge-results.svg  style="width:32px;"> [Azzera risultati](FEM_ResultsPurge/it.md): Cancella i risultati dell\'analisi attiva.

-   <img alt="" src=images/Fem-result.svg  style="width:24px;"> [Mostra i risultati](FEM_ResultShow/it.md): Visualizza i risultati di un\'analisi.

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Applicare le modifiche alla pipeline](FEM_PostApplyChanges/it.md): si attiva/disattiva se le modifiche alle pipeline e ai filtri vengono applicate immediatamente.

-   <img alt="" src=images/_FEM_PostPipelineFromResult.svg  style="width:32px;"> [Post pipeline dal risultato](FEM_PostPipelineFromResult/it.md): utilizzato per aggiungere una nuova rappresentazione grafica dei risultati dell\'analisi FEM (scala di colori e più opzioni di visualizzazione).

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Filtro di curvatura](FEM_PostFilterWarp/it.md): utilizzato per visualizzare la forma deformata in scala del modello.

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Filtro taglio scalare](FEM_PostFilterClipScalar/it.md): utilizzato per ritagliare un campo con un valore scalare specificato.

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Filtro taglio con funzione](FEM_PostFilterCutFunction/it.md): utilizzato per visualizzare i risultati su una sfera o un piano che attraversa il modello.

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Post Crea filtro di taglio](FEM_PostFilterClipRegion/it.md): utilizzato per ritagliare un campo con una sfera o un piano che attraversa il modello.

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Post crea filtro dati lungo la linea](FEM_PostFilterDataAlongLine/it.md): utilizzato per tracciare i valori di un campo lungo una linea specificata.

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Grafico di linearizzazione della sollecitazione](FEM_PostFilterLinearizedStresses/it.md): crea un grafico di linearizzazione delle sollecitazioni.

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Filtro di taglio dei dati in un punto](FEM_PostFilterDataAtPoint/it.md): utilizzato per visualizzare il valore di un campo selezionato in un determinato punto.

-   <img alt="" src=images/FEM_CompPostCreateFunctions.png  style="width:48px;"> [Funzioni di filtro](FEM_PostCreateFunctions/it.md): Questo è un menu a icone nella barra degli strumenti Risultati FEM che contiene i seguenti comandi:

  - <img alt="" src=images/Fem-post-geo-plane.svg  style="width:32px;"> [Piano della funzione di filtro](FEM_PostCreateFunctionPlane/it.md): Definisce che la mesh risultante viene tagliata con un piano.

  - <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:32px;"> [Sfera della funzione filtro](FEM_PostCreateFunctionSphere/it.md): Definisce che la mesh risultante viene tagliata con una sfera.

## Menu: Utilità 

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Piano di taglio di ritaglio sulla faccia](FEM_ClippingPlaneAdd/it.md): Aggiunge un piano di taglio per l\'intera vista del modello.

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Rimuovi tutti i piani di taglio](FEM_ClippingPlaneRemoveAll/it.md): Rimuove tutti i [piani di taglio](FEM_ClippingPlaneAdd/it.md) esistenti.

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [Apre gli esempi di FEM](FEM_Examples/it.md): Apre la GUI per accedere agli esempi FEM.

## Menu contestuale 

-   <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [Cancella mesh FEM](FEM_MeshClear/it.md): Elimina il file mesh dal file FreeCAD. Utile per alleggerire un file di FreeCAD.

-   <img alt="" src=images/_FEM_MeshDisplayInfo.svg  style="width:32px;"> [Visualizza info mesh FEM](FEM_MeshDisplayInfo/it.md): Visualizza le statistiche di base della mesh esistente - numero di nodi ed elementi di ogni tipo.

## Preferenze

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferenze\...](FEM_Preferences/it.md): Preferenze disponibili per gli strumenti FEM.

## Informazioni

Le seguenti pagine spiegano diversi argomenti dell\'ambiente FEM.

[FEM Install](FEM_Install/it.md): una descrizione dettagliata su come impostare i programmi esterni utilizzati in questo ambiente.

[Mesh FEM](FEM_Mesh/it.md): ulteriori informazioni su come ottenere una mesh per l\'analisi degli elementi finiti.

[FEM Solver](FEM_Solver/it.md): ulteriori informazioni sui diversi solutori disponibili nel workbench e quelli che potrebbero essere utilizzati in futuro.

[FEM CalculiX](FEM_CalculiX/it.md): ulteriori informazioni su CalculiX, il solutore predefinito utilizzato nel workbench per l\'analisi strutturale.

[FEM Concrete](FEM_Concrete/it.md): informazioni interessanti sul tema della simulazione di strutture in calcestruzzo.

## Tutorial

Tutorial 1: [FEM CalculiX Trave a sbalzo 3D](FEM_CalculiX_Cantilever_3D/it.md); analisi di base di una trave.

Tutorial 2: [Tutorial di FEM](FEM_tutorial/it.md); semplice analisi della tensione di una struttura.

Tutorial 3: [FEM Tutorial Python](FEM_Tutorial_Python/it.md); esempio di configurazione della trave a sbalzo interamente attraverso lo scripting in Python, inclusa la mesh.

Tutorial 4: [Taglio FEM di un blocco composito](FEM_Shear_of_a_Composite_Block/it.md); vedere la deformazione di un blocco composto da due materiali.

Tutorial 5: [Analisi FEM transitoria](Transient_FEM_analysis/it.md)

Tutorial 6: [Post-elaborazione dei risultati FEM con Paraview](Post-Processing_of_FEM_Results_with_Paraview/it.md)

Tutorial 7: [FEM Example Capacitance Two Balls](FEM_Example_Capacitance_Two_Balls/it.md); Elmer\'s GUI tutorial 6 \"Electrostatics Capacitance Two Balls\" using FEM Examples.

Tutorial di analisi meccaniche termiche di [openSIM](https://opensimsa.github.io/training.html)

Video Tutorial 1: [Articolo nel forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353) (con il link YouTube)

Video Tutorial 2: [Articolo nel forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321) (con il link YouTube)

Altri tutorial video: [anisim Open Source Engineering Software](https://www.youtube.com/channel/UCnvFCm2BbXOVI3ObfXcxXhw) (in tedesco).

## Estendere l\'ambiente FEM 

L\'ambiente FEM è in costante sviluppo. Un obiettivo del progetto è trovare i modi per interagire facilmente con i vari solutori FEM, in modo che l\'utente finale possa semplificare il processo di creazione, meshing, simulazione e ottimizzazione di un problema di progettazione tecnica, tutto in FreeCAD.

Le seguenti informazioni sono rivolte agli utenti esperti e agli sviluppatori che desiderano estendere l\'ambiente FEM in modi diversi. Serve avere familiarità con C++ e Python, ed è anche necessaria una certa conoscenza del sistema \"document object\" utilizzato in FreeCAD; queste informazioni sono disponibili nella [documentazione per utenti esperti](Power_users_hub/it.md) e nella [documentazione per gli sviluppatori](Developer_hub/it.md). Notare che, poiché FreeCAD è in fase di sviluppo attivo, alcuni articoli potrebbero essere vecchi e quindi obsoleti. Le informazioni più aggiornate sono discusse nel [forum di FreeCAD](https://forum.freecadweb.org/index.php), nella sezione Development. Per discussioni, consigli o assistenza FEM sull\'estensione dell\'ambiente, il fare riferimento al [subforum FEM](https://forum.freecadweb.org/viewforum.php?f=18).

I seguenti articoli spiegano come è possibile estendere il workbench, ad esempio aggiungendo nuovi tipi di condizioni (vincoli) o equazioni.

-   [Estendere il modulo FEM](Extend_FEM_Module/it.md)
-   [Integrazione degli sviluppatori FEM](Onboarding_FEM_Devs/it.md) tenta di orientare i nuovi sviluppatori su come contribuire all\'ambiente di lavoro FEM.
-   [Tutorial Aggiungere equazioni FEM](Add_FEM_Equation_Tutorial/it.md)
-   [Tutorial Aggiungere vincoli FEM](Add_FEM_Constraint_Tutorial/it.md)

Per aiutare gli utenti a comprendere la complessa base di codici di FreeCAD e le interazioni tra gli elementi principali e i singoli ambienti è stata scritta una guida per lo sviluppatore . Il libro è ospitato su github in modo che più utenti possano contribuirvi e tenerlo aggiornato.

-   [Early preview of ebook: Module developer\' guide to FreeCAD source](https://forum.freecadweb.org/viewtopic.php?t=17581) (forum thread)
-   [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) (github repository)

## Estensione della documentazione di FEM Workbench 

-   Maggiori informazioni sull\'estensione o la mancanza della documentazione FEM possono essere trovate nel forum: [FEM documentation missing on the Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [FEM](Category_FEM.md) > FEM Workbench/it
