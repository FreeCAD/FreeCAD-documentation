---
 GuiCommand:
   Name: Sketcher ConstrainHorizontal
   Name/it: Sketcher Vincolo orizzontale
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo orizzontale
   Workbenches: Sketcher_Workbench/it
   Shortcut: **H**
   SeeAlso: Sketcher_ConstrainHorVer/it, Sketcher_ConstrainVertical/it
---

# Sketcher ConstrainHorizontal/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [Sketcher Vincolo orizzontale](Sketcher_ConstrainHorizontal/it.md) vincola le linee o le coppie di punti ad essere orizzontali (parallele all\'asse orizzontale dello schizzo).


{{Version/it|1.0}}

: nella maggior parte dei casi è consigliabile utilizzare invece lo strumento combinato [Sketcher Vincolo orizzontale/verticale](Sketcher_ConstrainHorVer/it.md).



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](Sketcher_Preferences/it#General.md) **Strumento automatico per orizzontale/verticale** è selezionata (predefinito): premere la freccia giù a destra del pulsante **<img src="images/Sketcher_ConstrainHorVer.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare l\'opzione **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Vincolo orizzontale** dal menu a discesa.

    -   Se questa preferenza non è selezionata (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> [Vincolo orizzontale](Sketcher_ConstrainHorizontal/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Vincolo orizzontale** dal menu.

    -   Usare la scorciatoia da tastiera: **H**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Effettuare una delle seguenti operazioni:
    -   Selezionare due punti.
    -   Selezionare una singola riga.
5.  Viene aggiunto un vincolo.
6.  Facoltativamente, continuare a creare vincoli.
7.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare due o più punti.
    -   Selezionare una o più righe. I punti possono essere inclusi nella selezione, ma verranno ignorati.
2.  Richiamare lo strumento come spiegato sopra o con la seguente opzione aggiuntiva:
    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [3D view](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Vincolo orizzontale** dal menu contestuale .
3.  A seconda della selezione vengono aggiunti uno o più vincoli.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `Line` e contiene ulteriori esempi su come creare vincoli da script Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/it
