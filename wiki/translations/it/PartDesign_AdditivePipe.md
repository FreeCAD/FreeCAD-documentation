---
- GuiCommand   */it
   Name   *PartDesign AdditivePipe
   Name/it   *Sweep additivo
   Workbenches   *[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation   *PartDesign → Sweep additivo
   Version   *0.17
   SeeAlso   *[Loft additivo](PartDesign_AdditiveLoft/it.md)
---

# PartDesign AdditivePipe/it


</div>

## Descrizione

**Sweep additivo** crea un solido nel corpo attivo spazzando uno o più schizzi (detti anche sezioni trasversali) lungo un percorso aperto o chiuso. Se il corpo contiene già delle funzionalità, lo sweep additivo viene unito a loro.

![](images/PartDesign_AdditivePipe_example.svg )


<div class="mw-translate-fuzzy">

*A sinistra le sezioni trasversali (A) e (B) da spazzare lungo il percorso (C); a destra lo sweep additivo risultante.*


</div>

## Utilizzo

L\'immagine di esempio sopra mostra due diverse forme di sezione trasversale. Il testo seguente descrive la procedura con una sola forma. Ciò consente di ottenere una parte con la stessa sezione trasversale lungo l\'intero percorso.


<div class="mw-translate-fuzzy">

1.  Creare due schizzi separati;
    -   uno per il percorso, ad esempio due linee collegate da una curva come nell\'immagine sopra,
    -   uno per la forma della sezione trasversale, ad es. un cerchio come la prima forma nell\'immagine sopra.
2.  **Disporre** correttamente le due forme nello spazio 3D. L\'origine dello schizzo della sezione trasversale deve essere posizionata sulla linea del tracciato. I due schizzi devono essere **ortogonali**. Questo può essere fatto con la funzione \"Mappatura dello schizzo\" (rendere visibili entrambi gli schizzi con **Spazio**. Selezionare lo schizzo della sezione trasversale. Selezionare Proprietà/DataTab/MapMode. Fare clic sui **...** visualizzati sul lato destro Nella finestra di dialogo Associazione selezionare un vertice dello schizzo del percorso e selezionare la modalità corretta per allineare correttamente i due schizzi).
3.  Premere il pulsante **<img src="images/PartDesign_AdditivePipe.svg" width=16px> [Sweep additivo](PartDesign_AdditivePipe/it.md)**.
4.  Nella finestra di dialogo **Selezione della funzione**, selezionare lo schizzo da utilizzare perla sezione trasversale e fare clic su **OK**.
    -   In alternativa, è possibile selezionare lo schizzo della sezione trasversale prima di premere il pulsante Sweep additivo. In tal caso non viene visualizzata la finestra di dialogo \"Selezione della funzione\".
5.  Nella scheda **Parametri di sweep** in **Percorso di sweep**, premere il pulsante **Oggetto**.
6.  Selezionare lo schizzo da utilizzare come tracciato nella vista 3D. In questo caso l\'intero schizzo verrà utilizzato come tracciato.
    -   In alternativa, è possibile selezionare singoli bordi dello schizzo premendo **Aggiungi bordo** e selezionando i bordi nella vista 3D. Si noti che è necessario premere nuovamente **Aggiungi bordo** per ciascun bordo. Si deve selezionare una linea continua senza rami.
7.  Le altre impostazioni dovrebbero funzionare con le impostazioni predefinite nella maggior parte dei casi.
8.  Cliccare **OK**.


</div>


<div class="mw-translate-fuzzy">

Per utilizzare più di una sezione trasversale, iniziare con il primo schizzo della sezione trasversale come descritto sopra. Quindi in **Trasformazione della sezione** impostare la Modalità di trasformazione su *\' Multisezione*\', poi premere **Aggiungi sezione** quindi selezionare uno schizzo nella [vista 3D](3D_view/it.md). Ripetere l\'operazione per ogni sezione trasversale aggiuntiva.


</div>

## Options


<div class="mw-translate-fuzzy">

## Opzioni

**Trasformazione della sezione**   *

-   Selezionare **Constant** per usare un singolo profilo
-   Selezionare **Multisection** per usare più profili

**Orientamento della sezione**   *

-   Standard

       *   Ciò mantiene la forma della sezione trasversale perpendicolare al percorso. Questa è l\'impostazione predefinita.
-   Fissa
    -   Orientamento impostato dal primo profilo e costante per tutta la lunghezza. Ciò disattiva l\'allineamento al vettore normale del percorso. Ciò significa che la forma della sezione trasversale non ruoterà con il percorso. Provare uno sweep lungo un cerchio per vedere l\'effetto.
-   Frenet
    -   Crea la minima rotazione possibile del profilo. Per maggiori informazioni, vedere [Frenet-Serret Formulas](https   *//en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas)
-   Ausiliaria
    -   Specifica il percorso secondario per guidare lo sweep.
    -   Per ogni punto **P** lungo il percorso di sweep, ci sarà un corrispondente punto **Q** sul percorso ausiliario.
    -   Man mano che il profilo viene spostato, esso viene trasformato in modo tale che la linea **PQ** sia la normale del percorso di sweep.
    -   Se **Equivalenza curvilineare** viene attivata, allora i punti **Q** vengono ridimensionati proporzionalmente lungo il percorso di sweep, indipendentemente dalla sua lunghezza.
-   Binormale
    -   Specifica il vettore binomiale in X, Y e Z

**Angolo di transizione**

-   Trasformato
-   Angolo retto
-   Angolo arrotondato


</div>

## Proprietà

-    {{PropertyData/it|Label}}   * nome dato all\'operazione, questo nome può essere cambiato a piacere.

-    {{PropertyData/it|Refine}}   * vero o falso. Se impostato su true, pulisce il solido dai bordi residui lasciati dalle operazioni. Per maggiori dettagli vedere [Affina forma](Part_RefineShape/it.md).

-    {{PropertyData/it|Sections}}   * elenca le sezioni utilizzate.

-    {{PropertyData/it|Spine Tangent}}   * vero o falso (predefinito). True estende il percorso per includere i bordi tangenti.

-    {{PropertyData/it|Auxiliary Spine Tangent}}   * vero o falso (predefinito). Vero estende il percorso ausiliario per includere i bordi tangenti.

-    {{PropertyData/it|Auxiliary Curvelinear}}   * vero o falso (predefinito). True calcola la normale tra i punti equidistanti su entrambe le dorsali.

-    {{PropertyData/it|Mode}}   * modalità di profilo. vedere [Opzioni](#Opzioni.md).

-    {{PropertyData/it|Binormal}}   * vettore binomiale per la modalità di orientamento corrispondente.

-    {{PropertyData/it|Transition}}   * modalità di transizione. Le opzioni sono \"Trasformato\", \"Angolo retto\" o \"Angolo rotondo\".

-    {{PropertyData/it|Transformation}}   * \"Costante\" usa una singola sezione trasversale. \"Multisezione\" utilizza due o più sezioni trasversali. \"Linear\", \"S-shape\" e \"Interpolation\" non sono al momento funzionanti.

## Notes


<div class="mw-translate-fuzzy">

-   Gli schizzi devono formare profili chiusi.
-   Il percorso può provenire solo da un singolo schizzo, funzione o ShapeBinder. Nel caso in cui si desideri eseguire lo sweep su diversi schizzi, utilizzare un SubShapeBinder (verde).
-   Il percorso non deve contenere ramificazioni o giunzioni a T ecc. Gli anelli vanno bene.
-   Non è possibile utilizzare un vertice come sezione trasversale.
-   Si possono avere dei problemi se la sezione trasversale non è perpendicolare al percorso in 3D (alcuni altri sistemi CAD considerano l\'origine della sezione trasversale come il percorso e non richiedono di posizionare esplicitamente tale schizzo).
-   Una sezione trasversale non può giacere sullo stesso piano di quella immediatamente precedente.
-   Per controllare meglio la forma dello sweep, è consigliabile che tutte le sezioni abbiano lo stesso numero di segmenti. Ad esempio, per uno sweep tra un rettangolo e un cerchio, il cerchio può essere suddiviso in 4 archi collegati.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePipe/it
