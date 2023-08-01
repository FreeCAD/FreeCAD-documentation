# Navigation Cube/it
{{docnav/it
|[Metodi di selezione](Selection_methods/it.md)
|[Struttura del documento](Document_structure/it.md)
}}






## Introduzione

Il **Cubo di Navigazione** dà un\'informazione visiva riguardo l\'orientamento della telecamera nella [vista 3D](3D_view/it.md) attuale e può essere utilizzato per cambiarla. Di default è visibile e si trova nell\'angolo in alto a destra della vista.

![](images/Navigation_Cube_Example.png )

Il Cubo di Navigazione consiste in un certo numero di parti:

-   Il [cubo principale](#Cubo_Principale.md)
-   Sei [freccie direzionali](#Frecce_Direzionali.md)
-   Il [bottone inversione vista](#Bottone_Inversione_Vista.md) (in alto a destra) {{Version/it|0.20}}
-   Il [menu mini-cubo](#Menu_Mini-Cubo.md) (in basso a destra)
-   Gli indicatori degli assi X, Y e Z

Tutte le parti, eccetto gli indicatori degli assi, possono essere cliccate.



## Utilizzo



### Cubo Principale 

Il cubo principale ha 26 facce: 6 facce principali quadrate, 12 facce di bordo rettangolari ({{Version/it|0.20}}) e 8 facce d\'angolo triangolari. Facendo clic su uno di essi si riorienterà la telecamera in modo che la sua direzione sia perpendicolare alla faccia selezionata.



### Frecce Direzionali 

Ci sono sei frecce direzionali: quattro freccie con punte triangolari e due frecce curve. Facendo clic su una delle frecce triangolari, la [Vista 3D](3D_view/it.md) ruota attorno a una linea perpendicolare alla direzione della freccia. Facendo clic su una freccia curva, la [Vista 3D](3D_view/it.md) ruota attorno alla direzione della vista.



### Bottone Inversione Vista 

Facendo clic sul pulsante rotondo nell\'angolo in alto a destra del Cubo di navigazione, la [Vista 3D](3D_view/it.md) ruoterà di 180 gradi attorno all\'asse verticale della vista.



### Menu Mini-Cubo 

Facendo clic sul cubo nell\'angolo inferiore destro del Cubo di Navigazione viene visualizzato un menu con le seguenti opzioni:

-    **<img src="images/Std_OrthographicCamera.svg" width=16px>[Vista ortografica](Std_OrthographicCamera/it.md)**: passa a una vista ortogonale.

-    **<img src="images/Std_PerspectiveCamera.svg" width=16px>[Vista in prospettiva](Std_PerspectiveCamera/it.md)**: passa a una vista prospettica.

-    **<img src="images/Std_ViewIsometric.svg" width=16px>[Isometrica](Std_ViewIsometric/it.md)**: passa a una vista isometrica.

-    **<img src="images/Std_ViewFitAll.svg" width=16px> [Visualizza tutto](Std_ViewFitAll.md)**: esegue lo zoom e lo spostamento della telecamera in modo che tutti gli oggetti visibili rientrino nella vista.

-    **Cubo di navigazione mobile**: se questa casella di controllo ({{Version/it|0.21}}) è selezionata, l\'intero Cubo di navigazione può essere spostato tenendo premuto il pulsante sinistro del mouse in qualsiasi punto del cubo principale e trascinandolo. Questo ha lo scopo di spostare temporaneamente il cubo fuori ingombro. I [parametri avanzati](#Advanced_parameters.md) OffsetX e OffsetY possono essere usati per riposizionare permanentemente il cubo, vedi sotto.



## Personalizzazione



### Preferenze

Il Cubo di navigazione è controllato da diverse preferenze: **Modifica → Preferenze... → Visualizzazione → Navigazione → Cubo di navigazione**. Vedere [Impostare le Preferenze](Preferences_Editor/it#Navigazione.md).



### Parametri avanzati 

Alcuni parametri avanzati del Cubo di navigazione non possono essere modificati nell\'[Impostazione delle preferenze](Preferences_Editor/it#Navigazione.md). Questi parametri possono essere impostati manualmente in [Modifica parametri](Std_DlgParameter/it.md).

Per impostare manualmente i colori:

1.  Avviare <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Modifica parametri](Std_DlgParameter/it.md).
2.  Nel pannello a sinistra selezionare **Strumenti → Modifica parametri... → NaviCube**.
3.  Fare clic con il pulsante destro del mouse sul pannello a destra e selezionare **Nuovo elemento unsigned** dal menu contestuale.
4.  Inserire il nome di uno di questi colori:
    -   
        **BaseColor**
        
        : il colore di base di tutti gli elementi, il valore predefinito è {{Value|3806916544}} (hex: {{Value|e2e8efc0}}). Questo colore può essere impostato anche nell\'[Editor delle preferenze](Preferences_Editor/it#Navigazione.md). {{Version/it|0.21}}

    -   
        **EmphaseColor**
        
        : il colore del testo e delle linee, il default dipende dal **BaseColor**. È nero: {{Value|255}} (hex: {{Value|000000ff}}) o bianco: {{Value|4294967295}} (hex: {{Value|ffffffff}}). {{Version/it|0.21}}

    -   
        **HiliteColor**
        
        : il colore utilizzato per evidenziare le facce e i pulsanti, il valore predefinito è {{Value|2867003391}} (hex: {{Value|aae2ffff}}).
5.  Il valore del colore deve essere immesso come numero intero senza segno a 32 bit. Tradotto nel formato esadecimale questo numero intero ha la forma {{Value|RRGGBBAA}}. Dove {{Value|AA}} sta per il canale alfa (una misura della trasparenza), e le altre coppie di tre cifre stanno per rosso, verde e blu. Per convertire un valore esadecimale in un intero senza segno puoi usare la [Console Python](Python_console/it.md), inserire ad esempio {{Incode|int("323232ff", 16)}}.
6.  Facoltativamente si possono impostare più colori.
7.  Premere il pulsante **Chiudi**.

La tabella seguente elenca gli altri parametri avanzati del Cubo di navigazione che possono essere impostati in modo simile. Utilizzare le informazioni dalla colonna **Tipo** per creare un nuovo elemento corretto nel passaggio 3.

+++++
| Nome        | Descrizione                                                                                                                                                                       | Tipo    | Default |
+=============+===================================================================================================================================================================================+=========+=========+
| BorderWidth | La larghezza dei bordi del cubo e dei bordi attorno ai pulsanti in pixel.                                                                                                         | Float   | 1.1     |
+++++
| ChamferSize | Dimensione dei bordi e degli angoli come fattore dimensionale del cubo. I valori dovrebbero essere compresi tra 0,05 e 0,18.                                                      | Float   | 0.12    |
|             |                                                                                                                                                                                   |         |         |
|             |                                                                                                                                                                    |         |         |
|             | {{Version/it|0.21}}                                                                                                                                                               |         |         |
|             |                                                                                                                                                                                |         |         |
+++++
| FontStretch | La larghezza del carattere come percentuale della larghezza predefinita. Utilizzare 0 o 100 per la larghezza predefinita del carattere.                                           | Integer | 0       |
+++++
| FontWeight  | Il peso del carattere. Valori più alti rendono il carattere più grande. L\'effetto può dipendere dal carattere. Utilizzare 0 per lo spessore del carattere predefinito.\| Integer | 0       |         |
+++++
| FontZoom    | La dimensione delle etichette:                                                                                                                                                    | Float   | 0.3     |
|             |                                                                                                                                                                                   |         |         |
|             | -                                                                                                                                                                  |         |         |
|             |     {{Value|FontZoom &#61; 1.0}}                                                                                                                                                  |         |         |
|             |                                                                                                                                                                                |         |         |
|             |     : Rende le etichette il più grande possibile individualmente.                                                                                                                 |         |         |
|             |                                                                                                                                                                                   |         |         |
|             | -                                                                                                                                                                  |         |         |
|             |     {{Value|0.0 < FontZoom < 1.0}}                                                                                                                                                |         |         |
|             |                                                                                                                                                                                |         |         |
|             |     : Idem ma limita la dimensione massima del carattere.                                                                                                                         |         |         |
|             |                                                                                                                                                                                   |         |         |
|             | -                                                                                                                                                                  |         |         |
|             |     {{Value|FontZoom &#61; 0.0}}                                                                                                                                                  |         |         |
|             |                                                                                                                                                                                |         |         |
|             |     : Idem ma usa la stessa dimensione del carattere per tutti.                                                                                                                   |         |         |
|             |                                                                                                                                                                                   |         |         |
|             | -                                                                                                                                                                  |         |         |
|             |     {{Value|FontZoom < 0.0}}                                                                                                                                                      |         |         |
|             |                                                                                                                                                                                |         |         |
|             |     : Usa la stessa dimensione del carattere per tutti, ma ridimensionato.                                                                                                        |         |         |
|             |                                                                                                                                                                                   |         |         |
|             |                                                                                                                                                                    |         |         |
|             | {{Version/it|0.21}}                                                                                                                                                               |         |         |
|             |                                                                                                                                                                                |         |         |
+++++
| OffsetX     | L\'offset del cubo nella direzione X rispetto alla sua posizione d\'angolo in pixel.                                                                                              | Integer | 0       |
+++++
| OffsetY     | L\'offset del cubo nella direzione Y rispetto alla sua posizione d\'angolo in pixel.                                                                                              | Integer | 0       |
+++++
| ShowCS      | Alterna la visualizzazione del sistema di coordinate (gli indicatori degli assi X, Y e Z).                                                                                        | Boolean | true    |
+++++
| TextBottom  | Il testo sulla faccia inferiore del cubo. Il valore predefinito dovrebbe essere tradotto.                                                                                         | String  | BOTTOM  |
+++++
| TextFront   | Il testo sulla faccia anteriore del cubo. Idem.                                                                                                                                   | String  | FRONT   |
+++++
| TextLeft    | Il testo sulla faccia sinistra del cubo. Idem.                                                                                                                                    | String  | LEFT    |
+++++
| TextRear    | Il testo sulla faccia posteriore del cubo. Idem.                                                                                                                                  | String  | REAR    |
+++++
| TextRight   | Il testo sulla faccia destra del cubo. Idem.                                                                                                                                      | String  | RIGHT   |
+++++
| TextTop     | Il testo sulla faccia superiore del cubo. Idem.                                                                                                                                   | String  | TOP     |
+++++


{{docnav/it
|[Metodi di selezione](Selection_methods/it.md)
|[Struttura del documento](Document_structure/it.md)
}}



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/it
