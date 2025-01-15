---
 GuiCommand:
   Name: Sketcher ConstrainHorVer
   Name/it: Sketcher Vincolo orizzontale/verticale
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo orizzontale/verticale
   Workbenches: Sketcher_Workbench/it
   Shortcut: **A**
   Version: 1.0
   SeeAlso: Sketcher_ConstrainHorizontal/it, Sketcher_ConstrainVertical/it
---

# Sketcher ConstrainHorVer/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:24px;"> [Sketcher Vincolo orizzontale/verticale](Sketcher_ConstrainHorVer/it.md) vincola le linee o le coppie di punti ad essere orizzontali (parallele all\'asse orizzontale dello schizzo) o verticali, a seconda di quale sia il più vicino all\'allineamento corrente .

Questo strumento combina gli strumenti [Sketcher Vincolo orizzontale](Sketcher_ConstrainHorizontal/it.md) e [Sketcher Vincolo verticale](Sketcher_ConstrainVertical/it.md).



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Se la [preferenza](Sketcher_Preferences/it#General.md) **Strumento automatico per orizzontale/verticale** è selezionata (predefinito): premere il pulsante **<img src="images/Sketcher_ConstrainHorVer.svg" width=16px> [Vincolo orizzontale/verticale](Sketcher_ConstrainHorVer/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Vincolo orizzontale/verticale** dal menu.
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **Vincolo → <img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Vincolo orizzontale/verticale** dal menu contestuale.
    -   Usare la scorciatoia da tastiera: **A**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Effettuare una delle seguenti operazioni:
    -   Selezionare due punti.
    -   Selezionare una singola linea.
5.  Viene aggiunto un vincolo.
6.  Facoltativamente, continuare a creare vincoli.
7.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare due o più punti (l\'ordine di selezione può essere rilevante vedere [Note](#Note.md)).
    -   Selezionare una o più linee. I punti possono essere inclusi nella selezione, ma verranno ignorati.
2.  Richiamare lo strumento come spiegato sopra o con la seguente opzione aggiuntiva:
    -   Fare clic con il pulsante destro del mouse nella [3D view](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Vincolo orizzontale/verticale** dal menu contestuale.
3.  A seconda della selezione vengono aggiunti uno o più vincoli.



## Note

-   Vengono elaborati più di 2 punti nell\'ordine di selezione, una coppia alla volta. Il 1° punto è accoppiato con il 2°. Quando sono vincolati, il 2° punto può spostarsi. La nuova posizione del 2° punto determina quale vincolo viene applicato quando il 2° e il 3° punto vengono vincolati, ecc.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorVer/it
