# Sketcher ConstrainRadius/it
---
- GuiCommand:/it   Name:Sketcher_ConstrainRadius   Name/it:Raggio   Workbenches:[MenuLocation:Schizzo → Vincoli → Raggio   SeeAlso:[[Sketcher ConstrainDistance/it|Distanza orizzontale](Sketcher_Workbench/it___Schizzo]].md), [Distanza verticale](Sketcher_ConstrainDistanceY/it.md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo vincolo forza il valore del raggio di un cerchio o di un arco a un valore specifico. Se viene selezionato più di un cerchio o arco prima di avviare il comando, un prompt chiede se tutti gli elementi selezionati devono condividere lo stesso raggio. Nel caso di una risposta affermativa, viene aggiunto un vincolo di raggio e un vincolo di [uguale lunghezza](Sketcher_ConstrainEqual/it.md) a tutti gli elementi. Se la risposta è negativa, vengono creati vincoli di raggio separati per ogni cerchio o arco ma con valori uguali che è possibile modificare singolarmente dopo la creazione.


</div>

![](images/Sketcher_ConstrainRadius_example.png )

## Utilizzo

1.  Selezionare uno o più cerchi o archi.
2.  Premere il pulsante **<img src=images/Sketcher_ConstrainRadius.svg style="width:16px"> Raggio**.
3.  Si apre una finestra di dialogo per modificare o confermare il valore. Premere **OK** per confermare. Se sono stati selezionati più cerchi o archi, tutti i vincoli adottano questo valore. Modificare i loro valori separatamente facendo doppio clic sull\'etichetta della dimensione nella vista 3D; oppure nell\'elenco dei Vincoli, fare doppio clic sul vincolo o fare clic con il tasto destro e selezionare **Cambia valore**.
4.  L\'etichetta e la linea della quota possono essere spostate e ruotate a piacere nella vista 3D facendo clic sul valore e trascinando il mouse tenendo premuto il tasto sinistro.

**Nota:** lo strumento vincolo può anche essere avviato senza selezione preliminare. Di default il comando èà in modalità continua per creare nuovi vincoli; premere una volta il tasto destro del mouse o **Esc** per uscire dal comando.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `ArcOrCircle`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/it
