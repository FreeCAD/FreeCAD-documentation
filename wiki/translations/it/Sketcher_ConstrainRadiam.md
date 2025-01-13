---
 GuiCommand:
   Name: Sketcher ConstrainRadiam
   Name/it: Sketcher Vincolo raggio/diametro automatico
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo raggio/diametro automatico
   Workbenches: Sketcher_Workbench/it
   Shortcut: **K** **S**
   Version: 0.20
   SeeAlso: Sketcher_ConstrainRadius/it, Sketcher_ConstrainDiameter/it
---

# Sketcher ConstrainRadiam/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:24px;"> [Sketcher Vincolo raggio/diametro automatico](Sketcher_ConstrainRadiam/it.md) fissa il raggio degli archi e [Cerchi di peso B-spline](Sketcher_CreateBSpline/it#Notes.md) e il diametro dei cerchi.



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](Sketcher_Preferences/it#General.md) **Vincoli dimensionali** è impostata su {{Value|Strumento singolo}} (predefinito): premere la freccia giù a destra del Pulsante **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare il pulsante **<img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Vincolo  raggio/diametro automatico** dal menu a discesa.

    -   Se questa preferenza ha un valore diverso (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/Sketcher_ConstrainRadiam.svg" width=16px> [Vincolo raggio/diametro automatico](Sketcher_ConstrainRadiam/it.md)**.

    -   Selezionare l\'opzione **Sketch → Vincoli Sketcher → <img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Vincolo raggio/diametro automatico** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [3D view](3D_view/it.md) e selezionare **Dimensione → <img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Vincolo raggio/diametro automatico** dal menu contestuale.

    -   Usare la scorciatoia da tastiera: **K** quindi **S**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Effettuare una delle seguenti operazioni:
    -   Selezionare il bordo di un cerchio o di un arco.
    -   Selezionare il bordo di un cerchio di peso B-spline.
5.  Se viene creato un [vincolo dimensionale guida](Sketcher_ToggleDrivingConstraint/it.md), a seconda delle [preferenze](Sketcher_Preferences/it#Display.md), si apre una finestra di dialogo per [modificarne il valore](Sketcher_Workbench/it#Edit_constraints.md).
6.  Viene aggiunto un vincolo.
7.  Facoltativamente, continuare a creare vincoli.
8.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare il bordo di uno o più cerchi o archi.
    -   Selezionare il bordo di uno o più cerchi di peso B-spline.
2.  Richiamare lo strumento come spiegato sopra.
3.  Facoltativamente [modificare il valore del vincolo](Sketcher_Workbench/it#Edit_constraints.md).
4.  A seconda della selezione vengono aggiunti uno o più vincoli, vedere [Note](#Note.md).



## Note

-   Se vengono creati [vincoli guida](Sketcher_ToggleDrivingConstraint/it.md) e sono stati preselezionati più elementi che non sono [geometria esterna](Sketcher_External/it.md), solo il primo di questi riceve un vincolo dimensionale, mentre tra il primo e gli altri vengono applicati [Vincoli uguale](Sketcher_ConstrainEqual/it.md).



## Script


```python
Sketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))
Sketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('246.0 mm')))
```

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `ArcOrCircle` e contiene ulteriori esempi su come creare vincoli da script Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadiam/it
