---
 GuiCommand:
   Name: Sketcher ConstrainBlock
   Name/it: Sketcher Vincolo blocca
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo blocca
   Workbenches: Sketcher_Workbench/it
   Shortcut: **K** **B**
   Version: 0.17
   SeeAlso: Sketcher_ConstrainLock/it
---

# Sketcher ConstrainBlock/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;"> [Sketcher Vincolo blocca](Sketcher_ConstrainBlock/it.md) blocca i bordi in posizione con un singolo vincolo. È destinato principalmente alle [B-spline](Sketcher_CreateBSpline/it.md), che altrimenti possono essere difficile da vincolare completamente.

Il vincolo blocca influisce solo sulle parti liberamente mobili di un bordo. I bordi bloccati possono avere altri vincoli e l\'applicazione di vincoli aggiuntivi a un bordo bloccato può modificarlo.



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_ConstrainBlock.svg" width=16px> [Vincolo blocca](Sketcher_ConstrainBlock/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainBlock.svg" width=16px> Vincolo blocca** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **Vincolo → <img src="images/Sketcher_ConstrainBlock.svg" width=16px> Vincolo blocca** dall\'elenco menu contestuale.

    -   Usare la scorciatoia da tastiera: **K** quindi **B**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Selezionare un singolo bordo.
5.  Viene aggiunto un vincolo.
6.  Facoltativamente, continuare a creare vincoli.
7.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Selezionare uno o più bordi.
2.  Richiamare lo strumento come spiegato sopra o con la seguente opzione aggiuntiva:
    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [3D view](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_ConstrainBlock.svg" width=16px> Vincolo blocca** dal menu contestuale .
3.  A seconda della selezione vengono aggiunti uno o più vincoli.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `Edge` e contiene ulteriori esempi su come creare vincoli da script Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/it
