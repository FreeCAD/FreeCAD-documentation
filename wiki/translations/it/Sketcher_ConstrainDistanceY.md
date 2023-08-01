---
- GuiCommand:/it
   Name:Sketcher ConstrainDistanceY
   Name/it:Distanza Verticale   Workbenches:[Sketcher](Sketcher_Workbench/‭it.md)
   MenuLocation:Sketch → Vincoli → Distanza verticale
   Shortcut:Shift+V
   SeeAlso:[Distanza Orizzontale](Sketcher_ConstrainDistanceX/it.md), [Distanza](Sketcher_ConstrainDistance/it.md)
---

# Sketcher ConstrainDistanceY/it


</div>



## Descrizione

Fissa una distanza verticale tra due punti. È applicabile tra tutti i punti dello schizzo. Quando viene selezionato un solo punto la distanza è riferita all\'origine.

![](images/Sketcher_ConstraintDistanceY_example.png )



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare due punti o una linea
2.  Richiamare il comando in uno di questi modi:
    -   Cliccare sull\'icona **[<img src=images/Sketcher_ConstrainDistanceY.png style="width:24px"> '''Distanza verticale'''** della barra degli strumenti.
    -   Usare la scorciatoia da tastiera **Maiusc** + **V**.
    -   Usare la voce **Sketch → Vincoli → Distanza verticale** dal menu principale.
3.  Si apre una finestra di dialogo per modificare o confermare il valore. Premere **OK** per confermare.


</div>


<div class="mw-translate-fuzzy">

**Nota:** lo strumento di vincolo può essere avviato anche senza selezione precedente, ma richiede la selezione di due punti o una linea. Per impostare la distanza dall\'origine, è necessario selezionare anche il punto di origine dello schizzo. Di default il comando è in modalità continua per creare nuovi vincoli; per uscire dal comando premere il tasto destro del mouse o una volta il tasto **ESC**.


</div>

## Scripting

Distance from origin:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distance between two vertices:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Vertical span of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, ` PointOfEdge1`, ` PointOfEdge2` and `Line`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceY/it
