---
 GuiCommand:
   Name: Sketcher ConstrainDistanceX
   Name/it: Sketcher Vincolo distanza orizzontale
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo distanza orizzontale
   Workbenches: Sketcher_Workbench/it
   Shortcut: **L**
   SeeAlso: Sketcher_ConstrainDistanceY/it, Sketcher_ConstrainDistance/it
---

# Sketcher ConstrainDistanceX/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Sketcher Vincolo distanza orizzontale](Sketcher_ConstrainDistanceX/it.md) fissa la distanza orizzontale tra due punti o gli estremi di una linea. Se viene preselezionato un punto singolo, la distanza è relativa all\'origine dello schizzo.

![](images/Constraint_H_Distance.png )



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](Sketcher_Preferences/it#General.md) **Vincoli dimensionali** è impostata su {{Value|Strumento singolo}} (predefinito): premere la freccia giù a destra del Pulsante **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare il pulsante **<img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Vincolo distanza orizzontale** dal menu a discesa.

    -   Se questa preferenza ha un valore diverso (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> [Vincolo distanza orizzontale](Sketcher_ConstrainDistanceX/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Vincolo distanza orizzontale** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **Dimensione → <img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Vincolo distanza orizzontale** dal menu contestuale.

    -   Usare la scorciatoia da tastiera: **L**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Effettuare una delle seguenti operazioni:
    -   Selezionare due punti (uno dei quali può essere l\'origine).
    -   Selezionare una singola linea.
5.  Se viene creato un [vincolo dimensionale guida](Sketcher_ToggleDrivingConstraint/it.md), a seconda delle [preferenze](Sketcher_Preferences/it#Display.md), si apre una finestra di dialogo per [modificarne il valore](Sketcher_Workbench/it#Edit_constraints.md).
6.  Viene aggiunto un vincolo.
7.  Facoltativamente, continuare a creare vincoli.
8.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



### Modalità di esecuzione una sola volta 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare uno o due punti.
    -   Selezionare una singola linea.
2.  Richiamare lo strumento come spiegato sopra.
3.  Facoltativamente [modificare il valore del vincolo](Sketcher_Workbench/it#Edit_constraints.md).
4.  Viene aggiunto un vincolo.



## Script

Distanza dall\'origine:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distanza tra due vertici:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Tratto orizzontale della linea (la GUI consente di selezionare il bordo stesso, ma è solo una scorciatoia per utilizzare le due estremità della stessa linea):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, ` PuntoOfEdge1`, ` PointOfEdge2` e `Line` e contiene ulteriori esempi su come creare vincoli da script Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceX/it
