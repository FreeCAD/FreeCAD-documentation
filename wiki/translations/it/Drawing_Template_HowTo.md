---
 TutorialInfo:t   Topic: Disegno 2D   Level: Intermedio   Author: Mark Stephen |Time: Circa un'ora   FCVersion: 0.14.3700 o superiore
---

# Drawing Template HowTo/it




<div class="mw-translate-fuzzy">


**L'ambiente [Drawing](Drawing_Workbench/it.md) è diventato obsoleto nella versione 0.17. Al suo posto utilizzare [TechDraw](TechDraw_Workbench/it.md).**


</div>


<div class="mw-translate-fuzzy">




</div>

## Introduction


<div class="mw-translate-fuzzy">

## Introduzione

Questo tutorial è una guida per creare la base e modificare un file grafico SVG da usare come un modello di squadratura nell\'ambiente [Drawing](Drawing_Workbench/it.md) di FreeCAD. A partire dalla versione 0.14, rev. 2995, di FreeCAD, il modulo Drawing proietta su un foglio di disegno la parte selezionata del modello attenendosi alle regole stabilite nel documento SVG. Tali regole definiscono l\'area di lavoro, in coordinate X e Y, in cui FreeCAD può proiettare la parte senza invadere lo spazio occupato dal cartiglio.


</div>

Chiunque progetti dei modelli da condividere dovrebbe seguire tutte le direttive di base enunciate in questo tutorial. Nel modello sono inclusi i tag per l\'area di lavoro, "Working space", e per il cartiglio, "Title block" che non sono inclusi nelle versioni precedenti di FreeCAD. Includendo questi tag si rende il modello completamente funzionante per la versione attuale.

Questo tutorial inizia con la creazione di una pagina in Inkscape e la costruzione di un disegno base del modello. Continua con l\'aggiunta di alcune opere grafiche che consentono di conferire al lavoro un tocco di personalizzazione o di professionalità. Infine, si vede come modificare il modello e quali informazioni deve contenere per essere utilizzabile in FreeCAD.

Questo tutorial presuppone che il lettore abbia una conoscenza di base di Inkscape e sappia utilizzare un editor di testo.

## Le Basi 

### Impostare la pagina 

Iniziare creando un nuovo documento in Inkscape. In riferimento alla pagina del Wiki di FreeCAD sul disegno di modelli: un pixel = un millimetro. Questo significa che per creare un modello adatto a una pagina con dimensioni ANSI A (letter size), che è di 216mm X 279mm, il modello deve avere le dimensioni di 216px X 279px. Per orientare la pagina in senso orizzontale, questi numeri devono essere invertiti. In questa esercitazione, viene utilizzato l\'orientamento orizzontale. La pagina è perciò definita con 279px per la larghezza e 216px per l\'altezza.

In Inkscape, aprire il menu \"File\" e selezionare \"Proprietà del documento\", si dovrebbe vedere la finestra delle Proprietà del documento. Modificare la larghezza e l\'altezza come detto prima e verificare che l\'unità impostata sia px.

<img alt="" src=images/Inkscape_Template_tut_1.png  style="width:780px;">

Ora si dispone di un documento Inkscape che è largo 279px e alto 216px. Si può procedere e inserire il bordo.

### Il bordo 

Quindi, creare il bordo. Sebbene ai fini di questa esercitazione non sia indispensabile, sarà utilizzato in seguito.

Usare lo strumento "Disegna tracciati e linee dritte" , e selezionare la Modalità "Crea una sequenza di segmenti parassiali", creare un rettangolo entro i confini del documento. Quando il rettangolo è chiuso, cliccare sullo strumento \"Seleziona e trasforma oggetti\". Ora il rettangolo dovrebbe apparire selezionato. In caso contrario, utilizzare lo strumento e selezionarlo.

Utilizzare le coordinate orizzontali e verticali di impostazione della selezione, insieme alle impostazioni di Larghezza e Altezza della selezione, per posizionare il rettangolo del bordo a 10 unità, (px) dai lati del documento. Inserire i seguenti valori: per X inserire 10, per Y inserire 10, per W inserire 259, e per H inserire 196. Osservare che questi valori impostano l\'angolo inferiore sinistro del rettangolo disegnato a 10 unità dal lato sinistro e 10 unità dal lato inferiore dell\'angolo inferiore sinistro della pagina. Inserendo Larghezza e Altezza si dimensiona e si centra il rettangolo nel bordo del documento.

![](images/Inkscape_Template_tut_2.png )

### Il blocco del cartiglio 

Ora è possibile costruire un riquadro delle iscrizioni o cartiglio. È la zona dove viene inserito il testo modificabile con Drawing quando il modello viene utilizzato in FreeCAD. Questo tutorial utilizza un esempio semplice. Il cartiglio può essere semplice o complesso quanto si vuole.

In questo esempio di cartiglio contiene: Nome del progetto, Data, Scala, e Autore. Viene posizionato nell\'angolo in basso a destra del bordo.

Iniziare tracciando un rettangolo qualsiasi entro i bordi del documento. Costruirlo nello stesso modo in cui si è costruito il bordo. Poi dividerlo in 4 parti a piacere. Terminata la costruzione, selezionare il rettangolo e le linee di suddivisione, renderli un gruppo, posizionarlo a X = 169, Y = 10 e dimensionarlo con W = 100, H = 50, nello stesso modo usato per il bordo.

![](images/Inkscape_Template_tut_3.png )

### Il testo fisso 

A questo punto si possono inserire nel cartiglio i blocchi di testo fissi. Sono: Nome del progetto, Data, Scala, e Autore. Per fare questo, basta selezionare lo strumento testo, fare clic da qualche parte nel documento e digitare il testo, usando un blocco diverso per ogni nome. Quindi, fare clic sullo strumento testo, poi nel documento, selezionare la dimensione appropriata del carattere, (la dimensione 6 per questo esempio) e digitare \"Nome del progetto\". Spostare il puntatore in una nuova posizione, fare di nuovo clic per iniziare un nuovo blocco di testo e digitare \"Data\". Fare la stessa cosa per Scala, e Autore. Ora, utilizzando lo strumento di selezione, spostare i singoli blocchi di testo, trascinandoli o utilizzando i tasti freccia, per sistemarli nelle posizioni desiderate.

Quando i blocchi di testo sono posizionati correttamente devono essere selezionati, insieme al cartiglio e resi un gruppo. In questo modo il cartiglio e il testo fisso diventano un blocco unico.

![](images/Inkscape_Template_tut_4.png )

### Il testo editabile 

Ora si possono aggiungere i blocchi di testo modificabili con FreeCAD. Creare e posizionare il testo modificabile nello stesso modo usato per il testo fisso. Si può digitare: NOME, DATA, SCALA, AUTORE, e impostare la dimensione 8. Quando il testo è inserito, selezionare i 4 campi di testo che si desidera siano modificabile e renderli un gruppo separato. Non includerli nel gruppo del cartiglio o del bordo. Con questa parte si è definito il testo modificabile, ma dopo aver aggiunto al modello anche la parte grafica, si deve poi completare il processo di creazione del testo modificabile con FreeCAD. Terminiamo aggiungendo al modello solo una piccola parte grafica.

![](images/Inkscape_Template_tut_5.png )

## Avanzamento

### Aggiungere una parte grafica 

Ora che il modello di base è pronto, si può aggiungere una piccola parte grafica. Può essere costituita da quello che si vuole. Il logo di una ditta o un logo grafico personale, una foto o un rendering del progetto, ecc. In questa esercitazione viene utilizzato il logo di FreeCAD, che si trova nella sezione [Artwork](Artwork/it.md) del Wiki di FreeCAD Wiki. Basta fare clic destro su di esso e selezionare Salva immagine, poi importarlo in Inkscape. L\'immagine importata nel modello può essere ridimensionata e posizionata dove si vuole. Aggiungere delle immagini al modello è facile così.

A questo punto, è possibile selezionare File, quindi Salva. In questo tutorial, il file è stato chiamato semplicemente TemplateExample.svg ma si può nominarlo come si vuole.

![](images/Inkscape_Template_tut_6.png )

## Quando il modello è pronto 

### Aprire il file con un editor di testo 

Dopo aver salvato il modello, aprirlo con l\'editor di testo preferito. Può essere un editor di base, come Blocco note di Windows, o un editor più completo, come Kate. In questo tutorial, viene utilizzato Kate e tutte le immagini sono di tale editor.

Aprendo il file SVG con l\'editor di testo si vede quanto segue.

![](images/Kate1.png )

### Il tag "xmlns:freecad" 

La prima cosa da fare è inserire nel documento la riga sottostante. Questa riga è la dichiarazione \"SVG namespace\" e deve essere fornita affinché tutti gli elementi SVG siano identificati come appartenenti a SVG namespace.

 XML
xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"



<div class="mw-translate-fuzzy">

Questa riga deve essere aggiunta immediatamente dopo il primo tag \<svg, e con la stessa indentazione con cui sono poste le altre voci xmlns.


</div>

![](images/Kate2.png )

### Page Size 


<div class="mw-translate-fuzzy">

### Formato della pagina 

Per ottenere un disegno finale stampato correttamente in scala, il modello deve contenere le sue dimensioni in unità reali. Altrimenti l\'intera pagina di disegno viene stampata ridotta di un fattore di 3,54 (90(px/in)/25,4(in/mm)).

Nel \<SVG\>-Tag viene aggiunta l\'unità \"mm\" ai campi Larghezza e Altezza. Deve anche essere aggiunto un attributo Viewbox. Il Viewbox varia da 0 alla larghezza e all\'altezza del modello. In questo modo l\'unità SVG usata (px) viene ridefinita pari a un millimetro. Di conseguenza programmi come Inkscape saranno in grado di stampare il disegno in scala. Le attuali versioni di Inkscape gestiscono molto male queste informazioni. Inkscape ridimensiona in modo efficace l\'intero documento a 90dpi. Questo non è un grosso problema per un disegno finale, ma crea delle difficoltà quando si vuole modificare i modelli. Dopo aver modificato un modello in Inkscape, si avrebbe la stessa dimensione reale, ma gli elementi del disegno sarebbero ridotti di un fattore di 3,54. (Poiché il modello sarebbe in 90dpi, ma FreeCAD assume 1px/mm). Pertanto si consiglia di rimuovere il \"mm\" dagli attributi dalla larghezza e l\'altezza prima di aprire un modello esistente in Inkscape e di ricreare dopo gli attributi unità e Viewbox.


</div>

 html
width="279mm"
height="216mm"
viewBox="0 0 279 216"


![](images/Kate2a.png )

### I tag Working space e Title block 


<div class="mw-translate-fuzzy">

Le altre righe da aggiungere sono i tag Working space (area di lavoro) e Title block (cartiglio). Questi tag e il loro utilizzo sono definiti nella pagina dei Modelli di disegno. Anche se questi tag non sono indispensabili, le versioni più recenti del Modulo Drawing di FreeCAD li usano e non influenzano le versioni precedenti.


</div>


<div class="mw-translate-fuzzy">

Il tag Working space viene utilizzato per definire lo spazio in cui FreeCAD può effettuare le proiezioni. Questo permette a FreeCAD di creare delle proiezioni automatiche nel modello di foglio rimanendo entro i bordi in cui può disegnare, o all\'interno di qualsiasi zona definita nella pagina.


</div>

Il tag Title block è usato per definire la posizione del cartiglio nell\'area di lavoro. Queste informazioni vengono usate da FreeCAD per evitare di utilizzare questo spazio come area di lavoro. L\'area del cartiglio può essere definita come \"area riservata\".

Se si utilizzano entrambi i tag, il tag Working space deve apparire per primo e essere seguito immediatamente dal tag Title block. Entrambi i tag devono anche apparire prima del primo tag \<metadata. Questi tag possono essere posizionati sia nella parte superiore, dopo il tag \<? xml o immediatamente prima del tag \<metadata. In questo tutorial sono posti all\'inizio.

#### Il tag Working space 


<div class="mw-translate-fuzzy">

Il primo tag è il tag Working space ed è formattato in questo modo:


</div>

 html



Dove:

-   X1 è la distanza sull\'asse X del lato sinistro del bordo dal lato sinistro della pagina.
-   Y1 è la distanza sull\'asse Y del lato inferiore del bordo dal lato inferiore della pagina.
-   X2 è la distanza sull\'asse X del lato destro del bordo dal lato sinistro della pagina.
-   Y2 è la distanza sull\'asse Y del lato superiore del bordo dal lato inferiore della pagina.

Quindi, per questo modello di esercitazione, il tag Working space è:

 html



#### Il tag Title block 


<div class="mw-translate-fuzzy">

Il tag successivo è il tag Title block ed è formattato in questo modo:


</div>

 html



Dove:

-   X1a è la distanza sull\'asse X del lato sinistro del cartiglio dal lato sinistro della pagina.
-   Y1a è la distanza sull\'asse Y del lato inferiore del cartiglio dal lato inferiore della pagina.
-   X2a è la distanza sull\'asse X del lato destro del cartiglio dal lato sinistro della pagina.
-   Y2a è la distanza sull\'asse Y del lato superiore del cartiglio dal lato inferiore della pagina.
-   X1a \<= X1 o X2a \>= X2
-   Y1a \<= Y1 o Y2a \>= Y2

In questo caso, sempre in riferimento al modello creato con questo tutorial, il tag Title block è:

 html



Posizionando questi due tag, in modo corretto nella parte superiore il documento appare simile al seguente:

![](images/Kate3.png )

### Il tag freecad:editable 

Aggiungendo nel documento SVG il tag freecad:editable si permette a FreeCAD di accedere ai blocchi di testo definiti per editarli. Per i blocchi di testo che si desidera siano modificabile con FreeCAD, effettuare le seguenti operazioni.

Cercare nel documento SVG fino a trovare la sezione che contiene il testo che si desidera definire modificabile. Quando si è creato il modello, il testo è stato inserito in un gruppo, e di conseguenza, anche all\'interno del documento dovrebbe apparire in un gruppo. Quando si trova questo gruppo di elementi di testo, aggiungere la riga freecad:editable=" " ad ogni blocco di testo dove il testo che si desidera rendere modificabile è contenuto all\'interno delle virgolette. Inserire la riga come indicato per tutte le quattro righe di testo da rendere modificabili.

![](images/Kate4.png )

### Il tag DrawingContent 

L\'ultimo tag necessario nel modello è il tag DrawingContent. Senza di esso, FreeCAD non può accedere al modello. Questo tag informa FreeCAD su dove, all\'interno del documento, può scrivere le proiezioni e gli altri attributi. È l\'unico tag indispensabile nel documento SVG affinché il modello funzioni con FreeCAD.

Questo tag è formattato come segue e si inserisce immediatamente prima dell\'ultimo tag \</ svg\>.

 html



![](images/Kate5.png )

Tutto qui. Ora il documento SVG può essere salvato e utilizzato con FreeCAD.

## Esempio di modello completo 


<div class="mw-translate-fuzzy">

Sotto è riportato il modello SVG finito. Siccome è in formato SVG, è possibile salvarlo e aprirlo con il proprio editor di testo per la revisione come riferimento per questa esercitazione o per creare dei propri modelli.


</div>

![](images/TemplateExample.svg )

## Strumenti

I due strumenti utilizzati in questa esercitazione sono Inkscape e Kate. Si possono trovare ai link riportati di seguito.

-   [Inkscape](http://www.inkscape.org/)
-   [Kate](http://kate-editor.org/)


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing Template HowTo/it
