---
 GuiCommand:
   Name: Sketcher ConstrainLock
   Name/it: Sketcher Vincolo fissa
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo fissa
   Workbenches: Sketcher_Workbench/it
   Shortcut: **K** **L**
   SeeAlso: Sketcher_ConstrainBlock/it
---

# Sketcher ConstrainLock/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Sketcher Vincolo fissa](Sketcher_ConstrainLock/it.md) applica i vincoli [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md) e [Distanza verticale](Sketcher_ConstrainDistanceY/it.md) ai punti. Se viene selezionato un singolo punto, i vincoli fanno riferimento all\'origine dello schizzo. Se vengono selezionati due o più punti, i vincoli fanno riferimento all\'ultimo punto della selezione.



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](Sketcher_Preferences/it#General.md) **Vincoli dimensionali** è impostata su {{Value|Strumento singolo}} (predefinito): premere la freccia giù a destra del pulsante **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare il pulsante **<img src="images/Sketcher_ConstrainLock.svg" width=16px> Vincolo fissa** dal menu a discesa.

    -   Se questa preferenza ha un valore diverso (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/Sketcher_ConstrainLock.svg" width=16px> [Vincolo fissa](Sketcher_ConstrainLock/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Vincolo fissa** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [3D view](3D_view/it.md) e selezionare l\'opzione **Dimensione → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Vincolo fissa** dall\'elenco menu contestuale.

    -   Usare la scorciatoia da tastiera: **K** quindi **L**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Selezionare un singolo punto.
5.  Vengono aggiunti due vincoli.
6.  Facoltativamente, continuare a creare vincoli.
7.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Selezionare uno o più punti.
2.  Richiamare lo strumento come spiegato sopra.
3.  A seconda della selezione vengono aggiunti due o più vincoli.



## Note

-   Non esiste una richiesta automatica per modificare i valori dei vincoli. Se richiesti, i valori possono essere [modificati manualmente](Sketcher_Workbench/it#Edit_constraints.md).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/it
