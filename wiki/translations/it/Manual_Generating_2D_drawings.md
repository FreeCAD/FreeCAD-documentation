# Manual:Generating 2D drawings/it
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC/it}}


<div class="mw-translate-fuzzy">

Quando il modello non può essere stampato o fresato direttamente da una macchina, perché, ad esempio, è troppo grande (un edificio) o richiede un montaggio manuale dopo che i pezzi sono pronti, di solito bisogna spiegare ad un\'altra persona come realizzarlo. Nel campo tecnico (ingegneria, architettura, ecc), questo di solito viene fatto con dei disegni che spiegano come farlo, e che vengono consegnati al responsabile dell\'assemblaggio del prodotto finale.


</div>


<div class="mw-translate-fuzzy">

Esempi tipici sono [architectural drawings](https://en.wikipedia.org/wiki/Architectural_drawing) o [blueprints](https://en.wikipedia.org/wiki/Blueprint). Questi disegni di solito contengono non solo i disegni stessi, ma anche molte annotazioni, quali testi, dimensioni, numeri, simboli che aiutano a capire che cosa deve essere fatto e come.


</div>


<div class="mw-translate-fuzzy">

In FreeCAD, l\'ambiente di lavoro responsabile della produzione di tali disegni è [TechDraw](TechDraw_Workbench/it.md).


</div>


<div class="mw-translate-fuzzy">

L\'ambiente Drawing consente di creare dei fogli, che possono essere vuoti o utilizzare un [modello](Drawing_templates/it.md) predefinito che ha già una serie di elementi, come i bordi e il titolo. Su questi fogli, si possono quindi posizionare le [viste](Drawing_View/it.md) degli oggetti 3D modellati in precedenza, e configurare come queste viste devono apparire sul foglio. Infine, grazie ad un [addon](https://github.com/FreeCAD/FreeCAD-addons) chiamato [Drawing Dimensioning Workbench](https://github.com/hamish2014/FreeCAD_drawing_dimensioning), sul foglio è anche possibile effettuare tutti i tipi di annotazioni, come le dimensioni, testi e altri usuali simboli comunemente usati nei disegni tecnici.


</div>

I fogli di disegno, una volta completi, possono essere stampati o esportati come file [SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics), PDF o [DXF](https://en.wikipedia.org/wiki/AutoCAD_DXF).


<div class="mw-translate-fuzzy">

Nel seguente esercizio, vedremo come creare un semplice disegno di un modello di sedia trovato in [FreeCAD library](https://github.com/FreeCAD/FreeCAD-library) (Furniture -\> Chairs -\> IkeaChair). La libreria FreeCAD può essere facilmente aggiunta alla propria installazione FreeCAD (consultare il capitolo [installazione](Manual:Installing/it.md) di questo manuale), oppure si può semplicemente scaricare il modello dalla libreria della pagina web, oppure tramite il link diretto fornito in fondo a questo capitolo.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_drawing_01.jpg )


</div>


<div class="mw-translate-fuzzy">

-   Caricare il file IkeaChair dalla libreria. Si può scegliere tra la versione .FCStd, che carica la storia completa della modellazione, o la versione .step, che crea solo un oggetto, senza la storia. Dato che ora non avremo bisogno di fare ulteriore modellazione, è meglio scegliere la versione .step, in quanto è più facile da manipolare.


</div>

![](images/Parts_library.jpg )


<div class="mw-translate-fuzzy">

-   Passare nell\'ambiente [Drawing](Drawing_Workbench/it.md)
-   Premere il pulsante a forma di piccola freccia accanto a <img alt="" src=images/Drawing_Landscape_A3.png  style="width:16px;"> [Nuovo disegno](Drawing_Landscape_A3/it.md).
-   Selezionare il modello **A4 Portrait / ISO7200**. Nella finestra FreeCAD si apre una nuova scheda, che mostra la nuova pagina.
-   Nella vista ad albero (o nella scheda modello), selezionare il modello di sedia.
-   Premere il pulsante <img alt="" src=images/Drawing_View.png  style="width:16px;"> [Inserisci vista](Drawing_View/it.md).
-   Sulla pagina viene creato un oggetto View. Dare alla vista le seguenti proprietà:
    -   X: 100
    -   Y: 150
    -   Scale: 0.1
    -   Rotation: 270
-   Ora abbiamo una bella vista dall\'alto (che è la proiezione di default) della sedia:

![](images/Exercise_drawing_02.jpg )


</div>


<div class="mw-translate-fuzzy">

-   Ripetere l\'operazione per due volte, per aggiungere altri due punti di vista. Poi impostare i valori X e Y, che indicano la posizione della vista nella pagina, per mostrarle spostate dalla vista dall\'alto, e impostare la loro direzione per creare i diversi orientamenti di vista. Dare alle nuove viste le seguenti proprietà:
    -   View001 (vista frontale): X: 100, Y: 130, Scale: 0.1, Rotation: 90, Direction: (-1,0,0)
    -   View002 (vista laterale): X: 180, Y: 130, Scale: 0.1, Rotation: 90, Direction: (0,-1,0)
-   Fatto questo, si ottiene la seguente pagina:

![](images/Exercise_drawing_03.jpg )


</div>


<div class="mw-translate-fuzzy">

-   Si può modificare l\'aspetto delle viste, se vogliamo, per esempio, possiamo aumentare la loro proprietà **Line Width** (spessore della linea) a 0,5.


</div>

-   We can tweak the aspect of our views if we want, for example we can change their **Line Width** property (under the View tab in the Combo View) to 0.5.


<div class="mw-translate-fuzzy">

Ora posizioniamo le quote e le indicazioni sul disegno. Ci sono due modi per aggiungere le dimensioni ad un modello, uno consiste nel mettere le dimensioni all\'interno del modello 3D, utilizzando lo strumento <img alt="" src=images/Draft_Dimension.png  style="width:16px;"> [Dimensione](Draft_Dimension/it.md) dell\'ambiente [Draft](Draft_Workbench/it.md), e poi posizionare una vista di queste dimensioni nel foglio con lo strumento <img alt="" src=images/Drawing_DraftView.png  style="width:16px;"> [Vista Draft](Drawing_DraftView/it.md) (che può essere utilizzato su una sola dimensione o su un intero gruppo contenente le dimensioni), oppure si può fare la stessa cosa direttamente sul foglio di disegno, utilizzando l\'ambiente [Drawing Dimensioning](https://github.com/hamish2014/FreeCAD_drawing_dimensioning), che è installabile da [FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons). Qui useremo quest\'ultimo metodo.


</div>


<div class="mw-translate-fuzzy">

-   Passare all\'ambiente [Drawing Dimensioning](https://github.com/hamish2014/FreeCAD_drawing_dimensioning)
-   Premere il pulsante **Add Linear Dimension**. Nella pagina di disegno i nodi disponibili vengono evidenziati in verde:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_drawing_04.jpg )


</div>


<div class="mw-translate-fuzzy">

-   Lo strumento Quota lineare, come la maggior parte degli altri strumenti di quotatura del disegno, non esce dopo aver definito una quota, ma consente di posizionare più dimensioni. Quando si ha finito, bisogna fare clic sul pulsante **Close** nel pannello Attività.
-   Ripetere l\'operazione, fino a quando tutte le dimensioni che si desidera indicare sono posizionate. Provare per un momento a navigare attraverso le varie opzioni proposte nel pannello Azioni delle dimensioni lineari. Ad esempio, deselezionando l\'opzione **auto place text**, si può posizionare il testo della dimensione altrove, come nell\'immagine qui sotto:


</div>


<div class="mw-translate-fuzzy">

-   Ora posizioniamo alcune indicazioni, utilizzando lo strumento **Welding/Groove symbols**, selezionare quella predefinita (nessun simbolo). Disegnare le due linee come sull\'immagine qui sopra.
-   Ora posizionare due testi usando lo strumento **Aggiungi testo**, e cambiare la loro proprietà **text** con un contenuto a piacere.
-   Il disegno ora è completo, tutto ciò che resta da fare è compilare le informazioni nel cartiglio del foglio. Con la maggior parte dei modelli di default di FreeCAD, questo può essere fatto facilmente, modificando la proprietà **Editable Texts** della pagina.


</div>


<div class="mw-translate-fuzzy">

La pagina può essere esportato in formato SVG per essere ulteriormente lavorata in applicazioni grafiche come [Inkscape](http://www.inkscape.org), o in DXF selezionando il menu **File -\> Esporta**. L\'ambiente di lavoro Drawing Dimensioning dispone anche di un proprio strumento **DXF export**, che supporta anche le annotazioni aggiunte con quell\'ambiente di lavoro. Il formato DXF è importabile in quasi tutte le applicazioni CAD 2D esistenti. Le pagine di disegno possono anche direttamente essere stampate o esportate in formato PDF.


</div>

**Download**


<div class="mw-translate-fuzzy">

-   Il modello della sedia: <https://github.com/FreeCAD/FreeCAD-library/blob/master/Furniture/Chairs/IkeaLikeChair.step>
-   Il file creato durante questo esercizio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/drawing.FCStd>
-   Il foglio SVG prodotto da quel file: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/drawing.svg>


</div>

**Approfondimenti**


<div class="mw-translate-fuzzy">

-   [L\'ambiente Drawing](Drawing_Workbench/it.md)
-   [L\'ambiente Drawing Dimensioning](https://github.com/hamish2014/FreeCAD_drawing_dimensioning)
-   [La libreria di FreeCAD](https://github.com/FreeCAD/FreeCAD-library)
-   [Inkscape](http://www.inkscape.org)


</div>

**Watch tutorials**

-   [Sliptonic\'s TechDraw playlist](https://www.youtube.com/watch?v=7LbOmSGW9F0&list=PLEuOia-QxyFKQnmM1U9yVo7eNrK_Mcln8)
-   [Symbols and Views](https://www.youtube.com/watch?v=cggBR1Ghq7k)


<div class="mw-translate-fuzzy">





</div>

[<img src="images/Property.png" style="width:16px"> Tutorials](Category_Tutorials.md)

---
[documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Generating 2D drawings/it
