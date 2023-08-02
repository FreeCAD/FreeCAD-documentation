# Sketcher CreatePolyline/it
---
- GuiCommand:   Name: Sketcher CreatePolyline   Name/it: Polilinea   Workbenches: Sketcher Workbench/it   Sketcher---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento funziona come lo strumento [Linea](Sketcher_CreateLine/it.md) di Schizzo, ma crea una successione di **segmenti** e di **archi** collegati ai loro estremi. Le linee e gli archi si alternano con il tasto **M**.

Quando si avvia lo strumento, il puntatore del mouse assume la forma di croce bianca accompagnata dall\'icona rossa di polilinea. Accanto al puntatore sono visualizzate, in blu, le coordinate della sua posizione, aggiornate in tempo reale.


</div>

![](images/Sketcher_PolylineExample1.png )


<div class="mw-translate-fuzzy">

*La polilinea inizia con una linea, continua con un arco tangente, poi un arco perpendicolare quindi una linea tangente*


</div>



## Utilizzo

La Polilinea inizia sempre con un segmento di linea retta: fare clic - spostare il mouse - fare clic. Muovi di nuovo il mouse. Dopo aver posizionato il primo segmento di linea, lo strumento polilinea Sketcher ha più modalità che possono essere attivate con il tasto **M**. Ad esempio è possibile disegnare archi tangenti o perpendicolari seguendo una linea o un segmento di arco. Premendo ripetutamente il tasto **M** si passa da queste diverse modalità:

1.  Premere sul tasto **M**: il nuovo segmento è una linea che è perpendicolare al segmento precedente
2.  Premere di nuovo sul tasto **M**: il nuovo segmento è una linea che è tangente al segmento precedente
3.  Premere di nuovo sul tasto **M**: il nuovo segmento è un arco che è tangente al segmento precedente
4.  Premere di nuovo sul tasto **M**: il nuovo segmento è un arco che è perpendicolare (a sinistra) al segmento precedente
5.  Premere di nuovo sul tasto **M**: il nuovo segmento è un arco che è perpendicolare (a destra) al segmento precedente
6.  Premere di nuovo sul tasto **M**: si ritorna allo stato iniziale; la linea è collegata solo con una coincidenza al segmento precedente.


<div class="mw-translate-fuzzy">

-   v0.18 e superiore Mentre ci si trova in una qualsiasi delle modalità arco, tenendo premuto il tasto **Ctrl** (MacOS: tasto **CMD**) e spostando il cursore, l\'arco si blocca di incrementi di 45 gradi, rispetto al segmento della polilinea precedentemente creato (v0.18).
-   Selezionare i punti su un\'area vuota della vista 3D, o su un oggetto esistente. I vincoli automatici (auto constraints) si attivano nella scheda **Azioni → Modifica controlli → Autovincoli** del pannello **Vista combinata**.
-   Premere il tasto **Esc**, o cliccare sul tasto destro del mouse prima di chiudere la polilinea in un anello termina la polilinea corrente e si può continuare con una nuova. Premendo **Esc** o facendo clic con il pulsante destro del mouse dopo aver chiuso la polilinea in un anello termina la funzione polilinea.
-   Premendo **Esc** o facendo clic con il pulsante destro del mouse \"dopo\" la chiusura della polilinea su un loop termina la funzione polilinea.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePolyline/it
