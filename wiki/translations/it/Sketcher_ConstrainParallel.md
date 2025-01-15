---
 GuiCommand:
   Name: Sketcher ConstrainParallel
   Name/it: Sketcher Vincolo parallelo
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo parallelo
   Workbenches: Sketcher_Workbench/it
   Shortcut: **P**
   SeeAlso: 
---

# Sketcher ConstrainParallel/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> [Sketcher Vincolo parallelo](Sketcher_ConstrainParallel/it.md) vincola le linee ad essere parallele.



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_ConstrainParallel.svg" width=16px> [Vincolo parallelo](Sketcher_ConstrainParallel/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainParallel.svg" width=16px> Vincolo parallelo** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **Vincolo → <img src="images/Sketcher_ConstrainParallel.svg" width=16px> Vincolo parallelo** dall\'elenco menu contestuale.

    -   Usare la scorciatoia da tastiera: **P**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Selezionare due linee.
5.  Viene aggiunto un vincolo.
6.  Facoltativamente, continuare a creare vincoli.
7.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Selezionare due o più linee. {{Version/it|1.0}}: i punti possono essere inclusi nella selezione, ma verranno ignorati.
2.  Richiamare lo strumento come spiegato sopra o con la seguente opzione aggiuntiva:
    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_ConstrainParallel.svg" width=16px> Vincolo parallelo** dal menu contestuale .
3.  A seconda della selezione vengono aggiunti uno o più vincoli.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `Line1` e `Line2` e contiene ulteriori esempi su come creare vincoli da script Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/it
