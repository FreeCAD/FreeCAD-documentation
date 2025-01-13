---
 GuiCommand:
   Name: Sketcher ConstrainDistance
   Name/it: Sketcher Vincolo distanza
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo distanza
   Workbenches: Sketcher_Workbench/it
   Shortcut: **K** **D**
   SeeAlso: Sketcher_ConstrainDistanceX/iy, Sketcher_ConstrainDistanceY/it
---

# Sketcher ConstrainDistance/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> [Sketcher Vincolo distanza](Sketcher_ConstrainDistance/it.md) fissa la lunghezza di una linea, la distanza tra due punti, la distanza perpendicolare tra un punto e una linea; oppure, {{Version/it|0.21}}, la distanza tra i bordi di due cerchi o archi, o tra il bordo di un cerchio o arco e una linea; o, {{Version/it|1.0}}, la lunghezza di un arco.

![](images/Sketcher_ConstrainDistance_example.png )



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](Sketcher_Preferences/it#General.md) **Vincoli dimensionali** è impostata su {{Value|Strumento singolo}} (predefinito): premere la freccia giù a destra del pulsante **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare **<img src="images/Sketcher_ConstrainDistance.svg" width=16px> Vincolo distanza ** dal menu a discesa.

    -   Se questa preferenza ha un valore diverso (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/Sketcher_ConstrainDistance.svg" width=16px> [Vincolo distanza](Sketcher_ConstrainDistance/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → [<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> Vincolo distanza** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **Dimensione → <img src="images/Sketcher_ConstrainDistance.svg" width=16px> Vincolo distanza** dalla menu contestuale.

    -   Usare la scorciatoia da tastiera **K** quindi **D**.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Effettuare una delle seguenti operazioni:
    -   Selezionare una singola linea.
    -   Selezionare due punti.
    -   Selezionare un punto e una linea (in quest\'ordine).
5.  Se viene creato un [vincolo dimensionale guida](Sketcher_ToggleDrivingConstraint/it.md), a seconda delle [preferenze](Sketcher_Preferences/it#Display.md), si apre una finestra di dialogo per [modificarne il valore](Sketcher_Workbench/it#Edit_constraints.md).
6.  Viene aggiunto un vincolo.
7.  Facoltativamente, continuare a creare vincoli.
8.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli



### Modalità di esecuzione una sola volta 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare una singola linea.

    -   Selezionare due punti.

    -   Selezionare un punto e una linea (in qualsiasi ordine).

    -   Selezionare i bordi di due cerchi o archi.

    -   Selezionare il bordo di un cerchio o arco e una linea (idem).

    -   
        {{Version/it|1.0}}
        
        : Selezionare il bordo di un singolo arco.
2.  Richiamare lo strumento come spiegato sopra.
3.  Facoltativamente [modificare il valore del vincolo](Sketcher_Workbench/it#Edit_constraints.md).
4.  Viene aggiunto un vincolo.



## Note

-   Se applicabile, considerare l\'utilizzo dei vincoli [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md) o [Distanza verticale](Sketcher_ConstrainDistanceY/it.md). Sono più efficienti.



## Script

Distanza dall\'origine:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distanza tra due vertici:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Lunghezza della linea (la GUI consente di selezionare il bordo stesso, ma è solo una scorciatoia per utilizzare le due estremità della stessa linea):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Distanza dal punto (`Edge, PointOfEdge`) al punto perpendicolare sulla linea (`Line`):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, Line, 0, App.Units.Quantity('123.0 mm')))```

Distanza tra i bordi di due cerchi:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Circle1, 0, Circle2, 0, App.Units.Quantity('123.0 mm')))```

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, `PointOfEdge1`, `PointOfEdge2`, `Line`, `Circle1` e `Circle2` e contiene ulteriori esempi su come creare vincoli da script Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/it
