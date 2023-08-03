---
 GuiCommand:
   Name: FEM_ConstraintDisplacement
   Name/it: Vincolo di dislocamento
   MenuLocation: Modello , Vincoli meccanici , Vincolo dislocamento
   Workbenches: FEM_Workbench/it
   Shortcut: 
   SeeAlso: FEM_tutorial/it
---

# FEM ConstraintDisplacement/it


</div>



## Descrizione

Crea un vincolo FEM per un determinato dislocamento di un oggetto selezionato per un dato grado di libertà.



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Cliccare su <img alt="" src=images/FEM_ConstraintDisplacement.png  style="width:32px;"> o scegliere **Modello** → **Vincoli meccanici** → **<img src="images/FEM_ConstraintDisplacement.png" width=32px> Vincolo dislocamento** dal menu principale.
2.  Selezionare nella vista 3D l\'oggetto a cui deve essere applicato il vincolo, che può essere
    1.  vertice (angolo)
    2.  bordo
    3.  faccia
3.  Scegliere un grado di libertà e prescrivere uno spostamento.


</div>

## Formulas


<small>(v0.21)</small> 

### General

For the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [solver Elmer](FEM_SolverElmer.md) it is possible to define the displacement as a formula. In this case the solver sets the displacement according to the given formula variable.

Take for example the case that we want to perform a [transient analysis](FEM_SolverElmer_SolverSettings#Timestepping_(transient_analyses).md). For every time step the displacement $d$ should be increased by 6 mm:

$\quad
d(t)=0.006\cdot t$

enter this in the *Formula* field: ` Variable "time"; Real MATC "0.006*tx"`

This code has the following syntax:

-   the prefix *Variable* specifies that the displacement is not a constant but a variable
-   the variable is the current time
-   the displacement values are returned as *Real* (floating point) values
-   *MATC* is a prefix for the Elmer solver indicating that the following code is a formula
-   *tx* is always the name of the variable in *MATC* formulas, no matter that *tx* in our case is actually *t*

### Rotations

Elmer only uses the **Displacement \*** fields of the constraint. To define rotations, we need a formula.

If for example a face should be rotated according to this condition:

$\quad
\begin{align}
d_{x}(t)= & \left(\cos(\phi)-1\right)x-\sin(\phi)y\\
d_{y}(t)= & \left(\cos(\phi)-1\right)y+\sin(\phi)x
\end{align}$

then we need to enter for **Displacement x** `  Variable "time, Coordinate"
Real MATC "(cos(tx(0)*pi)-1.0)*tx(1)-sin(tx(0)*pi)*tx(2)`

and for **Displacement y** `  Variable "time, Coordinate"
Real MATC "(cos(tx(0)*pi)-1.0)*tx(2)+sin(tx(0)*pi)*tx(1)`

This code has the following syntax:

-   we have 4 variables, the time and all possible coordinates (x, y z)
-   *tx* is a vector, *tx(0)* refers to the first variable, the time, while *tx(1)* refers to the first coordinate *x*
-   *pi* denotes $\pi$ and was added so that after $t=1\rm\, s$ a rotation of 180° is performed



## Note


<div class="mw-translate-fuzzy">

1.  Il vincolo utilizza \*BOUNDARY card in CalculiX. Come stabilire un grado di libertà è spiegato in <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node164.html> e prescrivere uno dislocamento per un grado di libertà è spiegato in <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node165.html>


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintDisplacement/it
