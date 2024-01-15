# Part Sweep/it
---
 GuiCommand:   Name: Part Sweep   Name/it: Sweep   MenuLocation: Parte , Sweep...   ---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Part_Sweep.svg  style="width:24px;"> **Part Sweep** di FreeCAD serve per creare una faccia, un guscio o una forma solida da uno o più profili (la sezione trasversale), proiettati lungo un percorso.


</div>


<div class="mw-translate-fuzzy">

Lo strumento Parte Sweep è simile a <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Part Loft](Part_Loft/it.md), ma con l\'aggiunta di un percorso per definire la proiezione tra i profili.


</div>

<img alt="" src=images/Part_Sweep_simple.png  style="width:400px;"> 
*A solid sweep generated from a single profile (A) distributed along a spine (B)*



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

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles and paths. <small>(v0.20)</small> 

## Options

#### Solid


<div class="mw-translate-fuzzy">

## Proprietà

### Solido

Se \"Solid\" è impostato \"true\" FreeCAD crea un solido se i profili sono delle geometrie chiuse, se è impostato \"false\" crea una faccia o, un guscio se ci sono più facce, sia per profili aperti che chiusi.


</div>

#### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">


<div class="mw-translate-fuzzy">

### Frenet 

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;"> La proprietà \"Frenet\" controlla come cambia l\'orientamento del profilo lungo il percorso di sweep. Se \"Frenet\" è \"false\", l\'orientamento del profilo rimane sempre lo stesso per tutti i punti. La forma risultante è quella con la minima torsione possibile. Quando un profilo viene trascinato lungo un\'elica, questo causa una lenta rotazione del profilo mentre segue dell\'elica. Impostando \"Frenet\" su true si previene questa rotazione. Se \"Frenet\" è \"true\", lungo un percorso elicoidale l\'orientamento del profilo sarà coerente all\'orientamento locale del percorso.


</div>


<div class="mw-translate-fuzzy">

Se \"Frenet\" è \"true\" l\'orientamento del profilo è calcolato basandosi sulla curvatura e tangenza dei vettori locali del percorso. Ciò mantiene l\'orientamento del profilo coerente quando si muove lungo un\'elica (in quanto il vettore di curvatura di un\'elica punta sempre al suo asse). Tuttavia, quando percorso non è un\'elica, la forma risultante può a volte avere strane torsioni. Per maggiori informazioni vedere [Frenet Serret formulas](http://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).


</div>

#### Transition


<div class="mw-translate-fuzzy">

### Transition 

\"Transition\" imposta lo stile di transizione (raccordo) del Sweep in un giunto nel percorso, se il percorso non definisce l\'angolo di transizione (per esempio se il percorso è una spezzata). La proprietà non è mostrata nella finestra Azioni e può essere trovata nella proprietà dopo che lo sweep è stato creato.


</div>

## Properties

See also: [Property editor](Property_editor.md).

A Part Sweep object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Sweep}}

-    **Sections|LinkList**: lists the sections used.

-    **Spine|LinkSub**: spine (path) to sweep along.

-    **Solid|Bool**: true or false (default). True creates a Solid.

-    **Frenet|Bool**: true or false (default). True uses Frenet algorithm.

-    **Transition|Enumeration**: transition mode. Options are *Transformed*, *Right corner* or *Round corner*.

## Limitations

### Vertex or point 

A vertex or point may only be used as the first and/or last profile.
For example:

-   You cannot Sweep from a circle to a point, to an ellipse.
-   You can however Sweep from a point to a circle to an ellipse to another point.

### Profiles

In one Sweep, all profiles (lines wires etc.) must be either open or closed.
For example:

-   FreeCAD cannot Sweep between a Part Circle and a Part Line.

### Sketches

-   The profile may be created with a sketch. However only valid sketches will be available for selection in the task panel.
-   The sketch must contain only one open or closed wire or line (can be multiple lines, if those lines are all connected as they are then a single wire).

### Draft Workbench objects 

A profile can be a [Draft Workbench](Draft_Workbench.md) object.
The following objects can be valid profiles:

-   Point
-   Line, Wire
-   B-spline, Bézier Curve
-   Circle, Ellipse
-   Rectangle, Polygon

### Part Workbench objects 

A profile can be a Part object created with the [Part Primitives](Part_Primitives.md) command.
The following objects can be valid profiles:

-   Point (Vertex)
-   Line (Edge)
-   Helix, Spiral
-   Circle, Ellipse
-   Regular Polygon
-   Plane (Face)

## Links


<div class="mw-translate-fuzzy">

## Link

-   Poiché Sweep viene spesso utilizzato per creare i filetti per viti e bulloni può essere utile consultare il [Tutorial per le filettature](Thread_for_Screw_Tutorial/it.md)


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/it
