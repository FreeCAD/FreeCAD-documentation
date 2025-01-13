---
 GuiCommand:
   Name: Part Sweep
   Name/it: Part Sweep
   MenuLocation: Parte , Sweep...
   Workbenches: Part_Workbench/it
   SeeAlso: Part_Loft/it
---

# Part Sweep/it



## Descrizione

Il comando <img alt="" src=images/Part_Sweep.svg  style="width:24px;"> [Part Sweep](Part_Sweep/it.md) crea una faccia, un guscio (shell) o una forma solida da uno o più profili (sezioni trasversali) distribuiti lungo un percorso.

Il comando Part Sweep è simile a <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Part Loft](Part_Loft/it.md), ma con l\'aggiunta di un percorso.

<img alt="" src=images/Part_Sweep_simple.png  style="width:400px;"> 
*Un'estrusione solida generata da un singolo profilo (A) distribuito lungo un percorso (B)*



## Utilizzo

1.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Part_Sweep.svg" width=16px> [Sweep...](Part_Sweep/it.md)**.
    -   Seleziona l\'opzione **Parte → <img src="images/Part_Sweep.svg" width=16px> Sweep...** dal menu.
2.  Si apre il [pannello azioni](Task_panel/it.md) di Sweep.
3.  Nell\'elenco *Profili disponibili* a sinistra selezionare un profilo e fare clic sulla freccia destra per inserirlo nell\'elenco *Profili selezionati* a destra.
4.  Ripetere se si desidera più di un profilo.
5.  Le frecce su e giù riordineranno l\'elenco a destra. Ma questo non ha alcun impatto sul risultato. La posizione dei profili lungo il percorso determina l\'ordine in cui vengono utilizzati.
6.  Fare clic sul pulsante **Percorso Sweep**, quindi scegliere una delle modalità di selezione:
    -   *Selezione segmento*: seleziona uno o più bordi contigui nella [vista 3D](3D_view/it.md) (premere **CTRL** per la selezione multipla) e fare clic su **Fatto**. Lo sweep verrà generato solo lungo i bordi selezionati.
    -   *Completa la selezione del percorso*: passa alla [Vista ad albero](Tree_view/it.md), selezionare l\'oggetto da utilizzare come percorso, ritornare al pannello delle azioni e fare clic su **Fine**. Lo sweep verrà generato lungo tutti i bordi contigui presenti nell\'oggetto.
7.  Definire le opzioni [Solid](#Solid.md) e [Frenet](#Frenet.md).
8.  Fare clic su **OK**.



### Geometria accettata 

-   **Profili:** può essere un punto (vertice), una linea (bordo), una polilinea o una faccia. I bordi e le polilinee possono essere aperti o chiusi. Esistono varie [Limitazioni](#Limitazioni.md), vedere di seguito. A volte non è sufficiente allineare correttamente il profilo con il percorso. Per far funzionare correttamente lo strumento, potrebbe anche essere necessario [associare](Part_EditAttachment/it.md) il profilo al percorso. Se lo schizzo del profilo è associato all\'estremità sbagliata del bordo del percorso, modificare **Map Path Parameter** da 0 a 1.

-   **Percorso**: può essere una linea (bordo) o una serie di linee collegate, una polilinea o vari oggetti dell\'ambiente Part, oggetti dell\'ambiente Draft o uno schizzo. Il percorso può essere aperto o chiuso.

-   Gli oggetti [App Link](App_Link/it.md) collegati ai tipi di oggetto appropriati e i contenitori [App Part](App_Part/it.md) con gli oggetti visibili appropriati all\'interno possono essere utilizzati anche come profili e percorsi. {{Version/it|0.20}}



## Opzioni



#### Solido

Se \"Solido\" è impostato su \"true\", FreeCAD crea un solido, a condizione che i profili siano chiusi; se impostato su \"false\", FreeCAD crea una faccia o un guscio (shell) per profili aperti o chiusi.

#### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">

La proprietà \"Frenet\" controlla come cambia l\'orientamento del profilo mentre questo segue il percorso. Se \"Frenet\" è \"false\", l\'orientamento del profilo viene mantenuto coerente da punto a punto. La forma risultante ha la minima torsione possibile. In modo non intuitivo, quando un profilo viene spostato lungo un\'elica, ciò si traduce in un orientamento del profilo che si sposta lentamente (ruota) mentre segue l\'elica. L\'impostazione di \"Frenet\" su \"true\" impedisce ciò.

Se \"Frenet\" è \"true\" l\'orientamento del profilo è basato sulla curvatura e tangenza dei vettori locali del percorso. Ciò mantiene l\'orientamento del profilo coerente quando si muove lungo un\'elica (in quanto il vettore di curvatura di un\'elica punta sempre al suo asse). Tuttavia, quando percorso non è un\'elica, la forma risultante può a volte avere strane torsioni. Per maggiori informazioni vedere [Frenet Serret formulas](http://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).

#### Transition

\"Transition\" imposta lo stile di transizione dello Sweep nei giunti non tangenziali del percorso. La proprietà non è esposta nel pannello delle attività e può essere trovata in [proprietà](Property_editor/it.md) dopo la creazione dello Sweep.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Part Sweep deriva da un oggetto [Funzione Part](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Sweep}}

-    **Sections|LinkList**: elenca le sezioni utilizzate.

-    **Spine|LinkSub**: percorso da seguire.

-    **Solid|Bool**: vero o falso (predefinito). True crea un solido.

-    **Frenet|Bool**: vero o falso (predefinito). True utilizza l\'algoritmo Frenet.

-    **Transition|Enumeration**: modalità di transizione. Le opzioni sono *Trasformato*, *Angolo destro* o *Angolo arrotondato*.



## Limitazioni



### Vertici o punti 

Un vertice o un punto possono essere utilizzati solo come primo e/o ultimo profilo.
Per esempio:

-   Non è possibile eseguire lo Sweep da un cerchio a un punto o a un\'ellisse.
-   E\' possibile comunque eseguire lo Sweep da un punto a un cerchio, da un\'ellisse a un altro punto.



### Profili

In uno Sweep, tutti i profili (linee, polilinee, ecc.) devono essere aperti o chiusi.
Per esempio:

-   FreeCAD non può eseguire lo Sweep tra un Part Cerchio e una Part Linea.



### Schizzi

-   Il profilo può essere creato con uno schizzo. Tuttavia, solo gli schizzi validi saranno disponibili per la selezione nel pannello delle azioni.
-   Lo schizzo deve contenere solamente una polilinea o linea aperte o chiuse (possono essere più linee, se tali linee sono tutte collegate come se fossero un unica polilinea).



### Oggetti dell\'Ambiente Draft 

Un profilo può essere un oggetto [Draft](Draft_Workbench/it.md).
I seguenti oggetti possono essere profili validi:

-   Punto
-   Linea, polilinea
-   B-spline, curva di Bézier
-   Cerchio, Ellisse
-   Rettangolo, Poligono



### Oggetti Ambiente Part 

Un profilo può essere un oggetto Part creato con il comando [Part Primitive](Part_Primitives/it.md).
I seguenti oggetti possono essere profili validi:

-   Punto (vertice)
-   Linea (Bordo)
-   Elica, Spirale
-   Cerchio, Ellisse
-   Poligono regolare
-   Piano (faccia)

## Links

-   Uno Sweep viene spesso utilizzato per creare filettature per viti e bulloni, vedere il [Tutorial per le filettature](Thread_for_Screw_Tutorial/it.md) per maggiori informazioni.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/it
