# Sketcher ConstrainLock/it
---
- GuiCommand:/it   Name:Sketcher ConstrainLock   Name/it:Blocca   Workbenches:[MenuLocation:PartDesign → Schizzo → Blocca   SeeAlso:[[Sketcher ConstrainBlock/it|Fissa](Sketcher_Workbench/it___Schizzo]].md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Il vincolo **Blocca** applica un vincolo <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:24px;"> [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md) e un vincolo <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:24px;"> [Distanza verticale](Sketcher_ConstrainDistanceY/it.md) ai vertici (punti) selezionati nello schizzo. Se viene selezionato un singolo vertice, i vincoli di distanza orizzontale e verticale si riferiscono al punto di origine dello schizzo. Se vengono selezionati due o più punti, verranno aggiunti i vincoli di distanza orizzontale e verticale per ogni coppia di punti. Non esiste un sistema automatico per modificare i valori dei vincoli, essi devono essere modificati manualmente.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare uno o più vertici (punti) nello schizzo.
2.  Premre il pulsante **[<img src=images/Sketcher_ConstrainLock.svg style="width:24px"> '''Blocca'''**.
3.  Per modificare i valori dei vincoli, fare doppio clic su un valore di vincolo nella vista 3D, oppure fare doppio clic sul vincolo stesso o fare clic con il tasto destro e selezionare **Modifica valore** nell\'elenco dei Vincoli nella scheda Azioni.


</div>

**Nota:** lo strumento Blocca può anche essere avviato senza una selezione precedente, ma funziona solo su un singolo vertice e definisce i vincoli con riferimento al punto di origine dello schizzo. Di default il comando è in modalità continua per creare nuovi vincoli; per uscire dal comando premere il tasto destro del mouse o una volta il tasto **ESC**.

## Scripting

The <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Lock](Sketcher_ConstrainLock.md) constraint is a GUI command which creates a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md) and a <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md) constraint, it is not a constraint of its own. See the [Sketcher scripting](Sketcher_scripting.md) page for details and examples on how to create these constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/it
