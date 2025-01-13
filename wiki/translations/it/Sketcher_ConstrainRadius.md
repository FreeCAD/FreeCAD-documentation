---
 GuiCommand:
   Name: Sketcher ConstrainRadius
   Name/it: Sketcher Vincolo raggio
   MenuLocation: Schizzo , Vincoli Sketcher , Vincolo raggio
   Workbenches: Sketcher_Workbench/it
   Shortcut: **K** **R**
   SeeAlso: Sketcher_ConstrainRadiam/it, Sketcher_ConstrainDiameter/it
---

# Sketcher ConstrainRadius/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;"> [Sketcher Vincolo raggio](Sketcher_ConstrainRadius/it.md) fissa il raggio di cerchi, archi e [Cerchi di peso B-spline](Sketcher_CreateBSpline/it#Notes.md).

![](images/Sketcher_ConstrainRadius_example.png )



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).



### [Modalità continua](Sketcher_Workbench/it#Continue_modes.md) 

1.  Assicurarsi che non ci sia alcuna selezione.
2.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](Sketcher_Preferences/it#General.md) **Vincoli dimensionali** è impostata su {{Value|Strumento singolo}} (predefinito): premere la freccia giù a destra del pulsante **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare il pulsante **[[Image:Sketcher_ConstrainRadius.svg|16px] ] Vincolo raggio** dal menu a discesa.

    -   Se questa preferenza ha un valore diverso (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/Sketcher_ConstrainRadius.svg" width=16px> [Vincolo raggio](Sketcher_ConstrainRadius/it.md)**.

    -   Selezionare l\'opzione **Schizzo → Vincoli Sketcher → <img src="images/Sketcher_ConstrainRadius.svg" width=16px> Vincolo raggio** dal menu.

    -   
        {{Version/it|1.0}}
        
        : fare clic con il pulsante destro del mouse nella [3D view](3D_view/it.md) e selezionare l\'opzione **Dimensione → <img src="images/Sketcher_ConstrainRadius.svg" width=16px> Vincolo raggio** dall\'elenco menu contestuale.

    -   Usare la scorciatoia da tastiera: **K** quindi **R**.
3.  Per ulteriori passaggi vedere [Sketcher Vincolo raggio/diametro](Sketcher_ConstrainRadiam/it#Continue_mode.md).



### Modalità di esecuzione una sola volta 

Vedere [Sketcher Vincolo raggio/diametro](Sketcher_ConstrainRadiam/it#Run-once_mode.md).



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

La pagina [Sketcher scripting](Sketcher_scripting/it.md) spiega i valori che possono essere utilizzati per `ArcOrCircle` e contiene ulteriori esempi su come creare vincoli da script Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/it
