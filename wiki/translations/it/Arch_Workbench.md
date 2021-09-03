




<img alt="L\'icona di Arch" src=images/Workbench_Arch.svg  style="width:128px;">


{{TOCright}}

## Introduzione

Il modulo <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> Arch fornisce a FreeCAD un moderno flusso di lavoro di tipo [building information modelling](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM), con supporto per funzionalità come entità architettoniche completamente parametriche come muri, travi, tetti, finestre, scale, tubazioni e mobili. Supporta i file [industry foundation classes](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) ([IFC](Arch_IFC/it.md)), e la produzione di planimetrie 2D in combinazione con l\'ambiente <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/it.md).

L\'ambiente Arch importa tutti gli strumenti dall\'ambiente <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft](Draft_Workbench/it.md), poiché usa oggetti 2D per costruire i suoi oggetti architettonici 3D parametrici. Tuttavia, Arch può anche utilizzare oggetti solidi creati in altri ambiente di lavoro come <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Parte](Part_Workbench/it.md) e <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/it.md).

La funzionalità BIM di FreeCAD ora è progressivamente distribuita in questo ambiente Arch, che contiene gli strumenti di base per l\'architettura, e <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/it.md), che è possibile installare tramite <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md). Questo ambiente BIM aggiunge un nuovo livello di interfaccia in cima agli strumenti Arch, con l\'obiettivo di rendere facile e più intuitivo il flusso di lavoro BIM in FreeCAD. Vedere [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide).

Gli sviluppatori di Draft, Arch e BIM collaborano anche con la più ampia [comunità OSArch](https://osarch.org), con l\'obiettivo finale di migliorare la progettazione degli edifici utilizzando software completamente gratuito.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

## Strumenti

Strumenti per creare gli oggetti architettonici.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Muro](Arch_Wall/it.md): crea un muro tramite uno schizzo o utilizzando come base un oggetto selezionato.
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Facciata continua](Arch_CurtainWall/it.md): crea una facciata continua da zero o utilizzando come base un oggetto selezionato. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Struttura](Arch_Structure/it.md): crea un elemento strutturale tramite uno schizzo o utilizzando come base un oggetto selezionato.

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Armature](Arch_CompRebarStraight/it.md): l\'Addon Reinforcement incrementa le Strutture di Arch.
    -   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Armatura dritta](Arch_Rebar_Straight/it.md): crea una armatura diritta in un elemento strutturale selezionato
    -   <img alt="" src=images/UShapeRebar.png  style="width:32px;"> [Armatura a U](Arch_Rebar_UShape/it.md): crea una armatura piegata a U in un elemento strutturale selezionato
    -   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [Armatura a L](Arch_Rebar_LShape/it.md): crea una armatura a forma di L in un elemento strutturale selezionato
    -   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Armatura sagomata](Arch_Rebar_BentShape/it.md): crea una armatura sagomata in un elemento strutturale selezionato
    -   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Staffe armatura](Arch_Rebar_Stirrup/it.md): crea le staffe di una armatura in un elemento strutturale selezionato
    -   <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Armatura elicoidale](Arch_Rebar_Helical/it.md): crea una armatura elicoidale in un elemento strutturale selezionato
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [Armatura di colonna](Arch_Rebar_ColumnReinforcement/it.md): crea barre di rinforzo all\'interno di una Struttura colonna di Arch.
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [Armatura di pilastro con due staffe e sei barre](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/it.md): crea barre di rinforzo con due staffe e sei barre all\'interno di una Struttura pilastro di Arch.
    -   <img alt="" src=images/Arch_Rebar_BeamReinforcement.png  style="width:32px;"> [Armatura di trave](Arch_Rebar_BeamReinforcement/it.md): crea barre di rinforzo all\'interno di una Struttura trave di Arch.
    -   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Armatura personalizzata](Arch_Rebar/it.md): crea l\'armatura in un elemento strutturale estrudendo uno schizzo o utilizzando come base un oggetto selezionato

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Piano](Arch_Floor/it.md): Crea un piano che comprende gli oggetti selezionati
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Parte di edificio](Arch_BuildingPart/it.md): Crea una parte di edificio che include oggetti selezionati
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Edificio](Arch_Building/it.md): Crea un edificio che comprende gli oggetti selezionati
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Sito](Arch_Site/it.md): Crea un sito che comprende gli oggetti selezionati
-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Progetto](Arch_Project/it.md): Crea un progetto includendo gli oggetti selezionati
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Riferimento esterno](Arch_Reference/it.md): Collega oggetti di un altro file di FreeCAD in questo documento
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Finestra](Arch_Window/it.md): Crea una finestra utilizzando come base un oggetto selezionato
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Piano di sezione](Arch_SectionPlane/it.md): Aggiunge un oggetto *Piano di sezione* al documento

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Assi](Arch_CompAxis/it.md): Lo strumento Assi consente di posizionare una serie di assi nel documento corrente.
    -   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Asse](Arch_Axis/it.md): Aggiunge al documento un sistema di assi in 1 direzione
    -   <img alt="" src=images/Arch_Axis_System.svg  style="width:32px;"> [Sistema di assi](Arch_AxisSystem/it.md): Aggiunge al documento un sistema di assi composto da più assi
    -   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Griglia](Arch_Grid/it.md): Inserisce un oggetto tipo griglia nel documento.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Tetto](Arch_Roof/it.md): Crea le falde del tetto partendo da una faccia selezionata
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Spazio](Arch_Space/it.md): Crea un oggetto spazio
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Scala](Arch_Stairs/it.md): Crea un oggetto scala

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Strumenti pannello](Arch_CompPanel/it.md): Permette di costruire tutti i tipi di elementi simili a pannelli.
    -   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Pannello](Arch_Panel/it.md): Crea un oggetto pannello basato su un oggetto 2D selezionato
    -   <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Sagoma pannello](Arch_Panel_Cut/it.md): Crea una vista in 2D di un pannello {{Version/it|0.17}}
    -   <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Foglio pannello](Arch_Panel_Sheet/it.md): Creates a 2D cut sheet including panel cuts or other 2D objects {{Version/it|0.17}}
    -   <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Nido](Arch_Nest/it.md): Consente di nidificare diversi oggetti piatti all\'interno di una forma contenitore {{Version/it|0.17}}

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Carpenteria](Arch_Frame/it.md): Crea un oggetto di carpenteria basato su uno schema selezionato.
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Recinzione](Arch_Fence/it.md): Crea un oggetto recinzione da una campata e un percorso selezionati. {{Version/it|0.19}}
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Travatura](Arch_Truss/it.md): Crea una travatura da una linea selezionata da zero. {{Version/it|0.19}}
-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Arredo](Arch_Equipment/it.md): Crea un oggetto di arredamento.
-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profilo](Arch_Profile/it.md): Crea un profilo 2D parametrico. {{Version/it|0.19}}

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Tubazioni](Arch_CompPipe/it.md) {{Version/it|0.17}}
    -   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Tubo](Arch_Pipe/it.md): Crea un tubo {{Version/it|0.17}}
    -   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Raccordo](Arch_PipeConnector/it.md): Crea una connessione a angolo o un tee (raccordo) tra 2 o 3 tubi selezionati {{Version/it|0.17}}

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Materiali](Arch_CompSetMaterial/it.md): Gli strumenti Materiale consentono di aggiungere materiali al documento attivo.
    -   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Materiale](Arch_SetMaterial/it.md): Crea un materiale e lo attribuisce agli oggetti selezionati
    -   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Multi-Materiale](Arch_MultiMaterial/it.md): Crea un materiale e lo attribuisce agli oggetti selezionati {{Version/it|0.17}}
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Scheda](Arch_Schedule/it.md): Crea diversi tipi di schede

### Strumenti di modifica 

Strumenti per modificare gli oggetti architettonici.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Taglia con una linea](Arch_CutLine/it.md): Taglia un oggetto secondo una linea. {{Version/it|0.19}}
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Taglia con un piano](Arch_CutPlane/it.md): Taglia un oggetto secondo un piano.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Aggiungi componente](Arch_Add/it.md): Aggiunge oggetti ad un componente
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Rimuovi componente](Arch_Remove/it.md): Sottrae o rimuove oggetti da un componente
-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Ispeziona](Arch_Survey/it.md): Entra o esce dalla modalità ispezione

### Utilità

Strumenti aggiuntivi di aiuto per operazioni specifiche.

!!FUZZY!!\* <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Componenti](Arch_Component/it.md): Crea un componente Arch non parametrico

-   <img alt="" src=images/Arch_ComponentClone.svg  style="width:32px;"> [Clona componente](Arch_CloneComponent/it.md): Produce componenti Arch che sono cloni di oggetti Arch selezionati (da non confondere con [Clona di Draft](Draft_Clone/it.md))
-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Dividi mesh](Arch_SplitMesh/it.md): Divide una maglia selezionata in componenti separati
-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Forma da Mesh](Arch_MeshToShape/it.md): Converte una maglia in una forma, unificando le facce complanari
-   <img alt="" src=images/Arch_SelectNonManifold.svg  style="width:32px;"> [Seleziona le mesh non-manifold](Arch_SelectNonSolidMeshes/it.md): Seleziona tutti gli oggetti maglia non-solidi della selezione corrente o del documento
-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Rimuovi forma](Arch_RemoveShape/it.md): Converte le forme basate su cubi in oggetti architettonici completamente parametrici
-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Chiudi aperture](Arch_CloseHoles/it.md): Chiude le aperture in un oggetto selezionato basato su forme
-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Unisci pareti](Arch_MergeWalls/it.md): Unisce due o più pareti
-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Verifica](Arch_Check/it.md): Controlla se gli oggetti selezionati sono solidi e non contengono difetti
-   <img alt="" src=images/IFC.svg  style="width:32px;"> [Ifc Explorer](Arch_IfcExplorer/it.md): Esplora il contenuto di un file [IFC](Arch_IFC/it.md)
-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Attiva/Disattiva IFC Brep](Arch_ToggleIfcBrepFlag/it.md): Forza l\'esportazione [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm) di un oggetto selezionato.
-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [3 Viste da mesh](Arch_3Views/it.md): Crea la vista superiore, frontale e laterale di un [mesh](Mesh_Workbench/it.md).
-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Crea un foglio IFC\...](Arch_IfcSpreadsheet/it.md): Crea un foglio di calcolo per memorizzare le proprietà [IFC](Arch_IFC/it.md) di un oggetto
-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Mostra/Nascondi sottocomponenti](Arch_ToggleSubs/it.md): Mostra o nasconde i sotto-componenti di un oggetto Arch.

### Preferences

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Preferenze](Arch_Preferences/it.md): preferenze per l\'aspetto predefinito di pareti, strutture, armature, finestre, scale, pannelli, tubazioni, griglie e assi.

### Formati dei file 

-   [IFC](Arch_IFC/it.md): Industry foundation classes
-   [DAE](Arch_DAE/it.md): Formato mesh Collada
-   [OBJ](Arch_OBJ/it.md): Formato mesh Obj (solo esportazione)
-   [JSON](Arch_JSON/it.md): Formato JavaScript Object Notation (solo esportazione)
-   [3DS](Arch_3DS/it.md): Formato 3DS (solo importazione)
-   [SHP](Arch_SHP/it.md): GIS Shapefiles (solo importazione)

## API

Il Modulo Arch può essere usato negli [Python](Python/it.md) e [macro](macros/it.md) utilizzando la funzione [Arch Python API](http://www.freecadweb.org/api/Arch.html).

## Tutorial

-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad): Un esempio di flusso di lavoro di FreeCAD in architettura.
-   [Tutorial di Arch](Arch_tutorial/it.md) (v0.14)
-   [Breve panoramica su Arch nel blog di Yorik](http://yorik.uncreated.net/guestblog.php?2012=180) (v0.13)
-   [Presentazione video dell\'ambiente Arch](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Tutorial Pannello di Arch ](Arch_panel_tutorial/it.md) (v0.15)
-   [Il capitolo sulla modellazione BIM nel manuale di FreeCAD](Manual:BIM_modeling/it.md)
-   [Importare da STL o OBJ](Import_from_STL_or_OBJ/it.md)
-   [Esportare in STL o OBJ](Export_to_STL_or_OBJ/it.md)





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
