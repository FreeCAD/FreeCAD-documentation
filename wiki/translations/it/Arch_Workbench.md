# Arch Workbench/it
**In v1.0 the BIM, Native-IFC and Arch Workbenches have been merged into the integrated [BIM Workbench](BIM_Workbench.md).**

<img alt="L\'icona di Arch" src=images/Workbench_Arch.svg  style="width:128px;">






## Introduzione

The <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Workbench](Arch_Workbench.md) provides a modern [**B**uilding **I**nformation **M**odelling](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM) workflow to FreeCAD, with support for features like fully parametric architectural entities such as walls, beams, roofs, windows, stairs, pipes, and furniture. It supports [**I**ndustry **F**oundation **C**lasses](Arch_IFC.md) (IFC) files, and production of 2D floor plans in combination with the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

L\'ambiente Arch importa tutti gli strumenti dall\'ambiente <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft](Draft_Workbench/it.md), poiché usa oggetti 2D per costruire i suoi oggetti architettonici 3D parametrici. Tuttavia, Arch può anche utilizzare oggetti solidi creati in altri ambiente di lavoro come <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Parte](Part_Workbench/it.md) e <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/it.md).

La funzionalità BIM di FreeCAD ora è progressivamente distribuita in questo ambiente Arch, che contiene gli strumenti di base per l\'architettura, e <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/it.md), che è possibile installare tramite <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md). Questo ambiente BIM aggiunge un nuovo livello di interfaccia in cima agli strumenti Arch, con l\'obiettivo di rendere facile e più intuitivo il flusso di lavoro BIM in FreeCAD. Vedere [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide).

Gli sviluppatori di Draft, Arch e BIM collaborano anche con la più ampia [comunità OSArch](https://osarch.org), con l\'obiettivo finale di migliorare la progettazione degli edifici utilizzando software completamente gratuito.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">



## Strumenti

Strumenti per creare gli oggetti architettonici.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Muro](Arch_Wall/it.md): Crea un muro da zero o utilizzando un oggetto selezionato come base.

-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Struttura](Arch_Structure/it.md): Crea un elemento strutturale da zero o utilizzando un oggetto selezionato come base.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Strumenti armatura](Arch_CompRebarStraight/it.md): Questi strumenti sono disponibili solo se è stato installato l\'[Ambiente Rinforzi](Reinforcement_Workbench/it.md).


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_Straight.svg  style="width:32px;"> [Armatura diritta](Arch_Rebar_Straight/it.md): Crea una barra d\'armatura diritta in un elemento strutturale selezionato.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_UShape.svg  style="width:32px;"> [Armatura a U](Arch_Rebar_UShape/it.md): Crea una barra d\'armatura a forma di U in un elemento strutturale selezionato.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_LShape.svg  style="width:32px;"> [Armatura a L](Arch_Rebar_LShape/it.md): Crea una barra d\'armatura a forma di L in un elemento strutturale selezionato.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width:32px;"> [Staffe armatura](Arch_Rebar_Stirrup/it.md): Crea una barra d\'armatura a staffa in un elemento strutturale selezionato.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_BentShape.svg  style="width:32px;"> [Armatura sagomata](Arch_Rebar_BentShape/it.md): Crea una barra d\'armatura sagomata in un elemento strutturale selezionato.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_Helical.svg  style="width:32px;"> [Armatura elicoidale](Arch_Rebar_Helical/it.md): Crea una barra d\'armatura elicoidale in un elemento strutturale selezionato.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Armatura pilastro](Arch_Rebar_ColumnReinforcement/it.md): Crea barre d\'armatura in un pilastro rettangolare selezionato.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [Armatura trave](Arch_Rebar_BeamReinforcement/it.md): Crea barre d\'armatura in una trave selezionata.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_Slab_Reinforcement.svg  style="width:32px;"> [Armatura soletta](Arch_Rebar_Slab_Reinforcement/it.md): Crea barre d\'armatura in una soletta selezionata.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width:32px;"> [Armatura fondamenta](Arch_Rebar_Footing_Reinforcement/it.md): Crea barre d\'armatura all\'interno di una fondamenta selezionata.


</div>

  - <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Armatura personalizzata](Arch_Rebar/it.md): Crea una barra d\'armatura personalizzata in un elemento strutturale selezionato utilizzando uno schizzo.

-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Facciata continua](Arch_CurtainWall/it.md): Crea una facciata continua da zero o utilizzando un oggetto selezionato come base.

-   <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Parte di edificio](Arch_BuildingPart/it.md): Crea una parte dell\'edificio che include gli oggetti selezionati.

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Progetto](Arch_Project/it.md): Crea un progetto che include oggetti selezionati.

-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Sito](Arch_Site/it.md): Crea un sito che include oggetti selezionati.

-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Edificio](Arch_Building/it.md): Crea un edificio che include gli oggetti selezionati.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Piano](Arch_Floor/it.md): Crea un piano che include gli oggetti selezionati.

-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Riferimento esterno](Arch_Reference/it.md): Collega gli oggetti da un altro file di FreeCAD al documento corrente.

-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Finestra](Arch_Window/it.md): Crea una finestra da zero o utilizzando un oggetto selezionato come base.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Tetto](Arch_Roof/it.md): Crea un tetto inclinato da un filo selezionato.

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Strumenti Assi](Arch_CompAxis/it.md)

  - <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Asse](Arch_Axis/it.md): Aggiunge una matrice di assi a 1 direzione.

  - <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Sistema di assi](Arch_AxisSystem/it.md): Aggiunge un sistema di assi composto da più assi.

  - <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Griglia](Arch_Grid/it.md): Aggiunge un oggetto simile a una griglia.

-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Piano di sezione](Arch_SectionPlane/it.md): Aggiunge un oggetto piano di sezione.

-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Spazio](Arch_Space/it.md): Crea un oggetto spazio.

-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Scale](Arch_Stairs/it.md): Crea un oggetto scala.

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Strumenti pannello](Arch_CompPanel/it.md)

  - <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Pannello](Arch_Panel/it.md): Crea un oggetto pannello da un oggetto 2D selezionato.

  - <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Sagoma pannello](Arch_Panel_Cut/it.md): Crea una vista piana 2D da un pannello.

  - <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Foglio pannello](Arch_Panel_Sheet/it.md): Crea un foglio 2D che include sagome di pannelli o altri oggetti 2D.

  - <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Nido](Arch_Nest/it.md): Consente di annidare più oggetti piatti all\'interno di una forma contenitore.

-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Arredo](Arch_Equipment/it.md): Crea un elemento o un oggetto di arredo.

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Telaio](Arch_Frame/it.md): Crea un oggetto di carpenteria da un layout selezionato.

-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Recinzione](Arch_Fence/it.md): Crea un oggetto recinzione da un palo e un percorso selezionati.

-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Travatura](Arch_Truss/it.md): Crea una travatura reticolare da una linea selezionata o da zero.

-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profilo](Arch_Profile/it.md): Crea un profilo 2D parametrico.

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Materiali](Arch_CompSetMaterial/it.md)

  - <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Materiale](Arch_SetMaterial/it.md): Crea un materiale e lo attribuisce agli oggetti selezionati, se presenti.

  - <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Multi-Materiale](Arch_MultiMaterial/it.md): Crea un multi-materiale e lo attribuisce agli oggetti selezionati, se presenti.

-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Scheda](Arch_Schedule/it.md): Crea diversi tipi di schede.

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Tubazioni](Arch_CompPipe/it.md)

  - <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Tubo](Arch_Pipe/it.md) Crea un tubo.

  - <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Raccordo](Arch_PipeConnector/it.md): Crea un angolo o una connessione a T tra 2 o 3 tubi selezionati.



### Strumenti di modifica 

Strumenti per modificare gli oggetti architettonici.

-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Taglio con piano](Arch_CutPlane/it.md): Taglia un oggetto secondo un piano.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Taglio con una linea](Arch_CutLine/it.md): Taglia un oggetto secondo una linea. Non disponibile nella {{VersionPlus/it|0.22}}.


</div>

-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Aggiungi componente](Arch_Add/it.md): Aggiunge oggetti a un componente.

-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Rimuovi componente](Arch_Remove/it.md): Sottrae o rimuove oggetti da un componente.

-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Ispeziona](Arch_Survey/it.md): Entra o esce dalla modalità di rilevamento.



### Utilità

Strumenti aggiuntivi di aiuto per operazioni specifiche.

-   <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Componente](Arch_Component/it.md): Crea un componente Arch non parametrico.

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Clona componente](Arch_CloneComponent/it.md): Produce componenti Arch che sono cloni di oggetti Arch selezionati (da non confondere con [Draft Clona](Draft_Clone/it.md)).

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Dividi mesh](Arch_SplitMesh/it.md): Divide una mesh selezionata in componenti separati.

-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Da Mesh a Forma](Arch_MeshToShape/it.md) Converte una mesh in una forma, unificando le facce complanari.

-   <img alt="" src=images/Arch_SelectNonSolidMeshes.svg  style="width:32px;"> [Seleziona le mesh non-manifold](Arch_SelectNonSolidMeshes/it.md): Seleziona tutte le mesh non-manifold dalla selezione corrente o dal documento.

-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Rimuovi forma](Arch_RemoveShape/it.md): Trasforma l\'oggetto Arch basato sulla forma cubica in un oggetto completamente parametrico.

-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Chiudi fori](Arch_CloseHoles/it.md): Chiude i fori in un oggetto basato sulla forma selezionato.

-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Unisci i muri](Arch_MergeWalls/it.md): Unisce due o più pareti.

-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Controlla](Arch_Check/it.md): Controlla se gli oggetti selezionati sono solidi e non contengono difetti.

-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Attiva\\Disattiva IFC Brep](Arch_ToggleIfcBrepFlag/it.md): Forza l\'esportazione di un oggetto selezionato come un [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [3 viste da mesh](Arch_3Views/it.md): Crea viste dall\'alto, frontale e laterale da un [mesh](Mesh_Workbench/it.md).

-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Crea un foglio di calcolo Ifc\...](Arch_IfcSpreadsheet/it.md): Crea un foglio di calcolo per archiviare le proprietà di un oggetto [IFC](Arch_IFC/it.md).

-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Attiva o disattiva i sottocomponenti](Arch_ToggleSubs/it.md): Attiva o Disattiva i sottocomponenti di un oggetto Arch.

### Preferences

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Preferenze](Arch_Preferences/it.md): preferenze per l\'aspetto predefinito di pareti, strutture, armature, finestre, scale, pannelli, tubazioni, griglie e assi.



### Formati dei file 

-   [IFC](Arch_IFC/it.md): Industry foundation classes
-   [DAE](Arch_DAE/it.md): Formato mesh Collada
-   [OBJ](Arch_OBJ/it.md): Formato mesh OBJ (solo esportazione)
-   [JSON](Arch_JSON/it.md): Formato JavaScript Object Notation (solo esportazione)
-   [3DS](Arch_3DS/it.md): Formato 3DS (solo importazione)
-   [SHP](Arch_SHP/it.md): GIS Shapefiles (solo importazione)

## API

Il Modulo Arch può essere usato negli [Python](Python/it.md) e [macro](macros/it.md) utilizzando le funzioni [Python API di Arch](Arch_API/it.md).



## Tutorial

-   [Migrare a FreeCAD da Revit](Migrating_to_FreeCAD_from_Revit/it.md)
-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad): Un esempio di flusso di lavoro di FreeCAD in architettura.
-   [Tutorial di Arch](Arch_tutorial/it.md) (v0.14)
-   [Breve panoramica su Arch nel blog di Yorik](http://yorik.uncreated.net/guestblog.php?2012=180) (v0.13)
-   [Presentazione video dell\'ambiente Arch](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Tutorial Pannello di Arch ](Arch_panel_tutorial/it.md) (v0.15)
-   [Il capitolo sulla modellazione BIM nel manuale di FreeCAD](Manual:BIM_modeling/it.md)
-   [Importare da STL o OBJ](Import_from_STL_or_OBJ/it.md)
-   [Esportare in STL o OBJ](Export_to_STL_or_OBJ/it.md)



---
⏵ [documentation index](../README.md) > [Obsolete_Workbenches](Category_Obsolete_Workbenches.md) > [Arch](Category_Arch.md) > Arch Workbench/it
