# <img alt="Assembly3 workbench icon" src=images/Assembly3_workbench_icon.svg  style="width:64px;"> Assembly3 Workbench/it


{{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

[Assembly3](Assembly3_Workbench.md) è un [banco di lavoro esterno](External_workbenches.md) che viene utilizzato per eseguire l\'assemblaggio di diversi corpi contenuti in un unico file o in più documenti. Il banco da lavoro si basa su diverse modifiche delle funzioni principali effettuate per la versione di FreeCAD 0.19 (ad es. [App Link](App_Link.md)), quindi il banco da lavoro Assembly3 non può essere utilizzato con le versioni precedenti.


</div>

Le caratteristiche principali del banco da lavoro Assembly3 sono

-   **dynamic/interactive solver**. Ciò significa che è possibile spostare le parti con il mouse mentre il risolutore limita il movimento. Ciò consente, ad esempio, di collegare una ruota ad un asse e di ruotare la ruota in modo interattivo con il mouse.
-   **links**. Ciò significa che è possibile utilizzare un solo pezzo, ad es. una vite più volte in un assemblaggio (in luoghi diversi) senza duplicare la geometria.
-   **external links**. E\' possibile avere un documento freecad che contiene solo un assemblaggio e non parti. Tutte le parti potrebbero essere in file singoli. I file potrebbero anche essere in una libreria o in qualsiasi altra parte del file system. L\'unico requisito è che il file deve essere caricato al momento del collegamento. Dopo che il collegamento è stato fatto, il file deve essere aperto per fare gli aggiornamenti ai collegamenti che coinvolgono il file. Assembly3 risolve questo problema aprendo i file in background.
-   **hierarchical assemblies**. Come nella vita reale, un assemblaggio meccanico può essere costituito da sottoinsiemi. Questi potrebbero consistere di nuovo in sottoinsiemi e così via.
-   **assembly freeze**. Poiché la CPU può gestire solo un numero limitato di vincoli simultanei in tempo reale, il congelamento di un assieme permette di utilizzare i vincoli anche per assiemi di grandi dimensioni. Congelando gli assiemi finiti o i vincoli che non devono rimanere dinamici (ad es. parti saldate, bullonate o incollate), questi vengono esclusi dai calcoli di aggiornamento e considerati geometria fissa dal solutore Assembly3.

    :   Si noti che altri approcci offrono soluzioni diverse a questo problema, per esempio <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Assembly4 Workbench](Assembly4_Workbench.md).

[Torna all\'inizio](#top.md)

### Barre degli strumenti 

A partire dal 2020 il banco da lavoro Assembly3 è dotato delle seguenti barre degli strumenti.


<div class="mw-translate-fuzzy">


:   La **barra degli strumenti principale** contiene strumenti che coprono le caratteristiche più utilizzate del banco di lavoro. I suggerimenti forniranno scorciatoie da tastiera.
    -   aggiungere una cartella di assemblaggio
    -   gruppo di oggetti
    -   creare un collegamento. Questo è disponibile anche in un menu contestuale
    -   Importare file STEP
    -   Risolvere i vincoli
    -   Risoluzione rapida dei vincoli
    -   tool1 per spostare le parti in 3D, questo è specifico per Assembly3
    -   tool2 per spostare parti in 3D, questo è il classico strumento disponibile in FreeCAD
    -   Spostamento rapido. Questo vincola la parte selezionata nell\'albero al cursore del mouse. Cambierà la posizione della parte quando si clicca.

        :   Spesso le parti aggiunte sono impilate l\'una sull\'altra nell\'origine. Utilizzare questa funzione per afferrare una parte che non si vede.
    -   Sblocco per le parti bloccate. Pulsante a levetta. Quando questo non è selezionato è possibile spostare le parti che hanno un vincolo \"Bloccato\".
    -   Attivare la visibilità. Questo attiva/disattiva la visibilità della parte selezionata.

        :   Si noti che questo è diverso dall\'uso dello spazio. L\'uso dello spazio con elementi selezionati da un sottoinsieme nella vista 3D spesso non si comporta come previsto. Utilizzare questa funzione in questi casi (o la scorciatoia A-Space)
    -   Tracciare il movimento delle parti (TBD)
    -   Calcolo automatico. Di solito è abilitata.

        :   Può essere non selezionato quando si riparano vincoli o si fissano parti in cui il solutore dà un messaggio *non convergente* (ad esempio ruotando la parte di 180deg)
    -   Smart-Recompute. Di solito è abilitato.
    -   Element Auto Fixing. Caratteristica sperimentale in 0.19\_pre
    -   Element Style. Questo ha due impostazioni
        -   Auto visibilità dell\' elemento.
        -   Mostra il sistema di coordinate dell\'elemento
    -   Comandi workplane. Aggiunge un piano di lavoro, il posizionamento o l\'origine. Una parte deve essere selezionata
        -   Aggiungi un workplane
        -   Aggiungi un XZ workplane
        -   Aggiungi un YZ workplane
        -   Aggiungi il posizionamento
        -   Aggiungi Origine
    -   Spostare l\'elemento selezionato dell\'albero verso l\'alto
    -   Spostare l\'elemento selezionato dell\'albero verso il basso

        :   Permette di ordinare parti, elementi o vincoli nell\'albero. Gli elementi si muovono (dall\'alto verso il basso e viceversa). Funziona solo per una singola selezione.
    -   Moltiplicare il vincolo. Questo può essere selezionato se sono presenti più parti ed elementi adatti. Viene utilizzato ad esempio per assegnare più elementi di fissaggio dello stesso tipo in più fori con un unico vincolo.


</div>


<div class="mw-collapsible mw-collapsed">


:   The **Main Toolbar** contains tools that cover the most often used features of the workbench. The tooltips will give the keyboard short cuts.


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width:32px;"> [Create assembly](Assembly3_CreateAssembly.md): Add an assembly folder

:\* <img alt="" src=images/Assembly_New_Group.svg‎‎  style="width:32px;"> [Group objects](Assembly3_GroupObjects.md): Group objects

:\* <img alt="" src=images/Assembly_New_Element.svg‎‎  style="width:32px;"> [Create element](Assembly3_CreateElement.md): Create element.

:\* Import from STEP. This has two settings

:\*\* <img alt="" src=images/Assembly_Import.svg‎‎  style="width:32px;"> [Import from STEP](Assembly3_ImportFromSTEP.md): Import STEP files

:\*\* <img alt="" src=images/Assembly_ImportMulti.svg‎‎  style="width:32px;"> [Import as multi-document](Assembly3_ImportMultiDocument.md): Import assemblies from STEP into separate documents

:\* <img alt="" src=images/Assembly3_workbench_icon.svg‎‎  style="width:32px;"> [Resolve constraints](Assembly3_ResolveConstraints.md): Resolve constraints

:\* <img alt="" src=images/Assembly_QuickSolve.svg‎‎  style="width:32px;"> [Quick solve](Assembly3_QuickSolve.md): Quick resolve constraints

:\* <img alt="" src=images/Assembly_Move.svg‎‎  style="width:32px;"> [Move part](Assembly3_MovePart.md): Move parts in 3D, this is specific to Assembly3

:\* <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:32px;"> [Axial move](Assembly3_AxialMove.md): Axial move parts in 3D, this is the classical tool available elsewhere in FreeCAD

:\* <img alt="" src=images/Assembly_QuickMove.svg‎‎  style="width:32px;"> [Quick move](Assembly3_QuickMove.md): This will attach the part selected in the tree to the mouse cursor. It will change the position of the part when you click.

:\*: Often added parts are stacked upon each other in the origin. Use this function to grab a part you can not see.

:\* <img alt="" src=images/Assembly_LockMover.svg‎‎  style="width:32px;"> [Lock mover](Assembly3_LockMover.md): Lock mover for fixed part. Toggle Button. When this is un-selected you can move the parts that have a \"Locked\" constraint.

:\* <img alt="" src=images/Assembly_TogglePartVisibility.svg‎‎  style="width:32px;"> [Toggle part visibility](Assembly3_TogglePartVisibility.md): This toggles the visiblity of the selected part on/off.

:\*: Note that this differs from using space. Using space with selected items from a sub-assembly in the 3D view often does not behave as expected. Use this function in those cases (or shortcut A-Space)

:\* <img alt="" src=images/Assembly_Trace.svg‎‎  style="width:32px;"> [Trace part move](Assembly3_TracePartMove.md): Trace part move (TBD)

:\* <img alt="" src=images/Assembly_AutoRecompute.svg‎‎  style="width:32px;"> [Auto recompute](Assembly3_AutoRecompute.md): Auto recompute. Usually enabled.

:\*: May be un-selected when repairing constraints or fixing parts where the solver gives a *\"do not converge\"* message (e.g. by turning the part 180deg)

:\* <img alt="" src=images/Assembly_SmartRecompute.svg‎‎  style="width:32px;"> [Smart recompute](Assembly3_SmartRecompute.md): Smart recompute. Usually enabled.

:\* <img alt="" src=images/Assembly_AutoFixElement.svg‎‎  style="width:32px;"> [Auto fix element](Assembly3_AutoFixElement.md): Element Auto Fixing. Experimental feature in 0.19\_pre

:\* Element Style. This has two settings

:\*\* <img alt="" src=images/Assembly_AutoElementVis.svg‎‎  style="width:32px;"> [Auto element visibility](Assembly3_AutoElementVisibility.md): Auto element visibility

:\*\* <img alt="" src=images/Assembly_ShowElementCS.svg‎‎  style="width:32px;"> [Show element coordinate system](Assembly3_ShowElementCS.md): Show element coordinate system

:\* Workplane and origin. Adds a workplane, placement or origin. A part must be selected. This has five settings

:\*\* <img alt="" src=images/Assembly_Add_Workplane.svg‎‎  style="width:32px;"> [Add workplane](Assembly3_AddXYWorkplane.md): Add XY workplane

:\*\* <img alt="" src=images/Assembly_Add_WorkplaneXZ.svg‎‎  style="width:32px;"> [Add XZ workplane](Assembly3_AddXZWorkplane.md): Add XZ workplane

:\*\* <img alt="" src=images/Assembly_Add_WorkplaneZY.svg‎‎  style="width:32px;"> [Add ZY workplane](Assembly3_AddZYWorkplane.md): Add YZ workplane

:\*\* <img alt="" src=images/Assembly_Add_Placement.svg‎‎  style="width:32px;"> [Add placement](Assembly3_AddPlacement.md): Add placement

:\*\* <img alt="" src=images/Assembly_Add_Origin.svg‎‎  style="width:32px;"> [Add Origin](Assembly3_AddOrigin.md): Add Origin

:\* <img alt="" src=images/Assembly_TreeItemUp.svg‎‎  style="width:32px;"> [Move item up](Assembly3_MoveItemUp.md): Move selected tree item up

:\* <img alt="" src=images/Assembly_TreeItemDown.svg‎‎  style="width:32px;"> [Move item down](Assembly3_MoveItemDown.md): Move selected tree item down

:\*: Allows to sort Parts, Elements or Constraints in the tree. Element roll over (top to bottom and vice versa). Only works for a single selection.

:\* <img alt="" src=images/Assembly_ConstraintMultiply.svg‎‎  style="width:32px;"> [Multiply constraint](Assembly3_MultiplyConstraint.md): Multiply Constraint. This can be selected if multiple parts and suitable Elements are present.

:\*: It is used e.g. to assign multiple fasteners of the same type into multiple holes with one constraint.


</div>


</div>


<div class="mw-translate-fuzzy">

:\* \"Bloccare\" il primissimo vincolo. In ogni assemblaggio una parte deve essere bloccata per agire come parte base. Bloccare non significa altro che vincolare questa parte in 6DOF alla sua posizione e orientamento attuali.


</div>


:   <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width:28px;">


<div class="mw-collapsible mw-collapsed">


:   Some tools are actually a menu for more tools.


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:32px;"> [Locked](Assembly3_ConstraintLock.md): Add a \"Locked\" constraint to fix one or more parts.

:\*: You must select a geometry element of the part.

:\*: If you fix a vertex or an edge the part is still free to rotate around the vertex or edge.

:\*: Fixing a face will completely lock the part.

:\* <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width:32px;"> [Plane Alignment](Assembly3_ConstraintAlignment.md): Add a \"Plane alignment\" constraint to align planar faces of two or more parts.

:\*: The faces become coplanar or parallel with an optional distance.

:\* <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:32px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence.md): Add a \"Plane coincidence\" constraint to coincide planar faces of two or more parts.

:\*: The faces are coincided at their centers with an optional distance.

:\* <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width:32px;"> [Attachment](Assembly3_ConstraintAttachment.md): Add an \"Attachment\" constraint to attach two parts by the selected geometry elements.

:\*: This constraint completely fixes the parts relative to each other.

:\* <img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width:32px;"> [Axial Alignment](Assembly3_ConstraintAxial.md): Add an \"Axial alignment\" constraint to align edges/faces of two or more parts.

:\*: The constraint accepts

:\*:: linear edges, which become collinear,

:\*:: planar faces, which are aligned using their surface normal axis,

:\*:: and cylindrical face, which are aligned using the axial direction.

:\*: Different types of geometry elements can be mixed.

:\* <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width:32px;"> [Same orientation](Assembly3_ConstraintSameOrientation.md): Add a \"Same orientation\" constraint to align faces of two or more parts.

:\*: The planes are aligned to have the same orientation (i.e. rotation)

:\* <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width:32px;"> [Multi parallel](Assembly3_ConstraintMultiParallel.md): Add a \"Multi parallel\" constraint to make planar faces or linear edges of two or more parts parallel.

:\* <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width:32px;"> [Angle](Assembly3_ConstraintAngle.md): Add an \"Angle\" constraint to set the angle of planar faces or linear edges of two parts.

:\* <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width:32px;"> [Perpendicular](Assembly3_ConstraintPerpendicular.md): Add a \"Perpendicular\" constraint to make planar faces or linear edges of two parts perpendicular.

:\* <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width:32px;"> [Points coincident](Assembly3_ConstraintPointsCoincident.md): Add a \"Point coincident\" constraint to coincide two points in 2D or 3D.

:\* <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width:32px;"> [Point on plane](Assembly3_ConstraintPointInPlane.md): Add a \"Point on plane\" to constrain one or more point onto a plane.

:\* <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:32px;"> [Point on line](Assembly3_ConstraintPointOnLine.md): Add a \"Point on line\" to constrain a point onto a line in 2D or 3D.

:\* <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width:32px;"> [Point on circle](Assembly3_ConstraintPointOnCircle.md): Add a \"Point on circle\" to constrain one or more points on to a clyndrical surface defined by a cricle.

:\*: Note that you must select a point (any geometry element can define a point), and then select the circle (or clyndrical surface),

:\*: after which you can add more points to your selection if you want.

:\* <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width:32px;"> [Points distance](Assembly3_ConstraintPointsDistance.md): Add a \"Points distance\" to constrain the distance of two or more points.

:\* <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width:32px;"> [Point plane distance](Assembly3_ConstraintPointPlaneDistance.md): Add a \"Point plane distance\" to constrain the distance between one or more points and a plane.

:\* <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width:32px;"> [Point line distance](Assembly3_ConstraintPointLineDistance.md): Add a \"Point line distance\" to constrain the distance between a point and a linear edge in 2D or 3D.

:\* <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width:32px;"> [Symmetric](Assembly3_ConstraintSymmetric.md): Add a \"Symmetric\" constraint to make geometry elements of two parts symmetric about a plane.

:\*: The supported elements are linear edge and planar face.

:\* <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width:32px;"> [More](Assembly3_ConstraintMore.md): Toggle toolbars for more constraints

:\*: Not really a constraint but a toggle switch to show/hide the **Additional Constraints Toolbars**.


</div>


</div>

#### Additional Constraints Toolbars 

:   <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width:28px;"> (Assembly3 Constraints2)





:   <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width:28px;"> (Assembly3 Sketch Constraints)


<div class="mw-collapsible mw-collapsed">


:   You can enable these by selecting the **<img src="images/Assembly_ConstraintMore.svg‎‎" width=16px> [More](Assembly3_ConstraintMore.md)** button on the Main Constraints toolbar.


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width:32px;"> [Point distance](Assembly3_ConstraintPointDistance.md): Add a \"Point distance\" to constrain the distance of two points in 2D or 3D.

:\* <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width:32px;"> [Equal angle](Assembly3_ConstraintEqualAngle.md): Add an \"Equal angle\" to equate the angles between two lines or normals.

:\* <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width:32px;"> [Points symmetric](Assembly3_ConstraintPointsSymmetric.md): Add a \"Points symmetric\" constraint to make two points symmetric about a plane.

:\* <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:32px;"> () [Symmetric horizontal](Assembly3_ConstraintSymmetricHorizontal.md): Symmetric horizontal

:\* <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:32px;"> () [Symmetric vertical](Assembly3_ConstraintSymmetricVertical.md): Symmetric vertical

:\* <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width:32px;"> [Symmetric line](Assembly3_ConstraintSymmetricLine.md): Add a \"Symmetric line\" constraint to make two points symmetric about a line.

:\* <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width:32px;"> [Points horizontal](Assembly3_ConstraintPointsHorizontal.md): Add a \"Points horizontal\" constraint to make two points horizontal with each other when projected onto a plane.

:\* <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width:32px;"> [Points vertical](Assembly3_ConstraintPointsVertical.md): Add a \"Points vertical\" constraint to make two points vertical with each other when projected onto a plane.

:\* <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width:32px;"> [Line horizontal](Assembly3_ConstraintLineHorizontal.md):Add a \"Line horizontal\" constraint to make a line segment horizontal when projected onto a plane.

:\* <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width:32px;"> [Line vertical](Assembly3_ConstraintLineVertical.md): Add a \"Line vertical\" constraint to make a line segment vertical when projected onto a plane.

:\* <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width:32px;"> [Arc line tangent](Assembly3_ConstraintArcLineTangent.md): Add an \"Arc line tangent\" constraint to make a line tangent to an arc at the start or end point of the arc.

:\* <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width:32px;"> [Sketch plane](Assembly3_ConstraintSketchPlane.md): Add a \"Sketch plane\" to define the work plane of any draft element inside or following this constraint.

:\*: Add an empty \"Sketch plane\" to undefine the previous work plane.

:\* <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width:32px;"> [Line length](Assembly3_ConstraintLineLength.md): Add a \"Line length\" constrain the length of a non-subdivided Draft.Wire.

:\* <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width:32px;"> [Equal length](Assembly3_ConstraintEqualLength.md): Add an \"Equal length\" constraint to make two lines of the same length.

:\* <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width:32px;"> [Length ratio](Assembly3_ConstraintLengthRatio.md): Add a \"Length ratio\" to constrain the length ratio of two lines.

:\* <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width:32px;"> [Length difference](Assembly3_ConstraintLengthDifference.md): Add a \"Length difference\" to constrain the length difference of two lines.

:\* <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width:32px;"> [Length Equal Point Line Distance](Assembly3_ConstraintLengthEqualPointLineDistance.md): Add a \"Length Equal Point Line Distance\" to constrain the distance

:\*: between a point and a line to be the same as the length of a another line.

:\* <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:32px;"> ( <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width:32px;"> )[Equal Line Arc Length](Assembly3_ConstraintEqualLineArcLength.md): Add an \"Equal Line Arc Length\" constraint to make a line of the same length as an arc.

:\* <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width:32px;"> [Mid point](Assembly3_ConstraintMidPoint.md): Add a \"Mid point\" to constrain a point to the middle point of a line.

:\* <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width:32px;"> [Diameter](Assembly3_ConstraintDiameter.md): Add a \"Diameter\" to constrain the diameter of a circle/arc.

:\* <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width:32px;"> [Equal radius](Assembly3_ConstraintEqualRadius.md): Add an \"Equal radius\" constraint to make two circles/arcs of the same radius.

:\* <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width:32px;"> [Points project distance](Assembly3_ConstraintPointsProjectDistance.md): Add a \"Points project distance\" to constrain the distance of two points projected on a line.

:\* <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width:32px;"> [Equal point line distance](Assembly3_ConstraintEqualPointLineDistance.md): Add an \"Equal point line distance\" to constrain the distance

:\*: between a point and a line to be the same as the distance between another point and line.

:\* <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width:32px;"> [Colinear](Assembly3_ConstraintColinear.md): Add a \"Colinear\" constraint to make two lines collinear.


</div>


</div>


<div class="mw-translate-fuzzy">


:   Le **Barre dei vincoli** saranno l\'interfaccia principale utilizzata per l\'assemblaggio delle parti. Sono grigie di default, ma vengono attivate una volta selezionata almeno una faccia, una linea o un punto di una parte. Generalmente si selezionano gli elementi che devono essere uniti e poi si seleziona il tipo di vincolo. Le diverse cornici colorate contrassegnano le diverse caratteristiche dei vincoli: se è possibile aggiungere più di 2 elementi in 2D/3D. Una descrizione dettagliata si trova nel wiki di Gibhub.


</div>


<div class="mw-translate-fuzzy">


:   <img alt="" src=images/Assembly3_ToolbarNavigation.jpg  style="width:100px;">
:   *Barra degli strumenti di navigazione*
:   Queste funzioni sono utili quando si lavora con un assemblaggio con una gerarchia di file esterni collegati
    -   Selezionare l\'oggetto pezzo corrispondente nel gruppo di relazioni
    -   Selezionare l\'oggetto collegato
    -   Selezionare l\'oggetto link più profondo


</div>


<div class="mw-collapsible mw-collapsed">


:   Theses functions are useful when working with an assembly with a hierarchy of linked external files


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_GotoRelation.svg‎‎  style="width:32px;"> [Go to relation](Assembly3_GoToRelation.md): Reveals the Relations group (hidden by default) and selects a relation object.

:\* <img alt="" src=images/Std_LinkSelectLinked.svg  style="width:32px;"> [Select linked object](Std_LinkSelectLinked.md): Selects the linked object and switches to its document. <small>(v0.19)</small> 

:\* <img alt="" src=images/Std_LinkSelectLinkedFinal.svg  style="width:32px;"> [Select linked final](Std_LinkSelectLinkedFinal.md): Selects the deepest linked object and switches to its document. <small>(v0.19)</small> 


</div>


</div>


<div class="mw-translate-fuzzy">


:   <img alt="" src=images/Assembly3_ToolbarMeasurement.jpg  style="width:100px;">
:   *Barra degli strumenti di misura*
:   La **Barra degli strumenti di misura** aggiunge funzioni per misurare le distanze tra due punti, un punto e una retta o un punto e una faccia. Lo strumento *Misura angolo* traccia l\'angolo tra due facce o rette. Non esiste una funzione per misurare un raggio o un diametro.
:   Gli strumenti di misura sopravvivono ai cambiamenti del pezzo, ad esempio la distanza tra i bordi di un cubo quando il cubo viene ridimensionato. Come i vincoli, i calcoli sono fatti in tempo reale e aggiornati ad ogni cambiamento. Dietro le quinte, la funzione è molto simile alla funzione [vincoli](#Constraints.md). La distanza o l\'angolo viene calcolata tra [elementi](#Elements.md) come per i[vincoli](#Constraints.md). Il visualizzatore nell\'albero funziona allo stesso modo.


</div>


:   <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_MeasurePointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_MeasurePointPlaneDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_MeasureAngle.svg‎‎  style="width:28px;">


<div class="mw-collapsible mw-collapsed">


:   The **Measurement toolbar** adds functions to measure the distance or the angle between two objects


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width:32px;"> [Measure points](Assembly3_MeasurePoints.md): Add a \"Measure points\" to measure the distance of two points in 2D or 3D.

:\* <img alt="" src=images/Assembly_MeasurePointLineDistance.svg‎‎  style="width:32px;"> [Measure point to line](Assembly3_MeasurePointLine.md): Add a \"Measure point to line\" to measure the distance between a point and a linear edge in 2D or 3D.

:\* <img alt="" src=images/Assembly_MeasurePointPlaneDistance.svg‎‎  style="width:32px;"> [Measure point to plane](Assembly3_MeasurePointPlane.md): Add a \"Measure point to plane\" to measure the distance between a point and a plane.

:\* <img alt="" src=images/Assembly_MeasureAngle.svg‎‎  style="width:32px;"> [Measure angle](Assembly3_MeasureAngle.md): Add a \"Measure angle\" to measure the angle of planar faces or linear edges of two parts.

:   There is no function to measure a radius or diameter.
:   The measurement tools survive part changes, e.g. the distance between edges of a cube when the cube is re-sized.
:   As the constraints the calculations are done in real time and updated upon any change. Behind the scenes, the function is very similar to the [constraints](#Constraints.md). The distance or angle is calculated between [Elements](#Elements.md) in the same way as for [constraints](#Constraints.md). The display in the tree works in the same way.


</div>


</div>

Come al solito è possibile modificare le barre degli strumenti e aggiungere o rimuovere singoli strumenti. Accertarsi di controllare nel menu Assembly3 le funzioni che potrebbero non essere presenti nelle barre degli strumenti.

[Torna all\'inizio](#top.md)


<div class="mw-translate-fuzzy">

### Vincoli

Il progettista utilizza i vincoli per ottenere il risultato desiderato nella relazione tra due parti. L\'arte è la selezione dei giusti vincoli più adatti ad affrontare ogni problema. Ogni DOF eliminato dovrebbe in teoria essere eliminato solo una volta tra due oggetti, ma in pratica con molti strumenti CAD i vincoli selezionati causano combinazioni di vincoli eccessivi, spesso compensati da algoritmi complessi, a volte no. Assembly3 utilizza algoritmi per rilevare e compensare gli eccessi di vincoli, ma chiaramente non sono ancora molto maturi. Quindi in pratica per i vincoli di Assembly3 si evitano problemi essendo consapevoli di quanti gradi di libertà (DOF) sono stati utilizzati e quali devono ancora essere bloccati dai vincoli. Nessuna parte dovrebbe avere una connessione di vincoli utilizzati maggiore di 6DOF.


</div>


<div class="mw-translate-fuzzy">


:   Nota: Se il risolutore incontra una combinazione che non può essere risolta, darà un errore. È molto difficile per il risolutore scoprire cosa ha causato il problema, quindi tipicamente da questo errore dato non sarà chiaro *dove* è il problema. In assemblaggi più grandi questo può portare a ricerche complesse del problema. Purtroppo non c\'è un modo semplice per evitarlo. Tuttavia, aiuta essere pienamente consapevoli di come funziona il sistema (.e.g. vedi [Elementi](#Elements.md) qui sotto), utilizzare nomi chiari per tutti i componenti coinvolti e aggiungere vincoli aggiuntivi solo quando il risolutore risolve l\'assemblaggio corrente. Molto utile per rintracciare un problema è la funzione \"ContexMenu/Deactivate\" di ogni Vincolo.


</div>

Assembly3 I vincoli definiscono le restrizioni nella posizione o nell\'orientamento tra due [Elementi](#Elements.md). Alcuni vincoli funzionano anche con più di due [Elementi](#Elements.md). Un [Elemento](#Elements.md) può essere una faccia, una linea o un bordo o un punto di una parte. Generalmente i vincoli sono definiti selezionando gli [Elementi](#Elements.md) e poi selezionare il vincolo dai Vincoli [toolbar](#Toolbars.md).

-   Fissa 6 DOF, lascia 0 DOF:
    -   **Lock**: Il blocco del vincolo fissa tutti i DOF per una faccia. Dovrebbe essere usato per una parte di base in ogni assemblaggio. Si può anche attivare la funzione \"MoveLock\" (nella barra degli strumenti) in modo che il pezzo non possa essere spostato accidentalmente. Normalmente non importa quale faccia/linea/punto si usa per fissare un pezzo. Si noti inoltre che il blocco è valido solo per l\'assemblaggio diretto, cioè nel caso di un sottoinsieme l\'assemblaggio principale richiederebbe comunque una parte bloccata.
    -   **Attachment**: Rende i sistemi di coordinate di entrambi gli elementi uguali per tutti gli assi. Questa è la funzione più comoda per il calcolo e dovrebbe essere usata dove possibile. Si noti che si potrebbero usare le proprietà degli elementi per compensare gli offset e gli angoli se i due [elementi](#Elements.md) non sono perfettamente allineati.
-   Fissa 5 DOF, lascia 1 DOF:
    -   **Plane Coincident**: fissa Tx,Ty,Tz, Rx,Ry. Solo Rz è libero. Rimane la rotazione intorno al normale che passa attraverso il *centro del piano*.
-   Fissa 4 DOF, lascia 2 DOF:
    -   **Axial Alignment**: fissa Tx,Ty, Rx,Ry. Solo Tz, Rz sono liberi. Rimangono la rotazione intorno all\'asse della figura e la traslazione lungo questo stesso asse. Due vincoli *PointOnLine* (se i due punti sono diversi) danno lo stesso risultato. Come anche i vincoli\''Colinear\''.
    -   **PointOnLine**: In questo modo si elimina la traslazione e la rotazione lungo le normali verso la linea di riferimento. Sono consentite solo la traslazione e la rotazione lungo l\'asse della linea.
-   Fissa 3 DOF, lascia 3 DOF:
    -   **Same Orientation**: fissa Rx,Rz,Rz. Tutte le T rimangono libere.
    -   **Points Coincident**: fissa Tx,Ty,Tz. Tutte le R rimangono libere.
    -   **PointOnPoint** Il vincolo elimina le 3 traslazioni.
    -   **Plane Alignment**: fissa Tz, Rx,Ry. In movimento il piano e Rz. Questo elimina la traslazione lungo il piano normale verso il piano di riferimento e le due rotazioni intorno agli assi di questo piano.
-   Fissa 2 DOF, lascia 4 DOF:
    -   **Multi Parallel**: fissa Rx,Ry. rimangono tutte le T e le Rz. Questo elimina le due rotazioni intorno agli assi del piano di riferimento.
-   Fissa 1 DOF, lascia 5 DOF:
    -   **Points in Plane**: Fissa Tz. Questo elimina la traslazione lungo il piano normale verso il piano di riferimento.
    -   **Points Distance**: fissa la distanza tra le origini dell\'elemento.

        :   Questo ti dà più libertà rispetto a *Points in Plane*

Altro

-   **Points on Circle**: fissa Tz e parzialmente Tx,Ty. Congela la traslazione del punto (o più punti) su un cerchio o su un\'area del disco. Devi scegliere il cerchio per secondo. Questo lascia tutte le rotazioni libere e dà una traslazione limitata nel piano di riferimento del cerchio.

\'\': Nota: Nella seguente lista Tx,Ty,Tz e Rx,Ry,Rz sono usati per descrivere le traslazioni e le rotazioni dei sistemi di coordinate di riferimento dell\'elemento interessato. Questo non è sempre esatto o completamente definito, ad esempio quando è coinvolta una linea non è definito se corre in X, Y o qualsiasi altro angolo in mezzo. Il sistema è usato per un breve e facile comparazione a favore di una definizione corretta ma più complessa. Quindi Z è generalmente la direzione normale di tutte le facce coinvolte. Sentitevi liberi di modificarla con un approccio migliore con una migliore leggibilità\".

[Torna all\'inizio](#top.md)

Elements è un termine specifico usato nel banco di lavoro Assembly3 ed è importante capire Elements per capire come Assembly3 deve essere usato.

È utile pensare a un elemento come parola generale per un \"elemento selezionabile\" di una parte, cioè una faccia, un bordo, un cerchio o un angolo o un altro punto. Gli elementi che si selezionano per vincolarli, sono quegli elementi. Nell\'albero una cartella Assembly ha tre sottocartelle. Accanto a \'Parts\' e \'Constraints\' c\'è una cartella chiamata \'Elements\', che è vuota finché non vengono aggiunti vincoli. Quando si aggiunge un vincolo il vincolo stesso ottiene due (o più) linee, questi sono gli \'Elementi\' selezionati. Anche questi vengono aggiunti nella cartella \'Elements\' che è solo un elenco di tutti gli elementi utilizzati nell\'assieme. E\' una buona idea cambiare i loro nomi (con il tasto F2), specialmente negli assemblaggi più grandi.

Vediamo un esempio

:   Creare un nuovo file e aggiungere dal banco di lavoro Part un cubo e un cilindro.Impileremo il cilindro sul cubo. Prima fissiamo la parte base, nel nostro caso il cubo. Selezioniamo la faccia inferiore del cubo e selezioniamo i vincoli \"Bloccato\" (prima icona nei Vincoli [barra degli strumenti](#Toolbars.md)). Selezionare la faccia superiore del cilindro e la faccia superiore del cubo. Quindi selezionare il vincolo \"Plane Coincident\". Ora il cilindro viene spostato nel cubo e nell\'albero è stata aggiunta una nuova foglia con due nodi figli sotto \"Constraints\". Inoltre gli stessi due nodi figli sono stati aggiunti sotto \"Elements\". Se il cilindro si trova all\'interno del cubo invece che sopra il cubo, correggiamo prima questo: sotto \'Constraints\' selezionate il nodo figlio che mostra la faccia del cilindro e con un clic destro del mouse nel menu contestuale selezionate \'Flip Part\'. Ora il cilindro è impilato sul cubo.

La chiave per capire è che il vincolo opera sui collegamenti agli elementi nella lista della cartella ad albero \'Elements\'. Questo permette di mantenere intatta la struttura del vincolo mentre si cambiano le parti. Questo è molto difficile da comprendere senza un esempio.

Torniamo all\'esempio precedente

:   Nota: assicurarsi di aver aggiunto il vincolo \"Lock\" al cubo o questo sembrerà disorientante
:   Nella finestra CAD selezionare un\'altra faccia del cubo. Ora lavoriamo solo nella vista ad albero. Andate con il mouse nell\'albero dove il cubo deve apparire selezionato. Trascinare il cubo nella cartella \"Elements\". Trascinatelo sul nome \'Elements\', in nessun altro punto della cartella vedremo in seguito il motivo. Dovreste vedere che un altro Elemento viene aggiunto alla lista degli \'Elementi\'. Ora selezionate nella cartella \'Constraints\' il nodo figlio della faccia del cubo nel vincolo \"Plane Coincident\" e cancellatelo. Il Vincolo mostrerà un punto esclamativo poiché manca un elemento. Si noti che cancellando l\'elemento in Constraint non lo abbiamo cancellato dalla lista. Questo perché nel vincolo c\'era solo un link all\'Elemento. Ora prendiamo l\'Elemento appena aggiunto nella lista \'Elements\' e lo trasciniamo sul vincolo \"Plane Coincident\". Ora il cilidro si sposta sull\'altra faccia che abbiamo selezionato. Potremmo aver bisogno di selezionare di nuovo \'Flip Part nel menu contestuale\' se il cilindro è di nuovo all\'interno del cubo.

L\'esempio ha mostrato che senza rimuovere il vincolo possiamo cambiare gli Elementi che vengono utilizzati per il vincolo. Allo stesso modo possiamo spostare il cilindro in una parte totalmente diversa. Dopo aver giocato un po\' di più con questo esempio, si noteranno alcune cose aggiuntive come

-   Se si rinomina un elemento nella lista, il nome verrà cambiato in tutti i Vincoli.
-   è possibile utilizzare un elemento della lista in diversi vincoli.
-   È possibile utilizzare la finestra delle proprietà di un elemento per aggiungere **Offset**. Nell\'esempio questo potrebbe spostare il cilindro sulla faccia del cubo.
-   è possibile utilizzare il pulsante \"Show Element Coordinate System\" nella barra degli strumenti principale per vedere le funzioni \'Menu contestuale/Flip Part\' e \'Menu contestuale/Flip Element\'. Assicuratevi di guardare cosa succede nella finestra delle proprietà.
-   è possibile aggiungere un vincolo in un ordine completamente diverso: Per prima cosa aggiungere alcuni elementi alla \'Lista degli elementi\' (la denominazione è utile, es. \"Cube Top Face\" o \"Cube Front Face\"), poi aggiungere un vincolo senza selezionare nulla - sarà un vincolo vuoto. Quindi trascinare gli Elementi dalla lista \'Elements\'. Il risultato è lo stesso di quello che abbiamo fatto nel primo esempio. Dopo aver fatto questo esercizio, la natura di come funzionano i vincoli con gli Elementi dovrebbe essere chiara.
-   potete cambiare un vincolo esistente tra elementi esistenti semplicemente selezionando un elemento diverso nella Finestra delle proprietà/ConstraintType.

[Torna all\'inizio](#top.md)

## Compatibilità

Assembly3 è stato ispirato da [Assembly2](Assembly2_Workbench.md), ma non è con questo compatibile . Se avete modelli precedenti realizzati in Assembly2, dovreste rimanere con FreeCAD 0.16 e usare Assembly2.

I nuovi modelli sviluppati con Assembly3 devono essere aperti e modificati solo con questo banco di lavoro.

Anche se possono avere strumenti simili, Assembly3 non è compatibile con [A2plus](A2plus_Workbench.md) né con [Assembly4](Assembly4_Workbench.md). I modelli creati con questi workbenches devono essere aperti solo con il rispettivo workbench.

[Torna all\'inizio](#top.md)

## Test

Il [Assembly3 Workbench](Assembly3_Workbench.md) è in fase di sviluppo e non è ancora disponibile (aprile 2020) tramite lo [Addon Manager](Std_AddonMgr.md), ma si prevede che ciò avverrà prima o poi.

Si può provare in due modi:

-   Uno speciale fork di FreeCAD realizzata da realthunder; vedi [FreeCAD\_assembly3 releases](https://github.com/realthunder/FreeCAD_assembly3/releases). Questo fork si basa su un particolare commit del ramo master di FreeCAD, ma ha anche caratteristiche aggiuntive attualmente non presenti nel ramo master. Dato che questo fork è basato su un particolare snapshot di sviluppo, non ha le ultime caratteristiche unite quotidianamente al ramo master.
-   Lo sviluppo [AppImage](AppImage.md); questo si basa sul ramo master corrente, e include le dipendenze necessarie per lavorare con Assembly3 come il solutore SolveSpace.

Dato che l\'AppImage funziona solo per Linux, per gli utenti Windows al momento l\'unica opzione per testare Assembly3 è la prima opzione (realthunder\'s fork).

[Torna all\'inizio](#top.md)

## Come fare 

#### Cominciamo

Ci sono molti modi per creare un assemblaggio con Assembly3. Ecco il più semplice che si possa fare.

:   <img alt="" src=images/Assembly3_Example-GettingStarted.jpg  style="width:600px;">
:   *Risultato finale del primo esempio. Nell\'immagine è selezionato il banco di lavoro Assembly3 Worksbench, quindi sono visibili le sue barre degli strumenti multiple. Si noti che la \"TabBar\" verticale a sinistra della vista ad albero è un AddOn Workbench che non è contenuto nel FreeCAD standard (ma può essere installato con l\'Addon-Manager)*\'.


<div class="mw-translate-fuzzy">

-   Creare un nuovo file FreeCAD
-   Selezionare il Workbench di montaggio. Selezionare *CreateAssembly* (prima icona)
-   Selezionare Part Workbench e aggiungere un cilindro e un cubo
-   Salva il file con il nome del file che preferisci. Chiudere e aprire il file.

    :   La vista ad albero dovrebbe avere questo aspetto


```python
 Assembly
   Constraints
   Elements
   Parts
 Cilindro
 Cubo
```

-   Ora disegnare e rilasciare con il mouse sia *Cilindro* che *Cubo* nella cartella *Parts*. Verranno spostati in quella cartella.

    :   Questo è il modo più veloce. Si noti che il modo *migliore*\' è quello di aprire il menu contestuale su entrambi e selezionare *ContetxMenu/LinkActions/MakeLink*. Questo aggiunge due file di link. Poi trascina i file di collegamento nella cartella *Parts*. Per casi semplici come questo non ha molta importanza.
-   Cliccare entrambe le superfici superiori di Cylinder e Cube (tenere premuto Ctrl)
-   Selezionare assembly Workbench. Selezionare \"PlaceCoincident\" dalla [Barra dei vincoli principali](#Toolbar.md).

    :   Ora le parti dovrebbero essere unite l\'una all\'altra e il vostro albero dovrebbe avere questo aspetto


```python
 Assembly
   Constraints
      PlaneConicident
        _Element
        _Element001
   Elements
        _Element
        _Element001
   Parts
      Cilindro
      Cubo
```

-   Cliccare con il tasto destro del mouse su uno dei due \"\_Element\" e selezionare \"Flip Part\".

    :   Ora il Cilindro dovrebbe essere sopra la scatola. Se il tutto è sottosopra, tornare indietro e selezionare \"Flip Part\" sull\'altro elemento.

Abbiamo omesso un passo importante che dovrebbe essere fatto negli assemblaggi più grandi: bloccare una parte base. Ciò significa definire una parte che non deve essere spostata da vincoli. Nel vostro caso per questo usiamo il cubo:

-   Selezionare la faccia inferiore del cubo. Solo la faccia inferiore, non l\'intero cubo.
-   selezionare il vincolo \"Lock\" dalla barra degli strumenti dei vincoli

    :   L\'albero di montaggio finito dovrebbe apparire come nell\'immagine qui sopra

Fatto.
Se volete nell\'albero potete spostare verso l\'alto il vincolo \"Bloccato\". Utilizzare il pulsante \"MoveItemUp\" nella barra [Barra degli strumenti principale](#Toolbar.md).


</div>

The tree view should look like this (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-01.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-02.png  style="width:280px;">

-   Now *Drag&Drop* with the mouse both **Cylinder** and **Cube** onto the **Parts** folder. They are moved into that folder.

    :   That is the quickest way and suitable for simple cases like this. A better way is via the use of link objects:
    :   Select **Cube** and **Cylinder** and then **<img src="images/Std_LinkMake.svg" width=16px> [Make link](Std_LinkMake.md)** either from the **Context menu** (-\> LinkActions -\> MakeLink) or the **Structure** panel.
    :   This adds two link objects. Then *Drag&Drop* the link objects to the **Parts** folder.
-   Click both top surfaces of **Cylinder** and **Cube** (keep Ctrl pressed (Cmd on a Mac))
-   Change to <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench.md) workbench
-   Select **<img src="images/Assembly_ConstraintCoincidence.svg‎‎" width=16px> [Plane Coincidence](Assembly3_ConstraintCoincidence.md)** from the [Main constraints toolbar](#Main_Constraints_Toolbar.md).

Now the parts should be joined into each other and your tree should look like this (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-03.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-04.png  style="width:280px;">

-   Right click **\_Element** (either of the two) and select **Flip Part**.

Now the **Cylinder** should be on top of the **Cube**. If the whole thing is upside down, go back and select **Flip Part** on the other element.

:   We omitted one important step that should be done in larger assemblies: Locking a base part.
:   That means to define one part that should not be moved by constraints. In this example we use the **Cube** for that:
    -   Select the lower face of the **Cube**. Only the lower face, not the whole **Cube**
    -   select the **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Locked](Assembly3_ConstraintLock.md)** constraint from the [Main constraints toolbar](#Main_Constraints_Toolbar.md)

Done.

The finished assembly tree should look like (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-05.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-06.png  style="width:280px;">:

If you like you can move the **Locked** constraint upwards in the tree. Use the **<img src="images/Assembly_TreeItemUp.svg‎‎" width=16px> [Move item up](Assembly3_MoveItemUp.md)** button on the [Main toolbar](#Main_Toolbar.md) for that.


<div class="mw-translate-fuzzy">

Nota: tutti i nuovi file esterni devono essere salvati, chiusi e riaperti almeno una volta, in modo che Assembly3 possa trovarlo. Senza fare questo FreeCAD non può dare una gestione dei file al Workbench Assembly3 e non può trovare il nuovo pezzo. Quando tutte le parti sono nello stesso file, è necessario salvare e riaprire il file.


</div>

[Torna all\'inizio](#top.md)

#### Aggiungete un Offset 

Il montaggio3 non offre l\'Offset con i vincoli nel modo in cui lo fanno [A2plus Workbench](A2plus_Workbench.md) o altri strumenti CAD. Offre invece un sistema più generale e flessibile per aggiungere traslazioni offset ma anche angoli.

-   Aggiungere l\'offset nelle proprietà [Vincolo](#Constraint.md) di un [Elemento](#Elements.md).

    :   è possibile scegliere quale dei due utilizzare.

Esempio:

-   Aggiungere 2 cubi ad un gruppo e selezionare le loro facce laterali.
-   selezionare \"PlaneCoincident\". I cubi saranno attaccati l\'uno all\'interno dell\'altro.
-   selezionare un elemento e *Menu contestuale/Flip Part*. I cubi saranno attaccati uno accanto all\'altro.
-   selezionare una proprietà Element Offset/Position/Zz e impostare a 5mm. I cubi saranno distanziati di 5mm.

Test con altri assi o con i campi angolo/asse. Verificare anche che si ottenga lo stesso risultato quando si utilizza l\'altro Elemento. Questo è lo stesso approccio per tutti gli altri vincoli

[Torna all\'inizio](#top.md)


<div class="mw-translate-fuzzy">

#### Risolvi un errore del risolutore 

Questo accade spesso quando le parti sono eccessivamente vincolate, cioè più di 6 DOF sono bloccati.


</div>

Il modo più semplice per trovare il problema è cliccare sui vincoli rilevanti nell\'albero e selezionare *Menu contestuale/Disable* e ricalcolare. È utile conoscere gli ultimi vincoli aggiunti prima che il risolutore fallisca e semplicemente annullarli.

Nota: poiché l\'Assemblaggio3 cerca di compensare le parti eccessivamente vincolate dietro le quinte, a volte il problema è innescato solo da un nuovo vincolo, ma la causa alla radice è da qualche altra parte. Prima di cancellare tutto e ricominciare da capo, ricordate che potete riutilizzare gli Elementi. Se li avete nominati potete identificare gli elementi richiesti e ricostruire i vincoli senza usare affatto la vista 3D. Vedi [Elementi](#Elements.md) sopra

[Torna all\'inizio](#top.md)

### Sostituire una parte o rinominare un nome di file 

Quando una parte viene rimossa o quando un nome di file cambia, l\'assemblaggio si rompe, non può più essere risolto e il risolutore emetterà il messaggio \"Vincoli incoerenti\". Il risolutore contrassegnerà nell\'albero Elementi e Vincoli non validi con un punto interrogativo.

Un modo per risolvere questo problema è quello di eliminare tutti i vincoli e gli elementi non validi, importare la nuova parte e rifare tutto. Ma c\'è un modo migliore:

-   Rinominare un file
    1.  Utilizzare un file manager e copiare il file che si desidera rinominare. Poi date il nuovo nome alla copia.
    2.  Aprire la copia in FreeCAD. Anche l\'assemblaggio e il vecchio file devono essere aperti
    3.  Selezionare il vecchio oggetto nell\'albero e cliccare per cambiare il proprio \"Oggetto collegato\" (contiene il vecchio nome del file)
    4.  Si aprirà una lista in una finestra di dialogo contenente tutte le parti aperte. Essa mostra i nomi dei file e gli oggetti di ogni parte. La vecchia parte e l\'oggetto sono selezionati. Individuare la parte rinominata nell\'albero e selezionare lo stesso oggetto nella nuova parte. Poi confermate la selezione.
    5.  Cancellare la parte vecchia dell\'albero. Ora anche il file può essere cancellato.
    6.  I vincoli e gli elementi della vecchia parte non sono più validi. Aprire la lista dei vincoli o degli elementi nell\'albero. Poi in sequenza
        -   selezionare ogni superficie dell\'elemento sulla nuova parte. Un oggetto nell\'albero sarà evidenziato.
        -   Prendete quell\'elemento e trascinatelo sopra il vecchio elemento (sia nell\'elenco degli elementi che in uno dei vincoli in cui è stato usato). Quell\'elemento dovrebbe diventare valido.
        -   Ripetere la procedura per gli altri elementi. Spesso un singolo elemento è sufficiente per permettere all\'Assembly3 di identificare automaticamente gli elementi rimanenti del pezzo.
        -   Se per errore un elemento è stato assegnato alla superficie sbagliata, è sufficiente ripetere l\'operazione con la superficie corretta.
    7.  Se si desidera, modificare il nome dell\'oggetto in FreeCAD

-   Sostituire una parte con un\'altra

    :   *ovviamente è necessario che sia abbastanza simile alla parte originale tanto che i vincoli originali hanno ancora un senso*

    1.  Cancellare la vecchia parte dall\'albero. Anche il file può essere cancellato.
    2.  I vincoli e gli elementi della vecchia parte non sono più validi. Aprire la lista dei vincoli o degli elementi nell\'albero.
        -   Selezionare una superficie sulla nuova parte. Un elemento nell\'albero sarà in alto.
        -   Prendete quell\'elemento e trascinatelo sopra il vecchio elemento (sia nell\'elenco degli elementi che in uno dei vincoli in cui è stato usato). Quell\'elemento dovrebbe diventare valido.
        -   ripetere la procedura per i restanti elementi.
        -   Se un elemento è stato assegnato per caso alla superficie sbagliata, basta ripetere con la superficie corretta.
    3.  Se si vuole, modificare il nome dell\'oggetto in FreeCAD.


<div class="mw-translate-fuzzy">

\'\'Nota
\* Non sono così complicate come qui può sembrare . Dopo 2-3 volte dovrebbero diventare naturali ed essere molto facili da fare.

-   Di solito non solo è più veloce di cancellare e rifare i vincoli, ma è anche più sicuro perché un elemento potrebbe essere usato in un assemblaggio parente. Cancellare l\'originale distruggerebbe quel collegamento, ri-assegnarlo lo manterrebbe.
-   Questa procedura diventa davvero veloce e facile da fare se si dà un nome ai vincoli e agli elementi. Non c\'è modo di indovinare dove le superfici devono essere trascinate, perché i nomi lo dicono (vedi [Consigli e suggerimenti](#Tips_&_Tricks.md)).

\'\'


</div>

[Torna all\'inizio](#top.md)

### Consigli e suggerimenti 

-   L\'utilizzo di assemblaggi gerarchici aiuta ad evitare problemi di risoluzione e a mantenere il modello fluido. È possibile congelare un sottoassieme con un clic e risparmiare facilmente le risorse della CPU (utilizzare il menu contestuale nell\'albero). Quando si carica un assemblaggio l\'assieme3 non ha bisogno di aprire file esterni per i sottoinsiemi congelati, il che mantiene l\'albero compatto.
-   È molto utile per abituarsi a dare un nome agli elementi e ai vincoli. Usare il tasto **F2** per farlo rapidamente nella struttura ad albero. Troverete molto utili gli strumenti di ordinamento dell\'albero nella barra degli strumenti principale. Un insieme con i vincoli e con elementi con nome completo è più facilmente comprensibile per le altre persone o per voi stessi quando guardate un file vecchio.

    :   Esempi di nomi di vincoli per una tabella potrebbero essere \"Align\_FrontLegs\", \"Align\_FrameBottom-LegTops\" e i nomi degli elementi potrebbero essere \"Leg1\_Top\" o \"TableTop\_Front\", \"TableTop\_Left\".
-   Si noti che una volta aperti i file esterni da un assemblaggio non è possibile chiuderli nuovamente senza chiudere l\'assemblaggio. Poiché l\'assemblaggio tiene aperti i file in backgound, la scheda può scomparire, ma il file rimane visibile nell\'albero. Se si dispone di più sottoinsiemi, diventa quasi impossibile chiudere i singoli file. Questo approccio potrebbe cambiare, ma fino ad allora un possibile metodo potrebbe essere quello di utilizzare regolarmente i comandi *File/Salva tutto* e *File/Chiudi tutto* per ripulire la struttura ad albero prima di lavorare su un altro sottoinsieme.

    :   \'\'Esempio: si consideri di avere una grande macchina CNC con un gruppo principale e un sottoinsieme per ogni modulo. Una volta aperto l\'assemblaggio principale, si possono aprire letteralmente centinaia di file fino a un singolo cuscinetto a sfere. Prima di lavorare sul sottoinsieme del quadro elettrico della macchina è una buona idea salvare e chiudere tutti i file per ottenere un albero vuoto. Poi aprire solo il sottoinsieme per il quadro elettrico. Questo aprirà tutti i file di cui ha bisogno, ma solo quelli.
-   L\'utilizzo di file esterni rende più facile il riutilizzo di una parte o il cambio di versione di una parte con sistemi come git o subversion. Il flusso di lavoro in FreeCAD con Assembly è simile a quello dei file che hanno tutte le parti nello stesso file. Per lo scambio frequente di file con altre parti, i file singoli potrebbero essere più convenienti.
-   Moltiplicare le parti collegate. Se si aggiunge un collegamento nell\'insieme, questo avrà un valore di proprietà denominato \"Element Count\", predefinito 0. Se lo si imposta a 3 si ottengono 3 istanze di quella parte. Saranno aggiunte in una sottocartella e possono essere usate come parti completamente separate. Usate questa funzione per mantenere bassa l\'impronta dei dati del vostro file, perché la parte viene salvata solo una volta. Ogni istanza contiene solo le differenze.
-   Inserire più parti, ad es. viti, con un clic. Consultare il [Assembly3 Wiki3 Wiki](https://github.com/realthunder/FreeCAD_assembly3/wiki/Constraints-and-Solvers) sul sito di Github. Questa non è solo una funzione sbalorditiva (anche un po\' magica), ma davvero molto utile.

-   L\'utilizzo del [TabBar Workbench](https://github.com/triplus/TabBar) accelera il lavoro con il montaggio. Questo aggiunge una barra degli strumenti con un pulsante per ogni banco di lavoro. È possibile ordinare la barra degli strumenti e metterla dove si vuole. Molte persone la mettono in verticale sul lato sinistro, proprio accanto alla vista ad albero. Avere Assembly3, Part, PartDesign e altri banchi da lavoro, spesso usati, vicino alla parte superiore, passare da uno all\'altro diventa estremamente facile.

[Torna all\'inizio](#top.md)

## Link


<div class="mw-translate-fuzzy">

-   [App Link](App_Link/it.md) oggetto che fa funzionare Assembly3.
-   [FreeCAD\_assembly3](https://github.com/realthunder/FreeCAD_assembly3) archivio e documentazione.
-   [Assembly3 preview](https://forum.freecadweb.org/viewtopic.php?f=20&t=25712), big discussion thread.
-   [Test tutorial for Assembly 3 WB](https://forum.freecadweb.org/viewtopic.php?f=36&t=29562) by jpg87.
-   [Current Assembly Status](https://forum.freecadweb.org/viewtopic.php?f=20&t=34583)
-   [Ambienti complementari](External_workbenches/it.md)
-   [Progetto di Assemblaggio](Assembly_project/it.md) piano di sviluppo, per conoscere la storia della materia.


</div>




_ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > Assembly3 Workbench/it
