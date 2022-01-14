---
- GuiCommand:/it
   Name:Constraint InternalAlignment
   Name/it:Allineamento interno
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   MenuLocation:Sketch → Vincoli → Allineamento interno
   Shortcut:**Ctrl** + **A**
   SeeAlso:[Mostra/Nascondi la geometria interna](Sketcher_RestoreInternalAlignmentGeometry/it.md), [Ellisse](Sketcher_CreateEllipseByCenter/it.md)
   Version:0.15
---

# Sketcher ConstrainInternalAlignment/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo vincolo allinea le linee ed i punti di un elemento Sketcher complesso in particolari posizioni (per ora, l\'unico elemento complesso è [Ellisse](Sketcher_CreateEllipseByCenter/it.md)).


</div>


<div class="mw-translate-fuzzy">

Per [Ellisse](Sketcher_CreateEllipseByCenter/it.md) e per il suo [Arco](Sketcher_CreateArcOfEllipse/it.md), permette di vincolare delle linee e di farle diventare il diametro maggiore e il diametro minore, e di vincolare dei [punti](Sketcher_CreatePoint/it.md) nella posizione dei fuochi dell\'ellisse.


</div>


<div class="mw-translate-fuzzy">

Per essere utilizzato, questo vincolo richiede più impegno di quanto ne richiedano gli altri vincoli. Di default, questo strumento non è mostrato nella barra degli Strumenti dei vincoli, ma si trova nel menu *Sketch/Part Design → Vincoli dello Sketcher → Vincolo Allineamento interno*. Nella barra degli strumenti *Sketcher tools* (Strumenti di Sketcher) c\'è uno strumento di supporto chiamato [Mostra/Nascondi la geometria interna](Sketcher_RestoreInternalAlignmentGeometry/it.md) che serve per rimuovere o ricostruire completamente i vincoli, secondo le proprie esegenze.


</div>

## Operation on Ellipse 


<div class="mw-translate-fuzzy">

## Operazioni su Ellisse 

1.  Selezionare gli elementi da allineare e un\'ellisse. L\'ellisse deve essere selezionato per ultimo. Sono accettate fino a due linee e fino a due punti.
2.  Richiamare il vincolo in uno di questi modi:
    -   Cliccare sull\'icona **<img src="images/Constraint_InternalAlignment.svg" width=16px>** della barra degli strumenti.
    -   Usare la scorciatoia da tastiera **Ctrl** + **A**.
    -   Usare la voce **Sketch → Vincoli → Allineamento interno** dal menu principale.


</div>

La prima linea selezionata viene allineata per diventare il diametro maggiore dell\'ellisse, se il diametro maggiore non è già occupato da un\'altra linea, altrimenti diventa il suo diametro minore. La seconda linea viene allineata per diventare il raggio minore. Le linee sono automaticamente commutate in [linee di costruzione](Sketcher_ToggleConstruction/it.md).

Analogamente, il primo punto viene vincolato per diventare il primo fuoco non occupato, e il secondo punto viene assegnato all\'altro fuoco.

**Note:** By default new ellipses have an internal construction geometry. When this defines the ellipse already completely, you cannot directly use the InternalAlignment constraint. You first need to delete the construction geometry or parts of it. In case you don\'t see the construction geometry, select the ellipse and use the tool **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Show/Hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md)** to make it visible.

## Script


```python
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseMajorDiameter', index_of_line, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseMinorDiameter', index_of_line, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseFocus1', index_of_point, 1, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseFocus2', index_of_point, 1, index_of_ellipse))
```


<div class="mw-translate-fuzzy">

Notare:

:   Sketch è un oggetto schizzo.
:   Il numero 1 nei fuochi richiama i punti iniziali di un elemento punto, quindi è ignorato.


</div>

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `index_of_line`, `index_of_point` and `index_of_ellipse` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainInternalAlignment/it
