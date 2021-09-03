


<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC/it}}

FreeCAD dispone di un altro ambiente di lavoro interessante da esplorare: l\'ambiente [Spreadsheet](Spreadsheet_Workbench/it.md). Questo ambiente permette di creare direttamente in FreeCAD un [foglio di calcolo](https://en.wikipedia.org/wiki/Spreadsheet) come quelli fatti con [Excel](https://en.wikipedia.org/wiki/Microsoft_Excel) o con [LibreOffice](https://en.wikipedia.org/wiki/OpenOffice.org_Calc). Questi fogli di calcolo possono essere popolati con dei dati estratti dal modello, e possono anche eseguire una serie di calcoli tra i valori. I fogli di calcolo possono essere esportati come file CSV, che possono essere importati in qualsiasi altra applicazione che gestisca i foglio di calcolo.

In FreeCAD, però, fogli di calcolo hanno un\'utilità aggiuntiva: le loro celle possono ricevere un nome, e possono quindi essere referenziate da qualsiasi campo supportato dal [motore delle espressioni](Expressions/it.md). Questo trasforma fogli di calcolo in potenti strutture di controllo, in cui i valori inseriti nelle specifiche celle possono guidare le dimensioni del modello. C\'è solo una cosa da tenere a mente, dato che FreeCAD vieta le dipendenze circolari tra oggetti, lo stesso foglio non può essere utilizzato per impostare una proprietà di un oggetto e allo stesso tempo recuperare il valore della proprietà dallo stesso oggetto. Ciò renderebbe il foglio di calcolo e l\'oggetto dipendenti l\'uno dall\'altro.

Nel seguente esempio, creeremo un paio di oggetti, recupereremo alcune delle loro proprietà in un foglio di calcolo, e quindi utilizzeremo il foglio di calcolo per guidare direttamente le proprietà di altri oggetti.

### Leggere le proprietà 


<div class="mw-translate-fuzzy">

-   Iniziare passando all\'ambiente [Part](Part_Workbench/it.md), e creare alcuni oggetti: un <img alt="" src=images/Part_Box.png  style="width:16px;"> [box](Part_Box/it.md), un <img alt="" src=images/Part_Cylinder.png  style="width:16px;"> [cilindro](Part_Cylinder/it.md) e una <img alt="" src=images/Part_Sphere.png  style="width:16px;"> [sfera](Part_Sphere/it.md).
-   Modificare le loro proprietà **Placement** (o usare lo strumento <img alt="" src=images/Draft_Move.png  style="width:16px;"> [Muovi](Draft_Move/it.md)) per separarli, in modo che si possa vedere meglio gli effetti di quello che faremo:


</div>

![](images/Exercise_spreadsheet_01.jpg )

-   Ora, si tratta di estrarre alcune informazioni su questi oggetti. Passare all\'ambiente [Spreadsheet](Spreadsheet_Workbench/it.md)
-   Premere il pulsante <img alt="" src=images/Spreadsheet_Create.png  style="width:16px;"> 
**Nuovo foglio di calcolo**
-   Fare doppio clic sul nuovo oggetto Spreadsheet nella vista ad albero. Si apre l\'editor dei fogli di calcolo:

![](images/Exercise_spreadsheet_02.jpg )

L\'editor di FreeCAD, anche se non è così completo e potente come quello dei fogli di calcolo elencati sopra, posside comunque la maggior parte degli strumenti di base e le funzioni che vengono utilizzate comunemente, come ad esempio la possibilità di cambiare l\'aspetto delle celle ( dimensione, colore, allineamento), unire e dividere le celle, l\'uso di formule come **= 2 + 2**, o di riferirsi ad altre celle con **= B1**.

In FreeCAD, oltre a queste funzionalità comuni, ce n\'è una nuova interessante: la possibilità di fare riferimento non solo ad altre celle, ma anche ad altri oggetti del documento, e di recuperare i valori dalle loro proprietà. Come esempio, proviamo a recuperare alcune proprietà dai 3 oggetti creati in precedenza. Le proprietà sono quello che possiamo vedere nella finestra dell\'editor delle proprietà, nella scheda **Dati**, quando si seleziona un oggetto.

-   Iniziamo inserendo un paio di testi nelle celle A1, A2 e A3, in modo che più avanti si possa ricordare a cosa si riferiscono, per esempio **Cube Length**, **Cylinder Radius** e **Sphere Radius**. Per immettere il testo, basta scrivere nel campo \"Contents\" sopra il foglio di calcolo, o fare doppio clic su una cella.
-   Ora recuperiamo la lunghezza attuale del cubo. Nella cella B1, digitare **=Cube.Length**. Notare che il foglio di calcolo ha un meccanismo di completamento automatico, che in realtà è lo stesso dell\'editor delle espressioni che abbiamo usato nel capitolo precedente.
-   Fare lo stesso per le celle B2 (**=Cylinder.Radius**) e B3 (**=Sphere.Radius**).

![](images/Exercise_spreadsheet_03.jpg )

-   Anche se questi risultati sono espressi con le loro unità, i valori possono essere manipolati come qualsiasi numero, provare ad esempio ad inserire nella cella C1: **=B1\*2**.
-   Ora si può cambiare uno di questi valori nel editor delle proprietà, e il cambiamento si rifletterà immediatamente nel foglio di calcolo. Per esempio, cambiamo la lunghezza del cubo a **20 mm**:

![](images/Exercise_spreadsheet_04.jpg )

Nella pagina [L\'ambiente foglio di calcolo](Spreadsheet_Workbench/it.md) sono descritte più in dettaglio tutte le possibili operazioni e le funzioni disponibili nei fogli di calcolo.

### Scrivere le proprietà 

Un altro uso molto interessante del foglio di calcolo in FreeCAD è quello di fare il contrario di quello che abbiamo fatto fino ad ora: invece di leggere i valori delle proprietà degli oggetti 3D, possiamo anche assegnare i valori a questi oggetti. Ricordate, però, una delle regole fondamentali di FreeCAD: le dipendenze circolari sono vietate. Pertanto, non possiamo usare lo stesso foglio per leggere **e** scrivere i valori di un oggetto 3D. Ciò renderebbe l\'oggetto dipendente dal foglio di calcolo, che a sua volta sarebbe dipendente dall\'oggetto. Creiamo invece un altro foglio di calcolo.


<div class="mw-translate-fuzzy">

-   Ora possiamo chiudere la scheda foglio di calcolo (nella vista 3D). Questo non è obbligatorio, non c\'è nessun problema nel mantenere diverse finestre di fogli di calcolo aperte.
-   Premere nuovamente il pulsante <img alt="" src=images/Spreadsheet_Create.png  style="width:16px;"> 
**Nuovo foglio di calcolo**
-   Cambiare il nome del nuovo foglio di calcolo con qualcosa di più significativo, come ad esempio **Input** (cliccare col tasto destro sul nuovo oggetto foglio di calcolo, e scegliere **Rinomina**).
-   Fare doppio clic sul foglio Input per aprire l\'editor dei fogli.
-   Nella cella A1, inserire un testo descrittivo, per esempio: \"Cube dimensions\"
-   Nella cella B1, scrivere **=5mm** (utilizzando il segno = si è certi che il valore viene interpretato come un valore unitario, non come un testo).
-   Ora, per poter utilizzare questo valore al di fuori del foglio di calcolo, bisogna dare un nome, o un alias, alla cella B1. Fare clic con il tasto destro del mouse sulla cella, poi fare clic su **Proprietà** e selezionare la scheda **Alias**. Dargli un nome, ad esempio **cubedims**:


</div>

![](images/Exercise_spreadsheet_05.jpg )

-   Premere **OK**, quindi chiudere la scheda foglio di calcolo
-   Selezionare l\'oggetto cubo
-   Nel editor di proprietà, fare clic sulla piccola icona <img alt="" src=images/Bound-expression-unset.png  style="width:16px;"> **espressioni** sul lato destro del campo **Length**. Si apre l\'[editor delle espressioni](Expressions.md), dove si può scrivere **Spreadsheet001.cubedims**. Ripetere questa operazione per Height e Width:

![](images/Exercise_spreadsheet_06.jpg )


<div class="mw-translate-fuzzy">

Si potrebbe chiedere perché nell\'espressione sopra abbiamo dovuto usare \"Spreadsheet001\" invece di \"Input\". Questo perché, in un documento FreeCAD, ogni oggetto ha un **nome interno**, che è unico nel documento, e una **etichetta**, che è quello che appare nella vista ad albero. Deseleziondo l\'opzione appropriata nelle impostazioni delle preferenze, FreeCAD permette di dare la stessa etichetta a più di un oggetto. Questo è il motivo per cui tutte le operazioni che devono identificare con certezza un oggetto utilizzano il nome interno ivece dell\'etichetta, che potrebbe designare più di un oggetto. Il modo più semplice per conoscere il nome interno di un oggetto è quello di mantenere aperto il **pannello selezione** (menù Visualizza -\> Pannelli -\> Selezione), esso indica sempre il nome interno di un oggetto selezionato:


</div>

![](images/Exercise_spreadsheet_07.jpg )

Usando gli alias delle celle nei fogli di calcolo, è possibile utilizzare un foglio di calcolo per memorizzare i \"valori master\" in un documento FreeCAD. Questo può essere utilizzato, ad esempio, per avere un modello di un pezzo con certe dimensioni, e per memorizzare tali dimensioni in un foglio di calcolo. Diventa quindi molto facile produrre un altro modello con dimensioni diverse, basta aprire il file e modificare un paio di quote nel foglio di calcolo.

Infine, notare che anche i vincoli all\'interno uno schizzo possono ricevere il valore da una cella del foglio:

![](images/Exercise_spreadsheet_08.jpg )

Si può anche dare un alias a vincoli dimensionali (orizzontale, verticale o distanza) in uno schizzo (quindi è anche possibile utilizzare tale valore al di fuori dello schizzo):

![](images/Exercise_spreadsheet_09.jpg )

**Download**

-   Il file prodotto in questo esercizio: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/spreadsheet.FCStd>

**Approfondimenti**

-   [L\'ambiente Foglio di calcolo](Spreadsheet_Workbench/it.md)
-   [Le espressioni](Expressions/it.md)


<div class="mw-translate-fuzzy">





</div>

[Category:Tutorials/it](Category:Tutorials/it.md)
