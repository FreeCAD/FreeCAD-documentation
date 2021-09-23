# Path Simulator/it
---
- GuiCommand:/it   Name:Path Simulator   Name/it:Simulatore   Workbenches:[MenuLocation:Path → Simulatore CAM   SeeAlso:[[Path_Inspect/it|Ispeziona](Path_Workbench/it___Path]].md) ---


</div>

## Descrizione

Questo strumento consente di simulare il percorso della lavorazione. Spazza i modelli 3D degli strumenti utilizzati in ciascuna operazione lungo i percorsi del codice G. Dove il pezzo e lo strumento si sovrappongono sottrae del materiale dal pezzo, e fornisce la visualizzazione della lavorazione. Ciò consente il rilevamento e l\'isolamento degli errori prima di eseguire il lavoro su una fresatrice.

![](images/Path-Simulation.gif )

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

1.  Premere il pulsante **<img src="images/Path_Simulator.png" width=16px> [Simulatore CAM](Path_Simulator/it.md)
**
2.  Deselezionare tutte le Operazioni che non devono essere simulate
3.  Regolare le impostazioni di velocità e precisione.
4.  Selezionare la lavorazione da simulare dal menu a discesa.
5.  Premere il pulsante Riproduci per riprodurre un\'animazione delle operazioni.
    Premere il pulsante Avanti veloce per velocizzare i percorsi complicati.
6.  Per risolvere tagli o movimenti specifici sono fornite le funzionalità Pausa e Singolo-passo.
7.  Facendo clic sul pulsante Annulla si rimuove il pezzo creato per la simulazione. Facendo clic su Ok questo oggetto viene mantenuto nella lavorazione.


</div>


<div class="mw-translate-fuzzy">

## Proprietà


</div>

-    **Playback Speed**: La velocità di riproduzione della simulazione, in linee di codice G al secondo

-    **Accuracy**: La precisione della simulazione espressa in percentuale che indica la deviazione delle simulazioni dalla lavorazione. Per la simulazione interattiva, riducendo la precisione a 0,3 funziona molto più velocemente.

-    **Job**: La lavorazione usata come base della simulazione

-    **Operation List**: L\'elenco delle operazioni selezionate per l\'inclusione nella simulazione.





{{Path_Tools_navi

}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path Simulator/it
