---
- GuiCommand:
   Name:FEM ConstraintDisplacement
   Name/de:FEM RandbedingungVersatz
   MenuLocation:Modell → Mechanische Randbedingungen → Randbedingung Versatz
   Workbenches:[FEM](FEM_Workbench/de.md)
   Shortcut:
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM ConstraintDisplacement/de



## Beschreibung

Erstellt eine FEM-Randbedingungn für einen festgelegten Versatz eines ausgewählten Objekts für einen bestimmten Freiheitsgrad.



## Anwendung

1.  Entweder die Schaltfläche **<img src="images/FEM_ConstraintDisplacement.svg" width=16px> '''Randbedingung Versatz'''** drücken oder den Menüeintrag **Modell → Mechanische Randbedingungen → <img src="images/FEM_ConstraintDisplacement.svg" width=16px> Randbedingung Versatz** auswählen.
2.  In der [3D-Ansicht](3D_view.md) as Objekt auswählen, dem die Randbedingung zugeordnet werden soll; dies kann ein Knoten (Ecke), eine Kante, oder eine Fläche sein.
3.  Die Schaltfläche **Hinzufügen** drücken.
4.  Das Deaktivieren von *Unspecified* aktiviert die erforderlichen Felder zum Bearbeiten.
5.  Die Werte anpassen oder ({{Version/de|0.21}}) eine Formel für die Versatzwerte festlegen.



## Formeln


{{Version/de|0.21}}



### Allgemein

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



### Drehungen

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



## Hinweise

For the <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [solver CalculiX](FEM_SolverCalculixCxxtools.md):

-   The constraint uses the \*BOUNDARY card.
-   Fixing a degree of freedom is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node164.html>
-   Prescribing a displacement for a degree of freedom is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node165.html>





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintDisplacement/de
