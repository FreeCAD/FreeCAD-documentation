---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintDisplacement
   Name/de: FEM RandbedingungVerschiebung
   MenuLocation: Modell , Mechanische Randbedingungen und Belastungen , Randbedingung Verschiebung
   Workbenches: FEM_Workbench/de
   Shortcut: 
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintDisplacement/de



## Beschreibung

Erstellt eine FEM-Randbedingungn für eine festgelegte Verschiebung (Auslenkung) eines ausgewählten Objekts für bestimmte Freiheitsgrade.



## Anwendung

1.  Die Schaltfläche **<img src="images/FEM_ConstraintDisplacement.svg" width=16px> '''Randbedingung Verschiebung'''** drücken oder den Menüeintrag **Modell → Mechanische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintDisplacement.svg" width=16px> Randbedingung Verschiebung** auswählen.
2.  Die Schaltfläche **Hinzufügen** drücken.
3.  In der [3D-Ansicht](3D_view/de.md) das Objekt auswählen, dem die Randbedingung zugeordnet werden soll; dies kann ein Knoten, eine Kante, oder eine Fläche sein (aber alle ausgewählten Objekte müssen von derselben Art sein). Um Elemente von der Liste zu entfernen wird die Schaltfläche **Entfernen** gedrückt und die Objekte angeklickt.
4.  Die Felder neben den Freiheitsgraden aktivieren, die man verwenden möchte. Standardmäßig sind sie auf Null gesetzt (fixed), können aber auf einen beliebigen Wert ({{Version/de|0.21}}: oder eine Formel für Elmer) geändert werden.



## Formeln


{{Version/de|0.21}}



### Allgemein

Für den <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) ist es möglich, die Verschiebung als Formel zu definieren. In diesem Fall berechnet der Solver die Verschiebung entsprechend der angegebenen Formelvariablen.

Nehmen wir zum Beispiel den Fall, dass wir eine [Transientenanalyse](FEM_SolverElmer_SolverSettings/de#Timestepping_(transient_analyses).md) durchführen wollen. Für jeden Zeitschritt soll die Verschiebung $d$ um 6 mm erhöht werden:

$\quad
d(t)=0.006\cdot t$

dies in das Feld *Formel* eingeben: ` Variable "time"; Real MATC "0.006*tx"`

Dieser Code hat die folgende Syntax:

-   das Präfix \"Variable\" gibt an, dass es sich bei der Verschiebung nicht um eine Konstante, sondern um eine Variable handelt.
-   die Variable ist die aktuelle Zeit.
-   die Verschiebungswerte werden als *Real* (Fließkomma) Werte zurückgegeben.
-   MATC ist ein Präfix der dem Elmer Solver angibt, dass der folgende Code eine Formel ist
-   *tx* ist immer der Name der Variablen in *MATC*-Formeln, unabhängig davon, dass *tx* in unserem Fall eigentlich *t* ist



### Drehungen

Elmer verwendet nur die Felder *Verschiebung \** der Randbedingung. Um Drehungen zu definieren, benötigen wir eine Formel.

Wenn zum Beispiel eine Fläche entsprechend dieser Bedingung gedreht werden soll:

$\quad
\begin{align}
d_{x}(t)= & \left(\cos(\phi)-1\right)x-\sin(\phi)y\\
d_{y}(t)= & \left(\cos(\phi)-1\right)y+\sin(\phi)x
\end{align}$

dann müssen wir für **Verschiebung x** ` Variable "Zeit, Koordinate"
Real MATC "(cos(tx(0)*pi)-1.0)*tx(1)-sin(tx(0)*pi)*tx(2)` eingeben

und für **Displacement y** `  Variable "time, Coordinate"
Real MATC "(cos(tx(0)*pi)-1.0)*tx(2)+sin(tx(0)*pi)*tx(1)`

Dieser Code hat die folgende Syntax:

-   wir haben 4 Variablen, die Zeit und alle möglichen Koordinaten (x, y z)
-   *tx* ist ein Vektor, *tx(0)* bezieht sich auf die erste Variable, die Zeit, während *tx(1)* sich auf die erste Koordinate *x* bezieht
-   *pi* bezeichnet $\pi$ und wurde hinzugefügt, damit nach $t=1\rm\, s$ eine Drehung um 180° durchgeführt wird



## Hinweise

Für den <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Löser CalculiX](FEM_SolverCalculixCxxtools/de.md):

-   Calkulix verwendet die \*BOUNDARY-Karte.
-   Die Fixierung eines Freiheitsgrades wird unter <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node164.html> erklärt.
-   Die Vorgabe einer Verschiebung für einen Freiheitsgrad wird erklärt unter <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node165.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintDisplacement/de
