---
- GuiCommand:
   Name: FEM ConstraintFlowVelocity
   Name/de: FEM ConstraintFlowVelocity
   MenuLocation: Model -> Fluid-Randbedingungen -> Constraint flow velocity
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_ConstraintInitialFlowVelocity/de
---

# FEM ConstraintFlowVelocity/de



## Beschreibung

Ordnet einer Kante in 2D oder einer Fläche in 3D eine Strömungsgeschwindigkeit als Grenzbedingung zu.



## Anwendung

1.  Either press the toolbar button **<img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> '''FEM ConstraintFlowVelocity'''** or select the menu **Model → Fluid Constraints → <img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> Constraint flow velocity**.
2.  Select the target Edges or Faces.
3.  Press the **Add** button.
4.  Uncheck *Unspecified* to activate the necessary fields for edition.
5.  Set the velocity values or (<small>(v0.21)</small> ) specify a formula.



## Formeln


{{Version/de|0.21}}

Es ist möglich eine Geschwindigkeit festzulegen, durch Angabe des Geschwindigkeitsprofils als Formel. In diesem Falle verwendet der Löser die Geschwindigkeiten an den unterschiedlichen Stellen dem Profil entsprechend.

Als Beispiel für die Festlegung des Geschwindigkeitsprofils

$\quad
v_{x} (y)=6\left(y-1\right)\left(2-y\right)$

für $y\in[1;2]$ (unter Annahme, dass z.B. eine Leitung die Wand bei y = 1 m und y = 2 m hat)

gibt man dies in das Feld *Formula* ein: ` Variable Coordinate 2; Real MATC "6*(tx-1)*(2-tx)"`

Dieser Code hat die folgende Syntax :

-   Das Präfix *Variable* legt fest, dass die Geschwindigkeit keine Konstante sondern eine Variable ist.
-   Die Variable für die Berechnung der Geschwindigkeit ist *Coordinate 2*, also y.
-   Die Geschwindigkeitswerte werden als *Real* (Fließkommazahl) zurückgegeben.
-   Das Präfix *MATC* zeigt dem Löser Elmer an, dass der folgende Code eine Formel ist.
-   *tx* ist immer der Name der Variable in *MATC*-Formeln, auch wenn in unserem Falle *tx* eigentlich *y* ist.

Dieses *y* gilt nur in dem Intervall $y\in[1;2]$, da *MATC* nur das *tx*-Intervall auswertet, in dem das Ergebnis positiv ist. Dieses Verhalten ist etwas ungewöhnlich, hat aber den Vorteil, dass man das Intervall nicht von Hand festlegen muss.

Es ist auch möglich, mehr als eine Variable zu verwenden. Siehe z.B. die Festlegung von Drehungen unter [Randbedingung Versatz](FEM_ConstraintDisplacement/de#Drehungen.md).



## Hinweise

-   Any vector component that should be the result of the solver must be set as *Unspecified*.
-   If the target face or edge is not aligned with the main Cartesian coordinate system, it is possible to set the option **Normal to boundary**.

    :   If **Normal to boundary** is checked, the normal vector to the selected edge or face is X and it will be oriented away from the mesh domain.
    :   For example, if a flow of 20 mm/s of air should enter the domain, then with **Normal to boundary** one must input -20 mm/s in the *Velocity x* field.

-   For a wall with non-slip condition, set all velocity components to 0.
-   For a symmetry condition, set the the flow to (0, Unspecified, Unspecified) if **Normal to boundary** is checked.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFlowVelocity/de
