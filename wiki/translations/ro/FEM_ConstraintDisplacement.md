# FEM ConstraintDisplacement/ro
---
 GuiCommand:   Name: FEM ConstraintDisplacement   Name/ro: FEM ConstraintDisplacement   MenuLocation: Model , Mechanical Constraints , Constraint displacement   ---


</div>



## Descriere


<div class="mw-translate-fuzzy">

Creează o constrângere MEF pentru a o deplasare prescrisă a unui obiect selectat pentru un număr specificat de grade de libertate.


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Click pe <img alt="" src=images/FEM_ConstraintDisplacement.png  style="width:32px;"> sau alegeți **Model** → **Mechanical Constraints** → **<img src="images/FEM_ConstraintDisplacement.png" width=32px> Constraint displacement** din meniul de sus.
2.  Selectați în vizualizarea 3D obiectul la care trebuie aplicată constrângerea, care poate fi
    1.  vertices (corners)
    2.  edges
    3.  faces
3.  Alegeți un grad de libertate pentru a stabili sau a prescrie o deplasare la.


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

Elmer only uses the **Displacement \*** fields of the boundary condition. To define rotations, we need a formula.

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

1.  constrângerea utilizează tabelul \*BOUNDARY în CalculiX. Fixarea unui grad de libertate este explicată la <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node164.html> și se precizează o deplasare pentru un anumit grad de libertate <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node165.html>


</div>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintDisplacement/ro
