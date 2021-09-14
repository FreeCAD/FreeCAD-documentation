---
- GuiCommand:/it
   Name:FEM_ElementGeometry2D
   Name/it:FEM ElementGeometry2D
   MenuLocation:Model → Spessore di una lastra
   Workbenches:[FEM](FEM_Workbench/it.md)
   Shortcut:**C** **S**
   SeeAlso:[FEM tutorial](FEM_tutorial/it.md)
---


</div>

## Descrizione

Spessore di una lastra viene utilizzato per definire lo spessore degli elementi FEM 2D, tutti o posizionati sulla superficie scelta.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/FEM_ElementGeometry2D.png" width=32px> [Spessore di una lastra](FEM_ElementGeometry2D/it.md)**, o premere i tasti **C** e poi **S**.
2.  Definire un parametro di spessore.
3.  Opzionalmente, fare clic su `Aggiungi` nel pannello Azioni e poi fare clic sull\'icona. Se la selezione della faccia è libera, tutte le facce rimanenti (lo spessore non definito da altri oggetti [Spessore di una lastra](FEM_ElementGeometry2D/it.md)) vengono assegnate automaticamente.


</div>

## Limitazioni

-   L\'analisi combinata di elementi di shell con elementi solidi o bordi non è supportata nella versione corrente (FreeCAD 0.18).

## Proprietà


**Thickness**

: specifica lo spessore della shell.

## Script

## Note


<div class="mw-translate-fuzzy">

Per visualizzare i risultati dal risolutore CalculiX sulla mesh espansa allo spessore prescritto, la proprietà `Beam Shell Result Output 3D` in [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools/it.md) deve essere impostata su `True`.


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}  
