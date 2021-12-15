# Wikihouse porting tutorial/it
{{TutorialInfo/it
|Topic= Wikihouse porting tutorial
|Level= Intermediate/Advanced
|Time= 60 minuti
|Author=
|FCVersion=
|Files=
}}

## Introduzione

Questo tutorial spiega come convertire in FreeCAD i file di _ di FreeCAD. Il risultato è una copia completa dell\'originale file SketchUp, tranne che è diventato completamente parametrico. Il livello di parametricità del file finale dipende dalla quantità di lavoro ad esso dedicato, come spiegato di seguito. È possibile fare le cose passo dopo passo, e ricostruire il file Wikihouse abbastanza rapidamente, e rimandare a dopo il più lungo lavoro di conversione in schizzi dei profili di base.

Questo tutorial richiede una conoscenza intermedia di FreeCAD, cioè, di sapersi destreggiare tra gli ambienti di lavoro e gli strumenti, di essere già in grado di modellare oggetti semplici, e, soprattutto, di essere a proprio agio con [Draft Sposta](Draft_Move/it.md) e [Draft Ruota](Draft_Rotate/it.md). Si utilizzeranno principalmente gli strumenti di Draft e Arch, ma la conoscenza di Sketcher diventerà necessaria per convertire gli schizzi in profili di base.

Dato che il progetto Wikihouse è per natura aperto, è facile trovare i file sul sito del progetto, ma anche in [SketchUp 3D Warehouse](https://3dwarehouse.sketchup.com/search.html?q=wikihouse&backendClass=both) o nel repositorio [repositorio github](https://github.com/wikihouseproject) del progetto. Il formato preferito utilizzato dal progetto è Sketchup, quindi la maggior parte dei file che si trovano sono in tale formato.

Nel seguente tutorial abbiamo utilizzato il file [Chassis](https://github.com/wikihouseproject/Microhouse/blob/master/microhouse_0.5_chassis.skp) del sotto-progetto Wikihouse\'s Microhouse.

## Preparare il file di Sketchup 

La prima cosa da fare è aprire il file in SketchUp ed eliminare tutto ciò che non si desidera esportare. Si esporta solo una parte della Microhouse, quindi tutto il resto deve essere eliminato.

![](images/Arch_Wikihouse_05.jpg )

In SketchUp, gli elementi Wikihouse sono realizzati in un determinato modo specifico: aggiungendo un po alla volta dei piccoli \"pezzi\" per creare i diversi componenti:

![](images/Arch_Wikihouse_06.jpg )


<div class="mw-translate-fuzzy">

Questo non è il modo in cui si procederà in FreeCAD. Dato che una delle caratteristiche più potenti di FreeCAD sono gli [Schizzi vincolati](Sketcher_Workbench/it.md), è meglio approfittare di questo, e basare tutti gli elementi Wikihouse su degli schizzi. In questo modo, si può modificare qualsiasi parte in Sketcher, il che è molto più comodo.


</div>

Per trasformare gli oggetti di SketchUp in schizzi di FreeCAD, che possano poi essere utilizzati per creare dei [Pannelli](Arch_Panel/it.md), bisogna estrarre una faccia piatta da ogni pezzo Wikihouse. Lo spessore sarà nuovamente aggiunto in seguito, in FreeCAD, direttamente nelle proprietà del pannello Arch. In questo modo, diventa anche esso parametrico. Per convertire ciascun componente Wikihouse in una unica faccia piatta, entrare in ogni componente facendo doppio clic su di esso, quindi selezionare ogni sotto-componente, e fare clic destro → esplodere, fino a quando tutti i sotto-componenti sono esplosi e il componente è composto solo da facce e spigoli:

![](images/Arch_Wikihouse_08.jpg )

Fatto questo, selezionare tutto nel componente, e deselezionare, con Shift + doppio clic, ogni faccia frontale del componente. Essere sicuri di fare doppio clic, invece di un solo clic, perché altrimenti si deseleziona solo la faccia e non i suoi bordi di confine (che sono anche necessari). Con questo, avremo deselezionato tutto ciò non vogliamo mantenere, quindi basta premere il tasto di cancellazione. Ora il componente è una unica grande faccia piatta.

![](images/Arch_Wikihouse_07.jpg )

Ripetere questa operazione per ogni componente. Dato che molti sono dei duplicati, questo non è un compito così enorme come sembra. Inoltre, se non si ha familiarità con il sistema Wikihouse, questo passaggio dà una buona comprensione di come funziona.

Quando il pezzo di casa è completamente fatto di elementi piani, possiamo selezionare tutto ed esportare in un file .dae, e quindi importare questo file in FreeCAD. Assicurarsi di spuntare \"triangulate all\"

## Risolvere il bug delle facce doppie 

C\'è un brutto problema per il quale non ho trovato una soluzione migliore: gli oggetti mesh esportati da SketchUp nel formato .dae hanno le loro facce duplicate. Ogni faccia diventa in realtà due facce. Il modo più semplice che ho trovato finora è quello di aprire il file esportato in [Blender](http://www.blender.org) per ripararlo:


<div class="mw-translate-fuzzy">

1.  Aprire il file dae in Blender (File → Import → Collada)
2.  Selezionare un componente, e premere TAB per entrare in modalità di modifica
3.  Premere A per deselezionare tutto, poi di nuovo A per selezionare tutto
4.  Premere W → Remove doubles
5.  Premere TAB per uscire dalla modalità di modifica
6.  Ripetere l\'operazione per tutti i componenti
7.  Salvare un nuovo file dae (File → Export → Collada)


</div>

Normalmente l\'operazione di cui sopra non dovrebbe modificare la scala, ma prima di andare avanti è sempre meglio verificare con gli strumenti di misura che la geometria sia importata nella scala corretta. Potrebbe essere necessario modificare le impostazioni di esportazione Collada di Blender.

## L\'importazione e la conversione in polilinee 


<div class="mw-translate-fuzzy">

Notare che potrebbe essere più facile procedere per parti e trattare + esportare gli oggetti gruppo per gruppo, come abbiamo fatto qui di seguito, dove abbiamo esportato solo il primo strato, fatto di elementi gialli in SketchUp. Questi elementi entreranno in FreeCAD come oggetti [Mesh](Mesh_Workbench/it.md):


</div>

![](images/Arch_Wikihouse_09.jpg )

Il passo successivo consiste nel creare dei wire da ciascuno degli oggetti mesh. C\'è una macro utile chiamata [Estrai wire da mesh](Macro_Extract_Wires_from_Mesh/it.md) che fa proprio questo. Installarla (Fare riferimento alla pagina delle [macro](Macros/it.md) per le istruzioni), poi uno ad uno convertire tutti i mesh in oggetti wire (si può fare tutto in una volta, ma questa macro richiede un po\' di tempo):

![](images/Arch_Wikihouse_10.jpg )

Ora potremmo già creare degli oggetti _, ma questi schizzi sarebbero piuttosto pesanti, e potrebbero non essere molto maneggevoli su una macchina lenta, oppure possiamo trasformare ogni singolo wire (il contorno e ogni foro) dello schizzo in uno schizzo separato. Ciò permette, ad esempio, di riutilizzare un foro tipico, cioè di crearlo una volta sola e poi duplicarlo con [Clona](Draft_Clone/it.md) per creare gli altri fori uguali. In questo modo, basta modificarne uno per modificarli tutti.

La macro Estrai wire da mesh talvolta non riesce a trovare dei wire chiusi all\'interno di un mesh, e non produce dei pannelli corretti. Una procedura facile per ricomporre i wire di un componente è questa:

1.  Selezionare il componente, opzionalmente nascondere tutto il resto per avere una visione migliore
2.  [Scomporlo](Draft_Downgrade/it.md). Esso viene esploso in una serie di singoli spigoli
3.  Iniziare a selezionare i fori con Ctrl o utilizzando Shift + B con un rettangolo di selezione
4.  Premere [Promuovi](Draft_Upgrade/it.md) per riconvertire ogni foro in un singolo wire
5.  Infine selezionare nella struttura tutti i rimanenti singoli bordi che formano il contorno e [Promuovere](Draft_Upgrade/it.md) anche essi
6.  Selezionare **Part → crea Composto** per unire di nuovo tutti questi wire in un unico oggetto
7.  Selezionare il composto e premere il pulsante [Pannello](Arch_Panel/it.md)

![](images/Arch_Wikihouse_11.jpg )

Qui sono possibili molte strategie, a seconda di come è necessario che il risultato sia modificabile e preciso. L\'oggetto [Pannello](Arch_Panel/it.md) ha bisogno di un oggetto di base fatto di wire. Non importa come viene realizzato questo oggetto, se è un singolo schizzo, o se è, come nell\'esempio precedente, un composto di diversi schizzi o se è un oggetto di Draft.

## Conversione in Schizzi 

Dato che possiamo già creare dei pannelli da ciascun componente, si può fare questa parte in seguito, ma vediamo comunque come convertire un oggetto filiforme in uno schizzo:


<div class="mw-translate-fuzzy">

1.  Creare una copia dell\'oggetto filiforme con Ctrl+C, Ctrl+V. In questo modo è possibile modificarlo, ma mantenere ancora una copia nella sua posizione corretta
2.  Spostarlo e ruotarlo in modo che si trovi nel piano XY, utilizzando [Sposta](Draft_Move/it.md) e [Ruota](Draft_Rotate/it.md). Questo non è sempre indispensabile, ma è utile, altrimenti il punto successivo a volte fallisce
3.  Usare [Draft2Sketch](Draft_Draft2Sketch/it.md) per trasformare il wire in uno schizzo. State attenti, questa operazione può fallire o richiedere un tempo molto lungo con grossi wire. È meglio scomporre l\'oggetto in singoli wire come indicato sopra.
4.  Se il comando precedente non riesce, utilizzando [Promuovi](Draft_Upgrade/it.md) due volte su un oggetto filiforme, per convertirlo in una faccia e poi in un [Wire](Draft_Wire/it.md), prima di utilizzare [Draft Draft2Sketch](Draft_Draft2Sketch/it.md), di solito funziona meglio, perché Draft Wire mantiene una migliore traccia dell\'ordine dei vertici all\'interno di un wire.
5.  Le curve sono composte da tanti piccoli segmenti. Esse possono essere lasciate così come sono, ma introducono un sacco di vincoli endpoint. È meglio sostituirle con degli archi. È abbastanza facile da fare, basta eliminare i piccoli segmenti e sostituirli con un arco. L\'arco può quindi essere reso tangente ai segmenti attigui, ma prima di fare questo assicurarsi che la posizione di questi segmenti sia bloccata, perché questa operazione può farli muovere.
6.  Se si sono lavorati diversi schizzi, fare con essi un [Composto](Part_Compound/it.md) di Parte.
7.  Dal composto creare un [Pannello](Arch_Panel/it.md)
8.  Ruotarlo e spostarlo per riportarlo nella posizione iniziale con [Sposta](Draft_Move/it.md) e [Ruota](Draft_Rotate/it.md)


</div>

![](images/Arch_Wikihouse_12.jpg )

## Ricostruire la Wikihouse ed esportare le sagome dei fogli 

Inoltre, fare attenzione a non duplicare nessuna parte. Invece, selezionare lo strumento [Clona](Draft_Clone/it.md) per duplicare le parti basate sullo stesso profilo, in modo che esse condividano uno stesso oggetto profilo. Dopo, dato che abbiamo il contorno nella posizione corretta utilizzabile come guida, è abbastanza facile ruotare e spostare il clone nella sua corretta posizione con [Sposta](Draft_Move/it.md) e [Ruota](Draft_Rotate/it.md).

In breve tempo, tutta la sezione della Microhouse è pronta.

![](images/Arch_Wikihouse_01.jpg )


<div class="mw-translate-fuzzy">

Ora possiamo creare con facilità i fogli singoli, che sono dei file DXF da inviare al laboratorio che deve tagliare i pannelli. Il modo più semplice per farlo è quello di selezionare tutto il contenuto del documento con Ctrl+A, e quindi utilizzare lo strumento [Sagoma pannello](Arch_Panel_Cut/it.md). Questo produce un oggetto Sagoma pannello per ogni oggetto Panello trovato nella selezione. Separandoli, si ottiene una visione chiara di tutti i pezzi:


</div>

![](images/Arch_Wikihouse_02.jpg )

Bisogna quindi \"annidare\" i pezzi, cioè, spostarli e ruotarli in modo che essi occupino tutto lo spazio possibile di un determinato pannello, per generare il minor sfrido possibile. Purtroppo questa operazione deve essere fatta a mano, ma se si utilizza un progetto Wikihouse che già ha prodotto sagome di fogli, copiandoli si va abbastanza veloci:


<div class="mw-translate-fuzzy">

1.  Per essere sicuri che tutto rimarrà nel piano XY, si consiglia di impostare il [Piano di lavoro](Draft_SelectPlane/it.md) su XY (dall\'alto)
2.  Creare un [Foglio pannello](Arch_Panel_Sheet/it.md)
3.  Dargli i valori di larghezza e di altezza desiderati (I pannelli Wikihouse di solito sono stampati su fogli di compensato 122x244cm)
4.  Spostarlo in un posto comodo con [Sposta](Draft_Move/it.md)
5.  Opzionalmente, impostare i valori dei margini per avere un aiuto nel posizionare le sagome
6.  Spostare e ruotare i singoli oggetti [Sagoma pannello](Arch_Panel_Cut/it.md) in modo da inserirli nel Foglio pannello
7.  Quando si è più o meno pronti, selezionare il Foglio pannello e fare doppio clic su di esso nella vista ad albero per entrare in modalità Modifica
8.  Selezionare tutte le singole Sagome pannello che si desidera inserire in esso (si consiglia di passare dalla vista \"progetto\" alla vista albero, per poter selezionare nella struttura ad albero)
9.  Selezionare la sezione \"gruppo\" nella vista Azioni di Foglio panello
10. Premere il pulsante \"Add\"
11. Premere il pulsante \"OK\"


</div>

Nella vista Azioni di Foglio pannello, vi è anche un pulsante che consente di spostare le singole Sagome pannello dopo che esse sono state inserite nel foglio. In breve tempo, tutti i fogli sono pronti:

![](images/Arch_Wikihouse_03.jpg )

L\'ultimo passo è semplicemente quello di selezionare tutti i fogli, poi esportarli in DXF dal menu File → Esporta. I fogli contenuti vengono esportati separati in layer diversi, con lo stesso codice colore comunemente usato dal progetto Wikihouse:

![](images/Arch_Wikihouse_04.jpg )

Questi file sono pronti per essere inviati ai laboratori che faranno il taglio vero e proprio. Sarebbe anche possibile generare il codice G da inviare alla macchina CNC direttamente da FreeCAD, ma questo è materia per un altro tutorial.

---
[documentation index](../README.md) > Wikihouse porting tutorial/it
