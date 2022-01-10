# PartDesign LinearPattern/it
---
- GuiCommand:/it   Name:PartDesign LinearPattern   Name/it:Schiera lineare   MenuLocation:PartDesign → Serie lineare   Workbenches:[SeeAlso:[[PartDesign PolarPattern/it|Serie polare](PartDesign_Workbench/it___PartDesign]].md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:24px;"> **Serie lineare** crea copie equidistanti di una funzione in una direzione lineare. A partire da v0.17, è in grado di replicare più funzioni.


</div>

![](images/PartDesign_LinearPattern_example.svg )

*Sopra: un Pad a forma di L (B) creato su un pad di base (A, indicato anche come \"supporto\") è usato per produrre una schiera lineare. A destra viene mostrato il risultato (C).*

## Uso


<div class="mw-translate-fuzzy">

1.  Selezionare le funzioni da modellare. In alternativa, è possibile selezionare la funzione da un dialogo dopo il passaggio 2.

    :   v0.16 e precedenti È possibile selezionare solo una singola funzione e deve essere l\'ultima nella parte inferiore dell\'albero delle funzioni.
2.  Premere il pulsante **<img src=images/PartDesign_LinearPattern.png style="width:24px"> '''Serie lineare'''**.
3.  v0.17 e superiore Premere **Aggiungi funzione** per aggiungere una funzione da modellare. La funzione deve essere visibile nella vista 3D:
    1.  Passare all\'albero del modello;
    2.  Selezionare nell\'albero la funzione da aggiungere e premere **spazio** per renderla visibile nella vista 3D;
    3.  Tornare al pannello Azioni;
    4.  Selezionare la funzione nella vista 3D; essa viene aggiunta alla lista.
    5.  Ripetere per aggiungere altre funzioni.
4.  v0.17 e superiore Premere **Rimuovi funzione** per rimuovere una funzione dall\'elenco o fare clic con il tasto destro del mouse sulla funzione nell\'elenco e selezionare \"Rimuovi\".
5.  Definire la Direzione. Vedere le [Opzioni](#Options/it.md).
6.  Definire la lunghezza (distanza) tra l\'ultima occorrenza copiata e la funzione originale.
7.  Impostare il numero di occorrenze.
8.  Premere **OK** .


</div>

To add or remove features from an existing pattern:

1.  Press **Add feature** to add a feature to be patterned. The feature must be visible in the [3D view](3D_view.md):
    1.  Switch to the Model tree;
    2.  Select in the tree the feature to be added and press **Space** to make it visible in the [3D view](3D_view.md);
    3.  Switch back to the Tasks panel;
    4.  Select the feature in the 3D view; it will be added to the list.
    5.  Repeat to add other features.
2.  Press **Remove feature** to remove a feature from the list, or right-click on the feature in the list and select **Remove**

## Opzioni

![Parametri LinearPattern in v0.16 e precedenti.](images/Linearpattern_parameters.png ) ![Parametri LinearPattern in v0.17 e successive.](images/Linearpattern_parameters_v017.png )

### Direzione

Quando si crea una funzione di schiera lineare, il dialogo **Parametri LinearPattern** offre diversi modi per specificare la direzione del pattern.

#### Asse orizzontale dello schizzo 

Usa l\'asse orizzontale dello schizzo per la direzione.

#### Asse verticale dello schizzo 

Usa l\'asse verticale dello schizzo per la direzione.

#### Asse normale allo schizzo 

v0.17 e superiori Usa l\'asse normale dello schizzo per la direzione.

#### Seleziona riferimento\... 

Consente di selezionare una linea di riferimento, DatumLine, o un bordo di un oggetto o una linea di uno schizzo da utilizzare per la direzione.

#### Asse di schizzo personalizzato 

Se lo schizzo che definisce la funzione da modellare contiene anche una linea di costruzione (o linee), l\'elenco a discesa contiene un asse dello schizzo personalizzato per ogni linea di costruzione. La prima linea di costruzione è etichettata come \"Schizzo asse 0\".

#### Asse Base (X/Y/Z) 

v0.17 e superiore Seleziona uno degli assi standard di Origine del Corpo (X, Y o Z) come direzione. 

## Limitations


<div class="mw-translate-fuzzy">

## Limitazioni

-   Le forme della schiera non possono sovrapporsi l\'un l\'altra ad eccezione del caso particolare di due sole forme (l\'originale più una copia)
-   Qualsiasi forma della schiera che non si sovrapponga con il supporto dell\'originale viene esclusa. Questo assicura che qualsiasi oggetto di Progettazione Parte (PartDesign) è sempre costituito da un unico solido collegato
-   Funziona solo con gli strumenti [additivi](PartDesign_Workbench/it#Strumenti_Additivi.md) e [sottrattivi](PartDesign_Workbench/it#Strumenti_sottrattivi.md). Gli [strumenti di trasformazione](PartDesign_Workbench/it#Strumenti_di_trasformazione.md), gli [strumenti di vestizione](PartDesign_Workbench/it#Strumenti_di_vestizione.md) e le [operazioni booleane](PartDesign_Boolean/it.md) non sono supportati.
-   Per altre limitazioni, vedere la funzione [Simmetria](PartDesign_Mirrored/it.md)





</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign LinearPattern/it
