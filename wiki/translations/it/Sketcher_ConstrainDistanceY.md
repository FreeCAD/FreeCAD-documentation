---
 GuiCommand:
   Name: Sketcher ConstrainDistanceY
   Name/it: Sketcher Vincolo distanza verticale
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo distanza verticale
   Workbenches: Sketcher_Workbench/it
   Shortcut: **I**
   SeeAlso: Sketcher_ConstrainDistanceX/it, Sketcher_ConstrainDistance/it
---

# Sketcher ConstrainDistanceY/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Sketcher Vincolo distanza verticale](Sketcher_ConstrainDistanceY/it.md) fissa la distanza verticale tra due punti o gli estremi di una linea. Se viene preselezionato un punto singolo, la distanza è relativa all\'origine dello schizzo.

![](images/Sketcher_ConstraintDistanceY_example.png )



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](Sketcher_Preferences/it#General.md) **Vincoli dimensionali** è impostata su {{Value|Strumento singolo}} (predefinito): premere la freccia giù a destra del Pulsante **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare il pulsante **<img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Vincolo distanza verticale** dal menu a discesa.

    -   Se questa preferenza ha un valore diverso (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> [Vincolo distanza verticale](Sketcher_ConstrainDistanceY/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Vincolo distanza verticale** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **Dimensione → <img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Vincolo distanza verticale** dal menu contestuale.

    -   Usare la scorciatoia da tastiera: **I**.
3.  Per ulteriori passaggi vedere [Sketcher Vincolo distanza orizzontale](Sketcher_ConstrainDistanceX/it#Continue_mode.md)



### Modalità di esecuzione una sola volta 

Vedere [Sketcher Vincolo distanza orizzontale](Sketcher_ConstrainDistanceX/it#Run-once_mode.md).



## Script

Distanza dall\'origine:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distanza tra due vertici:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Tratto verticale della linea (la GUI consente di selezionare il bordo stesso, ma è solo una scorciatoia per utilizzare le due estremità della stessa linea):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, ` PuntoOfEdge1`, ` PointOfEdge2` e `Line` e contiene ulteriori esempi su come creare vincoli da script Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceY/it
