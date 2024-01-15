# Manual:Generating 2D drawings/it
{{Manual:TOC}}

Quando il modello non può essere stampato o fresato direttamente da una macchina, perché, ad esempio, è troppo grande (un edificio) o richiede un montaggio manuale dopo che i pezzi sono pronti, di solito bisogna spiegare ad un\'altra persona come realizzarlo. Nel campo tecnico (ingegneria, architettura, ecc), questo di solito viene fatto con dei disegni. I disegni vengono consegnati alla persona responsabile dell\'assemblaggio del prodotto finale e questi spiegheranno come farlo.

Esempi tipici sono [architectural drawings](https://en.wikipedia.org/wiki/Architectural_drawing) e [blueprints](https://en.wikipedia.org/wiki/Blueprint). Questi disegni di solito contengono non solo i disegni stessi, ma anche molte annotazioni, quali testo, quote, numeri, simboli che aiutano a capire che cosa deve essere fatto e come.

In FreeCAD, l\'ambiente di lavoro responsabile della produzione di tali disegni è l\'ambiente <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench.md).

L\'ambiente TechDraw consente di creare dei fogli, che possono essere vuoti o utilizzare un [modello](TechDraw_Templates/it.md) predefinito che ha già una serie di elementi, come i bordi e un cartiglio. Su questi fogli, si possono quindi posizionare le viste degli oggetti 3D modellati in precedenza, e configurare come queste viste devono apparire sul foglio. E\' anche possibile effettuare tutti i tipi di annotazione, come quotatura, testi e altri simboli comunemente usati nei disegni tecnici.

I fogli di disegno, una volta completi, possono essere stampati o esportati come file [SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics), PDF o [DXF](https://en.wikipedia.org/wiki/AutoCAD_DXF).

Nel seguente esercizio, vedremo come creare un semplice disegno di un modello di sedia trovato in [FreeCAD library](https://github.com/FreeCAD/FreeCAD-library) (Industrial Design → Chairs → IkeaLikeChair). La libreria FreeCAD può essere facilmente aggiunta alla propria installazione FreeCAD (consultare il capitolo [installazione](Manual:Installing/it.md) di questo manuale), oppure si può semplicemente scaricare il modello dalla libreria della pagina web, oppure tramite il link diretto fornito in fondo a questo capitolo.

![](images/Exercise_TechDraw_01.svg )

-   Caricare il file IkeaLikeChair dalla libreria. Si può scegliere tra la versione .[FCStd](File_Format_FCStd/it.md), che carica la storia completa della modellazione, o la versione .[step](STEP.md), che crea solo un oggetto, senza la storia. Dato che ora non avremo bisogno di fare ulteriore modellazione, è meglio scegliere la versione .step, in quanto è più facile da manipolare.

![](images/Parts_library.jpg )

-   Passare all\'ambiente <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/it.md)
-   Premere il pulsante <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:16px;"> [Nuovo disegno da modello](TechDraw_PageTemplate/it.md).
-   Selezionare il modello **A4_Portrait_ISO7200TD**. Una nuova scheda si aprirà nella finestra di FreeCAD, mostrando la nuova pagina.
-   Nella [Vista ad albero](Tree_view/it.md) (o nella scheda del modello), selezionare il modello della sedia. Molto probabilmente si chiamerà qualcosa come \"Open CASCADE STEP translator\".
-   Premere il pulsante <img alt="" src=images/TechDraw_View.svg  style="width:16px;"> [Vista](TechDraw_View/it.md).
-   Verrà creato un oggetto View sulla nostra pagina. Selezionare l\'oggetto della vista nella vista ad albero, quindi assegnare alla vista le seguenti [proprietà](TechDraw_View#Properties/it.md) nella scheda dati della vista combinata:
    -   Sotto la categoria Base:
        -   X: 70 mm
        -   Y: 120 mm
        -   Rotazione: 0
        -   Scala: 0.1
    -   Sotto la categoria Proiezione (premi la freccia del menu a discesa per modificare singolarmente i componenti x, y e z di queste proprietà):
        -   Direzione: \[0 0 1\]
        -   XDirection: \[0 -1 0\] (Cambia prima il campo y, poi il campo x)
-   Ora abbiamo una bella vista dall\'alto della nostra sedia. Premere il pulsante <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> [Attiva o disattiva la cornice](TechDraw_ToggleFrame/it.md) per disattivare la cornice, le etichette e i vertici della vista.

![](images/Exercise_drawing_02.jpg )

-   Ripetere l\'operazione per due volte, per aggiungere altri due punti di vista. Poi impostare i valori X e Y, che indicano la posizione della vista nella pagina, per mostrarle spostate dalla vista dall\'alto, e impostare la loro direzione per creare i diversi orientamenti di vista. Dare alle nuove viste le seguenti proprietà:
    -   View001 (vista frontale): X: 70, Y: 220, Scale: 0.1, Rotation: 0, Direction: (-1,0,0), XDirection: (0,-1,0)
    -   View002 (vista laterale): X: 150, Y: 220, Scale: 0.1, Rotation: 0, (0,-1,0), XDirection: (1,0,0)
-   Fatto questo, si ottiene la seguente pagina:

![](images/Exercise_TechDraw_04.png )

-   Tieni presente che potrebbero esserci modi più semplici per ottenere le visualizzazioni che desideri. Puoi semplicemente [ruotare](Manual:Navigating_in_the_3D_view/it.md) la vista 3D del tuo modello e, una volta ottenuta la vista che desideri, selezionare il modello nella vista ad albero e premere [16px ](Image:TechDraw_View.svg.md) Nuova vista. Questo inserirà automaticamente una vista con le proprietà di rotazione e direzione desiderate. Puoi anche utilizzare lo strumento <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:16px;"> [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md).

-   Possiamo modificare l\'aspetto delle nostre viste se vogliamo, per esempio possiamo cambiare la loro proprietà **Line Width** (sotto la scheda View nella Combo View) a 0.5.

Apporremo ora quote e indicazioni sul nostro disegno. Esistono due modi per aggiungere quote a un modello: uno consiste nel posizionare le quote all\'interno del modello 3D, utilizzando lo strumento <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Quotatura](Draft_Dimension/it.md) dell\'ambiente [Draft](Draft_Workbench/it.md), quindi posizionando una vista di queste dimensioni sul nostro foglio con lo strumento <img alt="" src=images/TechDraw_DraftView.svg  style="width:16px;"> [Vista di Draft](TechDraw_DraftView/it.md). L\'altro è fare le cose direttamente sul foglio TechDraw. Useremo quest\'ultimo metodo.

-   Premere il pulsante di commutazione <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> per attivare i vertici.
-   Utilizzare Ctrl + clic sinistro del mouse per selezionare i due vertici tra cui si desidera misurare la distanza.
-   Premere il pulsante <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Lunghezza](TechDraw_LengthDimension/it.md).

![](images/Exercise_TechDraw_05.png )

-   Ripetere l\'operazione, fino a posizionare tutte le quote che si desidera indicare. Usare gli strumenti <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Dimensione verticale](TechDraw_VerticalDimension/it.md) e <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Dimensione orizzontale](TechDraw_HorizontalDimension/it.md) se necessario.
-   Prendersi un minuto per guardare le [proprietà](TechDraw_LengthDimension/it#Proprietà.md) dell\'oggetto Dimension nella vista combinata.
-   Tieni presente che se stai quotando una vista [axonometric](https://en.wikipedia.org/wiki/Axonometric_projection) (ad es. vista isometrica) invece di una [multiview](https://en.wikipedia.org/wiki/Multiview_projection) vista (ad esempio, vista frontale) come abbiamo fatto qui, dovrai utilizzare lo strumento <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:16px;"> [Link alla geometria 3D](TechDraw_LinkDimension/it.md) per ottenere una dimensione precisa.

![](images/Exercise_TechDraw_07.png )

-   Ora posizioneremo le due annotazioni mostrate nell\'immagine sopra, utilizzando lo strumento <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [Pallinatura](TechDraw_Balloon/it.md).

![](images/Exercise_TechDraw_06.png )

1.  Guardando la Pagina nella finestra [Vista 3D](3D_view/it.md), selezionare la Vista a cui sarà collegata la Pallinatura, come mostrato nell\'immagine qui sopra.
2.  Premere il pulsante <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;">.
3.  Il cursore viene ora visualizzato come icona a fumetto. Fare clic sulla pagina per posizionare l\'origine del fumetto nella posizione desiderata.
4.  La bolla del fumetto può essere trascinata nella posizione desiderata.
5.  Modificare le proprietà del fumetto facendo doppio clic sull\'etichetta del fumetto o sull\'oggetto del fumetto nella [Vista ad albero](Tree_view/it.md). Questo aprirà la finestra di dialogo Balloon Task. Impostare il campo Valore sul testo desiderato e modificare la selezione del menu a discesa Simbolo in **None**
6.  Premere **OK**
7.  Ripetere l\'operazione per il secondo callout.

-   Adesso compileremo il cartiglio del foglio.
    -   Assicurarsi che i frame, le etichette e i vertici della vista siano visibili. In caso contrario, premere il pulsante di commutazione <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;">.
    -   Modificare il testo in ogni sezione del cartiglio del foglio facendo clic sul quadratino verde a sinistra del testo.

La pagina può essere esportata in formato SVG per essere ulteriormente lavorata in applicazioni grafiche come [Inkscape](http://www.inkscape.org), o in DXF. Selezionare la pagina nella [vista ad albero](Tree_view/it.md) e poi selezionare dal menu **File → Export**. Il formato DXF è importabile in quasi tutte le applicazioni CAD 2D esistenti. Le pagine TechDraw possono anche essere direttamente stampate o esportate in formato PDF.

**Download**

-   Il file creato durante questo esercizio: [drawing.FCStd](https://github.com/JoshuaCall/FreeCAD-manual/blob/master/files/drawing.FCStd)
-   Il foglio SVG prodotto da quel file: [drawing.svg](https://github.com/JoshuaCall/FreeCAD-manual/blob/master/files/drawing.svg)

**Approfondimenti**

-   [L\'ambiente TechDraw](TechDraw_Workbench/it.md)
-   [Come creare dei modelli TechDraw personalizzati](TechDraw_TemplateHowTo/it.md)
-   [Tutorial base di TechDraw](Basic_TechDraw_Tutorial/it.md)
-   [The FreeCAD library](https://github.com/FreeCAD/FreeCAD-library)
-   [Inkscape](http://www.inkscape.org)

**Guarda i tutorial**

-   [Sliptonic\'s TechDraw playlist](https://www.youtube.com/watch?v=7LbOmSGW9F0&list=PLEuOia-QxyFKQnmM1U9yVo7eNrK_Mcln8)
-   [Symbols and Views](https://www.youtube.com/watch?v=cggBR1Ghq7k)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Generating 2D drawings/it
