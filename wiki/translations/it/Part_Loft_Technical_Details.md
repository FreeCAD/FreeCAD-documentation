# Part Loft Technical Details/it
Questa pagina spiega nei dettagli come viene creata una superficie con [Part Loft](Part_Loft/it.md). Questo vale anche per una superficie [Part Sweep](Part_Sweep/it.md) prodotta lungo un percorso rettilineo, anche se ci sono alcune differenze.

Le informazioni fornite si riferiscono a una specifica implementazione e potrebbero cambiare. Queste sono adatte per FreeCAD 0.15.4119 e OCC versione: 6.7.0.

## Stages of the Loft creation 


<div class="mw-translate-fuzzy">

## Fasi della creazione di Loft 

Per spiegare il processo di Loft, convene dividerlo in fasi:

1.  creare lo stesso numero di segmenti nei profili (se non sono ancora uguali)
2.  stabilire la corrispondenza tra i segmenti
3.  produrre la superficie Loft


</div>

### Step 1. Making numbers of segment in profiles match 


<div class="mw-translate-fuzzy">

### Fase 1. Creare nei profili il numero di segmenti da abbinare 

Lo strumento Loft ha bisogno del numero dei segmenti da abbinare per poter creare delle superfici tra i segmenti corrispondenti. Se il numero di segmenti corrisponde in tutti i profili, questo passaggio viene saltato.


</div>

Se almeno uno dei profili ha un numero di segmenti diverso dagli altri, viene applicata la seguente procedura. Per sempicità, in questo esempio la procedura è descritta usando solo due profili.

1.  i profili vengono temporaneamente allineati per renderli complanari e far coincidere i loro centri di massa\* (baricentri).
2.  come si vede nell\'immagine sottostante, per ogni vertice di un profilo, il secondo profilo viene suddiviso con lo stesso angolo polare (il centro polare è il centro di massa). Se è possibile fare più di una suddivisione o non è possibile farne nessuna (può succedere su profili molto convessi), il Loft di solito fallisce.
3.  lo stesso avviene nella direzione opposta.

L\'operazione è applicata a tutti i profili, per produrre in ognuno un numero uguale di segmenti. Il numero totale di segmenti in ciascun profilo sarà pari alla somma di tutti i numeri di segmenti di tutti i profili (capita che su un determinato angolo polare non sia disponibile nessun vertice).

   
  <img alt="Il processo con cui profile2 (la forma simile a una mezzaluna bianca) viene suddiviso per creare le giunzioni corrispondenti ai vertici di profile1 (il pentagono rosso). Le giunzioni inserite sono contrassegnate dalle frecce gialle." src=images/Loft-vertex-insertion.png  style="width:300px;">   <img alt="Il risultato del Loft relativo all\'immagine di sinistra." src=images/Loft_crescent_pentagon.png  style="width:300px;">
   

### Step 2. Establishing correspondence between segments 


<div class="mw-translate-fuzzy">

### Fase 2. Stabilire la corrispondenza tra i segmenti 

<img alt="Dimostrazione che Loft mantiene il numero di segmenti nei profili quando essi corrispondono. Notare come 3 bordi del quadrato superiore \"collassino\" in un breve tratto poligonale del profilo inferiore." src=images/Loft_Number_of_verts_match.png  style="width:300px;"> Nel caso che il numero di segmenti non fosse stato uguale in tutti i profili, sarebbe stata fatta una suddivisione come nella fase 1. La corrispondenza è banale. Nel caso in cui il numero di segmenti è uguale in tutti i profili, vengono utilizzati i segmenti esistenti (vedi immagine). Questo è il momento in cui deve essere stabilita la corrispondenza.


</div>

L\'algoritmo completo usato per trovare i segmenti corrispondenti è complesso, ma generalmente tende a minimizzare la torsione del Loft risultante. Ciò significa che se si sta facendo un Loft tra due quadrati, la torsione massima possibile è \<45 °. Una ulteriore rotazione di uno dei quadrati provoca lo scambio dei vertici.

La corrispondenza tra i profili adiacenti è fatta in modo indipendente. Ciò significa che si può ottenere una torsione aggiuntiva (maggiore) aggiungendo più profili.

Un\'altra cosa da notare è che quando il numero di segmenti nei profili è uguale, il Loft risultante è sostanzialmente più robusto rispetto ai profili complessi, specie per quelli non convessi. 

### Step 3. Making the loft surface 


<div class="mw-translate-fuzzy">

### Fase 3. Creare la superficie Loft. 

<img alt="Esempio di una curva di interpolazione spline (rossa) che segue la superficie Loft. I punti attraverso cui è interpolata sono visualizzati come quadrati rossi." src=images/Loft_B-spline.png  style="width:400px;"> Se ci sono solo due profili, le superfici create sono delle superfici rigate tra i segmenti corrispondenti dei profili. Per collegare i vertici corrispondenti dei profili vengono creati dei bordi dritti.


</div>

Se vi sono più di due profili, le superfici sono costituite di spline costruite nello stesso modo delle linee rette delle superfici rigate. La superficie è \"fatta di\" spline immaginarie che sono disegnate interpolando i punti corrispondenti nei corrispettivi segmenti dei profili.

Le spline sono una interpolazione di B-spline.

-   Se il numero di profili è inferiore a 10, l\'interpolazione viene eseguita con da una B-spline con il massimo grado possibile (es. gradi = numero_di_profili - 1).
-   Se il numero di profili è maggiore di 10, l\'interpolazione avviene secondo una B-spline di 3°grado.

Il metodo di lavoro utilizzato è \"lunghezza approssimativa della corda\". Rimangono approssimative per il fatto che in un Loft il nodo vettore è esattamente lo stesso per ogni spline. Per maggiori informazioni su ciò che riguarda l\'interpolazione delle B-spline, il nodo vettore, il metodo \"lunghezza della corda\", si veda, ad esempio, [cs.mtu.edu Curve Global Interpolation](http://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/INT-APP/CURVE-INT-global.html).

Notare che Loft ha una proprietà \"Ruled\". Se è impostata su true, le superfici rigate sono realizzate tra profili vicini anche quando c\'è più di un profilo. Questo significa che l\'interpolazione delle B-spline è sostituita da una interpolazione lineare a tratti. 

## The main point 


<div class="mw-translate-fuzzy">

## Il punto principale 

-   Il Loft è prodotto con delle B-spline interpolate tra i profili forniti. L\'interpolazione viene commutata in lineare a tratti quando la proprietà \"Ruled\" è impostata su true.
-   Quando il numero di profili è maggiore di 9, il grado di interpolazione scende a 3. Questo passaggio può ridurre in modo sostanziale le oscillazioni.
-   La corrispondenza del numero di segmenti (alias numero di vertici) nei profili permette di dare ai Loft una leggera torsione, e tipicamente permette di utilizzare dei profili più complessi.
-   Quando i numeri di segmenti non sono corrispondenti, è meglio mantenere i profili in modo che possano essere rappresentati con una corretta funzione r (phi) in coordinate polari.


</div>

## Additional remarks 


<div class="mw-translate-fuzzy">

## Altre osservazioni 

-   Non è necessario che i profili siano paralleli (vedere figura).
-   Per Loft, non è necessario che i profili siano separati (vedere figura sotto). Possono essere complanari, ma non dovrebbero intersecarsi.
-   Quando la proprietà \"Closed\" del Loft è \"true\", appare una giunzione a cuspide per tutte le spline che formano il Loft (vedere l\'immagine qui sotto). Per ora, non c\'è alcun modo affidabile per chiudere il Loft senza spigoli vivi.


</div>

    
  <img alt="Non è necessario che i profili siano paralleli." src=images/Loft_nonparallel.png  style="width:300px;">   <img alt="In Loft, i profili possono essere complanari. In questo esempio, due dei tre profili sono complanari." src=images/Loft_Coplanar.png  style="width:300px;">   <img alt="Un esempio di un Loft chiuso tra tre profili pentagonali bianchi. Notare la giunzione non levigata sul profilo più esterno. Questo è il primo profilo nel loft chiuso." src=images/Loft-closed.png  style="width:300px;">



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft Technical Details/it
