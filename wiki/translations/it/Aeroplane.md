---
- TutorialInfo:/it
   Topic:Part
   Level:Base
   Time:10 minuti
   Author:Hughthecat
   FCVersion:
   Files:
---

# Aeroplane/it





## First Steps 


<div class="mw-translate-fuzzy">

## Prima parte 

L\'ambiente di lavoro è <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Parte](Part_Workbench/it.md) - selezionarlo tramite il menu **Visualizza → Ambiente → Parte** oppure tramite il [selettore degli ambienti](Std_Workbench/it.md).


</div>


<div class="mw-translate-fuzzy">

-   Creare un nuovo documento vuoto.
-   Passare alla visualizzazione assonometrica.
-   Attivare la visualizzazione del sistema di coordinate (nel menu Visualizza → Origine degli assi).
-   Assicurarsi di avere disponibile la [Vista combinata](Combo_View/it.md), attivabile tramite **Visualizza → Viste → Vista combinata**.


</div>

-   Creare un cilindro standard facendo clic sul pulsante <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Cilindro](Part_Cylinder/it.md).
-   Selezionare il cilindro facendo clic su di esso nell\'esploratore del progetto.
-   Fare clic sulla scheda Dati nella parte inferiore dell\'esploratore del progetto.

Impostare una Altezza pari a 20 mm. Lasciare il Raggio a 2 mm.


<div class="mw-translate-fuzzy">

Cliccare sul testo Posizionamento (Placement; non sul segno di espansione; non sul piccolo **[+]**), in modo da far apparire un nuovo pulsante contenente tre punti. Fare clic sul pulsante con i tre puntini **...**. (Si può anche selezionare: **Menu → Modifica → Posizionamento**). Viene mostrata la finestra delle Azioni di Posizionamento.


</div>

<img alt="" src=images/HTCaeroplane01.png  style="width:300px;">

Per acquisire dimestichezza con gli assi X, Y e Z si possono sperimentare diversi valori nelle caselle di posizionamento. Alla fine, per annullare le modifiche, premere il pulsante **Ripristina**.



## Seconda parte 

<img alt="" src=images/HTCaeroplane02.png  style="width:400px;">

Ora si deve ruotare il cilindro in modo da allinearlo con l\'asse X. Per ottenere questo, il cilindro deve essere ruotato intorno all\'asse Y. Nella finestra di Posizionamento, selezionare la voce *Asse di rotazione con angolo* della sezione \"Rotazione\", quindi impostare l\'asse Y come asse di rotazione e incrementare l\'angolo fino a raggiungere il valore 90°. Fare clic su **OK**.

A questo punto fare pratica con la rotazione della vista (ripetutamente!), con tutti i modi a disposizione. La \'cucitura\' del cilindro deve trovarsi sul lato inferiore.

<img alt="" src=images/HTCaeroplane03.png  style="width:400px;">

Ora si deve aggiungere un cubo facendo clic sul pulsante <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cubo](Part_Box/it.md) e successivamente modificarlo. Selezionarlo facendo clic su Cubo nell\'esploratore del progetto. Modificare l\'altezza a 1 mm, la lunghezza a 5 mm e la larghezza a 20 mm.


<div class="mw-translate-fuzzy">

Cliccare su [Posizionamento → **...**](Tasks_Placement.md) per visualizzare le \"Azioni di posizionamento\". Digitare nei campi del comando \"Traslazione\" Y: -10 e Z: -1. Fare clic su **OK**.


</div>


<div class="mw-translate-fuzzy">

Ora si devono unire queste due forme con una operazione booleana. Fare clic sul pulsante <img alt="" src=images/Part_Booleans.svg  style="width:32px;"> [Operazioni Booleane](Part_Boolean/it.md) per visualizzare il selettore delle operazioni booleane nella finestra delle Azioni.


</div>

Assicurarsi che sia selezionata l\'operazione Unione, e che il cilindro e il parallelepipedo siano entrambi selezionati una volta nei due elenchi delle forme. Fare clic su **Applica** e dopo su **Chiudi**. Ora si dispone di un singolo oggetto chiamato **Fusione**.




Aggiungere un nuovo parallelepipedo per completare il modello. Creare un Cubo, selezionarlo e modificare la sua altezza a 5 mm, lunghezza a 3 mm e larghezza a 1 mm. Cambiare il suo posizionamento con Y: -0,5.


<div class="mw-translate-fuzzy">

Ora si deve unire l\'oggetto Fusione con l\'oggetto Box001, vediamo quindi come farlo nel modo più veloce. Fare clic sull\'oggetto Fusione nell\'esploratore del progetto e con il tasto **Ctrl** premuto fare clic sull\'oggetto Box001. Questo seleziona entrambe le parti. Ora cliccare sul pulsante <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Fusione](Part_Union/it.md) per ottenere come risultato l\'oggetto **Fusion001**.


</div>

A questo punto, si dovrebbe avere un modello molto elementare di aereo. Fare clic con il destro su **Fusion001** e rinominarlo **Aeroplane**.

<img alt="" src=images/HTCaeroplane04.png  style="width:500px;">

Supponiamo di voler spostare in avanti le ali. Selezionando \'Aeroplane\' e provando a modificare la sua Posizione di traslazione sull\'asse X si muove tutto l\'oggetto. Si vuole invece modificare solo il Posizionamento delle ali.

Espandere \'Aeroplane\' (clic su **[+]** alla sua sinistra) e espandere anche Fusione.


<div class="mw-translate-fuzzy">

Fare clic su Cubo e visualizzare le azioni per il suo posizionamento. Notare che in Traslazione sono già impostati i valori Y: -10 e Z: -1. Modificare la traslazione e impostare X = 3 poi fare clic su **Applica**. Questo modo funziona. Fare clic su **OK**.


</div>






## Rotazioni


<div class="mw-translate-fuzzy">

Cliccare su Aeroplane e visualizzare le Azioni per il suo posizionamento. Nella sezione Rotazione cambiare \'asse di rotazione con angolo\' con \'angoli di Eulero\' con cui è molto più facile lavorare.


</div>

![](images/Tache_Placement_Lacet_fr_Mini.gif )**Imbardata è la rotazione intorno all\'asse Z**, da destra a sinistra e viceversa. (L\'angolo di imbardata è **Psi ψ**).  ![](images/Tache_Placement_Tangage_fr_Mini.gif )**Beccheggio è la rotazione intorno all\'asse Y**, alzare o abbassare il naso. (L\'angolo di beccheggio è **Phi φ**).  ![](images/Tache_Placement_Roulis_fr_Mini.gif )**Rollio è la rotazione intorno all\'asse X**, dondolare le ali. (L\'angolo di rollio è **Thêta θ**).




Tuttavia, ci sono alcune cose importanti da ricordare:

-   Le rotazioni positive sono in senso orario se viste dall\'origine nella direzione positiva di un asse. O, per dirla in altro modo: le rotazioni positive sono in senso antiorario se viste da un asse positivo verso l\'origine.

-   Anche se le tre etichette utilizzate per le rotazioni sono Imbardata, Beccheggio e Rollio, in realtà non sono esattamente questo. Imbardata, Beccheggio e Rollio si riferiscono alle *coordinate corpo* di un oggetto nello spazio 3D. Le voci delle etichette dovrebbero essere, Longitudine, Latitudine e Inclinazione o anche Azimuth, Inclinazione e Bank perché si riferiscono in realtà alle *coordinate spaziali* del sistema 3D. Questi sono gli **angoli di Tait-Bryan**. Per maggiori informazioni consultare [Angoli di Eulero](http://es.wikipedia.org/wiki/%C3%81ngulos_de_Euler).

-   Con l\'Aeroplane nella sua posizione attuale si applicano le seguenti semplici regole. Imbardata è la rotazione attorno all\'asse Z, vale a dire sinistra e destra. Beccheggio è la rotazione attorno all\'asse Y, ossia muso verso l\'alto o verso il basso. Rollio è la rotazione attorno all\'asse X, vale a dire alzare o abbassare le ali. Questo va bene per cominciare, ma in seguito non sarà sufficiente!

Esercitarsi con i tre valori di Imbardata, Beccheggio e Rollio (angoli di rotazione). Basta solo cambiare i valori di pochi gradi per capire cosa succede. Al termine, utilizzare il pulsante Ripristina .

Ora vedremo perché le etichette Imbardata, Beccheggio e Rollio, non sono le più adatte. Modificare il valore di Rollio in 90°. Imbardata dovrebbe spostare il muso dell\'aereo in sù o in giù e Beccheggio dovrebbe muoverlo lateralmente *come visto dall\'esterno del velivolo* cioè dalla posizione in cui ci troviamo. Ma non lo fanno! Beccheggio modifica Imbardata e Imbardata cambia Beccheggio. OK, Reset.

Quindi, un modo migliore di pensare le rotazioni è che Imbardata cambia la longitudine, Beccheggio modifica la latitudine e Rollio la direzione (Nord, Sud, Est e Ovest) che si sta seguendo. Per maggiori informazioni si può consultare [Convenzioni per gli assi](http://en.wikipedia.org/wiki/Axes_conventions).


<div class="mw-translate-fuzzy">

Bene, torniamo al lavoro. Cambiare Imbardata a 45° e Beccheggio a -30°. Fare clic su OK per indicare che l\'operazione è stata completata. Ora tornare alle Azioni di Posizionamento e osservare la sezione Rotazione. E\' ritornata l\'impostazione \"Asse di rotazione con angolo\" e i campi degli assi e degli angoli contengono degli strani valori. Ad esempio Assi: (0.219493, -0.529904, 0.819161) e Angolo: 53,65°. I tre numeri tra parentesi sono i componenti XYZ di un vettore unitario nello spazio 3D. E\' l\'asse intorno al quale l\'Aeroplane originale è stato ruotato per ottenere l\'Aeroplane finale. L\'angolo indica di quanto è stato ruotato. Interessante, ma non proprio semplice! E\' stato Eulero che ha dimostrato che si può combinare una serie di rotazioni XYZ in una rotazione su un asse.


</div>

Ecco alcuni ulteriori suggerimenti per esercitarsi con l\'Aereo:

-   Modificare la Posizione Z (e Applicare), quindi modificare i valori YPR (valori dei campi della rotazione) e vedere che cosa succede. Dopo provare a modificare le posizioni X e Y e la Rotazione.
-   Modificare il Centro X (e Applicare) e poi cambiare i valori YPR e vedere che cosa succede. Provare a cambiare il centro di rotazione in Y e in Z e la rotazione.

Spero che questo piccolo tutorial sia di aiuto per gestire le rotazioni.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Category_Part.md) > Aeroplane/it
