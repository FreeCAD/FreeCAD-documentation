# PartDesign Mirrored/it
---
- GuiCommand   */it   Name   *PartDesign Mirrored   Name/it   *Simmetria   Workbenches   *[[PartDesign Workbench/it   PartDesign]]|MenuLocation   *PartDesign → Simmetria---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento **Simmetria** riflette una funzione su un piano. A partire da v0.17, è in grado di eseguire la riflessione di più funzioni.


</div>

![](images/PartDesign_Mirrored_example.svg )



*Sopra, a sinistra è stata creata una funzione Tasca da uno schizzo contenente un cerchio (A), poi la Tasca è stata utilizzata per creare una funzione Simmetria. Come asse di simmetria è stato utilizzato l'asse verticale dello schizzo (B). A destra è mostrato il risultato (C).*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare le funzioni da rispecchiare. In alternativa, è possibile selezionare la funzione dal dialogo dopo il passaggio 2.

       *   v0.16 e precedenti È possibile selezionare solo una singola funzione e deve essere l\'ultima nella parte inferiore dell\'albero delle funzioni.
2.  Premere il pulsante **[<img src=images/PartDesign_Mirrored.svg style="width   *24px"> '''Simmetria'''**.
3.  v0.17 e superiori Premere **Aggiungi funzione** per aggiungere una funzione da riflettere. La funzione deve essere visibile nella vista 3D   *
    1.  Passare all\'albero del modello;
    2.  Selezionare nell\'albero la funzione da aggiungere e premere **spazio** per renderla visibile nella vista 3D;
    3.  Tornare al pannello Azioni;
    4.  Selezionare la funzione nella vista 3D; essa viene aggiunta alla lista.
    5.  Ripetere per aggiungere altre funzioni.
4.  v0.17 e superiori Premere **Removi funzione** per rimuovere una funzione dall\'elenco o fare clic con il tasto destro del mouse sulla funzione nell\'elenco e selezionare *Rimuovi*.
5.  Definire il piano di riflessione. Vedere le [Opzioni](#Opzioni.md).
6.  Premere **OK**.


</div>

To add or remove features from an existing mirroring   *

1.  Press **Add feature** to add a feature to be mirrored. The feature must be visible in the [3D view](3D_view.md)   *
    1.  Switch to the Model tree;
    2.  Select in the tree the feature to be added and press **Space** to make it visible in the [3D view](3D_view.md);
    3.  Switch back to the Tasks panel;
    4.  Select the feature in the 3D view; it will be added to the list.
    5.  Repeat to add other features.
2.  Press **Remove feature** to remove a feature from the list, or right-click on the feature in the list and select *Remove*.

## Opzioni


<div class="mw-translate-fuzzy">

![Parametri della simmetria in v0.16 e precedenti.](images/mirrored_parameters.png ) ![Parametri della simmetria in v0.17 e successive.](images/Mirrored_parameters_v017_it.png )


</div>

### Selezione del piano di riflessione 

Quando si crea una operazione Simmetria, la finestra di dialogo **Mirrored parameters** (Parametri della simmetria) offre diversi modi per specificare la linea o il piano di riflessione.

#### Asse orizzontale dello sketch 

Utilizza l\'asse orizzontale dello schizzo come asse di simmetria.

#### Asse verticale dello sketch 

Utilizza l\'asse verticale dello schizzo come asse di simmetria.

#### Seleziona riferimento\... 

Consente di selezionare un piano (ad esempio una faccia di un oggetto) da utilizzare come piano di riflessione.

#### Asse creato nello Schizzo 

Se lo schizzo che definisce la caratteristica da rispecchiare contiene anche una linea di costruzione (o più linee) l\'elenco a discesa contiene un asse personalizzato per ognuna delle linee di costruzione presenti nello schizzo. La prima linea di costruzione è etichettata \'Sketch axis 0\'.

![](images/PartDesign_Mirrored_axis_fromconstructionlines.jpg )

#### Piano di base XY/XZ/YZ 


<div class="mw-translate-fuzzy">

v0.17 e successive Seleziona uno dei piani standard dell\'origine del corpo (XY, XZ o YZ).


</div>

### Anteprima

Il risultato della funzione di simmetria può essere visualizzato in tempo reale, prima dell\'esecuzione, attivando **Aggiorna vista**. 

### Limitazioni


<div class="mw-translate-fuzzy">

-   La funzione simmetria non può riflettere un intero corpo solido. Per questo, vedere [Specchia](Part_Mirror/it.md) di Part .


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Mirrored/it
