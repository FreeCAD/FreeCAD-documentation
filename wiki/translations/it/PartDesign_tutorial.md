---
- TutorialInfo   */it
   Topic   * Schizzo
   Level   * Base
   Time   * 15 minuti
   Author   *[http   *//freecadweb.org/wiki/index.php?title=User   *Drei Drei]
   FCVersion   *0.16 o superiore
   Files   *
}}

### Introduzione

Questo tutorial ha lo scopo di introdurre il lettore al flusso di lavoro di base dell\'ambiente [PartDesign](PartDesign_Workbench/it.md). Il lettore vedrà come creare oggetti 3D sulla base di schizzi, eseguire operazioni di sottrazione e come replicare specifiche funzioni in una schiera.

<img alt="" src=images/Sketcher_tutorial_result.png  style="width   *480px;">


<div class="mw-translate-fuzzy">

### Requisiti

-   FreeCAD versione 0.17 o superiore
-   Il lettore abbia terminato il [tutorial di Schizzo](Basic_Sketcher_Tutorial/it.md)


</div>

### Procedimento

#### Creare la geometria 3D 

Lo scopo dell\'ambiente PartDesign è quello di consentire all\'utente di creare la geometria nello spazio 3D. Pertanto, esso è dotato degli strumenti adatti ad usare gli schizzi e a convertirli in oggetti 3D.


<div class="mw-translate-fuzzy">

Per raggiungere questo obiettivo ci sono due funzioni fondamentali    * <img alt="" src=images/PartDesign_Pad.png  style="width   *32px;"> [Prisma](PartDesign_Pad/it.md) e <img alt="" src=images/PartDesign_Revolution.png  style="width   *32px;"> [Rivoluzione](PartDesign_Revolution/it.md). Assieme alle loro controparti sottrattive (<img alt="" src=images/PartDesign_Pocket.png  style="width   *32px;"> [Cavità](PartDesign_Pocket/it.md) e <img alt="" src=images/PartDesign_Groove.png  style="width   *32px;"> [Gola](PartDesign_Groove/it.md)) esse costituiscono la maggior parte delle azioni comuni utilizzate da questo ambiente.


</div>


<div class="mw-translate-fuzzy">

1.  Passare nell\'ambiente PartDesign
2.  Selezionare lo schizzo creato nel [tutorial di Schizzo](Basic_Sketcher_Tutorial/it.md)
3.  Selezionare <img alt="" src=images/PartDesign_Pad.png  style="width   *32px;"> [Pad](PartDesign_Pad/it.md)
4.  Impostare la distanza 5 mm
5.  Selezionare **Ok**


</div>


<div class="mw-translate-fuzzy">

Un altro strumento per creare la geometria 3D è <img alt="" src=images/PartDesign_Revolution.png  style="width   *32px;"> [Rivoluzione](PartDesign_Revolution/it.md).


</div>

<img alt="" src=images/PartDesign_revolution_exercise.png  style="width   *480px;">


<div class="mw-translate-fuzzy">

1.  Creare uno schizzo basato sull\'immagine predente
2.  Selezionare <img alt="" src=images/PartDesign_Revolution.png  style="width   *32px;"> [Rivoluzione](PartDesign_Revolution/it.md)
3.  Impostare \"Axis\" su \"Asse orizzontale dello schizzo\"
4.  Impostare l\'angolo a 360°


</div>

#### Funzioni sottrattive 

Iniziare creando un disegno con la forma da sottrarre.


<div class="mw-translate-fuzzy">

1.  Selezionare la faccia piatta superiore di **Revolution**
2.  Selezionare <img alt="" src=images/Sketcher_NewSketch.png‎‎  style="width   *32px;"> [Nuovo schizzo](Sketcher_NewSketch/it.md)
3.  Selezionare <img alt="" src=images/Sketcher_External.png  style="width   *32px;"> [Geometria esterna](Sketcher_External/it.md)
4.  Avvicinarsi al bordo del pad. Viene evidenziato un arco
5.  Selezionare l\'arco. Nel disegno dovrebbe apparire un arco di un colore diverso
6.  Creare un esagono centrato nello stesso centro dell\'arco e impostare il raggio del cerchio di riferimento a 5 mm


</div>


<div class="mw-translate-fuzzy">


{{Message| '''Geometria esterna'''
Dopo che è stato creato un elemento 3D è possibile creare dei riferimenti ad esso all'interno di uno schizzo.
# Selezionare <img src="images/Sketcher_External.png" width=32px> [Geometria esterna](Sketcher_External/it.md).
# Accostarsi all'elemento a cui si desidera fare riferimento, ad esempio, il bordo di un '''Pad'''.
# Cliccare sull'elemento
# Nello schizzo dovrebbero apparire dei nuovi elementi di un colore diverso  nella posizione della funzionalità a cui si desidera fare riferimento.
---

# PartDesign tutorial/it

 

</div>

<img alt="" src=images/PartDesign_pocket_exercise.png  style="width   *480px;">

Procedere applicando una funzione **Cavità**.


<div class="mw-translate-fuzzy">

1.  Selezionare lo schizzo
2.  Selezionare <img alt="" src=images/PartDesign_Pocket.png  style="width   *32px;"> [Cavità](PartDesign_Pocket/it.md)
3.  Impostare la lunghezza **Attraversa tutto**


</div>

#### Le funzioni Serie 

Richiamare il profilo estruso che è stato creato all\'inizio del tutorial.

1.  Selezionare la faccia superiore dell\'oggetto
2.  Creare un nuovo schizzo
3.  Creare una geometria di riferimento collegata alla parte superiore della figura
4.  Creare un cerchio vincolato al centro dell\'arco di riferimento
5.  Impostare il suo raggio a 3 mm
6.  Scavare (Pocket) lo schizzo attraverso tutto il pezzo

Invece di creare un cerchio per ogni foro nello schizzo, introduciamo il concetto di **Pattern Features** (Schiera di funzioni). Questi strumenti funzionano replicando una funzione che è già stata creata nel pezzo e che si vuole riprodurre in una disposizione lineare o circolare. Utilizzeremo una combinazione di schiere **Lineari** e **Polari** simulativamente per ottenere il pezzo finale.


<div class="mw-translate-fuzzy">

1.  Nella vista ad albero selezionare la funzione Pocket appena creata.
2.  Selezionare <img alt="" src=images/PartDesign_MultiTransform.png  style="width   *32px;"> [MultiTrasformazione](PartDesign_MultiTransform/it.md) di PartDesign


</div>

Nella Vista combinata viene chiesto di introdurre le trasformazioni che si desiderano. Si noti che nel menu dei parametri di MultiTransform si vede che FreeCAD ha identificato la Pocket come funzionalità originale e una seconda casella chiede di fare clic con il tasto destro per introdurre le funzionalità del modello.

1.  Fare clic con il pulsante destro del mouse sulla casella
2.  Selezionare **Add Linear Pattern**
3.  Impostare la **Direction** in **Vertical Sketch Axis**
4.  Impostare la lunghezza su 10 mm
5.  Lasciare le occorrenze a 2
6.  Cliccare OK
7.  Fare nuovamente clic sulla casella per aggiungere un **Polar Pattern**. Notare che nella visualizzazione 3D ora è stata aggiunta la schiera lineare.
8.  Impostare le occorrenze a 5
9.  Fare due volte clic su OK

Dopo aver completato questa attività, si dovrebbe avere il seguente risultato.

<img alt="" src=images/PartDesign_multitransform_exercise.png  style="width   *480px;">

In caso contrario, modificare l\'operazione di MultiTransformazione facendo doppio clic su di essa nella visualizzazione di albero. Controllare entrambe le funzioni del modello per rilevare le modifiche necessarie, come l\'asse o se la direzione deve essere invertita.

A questo punto il flusso di lavoro di base per il [Modulo PartDesign](PartDesign_Workbench/it.md) è terminato.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign tutorial/it
