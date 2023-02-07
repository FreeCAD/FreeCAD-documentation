# <img alt="L\'icona di Draft" src=images/Workbench_Draft.svg  style="width:64px;"> Draft Workbench/it


{{TOCright}}



## Introduzione

L**\'Ambiente Draft** <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> si concentra principalmente sulla creazione e modifica di oggetti 2D in FreeCAD. Ma non è limitato al piano XY del sistema di coordinate globale. I suoi oggetti possono avere qualsiasi orientamento e posizione nello spazio 3D e alcuni oggetti Draft possono essere planari o non planari.

Gli oggetti Draft possono essere utilizzati per il disegno generale, in modo simile a quanto si può fare con Inkscape o AutoCAD. Ma possono anche costituire la base per la creazione di oggetti 3D in altri ambienti di lavoro. Una [Polilinea](Draft_Wire/it.md) può definire il percorso di un [Muro](Arch_Wall/it.md), un [Poligono](Draft_Polygon/it.md) può essere utilizzato per un [Estrusione](Part_Extrude/it.md), ecc. Molti degli [strumenti di Modifica](#Modificare.md) possono essere comunque applicati agli oggetti 2D e 3D creati con altri ambienti di lavoro. Ad esempio, puoi [spostare](Draft_Move/it.md) uno [Sketch](Sketcher_Workbench/it.md) o creare una [Serie ortogonale](Draft_OrthoArray/it.md) da un oggetto [Part](Part_Workbench/it.md).

L\'ambiente Draft fornisce anche strumenti per definire un [piano di lavoro](Draft_SelectPlane/it.md), una [griglia](Draft_Snap_Grid/it.md) e un [sistema di aggancio](Draft_Snap.md) per controllare con precisione la posizione della geometria.

Se il tuo obiettivo principale è la produzione di disegni 2D complessi e file [DXF](DXF/it.md) e non hai bisogno della modellazione 3D, FreeCAD potrebbe non essere la scelta giusta per te. Potresti invece prendere in considerazione un programma software dedicato per il disegno tecnico, come [LibreCAD](https://it.wikipedia.org/wiki/LibreCAD) o [QCad](https://it.wikipedia.org/wiki/QCad).

![](images/Draft_Workbench_Example.png ) 
*L'immagine mostra la [griglia](Draft_Snap_Grid/it.md) allineata con il piano XY.<br>
Alla sinistra, in bianco, alcuni oggetti piani.<br>
Alla destra una [Polilinea](Draft_Wire/it.md) usata come percorso per una [serie su tracciato](Draft_PathArray.md).*



## Disegnare

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linea](Draft_Line/it.md): crea una linea retta.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polilinea](Draft_Wire/it.md): crea una polilinea, una sequenza di diversi segmenti lineari connessi.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Raccordo](Draft_Fillet/it.md): crea un raccordo, un angolo arrotondato, o uno smusso, un angolo retto, tra due [Linee](Draft_Line/it.md). {{Version/it|0.19}}

-   <img alt="" src=images/Draft_Arc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Strumenti Arco:

  - <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arco](Draft_Arc/it.md): crea un arco circolare da un centro, un raggio, un angolo iniziale e un angolo di apertura.

  - <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arco per 3 punti](Draft_Arc_3Points/it.md): crea un arco circolare per tre punti che ne definiscono la circonferenza.

-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Cerchio](Draft_Circle/it.md): crea un cerchio da un centro e un raggio.

-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellisse](Draft_Ellipse/it.md): crea un\'ellisse da due punti definendo un rettangolo a cui l\'ellisse si adatterà.

-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rettangolo](Draft_Rectangle/it.md): crea un rettangolo da due punti.

-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Poligono](Draft_Polygon/it.md): crea un poligono regolare da un centro e un raggio.

-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-spline](Draft_BSpline/it.md): crea una curva B-spline da più punti.

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Strumento Bézier:

  - <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Curva Cubica di Bézier](Draft_CubicBezCurve/it.md): crea una curva di Bézier di terzo grado.

  - <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Curva di Bézier](Draft_BezCurve/it.md): crea una curva di Bézier da più punti.

-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punto](Draft_Point/it.md): crea un punto semplice.

-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Facce legate](Draft_Facebinder/it.md): crea un oggetto superficie dalle facce selezionate.

-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Forma da testo](Draft_ShapeString/it.md): crea una forma composta che rappresenta una stringa di testo.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Tratteggio](Draft_Hatch/it.md): crea tratteggi sulle facce piane di un oggetto selezionato. {{Version/it|0.20}}



## Annotazioni

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Testo](Draft_Text/it.md): crea un testo su più righe in un determinato punto.

-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimensione](Draft_Dimension/it.md): crea una quota lineare, una quota radiale o una quota angolare.

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Etichetta](Draft_Label/it.md): crea un testo su più righe con una linea guida a 2 segmenti e una freccia.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Stili di Annotazione\...](Draft_AnnotationStyleEditor/it.md): consente di definire stili che influiscono sulle proprietà visive di oggetti simili ad annotazioni.



## Modificare

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Sposta](Draft_Move/it.md): sposta o copia gli oggetti selezionati da un punto all\'altro.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Ruota](Draft_Rotate/it.md): ruota o copia gli oggetti selezionati attorno a un punto centrale di un determinato angolo.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scala](Draft_Scale/it.md): ridimensiona o copia gli oggetti selezionati attorno a un punto base.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Specchio](Draft_Mirror/it.md): crea copie specchiate da oggetti selezionati.

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Offset](Draft_Offset/it.md): sposta ogni segmento di un oggetto selezionato ad una determinata distanza o crea una copia traslata dell\'oggetto selezionato.

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Taglia/Estendi](Draft_Trimex/it.md): taglia o estende un oggetto selezionato.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stira](Draft_Stretch/it.md): allunga gli oggetti spostando i punti selezionati.

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clona](Draft_Clone/it.md): crea copie collegate, cloni, ​​di oggetti selezionati.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Strumenti Array:

  - <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Serie](Draft_OrthoArray/it.md): crea una serie ortogonale da un oggetto selezionato. Può opzionalmente creare una serie di [Link](App_Link.md).

  - <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Serie polare](Draft_PolarArray/it.md): crea una serie da un oggetto selezionato, posizionando copie lungo una circonferenza. Facoltativamente, può creare una serie di [Link](App_Link/it.md).

  - <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Serie circolare](Draft_CircularArray/it.md): crea una serie da un oggetto selezionato, posizionando copie lungo circonferenze concentriche. Facoltativamente, può creare un serie di [Link](App_Link.md).

  - <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Serie su tracciato](Draft_PathArray/it.md): crea una matrice da un oggetto selezionato posizionando le copie lungo un tracciato.

  - <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Serie di link su tracciato](Draft_PathLinkArray/it.md): idem, ma crea una serie di [Link](App_Link.md) invece di una serie normale.

  - <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Serie di punti](Draft_PointArray/it.md): crea una serie da un oggetto selezionato posizionando copie nei punti da un assieme di punti.

  - <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Serie di link su punti](Draft_PointLinkArray/it.md): idem, ma crea una serie di [Link](App_Link.md) invece di una serie normale.

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Modifica](Draft_Edit/it.md): mette gli oggetti selezionati in modalità Modifica bozza. In questa modalità le proprietà degli oggetti possono essere modificate graficamente.

-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Evidenzia sottoelemento](Draft_SubelementHighlight/it.md): evidenzia temporaneamente gli oggetti selezionati o gli oggetti base degli oggetti selezionati.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Congiungi](Draft_Join/it.md): unisce [Linee](Draft_Line/it.md) e [Polilinee](Draft_Wire/it.md) in un unico contorno.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Dividi](Draft_Split/it.md): divide una [Linea](Draft_Line/it.md) o una [Polilinea](Draft_Wire/it.md) in un punto o bordo specificato.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Promuovi](Draft_Upgrade/it.md): promuove gli oggetti selezionati.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Semplifica](Draft_Downgrade/it.md): semplifica gli oggetti selezionati.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Da Polilinea a B-spline](Draft_WireToBSpline/it.md): converte [Polilinee](Draft_Wire/it.md) in [BSplines](Draft_BSpline/it.md) e viceversa.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Bozza in Schizzo](Draft_Draft2Sketch/it.md): converte una [Bozza](Draft_Workbench/it.md) in [Schizzo](Sketcher_NewSketch/it.md) e vice versa.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Imposta la pendenza](Draft_Slope/it.md): imposta la pendenza delle [Linee](Draft_Line/it.md) o [Polilinee](Draft_Wire.md) selezionate aumentando o diminuendo la coordinata Z di tutti i punti dopo il primo.

-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Capovolgi quota](Draft_FlipDimension/it.md): ruota il testo della quota della [Dimensione](Draft_Dimension/it.md) selezionata di 180° attorno alla linea di quota.

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Vista forma 2D](Draft_Shape2DView/it.md): crea proiezioni 2D da oggetti selezionati.



## Barra di Draft 

La [Barra di draft](Draft_Tray/it.md) consente di selezionare il piano di lavoro, definire le impostazioni di stile, attivare/disattivare la modalità di costruzione e specificare il livello o il gruppo attivo.

![](images/Draft_tray_default.png )

-   ![](images/Draft_tray_button_plane.png ) [Piano di lavoro](Draft_SelectPlane/it.md): seleziona il piano di lavoro Draft corrente. Disponibile anche nel menu: **Draft → Utilità → <img src="images/Draft_SelectPlane.svg" width=16px> Seleziona piano**.

-   ![](images/Draft_tray_button_style.png ) [Cambia lo stile](Draft_SetStyle/it.md): imposta lo stile predefinito per i nuovi oggetti. Disponibile anche nel menu: **Draft → Utilità → <img src="images/Draft_SetStyle.svg" width=16px> Imposta stile**.

-   ![](images/Draft_tray_button_construction.png ) [Attiva/Disattiva la modalità costruzione](Draft_ToggleConstructionMode/it.md): attiva o disattiva la modalità di costruzione Draft. Disponibile anche nel menu: **Draft → Utilità → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Attiva/Disattiva la modalità costruzione**.

-   ![](images/Draft_tray_button_layer.png ) [Disattiva auto gruppo](Draft_AutoGroup/it.md): cambia l\'oggetto attivo [Strato Draft](Draft_Layer/it.md) o, facoltativamente, l\'oggetto attivo [Gruppo](Std_Group/it.md) o l\'oggetto gruppo di [Arch](Arch_Workbench/it.md).



## Scala per gli strumenti di annotazione 

Con il [widget Scala per gli strumenti di annotazione](Draft_annotation_scale_widget/it.md) è possibile specificare la scala di annotazione di Draft.

![](images/Draft_annotation_scale_widget_button.png )



## Widget di aggancio in Draft 

Il [widget di aggancio in Draft](Draft_snap_widget/it.md) può essere utilizzato come alternativa alla [Barra degli strumenti di aggancio](#Barra_degli_strumenti_di_aggancio.md).

![](images/Draft_snap_widget_button.png )



## Barra degli strumenti di aggancio 

La barra degli strumenti Snap di Draft consente di selezionare le opzioni di snap attive. I pulsanti appartenenti alle opzioni attive rimangono premuti. Per informazioni generali sullo snap vedere: [Aggancio](Draft_Snap/it.md).

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Blocca Snap](Draft_Snap_Lock/it.md): abilita o disabilita lo snap a livello globale.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Punto Finale](Draft_Snap_Endpoint/it.md): aggancia alle estremità dei bordi.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Punto Centrale](Draft_Snap_Midpoint/it.md): si aggancia al punto medio dei bordi.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Snap Centro](Draft_Snap_Center/it.md): aggancia al punto centrale delle facce e dei bordi circolari e al punto di **Posizionamento** dei [Piani di lavoro Proxy di Draft](Draft_WorkingPlaneProxy/it.md) e [Parti di edificio di Arch](Arch_BuildingPart/it.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap Angolo](Draft_Snap_Angle/it.md): aggancia agli speciali punti cardinali sui bordi circolari a multipli di 30° e 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap Intersezione](Draft_Snap_Intersection/it.md): aggancia all\'intersezione di due bordi.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap Perpendicolare](Draft_Snap_Perpendicular/it.md): esegue lo snap ai punti perpendicolari sulle facce ({{Version/it|1.0}}) e sugli spigoli.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap Estensione](Draft_Snap_Extension/it.md): aggancia a una linea immaginaria che si estende oltre i punti finali dei bordi diritti.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap Parallelo](Draft_Snap_Parallel/it.md): aggancia a una linea immaginaria parallela ai bordi dritti.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap Speciale](Draft_Snap_Special/it.md): aggancia ai punti speciali definiti dall\'oggetto.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap Vicino](Draft_Snap_Near/it.md): aggancia al punto più vicino alle facce e agli spigoli.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap Ortogonale](Draft_Snap_Ortho/it.md): aggancia alle linee immaginarie che attraversano il punto precedente a multipli di 45°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap Griglia](Draft_Snap_Grid/it.md): aggancia alle intersezioni delle linee della griglia.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Snap Piano di Lavoro](Draft_Snap_WorkingPlane/it.md): proietta i punti di aggancio sul [piano di lavoro](Draft_SelectPlane/it.md) corrente.

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap Quotature](Draft_Snap_Dimensions/it.md): mostra le quote X e Y temporanee.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Attiva/Disattiva la griglia](Draft_ToggleGrid/it.md): attiva o disattiva la griglia.



## Strumenti di utilità di Draft 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Livello](Draft_Layer/it.md): crea un [livello](Draft_Layer/it.md).

-   <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:32px;"> [Aggiunge un nuovo gruppo con nome](Draft_AddNamedGroup/it.md): crea un [gruppo](Std_Group.md) con nome e sposta gli oggetti selezionati in quel gruppo. {{Version/it|0.20}}

-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Sposta nel gruppo](Draft_AddToGroup/it.md): sposta gli oggetti in un [gruppo](Std_Group/it.md). Può anche separare gli oggetti.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Seleziona gruppo](Draft_SelectGroup/it.md): seleziona il contenuto dei [gruppi](Std_Group/it.md) o degli oggetti simili a gruppi [Arch](Arch_Workbench/it.md).

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Aggiungi al gruppo Costruzione](Draft_AddConstruction/it.md): sposta gli oggetti nel [Gruppo di costruzione Draft](Draft_ToggleConstructionMode/it.md).

-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Attiva/Disattiva la visualizzazione normale/reticolo](Draft_ToggleDisplayMode/it.md): cambia la proprietà **Display Mode** degli oggetti selezionati tra {{Value|Linee Piatte}} e {{Value|Reticolo}}.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Crea piano di lavoro proxy](Draft_WorkingPlaneProxy/it.md): crea un proxy del piano di lavoro per salvare il [piano di lavoro](Draft_SelectPlane/it.md) attuale.



## Strumenti aggiuntivi 

Il menu **Draft → Utilità** contiene diversi strumenti. Alla maggior parte di essi è possibile accedere anche dalle barre degli strumenti o dalla [Barra Draft](Draft_Tray/it.md) e sono già stati menzionati sopra. Per i seguenti strumenti non è questo il caso:

-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Applica lo stile corrente](Draft_ApplyStyle/it.md): applica le impostazioni di stile correnti agli oggetti selezionati.

-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Ripara](Draft_Heal/it.md): ripara gli oggetti Draft problematici trovati in file molto vecchi.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Attiva/Disattiva la modalità continua](Draft_ToggleContinueMode/it.md): attiva o disattiva la modalità continua.

-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Mostra la Barra degli strumenti di aggancio](Draft_ShowSnapBar/it.md): mostra la [barra degli strumenti di aggancio](#Barra_degli_strumenti_di_aggancio.md).



## Ulteriori funzioni 

-   [Piano di lavoro](Draft_SelectPlane/it.md): il piano nella [vista 3D](3D_view/it.md) dove vengono creati i nuovi oggetti Draft.
-   [Snap](Draft_Snap/it.md): seleziona punti geometrici esatti o definiti da oggetti esistenti o dalla griglia.
-   [Vincolare](Draft_Constrain/it.md): per ogni punto successivo è possibile vincolare il movimento del cursore alla direzione X, Y o Z.
-   [Modalità costruzione](Draft_ToggleConstructionMode/it.md): posiziona i nuovi oggetti Draft in un gruppo dedicato rendendo più facile nasconderli o eliminarli.
-   [Campitura](Draft_Pattern/it.md): Gli oggetti Draft con una proprietà **Make Face** possono essere visualizzati con un modello SVG invece di un colore della faccia a tinta unita.



## Menu contestuale della vista ad albero 

Le seguenti opzioni aggiuntive sono disponibili nel menu contestuale [Vista ad albero](Tree_view/it.md):



### Opzioni di default 

Per la maggior parte degli oggetti Draft è disponibile la seguente opzione:

-   Modifica: modifica l\'oggetto. A seconda del tipo di oggetto, viene utilizzata [Draft Modifica](Draft_Edit/it.md) o una soluzione di modifica dedicata. {{Version/it|1.0}}

Se c\'è un documento attivo il menu contestuale contiene un ulteriore sottomenu:

-   Utilità: un sottoinsieme degli strumenti disponibili nel menu principale Utilità di Draft.



### Opzioni polilinea 

Per [Linea](Draft_Line/it.md) e [Polilinea](Draft_Wire/it.md) è disponibile questa opzione aggiuntiva:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Appiattisci: appiattisce la polilinea sul corrente [Piano di lavoro](Draft_SelectPlane/it.md). Questa opzione non funziona correttamente in {{VersionMinus|0.19}}.



### Opzioni del contenitore di livelli 

Per un [Contenitore di livelli](Draft_Layer/it.md) sono disponibili queste opzioni aggiuntive:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Unisci i livelli duplicati](Draft_Layer/it#Opzioni_del_contenitore_di_Livelli.md): unisce tutti i livelli con la stessa etichetta di base.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Aggiungi un nuovo livello](Draft_Layer/it#Contenitore_di_liveeli_di_Draft.md): aggiunge un nuovo livello al documento corrente.



### Opzioni dei livelli 

Per un [Livello di Draft](Draft_Layer/it.md) sono disponibili queste opzioni aggiuntive.

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Attiva questo livello](Draft_AutoGroup/it.md): attiva il livello selezionato.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Seleziona il contenuto del livello](Draft_SelectGroup/it.md): seleziona gli oggetti all\'interno del livello selezionato.



### Opzioni del piano di lavoro proxy 

Per un [Piano di lavoro proxy](Draft_WorkingPlaneProxy/it.md) queste opzioni aggiuntive sono disponibili:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Memorizza posizione telecamera](Draft_WorkingPlaneProxy/it#Menu_contestuale.md): aggiorna la proprietà **View Data** del piano di lavoro proxy con la [vista 3D](3D_view.md) corrente nelle impostazioni della fotocamera.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Memorizza lo stato degli oggetti](Draft_WorkingPlaneProxy/it#Menu_contestuale.md): aggiorna la proprietà **Mappa di visibilità** del piano di lavoro proxy con lo stato di visibilità corrente degli oggetti nel documento.



## Menu contestuale vista 3D 

Le seguenti opzioni aggiuntive sono disponibili nel menu contestuale della [Vista 3D](Vista_3D/it.md):



### Opzioni di default 

Se è presente un documento attivo, il menu contestuale contiene un ulteriore sottomenu:

-   Utilità: un sottoinsieme degli strumenti disponibili nel menu principale Utilità di Draft.



### Strumenti obsoleti 

Questi comandi sono obsoleti ma ancora disponibili:

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Serie](Draft_Array/it.md): crea una serie ortogonale da un oggetto selezionato. La serie creata può essere trasformata in una [serie polare](Draft_PolarArray/it.md) o in una [serie circolare](Draft_CircularArray/it.md) modificandone la proprietà **Tipo di array**. {{Obsolete|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Disegno](Draft_Drawing/it.md): inserisce le viste degli oggetti selezionati in una pagina [disegno tecnico](Drawing_Workbench/it.md).{{Obsolete|0.17}}



## Preferenze

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Preferenze](Draft_Preferences/it.md): preferenze generali per l\'ambiente Draft.

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferenze Import Export](Import_Export_Preferences/it.md): preferenze disponibili per l\'importazione e l\'esportazione in diversi formati di file.



## Formato dei file 

L\'ambiente Draft fornisce a FreeCAD importatori ed esportatori per diversi formati di file. Questi sono utilizzati dai comandi [Import](Std_Import/it.md) e [Export](Std_Export/it.md).

-   [Autodesk .DXF](Draft_DXF/it.md): importa ed esporta file [Drawing Exchange Format](http://it.wikipedia.org/wiki/AutoCAD_DXF). Vedere anche [Importare i file DXF in FreeCAD](FreeCAD_and_DXF_Import/it.md).
-   [Autodesk .DWG](Draft_DXF/it.md): importa ed esporta file DWG tramite un convertitore DWG esterno. Vedere anche [Importare i file DWG in FreeCAD](FreeCAD_and_DWG_Import/it.md).
-   [Scalable Vector Graphics .SVG](Draft_SVG/it.md): importa ed esporta file [Scalable Vector Graphics](http://it.wikipedia.org/wiki/Scalable_Vector_Graphics).
-   [Open Cad format .OCA](Draft_OCA/it.md): importa ed esporta file [OCA/GCAD](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT/it.md): importa i file DAT che descrivono i profili del profilo alare.



## Test unitari 

Vedere anche: [Ambiente Test](Testing/it.md).

Per eseguire i test unitari dell\'ambiente, eseguire quanto segue dal terminale del sistema operativo:


```python
freecad -t TestDraft
```



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

L\'ambiente include un modulo per creare dei campioni di tutti gli oggetti in un nuovo documento.

Utilizzare questo per verificare che tutti gli oggetti siano prodotti correttamente:


```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

L\'esame del codice di questo modulo può aiutare a comprendere l\'interfaccia di programmazione.



## Tutorial

-   [Tutorial di Draft](Draft_tutorial/it.md)
-   [Tutorial di Draft Forma da Testo](Draft_ShapeString_tutorial/it.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Draft](Category_Draft.md) > Draft Workbench/it
