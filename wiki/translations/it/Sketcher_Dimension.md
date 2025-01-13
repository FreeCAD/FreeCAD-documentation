---
 GuiCommand:
   Name:  Sketcher Dimension
   Name/it:  Sketcher Dimensione
   MenuLocation: Schizzo , Vincoli Sketcher , Dimensione
   Workbenches: Sketcher_Workbench/it
   Shortcut: **D**
   Version: 1.0
---

# Sketcher Dimension/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_Dimension.svg  style="width:24px;"> [Sketcher Dimensione](Sketcher_Dimension/it.md) è lo strumento di vincolo sensibile al contesto dell\'ambiente Sketcher. In base alla selezione attuale, offre vincoli dimensionali adeguati, ma anche vincoli geometrici.



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

1.  Facoltativamente selezionare uno o più elementi (bordi o punti). I bordi [B-spline](Sketcher_Workbench/it#Sketcher_CompCreateBSpline.md) non sono attualmente supportati.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Se la [preferenza](Sketcher_Preferences/it#General.md) **Vincolo dimensionale** è impostata su {{Value|Entrambi}} o {{Value|Strumento singolo}} (predefinito): premere il pulsante **<img src="images/Sketcher_Dimension.svg" width=16px> [Dimensione](Sketcher_Dimension/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_Dimension.svg" width=16px> Dimensione** dal menu.
    -   Fare clic con il pulsante destro del mouse su [Vista 3D](3D_view/it.md) e selezionare l\'opzione **Dimensione → <img src="images/Sketcher_Dimension.svg" width=16px> Dimensione** dal menu contestuale.
    -   Se c\'è una selezione: fare clic con il pulsante destro del mouse nella vista 3D e selezionare l\'opzione **<img src="images/Sketcher_Dimension.svg" width=16px> Dimensione** dal menu contestuale.
    -   Usare la scorciatoia da tastiera: **D**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Se non si ha ancora selezionato un elemento: selezionane uno.
5.  A seconda dell\'elemento/i selezionato/i viene proposto un vincolo.
6.  Facoltativamente selezionare un elemento aggiuntivo.
7.  Facoltativamente deselezionare un elemento facendo nuovamente clic su di esso.
8.  Il vincolo proposto viene aggiornato dopo ogni modifica della selezione.
9.  Facoltativamente, premere il tasto **M** una o più volte per scorrere gli altri vincoli disponibili, se presenti.
10. Se viene proposto un vincolo geometrico, gli elementi selezionati potrebbero cambiare dando un\'anteprima del risultato.
11. Effettuare una delle seguenti operazioni:
    -   Fare clic in un\'area vuota nella [Vista 3D](3D_view/it.md) per confermare:
        1.  Se viene creato un vincolo dimensionale, il punto cliccato ne determina la posizione. Per una quota lineare, il punto su cui si fa clic ne determina anche il tipo: <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:16px;"> [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md), <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:16px;"> [Distanza verticale](Sketcher_ConstrainDistanceY/it.md) o <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:16px;"> [Distanza](Sketcher_ConstrainDistance/it.md).
        2.  Se viene creato un [vincolo dimensionale guida](Sketcher_ToggleDrivingConstraint/it.md), a seconda delle [preferenze](Sketcher_Preferences/it#Display.md), si apre una finestra di dialogo per [modificarne il valore](Sketcher_Workbench/it#Edit_constraints.md).
        3.  Viene aggiunto un vincolo.
        4.  Questo strumento viene sempre eseguito in modalità continua: facoltativamente continuare a creare vincoli.
    -   Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Dimension/it
