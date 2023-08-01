---
- TutorialInfo:/it
   Topic:Ambiente Navale
   Level: Base
   Time:
   Author:
   FCVersion:
   Files:
---

# FreeCAD-Ship s60 tutorial (II)/it





## Overview


<div class="mw-translate-fuzzy">

Prima di iniziare questo tutorial è bene eseguire il [primo tutorial](FreeCAD-Ship_s60_tutorial/it.md).


</div>


<div class="mw-translate-fuzzy">

Altre informazioni sono disponibili nella pagina [FreeCAD-Ship](Ship_Workbench/it.md)


</div>

## Introduzione

In questo tutorial lavoreremo con i pesi e i serbatoi al fine di calcolare la curva di GZ che è il più importante parametro di stabilità idrostatica. GZ è il momento statico generato quando la nave assume un angolo di rollio (angolo di inclinazione trasversale o di sbandamento). Naturalmente, quando il braccio di stabilità GZ è positivo la nave ha un momento positivo e cerca di recuperare la posizione eretta, ma quando il braccio di stabilità GZ assume valori negativi la nave non ha più stabilità e si trova in una situazione critica.

L\'Organizzazione Marittima Internazionale, IMO ha definito i seguenti criteri:

-   *GM* \>= 0.15 m. *GM* (altezza metacentrica) è la tangente iniziale della curva di *GZ*
-   Il massimo braccio di stabilità *GZ* deve registrarsi a un angolo di sbandamento superiore a 30°
-   Con un angolo di rollio di 30°, il braccio di stabilità *GZ* deve essere almeno di 0,20 m
-   L'area sotto la curva del braccio di stabilità (curva GZ) non deve essere inferiore a 0,09 metri-radianti fino a un angolo di rollio di 40°
-   L'area sotto la curva del braccio di stabilità (curva GZ) non deve essere inferiore a 0,055 metri-radianti fino a un angolo di sbandamento di 30°
-   L'area sotto la curva del braccio di stabilità (curva GZ) non deve essere inferiore a 0,03 metri-radianti fra gli angoli di sbandamento di 30° e 40° o fra 30° e l'angolo di allagamento, se tale angolo è minore di 40°


<div class="mw-translate-fuzzy">

In questo tutorial i pesi e i serbatoi della barca della serie 60 saranno distribuiti in modo irreale.


</div>

## Pesi della nave 

Per essere in grado di calcolare la curva di GZ è necessario conoscere il peso della nave e la posizione del centro di gravità per ogni angolo di sbandamento. Per questo i pesi possono essere suddivisi in due categorie:

-   Pesi fissi che si muovono congiuntamente e solidali alla nave.
-   Serbatoi contenenti del liquido che cambia la sua forma spostando il centro di gravità che deve essere ricalcolato per ogni angolo di rollio.


<div class="mw-translate-fuzzy">

FreeCAD-Ship offre due strumenti diversi per generare ognuna delle istanze.


</div>

![Weights definition tool icon.](images/FreeCAD-Ship-WeightIco.png )


<center>

Icona dello strumento per la definizione dei pesi.


</center>


<div class="mw-translate-fuzzy">

Lo strumento di definizione dei pesi può essere utilizzato per definire i pesi della prima categoria. Quando si avvia lo strumento per la prima volta (con una istanza di nave selezionata), FreeCAD-Ship inizializza i pesi della nave con Lightweight, un peso leggero, pari al dislocamento, che viene inserito nel centro di gravità della geometria della nave per la coordinata X, e all\'altezza della immersione di progetto. Di solito si hanno almeno 2 pesi rilevanti:

-   Struttura.
-   Motore (o più di uno).


</div>


<div class="mw-translate-fuzzy">

Fare doppio click sulla cella corrispondente per modificare il suo valore e impostare questi pesi:

-   Structure, 15000 kg, (-0.1, 0, 1.25) m
-   Starboard engine, 5000 kg, (-6.5, -0.65, 0.5) m
-   Port side engine, 5000 kg, (-6.5, 0.65, 0.5) m
-   Emergency engine, 2500 kg, (0.2, 0, 2.5) m


</div>

![Weights definition 3D preview.](images/FreeCAD-Ship-S60WeightsPreview.png )


<center>

Anteprima 3D della vista dei pesi.


</center>


<div class="mw-translate-fuzzy">

Le posizioni dei pesi sono visualizzate nella vista 3D. Le annotazioni vengono rimosse quando lo strumento viene chiuso. Quando si preme **OK** i pesi vengono archiviati nella istanza Ship.


</div>


<div class="mw-translate-fuzzy">

## Serbatoi

I serbatoi devono essere costruiti su di una geometria solida, come per il modello della nave, quindi cominciare creando due geometrie solide a prua, una per lato della nave, che poi saranno convertite in istanze Tank (serbatoio). Normalmente le navi hanno un sacco di serbatoi, per carburante, acqua dolce, acqua salata, carico, ecc..


</div>

### Creare la geometria 

Per creare i serbatoi caricare il [Modulo Part](Part_Workbench/it.md) e creare un solido parallelepipedo (box).


<div class="mw-translate-fuzzy">

È necessario modificare il parallelepipedo, selezionare quindi il box nell\'albero **Attributi e etichette** e nella scheda *Dati* aprire la voce *Placement* e impostare la *Position* con *x* a 1.5 e *z* a -1. Modificare anche la lunghezza del box impostando il suo valore a 5.0 (notare che le unità possono essere in mm, ma non preoccuparsi di questo).


</div>

La geometria del serbatoio sarà costituita dalla parte comune del box e della geometria della nave, perciò nascondere l\'istanza **Ship** e mostrare la geometria originale **s60_IowaUniversity**. Selezionare il **box** e **s60_IowaUniversity** e poi usare l\'operazione booleana di intersezione per generare la geometria del serbatoio di dritta.

![Generated tank geometry.](images/FreeCAD-Ship-S60TankGeometry.png )


<center>

Geometria del serbatoio generato.


</center>

Per costruire il serbatoio di babordo basta selezionare la geometria di dritta e eseguire lo strumento specchio, selezionando XZ come piano di riflessione.

Per convertire la geometria dei serbatoi in una forma solida usuale, and recover our **s60_IowaUniversity** geometry, caricare il [modulo Draft](Draft_Workbench/it.md), poi selezionare la geometria del serbatoio di dritta e eseguire Upgrade. Ripetere l\'operazione con la geometria del serbatoio di babordo. Si possono rinominare le geometrie con:

-   StarboardTankGeom
-   PortTankGeom

Ora si può anche eliminare il box, non serve più.


<div class="mw-translate-fuzzy">

### Creare le istanze serbatoio 

Riattivare il [modulo FreeCAD-Ship](FreeCADShip_Workbench/it.md) per rendere disponibile lo strumento generatore delle istanze serbatoio.


</div>

![Tank instance generation tool icon.](images/FreeCAD-Ship-TankIco.png )


<center>

Icona dello strumento generatore delle istanze serbatoio.


</center>


<div class="mw-translate-fuzzy">

Selezionare la geometria **StarboardTankGeom** e eseguire lo strumento generatore delle istanze serbatoio che apre la finestra per fornire alcuni dati. Impostare il livello di riempimento al 40%, e la densità a 925 kg/m³ (circa il peso del carburante). Quando si clicca su **OK** viene generata una nuova istanza denominata **Tank**. Si può rinominarla **StarboardTank** e nascondere **StarboardTankGeom**.


</div>

Ripetere lo stesso processo per generare **PortTank**.

![View of generated weights.](images/FreeCAD-Ship-S60WeightsTanksPreview.png )


<center>

Vista dei pesi generati.


</center>

La figura precedente mostra la barca di cui si vuole calcolare la curva di GZ.


<div class="mw-translate-fuzzy">

### Calcolare la curva di GZ 

FreeCAD-Ship fornisce uno strumento per calcolare facilmente la curva di *GZ*.


</div>


<div class="mw-translate-fuzzy">

![GZ curve computation tool icon.](images/FreeCAD-Ship-HydrostaticsIco.png )


<center>

Icona dello strumento di calcolo della curva di GZ.


</center>


</div>


<div class="mw-translate-fuzzy">

Selezionare l\'istanza **Ship** e eseguire lo strumento. La prima cosa che si vedere nel dialogo che viene aperto è una lista di tutte le istanze di serbatoi trovate nel documento attivo. Per utilizzarli entrambi cliccare sopra i serbatoi che sono evidenziati con uno sfondo diverso.


</div>

Per conoscere il dislocamento della nave e l\'immersione risultante, premere **Update displacement and draft** e attendere un po\' per avere i risultati dei calcoli. Si ottengono i seguenti dati:

-   Displacement = 37505.5 kg
-   Draft = 0.818664 m


<div class="mw-translate-fuzzy">

La nave quindi si trova in una situazione di poco carico, dove l\'immersione è inferiore a quella di progetto. Normalmente una bassa immersione implica una scarsa stabilità della nave. Dato che l\'immersione dipende dalle condizioni di carico, se si intende davvero far operare la nave in queste condizioni, si può considerare di implementare delle cisterne di zavorra per aumentare l\'immersione.


</div>

Inoltre, premendo sul pulsante **Auto** lo strumento calcola automaticamente l\'assetto della nave, operazione che può richiedere circa un minuto. In questo caso la nave avrebbe un angolo di assetto di 0,95° (positivi di poppa), ma in questo esempio si lavora senza angolo di assetto (con 0°).

Lo strumento richiede anche che siano considerati gli angoli di rollio. Per conoscere il comportamento della nave con qualsiasi angolo impostare i seguenti valori:

-   0 degrees starting roll angle.
-   180 degrees ending roll angle.
-   46 points. Oppure un punto ogni due gradi. Il calcolo di GZ può richiedere lunghi tempi di elaborazione, a seconda della complessità della geometria e del numero di punti richiesti, quindi impostare con attenzione questo ultimo valore.


<div class="mw-translate-fuzzy">

Quando si preme **OK** lo strumento avvia l\'elaborazione. Se si esegue FreeCAD da terminale è possibile vedere l\'avanzamento. In pochi secondi si ottiene la curva di GZ.


</div>

Questo strumento utilizza [pyxplot](http://www.pyxplot.org.uk/) e anche [ghostscript](http://www.ghostscript.com/). Si può vedere dove è stato posizionato il file di output **gz.dat** visualizzando il report (Visualizza / Vista / Visualizza report) e aprirlo con un software che disponga di un foglio di calcolo (ad esempio [LibreOffice](http://www.libreoffice.org)). Congiuntamente al file dei dati vengono anche creati alcuni file ausiliari:

-   **gz.dat**: Dati della curva GZ.
-   **gz.pyxplot**: Formato per pyxplot che permette di tracciare la curva.
-   **gz.eps**: Immagine in versione EPS.
-   **gz.png**: Immagine in versione PNG.

Quando lo strumento viene nuovamente eseguito i file vengono sovrascritti, quindi copiarli in un altro posto se si desidera preservarli.

### Risultati

<img alt="Resultant GZ curve." src=images/FreeCAD-Ship-s60GZ.png  style="width:800px;">


<center>

Curva di GZ.


</center>


<div class="mw-translate-fuzzy">

Il valore massimo *GZ* è a 45°, ben al di sopra dei 30° richiesti dalla norma. Con un rollio di 30° *GZ* vale 0,25 m e il minimo richiesto è di 0,2 metri. L\'area calcolata sotto la curva di *GZ* fino a 30° di sbandamento è di 0.065 m·rad, e fino a 40° è di 0.092 m·rad, entrambi i valori sono superiori a quelli richiesti. Tuttavia, l\'area sotto la curva di *GZ* tra 30° e 40° di sbandamento è di 0.027 m·rad, cioè al di sotto del valore minimo richiesto dalle norme dell\'IMO.


</div>


<div class="mw-translate-fuzzy">

In queste condizioni di carico, per risolvere il problema, sarebbe necessario zavorrare la nave.

Inoltre, nel grafico si può vedere che, in queste pessime condizioni, la barca ha un *GZ* positivo per valori fino a un angolo di rollio di 95°, ma questo non è sufficiente per raggiungere i requisiti IMO, e questo dà un\'idea di quanto sono severi i criteri di stabilità delle imbarcazioni.


</div>


<div class="mw-translate-fuzzy">

Naturalmente questo esempio non è realistico (anche perché i serbatoi del carburante non possono essere collocati nella struttura del doppio fondo, o senza avere un doppio scafo), ma è un buon esempio per imparare ad utilizzare [Ship](Ship_Workbench/it.md).


</div>



---
⏵ [documentation index](../README.md) > [Ship](Category_Ship.md) > FreeCAD-Ship s60 tutorial (II)/it
