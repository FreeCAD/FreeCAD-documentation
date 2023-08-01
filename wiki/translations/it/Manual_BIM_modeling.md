# Manual:BIM modeling/it
}





{{Manual:TOC/it}}

BIM sta per [Building Information Modeling](https://en.wikipedia.org/wiki/Building_information_modeling) (Modello di Informazioni di un Edificio). La definizione esatta di ciò che è varia, ma possiamo dire semplicemente che è il modo attuale di modellare gli edifici e le altre strutture di grandi dimensioni, come ponti, gallerie, ecc \... I modelli BIM sono di solito basate su modelli 3D, e comprendono anche una serie di ulteriori strati di informazioni, come le informazioni sui materiali, le relazioni con altri oggetti o modelli, o le istruzioni speciali per la costruzione o la manutenzione. Queste informazioni supplementari consentono tutti i tipi di analisi avanzate del modello, come ad esempio la resistenza strutturale, i costi e le stime dei tempi di costruzione, o il calcolo del consumo energetico.

L\'ambiente [Arch](Arch_Workbench/it.md) di FreeCAD implementa una serie di strumenti e servizi per la modellazione BIM. Anche se ha uno scopo diverso, è fatto per lavorare in stretta integrazione con il resto di FreeCAD. Qualsiasi cosa fatta con qualsiasi altro ambiente di FreeCAD può diventare un oggetto Arch, o essere utilizzato come base per un oggetto Arch.

Come nell\'ambiente [PartDesign](PartDesign_Workbench/it.md), gli oggetti prodotti dall\'ambiente Arch sono destinati ad essere costruiti nel mondo reale. Pertanto, devono essere **solidi**. Gli strumenti ad Arch di solito si prendono cura di questo automaticamente, e forniscono anche degli strumenti di utilità per facilitare la verifica della validità degli oggetti.

L\'ambiente Arch comprende anche tutti gli strumenti di [Draft](Draft_Workbench/it.md), e usa la sua griglia e il sistema di aggancio. Prima di iniziare, è sempre una buona idea sfogliare le pagine delle preferenze di entrambi, Draft e Arch, e definire le impostazioni di default secondo i vostri gusti.

In questo capitolo, vedremo come modellare questo piccolo edificio:

![](images/Exercise_arch_01.jpg )

e produrre un piano e una vista in sezione da esso:

![](images/Exercise_arch_02.jpg )

-   Creare un nuovo documento e passare all\'ambiente [Arch](Arch_Workbench.md).
-   Aprire il menu **Modifica → Preferenze → Draft → Griglia e Snap** e impostare:
    -   **Linee principali ogni** `10`.
    -   **Spaziatura della griglia** `1000mm` per avere una griglia di un metro, conveniente per le dimensioni del nostro edificio.
    -   **Dimensione della griglia** `100 righe`.
-   Sulla **barra degli strumenti di snap** assicurarsi che il pulsante <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> [Snap Griglia](Draft_Snap_Grid/it.md) sia abilitato, in modo da poter utilizzare la griglia il più possibile.
-   Se non si vedono gli assi, fare clic sul pulsante <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> [Attiva/disattiva griglia](Draft_Snap_Grid/it.md).
-   Impostare il [Piano di lavoro](Draft_SelectPlane/it.md) sul piano **XY**
-   Zoom indietro e panoramica in modo da poter vedere l\'area da (0,0) a (4,3). Vedere la [Navigazione con il mouse](Mouse_navigation/it.md) per le istruzioni.
-   Disegnare quattro linee con lo strumento <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Linea](Draft_Line/it.md). E\' possibile inserire le coordinate manualmente o semplicemente selezionando i punti sulla griglia con il mouse:
    -   Dal punto (0,0) al punto (0,3)
    -   Dal punto (0,3) al punto (4,3)
    -   Dal punto (4,3) al punto (4,0)
    -   Dal punto (4,0) al punto (0,0)

NOTA: A causa di un bug nella versione 0.18, assicurarsi di eseguire le righe in questo ordine e in questa direzione.

![](images/Exercise_arch_03.jpg )

Si noti che abbiamo disegnato sempre nella stessa direzione (in senso orario). Questo non è necessario, ma farà in modo che le pareti che noi costruiremo in seguito abbiano tutte la stessa direzione, sinistra e destra. Si potrebbe anche pensare che qui avremmo potuto semplicemente disegnare un rettangolo, il che è vero. Ma le quattro linee ci permetteranno di illustrare meglio come aggiungere un oggetto in un altro.

-   Una volta create le linee, controllare i loro punti di inizio e di fine e regolare se necessario per renderle esattamente corrette.

![](images/Manual-BIM_Modeling_-_Adjusting_Lines.png )

-   Selezionare la prima linea, quindi premere il pulsante <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Muro](Arch_Wall/it.md).
-   Ripetere questa operazione per le altre 3 linee, fino a quando si dispone di 4 muri.
-   Selezionare le quattro mura, e impostare la loro proprietà **Height** a **3.00 m** e la loro proprietà **Alignment** su **left**. Se non si tracciano le linee nello stesso ordine come abbiamo fatto in precedenza, alcune delle pareti potrebbero avere le loro direzioni sinistra e destra capovolte, e Alignement potrebbe dover essere invece impostato su **right** . Si otterranno quattro pareti intersecanti, all\'interno delle linee di base:

![](images/Exercise_arch_04.jpg )

Ora si devono unire queste mura, affinché si intersechino in modo corretto. Questo non è necessario quando i muri sono disegnati in modo che siano già collegati in modo corretto, ma qui dobbiamo farlo, dato che si intersecano. In Arch, questo viene fatto decidendo che una delle pareti è \"host\" (ospite), e aggiungendo le altre a questa, come \"aggiunte\". Tutti gli oggetti Arch possono avere qualsiasi numero di aggiunte (oggetti la cui geometria verrà aggiunta alla geometria ospite), e sottrazioni (oggetti la cui geometria verrà sottratta). Le aggiunte e le sottrazioni di un oggetto possono essere gestiti in qualsiasi momento facendo doppio clic sull\'oggetto nella struttura.

-   Selezionare le quattro pareti tenendo premuto il tasto **Ctrl**, l\'ultimo dei muri scelti diventa l\'ospite.
-   Premere il tasto <img alt="" src=images/Arch_Add.svg  style="width:16px;"> [Aggiungi](Arch_Add/it.md). Ora le quattro pareti sono state trasformate in una sola:

![](images/Exercise_arch_05.jpg )

Le singole pareti sono comunque ancora accessibili, espandendo il muro nella vista ad albero.

-   Vediamo ora come posizionare una porta. In FreeCAD, le porte sono considerate un caso particolare di finestre, quindi questo viene fatto usando lo strumento [Finestra](Arch_Window/it.md).
-   Iniziare selezionando il muro. Questo non è necessario, ma è una buona abitudine da prendere. Se si seleziona un oggetto quando si avvia lo strumento Finestra, si forza l\'inserimento della finestra in quell\'oggetto, anche se si aggancia un altro oggetto.
-   Impostare il [Piano di lavoro](Draft_SelectPlane/it.md) su **auto** in modo da non sono limitati al piano terra
-   Premere il pulsante <img alt="" src=images/Arch_Window.svg  style="width:16px;"> [Finestra](Arch_Window/it.md).
-   Nel pannello di creazione della finestra, selezionare la preset **Glass door** , e impostare la sua **Width** a 0.9 m e la sua **Height** a 2.1 m
-   Assicurarsi che la casella di snap a <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Vicino](Draft_Snap_Near/it.md) sia attivata, in modo che sia possibile agganciarsi alle facce
-   Posizionare la finestra verso il centro della faccia anteriore del muro:

![](images/Exercise_arch_06.jpg )

-   Dopo aver cliccato, la finestra viene posta sulla faccia giusta, ma non esattamente dove vogliamo:

![](images/Exercise_arch_07.jpg )

-   Ora possiamo impostare la posizione precisa, espandendo il muro e gli oggetti della finestra nella vista ad albero e cambiando la proprietà **Placement** dello schizzo di base della porta. Impostare la sua posizione a **x = 2 m, y = 0, z = 0**. Ora la finestra è esattamente dove vogliamo:

![](images/Exercise_arch_08.jpg )

-   Ripetere l\'operazione per inserire una finestra: Selezionare il muro, premere lo strumento finestra, selezionare il modello predefinito **Open 2-pane**, e posizionare una finestra di 1 m x 1 m nella stessa faccia della porta. Impostare il posizionamento dello schizzo sottostante nella posizione posizionare **x = 0.6 m, y = 0, z = 1.1 m**, così la linea superiore della finestra è allineata alla parte superiore della porta.

![](images/Exercise_arch_09.jpg )

Le finestre sono sempre costruite su schizzi. Per creare facilmente delle finestre personalizzate basta creare prima uno schizzo su una faccia, poi trasformarlo in una finestra selezionandolo e premendo il pulsante finestra. Poi, i parametri di creazione della finestra, cioè i profili del disegno che devono essere estrusi e di quanto, possono essere definiti facendo un doppio clic sulla finestra nella vista ad albero. Vediamo ora creare una soletta:

-   Impostare il [Piano di lavoro](Draft_SelectPlane/it.md) sul piano **XY**
-   Creare un <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [rettangolo](Draft_Rectangle/it.md) con una **lunghezza** di 5m, una **larghezza** di 4m, nella posizione x:-0.5m, y:-0.5m, z:0.
-   Selezionare il rettangolo
-   Cliccare lo strumento <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [struttura](Arch_Structure/it.md) per creare una soletta dal rettangolo
-   Impostare la proprietà **height** della soletta a 0.2m e la sua direzione **normal** a (0,0,-1) perché vogliamo che estruderla verso il basso. Potremmo anche semplicemente spostarla in basso di 0.2m , ma è una buona norma tenere sempre gli oggetti estrusi nella stessa posizione del loro profilo di base.
-   Impostare la proprietà **Role** della soletta su **slab**. Ciò non è necessario in FreeCAD, ma è importante per l\'esportazione IFC, questo garantisce che l\'oggetto viene esportato con il corretto tipo IFC.

![](images/Exercise_arch_10.jpg )

-   Vediamo ora come utilizzare uno dei modelli di strutture predefinite per fare una trave metallica. Cliccare sul pulsante <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [struttura](Arch_Structure/it.md), selezionare il preset **HEB 180**, e impostare la sua altezza a **4m**. Posizionarla ovunque:

![](images/Exercise_arch_11.jpg )

-   Regolare il suo **placement** impostando il suo **Angle** a 90° sugli assi (1,0,0), e la sua **position** a x:90 mm, y:3.5 m, z:3.09 m.

Ciò posiziona la putrella esattamente su una delle pareti laterali:

![](images/Exercise_arch_12.jpg )

-   Ora bisogna duplicare questa trave alcune volte. Potremmo fare i duplicati uno per volta con lo strumento <img alt="" src=images/Draft_Clone.svg  style="width:16px;"> [clona](Draft_Clone/it.md), ma c\'è un modo migliore, per fare tutte le copie in una sola volta utilizzando una schiera:
-   Selezionare la trave
-   Premere il pulsante <img alt="" src=images/Draft_OrthoArray.svg  style="width:16px;"> [Serie ortogonale](Draft_OrthoArray/it.md)
-   Impostare **Numero di elementi** per la direzione X dell\'array su 6, impostare il numero per la direzione Y e Z su 1 e premere **OK**.
-   Espandere la proprietà **interval X** della serie e premere la piccola icona <img alt="" src=images/Bound-expression-unset.png  style="width:16px;"> **espressione** sul lato destro del campo X. Questo apre un [editor delle espressioni](Expressions/it.md):

![](images/Exercise_arch_13.jpg )

-   Scrivere **(4m-180mm)/5** nel campo dell\'espressione, e premere **OK**. Questo imposta il valore di x a 0.764 (4 m è la lunghezza totale della parete frontale, 180 mm è la larghezza della trave, è per questo che si chiama HEB180, e vogliamo un quinto di quello spazio come intervallo tra ogni trave):

![](images/Exercise_arch_14.jpg )

-   Ora su di loro possiamo costruire facilmente una semplice soletta, disegnando un rettangolo direttamente sul piano superiore delle travi. Selezionare una faccia superiore di una delle travi
-   Premere il pulsante <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [piano di lavoro](Draft_SelectPlane/it.md). Il piano di lavoro è ora impostato su quella faccia.
-   Creare un <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [rettangolo](Draft_Rectangle/it.md), agganciarsi ai due punti opposti del limite delle travi:

![](images/Exercise_arch_15.jpg )

-   Selezionare il rettangolo
-   Clicccare sul pulsante <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [struttura](Arch_Structure/it.md) e creare una soletta di altezza **0.2m**.

Questo è tutto, il nostro modello è completo. Ora dovremmo organizzarlo in modo che sia esportato correttamente in IFC. Il formato IFC richiede che tutti gli oggetti di un edificio siano all\'interno di un oggetto edificio, ed eventualmente, in un piano. Richiede inoltre che tutti gli edifici siano posti in un sito, ma l\'esportatore IFC di FreeCAD aggiunge automaticamente un sito predefinito, se necessario, quindi qui non abbiamo bisogno di aggiungerne uno.

-   Selezionare le due solette, il muro, e la serie di travi
-   Premere il pulsante <img alt="" src=images/Arch_Floor.svg  style="width:16px;"> [Piano](Arch_Floor/it.md)
-   Selezionare il piano appena creato
-   Premere il pulsante <img alt="" src=images/Arch_Building.svg  style="width:16px;"> [Edificio](Arch_Building/it.md)

Ora il modello è pronto per l\'esportazione:

![](images/Exercise_arch_16.jpg )

Il [formato IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) è una delle cose più preziose nel mondo BIM free, perché permette lo scambio di dati tra tutte le applicazioni e attori del mondo delle costruzioni, in modo aperto (il formato è aperto, libero e mantenuto da un consorzio indipendente). Esportare i modelli BIM come IFC assicura che chiunque può vederli e analizzarli, non importa quale applicazione viene utilizzata.

In FreeCAD, lìimportazione e l\'esportazione IFC è fatta interfacciando un\'altra parte di software, chiamato [IfcOpenShell](http://ifcopenshell.org/). Per essere in grado di esportare in IFC da FreeCAD, nel sistema deve essere installato il pacchetto [IfcOpenShell-python](http://ifcopenshell.org/python). Assicurarsi di selezionarne uno che utilizza la stessa versione Python di FreeCAD. La versione Python utilizzata da FreeCAD viene visualizzata all\'apertura del pannello **Vista -\> Pannelli -\> Console Python** in FreeCAD. Fatto questo, è possibile esportare il modello:

-   Selezionare l\'oggetto superiore che si desidera esportare, vale a dire, l\'oggetto Building.
-   Selezionare il menu **File -\> Esporta -\> Industry Foundation Classes** e salvare il file.
-   Il file IFC risultante può essere aperto in una vasta gamma di applicazioni e di visualizzatori (L\'immagine sottostante mostra il file aperto nel visualizzatore free [IfcPlusPlus](http://www.ifcquery.com/)). Controllare il file esportato in una tale applicazione di visualizzazione prima di distribuirlo ad altre persone è importante per controllare che tutti i dati contenuti nel file siano corretti. Per riaprire il file IFC risultante può anche essere utilizzato FreeCAD stesso.

![](images/Exercise_arch_17.jpg )

Ora aggiungiamo alcune dimensioni. A differenza del [capitolo precedente](Manual:Generating_2D_drawings/it.md), dove abbiamo disegnato tutte le dimensioni direttamente sul foglio da disegno, qui usiamo un altro metodo, e mettiamo le [dimensioni di Draft](Draft_Dimension/it.md) direttamente nel modello 3D. Queste dimensioni saranno poi posizionate automaticamente nel foglio di disegno. Per prima cosa creiamo due gruppi per le dimensioni, uno per le dimensioni che appaiono nella vista in pianta, e un altro per quelle che appaiono nel prospetto.

-   Fare clic sul documento \"house\" nella vista ad albero, e di creare due nuovi gruppi: **Plan dimensions** and **Elevation dimensions**.
-   Impostare come [Piano di lavoro](Draft_SelectPlane/it.md) il piano **XY**
-   Accertarsi che l\'aggancio <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [limita al piano di lavoro](Draft_Snap_WorkingPlane/it.md) sia attivato, in modo che tutto quello che si disegna sia posizionato nel piano di lavoro.
-   Disegnare un paio di <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [dimensioni](Draft_Snap_Dimensions/it.md), per esempio come nell\'immagine sottostante. Premendo **Shift** e **Ctrl** mentre si agganciano i punti di quota si ottengono opzioni aggiuntive.

![](images/Exercise_arch_18.jpg )

-   Selezionare tutte le dimensioni, e trascinarle nel gruppo **Plan dimensions** nella vista ad albero
-   Impostare come [Piano di lavoro](Draft_SelectPlane/it.md) il piano **XZ**, cioè il piano verticale frontale.
-   Ripetere le operazioni, disegnare un paio di dimensioni, e metterle nel gruppo **Elevation dimensions**.

![](images/Exercise_arch_19.jpg )

Ora prepariamo una serie di viste del modello, per posizionarle in una pagina di Disegno. Possiamo farlo con gli strumenti dell\'ambiente Drawing, come abbiamo visto nel capitolo precedente, ma l\'ambiente Arch offre anche uno strumento avanzato tutto-in-uno per la produrre le viste in pianta, le sezioni ed i prospetti, chiamato [Piano di sezione](Arch_SectionPlane/it.md). Ora aggiungeremo due di questi piani di sezione, per creare una vista in pianta e in alzato.

-   Selezionare l\'oggetto building nella vista ad albero
-   Premere il pulsante <img alt="" src=images/Arch_SectionPlane.svg  style="width:16px;"> [Piano di sezione](Arch_SectionPlane/it.md).
-   Impostare la sua proprietà **Display Height** a 5m, e **Display Length** a 6m, così circondiamo la casa (questo non è necessario, ma serve a dare un aspetto migliore, e naturalmente sarà spiegato per cosa serve), e la sua posizione **Placement** a x:2m, y:1.5m, z:1.5m.
-   Controllare l\'elenco degli oggetti considerati dal piano di sezione con un doppio clic su di esso nella [vista ad albero](Tree_view/it.md). I piani di sezione considerano solo specifici oggetti del modello, non tutti. Gli oggetti considerati dal piano di sezione possono essere cambiati qui.

![](images/Exercise_arch_20.jpg )

-   Ripetere l\'operazione per creare un altro piano di sezione, dargli la stessa lunghezza ed altezza di visualizzazione, e dargli il seguente **Placement**: position: x:2m, y:-2m, z:1.5m, angle: 90°, axis: x:1, y:0, z:0. Assicurarsi che questo nuovo piano di sezione consideri anche l\'oggetto edificio.

![](images/Exercise_arch_21.jpg )

-   Ora abbiamo tutto quello che serve, e possiamo creare la pagina di disegno. Iniziare passando all\'ambiente [Drawing](Drawing_Workbench/it.md), e creare una nuova<img alt="" src=images/Drawing_Landscape_A3.png  style="width:16px;"> [pagina A3](Drawing_Landscape_A3/it.md) predefinita (o selezionare un altro modello se lo si desidera).
-   Selezionare il primo piano di sezione, utilizzato per la vista in pianta
-   Premere il pulsante <img alt="" src=images/Drawing_DraftView.png  style="width:16px;"> [Vista Draft](Drawing_DraftView/it.md). Questo strumento offre un paio di funzionalità aggiuntive rispetto allo strumento standard [Vista Drawing](Drawing_View/it.md), e supporta i Piani di sezione dall\'ambiente Arch.
-   Dare la nuova vista le seguenti proprietà:
    -   X: 50
    -   Y: 140
    -   Scale: 0.03
    -   Line width: 0.15
    -   Show Cut True
    -   Show Fill: True
-   Selezionare l\'altro piano di sezione, e creare una nuova Vista Draft, con le seguenti proprietà:
    -   X: 250
    -   Y: 150
    -   Scale: 0.03
    -   Rendering: Solid

![](images/Exercise_arch_22.jpg )

Ora creiamo due altre Viste Draft, una per ogni gruppo di dimensioni.

-   Selezionare il gruppo Plan dimensions
-   Premere il pulsante <img alt="" src=images/Drawing_DraftView.png  style="width:16px;"> [Vista Draft](Drawing_DraftView/it.md).
-   Dare alla nuova vista le seguenti proprietà:
    -   X: 50
    -   Y: 140
    -   Scale: 0.03
    -   Line width: 0.15
    -   Font size: 10mm
-   Ripetere l\'operazione per l\'altro gruppo, con le seguenti impostazioni:
    -   X: 250
    -   Y: 150
    -   Scale: 0.03
    -   Line width: 0.15
    -   Font size: 10mm
    -   Direction: 0,-1,0
    -   Rotation: 90°

Ora la pagina è pronta, e può essere esportata nel formato SVG o DXF, o stampata. Il formato SVG può essere aperto con le applicazioni di grafica come ad esempio [inkscape](http://www.inkscape.org), con il quale è possibile migliorare rapidamente i disegni tecnici e trasformarli in disegni di presentazione molto più belli. Offre molte più possibilità rispetto al formato DXF.

## Downloads

-   Il file prodotto nel corso di questo esercizio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd>
-   Il file IFC esportato dal file precedente: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.ifc>
-   Il file in formato SVG esportato dal precedente file: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.svg>



## Correlazioni

-   [BIM Workbench](BIM_Workbench.md)
-   [L\'ambiente Arch](Arch_Workbench/it.md)
-   [Il piano di lavoro di Draft](Draft_SelectPlane/it.md)
-   [Le impostazioni di snap in Draft](Draft_Snap/it.md)
-   [Il sistema delle espressioni](Expressions/it.md)
-   [The IFC format](https://en.wikipedia.org/wiki/Industry_Foundation_Classes)
-   [IfcOpenShell](http://ifcopenshell.org/)
-   [IfcPlusPlus](http://www.ifcquery.com)
-   [Inkscape](http://www.inkscape.org)



---
![](images/Button_right.svg) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > Manual:BIM modeling/it
