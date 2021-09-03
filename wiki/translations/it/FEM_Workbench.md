




<img alt="L\'icona dell\'ambiente FEM" src=images/Workbench_FEM.svg  style="width:128px;">


{{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

Il **Modulo FEM** offre a FreeCAD un moderno flusso di lavoro per [l\'analisi agli elementi finiti](https://en.wikipedia.org/wiki/Finite_element_analysis) (FEA). Questo significa che tutti gli strumenti per fare una analisi degli elementi finiti sono combinati in una GUI.


</div>

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">

## Flusso di lavoro 

I passaggi per effettuare un\'analisi ad elementi finiti sono:

1.  Preelaborazione: impostazione del problema di analisi.
    1.  Modellazione della geometria: creazione della geometria con FreeCAD o importazione da una diversa applicazione.
    2.  Creare una analisi.
        1.  Aggiungere i vincoli di simulazione quali i carichi e i supporti al modello da analizzare.
        2.  Aggiungere un materiale per il modello da analizzare.
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

-   <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [ Materiale rinforzato (calcestruzzo)](FEM_MaterialReinforced/it.md): consente di selezionare dal database i materiali rinforzati costituiti da una matrice e un rinforzo.

-   <img alt="" src=images/Arch_Material_Group.svg  style="width:32px;"> [Editor dei materiali](Material_editor/it.md): Consente di aprire l\'editor dei materiali per modificare i materiali.

### Geometria dell\'elemento 

-   <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Sezione trasversale di trave](FEM_ElementGeometry1D/it.md):

-   <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Rotazione di trave](FEM_ElementRotation1D/it.md):

-   <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Spessore di una lastra](FEM_ElementGeometry2D/it.md):

-   <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Sezione del fluido per flusso 1D](FEM_ElementFluid1D/it.md): Crea un elemento sezione del fluido FEM per reti pneumatiche e idrauliche.

### Vincoli elettrostatici 

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Potenziale elettrostatico di vincolo](FEM_ConstraintElectrostaticPotential/it.md):

### Vincoli dei fluidi 

-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Vincolo velocità iniziale del flusso](FEM_ConstraintInitialFlowVelocity/it.md): Utilizzato per definire una velocità di flusso iniziale per il dominio.

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Vincolo velocità del flusso](FEM_ConstraintFlowVelocity/it.md): Utilizzato per definire una velocità del flusso come condizione di un contorno su un bordo (2D) o una faccia (3D).

### Vincoli geometrici 

-   <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Vincolo piano di rotazione](FEM_ConstraintPlaneRotation/it.md): Serve per definire un vincolo piano di rotazione su una faccia piana.

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Stampa sezione dei vincoli](FEM_ConstraintSectionPrint/it.md): <small>(v0.19)</small> 

-   <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Vincolo trasforma](FEM_ConstraintTransform/it.md): Utilizzato per definire un vincolo di trasformazione su una faccia.

### Vincoli meccanici 

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Vincolo fissaggio](FEM_ConstraintFixed/it.md): Serve per definire un vincolo di fissaggio su un punto, bordo o faccia (e).

-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [ Vincolo di dislocamento](FEM_ConstraintDisplacement/it.md): Serve per definire un vincolo di dislocamento su un punto, bordo o faccia (e).

-   <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Vincolo contatto](FEM_ConstraintContact/it.md): Serve per definire un vincolo contatto tra due facce.

-   <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Legame di vincolo](FEM_ConstraintTie/it.md): <small>(v0.19)</small> 

-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Vincolo forza](FEM_ConstraintForce/it.md): Usato per definire una forza in N applicata uniformemente ad una faccia selezionabile, nella direzione definibile.

-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Vincolo pressione](FEM_ConstraintPressure/it.md): Usato per definire un vincolo pressione.

-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Vincolo peso proprio](FEM_ConstraintSelfWeight/it.md): Utilizzato per definire una accelerazione di gravità che agisce su un modello.

### Vincoli termici 

-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Vincolo temperatura iniziale](FEM_ConstraintInitialTemperature/it.md): Per definire un vincolo di temperatura iniziale di un corpo.

-   <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Vincolo scambio termico](FEM_ConstraintHeatflux/it.md): Per definire un vincolo di scambio termico su una faccia (e).

-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Vincolo temperatura](FEM_ConstraintTemperature/it.md): Per definire un vincolo di temperatura limite su un punto, bordo o faccia (e).

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Vincolo fonte di calore del corpo](FEM_ConstraintBodyHeatSource/it.md):

### Vincoli senza solutore 

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Condizione limite del fluido](FEM_ConstraintFluidBoundary/it.md):

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Vincolo cuscinetto](FEM_ConstraintBearing/it.md): Per definire un vincolo cuscinetto.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Vincolo ingranaggio](FEM_ConstraintGear/it.md): Per definire un vincolo ingranaggio.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Vincolo puleggia](FEM_ConstraintPulley/it.md): Per definire un vincolo puleggia.

### Sovrascrivere le costanti 

-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Permittività del vuoto costante](FEM_ConstantVacuumPermittivity/it.md): <small>(v0.19)</small> 

## Menu Mesh 

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [Mesh FEM da forma con Netgen](FEM_MeshNetgenFromShape/it.md):

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [Mesh FEM da forma con Gmsh](FEM_MeshGmshFromShape/it.md):

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [Strato limite di mesh FEM](FEM_MeshBoundaryLayer/it.md):Crea mesh anisotrope per calcoli accurati vicino ai confini.

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [Regione di mesh FEM](FEM_MeshRegion/it.md):Crea una o più aree localizzate da meshare in modo da ottimizzare il tempo di analisi.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [Gruppo di mesh FEM](FEM_MeshGroup/it.md):Raggruppa ed etichetta insieme gli elementi di una mesh (vertice, bordo, superficie), utile per esportare la mesh a solutori esterni.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [ Imposta i nodi](FEM_CreateNodesSet/it.md): Crea o definisce un set di nodi da mesh FEM.

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [Converti mesh FEM in mesh](FEM_FemMesh2Mesh/it.md): Converte la superficie di una mesh FEM in una mesh.

## Menu Solutore 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solutore Calculix Standard](FEM_SolverCalculixCxxtools/it.md): Crea un nuovo solutore per questa analisi. Nella maggior parte dei casi viene creato il risolutore unitamente all\'analisi.

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Solutore CalculiX (sperimentale)](FEM_SolverCalculiX/it.md):

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solutore Elmer](FEM_SolverElmer/it.md): Crea il controller del risolutore per Elmer. È indipendente da altri oggetti del risolutore.

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Solutore Z88](FEM_SolverZ88/it.md):

-   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Equation elasticity](FEM_EquationElasticity/it.md):

-   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Electricforce equation](FEM_EquationElectricforce.md): <small>(v0.19)</small> 

-   <img alt="" src=images/Fem-equation-electrostatic.svg  style="width:32px;"> [Equation electrostatic](FEM_EquationElectrostatic/it.md):

-   <img alt="" src=images/Fem-equation-flow.svg  style="width:32px;"> [Equation flow](FEM_EquationFlow/it.md):

-   <img alt="" src=images/Fem-equation-fluxsolver.svg  style="width:32px;"> [Equation fluxsolver](FEM_EquationFluxsolver/it.md):

-   <img alt="" src=images/Fem-equation-heat.svg  style="width:32px;"> [Equation heat](FEM_EquationHeat/it.md):

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Controlli del solutore](FEM_SolverControl/it.md): Apre il menu per regolare e avviare il risolutore selezionato.

-   <img alt="" src=images/Fem-run-solver.svg  style="width:32px;"> [Avvia il solutore](FEM_SolverRun/it.md): Avvia il risolutore selezionato per l\'analisi attiva.

## Menu Risultati 

-   <img alt="" src=images/Fem-purge-results.svg  style="width:32px;"> [Azzera risultati](FEM_ResultsPurge/it.md): Cancella i risultati dell\'analisi attiva.

-   <img alt="" src=images/Fem-result.svg  style="width:24px;"> [Mostra i risultati](FEM_ResultShow/it.md): Visualizza i risultati di un\'analisi.

-   <img alt="" src=images/FEM_PostApplyChanges.png  style="width:32px;"> [Post Applica le modifiche](FEM_PostApplyChanges/it.md):

-   <img alt="" src=images/Fem-data.svg  style="width:32px;"> [Post Mappa i colori dal risultato](FEM_PostPipelineFromResult/it.md):

-   <img alt="" src=images/Fem-warp.svg  style="width:32px;"> [Post Crea filtro vettoriale warp](FEM_PostCreateWarpVectorFilter/it.md):

-   <img alt="" src=images/Fem-clip-scalar.svg  style="width:32px;"> [Post Crea scalar clip filter](FEM_PostCreateScalarClipFilter/it.md):

-   <img alt="" src=images/Fem-cut.svg  style="width:32px;"> [Post Crea cut filter](FEM_PostCreateCutFilter/it.md):

-   <img alt="" src=images/Fem-clip.svg  style="width:32px;"> [Post Crea clip filter](FEM_PostCreateClipFilter/it.md):

-   <img alt="" src=images/Fem-DataAlongLine.svg  style="width:32px;"> [Post Crea data along line filter](FEM_PostCreateDataAlongLineFilter/it.md):

-   <img alt="" src=images/Fem-linearizedstresses.svg  style="width:32px;"> [Post Crea linearized stresses](FEM_PostCreateLinearizedStressesFilter/it.md):

-   <img alt="" src=images/fem-post-filter-data-at-point.png  style="width:32px;"> [Post Crea data at point filter](FEM_PostCreateDataAtPointFilter/it.md):

-   <img alt="" src=images/Fem_CompPostCreateFunctions.png  style="width:48px;"> [Post Crea funzioni](FEM_PostCreateFunctions/it.md):
    -   <img alt="" src=images/Fem-sphere.svg  style="width:32px;"> :
    -   <img alt="" src=images/Fem-plane.svg  style="width:32px;"> :

## Menu: Utilità 

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Piano di taglio di ritaglio sulla faccia](FEM_ClippingPlaneAdd/it.md):

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Rimuovi tutti i piani di taglio](FEM_ClippingPlaneRemoveAll/it.md):

-   <img alt="" src=images/Preferences-fem.svg  style="width:32px;"> [Esempi di FEM](FEM_Examples/it.md): Apri la GUI per accedere agli esempi FEM.

## Menu contestuale 

-   <img alt="" src=images/Fem-femmesh-clear-mesh.svg  style="width:32px;"> [Pulisci mesh FEM](FEM_MeshClear/it.md):

-   <img alt="" src=images/Fem-femmesh-print-info.svg  style="width:32px;"> [Stampa info mesh FEM](FEM_MeshPrintInfo/it.md):

## Preferenze

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferenze\...](FEM_Preferences/it.md): Preferenze disponibili per gli strumenti FEM.

## Informazioni

Le seguenti pagine spiegano diversi argomenti dell\'ambiente FEM.

[FEM Install](FEM_Install/it.md): una descrizione dettagliata su come impostare i programmi esterni utilizzati in questo ambiente.

[Mesh FEM](FEM_Mesh/it.md): ulteriori informazioni su come ottenere una mesh per l\'analisi degli elementi finiti.

[FEM Solver](FEM_Solver/it.md): ulteriori informazioni sui diversi solutori disponibili nel workbench e quelli che potrebbero essere utilizzati in futuro.

[FEM CalculiX](FEM_CalculiX/it.md): ulteriori informazioni su CalculiX, il solutore predefinito utilizzato nel workbench per l\'analisi strutturale.

[FEM Concrete](FEM_Concrete/it.md): informazioni interessanti sul tema della simulazione di strutture in calcestruzzo.

[Progetto FEM](FEM_project/it.md): ulteriori informazioni sul sistema di unità, limitazioni, e le idee di sviluppo e la tabella di marcia dell\'ambiente.

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

Le seguenti informazioni sono rivolte agli utenti esperti e agli sviluppatori che desiderano estendere l\'ambiente FEM in modi diversi. Serve avere familiarità con C++ e Python, ed è anche necessaria una certa conoscenza del sistema \"document object\" utilizzato in FreeCAD; queste informazioni sono disponibili nella [documentazione per utenti esperti](Power_users_hub/it.md) e nella [documentazione per gli sviluppatore](Developer_hub/it.md). Notare che, poiché FreeCAD è in fase di sviluppo attivo, alcuni articoli potrebbero essere vecchi e quindi obsoleti. Le informazioni più aggiornate sono discusse nel [forum di FreeCAD](https://forum.freecadweb.org/index.php), nella sezione Development. Per discussioni, consigli o assistenza FEM sull\'estensione dell\'ambiente, il fare riferimento al [subforum FEM](https://forum.freecadweb.org/viewforum.php?f=18).

I seguenti articoli spiegano come è possibile estendere il workbench, ad esempio aggiungendo nuovi tipi di condizioni (vincoli) o equazioni.

-   [Estendere il modulo FEM](Extend_FEM_Module/it.md)
-   [Tutorial Aggiungere equazioni FEM](Add_FEM_Equation_Tutorial/it.md)
-   [Tutorial Aggiungere vincoli FEM](Add_FEM_Constraint_Tutorial/it.md)

Per aiutare gli utenti a comprendere la complessa base di codici di FreeCAD e le interazioni tra gli elementi principali e i singoli ambienti è stata scritta una guida per lo sviluppatore . Il libro è ospitato su github in modo che più utenti possano contribuirvi e tenerlo aggiornato.

-   [Early preview of ebook: Module developer\' guide to FreeCAD source](https://forum.freecadweb.org/viewtopic.php?t=17581) (forum thread)
-   [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) (github repository)

## Estensione della documentazione di FEM Workbench 

-   More information regarding extending or missing FEM documentation can be found in the forum: [FEM documentation missing on the Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)





{{FEM Tools navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
