---
- TutorialInfo:/it
   Topic:Ambiente Navale
   Level:Base
   Time:
   Author:
   FCVersion:
   Files:
---

# FreeCAD-Ship s60 tutorial/it





## Introduction


<div class="mw-translate-fuzzy">

In questo tutorial lavoreremo con una barca della Serie 60, dell\'Università di Iowa. L\'esercitazione ha lo scopo di mostrare come lavorare con una imbarcazione monoscafo simmetrica, ma le imbarcazioni multiscafo o non simmetriche possono essere create con la stessa procedura.


</div>


<div class="mw-translate-fuzzy">

Potete trovare altre informazioni nella pagina [FreeCAD-Ship](Ship_Workbench/it.md)


</div>



## Caricare la geometria 


<div class="mw-translate-fuzzy">

### Introduzione

FreeCAD-Ship lavora su delle **entità Ship** che devono essere create preventivamente sulla base delle geometrie fornite. La geometria deve essere un solido, o un insieme di solidi, e deve rispettare i seguenti criteri:

-   Deve essere fornita tutta la geometria dello scafo (comprese le barche simmetriche).
-   La geometria di dritta, di tribordo, deve essere posizionata nel dominio *Y negativa*.
-   L\'origine (0,0,0) si trova nel punto di intersezione della **sezione maestra** (Punto medio tra la perpendicolare di poppa e quella di prua) e la **linea di base**.


</div>

![Schematic view of sign criteria](images/FreeCAD-Ship-SignCriteria.jpg )


<center>

Descrizione dei requisiti della forma base


</center>


<div class="mw-translate-fuzzy">

### Caricare una geometria della Serie 60 

Per aiutare i nuovi utenti, Ship include una serie di esempi di geometrie, dove si può scegliere tra i seguenti elementi:

-   Serie 60 della Iowa University
-   Canonica imbarcazione Wigley
-   Catamarano Serie 60
-   Catamarano Wigley


</div>


<div class="mw-translate-fuzzy">

![Example ship geometries loader icon.](images/FreeCAD-Ship-LoadIco.png )


<center>

Icona dello strumento per caricare le geometrie di esempio fornite con Ship


</center>


</div>

Eseguendo lo strumento (Caricare una geometria modello di nave) si apre una finestra di dialogo. Selezionare **Series 60 da Iowa Università** e premere il pulsante OK. Lo strumento carica un nuovo documento con la geometria **s60_IowaUniversity**


<div class="mw-translate-fuzzy">


**<center>'''Attenzione, prima di modificare qualsiasi cosa!'''</center>
<center>Ora si sta lavorando con il file originale del modello.</center>
<center>Per preservare l'esempio originale, senza modificarlo, '''è necessario salvarlo come nuovo file, prima di apportare delle modifiche'''</center>**


</div>

## Creare un\'istanza barca 

Per creare una **Ship instance** (una istanza della barca) selezionare la geometria s60 ed eseguire lo strumento **ship creation** (disegna/crea una nuova barca).


<div class="mw-translate-fuzzy">

![Ship creation tool.](images/FreeCAD-Ship-Ico.png )


<center>

Icona dello strumento **ship creation**


</center>


</div>


<div class="mw-translate-fuzzy">

Appare il dialogo per la Creazione della barca e nella vista 3D viene mostrata la sua sagoma con alcune annotazioni. Non preoccupatevi delle annotazioni perché vengono rimosse quando si chiude lo strumento di creazione della nave.


</div>


<div class="mw-translate-fuzzy">

Devono essere introdotti i dati principali della nave (FreeCAD-Ship utilizza un sistema di introduzione dei dati progressivo, in questo modo le operazioni di base possono essere eseguite utilizzando i dati di base della nave, e le ulteriori informazioni sono necessarie solo quando le operazioni diventano più complesse).


</div>

### Dati della nave 

Le dimensioni principali che devono essere introdotte qui:

-   *Length*: lunghezza tra le perpendicolari, 25,5 m per questo scafo.
-   *Beam*: baglio, larghezza massima della barca, 3,389 m per questo scafo.
-   *Draft*: immersione, 1.0 m per questo scafo.

![Front view annotations](images/FreeCAD-Ship-S60ShipCreationFront.png )


<center>

Annotazioni di lunghezza nella vista frontale.


</center>

La distanza tra le perpendicolari dipende dall\'immersione, quindi se non si conosce la lunghezza tra le perpendicolari è possibile impostare l\'immersione e regolare la lunghezza in modo da ottenere l\'intersezione del dritto o ruota di prua (linea superiore della prua) con la [linea di galleggiamento](http://it.wikipedia.org/wiki/Linea_di_galleggiamento).

![Side view annotations](images/FreeCAD-Ship-S60ShipCreationSide.png )


<center>

Annotazioni sulla vista laterale.


</center>

Lo stesso procedimento è valido per il baglio. Si noti che viene richiesto il valore del [baglio maestro](http://it.wikipedia.org/wiki/Baglio_%28nautica%29) (larghezza massima) , ma l\'annotazione si riferisce solo alla metà di dritta della barca.


<div class="mw-translate-fuzzy">

Quando si preme il pulsante **OK**, il programma crea la nuova istanza barca, questa nuova istanza è denominata **Ship** nell\'albero *Etichette e Attributi*. Ora la geometria originale non è più necessaria, quindi è possibile nasconderla.


</div>

![Ship instance icon](images/FreeCAD-Ship-ShipInstance.png )


<center>

Icona dello strumento istanza.


</center>


<div class="mw-translate-fuzzy">

Da questo punto in poi, è necessario che **Ship** sia sempre selezionata prima di eseguire qualsiasi strumento di FreeCAD-Ship.


</div>


<div class="mw-translate-fuzzy">

## Disegno delle linee 

Ship fornisce uno strumento che rende semplice ottenere un Piano delle linee dal disegno delle linee della nave


</div>


<div class="mw-translate-fuzzy">

![Outline draw tool.](images/FreeCAD-Ship-OutlineDrawIco.png )


<center>

Icona dello strumento per disegnare il contorno


</center>


</div>

Il disegno delle linee è un insieme di sezione sui 3 assi, che alla fine mostreranno la geometria dello scafo in un Piano delle linee. Dobbiamo fornire le linee per le 3 seguenti viste:

-   Body Plan (utilizzando le sezioni trasversali)
-   Sheer Plan (usando le sezioni longitudinali)
-   Half-Breadth Plan (usando le sezioni delle linee d\'acqua)


<div class="mw-translate-fuzzy">

### Sezioni trasversali 

Di solito devono essere eseguite 21 sezioni trasversali equidistanti tra le perpendicolari. Per eseguire questa operazione FreeCAD-Ship fornisce uno strumento automatico, è sufficiente selezionare **Transversal** come tipo di sezione, andare nel dialogo **Auto create** e impostare **21** nel campo delle sezioni, poi premere **Create sections**.


</div>

![Outline draw transversal sections preview.](images/S60OutlineTransversal.png )


<center>

Anteprima della vista delle sezioni trasversali


</center>


<div class="mw-translate-fuzzy">

Viene compilata la tabella delle sezioni e si crea un nuovo oggetto chiamato OutlineDraw che permette di visualizzare l\'anteprima delle sezioni adottate. Di solito si producono delle sezioni più ravvicinate nelle zone prossime alla poppa e alla prua, dove la curvatura più pronunciata; per fare questo basta andare alla fine della tabella e fare **doppio clic** nella riga vuota, aggiungere un nuovo valore e premere Invio per confermare. Aggiungere manualmente le seguenti due sezioni:


</div>


<div class="mw-translate-fuzzy">

-   X~22~ = -12.1125 m
-   X~23~ = 12.1125 m


</div>

Secondo la complessità della geometria dello scafo, l\'anteprima delle sezioni può richiedere del tempo per essere elaborata.


<div class="mw-translate-fuzzy">

### Sezioni longitudinali 

Devono essere aggiunte due sezioni longitudinali, quindi selezionare **Longitudinal** come tipo di sezione, andare nel dialogo **Auto create** e impostare **2** nel campo delle sezioni, poi premere **Create sections**. Viene compilata la tabella delle sezioni e viene aggiornata l\'anteprima.


</div>


<div class="mw-translate-fuzzy">

### Linee d\'acqua 

Di solito servono 6 linee d\'acqua tra la linea di base e la linea di galleggiamento, quindi selezionare **Waterlines** come tipo di sezione, andare nel dialogo **Auto create** e impostare **5** nel campo delle sezioni (La linea d\'acqua Z = 0 m non è inclusa automaticamente, se è necessaria può essere aggiunta manualmente in un secondo momento), quindi premere **Create sections**. Viene compilata la tabella delle sezioni e viene aggiornata l\'anteprima.


</div>

Devono essere aggiunte diverse linee d\'acqua supplementari:

-   Z~6~ = 1.2 m
-   Z~7~ = 1.4 m
-   Z~8~ = 1.6 m
-   Z~9~ = 1.8 m
-   Z~10~ = 2.0 m


<div class="mw-translate-fuzzy">

### Tracciare il piano di costruzione 

Selezionare una scala **1:100** e premere **Accept** per fare in modo che lo strumento generi le sezioni 3D in un nuovo oggetto.


</div>

![Resultant sections.](images/FreeCAD-Ship-S60Outline3DSections.png )


<center>

Sezioni risultanti.


</center>


<div class="mw-translate-fuzzy">

Per disegnare queste sezioni si può utilizzare il modulo [Drawing](Drawing_Workbench/it.md):


</div>

![Outline draw plot.](images/FreeCAD-Ship-S60OutlinePlot.png )


<center>

Proiezione dei piani.


</center>


<div class="mw-translate-fuzzy">

## Curva delle aree trasversali 

Un parametro idrodinamico tipico della progettazione navale è la curva delle aree trasversali che fornisce alcuni indicatori sul comportamento della carena (resistenza all\'avanzamento, comportamento in mare, \...). FreeCAD-Ship offre uno strumento semplice per tracciare la curva delle aree trasversali.


</div>

![Transversal areas curve tool icon.](images/FreeCAD-Ship-AreaCurveIco.png )


<center>

Icona dello strumento per tracciare le curve delle aree trasversali.


</center>


<div class="mw-translate-fuzzy">

Quando si esegue questo strumento appare la finestra di dialogo delle azioni e nella vista 3D viene mostrata una anteprima della superficie del mare (l\'anteprima della superficie del mare viene rimossa quando lo strumento viene chiuso, quindi non preoccupatevene). Nella finestra di dialogo sono presenti dei dati in ingresso e dei dati in uscita.


</div>


<div class="mw-translate-fuzzy">

### Dati in ingresso 

Devono essere forniti i valori di Draft e di Trim (Immersione e Assetto) (l\'angolo di rotazione dello scafo attorno a *y* è positivo se l\'immersione di poppa può aumentare). Si possono produrre le curve di diverse aree, a seconda delle condizioni di carico della nave, però si devono eseguire due grafici tipici:

-   Curva dell\'area trasversale di progetto: senza angolo di assetto e utilizzando l\'immersione di progetto, 1,0 m in questo caso.

-   Curva dell\'area trasversale massima: senza angolo di assetto e con immersione massima consentita, 2,0 m in questo caso.


</div>


<div class="mw-translate-fuzzy">

### Dati in uscita 

Alcuni dati rilevanti vengono visualizzati in tempo reale:

-   **L**: Lunghezza fra le perpendicolari, valore impostato al momento della creazione dell\'istanza nave.
-   **B**: Baglio, larghezza impostata al momento della creazione della nave.
-   **T**: Immersione attuale della sezione maestra.
-   **Trim**: Angolo di assetto.
-   **T~AP~**: Immersione nella perpendicolare avanti, prora.
-   **T~FP~**: Immersione nella perpendicolare addietro, poppa .
-   **Displacement**: Dislocamento della nave (considerando acqua salata, quindi dividere per 1,025 per conoscere volume spostato).
-   **XCB**: Coordinata X del Centro di carena (relativa alla sezione maestra).


</div>


<div class="mw-translate-fuzzy">

Quando si preme il pulsante **OK** viene prodotto il grafico (secondo la complessità della geometria può richiedere del tempo, si può vedere l\'avanzamento dell\'elaborazione nel terminale e si può fermarla premendo **Ctrl + C**). Quando l\'attività è terminata FreeCAD genera un grafico (vedere la documentazione del modulo [Plot](Plot_Workbench/it.md)) e un foglio di calcolo (vedere la documentazione del modulo [Spreadsheet](Spreadsheet_Workbench/it.md)).


</div>

![Design draft transversal areas curve. ](images/FreeCAD-Ship-s60Areas-it.png )


<center>

Curva dell\'area trasversale dell\'immersione di progetto. 


</center>

In modo analogo è possibile eseguire la curva dell\'area trasversale di massima immersione per evidenziare le differenze (per esempio l\'area della curva che passa per le perpendicolari di poppa o di prua).

## Idrostatica

Il calcolo idrostatico è una fase chiave nella progettazione navale, esso fornisce i principali parametri di stabilità dello scafo. Le società di classificazione richiedono tali informazioni per certificare le navi, che, insieme alle informazioni sulle condizioni di carico (pesi e posizione di gravità) forniscono i dati essenziali sulla stabilità della nave. FreeCAD-Ship offre uno strumento per ottenere le principali curve idrostatiche (le curve GZ sono elaborate con un altro strumento).

![Hydrostatics tool icon.](images/FreeCAD-Ship-HydrostaticsIco.png‎ )


<center>

Icona dello strumento Idrostatica.


</center>

Quando questo strumento viene eseguito appare la finestra di dialogo delle azioni per inserire il valore dell\'immersione e l\'angolo di assetto. Solitamente le curve idrostatiche sono presentate in un intervallo di immersione per ogni angolo di assetto. In questo tutorial sarà considerato solo l\'angolo 0 º con un ampio intervallo di immersione, per ogni condizione di carico possibile. Dato che non si conoscono le condizioni di carico che si possono verificare, si considerano diverse possibilità di immersione (Di solito, al fine di ottenere il maggior numero di risoluzioni possibili, gli architetti navali adottano l\'intervallo plausibile per le immersioni).

Quindi impostare i seguenti valori:

-   **Trim** = 0º
-   **Minimum Draft** = 0.1 m
-   **Maximum Draft** = 2.0 m
-   **Number of points** = 39. Un gran numero di punti o geometrie molto complesse implicano lunghi tempi di calcolo, in questo caso può essere necessario circa 1 minuto.


<div class="mw-translate-fuzzy">

Quando si preme il pulsante **OK** viene prodotto un grafico (vedere la documentazione del modulo [Plot](Plot_Workbench/it.md)) e un foglio di calcolo (vedere la documentazione del modulo [Spreadsheet](Spreadsheet_Workbench/it.md)).


</div>

![Hydrostatics curves. ](images/FreeCAD-Ship-HydrostaticsCurves.jpg )


<center>

Curve Idrostatiche. 


</center>




<div class="mw-translate-fuzzy">

## Approfondire le conoscenze su FreeCAD-Ship 

Ora si è pronti per continuare la lettura su [Ship](Ship_Workbench/it.md), [qui](FreeCAD-Ship_s60_tutorial_(II)/it.md) c\'è il secondo capitolo sulle barche della Serie 60, dell\'Università di Iowa.


</div>

The [FreeCAD Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md) is the second chapter of Series 60 from Iowa university ship.



---
⏵ [documentation index](../README.md) > [Ship](Category_Ship.md) > FreeCAD-Ship s60 tutorial/it
