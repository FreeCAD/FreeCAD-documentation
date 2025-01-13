---
 TutorialInfo:t
   Topic:  Draft
   Level:  Base
   Time:  30 minuti
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei e vocx
   FCVersion: 0.19
   Files: https://forum.freecadweb.org/viewtopic.php?f=36&t=43651 Draft tutorial updated
---

# Draft tutorial/it







## Introduzione

Questo tutorial è stato originariamente scritto da Drei ed è stato riscritto e illustrato da vocx.

Questo tutorial ha lo scopo di introdurre il lettore al flusso di lavoro di base di <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/it.md).

Il lettore si eserciterà:

-   nella creazione di linee, archi e poligoni
-   nell\'uso di piani di lavoro
-   nella la creazione di dimensioni, testo e stringhe di forma
-   nella realizzazione di un disegno tecnico

Questo tutorial utilizza la notazione {{Value|(x, y, z)}} per indicare le coordinate richieste per definire i punti in un oggetto. L\'unità predefinita è il millimetro {{Value|mm}}.

<img alt="" src=images/00_Dr01_Draft_Tutorial_final.png  style="width:" height="400px;"> 
*Disegno finale comprendente vari oggetti Draft.*



## Setup

1\. Aprire FreeCAD, creare un nuovo documento vuoto con **File → [<img src=images/Std_New.svg style="width:16px"> [Nuovo](Std_New/it.md)**.

:   1.1. Passare a [Draft](Draft_Workbench/it.md) dal [selettore degli ambienti](Std_Workbench/it.md) o dal menu **Visualizza → Ambiente → [<img src=images/Workbench_Draft.svg style="width:16px"> Draft**.
:   1.2. Assicurarsi di comprendere come utilizzare l\'[editor delle proprietà](property_editor/it.md), in particolare le schede **Data** e **View** per modificare le proprietà. Quando si modificano le proprietà, potrebbe essere necessario eseguire un comando **<img src="images/Std_Refresh.svg" width=16px> [Aggiorna](Std_Refresh/it.md)** per vedere il risultato nella [vista 3D](3D_view/it.md).
:   1.3. Poiché gli oggetti Draft sono forme planari, è meglio visualizzarli dall\'alto. Utilizzare **[<img src=images/Std_ViewTop.svg style="width:16px"> [Dall'alto](Std_ViewTop/it.md)** per impostare la [Vista 3D](3D_view/it.md).
:   1.4. Sebbene non venga utilizzata in questo tutorial, la griglia Draft è utile per posizionare gli elementi geometrici. Utilizzare le **[<img src=images/Draft_SelectPlane.svg style="width:16px"> [Impostazioni del piano di lavoro](Draft_SelectPlane/it.md)** per impostare sia il piano di lavoro che la griglia, quindi mostrare e nascondere la griglia con **[16px](File_:Draft_ToggleGrid.svg.md) [Attiva/disattiva griglia](Draft_ToggleGrid/it.md)**.



## Barra degli strumenti di snap 

2\. La [Barra degli strumenti Draft Snap](Draft_Snap/it.md) viene normalmente attivata quando si passa a [Draft](Draft_Workbench/it.md).

:   2.1. Per assicurarsi che sia sempre disponibile, andare su [Preferenze Draft](Draft_Preferences/it.md), **Modifica → Preferenze → Draft → Scheda Griglia e snap**.
:   2.2. Verificare che la spunta **Mostra la barra degli strumenti di aggangio Draft** sia selezionata.

In questa medesima finestra si possono modificare anche la visibilità e le proprietà della griglia Draft.



## Piani di lavoro 

La maggior parte degli oggetti Draft sono forme planari, quindi sono naturalmente basati su un **piano di lavoro**. Un piano di lavoro può essere uno dei principali piani di coordinate globali XY, XZ e YZ, oppure può essere un piano parallelo ad essi con un offset positivo o negativo, oppure può essere un piano definito dalla faccia di un oggetto solido.

3\. Premere **[<img src=images/Draft_SelectPlane.svg style="width:16px"> [Seleziona piano](Draft_SelectPlane/it.md)**, oppure andare al menu **Utilità → [<img src=images/Draft_SelectPlane.svg style="width:16px"> [Seleziona piano](Draft_SelectPlane/it.md)**, per aprire [pannello delle attività](task_panel/it.md) per il piano di lavoro.

:   3.1. Premere **[<img src=images/Std_ViewTop.svg style="width:16px"> Dall'alto (XY)**.

Prima di premere il pulsante è inoltre possibile modificare il valore dell\'offset in millimetri, nonché la spaziatura della griglia, le linee principali e il raggio di aggancio.



## Linee e Archi 

4\. Si creeranno archi e linee.

:   4.1. Premere **[<img src=images/Draft_Arc.svg style="width:16px"> [Arco](Draft_Arc/it.md)**.
:   4.2. Impostare il **Centro** su {{Value|(0, 0, 0)}} e premere **Invio**.
:   4.3. Impostare **Raggio** su {{Value|30 mm}} e premere **Invio**.
:   4.4. Impostare **Angolo iniziale** su {{Value|60.0°}} e premere **Invio**.
:   4.5. Impostare **Angolo di apertura** su {{Value|60.0°}} e premere **Invio**.
:   4.6 Ripetere la stessa procedura per un secondo arco con raggio di {{Value|25 mm}} e con le altre proprietà invariate.

5\. Ora si creerà un profilo chiuso collegando gli archi con delle linee.

:   5.1. Cliccare il pulsante **[<img src=images/Draft_Line.svg style="width:16px"> [Linea](Draft_Line/it.md)**.
:   5.2. Nella [barra degli strumenti Snap](Draft_Snap.md) assicurarsi che **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Attiva/disattiva snap](Draft_Snap_Lock/it.md)** sia attivo e che sia selezionato solo **[<img src=images/_Draft_Snap_Endpoint.svg style="width:16px"> [Snap punto finale](Draft_Snap_Endpoint/it.md)**. Quando si sposta il ​​puntatore sull\'arco vicino a uno dei suoi punti finali, dovrebbe apparire l\'icona <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:24px;"> [Punto finale](Draft_Snap_Endpoint/it.md). Inoltre, il punto agganciato viene evidenziato con un grande punto bianco. Fare clic per selezionare questo punto.
:   5.3. Spostare il puntatore sul punto finale più vicino dell\'altro arco per unire assieme i due archi.
:   5.4. Ripetere la procedura per l\'altro lato dell\'arco per chiudere il profilo.

<img alt="" src=images/01_Dr01_Draft_Arc_profile.png  style="width:" height="400px;"> 
*Profilo chiuso creato da due archi e due linee.*



## Fusione o composizione 

Ora ci sono diversi oggetti nella [vista ad albero](tree_view/it.md) che formano un profilo chiuso. Tuttavia questo profilo è ancora composto da oggetti disconnessi; ognuno di essi può essere modificato e spostato indipendentemente dagli altri. È possibile continuare a lavorare con gli elementi in questo modo, ma è anche possibile fonderli in un unico oggetto.

6a. Tenere presente che la fusione degli oggetti in un singolo oggetto creerà un oggetto che non è più parametrico, quindi le sue proprietà non potranno più essere modificate.

:   6a.1. Selezionare tutti e quattro gli oggetti nella [vista ad albero](tree_view/it.md), oppure tenendo premuto **Ctrl** e selezionandoli nella [vista 3D](3D_view/it.md).
:   6a.2. Con questi oggetti selezionati, fare clic su **[<img src=images/Draft_Upgrade.svg style="width:16px"> [Promuovi](Draft_Upgrade/it.md)**.
:   6a.3. Così si uniranno i quattro oggetti in un singolo {{Value|Wire}}.

6b. Se si desidera mantenere la natura parametrica degli oggetti si può invece creare un composto.

:   6b.1. Passare a <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md).
:   6b.2. Dopo aver selezionato gli oggetti, fare clic su **[<img src=images/Part_Compound.svg style="width:16px"> [Crea un composto](Part_Compound/it.md)**.



## Rettangoli, circonferenze e poligoni 

7\. Si disegnerà un rettangolo. (Tornare a <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/it.md)).

:   7.1. Fare click su **[<img src=images/Draft_Rectangle.svg style="width:16px"> [Rettangolo](Draft_Rectangle/it.md)**.
:   7.2. Inserire i valori del primo punto {{Value|(-100, -60, 0)}} e premere **Invio**.
:   7.3. Assicurarsi che l\'opzione **Relativo** sia deselezionata, poiché utilizzeremo unità assolute. Si può premere **R** sulla tastiera per attivare e disattivare rapidamente questa opzione.
:   7.4. Inserire i valori per il secondo punto {{Value|(140, 90, 0)}} e premere **Invio**.

Verrà disegnato il rettangolo. Andare nell\'[editor delle proprietà](Property_editor/it.md) per modificarne le proprietà. Se non si desidera che il rettangolo crei una faccia, impostare **Make Face** su {{false}}. Se si desidera creare la faccia, ma vedere solo i bordi di quell\'oggetto, mantenere **Make Face** su {{true}} e impostare **Display Mode** su {{Value|Wireframe}}.

8\. Si disegnerà un cerchio.

:   8.1. Premere **[<img src=images/Draft_Circle.svg style="width:16px"> [Cerchio](Draft_Circle/it.md)**.
:   8.2. Inserire i valori del centro {{Value|(0, 0, 0)}} e premere **Invio**.
:   8.3. Impostare il raggio su {{value|15 mm}} e premere **Invio**.

9\. Si disegnerà un poligono regolare.

:   9.1. Premere **[<img src=images/Draft_Polygon.svg style="width:16px"> [Poligono](Draft_Polygon/it.md)**.
:   9.2. Inserire i valori del centro {{Value|(0, 0, 0)}} e premere **Invio**.
:   9.3. Impostare il numero di lati su {{Value|6}} e premere **Invio**.
:   9.4. Impostare il raggio su {{Value|50 mm}} e premere **Invio**.

Ancora una volta, se lo si desidera, si può modificare le proprietà **Make Face** e **Display Mode** nell\'[editor delle proprietà](property_editor/it.md).

Il rettangolo, il cerchio, il poligono e la maggior parte degli altri oggetti creati con [Draft](Draft_Workbench/it.md) condividono molti dati e proprietà di visualizzazione perché derivano dalla stessa classe base, [Part Part2DObject](Part_Part2DObject/it.md).

<img alt="" src=images/02_Dr01_Draft_Rectangle_circle_polygon.png  style="width:" height="400px;"> 
*Aggiunti rettangolo, cerchio e poligono.*



## Serie

Le serie vengono utilizzate per replicare un oggetto più volte in una direzione ortogonale (X, Y, Z), attorno a un asse di rivoluzione o lungo un percorso.

10\. Creeremo una serie polare.

:   10.1. Selezionare l\'oggetto {{Value|Wire}} che è stato precedentemente creato con lo strumento **[<img src=images/Draft_Upgrade.svg style="width:16px"> [Promuovi](Draft_Upgrade/it.md)** o l\'oggetto {{Value|Composto} } creato con lo strumento **[<img src=images/Part_Compound.svg style="width:16px"> [Crea un composto](Part_Compound/it.md)**.
    :10.2. Fare click su **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Serie polare](Draft_PolarArray/it.md)**.
    :10.3. Impostare l'angolo polare su {{Value|360°}}.
    :10.4. Impostare il numero di elementi su {{Value|4}}.
    :10.5. Inserire i valori per il centro di rotazione {{Value|(0, 0, 0)}} e premere **Invio**.

    L'oggetto Array mostra le copie dell'oggetto attorno all'origine.

    [x<img src=images/03_Dr01_Draft_PolarArray.png style="width:400px">
    
*Serie polare del profilo piccolo centrata attorno all'origine.*

    <span id="Dimensions"></span>
    == Quote ==

    Le quote lineari funzionano meglio quando si utilizzano i metodi [Snap](Draft_Snap/it.md) appropriati per selezionare punti e bordi da misurare. Tuttavia, possono anche essere creati specificando le coordinate assolute.

    11. Creare dimensioni per i diversi oggetti.
    :11.1. Cliccare **[<img src=images/Draft_Dimension.svg style="width:16px"> [Dimensione](Draft_Dimension/it.md)**.
    :11.2. Sceglere il primo punto. In questo tutorial il primo punto sarà sempre l'origine {{Value|(0, 0, 0)}}.
    :11.3. Nella [barra degli strumenti Snap](Draft_Snap/it.md) assicurarsi che **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Attiva/disattiva snap](Draft_Snap_Lock/it.md)** sia attivo e che solo **[<img src=images/_Draft_Snap_Midpoint.svg style="width:16px"> [Punto centrale](Draft_Snap_Midpoint/it.md)** sia selezionato. Mentre ci si sposta col ​​puntatore sul bordo superiore del poligono, dovrebbe apparire l'icona del [<img src=images/Draft_Snap_Midpoint.svg style="width:24px"> [Punto centrale](Draft_Snap_Midpoint/it.md); fare clic per selezionare questo punto.
    :11.4. Spostare il cursore a destra per specificare la posizione della quota, quindi fare clic per impostare la posizione finale, attorno a {{Value|(100, 20, 0)}}. La quota mostrerà automaticamente il valore della lunghezza misurata tra i due punti.
    :11.5. Selezionare l'oggetto dimensione nella [vista ad albero](tree_view/it.md) e, nell'[editor delle proprietà](Property_editor/it.md), modificare **Font Size** in {{Value|6 mm}}, impostare {{PropertyView |Ext Lines}} su {{Value|45 mm}} e **Show Unit** su `False`.

    12. Ripetere l'operazione per i due archi del profilo chiuso. Il primo punto della misura sarà ancora l'origine e il secondo punto utilizzerà il [<img src=images/Draft_Snap_Midpoint.svg style="width:24px"> [punto medio](Draft_Snap_Midpoint/it.md) dell'arco.

    13. Ripetere la ​​procedura per il cerchio situato al centro. Il primo punto della misurazione sarà comunque l'origine. Per selezionare il secondo punto assicurarsi che lo **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [snap](Draft_Snap_Lock/it.md)** sia attivo e che sia selezionato solo **[16px ](File:Draft_Snap_Angle.svg.md) [Angolo](Draft_Snap_Angle/it.md)**. Mentre ci si sposta col ​​puntatore sulla parte superiore del cerchio, dovrebbe apparire l'icona [<img src=images/Draft_Snap_Angle.svg style="width:24px"> [Angolo](Draft_Snap_Angle/it.md); fare clic per selezionare questo punto. Quindi spostare il cursore a destra e fare clic per fissare la dimensione.

    Ricordare di impostare **Font Size** e le altre proprietà per visualizzare correttamente la quota.

    [x<img src=images/04_Dr01_Draft_Dimension.png style="width:400px">
    
*Quote per misurare la distanza verticale dall'origine alla parte superiore del cerchio, degli archi e del poligono.*

    <span id="Texts_and_ShapeStrings"></span>
    == Annotazioni e Testi ==

    14. Gli oggetti di testo sono semplici figure planari create nella [vista 3D](3D_view/it.md) ma non hanno una vera e propria "[shape](Shape/it.md)" sottostante. Ciò significa che non possono essere utilizzati in operazioni complesse con forme come estrusioni o operazioni booleane.
    :14.1. Premere **[<img src=images/Draft_Text.svg style="width:16px"> [Testo](Draft_Text/it.md)**.
    :14.2. Selezionare il punto di riferimento nella [vista 3D](3D_view/it.md). Nella [barra degli strumenti Snap](Draft_Snap/it.md) assicurarsi che **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Attiva/disattiva snap](Draft_Snap_Lock/it.md)** sia attivo e che sia selezionato solo **[<img src=images/_Draft_Snap_Midpoint.svg style="width:16px"> [Punto centrale](Draft_Snap_Midpoint/it.md)**. Spostare il puntatore sul bordo superiore dell'arco più alto, in modo che venga visualizzata l'icona [<img src=images/Draft_Snap_Midpoint.svg style="width:24px"> [Punto centrale](Draft_Snap_Midpoint/it.md); fare clic per selezionare questo punto.
    :14.3. Inserire il **Testo** desiderato e premere **Invio** una volta per iniziare una nuova riga; aggiungere più righe di testo a seconda della necessità.
    :14.4. Quando sei pronto per terminare la creazione, premere **Invio** due volte.
    :14.5. Selezionare l'oggetto di testo nella [vista ad albero](tree_view/it.md) e nell'[editor delle proprietà](Property_editor/it.md), modificare **Font Size** in {{Value|6 mm}} e **Justification** a {{Value|Center}}.

    15. Gli oggetti ShapeString sono shape costituite da linee primitive che seguono le linee indicate da un determinato carattere. Ciò significa che questi oggetti hanno una vera "[shape](Shape/it.md)" sottostante e quindi possono essere utilizzati in operazioni complesse come estrusioni e operazioni booleane.
    :15.1. Premere **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Forma da testo](Draft_ShapeString/it.md)**.
    :15.2. Spostare il puntatore nella posizione desiderata nella [vista 3D](3D_view/it.md) sopra il poligono regolare e fare clic una volta. Ciò risolverà il punto base per la ShapeString. Le coordinate possono essere inserite anche manualmente, ad esempio {{Value|(-20, 65, 0)}}.
    :15.3. Inserire la **Stringa** desiderata e impostare la **Altezza** desiderata.
    :15.4. Se non è presente un file di font predefinito, è necessario fare clic sui puntini di sospensione **...** per aprire una finestra di dialogo per scegliere la posizione del font nel sistema.
    :15.5. Una volta specificato un file di font valido, è possibile procedere facendo clic su **OK** o premendo **Invio**.

    [x<img src=images/05_Dr01_Draft_Text_ShapeString.png style="width:400px">
    
*Aggiunta di annotazione e testo.*

    Per estrudere lettere e inciderle su solidi, vedere il [Tutorial ShapeString](Draft_ShapeString_tutorial/it.md).

    <span id="Creating_technical_drawings"></span>
    == Creazione di disegni tecnici ==

    Così com'è adesso, gli oggetti che abbiamo creato possono essere salvati, esportati in altri formati come [SVG](SVG/it.md) o [DXF](DXF/it.md), o stampati.

    Se lo si desidera, si puoi creare un disegno tecnico per visualizzare questi oggetti insieme a informazioni aggiuntive come una cornice.

    Prima di procedere, nascondere la griglia Draft premendo **[<img src=images/Draft_ToggleGrid.svg style="width:16px"> [Attiva/disattiva griglia](Draft_ToggleGrid/it.md)**.

    16. Passare a [<img src=images/Workbench_TechDraw.svg style="width:24px"> [TechDraw](TechDraw_Workbench/it.md).
    :16.1. Creare una pagina standard premendo **[<img src=images/TechDraw_PageDefault.svg style="width:16px"> [Nuovo disegno standard](TechDraw_PageDefault/it.md)**.
    :16.2. Nella [vista ad albero](tree_view/it.md) selezionare tutti gli oggetti creati, ad eccezione della pagina, quindi premere **[<img src=images/TechDraw_ActiveView.svg style="width:16px"> [Vista 3D attiva](TechDraw_ActiveView/it.md)**. Premere **OK** con le opzioni predefinite; potrebbero essere necessari alcuni secondi per creare la visualizzazione nella pagina.
    :16.3. Selezionando l'oggetto Pagina nella [vista ad albero](tree_view/it.md) verrà automaticamente visualizzata la pagina nella finestra principale. Con la pagina selezionata, andare nell'[editor delle proprietà](Property_editor/it.md) e modificare **Scale** in {{Value|0.75}}.
    :16.4. Espandere l'oggetto Pagina nella [vista ad albero](tree_view/it.md) per selezionare l'oggetto ActiveView. Con questa visualizzazione selezionata, entrare nell'[editor delle proprietà](Property_editor/it.md) e modificare **Scale Type** in {{Value|Page}}.
    :16.5. Ricalcolare il modello utilizzando **[<img src=images/Std_Refresh.svg style="width:16px"> [Aggiorna](Std_Refresh/it.md)** o premendo **F5**.
    :16.6. Nascondere le cornici degli oggetti premendo **[<img src=images/TechDraw_ToggleFrame.svg style="width:16px"> [Attiva o dissattiva le cornici](TechDraw_ToggleFrame/it.md)**.

    Scopri di più su [TechDraw](TechDraw_Workbench/it.md) leggendo il [Tutorial di base di TechDraw](Basic_TechDraw_Tutorial/it.md).

    [x<img src=images/06_Dr01_Draft_TechDraw_page.png style="width:400px">
    
*Pagina di TechDraw con una proiezione delle forme create con Draft Workbench.*

    TechDraw funziona meglio con oggetti che hanno una [TopoShape](Part_TopoShape/it.md). Poiché alcuni oggetti di Draft, come [Testi](Draft_Text/it.md) e [Dimensioni](Draft_Dimension/it.md), non hanno tali "[Shapes](Shape/it.md)", alcune operazioni di TechDraw non funzionano con questi elementi.

    Strumenti come **[<img src=images/TechDraw_ActiveView.svg style="width:16px"> [Vista 3D attiva](TechDraw_ActiveView/it.md)**, **[<img src=images/TechDraw_DraftView.svg style="width:16px"> [Vista di Draft] ]** e **[[File:TechDraw_ArchView.svg|16px](TechDraw_DraftView/it.md) [Vista di Arch](TechDraw_ArchView/it.md)** funzionano ricevendo un'immagine SVG interna generata dalle funzioni Draft interne; pertanto, TechDraw non ha molto controllo sul modo in cui vengono visualizzate queste visualizzazioni. Una maggiore integrazione di Draft e TechDraw è un lavoro in corso.

    <span id="Final_remarks"></span>
    ==Osservazioni finali==

    L'ambiente [Draft](Draft_Workbench/it.md) è per molti aspetti simile a [Sketcher](Sketcher_Workbench/it.md), poiché entrambi sono destinati a produrre forme 2D. La differenza principale sta nel modo in cui ogni ambiente gestisce i sistemi di coordinate e nel modo in cui vengono posizionati gli oggetti. In Draft, gli oggetti vengono posizionati liberamente nel sistema di coordinate globali, solitamente agganciando i loro punti a una griglia o ad altri oggetti. In Sketcher, un "[oggetto schizzo](Sketch/it.md)" definisce un sistema di coordinate locale che funge da riferimento per tutti gli elementi geometrici all'interno di quello schizzo. Inoltre, lo schizzo si basa su "vincoli" per definire la posizione finale dei suoi punti.

    * L'ambiente [Draft](Draft_Workbench.md) è destinato ai disegni 2D adatti ad essere disegnati su una griglia. [BIM](BIM_Workbench/it.md) si basa principalmente sugli strumenti definiti in [Draft](Draft_Workbench/it.md).

    * Lo [Sketcher](Sketcher_Workbench/it.md) è destinato ai disegni 2D che richiedono relazioni precise tra i suoi punti. Non si basa su una griglia, ma su regole di posizionamento (vincoli) per determinare dove verranno posizionati i punti e i bordi. Lo [Sketcher](Sketcher_Workbench/it.md) viene utilizzato principalmente insieme a [PartDesign](PartDesign_Workbench/it.md) per la creazione di [corpi](Body/it.md) solidi.

    * È possibile trasformare un oggetto Draft in uno [Sketch](Sketch/it.md), e viceversa, utilizzando lo strumento **[<img src=images/Draft_Draft2Sketch.svg style="width:16px"> [Draft2Sketch](Draft_Draft2Sketch/it.md)**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft tutorial/it
