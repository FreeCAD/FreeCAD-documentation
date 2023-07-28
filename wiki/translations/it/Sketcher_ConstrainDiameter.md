---
- GuiCommand:/it
   Name:Sketcher_ConstrainDiameter   Name/it:Diametro
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   MenuLocation:Sketch → Vincoli → Diametro
   SeeAlso:[Distanza](Sketcher_ConstrainDistance/it.md), [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md), [Distanza verticale](Sketcher_ConstrainDistanceY/it.md)
---

# Sketcher ConstrainDiameter/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo vincolo forza il valore del diametro di un cerchio o di un arco a un valore specifico. Se viene selezionato più di un cerchio o arco prima di lanciare il comando, un prompt chiede se tutti gli elementi selezionati devono condividere lo stesso diametro. Nel caso di una risposta affermativa, viene aggiunto un vincolo di diametro e un vincolo di <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [uguale lunghezza](Sketcher_ConstrainEqual/it.md) a tutti gli elementi. Se la risposta è negativa, vengono creati vincoli di diametro separati per ogni cerchio o arco ma con valori uguali che è possibile modificare separatamente dopo la creazione.


</div>




<div class="mw-translate-fuzzy">

## Utilizzo


</div>

1.  Selezionare uno o più cerchi o archi.
2.  Premere il pulsante **[<img src=images/Sketcher_ConstrainDiameter.svg style="width:16px"> Diametro**.
3.  Si apre una finestra di dialogo per modificare o confermare il valore. Premere **OK** per confermare. Se sono stati selezionati più cerchi o archi, tutti i vincoli adottano questo valore. Per modificare i loro valori separatamente fare doppio clic sull\'etichetta della dimensione nella vista 3D; oppure nell\'elenco dei Vincoli, fare doppio clic sul vincolo o fare clic con il tasto destro e selezionare **Cambia valore**.
4.  L\'etichetta e la linea della quota possono essere spostate e ruotate nella vista 3D facendo clic sul valore e trascinando il mouse tenendo premuto il pulsante sinistro.

**Nota:** lo strumento vincolo può anche essere avviato senza selezione preliminare. Di default il comando è in modalità continua per creare nuovi vincoli; premere una volta il tasto destro del mouse o **Esc** per uscire dal comando.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `ArcOrCircle`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDiameter/it
