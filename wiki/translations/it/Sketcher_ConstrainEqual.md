---
 GuiCommand:
   Name: Sketcher ConstrainEqual
   Name/it: Sketcher Vincolo uguale
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo uguale
   Workbenches: Sketcher_Workbench/it
   Shortcut: **E**
   SeeAlso: 
---

# Sketcher ConstrainEqual/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> [Sketcher Vincolo uguale](Sketcher_ConstrainEqual.md) vincola i bordi ad avere la stessa lunghezza (linee) o curvatura (altri bordi eccetto [B-spline](Sketcher_CreateBSpline/it.md)). I bordi selezionati devono avere la stessa tipologia. Cerchi e archi circolari sono dello stesso tipo (i loro raggi sono resi uguali), così come lo sono le ellissi e gli archi ellittici (i loro raggi maggiore e minore sono resi uguali).



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> [Vincolo uguale](Sketcher_ConstrainEqual/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> Vincolo uguale** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **Vincolo → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> Vincolo uguale** dall\'elenco menu contestuale.

    -   Usare la scorciatoia da tastiera: **E**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Selezionare due bordi dello stesso tipo.
5.  Viene aggiunto un vincolo.
6.  Facoltativamente, continuare a creare vincoli.
7.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Selezionare due o più bordi dello stesso tipo.
2.  Richiamare lo strumento come spiegato sopra o con la seguente opzione aggiuntiva:
    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [3D view](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> Vincolo uguale** dal menu contestuale .
3.  A seconda della selezione vengono aggiunti uno o più vincoli.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `Edge1` e `Edge2` e contiene ulteriori esempi su come creare vincoli da script Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/it
