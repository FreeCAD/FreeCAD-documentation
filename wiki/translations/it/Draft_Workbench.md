


 

<img alt="L\'icona di Draft" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Introduzione

L\'[Ambiente Draft](Draft_Module/it.md) <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> consente di disegnare semplici oggetti 2D e offre diversi strumenti per modificarli in seguito. Fornisce inoltre strumenti per definire un piano di lavoro, una griglia e un sistema di snap per controllare con precisione la posizione della geometria.

Gli oggetti 2D creati possono essere utilizzati per il disegno in modo simile a Inkscape o Autocad. Queste forme 2D possono anche essere utilizzate come componenti di base di oggetti 3D creati con altri ambienti di lavoro, ad esempio con <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Part](Part_Workbench/it.md) e <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Arch](Arch_Workbench/it.md). È anche possibile convertire gli oggetti Draft in <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [schizzi](Sketcher_Workbench.md), il che significa che le forme possono essere utilizzate anche con <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign](PartDesign_Workbench.md) per creare dei corpi solidi.

FreeCAD è principalmente un\'applicazione di modellazione 3D, quindi i suoi strumenti 2D non sono così avanzati come in altri programmi di disegno. Se l\'obiettivo principale è la produzione di disegni 2D complessi e di file [DXF](DXF/it.md), e non si ha bisogno di modelli 3D, si può prendere in considerazione un programma software dedicato al disegno tecnico come [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), e altri.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

## Strumenti per disegnare oggetti 

Questi sono gli strumenti per creare gli oggetti

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linea](Draft_Line/it.md): disegna un segmento delimitato da due punti.
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polilinea](Draft_Wire/it.md): disegna una spezzata o polilinea specificando tutti i punti intermedi.
-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Raccordo](Draft_Fillet/it.md): disegna un raccordo (angolo arrotondato) o uno smusso (linea retta) tra due semplici [Linee](Draft_Line/it.md). {{Version/it|0.19}}
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arco](Draft_Arc/it.md): disegna un arco di circonferenza a partire dal centro e specificando il raggio, l\'angolo iniziale e l\'angolo finale.
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arco da 3 punti](Draft_Arc_3Points/it.md): disegna un segmento di arco circolare da tre punti che si trovano nella circonferenza. {{Version/it|0.19}}
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Cerchio](Draft_Circle/it.md): disegna una circonferenza prendendo in input il centro e il raggio.
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellisse](Draft_Ellipse/it.md): disegna una ellisse.
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rettangolo](Draft_Rectangle/it.md): disegna un rettangolo specificando gli angoli opposti.
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Poligono](Draft_Polygon/it.md): disegna un poligono regolare da centro, raggio e numero di lati.
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-Spline](Draft_BSpline/it.md): interpola una traiettoria curvilinea passante per i punti specificati.
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Curva di Bézier cubica](Draft_CubicBezCurve/it.md): disegna una curva di Bézier di terzo grado trascinando due punti. {{Version/it|0.19}}
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Curva di Bezier](Draft_BezCurve/it.md): disegna curve di Bezier su una serie di punti.
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punto](Draft_Point/it.md): inserisce un oggetto punto.
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Lega facce](Draft_Facebinder/it.md): Facebinder crea un nuovo oggetto costituito dalle facce selezionate in una forma.

## Strumenti per le annotazioni 

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Testo](Draft_Text/it.md): disegna delle annotazioni multilinea.
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Forma da testo](Draft_ShapeString/it.md): ShapeString inserisce una forma composta da una stringa di testo.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Quota](Draft_Dimension/it.md): aggiunge la quotatura.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Etichetta](Draft_Label/it.md): posiziona un\'etichetta con una freccia che punta a un elemento selezionato {{Version/it|0.17}}
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Editor degli stili di annotazione](Draft_AnnotationStyleEditor/it.md): apre un editor per modificare lo stile di annotazione di questi oggetti. <small>(v0.19)</small> 

## Strumenti per modificare gli oggetti 

Si tratta degli strumenti per la modifica di oggetti esistenti. Lavorano su oggetti selezionati precedentemente, quando nessun oggetto è selezionato, si viene invitati a scegliere uno.

Molti strumenti operativi (spostamento, rotazione, array, ecc.) Funzionano anche su oggetti solidi di ([Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md), [Arch](Arch_Workbench/it.md), ecc.).

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Sposta](Draft_Move/it.md): sposta uno o più oggetti da una posizione a un\'altra.
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Ruota](Draft_Rotate/it.md): ruota uno o più oggetti da un angolo di partenza a un angolo finale.
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scala](Draft_Scale/it.md): scala gli oggetti in relazione a un punto base.
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Simmetria](Draft_Mirror/it.md): riflette gli oggetti selezionati.
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Scosta](Draft_Offset/it.md): duplica e scosta in modo equidistante i componenti di un oggetto.
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Taglia/Estendi](Draft_Trimex/it.md): accorcia o estende (estrude) l\'oggetto selezionato.
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stira](Draft_Stretch/it.md): stira gli oggetti selezionati. {{Version/it|0.17}}

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clona](Draft_Clone/it.md): clona gli oggetti selezionati.
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> Strumenti serie.
    -   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Serie ortogonale](Draft_OrthoArray/it.md): crea una serie ortogonale di copie dell\'oggetto selezionato. Si possono anche creare copie [App Link](App_Link/it.md). {{Version/it|0.19}}
    -   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Serie polare](Draft_PolarArray/it.md): crea una serie polare di copie dell\'oggetto selezionato. Si possono anche creare copie [App Link](App_Link/it.md). {{Version/it|0.19}}
    -   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Serie circolare](Draft_CircularArray/it.md): crea una serie circolare di copie dell\'oggetto selezionato, partendo da un centro e andando radialmente verso l\'esterno. Si possono anche creare copie [App Link](App_Link/it.md). {{Version/it|0.19}}
    -   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Serie su tracciato](Draft_PathArray/it.md): crea una serie di copie dell\'oggetto selezionato distribuite su un percorso.
    -   <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Serie di link su tracciato](Draft_PathLinkArray/it.md): come [Serie su tracciato](Draft_PathArray/it.md), ma crea degli elementi [App::Link](Std_LinkMake/it.md) invece di normali copie. {{Version/it|0.19}}
    -   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Serie su punti](Draft_PointArray/it.md): crea una serie di oggetti posizionando le copie in determinati punti. {{version/it|0.18}}
    -   <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Serie di link su punti](Draft_PointLinkArray/it.md): come [Serie su punti](Draft_PointArray/it.md), ma crea degli elementi [App::Link](Std_LinkMake/it.md) invece di normali copie. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Modifica](Draft_Edit/it.md): consente di modificare un oggetto selezionato.
-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Evidenzia i sottoelementi](Draft_SubelementHighlight/it.md): entra in una modalità di modifica che consente di modificare oggetti diversi. {{Version/it|0.19}}

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Congiungi](Draft_Join/it.md): unisce le linee insieme in un unico contorno. {{version/it|0.18}}
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Separa](Draft_Split/it.md): divide un contorno in due in un punto. {{version/it|0.18}}
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Promuovi](Draft_Upgrade/it.md): unisce gli oggetti in un oggetto di livello superiore.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Declassa](Draft_Downgrade/it.md): scompone gli oggetti in oggetti di livello inferiore.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Da polilinea a BSpline](Draft_WireToBSpline/it.md): converte i segmenti di una polilinea (Wire) in curve di una linea B-Spline e viceversa.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Da Draft a Schizzo](Draft_Draft2Sketch/it.md): converte un oggetto di Draft in un oggetto di [Schizzo](Sketcher_Workbench/it.md) e viceversa.
-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Pendenza](Draft_Slope/it.md): cambia l\'inclinazione di una [Linea](Draft_Line/it.md) o di una [Polilinea](Draft_Wire/it.md) attualmente selezionata. {{Version/it|0.17}}
-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Inverti la direzione delle quote](Draft_FlipDimension/it.md): inverte l\'orientamento del testo di una [Quota](Draft_Dimension/it.md).

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Vista 2D](Draft_Shape2DView/it.md): crea un oggetto 2D quale proiezione di un oggetto 3D.

## Barra degli strumenti del vassoio di Draft 

La barra degli strumenti del vassoio di Draft viene visualizzata all\'avvio dell\'ambiiente e consente di selezionare il piano di lavoro, insieme ad alcune proprietà visive come il colore della linea, il colore della forma, la dimensione del testo, la larghezza della linea e il gruppo automatico.

![](images/Draft_tray_default.png )

Its tools are also available in the **Draft → Utilities** menu:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Piano di lavoro](Draft_SelectPlane/it.md): consente di impostare un piano di lavoro da una vista standard o da una faccia selezionata..
-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Modalità costruzione](Draft_ToggleConstructionMode/it.md): attiva o disattiva la modalità costruzione.
-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Imposta Stile](Draft_Apply/it.md): imposta lo stile di default per i nuovi oggetti e applica lo stile e il colore correnti agli oggetti selezionati.
-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [ AutoGruppo](Draft_AutoGroup/it.md): posiziona automaticamente i nuovi oggetti in un determinato <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Gruppo](Std_Group/it.md), <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Strato di Draft](Draft_Layer/it.md), o uno degli oggetti di [Arch](Arch_Workbench/it.md) simili ai gruppi come <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Parte di edificio](Arch_BuildingPart/it.md). {{Version/it|0.17}}

-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Set style](Draft_SetStyle.md): sets the default style for new objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off.

-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget 

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget 

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Barra degli strumenti di aggancio 

La barra degli strumenti di [Aggancio](Draft_Snap/it.md) consente di selezionare la modalità di aggancio corrente. Il suo pulsante rimane premuto quando una modalità è attiva.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Cambiar aggancio](Draft_Snap_Lock/it.md): attiva o disattiva [gli oggetti di aggancio](Draft_Snap/it.md) in modo globale.
-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Punto finale](Draft_Snap_Endpoint/it.md): esegue uno snap ai punti finali dei segmenti di linea, arco e spline.
-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Punto medio](Draft_Snap_Midpoint/it.md): esegue uno snap al punto centrale dei segmenti di linea e arco.
-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Centro](Draft_Snap_Center/it.md): si aggancia al punto centrale di cerchi, archi e facce,

[Piano lavoro proxies](Draft_SetWorkingPlaneProxy/it.md) e [Parte di un fabbricato](Arch_BuildingPart/it.md)

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Angolo](Draft_Snap_Angle/it.md): aggancia gli speciali punti cardinali di cerchi e archi, a 45° e 90°.
-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Intersezione](Draft_Snap_Intersection/it.md): esegue uno snap all\'intersezione di due segmenti di linea o arco. Passare il mouse sui due oggetti desiderati per attivare gli snap all\'intersezione.
-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Perpendicolare](Draft_Snap_Perpendicular/it.md): a segmenti di linea e arco, si aggancia perpendicolarmente all\'ultimo punto.
-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Estensione](Draft_Snap_Extension/it.md): aggancia una linea immaginaria che si estende oltre i punti finali dei segmenti di linea. Passare il mouse sull\'oggetto desiderato per attivare lo snap all\'estensione.
-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Parallela](Draft_Snap_Parallel/it.md): aggancia una linea immaginaria parallela a un segmento di linea. Passare il mouse sull\'oggetto desiderato per attivare lo snap parallelo.
-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Speciale](Draft_Snap_Special/it.md): agancia punti speciali definiti dall\'oggetto. {{Version/it|0.17}}
-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Vicino](Draft_Snap_Near/it.md): aggancia il punto o il bordo più vicino dell\'oggetto più vicino.
-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Orto](Draft_Snap_Ortho/it.md): aggancia linee immaginarie che attraversano l\'ultimo punto e si estendono a 0°, 45° e 90°.
-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Griglia](Draft_Snap_Grid/it.md): esegue uno snap alle intersezioni delle linee della griglia, se la griglia è visibile.
-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Piano di lavoro](Draft_Snap_WorkingPlane/it.md): posiziona sempre il punto di aggancio sul corrente [piano di lavoro](Draft_SelectPlane/it.md), anche se si aggancia un punto esterno al piano di lavoro.
-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Dimensione](Draft_Snap_Dimensions/it.md): mostra le dimensioni X e Y temporanee durante lo snap.
-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Attiva/disattiva la griglia](Draft_Snap_Grid/it.md): attiva o disattiva la visibilità della griglia.

## Strumenti di utilità 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Strato](Draft_Layer/it.md): crea uno strato nel documento corrente, a cui è possibile aggiungere oggetti per controllare la visibilità e il colore degli oggetti. Sostituisce [VisGruppo](Draft_VisGroup/it.md). {{Version/it|0.19}}
-   <img alt="" src=images/Draft_SetWorkingPlaneProxy.svg  style="width:32px;"> [Piano Proxy](Draft_SetWorkingPlaneProxy/it.md): aggiunge un oggetto proxy nel documento per memorizzare la posizione del [Piano di lavoro](Draft_SelectPlane/it.md) corrente. {{Version/it|0.17}}
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Cambia la visualizzazione](Draft_ToggleDisplayMode/it.md): commuta la modalità di visualizzazione degli oggetti selezionati da \"Flat lines\" a \"Wireframe\" (da facce a linee).
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Aggiungi al gruppo](Draft_AddToGroup/it.md): aggiunge rapidamente gli oggetti selezionati a un [Gruppo](Std_Group/it.md) o ad un [VisGruppo](Draft_VisGroup/it.md).
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Seleziona il contenuto del gruppo](Draft_SelectGroup/it.md): seleziona il contenuto di un [Gruppo](Std_Group/it.md) o di un [VisGruppo](Draft_VisGroup/it.md) esistente.
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Aggiungi al gruppo Costruzione](Draft_AddConstruction/it.md): aggiunge l\'oggetto selezionato al gruppo Costruzione. {{Version/it|0.17}}
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Ripara](Draft_Heal/it.md): risolve i problemi individuati negli oggetti di Draft in file molto vecchi.

## Menu di utilità 

Strumenti aggiuntivi disponibili dal menu **Draft → Utilità** o tramite il menu di scelta rapida visualizzato facendo clic con il pulsante destro del mouse, a seconda dell\'oggetto selezionato.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Modalità Continua](Draft_ToggleContinueMode/it.md): attiva o disattiva la modalità \"Continua con lo stesso strumento\".
-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Barra di snap](Draft_ShowSnapBar/it.md): mostra o nasconde la barra degli strumenti di [ancoraggio](Draft_Snap/it.md) di Draft.

## Ulteriori funzioni 

-   [Digitare le coordinate](Draft_Coordinates/it.md): permette di inserire le coordinate invece di fare clic sulla vista 3D per definire un nuovo punto.
-   [Vincolare](Draft_Constrain/it.md): limita il puntatore nei movimenti orizzontali o verticali rispetto a un punto precedente.
-   [Ancorare (Snap)](Draft_Snap/it.md): posiziona nuovi punti su posti speciali su oggetti esistenti o sulla griglia.
-   [Modalità copia](Draft_Copying/it.md): Tutti gli strumenti di modifica possono modificare gli oggetti selezionati o crearne una copia modificata. Tenendo premuto **Alt** durante la modifica dell\'oggetto, ad es. spostato o ruotato, crea una copia quando si rilascia il tasto.
-   [Modalità costruzione](Draft_ToggleConstructionMode/it.md): Permette di creare geometrie separate dalle altre semplicemente attivandola o disattivandola.
-   [Piano di lavoro](Draft_SelectPlane/it.md): consente di selezionare una superficie nello spazio 3D su cui lavorare.

## Tree view context menu 

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Selection options 

If there is a selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Wire options 

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options 

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Merge layer duplicates: this option currently does not work.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer.md): adds a new layer to the current document.

### Layer options 

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): makes the selected layer the active layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the camera settings stored in the working plane proxy.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the visibility state of objects stored in the working plane proxy.

## 3D view context menu 

The following additional options are available in the [3D view](3D_view.md) context menu:

### No-selection options 

If there is no selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Selection options 

If there is a selection the context menu contains two additional sub-menus:

-    **Draft**: tools for [drawing objects](#Drawing_objects.md) and [modifying objects](#Modifying_objects.md).

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Obsoleti

Questi strumenti sono stati rimossi dall\'interfaccia in v0.19 perché non avevano più alcuno scopo.

-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> [VisGruppo](Draft_VisGroup/it.md): crea nel documento corrente un gruppo di elementi con le stesse proprietà Vista. {{Obsolete/it|0.19}}
-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Termina la linea](Draft_FinishLine/it.md): termina il disegno della corrente [polilinea](Draft_Wire/it.md) o [BSpline](Draft_BSpline/it.md), senza chiuderla. {{Obsolete/it|0.19}}
-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Chiudi la linea](Draft_CloseLine/it.md): termina il disegno della corrente [polilinea](Draft_Wire/it.md) o [BSpline](Draft_BSpline/it.md), e la chiude. {{Obsolete/it|0.19}}
-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Annulla la linea](Draft_UndoLine/it.md): annulla l\'ultimo segmento di una [polilinea](Draft_Wire/it.md). {{Obsolete/it|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

## Preferenze

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Preferenze](Draft_Preferences/it.md): preferenze generali per il piano di lavoro e gli strumenti di disegno.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferenze Import-Export](Import_Export_Preferences/it.md): preferenze disponibili per l\'importazione e l\'esportazione in diversi formati di file.

## Formato dei file 

Queste sono le funzioni per l\'apertura, l\'importazione o l\'esportazione di altri formati di file. Il comando Apri apre un nuovo documento con i contenuti del file, mentre Importa aggiunge i contenuti del file al documento corrente. Esporta salva gli oggetti selezionati in un file. Se non viene selezionato nulla, vengono esportati tutti gli oggetti. Ricordare che lo scopo di Draft è di lavorare con oggetti 2D, quindi le procedure di importazione si concentrano solo su oggetti 2D e sebbene i formati DXF e OCA supportino anche le definizioni di oggetti nello spazio 3D (gli oggetti non sono necessariamente piatti), non importa oggetti volumetrici come mesh, superfici 3D, ecc., ma solo linee, cerchi, testi o forme piatte. I formati di file attualmente supportati sono:

-   [Autodesk .DXF](Draft_DXF/it.md): importa ed esporta file [Drawing Exchange Format](http://en.wikipedia.org/wiki/AutoCAD_DXF) creati con applicazioni CAD 2D. Vedere anche la pagina [Importare i file DXF in FreeCAD](FreeCAD_and_DXF_Import/it.md).
-   [Autodesk .DWG](Draft_DXF/it.md): importa ed esporta i file DWG tramite l\'importatore DXF, quando viene installata l\'utility [ODA Converter](Extra_python_modules/it#ODA_Converter_(già_Teigha_Converter).md). Vedere anche la pagina [Importare i file DWG in FreeCAD](FreeCAD_and_DWG_Import/it.md).
-   [SVG](Draft_SVG/it.md): importa ed esporta i file [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) creato con applicazioni di disegno vettoriale.
-   [Open Cad format .OCA](Draft_OCA/it.md): importa ed esporta file OCA/GCAD, potenzialmente un nuovo [formato di file open CAD](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT/it.md): importa file DAT che descrivono [profili aerodinamici](http://www.ae.illinois.edu/m-selig/ads/coord_database.html) portanti.

### Installa importatori 

-   [FreeCAD and DWG Import](FreeCAD_and_DWG_Import/it.md): Importazioni ed esportazioni di DWG files
-   [FreeCAD and DXF Import](FreeCAD_and_DXF_Import/it.md): Importazioni ed esportazioni di DXF files

## Test unitari 


**Vedere anche:**

[Ambiente Test](Test_Workbench/it.md).

Per eseguire i test unitari dell\'ambiente, eseguire quanto segue dal terminale del sistema operativo. 
```python
freecad -t TestDraft
```

## Script

Gli strumenti di Draft possono essere utilizzati nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando le [API Draft](Draft_API/it.md).

L\'ambiente include un modulo per creare dei campioni di tutti gli oggetti in un nuovo documento. {{Version/it|0.19}}

Utilizzare questo per verificare che tutti gli oggetti siano prodotti correttamente. 
```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Ispezionare il codice di questo modulo è utile per capire come utilizzare l\'interfaccia di programmazione. 
```python
$INSTALLDIR/Mod/Draft/drafttests/draft_test_objects.py
```

Dove `$INSTALLDIR` è la directory di livello superiore in cui è stato installato il software; per esempio, in Linux potrebbe essere `/usr/share/freecad`.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Oggetti test per l'ambiente [Draft](Draft_Workbench/it.md).*

## Tutorial

-   [Draft tutorial](Draft_tutorial/it.md)
-   [Draft tutorial obsoleto](Draft_tutorial_Outdated/it.md)
-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial/it.md)





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
