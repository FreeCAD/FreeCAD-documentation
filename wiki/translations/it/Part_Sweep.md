# Part Sweep/it
---
- GuiCommand:/it   Name:Part Sweep   Name/it:Sweep   MenuLocation:Parte → Sweep...   |Workbenches:[SeeAlso:[[Part_Loft/it|Loft](Part_Workbench/it___Parte]].md)---


</div>

## Descrizione

Lo strumento <img alt="" src=images/Part_Sweep.svg  style="width:24px;"> **Part Sweep** di FreeCAD serve per creare una faccia, un guscio o una forma solida da uno o più profili (la sezione trasversale), proiettati lungo un percorso.

Lo strumento Parte Sweep è simile a <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Part Loft](Part_Loft/it.md), ma con l\'aggiunta di un percorso per definire la proiezione tra i profili.

<img alt="Un solido sweep generato da un profilo (A) proiettato lungo un percorso (B)." src=images/Part_Sweep_simple.png  style="width:500px;">

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Part_Sweep.svg" width=16px> '''Sweep'''**. Questo apre la finestra per impostare i parametri di Sweep nel pannello [Azioni](Task_panel/it.md).
2.  Nella colonna di sinistra *Profili disponibili* (precedentemente nella Versione 0.16 *Vertex/Edge/Wire/Face*), fare clic sull\'elemento da utilizzare come profilo di sweep, quindi fare clic sulla freccia destra per posizionarlo nella colonna di destra *Profili selezionati* (precedentemente nella Versione 0.16 *Sweep*). Ripetere se si desidera usare più di un profilo. Utilizzare le frecce su e giù per riordinare i profili selezionati.
3.  Cliccare sul pulsante **Percorso Sweep**, quindi scegliere una delle due modalità di selezione:
    -   *Seleziona singoli segmenti*: si può selezionare uno o più bordi contigui nella vista 3D (premere **CTRL** per selezioni multiple) e poi cliccare su **Done**. Lo sweep viene generato solo lungo i bordi selezionati.
    -   *Seleziona un percorso completo*: si deve passare alla scheda Modello, selezionare nell\'albero l\'oggetto 2D da utilizzare come percorso, tornare al pannello Attività e fare clic su **Done**. Lo sweep viene generato lungo tutti i bordi contigui trovati nell\'oggetto 2D.
4.  Definire le opzioni [Solido](#Solido.md) e [Frenet](#Frenet.md).
5.  Cliccare **OK**.


</div>

### Accepted geometry 


<div class="mw-translate-fuzzy">

### Geometrie accettate 

I profili possono essere un punto (vertice), una linea (bordo), un wire o una faccia. Bordi e wire possono essere di tipo aperto o chiuso. Ci sono varie [limitazioni e complicazioni dei profili](Part_Sweep/it#Limitazioni_e_complicazioni_dei_profili.md), descritte in seguito, tuttavia i profili possono provenire da primitive di Parte, da funzioni di Draft e da Schizzi.


</div>


<div class="mw-translate-fuzzy">

Il percorso può essere costituito da una linea (bordo) o una serie di linee collegate, un wire o da alcune primitive di Parte, da funzioni di Draft e da Schizzi. Il percorso viene spesso selezionato direttamente nella finestra del modello principale, ma può anche essere selezionato dalla Vista ad albero, nella scheda Modello della Vista Combinata. Il percorso può essere una forma unica appropriata oppure un sotto-componente appropriato di una forma più complessa (ad esempio, come percorso può essere selezionato un bordo di un cubo di Parte). Il percorso può essere aperto o chiuso e quindi si può creare un Sweep aperto o chiuso. Un percorso chiuso come un cerchio Parte produce un Sweep chiuso. Ad esempio, lo Sweep di un cerchio piccolo lungo il percorso di un cerchio più grande crea un toro.


</div>

## Properties

### Solid


<div class="mw-translate-fuzzy">

## Proprietà

### Solido

Se \"Solid\" è impostato \"true\" FreeCAD crea un solido se i profili sono delle geometrie chiuse, se è impostato \"false\" crea una faccia o, un guscio se ci sono più facce, sia per profili aperti che chiusi.


</div>

### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">


<div class="mw-translate-fuzzy">

### Frenet 

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;"> La proprietà \"Frenet\" controlla come cambia l\'orientamento del profilo lungo il percorso di sweep. Se \"Frenet\" è \"false\", l\'orientamento del profilo rimane sempre lo stesso per tutti i punti. La forma risultante è quella con la minima torsione possibile. Quando un profilo viene trascinato lungo un\'elica, questo causa una lenta rotazione del profilo mentre segue dell\'elica. Impostando \"Frenet\" su true si previene questa rotazione. Se \"Frenet\" è \"true\", lungo un percorso elicoidale l\'orientamento del profilo sarà coerente all\'orientamento locale del percorso.


</div>

Se \"Frenet\" è \"true\" l\'orientamento del profilo è calcolato basandosi sulla curvatura e tangenza dei vettori locali del percorso. Ciò mantiene l\'orientamento del profilo coerente quando si muove lungo un\'elica (in quanto il vettore di curvatura di un\'elica punta sempre al suo asse). Tuttavia, quando percorso non è un\'elica, la forma risultante può a volte avere strane torsioni. Per maggiori informazioni vedere [Frenet Serret formulas](http://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).

### Transition


<div class="mw-translate-fuzzy">

### Transition 

\"Transition\" imposta lo stile di transizione (raccordo) del Sweep in un giunto nel percorso, se il percorso non definisce l\'angolo di transizione (per esempio se il percorso è una spezzata). La proprietà non è mostrata nella finestra Azioni e può essere trovata nella proprietà dopo che lo sweep è stato creato.


</div>

## Profile limitations and complications 


<div class="mw-translate-fuzzy">

## Limitazioni e complicazioni dei profili 

-   Un vertice o un punto
    -   vertice o punto possono essere utilizzati solo come primo e/o ultimo profilo nella lista dei profili.
        -   Per esempio
            -   non si può realizzare uno Sweep da un cerchio ad un punto,e poi ad una ellisse.
            -   Tuttavia si può realizzare uno Sweep da un punto a un cerchio a un\'ellisse a un altro punto.
-   Profili geometrici aperti o chiusi non possono essere mischiati in un unico Sweep
    -   In uno Sweep, tutti i profili usati (wire, linee ecc) devono essere dello stesso tipo, aperto o chiuso.
        -   Per esempio
            -   FreeCAD non può creare uno Sweep tra un cerchio di Parte e una linea di default di Parte.
-   Funzioni di Draft
    -   Le Funzioni di Draft possono essere utilizzate direttamente come profilo in FreeCAD 0.14 o versioni successive.
        -   Ad esempio, le seguenti funzioni di Draft possono essere utilizzate come profili in un Sweep Parte
            -   Poligono.
            -   Punto, Linea, Wire
            -   B-spline, Curva di Bezier
            -   Cerchio, Ellisse, Rettangolo
-   Schizzi e PartDesign
    -   Il profilo può essere creato con uno schizzo. Tuttavia solo gli schizzi validi verranno visualizzati nell\'elenco di quelli disponibili per la selezione.
    -   Lo schizzo deve contenere un solo wire o linea aperta o chiusa (può essere composto da più segmenti, in quanto se questi segmenti sono tutti collegati costituiscono un unico wire)
-   Part
    -   il profilo può essere una primitiva geometrica valida di Part che può essere creata con lo strumento [Crea Primitive](Part_CreatePrimitives/it.md)
        -   Per esempio le seguenti primitive geometriche di Part possono essere un profilo valido
            -   Punto (Vertex), Linea (Edge)
            -   Elica, Spirale
            -   Cerchio, Ellisse
            -   Poligono regolare
            -   Piano (Face)


</div>

## Links


<div class="mw-translate-fuzzy">

## Link

-   Poiché Sweep viene spesso utilizzato per creare i filetti per viti e bulloni può essere utile consultare il [Tutorial per le filettature](Thread_for_Screw_Tutorial/it.md)


</div>


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/it
