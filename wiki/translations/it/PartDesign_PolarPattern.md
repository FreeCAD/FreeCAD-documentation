---
- GuiCommand:/it
   Name:PartDesign_PolarPattern
   Name/it:Serie polare
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:PartDesign → Serie polare
   SeeAlso:[Serie lineare](PartDesign_LinearPattern/it.md)
---

# PartDesign PolarPattern/it


</div>

## Descrizione

Lo strumento **Serie polare** prende una funzione selezionata e ne crea una serie di copie ruotate attorno a un asse prescelto. A partire da v0.17, è in grado di replicare più funzioni.

![](images/PartDesign_PolarPattern_example.png )

*Sopra: una tasca a forma di slot (B) realizzata sopra un solido di base (A, indicato anche come supporto) viene utilizzata per un modello polare. Il risultato (C) è mostrato a destra.*

## Utilizzo

#### To create a pattern 


<div class="mw-translate-fuzzy">

1.  Selezionare le funzioni da replicare. In alternativa, è possibile selezionare la funzione da un dialogo dopo il passaggio 2.

    :   v0.16 e successive È possibile selezionare solo una singola funzione e deve essere l\'ultima nella parte inferiore dell\'albero delle funzioni.
2.  Premere il pulsante **<img src=images/PartDesign_PolarPattern.svg style="width:24px">** **Serie polare**.
3.  v0.17 e successive Premere **Aggiungi funzione** per aggiungere una funzione da modellare. La funzione deve essere visibile nella vista 3D:
    1.  Passare all\'albero del modello;
    2.  Selezionare nell\'albero la funzione da aggiungere e premere la **barra spaziatrice** per renderla visibile nella vista 3D;
    3.  Tornare al pannello Azioni;
    4.  Selezionare la funzione nella vista 3D; essa viene aggiunta alla lista.
    5.  Ripetere per aggiungere altre funzioni.
4.  v0.17 e successive Premere **Rimuovi funzione** per rimuovere una funzione dall\'elenco o fare clic con il tasto destro del mouse sulla funzione nell\'elenco e selezionare *Rimuovi*.
5.  Definire l\'asse. Vedere le [Opzioni](#Options/it.md).
6.  Definire l\'angolo tra l\'ultima occorrenza copiata e la funzione originale.
7.  Impostare il numero di occorrenze.
8.  Premere **OK**.


</div>

#### Ordering features 

![](images/PartDesign_feature-order.gif ) 
*Effect of the feature order*


<small>(v0.19)</small> 

You can change the order by dragging the feature in the list and you will see the result immediately as preview.

#### Adding features 

###### v0.18

1.  Press **Add feature** to add a feature to be patterned. The feature must be visible in the [3D view](3D_view.md):
2.  Switch to the Model tree;
3.  Select in the tree the feature to be added and press **Spacebar** to make it visible in the [3D view](3D_view.md);
4.  Switch back to the Tasks panel;
5.  Select the feature in the 3D view; it will be added to the list.
6.  Repeat to add other features.

###### v0.19

1.  Press **Add feature** to add a feature to be patterned.
2.  Switch to the Model tree;
3.  Select in the tree the feature to be added.
4.  Repeat to add other features.

#### Removing features 

-   Right-click on the feature in the list and select *Remove*.

or

###### v0.18 

1.  Press **Remove feature** to remove a feature from the list. The feature must be visible in the [3D view](3D_view.md):
2.  Switch to the Model tree;
3.  Select in the tree the feature to be removed and press **Spacebar** to make it visible in the [3D view](3D_view.md);
4.  Switch back to the Tasks panel;
5.  Select the feature in the 3D view; it will have been removed from the list.
6.  Repeat to remove other features.

###### v0.19 

1.  Press **Remove feature** to remove a feature from the list.
2.  Switch to the Model tree;
3.  Select in the tree the feature to be removed.
4.  Repeat to remove other features.

## Opzioni

![](images/Polarpattern_parameters.png )

### Asse

Durante la creazione di una funzione di serie polare, il dialogo \'Parametri serie polare\' offre modi diversi per specificare l\'asse di rotazione del modello.

#### Asse normale dello schizzo 

Come asse della serie viene preso un asse essendo perpendicolare al disegno e posto nell\'origine del disegno.
La direzione della schiera può essere invertita barrando \'direzione inversa\'.

#### Asse orizzontale dello schizzo 

Usa l\'asse orizzontale dello schizzo per l\'asse.

#### Asse verticale dello schizzo 

Usa l\'asse verticale dello schizzo per l\'asse.

#### Asse di schizzo personalizzato 

Se lo schizzo che definisce la funzione da modellare contiene anche una linea di costruzione (o linee), l\'elenco a discesa contiene un asse dello schizzo personalizzato per ogni linea di costruzione. La prima linea di costruzione è etichettata come \"Schizzo asse 0\".

#### Asse Base (X/Y/Z) 

v0.17 e superiore Seleziona uno degli assi standard di Origine del Corpo (X, Y o Z) come asse.

#### Seleziona riferimento\... 

Consente di selezionare una linea di riferimento, DatumLine, o un bordo di un oggetto o una linea di uno schizzo da utilizzare per l\'asse.

### Angolo e numero di duplicati 

Specifica l\'angolo da coprire con la schiera e il numero totale di forme della schiera (inclusa la forma originale). Per esempio, la combinazione quattro copie in un angolo di 180 gradi produce una spaziatura di 60 gradi tra ogni copia. C\'è una eccezione: quando l\'angolo è di 360 gradi e la prima e l\'ultima copia sono identiche, vengono prodotte quattro copie distanziate 90 gradi. 


## Limitazioni

-   Per le limitazioni vedere la funzione [Serie lineare](PartDesign_LinearPattern/it#Limitazioni.md).





<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign PolarPattern/it
