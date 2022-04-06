# BIM Workbench/it
}

<img alt="Icona dell\'ambiente aggiuntivo BIM" src=images/IFC.svg  style="width:128px;">


{{TOCright}}

## Introduzione

L\'ambiente <img alt="" src=images/_Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/it.md) è un [ambiente esterno](External_workbenches/it.md) finalizzato all\'implementazione completa in FreeCAD degli strumenti e del flusso di lavoro[Building Information Modeling](https://en.wikipedia.org/wiki/Building_information_modeling) (BIM). Può essere installato da <img alt="" src=images/_Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md).


<div class="mw-translate-fuzzy">

L\'ambiente BIM si basa sull\'ambiente interno <img alt="" src=images/_Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench/it.md) ed entrambi saranno probabilmente uniti in futuro. BIM è un \"meta ambiente\", inteso a raccogliere molti strumenti utili da altri ambienti in un unico luogo e creare un flusso di lavoro più conveniente e intuitivo sia per gli utenti BIM esperti che per i principianti. L\'ambiente BIM presenta anche alcuni strumenti specifici, per lo più procedure guidate e strumenti di gestione, che si trovano nel menu **Gestione**.


</div>

See [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide) for a quick overview if you are already a user of another BIM application.

Gli sviluppatori di Draft, Arch e BIM collaborano anche con la più ampia [comunità OSArch](https://osarch.org), con l\'obiettivo finale di migliorare la progettazione degli edifici utilizzando software completamente gratuito.

<img alt="" src=images/BIM_workbench_presentation.png  style="width:800px;">

## Installazione


<div class="mw-translate-fuzzy">

Il workbench BIM non è in bundle con il pacchetto FreeCAD predefinito, ma può essere facilmente installato tramite il <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md). Richiamarlo da **Strumenti → [Addons Manager](Std_AddonMgr/it.md)**. Il codice del workbench BIM è [ospitato e sviluppato su github](https://github.com/yorikvanhavre/BIM_Workbench) e può anche essere installato manualmente copiandolo nella directory {{FileName|MOD}} di FreeCAD.


</div>

**Note**

L\'ambiente BIM è un work in progress e cambierà spesso. Assicurarsi di aggiornarlo regolarmente! Se il modulo [Python-Git](https://github.com/chidimo/python-git) è installato, l\'ambiente BIM cerca automaticamente gli aggiornamenti disponibili all\'avvio e se è disponibile un aggiornamento mosta un\'icona nella barra di stato.

Se la propria versione di FreeCAD non è completamente aggiornata gli strumenti elencati di seguito potrebbero non essere tutti presenti. L\'ambiente BIM dovrebbe comunque funzionare perfettamente su tutte le versioni di FreeCAD, tranne che per gli strumenti non disponibili.

## Per iniziare 

<img alt="" src=images/BIM_welcome_screen.png  style="width:800px;">


<div class="mw-translate-fuzzy">

Al primo avvio di BIM viene visualizzata una finestra di benvenuto, che fornisce una rapida panoramica di come funziona questo ambiente e consente all\'utente di avviare il [tutorial in-game](BIM_ingame_tutorial/it.md). La finestra di benvenuto è disponibile anche dal menu **Aiuto**. Quando la schermata di benvenuto viene chiusa facendo clic su OK, viene visualizzata la [finestra di dialogo di configurazione BIM](BIM_Setup/it.md), che consente all\'utente di impostare rapidamente alcune delle più comuni preferenze relative al BIM di FreeCAD senza la necessità di sfogliare tutte le pagine delle preferenze di FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Lo strumento [Configurazione del progetto BIM](BIM_Project/it.md) consente di configurare rapidamente un progetto BIM riempiendo alcune informazioni di base sul progetto. È quindi possibile, ad esempio, utilizzare i diversi strumenti di disegno 2D per tracciare linee guida e linee di base, quindi utilizzare i diversi strumenti di modellazione 3D per creare automaticamente gli oggetti BIM 3D. Una linea, ad esempio, può diventare un muro semplicemente selezionandola e premendo il pulsante [Wall](Arch_Wall/it.md).


</div>


<div class="mw-translate-fuzzy">

Se si è abituati a lavorare con un\'altra applicazione BIM, controllare la nostra [Tabella di compatibilità dell\'applicazione BIM](BIM_application_compatibility_table/it.md) quando si inizia a lavorare con FreeCAD.


</div>

<img alt="" src=images/BIM_tutorial_screenshot.png  style="width:800px;">

The [in-game tutorial](BIM_ingame_tutorial.md) is an easy way to quickly get on track with the BIM workbench.

## Strumenti


<div class="mw-translate-fuzzy">

Il workbench BIM riunisce strumenti da diversi altri workbench di FreeCAD, principalmente [Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md) e [Part](Part_Workbench/it.md), riorganizzati approssimativamente in categorie logiche di strumenti: **disegno 2D**, **modellazione 3D**, **annotazione** e **modifica**. La categoria **gestione** contiene strumenti specifici per il workbench BIM.


</div>


<div class="mw-translate-fuzzy">

Inoltre, se sono installati degli [addon](External_workbenches/it.md), gli strumenti di [Armatura](Arch_Rebar/it.md) (strumenti supplementari per le armature), [Fasteners](Fasteners_Workbench/it.md) (bulloni e viti), [Flamingo/Dodo](Flamingo_Workbench/it.md) (struttura metallica e strumenti di piping) e [Libreria di parti](Parts_Library/it.md) sono automaticamente inclusi nel workbench BIM.


</div>

L\'ambiente BIM aggiunge anche una serie di elementi nella **barra di stato** di FreeCAD e un paio di **voci nel menu contestuale**, accessibili facendo clic con il tasto destro nella vista 3D o nella vista ad albero .

### Disegni 2D 


<div class="mw-translate-fuzzy">

Gli oggetti 2D sono comunemente usati come strumenti di disegno o per disegnare linee di base e profili per costruire oggetti BIM. Possono anche essere utilizzati per disegnare simboli e annotazioni nel modello. Oltre agli schizzi, che utilizzano il proprio sistema di coordinate, gli oggetti 2D verranno disegnati sul corrente [piano di lavoro](Draft_SelectPlane/it.md).


</div>

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Schizzo](Sketcher_NewSketch/it.md): Crea un nuovo schizzo ed entra nello schizzo.
-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linea](Draft_Line/it.md): Disegna un segmento delimitato da due punti.
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Wire](Draft_Wire/it.md): Disegna una spezzata o polilinea specificando tutti i punti intermedi.
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Cerchio](Draft_Circle/it.md): Disegna una circonferenza prendendo in input il centro e il raggio.
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arco](Draft_Arc/it.md): Disegna un arco di circonferenza a partire dal centro e specificando il raggio, l\'angolo iniziale e l\'angolo finale.
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arco da 3 punti](Draft_Arc_3Points/it.md): disegna un segmento di arco circolare da tre punti che si trovano nella circonferenza
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellisse](Draft_Ellipse/it.md): Disegna una ellisse.
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Poligono](Draft_Polygon/it.md): Disegna un poligono regolare da centro, raggio e numero di lati.
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rettangolo](Draft_Rectangle/it.md): Disegna un rettangolo specificando gli angoli opposti.
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-Spline](Draft_BSpline/it.md): Interpola una traiettoria curvilinea passante per i punti specificati.
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Curva di Bezier cubica](Draft_CubicBezCurve/it.md): disegna una curva di Bezier di terzo grado trascinando due punti.
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Curva di Bezier](Draft_BezCurve/it.md): Disegna curve di Bezier su una serie di punti.
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punto](Draft_Point/it.md): Inserisce un oggetto punto.

### Annotazioni


<div class="mw-translate-fuzzy">

Le annotazioni sono oggetti di aiuto visivo che possono essere inseriti all\'interno del modello. Possono essere utilizzati per esportare il modello direttamente in un formato 2D come [DXF](Draft_DXF/it.md), o riutilizzati durante la creazione di viste 2D del modello con [TechDraw](TechDraw_Workbench/it.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Testo](Draft_Text/it.md): Disegna delle annotazioni multilinea.
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [ShapeString](Draft_ShapeString/it.md): Disegna una riga di testo come geometria.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Quota](Draft_Dimension/it.md): Disegna una dimensione lineare, angolare, radiale o di diametro.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Etichetta](Draft_Label/it.md): Posiziona un\'etichetta con una freccia che punta a un elemento selezionato. {{Version/it|0.17}}
-   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Asse](Arch_Axis/it.md): Crea un singolo asse o una seie di assi in una direzione nel documento
-   <img alt="" src=images/Arch_Axis_System.svg  style="width:32px;"> [Sistema di assi](Arch_AxisSystem/it.md): Crea un sistema di assi composto da un massimo di 3 serie di assi
-   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Griglia](Arch_Grid/it.md): Crea un oggetto simile a una griglia nel documento
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Piano di sezione](Arch_SectionPlane/it.md): Aggiunge un oggetto *Piano di sezione* al documento. I piani di sezione definiscono le viste 2D di sezioni e prospetti come piani.


</div>

### Modellazione BIM/3D 

Gli oggetti 3D e BIM sono gli elementi del mondo reale che compongono il progetto BIM.

**Struttura dell\'edificio**: Questi strumenti aiutano a organizzare il modello.

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Progetto](Arch_Project/it.md): Crea un progetto includendo gli oggetti selezionati.
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Sito](Arch_Site/it.md): Crea un sito includendo gli oggetti selezionati.
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Edificio](Arch_Building/it.md): Crea un edificio includendo gli oggetti selezionati.
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Livello](Arch_BuildingPart/it.md) (Parte di edificio):: Crea una parte di edificio che include oggetti selezionati. Le parti dell\'edificio sono comunemente usate per rappresentare i piani.
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Spazio](Arch_Space/it.md): Crea un oggetto spazio nel documento.
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Referimento](Arch_Reference/it.md): Collega oggetti di un altro file di FreeCAD in questo documento.

**Strumenti BIM**: Questi strumenti creano componenti BIM


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Muro](Arch_Wall/it.md): Crea un muro da zero o utilizzando un oggetto selezionato come base
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Facciata continua](Arch_CurtainWall/it.md): Crea una facciata continua da zero o utilizzando un oggetto selezionato come base
-   <img alt="" src=images/BIM_Column.svg  style="width:32px;"> [Colonna](Arch_Structure/it.md): Crea un elemento [Struttura](Arch_Structure/it.md) verticale in un dato punto, opzionalmente utilizzando un oggetto selezionato come profilo
-   <img alt="" src=images/BIM_Beam.svg  style="width:32px;"> [Trave](Arch_Structure/it.md): Crea un elemento [Struttura](Arch_Structure/it.md) orizzontale tra due punti, opzionalmente utilizzando un oggetto selezionato come profilo
-   <img alt="" src=images/BIM_Slab.svg  style="width:32px;"> [Lastra](Arch_Structure/it.md): Crea un elemento [Struttura](Arch_Structure/it.md) piatto estrudendo un oggetto piatto selezionato
-   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Armatura](Arch_Rebar/it.md): Crea una barra d\'armatura in un elemento strutturale selezionato utilizzando uno schizzo. Richiede l\'addon [Reinforcement](Reinforcement_Addon/it.md)
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Finestra](Arch_Window/it.md): Crea una finestra utilizzando un oggetto selezionato come base
-   <img alt="" src=images/BIM_Door.svg  style="width:32px;"> [Porta](Arch_Window/it.md): Crea un oggetto [Finestra](Arch_Window/it.md) utilizzando i preset della porta
-   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Strumenti tubazini](Arch_Pipe/it.md): Crea tubi e connessione ad angolo o a T tra 2 o 3 tubi selezionati
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Scala](Arch_Stairs/it.md): Crea un oggetto scala nel documento
-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Tetto](Arch_Roof/it.md): Crea un tetto inclinato da una faccia selezionata
-   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Strumenti pannello](Arch_Panel/it.md): Crea oggetti pannello e sagome 2D da questi pannelli
-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Carpenteria](Arch_Frame/it.md): Crea un oggetto telaio da un layout selezionato
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Recinzione](Arch_Fence/it.md): Crea un oggetto recinzione da una campata e un percorso selezionati
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Travatura](Arch_Truss/it.md): Crea una travatura da una linea selezionata o da zero
-   <img alt="" src=images/BIM_Library.png  style="width:32px;"> [Libreria](BIM_Library/it.md): Inserisce un apparecchio o un mobile. Richiede l\'addon [Parts Library](Parts_Library/it.md)
-   <img alt="" src=images/Arch_Component.png  style="width:32px;"> [Componente BIM](Arch_Component/it.md): Trasforma qualsiasi oggetto selezionato in un oggetto BIM, con supporto IFC completo


</div>

**Strumenti 3D generici**: Questi strumenti costruiscono oggetti 3D generici che possono essere trasformati o utilizzati in componenti BIM


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profilo](Arch_Profile/it.md): Crea un profilo 2D parametrico da utilizzare ad esempio nelle estrusioni
-   <img alt="" src=images/BIM_Box.png  style="width:32px;"> [Box](BIM_Box/it.md): Disegna un cuboide specificandone le dimensioni graficamente
-   <img alt="" src=images/Part_Shapebuilder.svg  style="width:32px;"> [Crea forme](Part_Builder/it.md): Uno strumento per creare forme più complesse da varie primitive geometriche parametriche
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Lega facce](Draft_Facebinder/it.md): Crea un nuovo oggetto dalle facce selezionate sugli oggetti esistenti


</div>

### Strumenti di modifica 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Sposta](Draft_Move/it.md): Sposta uno o più oggetti da una posizione a un\'altra
-   <img alt="" src=images/BIM_Copy.png  style="width:32px;"> [Copia](BIM_Copy/it.md): Copia gli oggetti da una posizione a un\'altra
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Ruota](Draft_Rotate/it.md): Ruota uno o più oggetti da un angolo di partenza a un angolo finale
-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clona](Draft_Clone/it.md): Clona gli oggetti selezionati
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Scosta](Draft_Offset/it.md): Duplica e scosta in modo equidistante i componenti di un oggetto
-   <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [Offset 2D](Part_Offset2D/it.md): Crea un contorno parallelo ad una certa distanza dall\'originale, ingrandisce o contrae una faccia piana. {{Version/it|0.17}}
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Taglia/Estendi](Draft_Trimex/it.md): Accorcia o estende (estrude) l\'oggetto selezionato
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scala](Draft_Scale/it.md): Scala gli oggetti in relazione a un punto base
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stira](Draft_Stretch/it.md): Stira gli oggetti selezionati {{Version/it|0.17}}
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Schiera](Draft_Array/it.md): Duplica e crea una schiera a matrice polare o rettangolare degli oggetti selezionati
-   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray/it.md): Crea delle copie dell\'oggetto selezionato distribuite su un percorso
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Simmetria](Draft_Mirror/it.md): Riflette gli oggetti selezionati
-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Estrudi](Part_Extrude/it.md): Estrude le facce planari di un oggetto
-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Sottrai](Part_Cut/it.md): Taglia (sottrae) un oggetto da un altro
-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Unione](Part_Union/it.md): Unisce (fonde) due oggetti
-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Interseca](Part_Common/it.md): Estrae la parte comune (intersezione) di due oggetti
-   <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Crea un composto](Part_Compound/it.md): Crea un composto dagli oggetti selezionati.
-   <img alt="" src=images/Tree_Part.svg  style="width:32px;"> [Copia semplice](Part_SimpleCopy/it.md): Crea una copia non parametrica di un oggetto selezionato
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Promuovi](Draft_Upgrade/it.md): Unisce gli oggetti in un oggetto di livello superiore
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Declassa](Draft_Downgrade/it.md): Scompone gli oggetti in oggetti di livello inferiore
-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Vista 2D](Draft_Shape2DView/it.md): Crea un oggetto 2D quale proiezione di un oggetto 3D
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Da Draft a Schizzo](Draft_Draft2Sketch/it.md): Converte un oggetto di Draft in un oggetto di [Schizzo](Sketcher_Workbench/it.md) e viceversa
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Taglia con un piano](Arch_CutPlane/it.md): Taglia un oggetto secondo un piano.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Aggiungi componente](Arch_Add/it.md): Aggiunge oggetti ad un componente
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Rimuovi componente](Arch_Remove/it.md): Sottrae o rimuove oggetti da un componente


</div>

### Strumenti di gestione 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/BIM_Setup.png  style="width:32px;"> [Configurazione BIM](BIM_Setup/it.md): Configura alcune delle preferenze di FreeCAD più comunemente utilizzate per BIM
-   <img alt="" src=images/BIM_Project.png  style="width:32px;"> [Configurazione progetto](BIM_Project/it.md): Permette di creare alcuni oggetti di base come [Sito](Arch_Site/it.md), [Edificio](Arch_Building/it.md) e [Assi](Arch_Axis/it.md) riempiendo le informazioni di base del progetto.
-   <img alt="" src=images/BIM_Views.png  style="width:32px;"> [Gestione viste e livelli](BIM_Views/it.md): Gestisce le diverse viste e livelli del progetto
-   <img alt="" src=images/BIM_Windows.png  style="width:32px;"> [Gestione finestre](BIM_Windows/it.md): Gestisce le porte e le finestre del progetto
-   <img alt="" src=images/BIM_IfcElements.png  style="width:32px;"> [Gestione elementi IFC](BIM_IfcElements/it.md): Gestisce come i diversi elementi del progetto saranno esportati in IFC
-   <img alt="" src=images/BIM_IfcProperties.svg  style="width:32px;"> [Gestione delle proprietà IFC](BIM_IfcProperties/it.md): Gestisce le proprietà IFC associate a ciascun oggetto
-   <img alt="" src=images/BIM_IfcQuantities.svg  style="width:32px;"> [Gestione delle quantità IFC](BIM_IfcQuantities/it.md): Gestisce il modo in cui le quantità degli oggetti vengono esportate esplicitamente in IFC
-   <img alt="" src=images/BIM_Classification.png  style="width:32px;"> [Gestione classificazione](BIM_Classification.md): Gestisce come gli oggetti e i materiali del progetto si riferiscono a sistemi di classificazione del tipo [Uniclass](https://en.wikipedia.org/wiki/Uniclass)
-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> [Gestione dei livelli](BIM_Layers/it.md): Gestisce i livelli del documento
-   <img alt="" src=images/Arch_Material_Group.svg  style="width:32px;"> [Materiali](Arch_SetMaterial/it.md): Gestisce i materiali o i [multimateriali](Arch_MultiMaterial/it.md) degli oggetti selezionati
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Scheda](Arch_Schedule/it.md): Crea diversi tipi di schede
-   <img alt="" src=images/BIM_Preflight.svg  style="width:32px;"> [Controlli di verifica preliminare](BIM_Preflight/it.md): Esegue diversi controlli sul modello prima di esportarlo in IFC


</div>

## Tutorial e apprendimento 


<div class="mw-translate-fuzzy">

-   [Tutorial Architettura e BIM in questo wiki](Tutorials/it#Architettura_e_BIM.md)
-   [\"BIM with FreeCAD\" video series by Yorik](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
-   [\"FreeCAD tutorials\" video series by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
-   [\"Quinta Monroy\" video series by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)


</div>

## Ambienti aggiuntivi 

Gli ambienti di lavoro per FreeCAD sono facilmente programmabili in [Python](Python/it.md), quindi ci sono molte persone che stanno sviluppando degli ambienti aggiuntivi al di fuori del codice di base di FreeCAD.


<div class="mw-translate-fuzzy">

La pagina [Ambienti complementari](external_workbenches/it.md) contiene alcune informazioni e tutorial su alcuni di loro, e il progetto [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) mira a raccoglierli e renderli facilmente installabili dall\'interno di FreeCAD.


</div>

Sono in fase di sviluppo ulteriori nuovi ambienti.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [BIM](Category_BIM.md) > BIM Workbench/it
