


<div class="mw-translate-fuzzy">


{{docnav/it|[Modelli di mouse](Mouse_Model/it.md)|[Struttura del documento](Document_structure/it.md)}}


</div>


{{TOCright}}

Il controllo cubo di navigazione, o **cubo di navigazione**, è un aiuto grafico dell\'interfaccia utente per riorientare la vista 3D. Per impostazione predefinita, è visibile e si trova nell\'angolo in alto a destra del display 3D. Nella vista 3D standard appare in questo modo:

![](images/FreeCAD-v0-18-NavCube_Axonometric.png )

Il cubo di navigazione è costituito da diverse parti:

-   Frecce direzionali
-   Parte principale del Cubo di navigazione
-   Menu del mini-cubo

Passando il puntatore del mouse su una funzione del cubo di navigazione, la funzione diventa blu chiaro; facendo clic si riorienta la vista 3D come indicato dalla funzione. Nell\'esempio seguente, la vista 3D è stata ruotata con una [azione del mouse](Mouse_Model/it.md) in un orientamento \"non standard\". Il puntatore si trova su un angolo (indicato dal colore blu); facendo clic si riorienta la vista 3D in una vista assonometrica standard con l\'angolo rivolto verso l\'alto.

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

## Frecce direzionali 

Ci sono sei frecce direzionali: quattro punte di freccia triangolari, una in alto, in basso, a sinistra e a destra; e due frecce curve, una su ciascun lato della freccia in alto.

Facendo clic sulle frecce triangolari si ruota la vista 3D di 45 gradi attorno a una linea perpendicolare alla direzione della freccia. Facendo clic sulle frecce curve si ruota la vista 3D attorno a una linea che punta verso l\'osservatore.

## Parte principale del Cubo di navigazione 

La parte principale del cubo di navigazione (\"nav cubo\" nel resto di questa sezione), segue l\'orientamento dell\'oggetto principale della vista 3D. Qualsiasi operazione che riorienta la vista 3D principale riorienta anche il nav cubo.

Il cubo nav è essenzialmente una vista 3D di un cubo con i suoi tre tipi di componenti principali (facce, bordi e angoli) migliorati in modo che possano essere facilmente cliccati con il puntatore. Cliccando su un particolare componente si imposta la vista 3D in modo che quel componente sia centrato e rivolto verso l\'osservatore. Il cubo nav è un po \'\"schiacciato\", come se la funzione più lontana fosse più grande della funzione che si trova direttamente di fronte. Ciò consente alle funzioni adiacenti alla funzione frontale di essere viste e di conseguenza selezionate. Ad esempio, in una vista \"normale\" di un cubo regolare, quando una faccia è rivolta verso l\'osservatore, si possono vedere solo i quattro bordi della faccia e i quattro angoli di quella faccia. Nel cubo nav \"schiacciato\", si possono anche vedere le funzioni che rappresentano ciascuna delle facce adiacenti, i quattro bordi che collegano gli angoli della faccia frontale con la faccia opposta e gli angoli della faccia opposta. Ciò consente di selezionare una qualsiasi delle viste standard possibili tranne la faccia opposta e i suoi bordi (21 su 26 possibili visualizzazioni):

-   La faccia frontale (non fa nulla, poiché questa è la vista corrente)
-   I quattro bordi della faccia corrente
-   I quattro angoli della faccia corrente
-   Le quattro facce adiacenti
-   I quattro bordi che portano alla faccia opposta
-   I quattro angoli della faccia opposta

Non è possibile vedere:

-   La faccia opposta
-   I bordi della faccia opposta

Nota: al momento della scrittura (v 0.18), ci sono alcuni problemi con il cubo di navigazione; non tutte le funzioni sono attualmente selezionabili. In particolare, i bordi non sono selezionabili, e neppure i quattro angoli della faccia frontale.

### Selezione delle facce 

Cliccando su una faccia si orienta la vista 3D con quella particolare faccia rivolta frontalmente. Da una vista frontale sono disponibili altri punti di selezione, come indicato sopra. Ci sono quattro \"barre\" sottili su ciascuno dei bordi esterni, che rappresentano le quattro facce adiacenti; facendo clic su di essi si seleziona la vista corrispondente alla faccia adiacente. Ci sono quattro angoli arrotondati che possono essere usati per impostare la corrispondente vista assonometrica. C\'è anche un insieme interno di spigoli e angoli, che al momento non sono funzionali.

### Selezione dei bordi 

Sfortunatamente, la selezione dei bordi è attualmente interrotta. Il tentativo di selezionare un bordo seleziona la faccia che si trova dietro ad esso. Facendo clic su un bordo si dovrebbe centrare quel bordo in modo che sia rivolto verso l\'osservatore.

### Selezione degli angoli 

Facendo clic su uno degli angoli si ottiene una vista assonometrica vista da quell\'angolo. Come notato sopra, attualmente quando una faccia è rivolta frontalmente, gli angoli di quella faccia non sono selezionabili.

## Menu del mini-cubo 

Nell\'angolo in basso a destra del cubo di navigazione c\'è un piccolo cubo. Cliccando su questo cubo si apre un menu per cambiare il tipo di vista (ortografica, prospettiva, isometrica) e fare uno \"Zoom per adattare la vista\".


<div class="mw-translate-fuzzy">

## Spostare il cubo di navigazione 

È possibile spostare l\'intera struttura di controllo del cubo di navigazione in un\'altra posizione nella visualizzazione 3D premendo il mouse in qualsiasi punto del cubo di navigazione principale e trascinando. Al momento della scrittura (v 0.18), la struttura non inizia a muoversi finché il puntatore del mouse non viene spostato oltre il bordo del cubo di navigazione principale.


</div>

## Configuration

The navigation cube is configurable, including adjusting its size: **Edit → Preferences... → Display → Navigation → Navigation cube** <small>(v0.19)</small> .

For more advanced configuration, refer to the [CubeMenu](Interface_Customization#CubeMenu.md) [external workbench](External_workbenches.md).


<div class="mw-translate-fuzzy">


{{docnav/it|[Modelli di mouse](Mouse_Model/it.md)|[Struttura del documento](Document_structure/it.md)}}


</div>




[Category:User Documentation{{\#translation:}}](Category:User_Documentation.md)
