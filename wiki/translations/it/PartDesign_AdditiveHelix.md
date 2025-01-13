---
 GuiCommand:
   Name: PartDesign AdditiveHelix
   Name/it: Elica Additiva
   MenuLocation: Part Design , Crea una funzione additiva , Elica additiva
   Workbenches: PartDesign_Workbench/it
   Version: 0.19
   SeeAlso: PartDesign_SubtractiveHelix/it
---

# PartDesign AdditiveHelix/it



## Descrizione

Lo strumento **Elica additiva** crea un solido facendo scorrere uno schizzo selezionato o un oggetto 2D lungo un percorso elicoidale.

<img alt="" src=images/PartDesign_AdditiveHelix_example_overview.png  style="width:650px;">

*Il profilo (B), viene fatto scorrere attorno all\'asse (A) per produrre l\'elica solida (C)*



## Utilizzo

1.  Selezionare lo schizzo da trasformare in un\'elica. In alternativa è possibile utilizzare una faccia su un solido esistente.
2.  Premere il pulsante **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> [Elica additiva](PartDesign_AdditiveHelix/it.md)**.
3.  Impostare i parametri dell\'elica (vedere la sezione successiva).
4.  Esaminare l\'elica nella finestra di visualizzazione, per garantire che i parametri non risultino in un\'elica autointersecante.
5.  Cliccare su **OK**.



## Opzioni

Quando si crea un\'elica additiva, la finestra di dialogo **Parametri dell\'elica** offre diversi parametri che specificano come deve essere fatto scorrere lo schizzo.

![](images/PartDesign_AdditiveHelix_taskpanel.png )



### Asse

Questa opzione specifica l\'asse attorno al quale lo schizzo deve essere spostato.

-   **Asse normale allo schizzo**: seleziona la normale dello schizzo che attraversa l\'origine dello schizzo come asse. {{Version/it|0.20}}
-   **Asse verticale dello schizzo**: seleziona l\'asse verticale dello schizzo. Questa è l\'impostazione predefinita per le nuove eliche.
-   **Asse orizzontale dello schizzo**: seleziona l\'asse orizzontale dello schizzo.
-   **Linea di costruzione**: seleziona una linea di costruzione contenuta nello schizzo utilizzato dall\'Elica. L\'elenco a discesa conterrà una voce per ciascuna linea di costruzione. La prima linea di costruzione creata nello schizzo verrà etichettata *Linea di costruzione 1*.
-   **Asse (X/Y/Z) di Base**: seleziona l\'asse X, Y o Z dell\'Origine del Corpo;
-   **Seleziona riferimento\...**: consente la selezione nella vista 3D di un bordo sul Corpo, o di una [linea di riferimento](PartDesign_Line/it.md).



### Modalità

Questo indica quali parametri verranno utilizzati per definire l\'elica. Le scelte sono:

-   **Passo-Altezza-Angolo**: definisce tramite il passo e l\'altezza complessiva
-   **Passo-Numero giri-Angolo**: definisce tramite il passo e il numero di giri
-   **Altezza-Numero giri-Angolo**: definisce tramite l\'altezza totale e il numero di giri
-   **Altezza-Numero giri-Crescita** {{Version/it|0.20}}: definizione tramite l\'altezza totale, il numero di giri e la crescita del raggio dell\'elica. Quindi un\'altezza pari a zero porta ad un percorso a forma di spirale. Un\'altezza e una crescita pari a zero creano una figura a forma di cerchio.



### Passo

La distanza tra le spire dell\'elica.



### Altezza

La lunghezza dell\'elica (centro-centro).



### Numero giri 

Il numero di giri dell\'elica. Definiti come Altezza/Passo



### Angolo cono 

Angolo del cono che forma un avvolgimento attorno all\'elica. Intervallo consentito: \[-89°, +89°\].



### Sinistrorsa

Se selezionato, la direzione di rotazione dell\'elica viene invertita da quella predefinita in senso orario a quella antioraria.



### Invertita

Se selezionato, la direzione dell\'asse dell\'elica viene invertita rispetto a quella predefinita.



### Aggiorna la vista 

Se selezionato, l\'elica verrà mostrata nella vista e aggiornata automaticamente ad ogni modifica dei parametri.



## Preferenze

-   Un\'elica additiva che non interseca il corpo sarà visibile nell\'anteprima se **Strumenti → Modifica parametri... → BaseApp → Preferences → Mod → PartDesign → AdditiveHelixPreview** è impostato su `True`. Il valore predefinito per questa preferenza è `False`. {{Version/it|0.20}}



## Proprietà

-    **Pitch**: La distanza assiale tra due spire.

-    **Height**: La lunghezza totale dell\'elica (esclusa l\'estensione del profilo)

-    **Turns**: Il numero di giri (non è necessario che sia un numero intero)

-    **Left Handed**: Vedere [Sinistrorsa](#Sinistrorsa.md).

-    **Reversed**: Vedere [Invertita](#Invertita.md).

-    **Angle**: L\'inclinazione con cui il raggio dell\'elica aumenta lungo l\'asse. Intervallo consentito: \[-89°, +89°\].

-    **Reference axis**: L\'asse dell\'elica

-    **Mode**: La modalità di input dell\'elica (altezza e passo, spire e passo, altezza e giri)

-    **Outside**: Non utilizzato (utilizzato per l\'elica sottrattiva)

-    **Has Been Edited**: Se falso, lo strumento proporrà un valore iniziale per il passo in base al riquadro di delimitazione del profilo, in modo da evitare l\'autointersezione.

-    **Refine**: vero o falso. Se impostato su true, pulisce il solido dai bordi residui lasciati dalle lavorazioni. Per ulteriori dettagli, vedere [Affina forma](Part_RefineShape/it.md)..

-    **Profile**: Uno schizzo contenente un contorno chiuso o una faccia.

-    **Midplane**: Non usato.

-    **Up to face**: Non usato.

-    **Allow multiple face**: Non usato.



## Note

-   Un <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [ShapeBinder](PartDesign_ShapeBinder/it.md) non può essere utilizzato per il profilo.
-   Quando si utilizza un <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [SubShapeBinder](PartDesign_SubShapeBinder/it.md) per il profilo, la selezione del collegamento nella [Vista ad albero](Tree_view/it.md) fallirà, invece si deve selezionare la faccia del collegamento nella [vista 3D](3D_view/it.md).
-   Le eliche sono molto difficili da calcolare correttamente per il motore sottostante poiché le curve coinvolte spingono al limite la precisione in virgola mobile. Ciò significa che eseguire ulteriori operazioni su un\'elica come tentare operazioni booleane con un altro oggetto può essere molto sensibile a piccoli cambiamenti. Quando falliscono, spesso rompono il modello in modi sorprendenti. Per evitare ciò, si dovrebbe provare a fare in modo che le operazioni su un\'elica si sovrappongano chiaramente (interferiscano) o chiaramente non si sovrappongano. Le corrispondenze esatte in cui la superficie dell\'elica è perfettamente allineata con la superficie di un altro oggetto sono fragili. Un esempio di ciò è la filettatura attorno al cilindro del bullone. Potrebbe anche funzionare inizialmente, per poi rompersi in seguito quando gli oggetti vengono spostati leggermente.



## Esempi

![Esempio di elica che utilizza una [B-spline](images/Sketcher_CreateBSpline/it.md) nello schizzo](PartDesign_AdditiveHelix_example_bspline.png )

![Esempio di elica in cui l\'asse dell\'elica è normale al piano dello schizzo con conseguente effetto \"Pad con torsione\".](images/PartDesign_AdditiveHelix_example_twisting_pad.png )





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveHelix/it
