


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}


<div class="mw-translate-fuzzy">

Questo è il piano del progetto **Disegno di Parti** come parte del [Piano di sviluppo](Development_roadmap/it.md) (Development roadmap).


</div>


<div class="mw-translate-fuzzy">

## Finalità e principi 

Questo è un progetto di sviluppo del software con lo scopo di implementare le funzioni di disegno di oggetti di tipo Parte. Si tratta di implementare alcune **funzionalità di base** nei moduli CAD **Part, PartDesign e Assembly** di FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Le fasi dello sviluppo sono pianificate qui e sono monitorate nel sistema di gestione [Issue Tracker](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php) per tenere un registro storico ben strutturato delle modifiche.


</div>

## Risultati

Scopo del progetto è quello di consentire a FreeCAD di produrre un disegno come quello che si vede a destra.

<img alt="" src=images/Gripper.jpg  style="width:300px;">


<div class="mw-translate-fuzzy">

Questo si ottiene utilizzando **Sketcher** (Schizzo) e **PartDesign** (Progettazione di parti) per disegnare le parti speciali e utilizzando **Part** (Parte) per caricare le parti standard come STEP (ad esempio, il cuscinetto lineare). Poi **Assembly** (Assemblaggio) unisce il tutto con i vincoli.


</div>


<div class="mw-translate-fuzzy">

La **Metodologia Feature editing** (metodologia di modifica delle operazioni) è una realizzazione importante. Essa offre all\'utente un approccio intuitivo per istanziare e per modificare le funzioni. Questo è importante per tutti gli altri moduli e ambienti che stanno per arrivare, per compilarli con una interfaccia utente coerente!


</div>

<img alt="" src=images/TaskPanel.jpg  style="width:400px;">

![](images/CAD_Modeling.gif‎ )


<div class="mw-translate-fuzzy">

### Sketcher (Schizzo) 

Un disegnatore parametrico con un solutore di vincoli geometrici. Per maggiori dettagli vedere il **[Progetto di Schizzo](Sketcher_project/it.md)**.


</div>

### PartDesign (Disegno di Parte) 


<div class="mw-translate-fuzzy">

#### Body feature (Funzione Corpo) 

Dato che un modello basato su uno storico (serie di operazioni in ordine cronologico) può contenere numerosi passaggi per arrivare alla forma finale è necessario un gruppo di riferimento. Questo è il **corpo**, esso contiene il risultato finale della modellazione e funziona come gruppo per tutte le operazioni dell\'albero dello storico.


</div>


<div class="mw-translate-fuzzy">

#### Pad feature (operazione Estensione) 

Una operazione Pad estrude uno schizzo (o qualsiasi Part2DObject) nella sua direzione normale. Garantisce sempre la creazione di un solido, o dà errore.

#### Pocket feature (operazione Scavo) 

Crea uno scavo con la forma di uno schizzo in un solido di base, con la profondità definita o \"Fino all\'ultimo/Fino al primo\". Garantisce anche l\'ottenimento di un solido.


</div>

#### Bore feature (Operazione foratura) 

Ecco una ottima definizione dei parametri dei fori dalla specifica di NaroCad:

  ----------------------------------------------------------------------- ------------------------------------------------------------------------- -----------------------------------------------------------------------
  <img alt="" src=images/Counterbore_settings.png  style="width:300px;">   <img alt="" src=images/Counterbore_settings2.png  style="width:300px;">   <img alt="" src=images/Countersink_settings.png  style="width:300px;">
  ----------------------------------------------------------------------- ------------------------------------------------------------------------- -----------------------------------------------------------------------

  : **NaroCAD Bore definitions**

#### Pattern (Matrice, Modello) 

Replica una delle caratteristiche (operazioni) di cui sopra

##### **RectangularPattern** (Matrice rettangolare) 

Replica una delle caratteristiche di cui sopra lungo un modello x, y

##### **CircularPattern** (Matrice circolare) 

Replica una delle caratteristiche di cui sopra, lungo una matrice in coordinate polari

##### **ScriptedPattern** (Matrice script) 

Replica una delle caratteristiche di cui sopra in base ad una regola generale fornita in forma di script.

## Riflessioni

### Cosa fanno gli altri 

-   [Esempi di SolidWorks](http://www.youtube.com/watch?v=cVXQmDStHus)

### Implementare dei modelli, matrici 

La classe delle operazioni con matrici (modelli) può essere implementata come un modello tabellare e servire come classe base per le operazioni di matrici rettangolari, circolari e di script. Queste classi derivate dovranno solo essere compilate nella tabella delle ripetizioni della classe base.

Ogni riga della tabella delle ripetizioni della classe di pattern (matrice, modello) di base deve contenere almeno una matrice di trasformazione per applicare il posizionamento della operazione originale da replicare. Inoltre potremmo avere regole di trasformazione opzionali, come ad esempio la manipolazione di un certo valore del parametro della operazione da replicare (ad esempio per creare un modello di fori con raggio variabile).

## Organizzazione

### Gerarchia della modellazione degli oggetti 

Questo grafico di [UML](http://http://it.wikipedia.org/wiki/Unified_Modeling_Language) (linguaggio di modellazione unificato) mostra la gerarchia degli oggetti prevista e le sue relazioni. La classe base astratta è di colore giallo, le implementazioni in sono blu e in grigio quelle previste.

<img alt="" src=images/PartDesign_ModlingObjectsHirachy.png  style="width:1000px;">

## Tutorial


<div class="mw-translate-fuzzy">

[PartDesign Bearingholder Tutorial I](PartDesign_Bearingholder_Tutorial_I/it.md)


</div>


<div class="mw-translate-fuzzy">

[PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II/it.md)


</div>

## Azioni Successive 

L\'ordine di successione delle azioni per PartDesign è definito nella [Roadmap](http://www.freecadweb.org/tracker/roadmap_page.php).


<div class="mw-translate-fuzzy">

### Body (Corpo) 

Data la natura parametrica/associativa di PartDesign abbiamo bisogno di un \"Corpo\" di riferimento (il corpo principale, componente di base) che raggruppi e organizzi uno storico della costruzione. Il corpo stesso contiene il risultato finale come una forma e contiene raggruppate come figli le operazioni di PartDesign. Definisce inoltre l\'intestazione dello storico di modellazione. E\' anche relazionato al [Progetto di Assemblaggio](Assembly_project/it.md) che è il blocco di costruzione per i prodotti e i componenti.


</div>


<div class="mw-translate-fuzzy">

### Caratteristiche addizionali 

Le operazioni Pad e Pocket (Estensione e Scavo) sono la prima parte (i primi attrezzi) di PartDesign. C\'è ancora molto lavoro da fare soprattutto con la visualizzazione e il controllo visivo dei manipolatori. Poi sono necessarie ulteriori operazioni.


</div>

#### Matrici, Modelli 

Sono le operazioni di Matrice che applicano ripetutamente una operazione Pad o Pocket secondo un modello circolare o rettangolare. Un [esempio in IronCAD](http://www.ironcad.com/index.php/support/learning-center).


<div class="mw-translate-fuzzy">

#### Foratura

Fori con tutti i classici parametri per la filettatura e la svasatura \....


</div>

#### Sweep (Trascinamento) 

Trascina uno schizzo lungo una curva e crea un solido modellato secondo la stessa curva.

#### Rivoluzione

Ruota uno schizzo lungo uno dei suoi assi e di un certo angolo.

**Done \[jrheinlaender et al.\]**


<div class="mw-translate-fuzzy">

## Elenco di cose da fare 

**1. Raccordare/Smussare Parte**

1.a Applicare operazioni di raccordo/smusso a tipi diversi di selezione (faccia/coppia-di-facce/corpo completo)

**2. Strumento Espansione (Pad)**

2.a Creare la modalità \'fino al prossimo\' **FATTO** \[**mrlukeparry**\]

2.b Creare la modalità \'fino alla superficie/faccia\' \[**mrlukeparry**\]

2.c Creare proprietà di disegno per Pad **FATTO** \[mrlukeparry\]

2.d Quando su una faccia viene selezionato Pad, creare automaticamente uno schizzo?

2e. Creare la modalità \'piano medio\' **FATTO** \[**jrheinlaender**\]

**3. Strumento Scavo**

3.a Creare le modalità \'fino al primo\', \'fino all\'ultimo\', \'passante\', \'fino alla superficie/faccia\' **FATTO** \[**jrheinlaender**\]

3.b Quando su una faccia viene selezionato Pocket, creare automaticamente uno schizzo?

**4. Rivoluzionare Parte**

4.a Consentire che un generico segmento di linea/asse sia utilizzato come referimento

4b. Creare la modalità \'piano medio\' **FATTO** \[**jrheinlaender**\]

**5. Operazione Foratura**

**6. Operazione Matrice** **DONE** \[**jrheinlaender**\]

**7. Operazione Sweep**

**8. Operazione Corpo**

**9. Geometria di riferimento**

9.a Piano

**10. Strumento Simmetria** **DONE** \[**jrheinlaender**\]

**11. Strumento Copia caratteristiche**


</div>



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
