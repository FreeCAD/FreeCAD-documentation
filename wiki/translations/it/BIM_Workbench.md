# BIM Workbench/it
**Nella v1.0 gli ambienti di lavoro BIM, Native-IFC e [Arch](Arch_Workbench/it.md) sono stati uniti nell'ambiente BIM integrato.<br>
Questa pagina è stata aggiornata per quella versione.**

<img alt="L\'icona dell\'Ambiente BIM" src=images/Workbench_BIM.svg  style="width:128px;">






## Introduzione

L\'<img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [Ambiente BIM](BIM_Workbench/it.md) fornisce un moderno flusso di lavoro [Building Information Modeling](https://en.wikipedia.org/wiki/Building_information_modeling) in FreeCAD, con oggetti completamente parametrici come come muri, travi, tetti, finestre, scale, tubi e mobili. Supporta file [Industry Foundation Classes](Arch_IFC/it.md) (IFC) e la produzione di disegni progettuali 2D in combinazione con <img alt="" src=images/Workbench_TechDraw.svg  style="width:16px;"> l\'[Ambiente TechDraw](TechDraw_Workbench/it.md).

L\'ambiente BIM importa strumenti da <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft](Draft_Workbench/it.md), poiché utilizza i suoi oggetti 2D per costruire oggetti parametrici 3D. Ma può anche utilizzare forme solide create con altri ambienti di lavoro come <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench/it.md) e <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/it.md).

Vedere [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide) per una rapida panoramica se si è già utente di un\'altra applicazione BIM.

Gli sviluppatori di Draft e BIM collaborano anche con la più ampia [comunità OSArch](https://osarch.org), con l\'obiettivo finale di migliorare la progettazione degli edifici utilizzando software completamente gratuito.

<img alt="" src=images/BIM_workbench_presentation.png  style="width:800px;">



## Per iniziare 

<img alt="" src=images/BIM_welcome_screen.png  style="width:800px;">

Al primo avvio di BIM viene visualizzata una finestra di benvenuto, che fornisce una rapida panoramica di come funziona questo ambiente e consente all\'utente di avviare un [divertente tutorial di BIM](BIM_ingame_tutorial/it.md). La finestra di benvenuto è disponibile anche dal menu **Aiuto**. Quando la schermata di benvenuto viene chiusa facendo clic su OK, viene visualizzata la [finestra di dialogo di configurazione BIM](BIM_Setup/it.md), che consente all\'utente di impostare rapidamente alcune delle più comuni preferenze relative al BIM di FreeCAD senza la necessità di sfogliare tutte le pagine delle [Preferenze di FreeCAD](Preferences_Editor/it.md).

Lo strumento [Configurazione del progetto BIM](BIM_Setup/it.md) consente di configurare rapidamente un progetto BIM inserendo alcune informazioni di base sul progetto. È quindi possibile, ad esempio, utilizzare i diversi strumenti di disegno 2D per tracciare linee guida e linee di base, quindi utilizzare i diversi strumenti di modellazione 3D per creare automaticamente gli oggetti BIM 3D. Una linea, ad esempio, può diventare un muro semplicemente selezionandola e premendo il pulsante [Muro](Arch_Wall/it.md).

Elementi di costruzione comuni come [muri](Arch_Wall/it.md) o [colonne](BIM_Column/it.md) possono essere facilmente creati premendo il pulsante appropriato della barra degli strumenti e facendo clic sui punti nella vista 3D. Possono essere spostati, ruotati e modificati una volta creati. La maggior parte degli elementi BIM vengono creati sul [piano di lavoro](Draft_SelectPlane/it.md) corrente, quindi un flusso di lavoro tipico prevede prima il posizionamento del piano di lavoro, quindi la creazione di un elemento BIM. È possibile creare elementi più complessi disegnando prima gli elementi 2D, quindi utilizzando uno degli strumenti BIM per convertirli nell\'elemento desiderato.

Gli elementi che costituiscono il progetto possono essere organizzati utilizzando [siti](Arch_Site/it.md), [edifici](Arch_Building.md) e [livelli](Arch_BuildingPart.md), per riprodurre ciò che viene comunemente fatto in altre applicazioni BIM. In FreeCAD, tuttavia, tali strutture non sono obbligatorie e si è liberi di organizzare gli elementi del proprio modello come si ritiene opportuno, ad esempio utilizzando [gruppi](Std_Group/it.md).

I disegni 2D possono essere generati da un modello per rappresentare viste in pianta, sezione o prospetto. Per generare questi disegni, nel modello vengono posizionati dei [piani di sezione](Arch_SectionPlane/it.md), per indicare da dove deve essere tagliato o visto il modello. Una volta posizionati i piani di sezione, sono possibili due metodi:

1.  Creare viste proiettate nel documento utilizzando [shape views](Draft_Shape2DView/it.md), quindi aggiungere tutte le annotazioni necessarie come testi e quote e poi inserire tutto questo in una pagina. Questo è il metodo consigliato perché offre maggiore flessibilità.
2.  Creare una vista su una pagina direttamente dal piano di sezione. Quindi tutte le annotazioni 2D necessarie devono essere aggiunte al piano di sezione o eseguite direttamente sulla pagina. Questo è meno flessibile.

Infine, è possibile creare computi delle quantità utilizzando lo strumento [schedule](Arch_Schedule/it.md).

Se si è abituati a lavorare con un\'altra applicazione BIM, controllare la nostra [Tabella di compatibilità dell\'applicazione BIM](BIM_application_compatibility_table/it.md) per orientarsi quando si inizia a lavorare con FreeCAD.

<img alt="" src=images/BIM_tutorial_screenshot.png  style="width:800px;">

Il [tutorial divertente di BIM](BIM_ingame_tutorial/it.md) è un modo semplice per iniziare rapidamente a usare l\'ambiente BIM.



## Strumenti

L\'ambiente BIM raccoglie strumenti da diversi altri ambienti di FreeCAD, principalmente [Draft](Draft_Workbench/it.md) e [Part](Part_Workbench/it.md), approssimativamente riorganizzati in categorie logiche.

Inoltre, se tali [addon](External_workbench/it.md) sono installati, gli strumenti da [Reinforcement](Reinforcement_Workbench/it.md) (strumenti aggiuntivi per barre d\'armatura), [Fasteners](Fasteners_Workbench/it.md) (bulloni e viti), [Flamingo/Dodo ](Flamingo_Workbench/it.md) (strumenti per strutture metalliche e tubazioni) e [Parts Library](Parts_Library_Workbench/it.md) vengono automaticamente inclusi nell\'ambiente BIM.

L\'ambiente BIM aggiunge anche una serie di elementi nella **barra di stato** di FreeCAD e un paio di **voci nel menu contestuale**, accessibili facendo clic con il tasto destro nella vista 3D o nella vista ad albero .



### Disegni 2D 

Gli oggetti 2D sono comunemente usati come strumenti di disegno o per disegnare linee di base e profili per costruire oggetti BIM. Possono anche essere utilizzati per disegnare simboli e annotazioni nel modello. Oltre agli schizzi, che utilizzano il proprio sistema di coordinate, gli oggetti 2D verranno disegnati sul corrente [piano di lavoro](Draft_SelectPlane/it.md).

-   <img alt="" src=images/BIM_Sketch.svg  style="width:32px;"> [Schizzo](BIM_Sketch/it.md): crea un nuovo schizzo e accede alla modalità di modifica dello schizzo. Gli schizzi sono oggetti 2D avanzati con supporto di vincoli.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linea](Draft_Line/it.md): crea una linea retta.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polilinea](Draft_Wire/it.md): crea una polilinea (chiamata anche wire), una sequenza di diversi segmenti lineari connessi.

-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Cerchio](Draft_Circle/it.md): crea un cerchio da un centro e un raggio.

-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arco](Draft_Arc/it.md): crea un arco circolare da un centro, un raggio, un angolo iniziale e un angolo di apertura.

-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arco per 3 punti](Draft_Arc_3Points/it.md): crea un arco circolare per tre punti che ne definiscono la circonferenza.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Raccordo](Draft_Fillet/it.md): crea un raccordo, un angolo arrotondato, o uno smusso, un angolo retto, tra due [Draft Linee](Draft_Line/it.md).

-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellisse](Draft_Ellipse/it.md): crea un\'ellisse da due punti definendo un rettangolo a cui l\'ellisse si adatterà.

-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Poligono](Draft_Polygon/it.md): crea un poligono regolare da un centro e un raggio.

-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rettangolo](Draft_Rectangle/it.md): crea un rettangolo da due punti.

-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-spline](Draft_BSpline/it.md): crea una curva B-spline da più punti.

-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Curva di Bézier](Draft_BezCurve/it.md): crea una curva di Bézier da più punti.

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Curva Cubica di Bézier](Draft_CubicBezCurve/it.md): crea una curva di Bézier di terzo grado.

-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punto](Draft_Point/it.md): crea un punto semplice.

### 3D/BIM

Gli oggetti 3D e BIM sono gli elementi del mondo reale che compongono il progetto BIM.

-   <img alt="" src=images/BIM_Project.svg  style="width:32px;"> [Progetto](BIM_Project/it.md): Crea un progetto IFC includendo gli oggetti selezionati.

-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Sito](Arch_Site/it.md): Crea un sito che include oggetti selezionati.

-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Edificio](Arch_Building/it.md): Crea un edificio che include gli oggetti selezionati.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Piano](Arch_Floor/it.md): Crea un piano che include gli oggetti selezionati.

-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Spazio](Arch_Space/it.md): Crea un oggetto spazio.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Muro](Arch_Wall/it.md): Crea un muro da zero o utilizzando un oggetto selezionato come base.

-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Facciata continua](Arch_CurtainWall/it.md): Crea una facciata continua da zero o utilizzando un oggetto selezionato come base.

-   <img alt="" src=images/BIM_Column.svg  style="width:32px;"> [Colonna](BIM_Column/it.md): crea un elemento verticale [strutturale](Arch_Structure/it.md) in un dato punto, facoltativamente utilizzando un oggetto selezionato come profilo.

-   <img alt="" src=images/BIM_Beam.svg  style="width:32px;"> [Trave](BIM_Beam/it.md): Crea un elemento [strutturale](Arch_Structure/it.md) orizzontale tra due punti, opzionalmente utilizzando un oggetto selezionato come profilo.

-   <img alt="" src=images/BIM_Slab.svg  style="width:32px;"> [Soletta](BIM_Slab/it.md): crea un elemento piatto [strutturale](Arch_Structure/it.md) estrudendo un oggetto piatto selezionato.

-   <img alt="" src=images/BIM_Door.svg  style="width:32px;"> [Porta](BIM_Door/it.md): crea un oggetto [Finestra](Arch_Window/it.md) utilizzando le preimpostazioni della porta.

-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Finestra](Arch_Window/it.md): Crea una finestra da zero o utilizzando un oggetto selezionato come base.

-   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Tubo](Arch_Pipe/it.md): Crea una tubo.

-   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Raccordo](Arch_PipeConnector/it.md): Crea un raccordo ad angolo o a T tra 2 o 3 tubi selezionati.

-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Scale](Arch_Stairs/it.md): Crea un oggetto scala.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Tetto](Arch_Roof/it.md): Crea un tetto inclinato da un filo selezionato.

-   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Pannelllo](Arch_Panel/it.md): Crea un oggetto pannello da un oggetto 2D selezionato.

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Telaio](Arch_Frame/it.md): Crea un oggetto di carpenteria da un layout selezionato.

-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Recinzione](Arch_Fence/it.md): Crea un oggetto recinzione da un palo e un percorso selezionati.

-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Travatura](Arch_Truss/it.md): Crea una travatura reticolare da una linea selezionata o da zero.

-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Arredo](Arch_Equipment/it.md): Crea un\'attrezzatura o un oggetto di arredo.

-   Reinforcement tools:

:   Questi strumenti, tranne il primo, sono disponibili solo se è stato installato l\'[Ambiente Reinforcement](Reinforcement_Workbench/it.md).

  - <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Armatura perzonalizzata](Arch_Rebar/it.md): Crea un\'armatura personalizzata in un elemento strutturale selezionato utilizzando uno schizzo.

  - <img alt="" src=images/Reinforcement_StraightRebar.svg  style="width:32px;"> [Straight Rebar](Reinforcement_StraightRebar.md): Creates a straight reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_UShapeRebar.svg  style="width:32px;"> [U-Shape Rebar](Reinforcement_UShapeRebar.md): Creates a U-shape reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_LShapeRebar.svg  style="width:32px;"> [L-Shape Rebar](Reinforcement_LShapeRebar.md): Creates an L-shape reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_StirrupRebar.svg  style="width:32px;"> [Stirrup](Reinforcement_StirrupRebar.md): Creates a stirrup reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_BentShapeRebar.svg  style="width:32px;"> [Bent-Shape Rebar](Reinforcement_BentShapeRebar.md): Creates a bent-shape reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_HelicalRebar.svg  style="width:32px;"> [Helical Rebar](Reinforcement_HelicalRebar.md): Creates a helical reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_ColumnRebars.svg  style="width:32px;"> [Column Reinforcement](Reinforcement_ColumnRebars.md): Creates reinforcement bars in a selected column.

  - <img alt="" src=images/Reinforcement_BeamRebars.svg  style="width:32px;"> [Beam Reinforcement](Reinforcement_BeamRebars.md): Creates reinforcement bars in a selected beam.

  - <img alt="" src=images/Reinforcement_SlabRebars.svg  style="width:32px;"> [Slab Reinforcement](Reinforcement_SlabRebars.md): Creates reinforcement bars in a selected slab.

  - <img alt="" src=images/Reinforcement_FootingRebars.svg  style="width:32px;"> [Footing Reinforcement](Reinforcement_FootingRebars.md): Creates reinforcement bars in a selected footing.

-   Generic 3D tools:

:   Questi strumenti creano oggetti 3D generici che possono essere trasformati o utilizzati in componenti BIM.

  - <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profilo](Arch_Profile/it.md): Crea un profilo 2D parametrico.

  - <img alt="" src=images/BIM_Box.svg  style="width:32px;"> [Box](BIM_Box.md): Creates a box by specifying its dimensions graphically.

  - <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Shape builder\...](Part_Builder.md): Creates more complex shapes from various geometric primitives.

ː\* <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Lega facce](Draft_Facebinder/it.md): Crea un oggetto superficie dalle facce selezionate.

  - <img alt="" src=images/BIM_Library.svg  style="width:32px;"> [Objects library](BIM_Library.md): Inserts an equipment or furniture object. Requires the [Parts Library](Parts_Library.md) addon.

  - <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Component](Arch_Component.md): Creates a non-parametric Arch component.

  - <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [External reference](Arch_Reference.md): Links objects from another FreeCAD file into the current document.



### Annotazioni

Le annotazioni sono oggetti di aiuto visivo che possono essere inseriti all\'interno del modello. Possono essere utilizzati per esportare il modello direttamente in un formato 2D come [DXF](Draft_DXF/it.md), o riutilizzati durante la creazione di viste 2D del modello con [TechDraw](TechDraw_Workbench/it.md).

-   <img alt="" src=images/BIM_Text.svg  style="width:32px;"> [Text](BIM_Text.md): Creates a 2D text in a document or on a TechDraw page.

-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Shape from text](Draft_ShapeString.md): Creates a compound shape that represents a text string.

-   <img alt="" src=images/BIM_DimensionAligned.svg  style="width:32px;"> [Aligned dimension](BIM_DimensionAligned.md): Creates a dimension aligned with two points or a selected edge.

-   <img alt="" src=images/BIM_DimensionHorizontal.svg  style="width:32px;"> [Horizontal dimension](BIM_DimensionHorizontal.md): Creates an horizontal dimension between two points or from a selected edge.

-   <img alt="" src=images/BIM_DimensionVertical.svg  style="width:32px;"> [Vertical dimension](BIM_DimensionVertical.md): Creates a vertical dimension between two points or from a selected edge.

-   <img alt="" src=images/BIM_Leader.svg  style="width:32px;"> [Leader](BIM_Leader.md): Creates a 2-segment polyline with an arrow at its end, to be used as a leader line in conjunction with a [Text](BIM_Text.md).

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): Creates a multi-line text with a 2-segment leader line and an arrow.

-   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Axis](Arch_Axis.md): Adds a 1-direction array of axes.

-   <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Axis System](Arch_AxisSystem.md): Adds an axis system composed of several axes.

-   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Grid](Arch_Grid.md): Adds a grid-like object.

-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Section Plane](Arch_SectionPlane.md): Adds a section plane object.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Tratteggio](Draft_Hatch/it.md): Crea tratteggi sulle facce piane di un oggetto selezionato.

-   <img alt="" src=images/BIM_TDPage.svg  style="width:32px;"> [Page](BIM_TDPage.md): Creates a [TechDraw page](TechDraw_PageTemplate.md) from a template SVG file.

-   <img alt="" src=images/BIM_TDView.svg  style="width:32px;"> [View](BIM_TDView.md): Creates a view of the selected object(s) such as a [Section plane](Arch_SectionPlane.md) or a Group containing the different elements of a 2D view.

-   <img alt="" src=images/BIM_Shape2DView.svg  style="width:32px;"> [Shape-based view](BIM_Shape2DView.md): Creates a 2D projected view from a selected object such as a [Section plane](Arch_SectionPlane.md) or a [Level](Arch_BuildingPart.md).

### Snapping

This menu contains the [Draft Snap](Draft_Snap.md) tools as well as the following tools:

-   <img alt="" src=images/BIM_SetWPTop.svg  style="width:32px;"> [Working Plane Top](BIM_SetWPTop.md): Places the working plane on the global XY plane (ground).

-   <img alt="" src=images/BIM_SetWPFront.svg  style="width:32px;"> [Working Plane Front](BIM_SetWPFront.md): Places the working plane on the global XZ plane (front).

-   <img alt="" src=images/BIM_SetWPSide.svg  style="width:32px;"> [Working Plane Side](BIM_SetWPSide.md): Places the working plane on the global YZ plane (side).



### Modifica

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Sposta](Draft_Move/it.md): Sposta o copia gli oggetti selezionati da un punto all\'altro.

-   <img alt="" src=images/BIM_Copy.svg  style="width:32px;"> [Copy](BIM_Copy.md): Copies selected objects from one point to another.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Rotate](Draft_Rotate.md): Rotates or copies selected objects around a center point by a given angle.

-   <img alt="" src=images/BIM_Clone.svg  style="width:32px;"> [Clone](BIM_Clone.md): Clones selected objects.

-   <img alt="" src=images/BIM_SimpleCopy.svg  style="width:32px;"> [Create simple copy](BIM_SimpleCopy.md): Creates a non-parametric copy of a selected object. This is the same tool as [Part SimpleCopy](Part_SimpleCopy.md).

-   <img alt="" src=images/BIM_Compound.svg  style="width:32px;"> [Make compound](BIM_Compound.md): Creates a compound from selected objects. This is the same tool as [Part Compound](Part_Compound.md).

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Offset](Draft_Offset/it.md): Sposta ogni segmento di un oggetto selezionato ad una determinata distanza o crea una copia traslata dell\'oggetto selezionato.

-   <img alt="" src=images/BIM_Offset2D.svg  style="width:32px;"> [2D Offset\...](BIM_Offset2D.md): Constructs a parallel wire at a given distance from the original, or enlarges/shrinks a planar face (parametric version). This is the same tool as [Part Offset2D](Part_Offset2D.md).

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Taglia/Estendi](Draft_Trimex/it.md): Taglia o estende un oggetto selezionato.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Unisci](Draft_Join/it.md): Unisce [Linee](Draft_Line/it.md) e [Polilinee](Draft_Wire/it.md) in un unico contorno.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Dividi](Draft_Split/it.md): Divide una [Linea](Draft_Line/it.md) o una [Polilinea](Draft_Wire/it.md) in un punto o bordo specificato.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scala](Draft_Scale/it.md): Ridimensiona o copia gli oggetti selezionati attorno a un punto base.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stira](Draft_Stretch/it.md): Allunga gli oggetti spostando i punti selezionati.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft in sketch](Draft_Draft2Sketch/it.md): Converte oggetti Draft in [Schizzi](Sketcher_NewSketch/it.md) e vice versa.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Promuovi](Draft_Upgrade/it.md): Promuove gli oggetti selezionati.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Declassa](Draft_Downgrade/it.md): Declassa gli oggetti selezionati.

-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Aggiungi componente](Arch_Add/it.md): Aggiunge oggetti a un componente.

-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Rimuovi componente](Arch_Remove/it.md): Sottrae o rimuove oggetti da un componente.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Serie](Draft_OrthoArray/it.md): Crea una serie ortogonale da un oggetto selezionato. Può opzionalmente creare una serie di [Link](App_Link.md).

-   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Serie su tracciato](Draft_PathArray/it.md): Crea una matrice da un oggetto selezionato posizionando le copie lungo un tracciato.

-   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Serie polare](Draft_PolarArray/it.md): Crea una serie da un oggetto selezionato, posizionando copie lungo una circonferenza. Facoltativamente, può creare una serie di [Link](App_Link/it.md).

-   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Serie di punti](Draft_PointArray/it.md): Crea una serie da un oggetto selezionato posizionando copie nei punti da un assieme di punti.

-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Taglio con piano](Arch_CutPlane/it.md): Taglia un oggetto secondo un piano.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Specchio](Draft_Mirror/it.md): Crea copie specchiate da oggetti selezionati.

-   <img alt="" src=images/BIM_Extrude.svg  style="width:32px;"> [Extrude\...](BIM_Extrude.md): Extrudes planar faces of an object. This is the same tool as [Part Extrude](Part_Extrude.md).

-   <img alt="" src=images/BIM_Cut.svg  style="width:32px;"> [Difference](BIM_Cut.md): Subtracts one object from another. This is the same tool as [Part Cut](Part_Cut.md).

-   <img alt="" src=images/BIM_Fuse.svg  style="width:32px;"> [Union](BIM_Fuse.md): Fuses two objects. This is the same tool as [Part Fuse](Part_Fuse.md).

-   <img alt="" src=images/BIM_Common.svg  style="width:32px;"> [Intersection](BIM_Common.md): Extracts the common part of two objects. This is the same tool as [Part Common](Part_Common.md).



### Gestione

-   <img alt="" src=images/BIM_Setup.svg  style="width:32px;"> [BIM Setup\...](BIM_Setup.md): Configures some of the FreeCAD preferences most commonly used for BIM.

-   <img alt="" src=images/BIM_Views.svg  style="width:32px;"> [Views manager](BIM_Views.md): Manage the different views and levels of your project.

-   <img alt="" src=images/BIM_ProjectManager.svg  style="width:32px;"> [Manage project\...](BIM_ProjectManager.md): Allows to create some basic objects such as a [site](Arch_Site.md), a [building](Arch_Building.md) and [axes](Arch_Axis.md) by filling basic project information.

-   <img alt="" src=images/BIM_Windows.svg  style="width:32px;"> [Manage doors and windows\...](BIM_Windows.md): Manage the doors and windows of your project.

-   <img alt="" src=images/BIM_IfcElements.svg  style="width:32px;"> [Manage IFC elements\...](BIM_IfcElements.md): Manage how the different elements of your project will be exported to IFC.

-   <img alt="" src=images/BIM_IfcQuantities.svg  style="width:32px;"> [Manage IFC quantities\...](BIM_IfcQuantities.md): Manage how the quantities of your objects are explicitely exported to IFC

-   <img alt="" src=images/BIM_IfcProperties.svg  style="width:32px;"> [Manage IFC properties\...](BIM_IfcProperties.md): Manage the IFC properties attached to each of your objects.

-   <img alt="" src=images/BIM_Classification.svg  style="width:32px;"> [Manage classification\...](BIM_Classification.md): Manage how objects and materials of your project relate to classifications systems such as [Uniclass](https://en.wikipedia.org/wiki/Uniclass).

-   <img alt="" src=images/BIM_Layers.svg  style="width:32px;"> [Manage layers\...](BIM_Layers.md): Manage the layers of your document.

-   <img alt="" src=images/BIM_Material.svg  style="width:32px;"> [Material](BIM_Material.md): Manages [materials](Arch_SetMaterial.md) or [multimaterials](Arch_MultiMaterial.md) of selected objects

-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Schedule](Arch_Schedule.md): Creates different types of schedules.

-   <img alt="" src=images/BIM_Preflight.svg  style="width:32px;"> [Preflight checks\...](BIM_Preflight.md): Perform different checks on your model before exporting to IFC.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation styles\...](Draft_AnnotationStyleEditor.md): Allows you to define styles that affect the visual properties of annotation-like objects.

### Utils

-   <img alt="" src=images/BIM_TogglePanels.svg  style="width:32px;"> [Toggle bottom panels](BIM_TogglePanels.md): Shows or hides output windows (the Report view and the Python console).

-   <img alt="" src=images/BIM_Trash.svg  style="width:32px;"> [Move to Trash](BIM_Trash.md): Moves selected objects to a Trash group, which gets created if necessary

-   <img alt="" src=images/BIM_WPView.svg  style="width:32px;"> [Working Plane View](BIM_WPView.md): Sets the camera to face the current working plane

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select group](Draft_SelectGroup.md): Selects the contents of [Std Groups](Std_Group.md) or group-like [Arch](Arch_Workbench.md) objects.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Set slope](Draft_Slope.md): Slopes selected [Draft Lines](Draft_Line.md) or [Draft Wires](Draft_Wire.md) by increasing, or decreasing, the Z coordinate of all points after the first one.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Create working plane proxy](Draft_WorkingPlaneProxy.md): Creates a working plane proxy to save the current [Draft working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to construction group](Draft_AddConstruction.md): Moves objects to the [Draft construction group](Draft_ToggleConstructionMode.md).

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Split Mesh](Arch_SplitMesh.md): Splits a selected mesh into separate components.

-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Mesh to Shape](Arch_MeshToShape.md): Converts a mesh into a shape, unifying coplanar faces.

-   <img alt="" src=images/Arch_SelectNonSolidMeshes.svg  style="width:32px;"> [Select non-manifold meshes](Arch_SelectNonSolidMeshes.md): Selects all non-manifold meshes from the current selection or from the document.

-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Remove Shape from Arch](Arch_RemoveShape.md): Turns cubic shape-based Arch object fully parametric.

-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Close holes](Arch_CloseHoles.md): Closes holes in a selected shape-based object.

-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Merge Walls](Arch_MergeWalls.md): Merges walls.

-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Check](Arch_Check.md): Check if the selected objects are solids and don\'t contain defects.

-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Toggle IFC B-rep flag](Arch_ToggleIfcBrepFlag.md): Forces a selected object to be exported as an [IfcFacetedBrep](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Toggle subcomponents](Arch_ToggleSubs.md): Shows or hides the subcomponents of an Arch object.

-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Survey](Arch_Survey.md): Enters or leaves surveying mode.

-   <img alt="" src=images/BIM_Diff.svg  style="width:32px;"> [IFC Diff](BIM_Diff.md): Shows a visual diff between two IFC files

-   <img alt="" src=images/BIM_IfcExplorer.svg  style="width:32px;"> [IFC explorer](BIM_IfcExplorer.md): Opens a tool to explore the structure of an IFC file prior to importing

-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Create IFC spreadsheet\...](Arch_IfcSpreadsheet.md): This tool creates a spreadsheet to store IFC properties of an object.

-   <img alt="" src=images/BIM_ImagePlane.svg  style="width:32px;"> [Image plane](BIM_ImagePlane.md): Inserts an image plane in the document.

-   <img alt="" src=images/BIM_Unclone.svg  style="width:32px;"> [Unclone](BIM_Unclone.md): Makes a cloned object independent from its original object

-   <img alt="" src=images/BIM_Rewire.svg  style="width:32px;"> [Rewire](BIM_Rewire.md):

-   <img alt="" src=images/BIM_Glue.svg  style="width:32px;"> [Glue](BIM_Glue.md):

-   <img alt="" src=images/BIM_Reextrude.svg  style="width:32px;"> [Reextrude](BIM_Reextrude.md): Recreates an extrusion from a shape that has lost its parametric extrusion by selecting a base face

-   Panel tools:

  - <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panel](Arch_Panel.md): Creates a panel object from a selected 2D object.

  - <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Panel Cut](Arch_Panel_Cut.md): Creates a 2D cut view from a panel.

  - <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Panel Sheet](Arch_Panel_Sheet.md): Creates a 2D cut sheet including panel cuts or other 2D objects.

  - <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Nest](Arch_Nest.md): Allows to nest several flat objects inside a container shape.

-   Structure tools:

  - <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Structure](Arch_Structure.md): Creates a structural element from scratch or using a selected object as a base.

  - <img alt="" src=images/Arch_StructuralSystem.svg  style="width:32px;"> [Structural System](Arch_StructuralSystem.md):

  - <img alt="" src=images/Arch_StructuresFromSelection.svg  style="width:32px;"> [Multiple Structures](Arch_StructuresFromSelection.md):

-   <img alt="" src=images/IFC_Diff.svg  style="width:32px;"> [IFC Diff\...](IFC_Diff.md):

-   <img alt="" src=images/IFC_Expand.svg  style="width:32px;"> [IFC Expand](IFC_Expand.md):

-   <img alt="" src=images/IFC_MakeProject.svg  style="width:32px;"> [Make IFC project](IFC_MakeProject.md):

-   <img alt="" src=images/IFC_UpdateIOS.svg  style="width:32px;"> [IfcOpenShell update](IFC_UpdateIOS.md):

-   Nudge:

  - [Nudge Switch](BIM_Nudge_Switch.md):

  - [Nudge Up](BIM_Nudge_Up.md):

  - [Nudge Down](BIM_Nudge_Down.md):

  - [Nudge Left](BIM_Nudge_Left.md):

  - [Nudge Right](BIM_Nudge_Right.md):

  - [Nudge Rotate Left](BIM_Nudge_RotateLeft.md):

  - [Nudge Rotate Right](BIM_Nudge_RotateRight.md):

  - [Nudge Extend](BIM_Nudge_Extend.md):

  - [Nudge Shrink](BIM_Nudge_Shrink.md):

### Status bar 

The status bar contains a few buttons that allow to easily change different states:

-   <img alt="" src=images/BIM_TogglePanels.svg  style="width:32px;"> [Toggle panels](BIM_TogglePanels.md): Shows or hides the [Report view](Report_view.md) and the [Python console](Python_console.md).

-   <img alt="" src=images/BIM_ToggleViews.svg  style="width:32px;"> Toggle Views: Shows or hides the [BIM Views](BIM_Views.md) panel.

-   <img alt="" src=images/BIM_ToggleBackground.svg  style="width:32px;"> Cycle background: Cycles between vertical gradient, radial gradient and simple color background modes. This can be used to toggle between a dark background for modelling and a white background for 2D drawing.

-   <img alt="" src=images/IFC.svg  style="width:32px;"> Lock IFC: Switches between [locked and unlocked IFC mode](NativeIFC#Locked_and_unlocked_modes.md).

### Tree view context menu 

TBD

### 3D view context menu 

TBD

### Obsolete tools 

-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [Arch 3Views](Arch_3Views.md): Creates top, front and side views from a [mesh](Mesh_Workbench.md). Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Arch BuildingPart](Arch_BuildingPart.md): Creates a building part including selected objects. Not available in <small>(v1.0)</small> . Use [Arch Floor](Arch_Floor.md) instead.

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Arch CloneComponent](Arch_CloneComponent.md): Produces Arch Components that are clones of selected Arch objects. Not available in <small>(v1.0)</small> . Use [Draft Clone](Draft_Clone.md) instead.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Arch CutLine](Arch_CutLine.md): Cuts an object according to a line. Not available in <small>(v1.0)</small> . Use [Arch CutPlane](Arch_CutPlane.md) instead.

-   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Arch MultiMaterial](Arch_MultiMaterial.md): Creates a multi-material and attributes it to selected objects, if any. Not available in <small>(v1.0)</small> . Use [BIM Material](BIM_Material.md) instead.

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Arch Project](Arch_Project.md): Creates a project including selected objects. Not available in <small>(v1.0)</small> . Use [BIM Project](BIM_Project.md) instead.

-   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Arch SetMaterial](Arch_SetMaterial.md): Creates a material and attributes it to selected objects, if any. Not available in <small>(v1.0)</small> . Use [BIM Material](BIM_Material.md) instead.

## Preferences

-   <img alt="" src=images/Preferences-bim.svg  style="width:32px;"> [Preferences](BIM_Preferences.md): General preferences for the BIM Workbench.
-   [Fine tuning](Fine-tuning#BIM_Workbench.md): Extra parameters to fine-tune BIM behavior.

## Working with IFC 

The BIM workbench works natively with [Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC) files. Native means there is no more translation between the IFC contents and FreeCAD: The IFC contents are directly rendered in FreeCAD, and any change affects the IFC contents directly. Read more on [NativeIFC](NativeIFC.md).

If you don\'t plan to work with others, and have no need for IFC, you can still use the BIM workbench tools and simply ignore anything related to IFC. You can still export your model to IFC anytime.

The old [Arch IFC](Arch_IFC.md) importer is disabled by default in FreeCAD, but still available from Python.

## File formats 

-   [IFC](Arch_IFC.md): industry foundation classes
-   [DAE](Arch_DAE.md): Collada mesh format
-   [OBJ](Arch_OBJ.md): OBJ mesh format (export only)
-   [JSON](Arch_JSON.md): JavaScript Object Notation format (export only)
-   [3DS](Arch_3DS.md): 3DS format (import only)
-   [SHP](Arch_SHP.md): GIS Shapefiles (import only)

## API

The Arch module can be used in [Python](Python.md) scripts and [macros](Macros.md) using the [Arch Python API](Arch_API.md) functions.




<div class="mw-translate-fuzzy">

## Tutorial e apprendimento 


</div>


<div class="mw-translate-fuzzy">

-   [Migrazione a FreeCAD da Revit](Migrating_to_FreeCAD_from_Revit/it.md)
-   [Tutorial Architettura e BIM in questo wiki](Tutorials/it#Architettura_e_BIM.md)
-   [\"BIM with FreeCAD\" video series by Yorik](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
-   [\"FreeCAD tutorials\" video series by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
-   [\"Quinta Monroy\" video series by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)


</div>

## Example files 

-   FreeCAD features a BIM example file on the Start page.
-   More example BIM files are available at <https://github.com/yorikvanhavre/FreeCAD-BIM-examples> . From within FreeCAD, use menu Help -\> BIM examples.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > BIM Workbench/it
