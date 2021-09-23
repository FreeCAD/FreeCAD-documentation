---
- GuiCommand:/it
   Name:Sketcher_ConstrainBlock
   Name/it:Fissa
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   MenuLocation:Sketch → Vincoli → Fissa
   SeeAlso:[Blocca](Sketcher_ConstrainLock/it.md)
   Version:0.17
---

# Sketcher ConstrainBlock/it


</div>

## Descrizione

Il vincolo **Fissa** blocca un elemento geometrico in posizione con un singolo vincolo.

Il suo scopo principale è quello di lavorare con le <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:16px;"> [B-Splines](Sketcher_CreateBSpline/it.md) che altrimenti possono essere difficili da vincolare completamente.

## Utilizzo

1.  Selezionare un elemento da vincolare.
2.  Premere il pulsante **<img src=images/Sketcher_ConstrainBlock.svg style="width:16px"> Fissa**.

Oppure premere prima il pulsante, quindi selezionare gli elementi.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/it
