# <img alt="L\'icona dell\'ambiente Part" src=images/Workbench_Part.svg  style="width   *64px;"> Part Module/it


{{TOCright}}

## Introduzione

Le funzionalità di modellazione di solidi di FreeCAD sono basate sul kernel [OpenCASCADE](OpenCASCADE/it.md) (OCCT), un sistema CAD di livello professionale che offre funzionalità avanzate per la creazione e manipolazione della geometria 3D. L\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part](Part_Workbench/it.md) è su un livello superiore alle librerie OCCT, che fornisce all\'utente l\'accesso alle primitive e alle funzioni geometriche OCCT. Essenzialmente tutte le funzioni di disegno 2D e 3D in FreeCAD, negli ambienti <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> [Draft](Draft_Workbench/it.md), <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> [Sketcher](Sketcher_Workbench/it.md), <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [PartDesign](PartDesign_Workbench/it.md), ecc. si basano sulle funzioni esposte dall\'ambiente Parte. Pertanto, L\'ambiente Part può essere considerato il componente principale delle funzioni di disegno di FreeCAD.

Una discussione più dettagliata dell\'ambiente Part e dell\'ambiente PartDesign può essere trovata qui   * [Part e PartDesign](Part_and_PartDesign/it.md).

Gli oggetti creati con Part sono relativamente semplici; sono pensati per essere utilizzati con le operazioni booleane (unioni e tagli) al fine di costruire forme più complesse. **Questo paradigma di modellazione è noto come flusso di lavoro [geometria solida costruttiva](constructive_solid_geometry/it.md) (CSG) ed era la metodologia tradizionale utilizzata nei primi sistemi CAD.** D\'altra parte, l\'ambiente [PartDesign](PartDesign_Workbench/it.md) fornisce un flusso di lavoro più moderno per la costruzione di forme   * utilizza schizzi parametrici definiti, che vengono estrusi per formare un corpo solido di base, che viene poi modificato da trasformazioni parametriche ([editazione delle funzioni](feature_editing/it.md)), fino a quando non si ottiene l\'oggetto finale.

Gli oggetti Parte sono più complessi degli oggetti mesh creati con l\'ambiente [Mesh](Mesh_Workbench/it.md), e consentono operazioni più avanzate come le operazioni booleane coerenti, la cronologia delle modifiche e il comportamento parametrico.

<img alt="" src=images/Part_Workbench_relationships.svg  style="width   *600px;">



*Part Workbench è lo strato base che espone le funzioni di disegno OCCT a tutti gli ambienti di FreeCAD.*

## Gli strumenti 

Gli strumenti si trovano nel menu **Part** o nel menu **Measure**.

### Primitive

Questi sono strumenti per creare oggetti primitivi.

-   <img alt="" src=images/Part_Box.svg  style="width   *32px;"> [Prisma](Part_Box/it.md)   * Crea parallelepipedi.

-   <img alt="" src=images/Part_Cylinder.svg  style="width   *32px;"> [Cilindro](Part_Cylinder/it.md)   * Crea un cilindro.

-   <img alt="" src=images/Part_Sphere.svg  style="width   *32px;"> [Sfera](Part_Sphere/it.md)   * Crea una sfera.

-   <img alt="" src=images/Part_Cone.svg  style="width   *32px;"> [Cono](Part_Cone/it.md)   * Crea un cono.

-   <img alt="" src=images/Part_Torus.svg  style="width   *32px;"> [Toro](Part_Torus/it.md)   * Crea un toro.

-   <img alt="" src=images/Part_Tube.svg  style="width   *32px;"> [Tubo](Part_Tube/it.md)   * Crea un tubo. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_Primitives.svg  style="width   *32px;"> [Create primitives\...](Part_Primitives.md)   * A tool to create one of the following primitives   *
    -   <img alt="" src=images/Part_Plane.svg  style="width   *32px;"> [Plane](Part_Plane.md)   * Creates a plane.
    -   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width   *32px;"> [Box](Part_Box.md)   * Creates a box. This object can also be created with the <img alt="" src=images/Part_Box.svg  style="width   *32px;"> [Box](Part_Box.md) tool.
    -   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width   *32px;"> [Cylinder](Part_Cylinder.md)   * Creates a cylinder. This object can also be created with the <img alt="" src=images/Part_Cylinder.svg  style="width   *32px;"> [Cylinder](Part_Cylinder.md) tool.
    -   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width   *32px;"> [Cone](Part_Cone.md)   * Creates a cone. This object can also be created with the <img alt="" src=images/Part_Cone.svg  style="width   *32px;"> [Cone](Part_Cone.md) tool.
    -   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width   *32px;"> [Sphere](Part_Sphere.md)   * Creates a sphere. This object can also be created with the <img alt="" src=images/Part_Sphere.svg  style="width   *32px;"> [Sphere](Part_Sphere.md) tool.
    -   <img alt="" src=images/Part_Ellipsoid.svg  style="width   *32px;"> [Ellipsoid](Part_Ellipsoid.md)   * Creates a ellipsoid.
    -   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width   *32px;"> [Torus](Part_Torus.md)   * Creates a torus. This object can also be created with the <img alt="" src=images/Part_Torus.svg  style="width   *32px;"> [Torus](Part_Torus.md) tool.
    -   <img alt="" src=images/Part_Prism.svg  style="width   *32px;"> [Prism](Part_Prism.md)   * Creates a prism.
    -   <img alt="" src=images/Part_Wedge.svg  style="width   *32px;"> [Wedge](Part_Wedge.md)   * Creates a wedge.
    -   <img alt="" src=images/Part_Helix.svg  style="width   *32px;"> [Helix](Part_Helix.md)   * Creates a helix.
    -   <img alt="" src=images/Part_Spiral.svg  style="width   *32px;"> [Spiral](Part_Spiral.md)   * Creates a spiral.
    -   <img alt="" src=images/Part_Circle.svg  style="width   *32px;"> [Circle](Part_Circle.md)   * Creates a circular arc.
    -   <img alt="" src=images/Part_Ellipse.svg  style="width   *32px;"> [Ellipse](Part_Ellipse.md)   * Creates an elliptical arc.
    -   <img alt="" src=images/Part_Point.svg  style="width   *32px;"> [Point](Part_Point.md)   * Creates a point.
    -   <img alt="" src=images/Part_Line.svg  style="width   *32px;"> [Line](Part_Line.md)   * Creates a line.
    -   <img alt="" src=images/Part_RegularPolygon.svg  style="width   *32px;"> [Regular polygon](Part_RegularPolygon.md)   * Creates a regular polygon.

-   <img alt="" src=images/Part_Builder.svg  style="width   *32px;"> [Crea una forma\...](Part_Builder/it.md)   * Crea forme partendo da varie primitive.

### Creazione e modifica 

Questi sono strumenti per creare nuovi oggetti e modificare quelli esistenti.

-   <img alt="" src=images/Part_Extrude.svg  style="width   *32px;"> [Estrusione](Part_Extrude/it.md)   * Estrude facce planari.

-   <img alt="" src=images/Part_Revolve.svg  style="width   *32px;"> [Rivoluziona](Part_Revolve/it.md)   * Crea un solido tramite la rivoluzione di un oggetto (non solido) attorno ad un asse.

-   <img alt="" src=images/Part_Mirror.svg  style="width   *32px;"> [Specchia](Part_Mirror/it.md)   * Riflette l\'oggetto selezionato rispetto ad un asse stabilito.

-   <img alt="" src=images/Part_Fillet.svg  style="width   *32px;"> [Raccorda](Part_Fillet/it.md)   * Raccorda (arrotonda) i bordi di un oggetto.

-   <img alt="" src=images/Part_Chamfer.svg  style="width   *32px;"> [Smussa](Part_Chamfer/it.md)   * Smussa i bordi di un oggetto.

-   <img alt="" src=images/Part_MakeFace.svg  style="width   *32px;"> [Crea faccia](Part_MakeFace/it.md)   * Crea una faccia da un insieme di linee (contorni). <small>(v0.19)</small> 

-   <img alt="" src=images/Part_RuledSurface.svg  style="width   *32px;"> [Superficie rigata](Part_RuledSurface/it.md)   * Crea una superficie superficie rigata.

-   <img alt="" src=images/Part_Loft.svg  style="width   *32px;"> [Loft](Part_Loft.md)   * Lofts from one profile to another.

-   <img alt="" src=images/Part_Sweep.svg  style="width   *32px;"> [Sweep](Part_Sweep.md)   * Sweeps one or more profiles along a path.

-   <img alt="" src=images/Part_Section.svg  style="width   *32px;"> [Seziona](Part_Section/it.md)   * Crea una sezione intersecando un oggetto con un piano di sezione.

-   <img alt="" src=images/Part_CrossSections.svg  style="width   *32px;"> [Sezioni\...](Part_CrossSections/it.md)   * Crea una o più sezioni trasversali attraverso un oggetto.

-   <img alt="" src=images/Part_CompOffsetTools.png  style="width   *48px;"> [Strumenti offset](Part_CompOffsetTools/it.md)   *
    -   <img alt="" src=images/Part_Offset.svg  style="width   *32px;"> [Offset 3D](Part_Offset/it.md)   * Crea una forma parallela ad una data distanza dall\'originale.
    -   <img alt="" src=images/Part_Offset2D.svg  style="width   *32px;"> [Offset 2D](Part_Offset2D/it.md)   * Crea un contorno parallelo ad una certa distanza dall\'originale, ingrandisce o contrae una faccia piana.

-   <img alt="" src=images/Part_Thickness.svg  style="width   *32px;"> [Spessore](Part_Thickness/it.md)   * Svuota un solido.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width   *32px;"> [Proiezione su superficie](Part_ProjectionOnSurface/it.md)   * Proietta un logo, un testo o qualsiasi faccia, polilinea o bordo su una superficie. {{Version/it|0.19}}

-   <img alt="" src=images/Part_EditAttachment.svg  style="width   *32px;"> [Allegato](Part_EditAttachment/it.md)   * Allega un oggetto ad un altro oggetto.

### Boolean

Questi strumenti eseguono operazioni booleane.

-   <img alt="" src=images/Part_CompCompoundTools.png  style="width   *48px;"> [Strumenti Composto](Part_CompCompoundTools/it.md)   *
    -   <img alt="" src=images/Part_Compound.svg  style="width   *32px;"> [Crea un composto](Part_Compound/it.md)   * Crea un composto dagli oggetti selezionati.
    -   <img alt="" src=images/Part_ExplodeCompound.svg  style="width   *32px;"> [Esplodi composto](Part_ExplodeCompound/it.md)   * Divide i composti.
    -   <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width   *32px;"> [Filtra composto](Part_CompoundFilter/it.md)   * Estrae i singoli pezzi di un composto.

-   <img alt="" src=images/Part_Boolean.svg  style="width   *32px;"> [Operazione booleana](Part_Boolean/it.md)   * Esegue operazioni booleane sugli oggetti.

-   <img alt="" src=images/Part_Cut.svg  style="width   *32px;"> [Cut](Part_Cut.md)   * Cuts (subtracts) one object from another.

-   <img alt="" src=images/Part_Fuse.svg  style="width   *32px;"> [Fuse](Part_Fuse.md)   * Fuses (unions) two objects.

-   <img alt="" src=images/Part_Common.svg  style="width   *32px;"> [Intersezione](Part_Common/it.md)   * Estrae la parte comune (intersezione) di due oggetti.

-   <img alt="" src=images/Part_CompJoinFeatures.png  style="width   *48px;"> [Congiungi](Part_CompJoinFeatures/it.md)   *
    -   <img alt="" src=images/Part_JoinConnect.svg  style="width   *32px;"> [Congiungi oggetti](Part_JoinConnect/it.md)   * Congiunge le facce interne di oggetti.
    -   <img alt="" src=images/Part_JoinEmbed.svg  style="width   *32px;"> [Incastra oggetto](Part_JoinEmbed/it.md)   * Incastra un oggetto in un altro oggetto.
    -   <img alt="" src=images/Part_JoinCutout.svg  style="width   *32px;"> [Asporta con oggetto](Part_JoinCutout/it.md)   * Asporta un oggetto da un altro oggetto.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_CompSplittingTools.png  style="width   *48px;"> [Strumenti di suddivisione](Part_CompSplittingTools/it.md)   *
    -   <img alt="" src=images/Part_BooleanFragments.svg  style="width   *32px;"> [Frammenti booleani](Part_BooleanFragments/it.md)   * Crea qualsiasi pezzo ottenendolo da operazioni booleane.
    -   <img alt="" src=images/Part_SliceApart.svg  style="width   *32px;"> [Affetta in parti](Part_SliceApart/it.md)   * Taglia e divide un oggetto intersecandolo con altri oggetti.
    -   <img alt="" src=images/Part_Slice.svg  style="width   *32px;"> [Affetta in composto](Part_Slice/it.md)   * Taglia un oggetto intersecandolo con altri oggetti.
    -   <img alt="" src=images/Part_XOR.svg  style="width   *32px;"> [Booleana XOR](Part_XOR/it.md)   * Rimuove lo spazio condiviso da un numero pari di oggetti (versione simmetrica di [Taglia](Part_Cut/it.md)).


</div>

### Misure

<img alt="" src=images/Std_Measure_Menu.png  style="width   *64px;"> [Misure](Part_Measure_Menu/it.md)   * Strumenti per misure lineari e angolari.

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width   *32px;"> [Misure Lineari](Part_Measure_Linear/it.md) Crea una misura lineare.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width   *32px;"> [Misure angolari](Part_Measure_Angular/it.md)   * Crea una misura angolare.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width   *32px;"> [Aggiorna le misure](Part_Measure_Refresh/it.md)   * Aggiorna tutte le misure.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width   *32px;"> [Clear All](Part_Measure_Clear_All/it.md)   * Cancella tutte le misurazioni.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width   *32px;"> [Attiva o Disattiva tutte le misure](Part_Measure_Toggle_All/it.md)   * Mostra o nasconde tutte le misure.

-   <img alt="" src=images/Part_Measure_Toggle_3d.svg  style="width   *32px;"> [Attiva o Disattiva le misure 3D](Part_Measure_Toggle_3d/it.md)   * Mostra o nasconde le misure 3D.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width   *32px;"> [Attiva o Disattiva le misure Delta](Part_Measure_Toggle_Delta/it.md)   * Mostra o nasconde le misure delta.

### Altri strumenti 

-   <img alt="" src=images/Part_Import.svg  style="width   *32px;"> [Importa CAD](Part_Import/it.md)   * Importazione da file \*.IGES, \*.STEP, o \*.BREP.

-   <img alt="" src=images/Part_Export.svg  style="width   *32px;"> [Esporta CAD](Part_Export/it.md)   * Esportazione in file \*.IGES, \*.STEP, o \*.BREP.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_BoxSelection.svg  style="width   *32px;"> [Box di selezione](Part_BoxSelection/it.md)   * Seleziona le facce da un\'area rettangolare.


</div>

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width   *32px;"> [Crea forma da mesh](Part_ShapeFromMesh/it.md)   * Crea un oggetto forma da un oggetto mesh.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width   *32px;"> [Crea punti da mesh](Part_PointsFromMesh/it.md)   * Crea un oggetto forma composto da punti a partire da un oggetto mesh. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_MakeSolid.svg  style="width   *32px;">[Converti in solido](Part_MakeSolid/it.md)   * Converte un oggetto forma di un oggetto solido.

-   <img alt="" src=images/Part_ReverseShapes.svg  style="width   *32px;"> [Inverti le forme](Part_ReverseShapes/it.md)   * Capovolge le normali di tutte le facce dell\'oggetto selezionato.

-   Creare una copia   *
    -   <img alt="" src=images/Part_SimpleCopy‎.svg  style="width   *32px;"> [Crea una copia semplice](Part_SimpleCopy/it.md)   * Crea una semplice copia dell\'oggetto selezionato.
    -   <img alt="" src=images/Part_TransformedCopy.svg  style="width   *32px;"> [Crea una copia modificata](Part_TransformedCopy/it.md)   * Crea una copia trasformata dell\'oggetto selezionato. {{Version/it|0.19}}
    -   <img alt="" src=images/Part_ElementCopy.svg  style="width   *32px;"> [Crea una copia di un elemento](Part_ElementCopy/it.md)   * Crea una copia da un elemento (vertice, bordo, faccia) dell\'oggetto selezionato. {{Version/it|0.19}}
    -   <img alt="" src=images/Part_RefineShape.svg  style="width   *32px;"> [Affina una forma](Part_RefineShape/it.md)   * Pulisce le facce, eliminando le linee inutili.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width   *32px;"> [Controlla la geometria](Part_CheckGeometry/it.md)   * Controlla se la geometria degli oggetti selezionati contiene degli errori.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width   *32px;"> [Elimina funzioni](Part_Defeaturing/it.md)   * Rimuove le funzioni da un oggetto.

### Strumenti del menu contestuale 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width   *32px;"> [Aspetto](Std_SetAppearance/it.md)   * Determina l\'aspetto di un intero oggetto (colore, trasparenza, ecc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width   *32px;"> [Impostare il colore delle facce](Part_FaceColors/it.md)   * Assegna i colori alle singole facce degli oggetti.

## Preferenze

-   <img alt="" src=images/Preferences-part_design.svg  style="width   *32px;"> [Preferenze](PartDesign_Preferences/it.md)   * Preferenze disponibili per gli strumenti di Part (l\'ambiente Part utilizza anche le preferenze di PartDesign).
-   <img alt="" src=images/Preferences-import-export.svg  style="width   *32px;"> [Preferenze di Importa e esporta](Import_Export_Preferences/it.md)   * preferenze disponibili per l\'importazione e l\'esportazione in diversi formati di file.
-   [Ottimizzazione](Fine-tuning/it.md)   * Alcuni parametri extra per mettere a punto il comportamento di Part.

## Script

Vedere [Script di Part](Part_scripting/it.md)

## Tutorial

-   [Importare da STL o OBJ](Import_from_STL_or_OBJ/it.md)    * come importare file STL/OBJ in FreeCAD
-   [Esportare in STL o OBJ](Export_to_STL_or_OBJ/it.md)    * come esportare file STL/OBJ da FreeCAD
-   [Tutorial Sfera traforata](Whiffle_Ball_tutorial/it.md)    * come usare il modulo Part


<div class="mw-translate-fuzzy">





</div>


 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Part_Workbench.md) > Part Module/it
