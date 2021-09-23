---
- GuiCommand:/it
   Icon:Constraint Vertical.svg
   Name:Vertical constraint
   Name/it:Vincolo verticale
   Workbenches:[Schizzo](Sketcher_Workbench/it.md)
   Shortcut:**V**
   MenuLocation:Sketch → Vincoli → Verticale
   SeeAlso:[Orizzontale](Sketcher_ConstrainHorizontal/it.md)
---

# Sketcher ConstrainVertical/it


</div>

## Descrizione

Crea un vincolo verticale per le linee o le polilinee selezionate.

Può anche vincolare verticalmente i vertici. Si possono selezionare più oggetti {{VersionPlus/it|0.17}} .

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare le linee o i vertici da vincolare verticalmente.
2.  Richiamare il comando in uno di questi modi:
    -   Cliccare sull\'icona **<img src=images/Constraint_Vertical.svg style="width:24px">** **Vincolo verticale** della barra degli strumenti.
    -   Usare la scorciatoia da tastiera **V**.
    -   Usare la voce **Sketch → Vincoli → Verticale** dal menu principale.
3.  In alternativa, lo strumento può essere avviato senza previa selezione e quindi attende una selezione; ma in questo caso sono selezionabili solo le linee.
4.  Fare clic con il tasto destro del mouse o premere **Esc** una volta per uscire dallo strumento.


</div>

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Vertical', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainVertical/it
